---
title: Using the AEM Cloud Migration Skill
description: Reference for each migration pattern supported by the AEM Cloud Migration Skill, including OSGi config conversion, BPA source options, and session management guidance.
feature: Migration
role: Developer
---

# Using the AEM Cloud Migration Skill {#using-cloud-migration-skill}

This reference covers each supported migration pattern, how to provide BPA findings, and how to manage sessions across a large project. For an introduction and setup instructions, see the [overview](/help/journey-migration/cloud-migration-skill/overview-cloud-migration-skill.md).

## How a Session Works {#workflow-overview}

Every migration session follows this sequence:

1. **Name the pattern**: specify one pattern (for example, `scheduler`)
2. **Provide findings**: from a BPA CSV file, CAM via MCP, or specific file paths
3. **Agent reads transformation rules**: the skill reads the relevant best-practices module before making any code changes
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
