---
title: Figma to Visual Content Fragments Job
description: Learn what the Brand Experience Agent's Figma to Visual Content Fragments job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Figma to Visual Content Fragments Job {#figma-to-visual-content-fragments-job}

The Figma to Visual Content Fragments Job of the Experience Production Agent automates the process of recreating approved designs in HTML for Adobe Experience Manager (AEM) as a Cloud Service and Edge Delivery Services. 

>[!NOTE]
>
>The Figma to Visual Content Fragments job is currently in Limited Availability. 
>
>If you would like to participate, please send a request from your official email address to [experience-production-agent@adobe.com](mailto:experience-production-agent@adobe.com).

## Overview {#overview}

Content Fragments contain only structured content, without formatting. So AEM allows you to directly preview, and deliver, your Content Fragments using a visual layout based on an HTML template.

While defining style and layout information in hand-coded HTML templates is entirely feasible, it is a highly technical process that must be performed by web developers.

To streamline this process for Visual Content Fragments, the entire process of importing designs from Figma into AEM is available.

<!--
The Figma to Visual Content Fragments Job of the [Experience Production Agent](/help/ai-in-aem/agents/brand-experience/experience-production/overview.md) automates the process of recreating approved designs in HTML for Adobe Experience Manager (AEM) as a Cloud Service and Edge Delivery Services. 

Content Fragments contain only structured content, without formatting. So AEM allows you to directly preview, and deliver, your Content Fragments using a visual layout based on an [HTML template](/help/implementing/developing/extending/content-fragments-visualization-templates.md).

While defining style and layout information in hand-coded HTML templates is entirely feasible, it is a highly technical process that must be performed by web developers.

To streamline this process for [Visual Content Fragments](/help/sites-cloud/administering/content-fragments/visual-content-fragments.md), the entire process of importing designs from Figma into AEM is available.
-->

## Prerequisites {#prerequisites}

Before you start:

<!-- where in AEM is the access token stored? -->

* Importing from Figma requires authentication. The Figma user needs to create an access token in Figma and store it in the AEM service.

  This is achieved by:

  * generating a personal token in Figma 
  * logging into Adobe Experience Cloud
  * persisting the token at:

    `https://experience.adobe.com/#/{@ADOBE_IMS_ORG}/aem/figmatocontentfragment`

## To upload a design {#to-upload-a-design}

The flow is as follows: 

1. The designer (Figma user) creates the design in Figma.
1. The design is approved.
1. The Figma user sends a Figma share link to the AEM user.
1. Starting with an initial [prompt](#sample-prompts) the AEM user can then use the AI Assistant to interact with the Figma to Visual Content Fragments Job and automatically recreate the approved design in AEM. 
   * When necessary, the agent will ask for more information, such as the AEM environment to use.
   * The agentic creation process includes reasoning capabilities that allow existing content models or fragments to be reused when already available.
1. The agent generates a Content Fragment and a Content Fragment Model for the content, and an HTML template for the layout and design. 
   * The agent provides a direct link to the fragment, from where you can access the model and the template.

## Sample Prompts {#sample-prompts}

Sample prompts include:

* To import from Figma:
  * Import from Figma {*Figma_share_URL*} to AEM
* To select the AEM program from agent suggestions:
  * Import from Figma {*Figma_share_URL*} to {*AEMaaCS_program/environment_link*}
