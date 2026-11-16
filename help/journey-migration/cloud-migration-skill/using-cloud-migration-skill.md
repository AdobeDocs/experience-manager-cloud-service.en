---
title: Using the AEM Cloud Migration Skill
description: Reference for each migration pattern supported by the AEM Cloud Migration Skill, including OSGi config conversion, BPA source options, and session management guidance.
feature: Migration
role: Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: 5be0fc8f-1cff-5c3e-bb92-2903a56a3de6
    internal-label: Migration
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
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

### InputStream Usage {#input-stream}

Targets Java code that BPA flags for `java.io.InputStream` usage (subtype `java.io.inputstream`). On AEM as a Cloud Service, streaming large binaries through the JVM can exhaust container memory, so binaries should be uploaded and delivered directly through the cloud blob store and CDN (see [Development Guidelines](/help/implementing/developing/introduction/development-guidelines.md) and [direct binary upload](/help/assets/asset-microservices-overview.md#asset-upload-with-direct-binary-access)).

**BPA pattern id:** `inputStream`

The agent groups findings by risk and handles each group differently:

| Finding | Agent action |
|---------|--------------|
| Stream or JCR `Binary` not closed | Fixed automatically with try-with-resources |
| Whole stream read into memory | Bounded read or streaming, when a safe limit is clear; otherwise asks you |
| Local filesystem, binaries streamed through the JVM, or Java deserialization | Proposes a fix and waits for your decision |
| Benign usage | No change |

Start a session with:

```
Fix inputStream findings using BPA CSV at ./reports/bpa.csv
```

>[!NOTE]
>`inputStream` relies on BPA as the source of truth. When no BPA or CAM source is available, the agent falls back to scanning your Java files. Findings in code that is not in your workspace, such as product or third-party bundles, are reported for information only.

### HTL Lint (data-sly-test) {#htl-lint}

Targets HTL templates under `ui.apps` that produce `data-sly-test: redundant constant value comparison` lint warnings. The agent discovers affected templates by scanning the content package directly; this pattern does not require a BPA CSV or CAM connection.

**BPA pattern id:** `htlLint`

>[!NOTE]
>`htlLint` findings do not appear in BPA CSV exports. The agent discovers them through direct file scanning when you start a session for this pattern.

### OSGi Configs to Cloud Manager {#osgi-cloud-manager}

Converts OSGi configurations in `ui.config` to Cloud Manager–compatible `.cfg.json` format with full environment-specific handling. This covers several related tasks:

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

**Unsupported run modes (URC)**

AEM as a Cloud Service supports a fixed set of run mode identifiers. Configuration folders that use an unsupported run mode have no effect once deployed. The agent flags these Unsupported Run mode Configurations (URC), including:

* Unknown run mode tokens, for example `config.qa` or `install.local`
* A tier token that follows instead of precedes the environment token—`config.dev.author` instead of the valid `config.author.dev`
* Non-lowercase tokens, such as `config.Author.dev`, and the reserved `config.preview` (preview inherits from publish)

URC findings come from the Best Practices Analyzer first (subtype `unsupported.runmode`, severity `CRITICAL`); when no BPA source reports them, the agent scans `config.*` and `install.*` folders locally as a safety net. For each finding it reports the folder path, the offending run mode, and the remediation—evaluate whether the configuration is still needed, rename it to a supported run mode, or remove it if obsolete. For ordering-only violations, where every token is valid but out of order, the agent can apply a safe reorder automatically (for example, renaming `config.dev.author` to `config.author.dev`); unknown tokens and other ambiguous cases are flagged for you to resolve.

**Config format conversion and secret externalization do not require a BPA CSV or CAM, and URC detection uses BPA findings when available.** Start a session with:

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

### Dispatcher Conversion {#dispatcher-conversion}

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

### Oak Index Migration {#oak-index}

>[!NOTE]
>Oak index migration is in beta. Review the converted index definitions carefully before deploying them to production.

Converts legacy Oak index definitions under `ui.apps/.../_oak_index/` to AEM as a Cloud Service–compatible definitions. This capability wraps Adobe's maintained [Index Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/index-converter) tool rather than re-implementing its conversion rules. It covers custom Lucene indexes and out-of-the-box indexes that were modified in place.

**BPA pattern id:** `oakIndex` (subtypes `index.rule.violation` and `standard.index.modification`)

The agent runs the converter, shows you a diff with a datatype compatibility check, applies the changes only after you confirm, and then builds `ui.apps` and runs the AEM analyser.

AEM as a Cloud Service requires custom indexes to carry a `-custom-<n>` version suffix, where `<n>` increases each time the definition changes (see [Index Names](/help/operations/indexing.md#index-names)). The agent picks the next free `<n>`, so a repeat migration does not overwrite an existing index:

* **Modified out-of-the-box index:** `<indexName>-<version>-custom-<n>` (for example, `damAssetLucene-8-custom-1`)
* **New custom index:** `<originalName>-custom-<n>`
* **Already compliant index:** left unchanged

The pattern currently produces the classic `_oak_index` format. [Simplified Index Management](/help/operations/indexing.md) as a target format is planned but not yet supported.

Start a session with:

```
Fix oakIndex findings using BPA CSV at ./reports/bpa.csv
```

>[!NOTE]
>`oakIndex` relies on BPA as the source of truth. Indexes outside `_oak_index` and `nt:base` Lucene indexes are out of scope, and the agent does not update queries that depend on renamed indexes. See also [Content Search and Indexing](/help/operations/indexing.md).

### Validate a Migration {#validate-migration}

>[!NOTE]
>Migration validation is in beta. Treat a pass as a strong signal, not a guarantee, and review the validation report before you raise a pull request or deploy to a Cloud Service environment.

After a pattern is migrated, the agent can verify the result on your local AEM as a Cloud Service SDK. Validation is read-only for your code: the agent never edits your source to obtain a pass. If a check fails, the fix goes back to the migration pattern that owns the code.

Validation supports these patterns:

| Pattern | What is checked | Needs a local SDK |
|---------|-----------------|-------------------|
| `scheduler`, `assetApi`, `eventListener`, `eventHandler`, `resourceChangeListener`, `replication` | The built OSGi service contract, and bundle and component state after deployment | Yes |
| `lui`, `cdw` | The migrated dialogs in the built package | No |
| Template modernization | Component mapping, SDK health, and a side-by-side page comparison with your AEM 6.5 instance | Yes |

Other patterns, such as Dispatcher conversion and OSGi configs, are not covered by validation.

For the patterns that need it, start the Cloud SDK (by default on `http://localhost:4602`) and add its [AEM Quickstart MCP server](/help/ai-in-aem/local-development-with-ai-tools.md#aem-quickstart-mcp-server) to your IDE. The agent then:

1. **Checks setup** - Confirms the required tools, instances, and MCP server are available, and asks you to start anything that is missing.
2. **Prepares** - Builds the project and deploys the changed bundles through your project's Maven install profile.
3. **Diagnoses** - Reads bundle and component state from the AEM Quickstart MCP. Offline patterns (`lui`, `cdw`) skip this step.
4. **Verifies** - Writes a validation report to `.validate-migration/` in your project.

If your project is linked to a Cloud Acceleration Manager project (for example, through the migration runbook), the agent also records the validation outcome in CAM through the AEM MCP Server's Cloud Migration capabilities.

Start a session with:

```
Validate my scheduler migration on the local Cloud SDK.
```

>[!NOTE]
>Validation proves the migration contract and deployment health, not your business logic. The build skips unit tests, so run your own tests separately. Before deployment, the agent checks your configuration for side effects, such as connections to production systems, because installing a bundle can start schedulers or listeners.

## BPA Source Options {#bpa-source}

| Source | When to use |
|--------|------------|
| **BPA CSV file** | You have exported a CSV from your AEM instance or Cloud Acceleration Manager. Provide the file path when starting the session. |
| **CAM via MCP** | You have the AEM MCP Server configured. The agent lists your CAM projects, you confirm which one to use, and findings are fetched directly. See [Using AEM MCP Server Cloud Migration Capabilities](/help/journey-migration/cloud-migration-skill/using-cloud-migration-mcp.md). |
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
