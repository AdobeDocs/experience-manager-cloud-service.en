---
title: Repoless Multi Site Management
description: Learn best practice recommendations on how to set up a project in a repoless manner with localized sites that leverage a single code base, each served up by Edge Delivery Services. 
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Repoless Multi Site Management {#repoless-msm}

Learn best practice recommendations on how to set up a project in a repoless manner with localized sites that leverage a single code base, each served up by Edge Delivery Services. 

## Overview {#overview}

[Multi Site Manager (MSM)](/help/sites-cloud/administering/msm/overview.md) and its Live Copy features enable you to use the same site content in multiple locations, while allowing for variations. You can author content once and create Live Copies. MSM maintains live relationships between your source content and its Live Copies so that when you change the source content, the source and Live Copies are synchronized.

You can use MSM to create an entire content structure for your brand across locales and languages, authoring the content centrally. Your localized sites can then each be delivered by Edge Delivery Services, leveraging a central code base.

## Requirements {#requirements}

To configure the MSM repoless use case you must first complete a number of tasks.

* This document assumes that you have already created a site for your project based on the [Developer Getting Started Guide for WYSIWYG Authoring with Edge Delivery Services](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md) guide.
* You must have already [enabled the repoless feature for your project.](/help/edge/wysiwyg-authoring/repoless.md)

## Use Case {#use-case}

This document assumes that you have already created a basic localized site structure for your project. It uses the following structure for the wknd brand as an example.

