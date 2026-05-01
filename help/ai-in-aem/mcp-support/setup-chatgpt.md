---
title: Setting Up OpenAI ChatGPT with AEM MCP
description: Learn how to configure OpenAI ChatGPT to connect to AEM MCP servers
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 1f116225-168b-483c-9df6-c752a573b57b
---
# Setting Up OpenAI ChatGPT with AEM MCP {#setup-chatgpt}

Follow these steps to connect OpenAI ChatGPT to AEM's MCP servers.

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

1. In **Apps and Connectors**, open **Advanced Settings** to manage connector and MCP-related options.

   ![The Apps and Connectors Advanced Settings panel in ChatGPT.](assets/chatgpt-2.png)

1. Enable **Developer mode** in **Apps and Connectors** so you can add and configure custom apps or connectors.

   ![Enabling Developer mode in the Apps and Connectors section.](assets/chatgpt-3.png)

1. Start **Create new app** (or the equivalent control) to add an app entry for your AEM MCP server.

   ![The dialog for creating a new app in ChatGPT.](assets/chatgpt-4.png)

1. Complete the **New App** form—for example, name the app and enter your AEM MCP server URL and any other required fields—then **Save**.

   ![The New App configuration form in ChatGPT.](assets/chatgpt-5.png)

1. Confirm **AEM Content MCP Service** (or your configured app) appears in **Apps and Connectors** so ChatGPT can use it.

   ![The AEM Content MCP Service listed in Apps and Connectors.](assets/chatgpt-6.png)

1. In a chat, write a prompt that tells ChatGPT to use the configured **AEM Tools** (for example, to query author content or sites).

   ![Prompting ChatGPT to use the AEM Content MCP Service.](assets/chatgpt-7.png)
