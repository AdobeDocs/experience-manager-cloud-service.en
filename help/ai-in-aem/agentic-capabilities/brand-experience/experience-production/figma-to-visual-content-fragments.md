---
title: Figma to Visual Content Fragments Skill
description: Learn what the Brand Experience Agentic Capability Figma to Visual Content Fragments Skill is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Figma to Visual Content Fragments Skill {#figma-to-visual-content-fragments-skill}

Visual Content Fragments in Adobe Experience Manager (AEM) allow you to preview and deliver Content Fragments using a [layout that is defined in a visualization template](/help/implementing/developing/extending/content-fragments-visualization-templates.md). These templates are based on an HTML template.

While defining style and layout information in hand-coded HTML templates is entirely feasible, it is a highly technical process that is usually performed by web developers. As visual designs for modular experiences are often created in Figma, it is possible to streamline this process for Visual Content Fragments by directly importing designs from Figma into AEM.

<!-- Add link when available -->

<!--
For more details see this video.
-->

>[!NOTE]
>
>The Figma to Visual Content Fragments skill is part of the [Experience Production Agentic Capability](/help/ai-in-aem/agentic-capabilities/brand-experience/experience-production/overview.md). 

## Use cases {#use-cases}

| Use Case | Description | Skill(s) | Application | Sample Prompts |
| --- | --- | --- | --- | --- |
| Go from Figma to Visual Content Fragment | Import designs directly from Figma into Adobe Experience Manager using natural language. The skill automatically creates the required content model, content fragment, assets, and visualization template, enabling business users to move from design to web-ready content in minutes without manual setup. | `aem-sites-visualcontentfragments-create` | Adobe Experience Manager (AEM) | Import from &lt;Figma_URL&gt; |

## Prerequisites {#prerequisites}

Before you start:

* Importing from Figma requires authentication. 

  * The Figma user needs to create an access token in Figma and store it in the AEM service.

This is achieved by:

1. [Generating a personal token in Figma](https://developers.figma.com/docs/rest-api/personal-access-tokens/)
1. Logging into Adobe Experience Manager as a Cloud Service at [https://experience.adobe.com](https://experience.adobe.com)
1. Persisting the token at [https://experience.adobe.com/#/aem/figmatocontentfragment](https://experience.adobe.com/#/aem/figmatocontentfragment)

## To create a Visual Content Fragment from Figma {#to-create-a-visual-content-fragment-from-figma}

The flow is as follows:

1. Create a design in Figma.

1. Create a share link to the design object in Figma.

1. In AEM, the AEM user can start with an initial prompt to use Coworker to recreate the approved design in AEM. AEM will automatically create the required Content Fragment Models, Content Fragments and HTML templates.

   * When necessary, the agentic skill will ask for more information, such as the AEM environment to use.

   * The agentic creation process also includes capabilities that allow reusing existing content models or fragments when already available.

1. The agent generates a Content Fragment and a Content Fragment Model for the content, and an HTML template for the layout and design.

   * The agent provides a direct link to the fragment, from where you can access the model and the template.

## Sample Prompts {#sample-prompts}

<!-- curly or angled brackets? -->

Sample prompts include:

* To import from Figma:

  * Import from Figma {Figma_share_URL} to AEM

* To import from Figma and specify the AEM program:

  * Import from Figma {Figma_share_URL} to {AEMaaCS_program/environment_link}
