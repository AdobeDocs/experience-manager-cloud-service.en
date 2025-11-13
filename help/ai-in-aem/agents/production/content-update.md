---
title: Content Update Skill
description: Learn what the Experience Production Agent's content update skill is and what it can do for you.
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Content Update Skill {#content-update}

The content update skill of the Experience Production Agent automates content production to accelerate everyday tasks for Adobe Experience Manager (AEM) as a Cloud Service. 

## Overview {#overview}

The content update skill transforms the details that you provide into content updates on your page. You supply the URL of a page that needs updating, together with details of what needs updating, and the agent skill completes your task.

## Capabilities {#capabilities}

You can access the content update skill from:

* [Jira](#jira)
* AI Assistant <!-- add link to doc section, or remove -->

## Limitations {#limitations}

<!-- to be completed or removed -->

## Jira {#jira}

Using the content update skill with Jira allows you to create a ticket with simple instructions that automate your edits.

### Activation {#activation}

To activate and gain access to the content update skill for use with Jira you need to email Adobe.

To speed up the process it helps to provide the following information:

* the name of your application
* the URL of your Jira Cloud instance 
* the secret code you generated during the setup of your webhook
* the email addresses of new users to be registered 

### Create a ticket {#create-a-ticket}

Create a Jira ticket. 

There are two essential details needed in the **Description** field of your ticket:

1. The public facing URL of the page you need to edit.

1. The changes needed. 

   Currently the skill supports the following range of formats to describe your changes:

   * Natural Language in the ticket description
     * for example "Change the headline from X to Y"
   * Annotated PDF attached
     * for example, create a PDF of your page and add annotations detailing what you want changed
   * Comments in attached PDF
     * for example, create a PDF of your page and add comments detailing what you want changed
   * Annotated screenshot attached
     * for example, take a screenshot of part of your page and add annotations detailing what you want changed
   * Microsoft Word file attached, containing natural language changes

### Invoke the agent from your ticket {#invoke-the-agent-from-your-ticket}

To use the agent, add a comment to your ticket. In the comment mention the agent with the `@` symbol, together with the command it should execute; for example:

* `@aemagent@adobe.com process`

Currently, the agent understands the commands:

* `process` - process the request
* `cancel` - cancel a processing request
* `retry` - re-process a request
* `feedback` - apply feedback to a generation
  * for example: "update headline to I love AEM!"
* `reprocess` - reprocess the original request

### How the agent interacts {#how-the-agent-interacts}

After you issue a command to the agent, it responds with comments in the Jira. The comments detail the agent's progress, and actions taken.

In the case of a `process` command to trigger updates, the responses might follow the sequence:

* The initial comment confirms that the agent has started.

* Once the task is completed. the agent responds with another comment containing details of the actions taken. 
  * The content updates made by the agent are non-destructive - this means that they are made to a preview instance. 
  * The comment contains links to the updates, so that you can review and publish as required, or assign the Jira to whoever will be responsible.

* The following image shows an example Jira that triggers the `process`command for the content update skill:

  ![Example Jira using the content update skill of the Experience Production Agent](assets/content-update-jira-example.png)
