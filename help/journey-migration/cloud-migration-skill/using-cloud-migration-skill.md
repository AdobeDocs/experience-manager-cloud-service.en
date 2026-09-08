---
title: Using the AEM Cloud Migration Skill
description: Reference for each migration pattern supported by the AEM Cloud Migration Skill, including OSGi config conversion, BPA source options, and session management guidance.
feature: Migration
role: Developer
---

# Using the AEM Cloud Migration Skill {#using-cloud-migration-skill}

This reference covers each supported migration pattern, how to provide BPA findings, and how to manage sessions across a large project. For an introduction and setup instructions, see the [overview](/help/journey-migration/cloud-migration-skill/overview-cloud-migration-skill.md).

## Generate a Migration Runbook {#migration-runbook}

For a whole-project assessment, start with a runbook instead of naming a single pattern. Prompt the agent with:

```
Review my code for AEMaaCS migration
```

The skill generates a **read-only `migration-runbook.md`** at your project root without changing any code. The runbook covers **every** pattern the migration skill can address and, for each one, records:

* The detection strategy used (BPA/CAM findings, analyzer, or heuristic content scan)
* The affected files and a per-pattern finding count
* A copy-paste prompt to start that pattern's migration session

Because the runbook also writes a findings cache alongside the markdown, a later pattern session reuses the findings already discovered — the agent does not re-scan. Use the runbook to prioritize which patterns to tackle first, then start pattern sessions as described below.

>[!NOTE]
>The runbook is read-only. It never edits code, and heuristic (non-BPA) findings are candidate matches to confirm rather than authoritative counts.

## How a Session Works {#workflow-overview}

Every migration session follows this sequence:

1. **Name the pattern**: specify one pattern (for example, `scheduler`)
2. **Provide findings**: from a BPA CSV file, CAM via MCP, or specific file paths
3. **Agent reads transformation rules**: the skill reads the relevant transformation rules from the companion `code-assessment` skill before making any code changes
4. **First batch of five**: the agent transforms up to five findings and reports what it changed
5. **You review and continue**: after reviewing each batch, reply `continue` to proceed to the next

The agent processes one pattern and one batch at a time. It does not proceed automatically; each batch requires your confirmation.

## Migration Patterns {#patterns}

### Scheduler {#scheduler}

Targets Java classes using `sling.commons.scheduler` or `Scheduler` injection that are incompatible with AEMaaCS's stateless, containerized runtime.

**BPA pattern id:** `scheduler`

The agent converts `Scheduler`-injected jobs to `@Component` implementations of `Runnable` using `@Designate`, replacing constructor-based scheduler registration with `@Activate` / `@Deactivate` lifecycle methods.

### ResourceChangeListener {#resource-change-listener}

Targets `ResourceChangeListener` or `ResourceChange` listener implementations that require updates for AEMaaCS.

**BPA pattern id:** `resourceChangeListener`

### Replication {#replication}

Targets classes importing `com.day.cq.replication.Replicator` or related replication APIs, which are not supported in AEMaaCS. The agent replaces them with `ContentDistribution`-based equivalents and updates the corresponding OSGi service references.

**BPA pattern id:** `replication`

### Event Listener {#event-listener}

Targets OSGi `EventListener` or `EventHandler` implementations that must be updated for AEMaaCS event processing semantics.

**BPA pattern id:** `eventListener`

### Event Handler {#event-handler}

Targets synchronous OSGi `EventHandler` services that need to be adapted for AEMaaCS.

**BPA pattern id:** `eventHandler`

### Asset API {#asset-api}

Targets classes using deprecated `AssetManager`, `DAMEvent`, or unsupported DAM APIs. The agent replaces them with the supported AEM Assets API equivalents.

**BPA pattern id:** `assetApi`

### Guava Cache to Caffeine {#guava-cache}

Targets bundles that use Guava's cache (`com.google.common.cache.*`, such as `Cache`, `CacheBuilder`, and `LoadingCache`). On AEM as a Cloud Service the supported in-process cache library is [Caffeine](https://github.com/ben-manes/caffeine), so the agent swaps the Maven dependency, updates imports, and adjusts the affected call sites. Because Caffeine was written by the same author and its API is intentionally near-identical, the change is mostly mechanical.

