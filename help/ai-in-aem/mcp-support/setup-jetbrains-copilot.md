---
title: Setting Up JetBrains with GitHub Copilot and AEM MCP
description: Learn how to configure GitHub Copilot in JetBrains IDEs to connect to AEM MCP servers
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
exl-id: 3a7e5c8d-bf42-4d9a-a2c1-8f6e4b3d9c0a
---
# Setting Up JetBrains with GitHub Copilot and AEM MCP {#setup-jetbrains-copilot}

Follow these steps to connect GitHub Copilot in a JetBrains IDE (such as IntelliJ IDEA, WebStorm, or PyCharm) to AEM's MCP servers.

* Open GitHub Copilot Chat in your JetBrains IDE by clicking the **GitHub Copilot Chat** icon on the right side of the editor.
* Click the **settings** icon in the Copilot Chat panel to open the MCP configuration.
* In **Settings**, navigate to **Tools > GitHub Copilot > Model Context Protocol (MCP)** and click **Configure** to open the `mcp.json` configuration file.
* Add one or more AEM MCP server URLs to the `mcp.json` file. For example:

   ```json
   {
     "servers": {
       "aem": {
         "url": "https://mcp.adobeaemcloud.com/adobe/mcp/content"
       }
     }
   }
   ```

* Save the file. GitHub Copilot detects the new server configuration automatically and shows a **Start** action.
* Click the **Start** action and When prompted, sign in with your Adobe ID to complete the authentication flow.
* You can review and manage discovered tools by clicking the **tools** indicator that appears in the Copilot Chat panel. Optionally, enable or disable individual tools.
* Use GitHub Copilot Chat to invoke AEM tools as part of your development or content workflows.

![The JetBrains IDE with GitHub Copilot Chat open.](assets/jetbrains-copilot-1.png)

![The GitHub Copilot Chat panel with the settings icon highlighted.](assets/jetbrains-copilot-2.png)

![The JetBrains Settings dialog showing the Model Context Protocol (MCP) configuration under GitHub Copilot.](assets/jetbrains-copilot-3.png)

![The mcp.json configuration file with the AEM MCP server URL.](assets/jetbrains-copilot-4.png)

![The mcp.json file showing the configured AEM server with detected tools.](assets/jetbrains-copilot-5.png)

![The Configure Tools dialog showing available AEM MCP tools.](assets/jetbrains-copilot-6.png)
