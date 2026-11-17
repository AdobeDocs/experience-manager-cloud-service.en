---
title: Setting Up Cursor with AEM MCP
description: Learn how to configure Cursor to connect to AEM MCP servers
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: f0897898-cb1d-4af6-859c-f5a1c0ec6168
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: f2d27a5f-0d67-4d85-8a24-86a8d8a3574b
    internal-label: Developer tools
  - id: ac5ecfc1-cc78-4ecc-a90a-0362685062ce
    internal-label: AI Tools
subfeature_v2:
  - id: f88183b7-5ea5-436c-ac46-96b53f0281ea
    internal-label: Edge Delivery Services
  - id: f1710108-e0d1-47e5-9952-1888729a03da
    internal-label: Agentic AI
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Setting Up Cursor with AEM MCP {#setup-cursor}

Follow these steps to connect Cursor to AEM's MCP servers.

* In Cursor's MCP settings, create a new MCP server entry with one or more AEM MCP URLs.
* Authenticate with your Adobe ID when prompted.
* Optionally, enable or disable individual tools by clicking on the tool names. All tools are enabled by default.
* Use Cursor's editor or chat to invoke AEM Tools as part of development or content workflows.

>[!NOTE]
>
>The Cursor user interface is subject to change and is not definitive. These instructions are for illustrative purposes.

1. Open **Cursor Settings** so you can configure how Cursor connects to MCP servers.

   ![The Cursor Settings dialog.](assets/cursor-1.png)

1. Open **Tools and MCP**, then choose **Add Custom MCP** to start a custom MCP server entry.

   ![The Tools and MCP panel with the option to add a custom MCP server.](assets/cursor-2.png)

1. On the custom MCP server form, enter the **Name**, your AEM MCP **URL** (or URLs), and any other required fields, then **Save**.

   ![The custom MCP server settings form in Cursor.](assets/cursor-3.png)

1. When the connection dialog appears, complete sign-in by pressing **Connect** so the new MCP server is authorized.

   ![The connection dialog for the new MCP server in Cursor.](assets/cursor-4.png)

1. In **Chat** or the editor, write prompts that invoke **AEM Tools** so the configured MCP server participates in your workflow.

   ![Prompting Cursor to use the new AEM MCP service.](assets/cursor-5.png)
