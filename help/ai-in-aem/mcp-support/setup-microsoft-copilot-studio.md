---
title: Setting Up Microsoft Copilot Studio with AEM MCP
description: Learn how to configure Microsoft Copilot Studio to connect to AEM MCP servers
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: c8e96fe6-1a05-47c0-8215-0c28705e5e48
---
# Setting Up Microsoft Copilot Studio with AEM MCP {#setup-microsoft-copilot-studio}

Follow these steps to connect Microsoft Copilot Studio to AEM's MCP servers.

>[!NOTE]
>
>The Microsoft Copilot Studio user interface is subject to change and is not definitive. These instructions are for illustrative purposes.

1. In **Agents**, start the flow to add an agent that will use AEM MCP tools.

   * Create a new agent.

   ![The Agents panel in Microsoft Copilot Studio.](assets/copilot-1.png)

1. Open the tools area for that agent so you can register how it calls external capabilities.

   * Navigate to the tool section and click **Add tool**.

   ![The Add tool dialog in Microsoft Copilot Studio.](assets/copilot-2.png)

1. Decide whether to reuse an existing integration or define a new MCP-backed tool.

   * Select an existing tool or create a new one.

   ![Selecting Model Context Protocol as the tool type.](assets/copilot-3.png)

1. When you create a new MCP tool, continue through the **Model Context Protocol** server step, including preview mode when it appears.

   * Configure a new MCP tool pointing to one or more AEM MCP server **URLs**.

   ![Adding a Model Context Protocol server in preview mode.](assets/copilot-4.png)

1. Define how this MCP endpoint is reached by the agent, including whether access is shared or dedicated.

   * Establish a connection, which can be **shared** or **dedicated** between agents.

   ![The dialog for creating a new connection.](assets/copilot-5.png)

1. On **Add and configure**, supply or confirm MCP tool details so the agent can reach your AEM environment.

   ![The Add and configure panel for the MCP tool.](assets/copilot-6.png)

1. Finish fields on the MCP tool form (for example, server **URLs** and authentication-related options).

   * Optionally, enable **auto-confirm mode** or require **end-user confirmation** for all tool interactions.

   ![The MCP tool configuration form.](assets/copilot-7.png)

1. Validate connectivity to the MCP server; complete browser-based sign-in when Copilot Studio redirects you.

   * Sign in using your **Adobe ID** when redirected.

   ![Testing the connection to the AEM MCP server.](assets/copilot-8.png)

1. Before running a test, open **Manage Connections** (or the **connection manager**) and assign the right connection to your session.

   * When testing your agent, open the **connection manager** first to assign a connection to your session.

   ![The Manage Connections panel showing available connections.](assets/copilot-9.png)

1. In the test experience, run the agent against your AEM MCP connection.

   * When testing your agent, press **Retry** after you assign a connection in the **connection manager**.

   ![Testing the agent with the AEM MCP connection.](assets/copilot-10.png)
