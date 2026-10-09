---
title: Project Documentation Skill
description: Learn how the Experience Modernization Agent's documentation skill can help you accelerate project handovers.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 111cc47d-085f-4cf4-81bc-332e6a31bbeb
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
# Project Documentation Skill {#project-documentation}

Learn how the Experience Modernization Agent's documentation skill can help you accelerate project handovers.

## Accelerating Project Handovers {#project-handovers}

[The Experience Modernization Agent](/help/ai-in-aem/agents/brand-experience/modernization/overview.md) can automatically generate project documentation guides for AEM Edge Delivery Services projects featuring:

* **Project walkthrough** - Explanation of the project setup, structure, and conventions, generated without manual effort
* **Module &amp; component organization** - Clear documentation of how blocks, modules, and components are organized and how they relate to each other
* **Role-based guides** - Targeted documentation for authors, developers, and administrators, so each team member gets exactly what they need

This simplifies project handovers for AEM Edge Delivery Services projects.

## Prerequisites {#prerequisites}

Ensure the following before using this skill.

* Your project must be checked out to the workspace in the console.
* You must have admin permissions for the project for which you're creating documentation.
* Agent permissions must be allowed in the console.
  * Select the option **Allow LLM to access admin.hlx.page on my behalf** [in the settings of the console.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#settings-view)
  * If this option is not enabled, the the agent will generate the documentation based on the code base accessible to it.
  
## Creating Project Documentation {#creating-documentation}

Once the prerequisites are fulfilled, you simply need to ask the agent to create documentation for your project.

1. In the chat ask `Create documentation for this project`.
1. Provide the organization name of the project if the agent asks for it.
1. The agent will ask which documentation you would like to create. Normally, you would select **All**.

   ![Create documentation](assets/select-documentation.png)

1. Once created, the guides are placed in your workspace. Select one to view a description and click the link to download the full PDF.

   ![Documentation created](assets/documentation-created.png)

You can save the PDF directly to provide to your teams or upload it as part of the rest of the DA content.

![Admin guide](assets/admin-guide.png)

>[!NOTE]
>
>If you are not authorized to access the Edge Delivery Services admin API or the option **Allow LLM to access admin.hlx.page on my behalf** [in the settings of the console.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#settings-view) is not enabled, the agent will generate the documentation based on the code base accessible to it.

## Troubleshooting {#troubleshooting}

The following are common error messages encountered when using the project documentation skill and how to solve them.

### "Access Denied" or "Unauthorized" {#unauthorized}

* **Cause:** Missing admin permissions or agent permissions not enabled
* **Solution:**
  1. Verify you have admin access to the project
  1. Select the option **Allow LLM to access admin.hlx.page on my behalf** [in the settings of the console.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#settings-view)

### "Project Not Found" {#not-found}

* **Cause:** Repository not checked out in workspace
* **Solution:**
  1. Check out the project repository
  1. Ensure you're in the correct workspace

### "Config API Error" {#api-error}

* **Cause:** Unable to access Edge Delivery Services config service API
* **Solution:**
  1. Select the option **Allow LLM to access admin.hlx.page on my behalf** [in the settings of the console.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#settings-view)
  1. Check your network/VPN connection
  1. Confirm admin access to the project
