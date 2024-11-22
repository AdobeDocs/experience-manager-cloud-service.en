---
title: Repoless Multi Site Management
description: Learn best practice recommendations on how to set up a project with multilingual sites leveraging a single code base in a repoless manner.
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Repoless Multi Site Management {#repoless-msm}

This document assumes that you have already created a base site for your project called `my-aem-site` and you wish to localize it using AEM's MSM feature.

If you have set up your project already for the repoless use case, the cloud configuration is assigned at the level of the root page, `/content/my-aem-site`. For multilingual sites, this configuration assignment must be changed to the language root such as `/content/my-aem-site/language-master/de`.

