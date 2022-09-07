---
title: Enabling the Front-End Pipeline
description: Learn how you can enable the front-end pipeline for existing sites to leverage site themes to more quickly customize your site.
feature: Administering
role: Admin
exl-id: 55d54d72-f87b-47c9-955f-67ec5244dd6e
---
# Enabling the Front-End Pipeline {#enable-front-end-pipeline}

Learn how you can enable the front-end pipeline for existing sites to leverage site themes to more quickly customize your site.

## Overview {#overview}

The front-end pipeline is a mechanism that can quickly deploy just the front-end code of your websites based on [site themes](site-themes.md) and [site templates.](site-templates.md)

Instead of deploying the full-stack, only front-end code is handled by this pipeline making the process faster and also allows front-end developers to easily and quickly customize your site without knowledge of AEM.

Sites based on site templates can leverage the front-end pipeline by default. This document describes how you can adapt your existing sites to take advantage of the front-end pipeline.

>[!TIP]
>
>If you are not familiar with the front-end pipeline and how to quickly deploy sites using it and site templates, please review the [Quick Site Creation journey](/help/journey-sites/quick-site/overview.md) for an introduction.

If you have not created your existing site based on site templates and themes, AEM can configure your site to load the themes that are deployed with the Front End Pipeline on top of the existing client libraries.

## Technical Details {#technical-details}

When you activate the front-end pipeline for a site, AEM makes the following changes to your site structure.

* All pages of the site will include one additional CSS and JS file, which can be modified by deploying updates through a dedicated Cloud Manager front-end pipeline.
* The added CSS and JS files will initially be empty, but a "theme sources" folder can be downloaded to bootstrap the folder structure that allows to deploy CSS and JS code updates via that pipeline.
* This change can only be undone by a developer, by deleting the `SiteConfig` and `HtmlPageItemsConfig` nodes that this operation creates below `/conf/<site-name>/sling:configs`.

>[!NOTE]
>
>This action won't automatically convert the existing client libraries of the site to use the font-end pipeline. Moving these sources from the client library folder to the front-end pipeline folder is a task that requires manual work by a front-end developer.

## Requirements {#requirements}

AEM can automatically adapt your existing site to use the front-end pipeline. To be able to do this, your site must use [v2 or newer of the Page Component of the Core Components.](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/components/page.html)

## Enabling Front-End Pipeline {#enabling}

Enabling your site is done from the Sites console using the [Site rail.](site-rail.md)

1. Log into AEM and navigate to your site via **Global Navigation** &gt; **Sites**.
1. Select your site in the console. You must select the root of the site and not any child pages.
1. With your site selected, open the [rail selector](/help/sites-cloud/authoring/getting-started/basic-handling.md#rail-selector) at the left and choose **Site**.
1. In the **Site** rail, click the button **Enable Front End Pipeline**.

   ![Enable front-end pipeline](/help/sites-cloud/administering/assets/enable-front-end-pipeline.png)

1. AEM prompts you to confirm with an overview of the changes that will be made. Confirm and your site is adapted.

Now your site is ready to use the front-end pipeline. To learn more about the front-end pipeline and managing your site theme see:

* [Using the Site Rail to Manage Your Site Theme](site-rail.md)
* [Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) - This documentation journey gives you and beginning-to-end overview of the process of quickly deploying a site using the front-end pipeline and the Quick Site Creation tool.
* [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#front-end) - This document describes the front-end pipeline in the context of the full-stack and web tier pipelines.
