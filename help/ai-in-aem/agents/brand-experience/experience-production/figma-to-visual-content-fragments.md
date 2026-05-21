---
title: Figma to Visual Content Fragments Job
description: Learn what the Brand Experience Agent's Figma to Visual Content Fragments job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Figma to Visual Content Fragments Job {#figma-to-visual-content-fragments-job}

The Figma to Visual Content Fragments Job of the [Experience Production Agent](/help/ai-in-aem/agents/brand-experience/experience-production/overview.md) automates the process of recreating Figma designs in Adobe Experience Manager (AEM) as a Cloud Service. 

>[!NOTE]
>
>The Figma to Visual Content Fragments job is currently in Limited Availability. 
>
>If you would like to participate, please send a request from your official email address to [experience-production-agent@adobe.com](mailto:experience-production-agent@adobe.com).

## Overview {#overview}

AEM Visual Content Fragments allow previewing and delivering Content Fragments using a visual layout based on an [HTML template](/help/implementing/developing/extending/content-fragments-visualization-templates.md).

While defining style and layout information in hand-coded HTML templates is entirely feasible, it is a highly technical process that is commonly performed by web developers.

To streamline this process for [Visual Content Fragments](/help/sites-cloud/administering/content-fragments/visual-content-fragments.md), and since visual designs for modular experiences are often created in Figma, it is also possible to directly import designs from Figma directly into AEM.

## Prerequisites {#prerequisites}

Before you start:

* Importing from Figma requires authentication. The Figma user needs to create an access token in Figma and store it in the AEM service.

  This is achieved by:

  * generating a personal token in Figma 
  * logging into Adobe Experience Cloud at 'https://experience.adobe.com'
  * persisting the token at 'https://experience.adobe.com/#/aem/figmatocontentfragment`


## To upload a design {#to-upload-a-design}

The flow is as follows: 

1. The designer (Figma user) creates the design in Figma.
1. The Figma user creates a share link to the design object in Figma.
1. The Figma user sends the share link to the AEM user.
1. Starting with an initial [prompt](#sample-prompts) the AEM user can then use the AI Assistant to interact with the Figma to Visual Content Fragments Job and automatically recreate the approved design in AEM. AEM will automatically create required Content Fragment Models, Content Fragments and HTML templates. 
   * When necessary, the agent will ask for more information, such as the AEM environment to use.
   * The agentic creation process includes also includes capabilities that allow reusing existing content models or fragments when already available.
1. The agent generates a Content Fragment and a Content Fragment Model for the content, and an HTML template for the layout and design. 
   * The agent provides a direct link to the fragment, from where you can access the model and the template.

## Sample Prompts {#sample-prompts}

Sample prompts include:

* To import from Figma:
  * Import from Figma {*Figma_share_URL*} to AEM
* To select the AEM program from agent suggestions:
  * Import from Figma {*Figma_share_URL*} to {*AEMaaCS_program/environment_link*}

## Additional Resources {#additional-resources}

The following resources may be useful as you continue to explore Visual Content Fragments:

* [Visual Content Fragments](/help/sites-cloud/administering/content-fragments/visual-content-fragments.md)
* [Visual Content Fragments - Templates](/help/implementing/developing/extending/content-fragments-visualization-templates.md)
* [Visual Content Fragments - Deliver with the Publish URL](/help/implementing/developing/extending/content-fragments-visualization-publish-url.md)