**BPA pattern id:** `guavaCache`

BPA reports this pattern at **bundle** granularity (subtype `custom.guava.cache`), so the agent resolves the bundle to the Java files that actually import the Guava cache and edits those. This pattern is provided by the migration skill only—not `code-assessment`—because Guava cache usage occurs only in code carried over from legacy AEM, never in native Cloud Service code.

>[!NOTE]
>`guavaCache` relies on BPA as the source of truth. When no BPA or CAM source is available, the agent falls back to scanning your Java files for `import com.google.common.cache` imports as unconfirmed candidates.

### HTL Lint (data-sly-test) {#htl-lint}

Targets HTL templates under `ui.apps` that produce `data-sly-test: redundant constant value comparison` lint warnings. The agent discovers affected templates by scanning the content package directly; this pattern does not require a BPA CSV or CAM connection.

**BPA pattern id:** `htlLint`

>[!NOTE]
>`htlLint` findings do not appear in BPA CSV exports. The agent discovers them through direct file scanning when you start a session for this pattern.

### OSGi Configs to Cloud Manager {#osgi-cloud-manager}

Converts OSGi configurations in `ui.config` to Cloud Manager–compatible `.cfg.json` format with full environment-specific handling. This covers two related tasks:

**Config format conversion**

AEMaaCS requires OSGi configurations to be stored as `.cfg.json` files, with environment-specific configs in runmode-scoped folders (`config.author/`, `config.publish/`, `config.dev/`, and so on). The agent:

* Converts existing `.config`, `.cfg`, and XML-format OSGi configs to `.cfg.json`
* Splits configs containing both author- and publish-specific values into separate runmode-scoped files
* Validates property types against the OSGi metatype specification (strings, integers, booleans, arrays)
* Flags Adobe-owned PIDs for manual review rather than auto-converting them

**Secrets and environment variables**

Moves plaintext secrets and environment-specific values out of committed config files and replaces them with Cloud Manager placeholders:

* `$[secret:NAME]`: for passwords, tokens, and other sensitive values
* `$[env:NAME]`: for non-sensitive values that differ per environment (for example, service URLs)

The corresponding variables and secrets are applied in Cloud Manager and injected at runtime; no values are stored in source control.

>[!IMPORTANT]
>The agent never outputs secret values in the conversation. All sensitive data is written to a gitignored handoff file for you to apply via the Cloud Manager API or UI.

**This pattern does not use BPA CSV or CAM.** Start a session with:

```
Scan my config files and create Cloud Manager environment secrets or variables.
```

### Dialog Migration (Legacy UI) {#dialog-migration}

Converts Classic UI dialogs to Touch UI. The agent handles two dialog sub-types: ExtJS / Classic UI `cq:Dialog` definitions are rebuilt as Coral 3 `_cq_dialog` structures, and existing Coral 2 dialogs are upgraded in place to Coral 3. It also carries over listeners, `optionsProvider`, `namePrefix`, and updates `filter.xml`.

**BPA pattern id:** `lui` (dialog sub-types only)

When both dialog and custom widget findings exist for the same components, run custom widget migration first so all `xtype` references resolve before the dialogs are converted.

```
Convert my Classic UI dialogs to Touch UI Coral 3.
```

### Custom Design Widgets (Legacy UI) {#custom-design-widgets}

Migrates custom ExtJS widgets (`cq:Widget` definitions with custom `xtype` values). The agent inventories the widgets, then either maps each `xtype` to a known Coral 3 equivalent or scaffolds a Granite UI form component when no direct mapping exists.

**BPA pattern id:** `cdw`

```
Migrate my custom ExtJS widgets (CDW findings) from CAM.
```

### Template Modernization {#template-modernization}

Converts static templates to editable templates and generates the corresponding [AEM Modernize Tools](/help/journey-migration/refactoring-tools/aem-modernization-tools.md) rewrite rules (structure, component, and policy rules). The agent runs in three phases: it discovers the templates and produces a per-template plan, executes the plan template by template, and validates the generated `/conf` structures.

