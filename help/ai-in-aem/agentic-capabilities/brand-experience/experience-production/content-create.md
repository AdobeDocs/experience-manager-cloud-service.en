---
title: Content Create Skill
description: Learn what the Brand Experience Agentic Capability content create job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Content Create Skill {#content-create}

Content Create generates new, on-brand Adobe Experience Manager (AEM) pages in minutes, so accelerating time to market. It uses a natural language prompt together with a marketing brief to provide guidance, and an AEM reference page as a template for the layout. 

<!-- Check link -->

For more details see:

* [Use cases](/help/ai-in-aem/agentic-capabilities/brand-experience/experience-production/use-cases.md)

* [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide)

* Demonstration video

>[!VIDEO](https://video.tv.adobe.com/v/3504013?learn=on)

>[!NOTE]
>
>The Content Create skill is the part of the Experience Production Agentic Capability.

## Prerequisites {#prerequisites}

To instruct the skill where to apply updates you must supply a page link. You may provide either an author URL or a publish URL. 

Before you start you need to configure the Publish (public facing) URL, a one-time configuration:

* Prerequisites:

  * To make the configuration, the user must have System Admin or Product Admin rights.

* Configuration:

  1. Invoke the Content Create skill by requesting a content update for the URL.
  1. Coworker will walk you through the configuration, by asking you a number of questions. 
  1. Once complete the publish URL is configured and can be used.

## Provide the prompt and brief {#provide-the-prompt-and-brief}

To provide the prompt and brief you need to:

1. Use natural language to describe what you want done and identifying where the page will be located, using a path or URL within your website. For example, creating a new page based on your brief:
  
   * `create a new page based on the attached at https://frescopa.coffee/sustainability/coffee-bean-types`

1. Upload the brief relevant to your request. 

1. When you are ready, submit the prompt and the brief.

## Select a template {#select-a-template}

The skill will then request that you specify a template. The template provides the skill with the page structure and layout. Generation conforms to that layout. The skill can add and remove sections as needed, based on the brief; for example, to meet a different word count.

## Review the plan {#review-the-plan}

Next, the skill presents a plan for the changes it will make, as based on your inputs and its analysis of the brief. You can adjust the plan or proceed with the plan and start generation.

## Proceed with generation {#proceed-with-generation}

When generation finishes, the skill provides two links: 

* a **preview** link 
* an **edit** link
  * Use the edit link to [open the page in an AEM authoring surface](#further-refinement-in-authoring) for further refinement.

## Further refinement in authoring {#further-refinement-in-authoring}

After you choose to edit the page in AEM, it opens in your authoring environment; for example, the [Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md) or the [Page Editor](/help/sites-cloud/authoring/page-editor/introduction.md).

In the [Universal Editor](#universal-editor-edit-text-with-the-assistant), the AI Assistant is *context aware*: you can select elements on the canvas and work on them with the assistant.

### Universal Editor - edit text with the Assistant {#universal-editor-edit-text-with-the-assistant}

To refine copy from the Assistant while authoring:

1. Select the element in the [Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md).
1. Open the AI Assistant from the upper-right corner, enter your prompt, and submit.

Example prompts:

* `Update to Explore the World of Coffee`
* `Update to be more engaging for the 30-40 year old age demographic and avid coffee drinker`

Select **Apply changes** (or equivalent) so updates appear on the page.
