---
title: Content Update Job
description: Learn what the Brand Experience Agent's content update job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
exl-id: e2d1dae8-38de-4357-bb14-ad35acb71aee
---

# Content Update Job {#content-update}

The content update job of the [Brand Experience Agent](/help/ai-in-aem/agents/brand-experience/overview.md) automates content production to accelerate everyday tasks for Adobe Experience Manager (AEM) as a Cloud Service and Edge Delivery Services.

## Overview {#overview}

The content update job updates existing content, including content fragments, pages, forms and assets. The job can perform actions such as updating, removing, replacing, or adding content elements to keep experiences accurate and current. Inputs can be natural language description, and when used with Jira PDFs and screenshots can provide input too.

The content update job transforms the details that you provide, either through natural language or visuals, into content updates on your page. You supply the URL of a page that needs updating, together with details of what needs updating, and the agent skill completes your task.

## Capabilities {#capabilities}

You can access the content update skill from:

* [The AI Assistant](#ai-assistant)
* [Jira](#jira)

## AI Assistant {#ai-assistant}

You can access the job in AEM via the AI Assistant. 

Open the AI Assistant from [`experience.adobe.com`,](https://experience.adobe.com) then start interacting by specifying your prompt in natural language using the `Ask AI Assistant anything` field:

![Content Update Job](/help/ai-in-aem/agents/brand-experience/experience-production/assets/content-update-ai-assistant-example.png)

### Sample Prompts {#sample-prompts}

To initiate content updates you can give a wide range of natural language prompts. You also need to specify the public facing URL of the page you want to update. For example:

* Modify the following page `https://www.your-url.com/sale` Update the main hero heading to "Black Friday Mega Sale - Up to 70% Off", Change the countdown timer to show "Ends in 48 Hours", Remove  "Sign up for updates", Change all "Shop Now" buttons to "Grab the Deal""

* `https://www.your-url.com/laptops/your-laptop-model` Update banner copy to "Save 300 USD Today Only", Update pricing from 1,299 USD to 999 USD,  Remove financing option banner

* `https://www.your-url.com/your-sneaker` Update stock status from "Low Stock" to "Back in Stock - Limited Quantities", Change the size selector to highlight available sizes in green, Remove the "Coming Soon" badge

* `https://www.your-url.com/your-sneaker` Update the product images to show new colorways

>[!NOTE]
>
>File uploads can be used when interacting using [Jira](#jira), but are not supported with AI Assistant.

## Jira {#jira}

Using the content update job with Jira allows you to create a ticket with instructions that automate your edits.

### Create a Ticket {#create-a-ticket}

Create a Jira ticket (of any type). There are two essential details needed in the **Description** field of your ticket:

1. The public facing URL of the page you need to edit.

1. The changes needed. 

   The job supports the following range of formats to describe your changes:

   * Natural Language in the ticket description
     * for example "Change the headline from X to Y"
   * Annotated PDF attached
     * for example, create a PDF of your page and add annotations detailing what you want changed
   * Comments in attached PDF
     * for example, create a PDF of your page and add comments detailing what you want changed
   * Annotated screenshot attached
     * for example, take a screenshot of part of your page and add annotations detailing what you want changed
   * Microsoft Word file attached, containing natural language changes

### Invoke the Job from Your Ticket {#invoke-the-job-from-your-ticket}

To use the job, add a comment to your ticket. In the comment mention the job with the `@` symbol, together with the command it should execute; for example:

* `@aemagent@adobe.com process`

Currently, the job understands the commands:

* `process` - process the request
* `cancel` - cancel a processing request
* `retry` - re-process a request
* `feedback` - apply feedback to a previous generation
* `reprocess` - reprocess the original request

### How the Job Interacts {#how-the-agent-interacts}

After you issue a command to the job, it responds with comments in the Jira. The comments detail the job's progress, and actions taken.

In the case of a `process` command to trigger updates, the responses might follow the sequence:

* The initial comment confirms that the job has started.

* Once the task is completed, the job responds with another comment containing details of the actions taken. 
  * The content updates made by the job are non-destructive - this means that they are made to a preview instance. 
  * The comment contains links to the updates, so that you can review and publish as required, or assign the Jira to whoever will be responsible.

* The following image shows an example Jira that triggers the `process`command for the content update job:

  ![Example Jira using the content update job of the Experience Production Agent](assets/content-update-jira-example.png)

## Activation {#activation}

To activate and gain access to the communication creation job you need to contact Adobe. To get started you can either:

* Contact `experience-production-agent@adobe.com`
* Or reach out to your account team

To speed up the process it helps to provide the following information:

* For AEM as a Cloud Service, you need to provide your:
  * Organization ID
  * `product_id` 
  * `profile_id`

  * These values can be found following these steps:
    1. Your administrator needs to visit [`https://adminconsole.adobe.com`](https://adminconsole.adobe.com)
    1. Select **Adobe Experience Manager as a Cloud Service**
    1. Select the appropriate AEM instance
    1. Select the profile that allows read and write operations for the content in question
    1. Grab the browser URL
    1. Extract `product_id` and `profile_id` from the URL. 
      For example, `https://adminconsole.adobe.com/products/profiles/users`

* Edge Delivery Document Authoring
  * Provide your Adobe team with the following information:
    * Relevant domains
    * Relevant Github information:
      * Org
      * Repo
      * Branch

## Limitations {#limitations}

Please be aware of the following limitations:

* File uploads can be used when interacting with [Jira](#jira), but are not supported when interacting with the [AI Assistant.](#ai-assistant)
