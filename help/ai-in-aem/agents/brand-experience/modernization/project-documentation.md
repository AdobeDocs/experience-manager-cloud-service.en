---
title: Project Documentation Skill
description: Learn how the Experience Modernization Agent's documentation skill can help you accelerate project handovers.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
---

# Project Documentation Skill {#project-documentation}

Learn how the Experience Modernization Agent's documentation skill can help you accelerate project handovers.

## Accelerating Project Handovers {#project-handovers}

[The Experience Modernization Agent](/help/ai-in-aem/agents/brand-experience/modernization/overview.md) can automatically generate comprehensive project documentation guides for AEM Edge Delivery Services projects featuring:

* **Project walkthrough** - Complete setup explanation without manual effort
* **Module &amp; component organization** - Clear documentation of how everything fits together
* **Role-based guides** - Targeted content for Authors, Developers, and Admins

This simplifies project handovers for AEM Edge Delivery Services projects.

## Prerequisites {#prerequisites}

Ensure the following before using this skill.

* Your project must be checked out to the workspace in the console.
* You must have admin permissions for the project for which you're creating documentation.
* Agent permissions must be allowed in the console.
  * Select the option **Allow LLM to access admin.hlx.page on my behalf** [in the settings of the console.](/help/ai-in-aem/agents/brand-experience/modernization/console.md#settings-view)
  * If this option is not enabled, the documentation task will fail with a 401 error.

## Creating Project Documentation {#creating-documentation}

Once the prerequisites are fulfilled, you simply need to ask the agent to create documentation for your project.

1. In the chat ask "Create documentation of this project."
1. The agent will ask which documentation you would like to create. Normally, you would select **All**.

   ![Create documentation](assets/select-documentation.png)

1. Once created, the guides are placed in your workspace. Select one to view a description and click the link to download the full PDF.

   ![Documentation created](assets/documentation-created.png)

You can save the PDF directly to provide to your teams or upload it as part of the rest of the DA content.

![Admin guide](assets/admin-guide.png)
