---
title: Setting Up OpenAI ChatGPT with AEM MCP
description: Learn how to configure OpenAI ChatGPT to connect to AEM MCP servers
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 1f116225-168b-483c-9df6-c752a573b57b
---
# Setting Up OpenAI ChatGPT with AEM MCP {#setup-chatgpt}

This article covers two separate ways to use OpenAI ChatGPT with AEM:

- Manually configure one or more of AEM's MCP servers in ChatGPT (the servers described at [Using MCP with AEM as a Cloud Service — MCP servers](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md#mcp-servers)).
- Install the Adobe Experience Manager plugin from the ChatGPT plugin marketplace. It currently has feature parity with Content MCP Server and will expose a growing subset of tools available in AEM's MCP servers.

## Manually configure AEM's MCP servers in ChatGPT {#manually-configure-aems-mcp-servers-in-chatgpt}

This section describes the **manual configuration** approach, where you add one or more of AEM's MCP servers to ChatGPT as custom plugins.

* Add one or more AEM MCP server URLs in the area where MCP connections or tools are configured.
* Trigger the connection and sign in with your Adobe ID when redirected.
* In a chat, reference the configured AEM Tools in your prompts, for example:

   ```
   "Using the configured AEM MCP tools, list all sites in the author environment."
   ```

>[!NOTE]
>
>The OpenAI ChatGPT user interface is subject to change and is not definitive. These instructions are for illustrative purposes.

1. Open **Settings** so you can reach the area where MCP connections or tools are configured.

   ![The ChatGPT Settings dialog.](assets/chatgpt-1.png)

1. In **Plugins**, select **Developer mode**.

   ![The Developer mode option under Plugins in ChatGPT settings.](assets/chatgpt-2.png)

1. Enable **Developer mode** so you can add and configure a custom plugin.

   ![Enabling the Developer mode setting in ChatGPT.](assets/chatgpt-3.png)

1. In the left navigation menu, select **Plugins** again, then select **Browse plugins**.

   ![The Browse plugins option in the ChatGPT Plugins settings menu.](assets/chatgpt-4.png)

1. Select the plus sign (**+**) in the upper-right corner to add an app entry for your AEM MCP server.

   ![The dialog for creating a new plugin in ChatGPT.](assets/chatgpt-5.png)

1. Complete the **New Plugin** form—for example, name the plugin and enter your AEM MCP server URL and any other required fields—then **Create**.

   ![The New Plugin configuration form in ChatGPT.](assets/chatgpt-6.png)

1. Confirm **AEM Content MCP Service** (or your configured plugin) appears under **Plugins** so ChatGPT can use it.

   ![The AEM Content MCP Service listed under Plugins in ChatGPT.](assets/chatgpt-7.png)

1. In a chat, write a prompt that tells ChatGPT to use the configured **AEM Tools** (for example, to query author content or sites).

   ![Prompting ChatGPT to use the AEM Content MCP Service.](assets/chatgpt-8.png)

## Install the Adobe Experience Manager plugin (ChatGPT plugin marketplace) {#install-adobe-experience-manager-plugin}

This section describes the **installable plugin** from the ChatGPT plugin marketplace (as opposed to adding a custom MCP server URL). It includes a subset of the tools available in AEM's MCP servers.

>[!NOTE]
>
>The OpenAI ChatGPT user interface is subject to change and is not definitive. These instructions are for illustrative purposes.

You can reach the Adobe Experience Manager plugin in either of two ways. Use whichever is more convenient, then continue with the sign-in steps that follow.

**Option 1: Open the plugin page directly**

Go to the [Adobe Experience Manager plugin page](https://chatgpt.com/plugins/plugin_asdk_app_6a35d3c1258081919c084a1fd22cd02d) and choose **Install plugin**.

   ![The Adobe Experience Manager plugin page with the Install plugin button.](assets/chatgpt-plugin-install.png)

**Option 2: Find the plugin in the marketplace**

1. From **Settings**, choose **Plugins**, then at the bottom of the list choose **Browse plugins**.

   ![The Plugins page in ChatGPT Settings with Browse plugins.](assets/chatgpt-plugin-1.png)

1. Search for **Adobe Experience Manager**, then select it.

   ![Searching for the Adobe Experience Manager plugin in the plugin marketplace.](assets/chatgpt-plugin-2.png)

**Sign in and confirm**

After you locate or install the plugin using either option above, complete the connection:

1. Choose **Sign in with Adobe Experience Manager** and log in to AEM when redirected.

   ![The Add Adobe Experience Manager to ChatGPT dialog with Sign in with Adobe Experience Manager.](assets/chatgpt-plugin-3.png)

1. Confirm the green banner indicates that Adobe Experience Manager is now connected.

   ![The green banner confirming the Adobe Experience Manager plugin is connected.](assets/chatgpt-plugin-4.png)
