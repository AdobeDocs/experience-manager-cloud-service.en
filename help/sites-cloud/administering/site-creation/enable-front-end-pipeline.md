---
title: Enabling the Front-End Pipeline
description: Learn how you can enable the front-end pipeline for existing sites to use site themes to customize your site more quickly.
feature: Administering
role: Admin
exl-id: 55d54d72-f87b-47c9-955f-67ec5244dd6e
solution: Experience Manager Sites
---
# Enabling the Front-End Pipeline {#enable-front-end-pipeline}

Learn how you can enable the front-end pipeline for existing sites to use site themes to customize your site more quickly.

## Overview {#overview}

The front-end pipeline is a mechanism that can quickly deploy just the front-end code of your websites based on [site themes](site-themes.md) and [site templates](site-templates.md).

This pipeline handles only front-end code, making the deployment process faster than full-stack deployments. It allows front-end developers to customize your site easily without needing knowledge of AEM.

Sites based on site templates can use the front-end pipeline by default. This document describes how you can adapt your existing sites to take advantage of the front-end pipeline.

>[!TIP]
>
>If you are not familiar with the front-end pipeline and how to deploy sites quickly using it and site templates, see [Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) for an introduction.

AEM can configure your site to load themes deployed with the Front End Pipeline, even if your site was not created using site templates and themes, by layering them on top of existing client libraries.

## Technical Details {#technical-details}

When you activate the front-end pipeline for a site, AEM makes the following changes to your site structure.

* All pages of the site include one additional CSS and JS file, which can be modified by deploying updates through a dedicated Cloud Manager front-end pipeline.
* The added CSS and JS files are empty initially. However, you can download a "theme sources" folder to set up the folder structure needed to deploy CSS and JS code updates through the pipeline.
* Only a developer can undo the change, by deleting the `SiteConfig` and `HtmlPageItemsConfig` nodes that this operation creates below `/conf/<site-name>/sling:configs`.

>[!NOTE]
>
>This action does not automatically convert the existing client libraries of the site to use the font-end pipeline. Moving these sources from the client library folder to the front-end pipeline folder is a task that requires manual work by a front-end developer.

## Requirements {#requirements}

AEM can automatically adapt your existing site to use the front-end pipeline. To be able to do this workflow, your site must use [v2 or newer of the Page Component of the Core Components](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/wcm-components/page).

## Enabling Front-End Pipeline {#enabling}

{{add-cm-allowlist-frontend-pipeline}}

Enabling your site is done from the Sites console using the [Site rail](site-rail.md). 

1. Log into AEM and navigate to your site via **Global Navigation** &gt; **Sites**.
1. Select your site in the console. Select the root of the site and not any child pages.
1. With your site selected, open the [rail selector](/help/sites-cloud/authoring/basic-handling.md#rail-selector) at the left and choose **Site**.
1. In the **Site** rail, click the button **Enable Front End Pipeline**.

   ![Enable front-end pipeline](/help/sites-cloud/administering/assets/enable-front-end-pipeline.png)

1. AEM prompts you to confirm with an overview of the changes that are made. Confirm and your site is adapted.

Now, your site is ready to use the front-end pipeline. To learn more about the front-end pipeline and managing your site theme see:

* [Using the Site Rail to Manage Your Site Theme](site-rail.md)
* [Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) - This documentation journey gives you and beginning-to-end overview of the process of quickly deploying a site using the front-end pipeline and the Quick Site Creation tool.
* [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#front-end) - This document describes the front-end pipeline in the context of the full-stack and web tier pipelines.

## Front-End Pipeline and Custom Domains {#custom-domains}

As described in the [Technical Details](#technical-details) section, activating the Front-End Pipeline feature for a site creates a `SiteConfig` and `HtmlPageItemsConfig` nodes below `/conf/<site-name>/sling:configs`.

If you wish to use [Cloud Manager's custom domains feature](/help/implementing/cloud-manager/custom-domain-names/introduction.md) for your site along with the Front End Pipeline, additional properties must be added to these nodes.

1. Set the `customFrontendPrefix` property in `SiteConfig` for the site.
1. This updates the `prefixPath` value of the `HtmlPageItemsConfig` with the custom domain.

Pages for the site then reference theme artifacts from that updated URL.
