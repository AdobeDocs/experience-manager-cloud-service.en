---
title: Content Create Job
description: Learn what the Brand Experience Agent's content create job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Content Create Job {#content-create}

The Content Create job of the [Experience Production Agent](/help/ai-in-aem/agents/brand-experience/experience-production/overview.md) creates new on-brand pages using natural language, a marketing brief, and an AEM template. It accelerates page production for Adobe Experience Manager (AEM) as a Cloud Service and Edge Delivery Services.

>[!NOTE]
>
> The Content Create job is currently in Limited Availability. If you would like to participate, please send a request from your official email address to [experience-production-agent@adobe.com](mailto:experience-production-agent@adobe.com).

## Overview {#overview}

The Content Create job generates copy and structure from your inputs. 

You provide:

* a [brief](#the-brief); covering goals, audience, topics, target word count, keywords, and similar guidance, 
* a [natural-language prompt](#the-prompt): that describes what to create and where the page should live, 
* an [AEM template](#select-a-template): that defines the required layout. 

The agent aligns generation to the template and can add or remove sections to match the brief; for example, when you need a higher or lower word count.

## Capabilities {#capabilities}

You can access the content create skill from:

* [The AI Assistant](#ai-assistant)

## AI Assistant {#ai-assistant}

You can access the job in AEM via the AI Assistant. Open the AI Assistant from [`experience.adobe.com`](https://experience.adobe.com). Then use the Assistant in the upper-right area of the interface to run the workflow below.

### The brief {#the-brief}

Content create uses a marketing brief or document that describes what the agent should generate. Many brief formats are supported. Effective briefs often specify goals, audience, topics, target word count, and keywords.

### The prompt {#the-prompt}

In the Assistant, describe in natural language what you want—for example, creating a new page based on your brief—and **identify where the page will be located** (for example, a path or URL under your site).

Example:

* `Create a new page based on the attached brief at https://example.com/your-site/sustainability/coffee-bean-types`

You also need to **upload the brief** with your request.

<!--
>[!NOTE]
>
> File upload is part of the Limited Availability program and is only available if you are enrolled in the program.
-->

To attach a file:

1. Select **+** in the lower-left of the Assistant and choose **Attach files**.
1. Add your brief file. The prompt area should show the attachment (for example, in the upper-left of the prompt).

When you are ready, submit the prompt using the blue submit control.

### Select a template {#select-a-template}

The template tells the agent the page structure and layout. Generation conforms to that layout. The agent may add or remove sections as needed based on the brief (for example, to meet a different word count).

### Review the plan {#review-the-plan}

Next, the agent presents a **plan** for what it will do based on your inputs and its analysis of the brief. You can adjust the plan or proceed to start generation.

>[!NOTE]
>
> If you use the [Governance Agent](/help/ai-in-aem/agents/governance/overview.md), generation can follow your brand guidelines.

### Proceed with generation {#proceed-with-generation}

When generation finishes, the agent provides **two links**: a **preview** link and an **edit** link. Use the edit link to open the page in an AEM authoring surface for further refinement.

### Further refinement in authoring {#further-refinement-in-authoring}

After you choose to edit the page in AEM, it opens in your authoring environment (for example, the [Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md) or the [Page Editor](/help/sites-cloud/authoring/page-editor/introduction.md)).

In the **Universal Editor**, the AI Assistant is **context aware**: you can select elements on the canvas and work on them with the Assistant.

<!--
>[!NOTE]
>
> Support for additional authoring surfaces will expand over time.
-->

### Edit text with the Assistant {#edit-text-with-the-assistant}

To refine copy from the Assistant while authoring:

1. Select the element in the Universal Editor.
1. Open the AI Assistant from the upper-right corner, enter your prompt, and submit.

Example prompts:

* `Update to Explore the World of Coffee`
* `Update to be more engaging for the 30-40 year old age demographic and avid coffee drinker`

Select **Apply changes** (or equivalent) so updates appear on the page.

## Activation {#activation}

You can explore AEM Agents through the [Playground](https://www.aem.live/developer/aem-playground), or connect with your CSM or TAM to discuss access via the Agentic SKU.

## Limitations {#limitations}

Please be aware of the following limitations:

* The capability is in Limited Availability and requires manual onboarding for participation.

## Additional Resources {#additional-resources}

The following resources may be useful as you continue to explore the Experience Production Agent:

* You can also use the [Experience Production Agent Workbook](https://www.adobe.com/go/aem-epa-workbook) for guided, hands-on instructions.
