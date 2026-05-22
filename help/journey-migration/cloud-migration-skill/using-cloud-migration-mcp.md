---
title: Using the AEM Cloud Migration MCP
description: Learn how to add the AEM Cloud Migration MCP server to your AI-enabled IDE and use it to fetch Best Practices Analyzer findings from Cloud Acceleration Manager during a migration session.
exl-id: d5e6f7a8-b9c0-1234-e5f6-a7b8c9d0e123
feature: Migration
role: Developer
---

# Using the AEM Cloud Migration MCP {#using-cloud-migration-mcp}

The **AEM Cloud Migration MCP** is a hosted [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that connects your IDE agent to **Cloud Acceleration Manager (CAM)**. Once configured, the [AEM Cloud Migration Skill](/help/journey-migration/cloud-migration-skill/overview-cloud-migration-skill.md) can fetch Best Practices Analyzer findings directly from your CAM project — no CSV export required.

## MCP Server URL {#server-url}

```
https://mcp.adobeaemcloud.com/adobe/mcp/cloud-migration
```

Add this URL to your IDE's MCP configuration to connect.

## What It Provides {#what-it-provides}

The MCP server exposes two tools that the migration skill invokes automatically during a session:

| Tool | Description |
|------|-------------|
| `fetch-cam-bpa-findings-by-pattern` | Returns BPA findings for a specific migration pattern (`scheduler`, `assetApi`, `eventListener`, `resourceChangeListener`, `eventHandler`, or `all`) from the latest BPA report in a CAM project. |
| `fetch-cam-bpa-findings-by-importance` | Returns all BPA findings at a given severity (`CRITICAL`, `MAJOR`, `ADVISORY`, `INFO`) from the latest BPA report, sorted by descending count. Useful for prioritizing which patterns to address first. |

## Prerequisites {#prerequisites}

* A **Cloud Acceleration Manager** project with an uploaded BPA report. See [CAM Readiness Phase](/help/journey-migration/cloud-acceleration-manager/using-cam/cam-readiness-phase.md).
* An **Adobe ID** with access to that CAM project.
* An AI-enabled IDE that supports remote MCP servers.

## Setup {#setup}

1. In your IDE's MCP configuration, add a new MCP server entry with the URL `https://mcp.adobeaemcloud.com/adobe/mcp/cloud-migration`.
2. Save or activate the configuration so your IDE connects to the server.
3. When prompted, sign in with your **Adobe ID** to complete authentication.
4. Once authenticated, your IDE discovers the available migration tools and the migration skill can use them in sessions.

For IDE-specific configuration steps, refer to the guides under [Setting Up MCP with AEM](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md).

>[!NOTE]
>You must sign in with the Adobe ID that has access to your CAM projects. If you see an authorization error, verify that your account has the appropriate permissions in Cloud Acceleration Manager.

## Using the MCP in a Migration Session {#using-in-session}

With the MCP server connected, start a migration session in your IDE with a prompt such as:

```
Fetch scheduler findings for project <name>/<id>.
```

The agent:

1. Fetches the BPA findings for that project
2. Proceeds with the batch-by-batch migration workflow

>[!IMPORTANT]
>Always confirm the project from the list before the agent proceeds. Findings are not fetched until you have explicitly selected a project.

### Prioritizing by severity {#by-severity}

To see a count-sorted summary of your BPA report findings before starting pattern migration:

```
Show me CRITICAL findings from CAM for project <name>/<id>.
```

Use this to decide which patterns to prioritize in your sessions.

## Troubleshooting {#troubleshooting}

**IDE cannot connect to the MCP server**

* Verify the URL is entered exactly as shown above, with no trailing slash
* Restart your IDE after saving the MCP configuration

**Authentication fails**

* Ensure you are signing in with the Adobe ID that has access to your CAM projects

**No BPA report found**

* Verify that a BPA report has been uploaded to the selected CAM project. See [Using Best Practices Analyzer](/help/journey-migration/best-practices-analyzer/using-best-practices-analyzer.md).

## What's Next {#whats-next}

With the MCP configured, see [Using the Cloud Migration Skill](/help/journey-migration/cloud-migration-skill/using-cloud-migration-skill.md) for a full reference on migration patterns and session management.
