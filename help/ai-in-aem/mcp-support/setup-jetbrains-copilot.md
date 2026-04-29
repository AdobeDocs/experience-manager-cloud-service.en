---
title: Setting Up JetBrains with GitHub Copilot and AEM MCP
description: Learn how to configure GitHub Copilot in JetBrains IDEs to connect to AEM MCP servers
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: e153da42-51e0-49ea-8457-10bb5e77e2de
---
# Setting Up JetBrains with GitHub Copilot and AEM MCP {#setup-jetbrains-copilot}

Follow these steps to connect GitHub Copilot in a JetBrains IDE (such as IntelliJ IDEA, WebStorm, or PyCharm) to AEM's MCP servers.

1. Open GitHub Copilot Chat in your JetBrains IDE by clicking the **GitHub Copilot Chat** icon on the right side of the editor.

   ![The JetBrains IDE with GitHub Copilot Chat open.](assets/jetbrains-copilot-1.png)

1. Click the **settings** icon in the Copilot Chat panel to open the MCP configuration.

   ![The GitHub Copilot Chat panel with the settings icon highlighted.](assets/jetbrains-copilot-2.png)

1. In **Settings**, navigate to **Tools > GitHub Copilot > Model Context Protocol (MCP)** and click **Configure** to open the `mcp.json` configuration file.

   ![The JetBrains Settings dialog showing the Model Context Protocol (MCP) configuration under GitHub Copilot.](assets/jetbrains-copilot-3.png)

1. Add one or more AEM MCP server URLs to the `mcp.json` file. For example:

   ```json
   {
     "servers": {
       "aem": {
         "url": "https://mcp.adobeaemcloud.com/adobe/mcp/content"
       }
     }
   }
   ```


   ![The mcp.json configuration file with the AEM MCP server URL.](assets/jetbrains-copilot-4.png)


1. Save the file. GitHub Copilot detects the new server configuration automatically and shows a **Start** action.

   ![The mcp.json file showing the configured AEM server with detected tools.](assets/jetbrains-copilot-5.png)

1. Click the **Start** action and When prompted, sign in with your Adobe ID to complete the authentication flow.

1. You can review and manage discovered tools by clicking the **tools** indicator that appears in the Copilot Chat panel. Optionally, enable or disable individual tools.


   ![The Configure Tools dialog showing available AEM MCP tools.](assets/jetbrains-copilot-6.png)

1. Use GitHub Copilot Chat to invoke AEM tools as part of your development or content workflows.
