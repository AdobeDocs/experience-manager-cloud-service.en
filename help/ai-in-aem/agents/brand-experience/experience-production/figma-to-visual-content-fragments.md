---
title: Figma to Visual Content Fragments Job
description: Learn what the Brand Experience Agent's Figma to Visual Content Fragments job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
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

# Figma to Visual Content Fragments Job {#figma-to-visual-content-fragments-job}

The Figma to Visual Content Fragments job of the [Experience Production Agent](/help/ai-in-aem/agents/brand-experience/experience-production/overview.md) automates the process of recreating Figma designs in Adobe Experience Manager (AEM) as a Cloud Service. 

## Overview {#overview}

AEM Visual Content Fragments allow previewing and delivering Content Fragments using a visual layout based on an [HTML template](/help/implementing/developing/extending/content-fragments-visualization-templates.md).

While defining style and layout information in hand-coded HTML templates is entirely feasible, it is a highly technical process that is usually performed by web developers.

To streamline this process for [Visual Content Fragments](/help/sites-cloud/administering/content-fragments/visual-content-fragments.md), and since visual designs for modular experiences are often created in Figma, it is also possible to directly import designs from Figma into AEM.

## Prerequisites {#prerequisites}

Before you start:

* Importing from Figma requires authentication. The Figma user needs to create an access token in Figma and store it in the AEM service.

  This is achieved by:

  * generating a personal token in Figma 
  * logging into Adobe Experience Cloud at `https://experience.adobe.com`
  * persisting the token at `https://experience.adobe.com/#/aem/figmatocontentfragment`

## To upload a design {#to-upload-a-design}

The flow is as follows: 

1. The designer (Figma user) creates the design in Figma.
1. The Figma user creates a share link to the design object in Figma.
1. The Figma user sends the share link to the AEM user.
1. Starting with an initial [prompt](#sample-prompts) the AEM user can then use the AI Assistant to interact with the Figma to Visual Content Fragments Job and automatically recreate the approved design in AEM. AEM will automatically create the required Content Fragment Models, Content Fragments and HTML templates. 
   * When necessary, the agent will ask for more information, such as the AEM environment to use.
   * The agentic creation process also includes capabilities that allow reusing existing content models or fragments when already available.
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
