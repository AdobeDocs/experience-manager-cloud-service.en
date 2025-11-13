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

## Jira {#jira}

## Activation {#activation}

## Use {#use}

### Create a ticket {#create-a-ticket}

Create a ticket. There are 2 main things needed in a ticket:

1. The public facing URL of the page you are needing to edit

1. The changes needed. Its our vision to allow users to provide a wide range of formats to describe changes needed. However, currently this is what we support:

   * Natural Language in the ticket description example "Change the headline from X to Y"
   * Annotated PDF (see video above)
   * Comments in PDF
   * Annotated screenshot
   * Word file attached with natural language changes

### Invoke the agent {#invoke-the-agent}

To use the agent, mention the agent with the @ symbol. Currently, there are only certain commands the agent understands:

* process - process the request
* cancel - cancel a processing request
* retry - re-process a request
* feedback: apply feedback to a generation, for example: "update headline to I love AEM!"
* reprocess - reprocess the original request

![Example Jira using the Content Update skill of the Experience Production Agent](assets/content-update-jira-example.png)
