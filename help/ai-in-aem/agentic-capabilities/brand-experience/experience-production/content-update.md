---
title: Content Update Skill
description: Learn what the Brand Experience Agentic Capability content update job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Content Update Skill {#content-update}

Content Update performs updates to existing content in Adobe Experience Manager (AEM), including Content Fragments, Pages and Assets. It can perform actions such as updating, removing, replacing, or adding content elements to keep experiences current and accurate. The skill accepts both natural language descriptions or visual elements such as annotated PDFs and screenshots.

<!-- Check link -->

For more details see:

* [Use cases](/help/ai-in-aem/agentic-capabilities/brand-experience/experience-production/use-cases.md)

* [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide)

* Demonstration video

>[!VIDEO](https://video.tv.adobe.com/v/3504014?learn=on)

>[!NOTE]
>
>The Content Update skill is part of the Experience Production Agentic Capability.

## Prerequisites {#prerequisites}

To instruct the skill where to apply updates you must supply a page link. You may provide either an author URL or a publish URL. 

Before you start you need to configure the Publish (public facing) URL, a one-time configuration:

* Prerequisites:

  * To make the configuration, the user must have System Admin or Product Admin rights.

* Configuration:

  1. Invoke the Content Create skill by requesting a content update for the URL.
  1. Coworker will walk you through the configuration, by asking you a number of questions. 
  1. Once complete the publish URL is configured and can be used.

## Interact with the skill {#interact-with-the-skill}

To initiate content updates you can give a wide range of natural language prompts. You need to specify the public facing (publish) URL, or the author environment URL, of the page you want to update. Some, but not all, of the verbs that are supported; replace, update, remove, change, revised, modify, adjust, delete. 

>[!NOTE]
>
>An inbuilt **Questionnaire** can help guide you through your interaction with the skill. 

### Sample Prompts {#sample-prompts}

Sample prompts include:

* on `<your-publish-URL>` update "Your perfect coffee is four questions away!" to "Your coffee, your way!"
* on `<your-author-env-URL>` replace the image from "holdingcup.png" to "stairhead.png"
* on `<your-publish-URL>` change "Take our Coffee Quiz" button to a more engaging version"
* on `<your-author-env-URL>` remove the section "Rewards unclaimed is a Gift missed!"
* on `<your-author-env-URL>` update based on the attached

### File Upload {#file-upload}

As well as entering natural language prompts directly, you can also upload a document to request changes.

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
