---
title: Content Create Job
description: Learn what the Brand Experience Agent's content create job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Content Create Job {#content-create}

The Content Create job is the part of the [Experience Production Agent](/help/ai-in-aem/agents/brand-experience/experience-production/overview.md) that creates new on-brand pages using natural language, a marketing brief, and an AEM template. It accelerates page production for Adobe Experience Manager (AEM) as a Cloud Service and Edge Delivery Services.

<!-- see Limitations too -->

>[!NOTE]
>
>The Content Create job is currently in Limited Availability. If you would like to participate, please send a request from your official email address to [experience-production-agent@adobe.com](mailto:experience-production-agent@adobe.com).

## Overview {#overview}

The Content Create job generates new on-brand pages using natural language along with a marketing brief and AEM template. 

You can access the Content Create job from:

* [The AI Assistant](#access-ai-assistant)

>[!VIDEO](https://video.tv.adobe.com/v/3488436?learn=on)

To use the Create Content Job:

* You provide:

  * a [natural-language prompt](#the-prompt): that describes what to create and where the page should live, 
  * a [brief](#the-brief); covering goals, audience, topics, target word count, keywords, and similar guidance, 

* You then [Submit](#submit) the prompt and brief
* Next you specifiy an [AEM template](#select-a-template): that defines the required layout
* The job will provide a [plan for you to review](#review-the-plan)
* You can then [proceed with the generation](#proceed-with-generation), and [further refine in authoring if required](#further-refinement-in-authoring)

The agent aligns generation to the template and can add or remove sections to match the brief; for example, when you need a higher or lower word count.

>[!NOTE]
>
>This page uses an example, to create a new page based on an attached brief at `https://frescopa.coffee/sustainability/coffee-bean-types`

## Access - AI Assistant {#access-ai-assistant}

You can access the job in AEM via the AI Assistant. 

Open the [AI Assistant](/help/implementing/cloud-manager/ai-assistant-in-aem.md)  from the top-right toolbar of [`experience.adobe.com`](https://experience.adobe.com). 

## The prompt {#the-prompt}

In the AI Assistant you need to:

* use natural language to describe what you want done; for example, creating a new page based on your brief
* identify where the page will be located, using a path or URL within your website
* upload the brief relevant to your request

  * To attach a file:

    1. Select **+** in the lower-left of the AI Assistant and choose **Attach files**.
    1. Add your brief file. The prompt area should show the attachment; for example, in the upper-left of the prompt.

* submit the prompt using the blue submit icon (blue arrowhead).

To specify the prompt:

* `create a new page based on the attached at https://frescopa.coffee/sustainability/coffee-bean-types`

  ![Content Create Job - add a prompt](/help/ai-in-aem/agents/brand-experience/experience-production/assets/create-content-example-create-page.png)

## The brief {#the-brief}

The Content Create job uses a marketing brief or document that describes what the agent should generate. The job accepts a wide range of formats for the brief. Effective briefs often specify goals, audience, topics, target word count, and keywords.

To load the brief:

![Content Create Job - load a brief](/help/ai-in-aem/agents/brand-experience/experience-production/assets/create-content-example-load-brief.png)

The loaded brief will be shown in the top-right of the prompt dialog:

![Content Create Job - loaded brief](/help/ai-in-aem/agents/brand-experience/experience-production/assets/create-content-example-loaded-brief.png)

<!--
>[!NOTE]
>
> File upload is part of the Limited Availability program and is only available if you are enrolled in the program.
-->

## Submit {#submit}

When you are ready, submit the prompt and the brief using the blue submit control.

## Select a template {#select-a-template}

The agent will then request that you specify a template. The template provides the agent with the page structure and layout. Generation conforms to that layout. The agent can add and remove sections as needed, based on the brief; for example, to meet a different word count.

![Content Create Job - specify the template](/help/ai-in-aem/agents/brand-experience/experience-production/assets/create-content-example-select-template.png)

## Review the plan {#review-the-plan}

Next, the agent presents a plan for the changes it will make, as based on your inputs and its analysis of the brief. You can adjust the plan or proceed with the plan and start generation.

>[!NOTE]
>
> If you use the [Governance Agent](/help/ai-in-aem/agents/governance/overview.md), generation can follow your brand guidelines.

![Content Create Job - review the plan](/help/ai-in-aem/agents/brand-experience/experience-production/assets/create-content-example-review-plan.png)

## Proceed with generation {#proceed-with-generation}

When generation finishes, the agent provides two links: 

* a **preview** link 
* an **edit** link
  * Use the edit link to [open the page in an AEM authoring surface](#further-refinement-in-authoring) for further refinement.

![Content Create Job - proceed with generation](/help/ai-in-aem/agents/brand-experience/experience-production/assets/create-content-example-proceed-generation.png)

## Further refinement in authoring {#further-refinement-in-authoring}

After you choose to edit the page in AEM, it opens in your authoring environment (for example, the [Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md) or the [Page Editor](/help/sites-cloud/authoring/page-editor/introduction.md)).

In the Universal Editor, the AI Assistant is *context aware*: you can select elements on the canvas and work on them with the assistant.

<!--
>[!NOTE]
>
> Support for additional authoring surfaces will expand over time.
-->

<!--
## Edit text with the Assistant {#edit-text-with-the-assistant}

To refine copy from the Assistant while authoring:

1. Select the element in the Universal Editor.
1. Open the AI Assistant from the upper-right corner, enter your prompt, and submit.

Example prompts:

* `Update to Explore the World of Coffee`
* `Update to be more engaging for the 30-40 year old age demographic and avid coffee drinker`

Select **Apply changes** (or equivalent) so updates appear on the page.
-->

## Activation {#activation}

You can explore AEM Agents through the [Playground](https://www.aem.live/developer/aem-playground), or connect with your CSM or TAM to discuss access via the Agentic SKU.

## Limitations {#limitations}

Please be aware of the following limitations:

* The capability is in Limited Availability and requires manual onboarding for participation. If you would like to participate, please send a request from your official email address to [experience-production-agent@adobe.com](mailto:experience-production-agent@adobe.com).

## Additional Resources {#additional-resources}

The following resources may be useful as you continue to explore the Experience Production Agent:

* You can also use the [Experience Production Agent Workbook](https://www.adobe.com/go/aem-epa-workbook) for guided, hands-on instructions.
