---
title: Setting Up Anthropic Claude with AEM MCP
description: Learn how to configure Anthropic Claude to connect to AEM’s MCP servers
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 2b90b2b2-cdd0-4f1e-890f-2f58f578face
---
# Setting Up Anthropic Claude with AEM MCP {#setup-claude}

This article covers two separate ways to use Anthropic Claude with AEM:

- Manually configure AEM’s MCP servers in Claude (the servers described at [Using MCP with AEM as a Cloud Service — MCP servers](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md#mcp-servers)).
- Install the Adobe Experience Manager Connector from Anthropic’s connector marketplace.

## Manually configure AEM’s MCP servers in Claude {#manual-configure-aems-mcp-servers-in-claude}

This section describes the **manual configuration** approach, where you add one or more of AEM’s MCP servers to Claude as custom connectors.

>[!NOTE]
>
>The Claude user interface is subject to change and is not definitive. These instructions are for illustrative purposes.

1. Open the account menu in the lower-left corner of the Claude web app and choose **Settings** to open the Settings area.

   ![Account menu in Claude with Settings selected.](assets/claude-1.png)

1. In the Settings sidebar, select **Connectors**. On the Connectors page, choose **Add custom connector** to register a custom MCP endpoint.

   ![Connectors page in Settings with Add custom connector.](assets/claude-2.png)

1. In the **Add custom connector** dialog, enter a display name (for example, **AEM Content MCP Service**) and your MCP server URL, then choose **Add**. Use **Advanced settings** only when your deployment requires extra options.

   ![Add custom connector dialog with name and MCP URL.](assets/claude-3.png)

1. On the Connectors list, find your custom connector entry (it shows a **CUSTOM** label) and choose **Connect** to sign in and link the connector to your Claude account.

   ![Connectors list with Connect selected for AEM Content MCP Service.](assets/claude-4.png)

1. When the connector appears in the list with its URL, choose **Configure** next to **AEM Content MCP Service** to open the connector details and continue setup.

   ![Connectors list with Configure selected for AEM Content MCP Service.](assets/claude-5.png)

1. On the **Tool permissions** page, review the default (for example, **Needs approval**), then set each AEM tool to **Always allow**, **Ask for permission**, or **Never allow** according to your security policy.

   ![Tool permissions for AEM Content MCP Service.](assets/claude-6.png)

1. Open a conversation. Select the tools and model menu (sliders icon) to the left of the message field, enable **AEM Content MCP Service** under Connectors, then enter your prompt so Claude can use the MCP tools for that chat.

   ![Chat composer with AEM Content MCP Service enabled in the tools menu.](assets/claude-7.png)

## Install the Adobe Experience Manager Connector (Anthropic connector marketplace) {#install-adobe-experience-manager-connector}

This section describes the **installable connector** from Anthropic’s connector marketplace (as opposed to adding a custom connector URL).

To install the **Adobe Experience Manager Connector**, open **Settings** > **Connectors** in Claude. You can also open the Connectors page directly at [https://claude.ai/settings/connectors](https://claude.ai/settings/connectors). The connector registers an MCP server that exposes a growing set of tools for AEM workflows.

![Installing the Adobe Experience Manager Claude Connector from the connectors directory.](assets/claude-connector.png)