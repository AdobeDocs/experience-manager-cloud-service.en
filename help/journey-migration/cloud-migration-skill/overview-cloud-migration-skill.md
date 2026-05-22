---
title: AI-Assisted Code Migration to AEM as a Cloud Service
description: Overview of the AEM Cloud Migration Skill and MCP, an AI agent solution that reads BPA findings and migrates AEM 6.x code to AEM as a Cloud Service, pattern by pattern.
exl-id: a3b2c4e5-d6f7-8901-b2c3-d4e5f6a7b890
feature: Migration
role: Developer
---

# AI-Assisted Code Migration to AEM as a Cloud Service {#cloud-migration-skill-overview}

The **AEM Cloud Migration** solution is an agent-based toolset that guides developers through migrating AEM 6.x, AMS, or on-premise Java code and OSGi configurations to **AEM as a Cloud Service (AEMaaCS)**. It works inside any AI-enabled IDE that supports agent skills and the Model Context Protocol (MCP).

The solution consists of two components:

| Component | Role |
|-----------|------|
| **Migration Skill** | Orchestrates the migration workflow, it sources Best Practices Analyzer (BPA) findings, identifies affected files in your project, and applies code transformations pattern by pattern. Works with a local BPA CSV export or with the Cloud Migration MCP (recommended). |
| **Cloud Migration MCP** | Connects your IDE agent to Cloud Acceleration Manager (CAM), enabling it to fetch BPA findings directly without a CSV export. Recommended over a local CSV for the most up-to-date findings. |

## Prerequisites {#prerequisites}

- An AEM project (Maven or Gradle) open in your IDE
- One of the following BPA finding sources (strongly recommended, not required for manual flows):
  - A **BPA CSV export** from your AEM instance
  - A **Cloud Acceleration Manager project** with an uploaded BPA report and the Cloud Migration MCP configured

## The Migration Skill {#migration-skill}

The migration skill is an agent skill for AI-enabled IDEs. It orchestrates a **one-pattern-per-session** workflow: you name the pattern to fix, point the agent at your BPA findings, and the agent reads the relevant transformation rules, locates the affected files in your project, and applies the changes in batches of five, pausing for your review after each batch.

### Supported Patterns {#supported-patterns}

| Pattern | What it fixes |
|---------|--------------|
| `scheduler` | `sling.commons.scheduler`-based jobs incompatible with AEMaaCS's stateless runtime |
| `resourceChangeListener` | `ResourceChangeListener` implementations requiring Cloud Service updates |
| `replication` | Legacy `Replicator` API calls replaced by `ContentDistribution` equivalents |
| `eventListener` | OSGi `EventListener` implementations updated for AEMaaCS event semantics |
| `eventHandler` | Synchronous OSGi `EventHandler` services adapted for Cloud Service |
| `assetApi` | Deprecated `AssetManager` and DAM API calls replaced with supported equivalents |
| `htlLint` | `data-sly-test` redundant constant comparison warnings in HTL templates |
| OSGi configs | `.cfg.json` conversion, runmode scoping, and Cloud Manager secrets/env-var extraction |

The skill delegates all code transformation steps to the companion `best-practices` skill. Both are distributed together as the `aem-cloud-service` skill package; install the package once to get both.

### Getting Started {#getting-started-skill}

1. Install the `aem-cloud-service` skill package from the [Adobe Skills repository](https://github.com/adobe/skills).
2. Open your AEM project as the workspace root in your IDE.
3. Obtain BPA findings: export a CSV from BPA or configure the Cloud Migration MCP (see below).
4. Start a session with your agent using one of these prompts:

   **BPA CSV:**

   ```
   Use the migration skill: scheduler only, BPA CSV at ./reports/bpa.csv
   ```

   **CAM via MCP:**

   ```
   Fix replictaion findings from project <projectname>/<projectId>.
   ```

   **Manual (no BPA):**

   ```
   Migrate event listener in core/src/main/java/com/example/Listener.java
   ```

   **OSGi configs:**

   ```
   Scan my config files and create Cloud Manager environment secrets or variables.
   ```

   **HTL lint:**

   ```
   Fix htlLint in ui.apps - scan for data-sly-test redundant constant warnings.
   ```

>[!NOTE]
>The skill processes one pattern per session. If your BPA report contains multiple patterns, the agent asks you to pick one before starting.

For full pattern reference and session management guidance, see [Using the Cloud Migration Skill](/help/journey-migration/cloud-migration-skill/using-cloud-migration-skill.md).

## The Cloud Migration MCP {#cloud-migration-mcp}

The **AEM Cloud Migration MCP** is a [Model Context Protocol](https://modelcontextprotocol.io) server that connects your IDE agent to Cloud Acceleration Manager. When configured, the migration skill can fetch BPA findings directly from your CAM project without requiring a CSV download.

### What the MCP Provides {#mcp-tools}

| Tool | Description |
|------|-------------|
| `fetch-cam-bpa-findings-by-pattern` | Returns BPA findings for a specific code migration pattern from the latest BPA report in a CAM project. |
| `fetch-cam-bpa-findings-by-importance` | Returns all BPA findings at a given severity (`CRITICAL`, `MAJOR`, `ADVISORY`, `INFO`), sorted by count. Useful for prioritizing which patterns to work on first. |

These tools are invoked automatically by the migration skill; you do not call them directly.

### Getting Started {#getting-started-mcp}

1. In your IDE's MCP configuration, add the Cloud Migration MCP server URL: `https://mcp.adobeaemcloud.com/adobe/mcp/cloud-migration`
2. When prompted, sign in with your Adobe ID to authenticate against Cloud Acceleration Manager.
3. The migration skill can now fetch BPA findings directly from your CAM projects.

For detailed setup and troubleshooting, see [Using the Cloud Migration MCP](/help/journey-migration/cloud-migration-skill/using-cloud-migration-mcp.md).

## How They Fit Into the Migration Journey {#migration-journey}

The skill and MCP complement the other tools in the **Implementation Phase**:

- **Best Practices Analyzer**: produces the findings that drive the skill. See [Using Best Practices Analyzer](/help/journey-migration/best-practices-analyzer/using-best-practices-analyzer.md).
- **Cloud Acceleration Manager**: hosts BPA reports and tracks overall migration progress. See [Getting Started with CAM](/help/journey-migration/cloud-acceleration-manager/using-cam/getting-started-cam.md).
- **Refactoring Tools**: handles repository structure and dispatcher configuration modernization. See [Refactoring Tools Overview](/help/journey-migration/refactoring-tools/overview-refactoring-tools.md).
- **Content Transfer Tool**: migrates repository content from AEM 6.x to AEMaaCS.

See the [Implementation Phase overview](/help/journey-migration/implementation.md) for the full picture.
