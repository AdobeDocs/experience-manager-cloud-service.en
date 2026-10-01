---
title: Content Update Job
description: Learn what the Brand Experience Agent's content update job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: e2d1dae8-38de-4357-bb14-ad35acb71aee
---

# Content Update Job {#content-update}

The content update job of the [Experience Production Agent](/help/ai-in-aem/agents/brand-experience/experience-production/overview.md) automates content production to accelerate everyday tasks for Adobe Experience Manager (AEM) as a Cloud Service and Edge Delivery Services. 

## Overview {#overview}

The content update job updates existing content, including content fragments, pages, forms and assets. The job can perform actions such as updating, removing, replacing, or adding content elements to keep experiences accurate and current. Inputs can be natural language description, and when used with Jira PDFs and screenshots can provide input too.

The content update job transforms the details that you provide, either through natural language or visuals, into content updates on your page. You supply the URL of a page that needs updating, together with details of what needs updating, and the agent job completes your task. When used with AEM as a Cloud Service, the job creates a new [launch](/help/sites-cloud/authoring/launches/overview.md) so you can review the updates before applying. When used with Document authoring, the job creates a new [version](https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/document-authoring/how-to/document-versions#).

>[!VIDEO](https://video.tv.adobe.com/v/3486418?learn=on)

## Capabilities {#capabilities}

You can access the content update job from:

* [The AI Assistant](#ai-assistant)
* [Jira](#jira)

## AI Assistant {#ai-assistant}

You can access the job in AEM via the AI Assistant. 

Open the [AI Assistant](/help/implementing/cloud-manager/ai-assistant-in-aem.md#ai-use) from the top-right toolbar to start a conversation. 

![AI Assistant icon on the toolbar](/help/ai-in-aem/agents/brand-experience/experience-production/assets/ai-assistant-icon.png)

### Configuring the Publish URL {#configuring-the-publish-url}

To instruct the agent where to apply updates you must supply a page link. You may provide either an author URL or a publish URL. 

To use a publish (public facing) URL a one-time configuration must be made:

* Prerequisites:

  * To make the configuration, the user must have System Admin or Product Admin rights.

* Configuration:

  1. Invoke the Content Update job by requesting a content update for the URL.
  1. The assistant will walk you through the configuration, by asking you a number of questions. 
  1. Once complete the publish URL is configured and can be used.

For example:

![Content Update job - configure publish URL](/help/ai-in-aem/agents/brand-experience/experience-production/assets/content-update-publish-url-configuration.png)

### Prompts {#prompts}

To initiate content updates you can give a wide range of natural language prompts. You need to specify the public facing (publish) URL, or the author environment URL, of the page you want to update. Some, but not all, of the verbs that are supported; replace, update, remove, change, revised, modify, adjust, delete. 

### Sample Prompts {#sample-prompts}

Sample prompts include:

* on `<your-publish-URL>` update "Your perfect coffee is four questions away!" to "Your coffee, your way!"
* on `<your-author-env-URL>` replace the image from "holdingcup.png" to "stairhead.png"
* on `<your-publish-URL>` change "Take our Coffee Quiz" button to a more engaging version"
* on `<your-author-env-URL>` remove the section "Rewards unclaimed is a Gift missed!"
* on `<your-author-env-URL>` update based on the attached

### File Upload in AI Assistant {#file-upload-in-ai-assistant}

As well as entering natural language prompts directly, you can also upload a document to request changes.

Use the `+` icon in the bottom left of the prompt menu to upload a file specifying your requirements. Supported file formats include; PDF, JPG, PNG, DOCX, and others.

![Content Update job - file upload](/help/ai-in-aem/agents/brand-experience/experience-production/assets/content-update-file-upload.png)

For example, an annotated PDF specifying the requested changes:

![Content Update job - annotated PDF](/help/ai-in-aem/agents/brand-experience/experience-production/assets/content-update-annotated-pdf.png)

>[!VIDEO](https://video.tv.adobe.com/v/3491297?learn=on)

### Orchestration with the Brand Governance Agent  {#orchestration-with-the-brand-governance-agent}

If the organization has imported their brand policy the Content Update job will use this policy during agentic content updates (see the [Overview](#overview) video).

For a *prescriptive* prompt such as:

* `on <your-publish-URL> update “Your perfect coffee is four questions away!” to “Your coffee, your way!”`

The Content Update job orchestrates with the [Brand Governance agent](/help/ai-in-aem/agents/brand-experience/overview.md) and notifies the user if the provided copy is on-brand or not.

![Content Update job - orchestration with the Brand Governance Agent](/help/ai-in-aem/agents/brand-experience/experience-production/assets/content-update-brand-experience.png)

For more abstract prompts such as:

* `on <your-publish-env-URL> change “Take our Coffee Quiz” button to a more engaging version`

During generation the agent will utilize the brand guidelines to ensure that the output is on-brand.

## Further refinement in authoring {#further-refinement-in-authoring}

After you choose to edit the page in AEM, it opens in your authoring environment (for example, the [Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md) or the [Page Editor](/help/sites-cloud/authoring/page-editor/introduction.md)).

In the [Universal Editor](#universal-editor-edit-text-with-the-assistant), the AI Assistant is *context aware*: you can select elements on the canvas and work on them with the assistant.

### Universal Editor - edit text with the Assistant {#universal-editor-edit-text-with-the-assistant}

To refine copy from the Assistant while authoring:

1. Select the element in the [Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md).
1. Open the AI Assistant from the upper-right corner, enter your prompt, and submit.

Example prompts:

* `Update to Explore the World of Coffee`
* `Update to be more engaging for the 30-40 year old age demographic and avid coffee drinker`

Select **Apply changes** (or equivalent) so updates appear on the page.

## Activation {#activation}

You can explore AEM Agents through the [Playground](https://www.aem.live/developer/aem-playground), or connect with your CSM or TAM to discuss access via the Agentic SKU.

## Additional Resources {#additional-resources}

The following resources may be useful as you continue to explore the Experience Production Agent:

* You can also use the [Experience Production Agent Workbook](https://www.adobe.com/go/aem-epa-workbook) for guided, hands-on instructions.
