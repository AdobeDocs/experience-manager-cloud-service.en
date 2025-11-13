---
title: Content Update Skill
description: Learn what the Experience Production Agent's content update skill is and what it can do for you.
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Content Update Skill {#content-update}

The Content Update Skill of the Experience Production Agent automates content production to accelerate everyday tasks for the CMS. 

## Overview {#overview}

You can access the Content Updater from:

* [Jira](#jira)
* AI Assistant

## What the skill does {#what-the-skill-does}

## Jira {#jira}

Using the Content Update skill with Jira allows you to create a ticket with simple instructions that automate your edits.

## Activation {#activation}

To activate and gain access to the Content Update skill for use with Jira you need to email Adobe at `aemagent@adobe.com`.

To speed up the process it helps to provide the following information:

* the name of your application
* the URL of your Jira Cloud instance 
* the secret code you generated during the setup of your webhook
* the email addresses of new users to be registered 

## Use {#use}

There are several steps for using the agent with Jira:

* [Create a Jira ticket with your requirements](#create-a-ticket)
* [Invoke the agent to realize your request](#invoke-the-agent)

### Create a ticket {#create-a-ticket}

Create a ticket. There are two essential details needed in a ticket:

1. The public facing URL of the page you need to edit.

1. The changes needed. 

   Currently we support the following range of formats to describe changes needed:

   * Natural Language in the ticket description
     * for example "Change the headline from X to Y"
   * Annotated PDF 
   * Comments in PDF
   * Annotated screenshot
   * Word file attached with natural language changes

### Invoke the agent {#invoke-the-agent}

To use the agent, mention the agent with the `@` symbol. 

Currently, there are only certain commands the agent understands:

* `process` - process the request
* `cancel` - cancel a processing request
* `retry` - re-process a request
* `feedback` - apply feedback to a generation
  * for example: "update headline to I love AEM!"
* `reprocess` - reprocess the original request

The following image shows an example Jira that uses the Content Update skill:

![Example Jira using the Content Update skill of the Experience Production Agent](assets/content-update-jira-example.png)