During discovery, the agent walks the templates under `apps/<appId>/templates/` at any depth—including nested or grouped template folders—and classifies each static template as legacy or custom based on its page-component resource type. This classification holds even without a BPA report, so custom templates are handled distinctly from legacy ones.

**This pattern does not use a BPA pattern id.** Start a session with:

```
Migrate my static templates to editable templates and generate the Modernize Tools rewrite rules.
```

### Dispatcher Conversion (Beta) {#dispatcher-conversion}

>[!IMPORTANT]
>Dispatcher configuration conversion is in **beta** and under active development. Review its output carefully before applying it to production Dispatcher configurations.

Converts an AMS or on-premise Apache HTTPD and Dispatcher configuration to the AEM as a Cloud Service structure. This capability wraps Adobe's maintained [Dispatcher Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/dispatcher-converter) tool, adding detection, configuration generation, output verification, and validation around it.

The agent works through a phased flow:

1. **Detect and inventory** - Determines the configuration *mode* and records a baseline count of filter, rewrite, and cache rules. Recognized modes are `standard` (AMS), `flexible` (monolithic on-premise), `v1` (older layouts), `already-cloud`, `not-dispatcher`, and `unknown`. For `already-cloud`, `not-dispatcher`, or `unknown`, the agent stops and asks you to confirm before proceeding.
2. **Plan and generate config** - Builds the converter configuration and confirms the plan with you.
3. **Convert** - Runs Adobe's Dispatcher converter (installed automatically on first use).
4. **Verify** - Checks the output against the baseline. An emptied filter set (`filter-acl-loss`) is a hard stop that must be resolved before continuing.
5. **Cross-boundary handoff** - Routes Cloud Manager environment variables to the OSGi configs flow and flags CDN or security-header candidates.
6. **Validate** - Runs the Cloud Service Dispatcher validator and produces a consolidated conversion report.

**Runbook pattern id:** `dispatcherConversion` (detected heuristically from the configuration layout). This pattern does not use BPA or CAM. Start a session with:

```
Convert my AMS / on-prem Dispatcher config to AEM as a Cloud Service.
```

>[!NOTE]
>Run this against a clean working tree so the converted output is easy to review and roll back. The degree of automation depends on the detected mode—`standard` (AMS) configurations are near-automated, while `flexible` and `v1` layouts need more review.

## BPA Source Options {#bpa-source}

| Source | When to use |
|--------|------------|
| **BPA CSV file** | You have exported a CSV from your AEM instance or Cloud Acceleration Manager. Provide the file path when starting the session. |
| **CAM via MCP** | You have the AEM Cloud Migration MCP configured. The agent lists your CAM projects, you confirm which one to use, and findings are fetched directly. See [Using the Cloud Migration MCP](/help/journey-migration/cloud-migration-skill/using-cloud-migration-mcp.md). |
| **Manual file paths** | You want to migrate specific files without a BPA report. Provide the paths directly in your prompt. |

### MCP Error Handling {#mcp-errors}

If the MCP connection returns an error (including project-not-found or authentication failures), the agent stops and shows you the error. It does not automatically switch to another source. From the stopped state, you can:

* Confirm the correct project from the list the agent displayed
* Supply a BPA CSV path as an alternative
* Provide specific Java file paths for a manual migration

## Managing Sessions Across Large Reports {#large-reports}

For BPA reports with many findings, the batch-by-batch approach lets you validate incrementally:

1. Review the diff for each batch 
2. Commit the batch with a pattern-scoped commit message
3. Reply `continue` to start the next batch
4. Repeat until the agent reports that all findings for the pattern are done

**One pattern per commit** keeps your git history readable and makes individual pattern transformations easy to revert if needed.

>[!NOTE]
>If you end a session before all findings are processed, restart with the same pattern and BPA source in a new session. The agent resumes from where it left off.

## Workspace Scope {#workspace-scope}

The agent searches for and edits files only within the open IDE workspace folders. It does not scan parent directories, sibling folders, or other locations on disk.

If a BPA finding references a file path that does not exist in the workspace, the agent stops and tells you which paths are missing. Open the correct project folder or provide the paths explicitly to continue.

