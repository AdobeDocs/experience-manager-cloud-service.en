---
title: Using the Site Rail to Manage Your Site Theme
description: Learn the powerful features of the Site rail to help you easily customize and manage your site theme.
feature: Administering
role: Admin
exl-id: 45785e5a-4fa2-4cf2-a300-f1865f6f5807
---
# Using the Site Rail to Manage Your Site Theme {#site-rail}

Learn the powerful features of the Site rail to help you easily customize and manage your site theme.

## Overview {#overview}

The Site rail allows you to manage the theme and template resources of your site. [Like other rails](/help/sites-cloud/authoring/getting-started/basic-handling.md#rail-selector) such as the Content Tree, References, or Timeline rails, the Site rail is displayed as the leftmost panel in the sites console, displaying information about the selected item. Unlike other rails, the Site rail only applies to Site roots.

The Site rail is used to manage theme and template related information for your site including:

* [Downloading theme sources](#downloading-theme-sources)
* [Downloading template resources such as wireframes](#downloading-template-resources)
* [Viewing and changing theme versions](#theme-vrsions)
* [Enabling the front-end pipeline](#enabling-the-front-end-pipeline)

>[!TIP]
>
>Review the [Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) to familiarize yourself with the Quick Site Creation tool and the front-end pipeline to easily customize your site theme.

## Downloading Theme Sources {#downloading-theme-sources}

When you create a site in AEM based on a [site template,](site-templates.md) you can download your [site theme](site-themes.md) using the Site rail.

With the Site rail showing in the sites console, select the root of your site to reveal theme information about the site.

![Download theme sources](/help/sites-cloud/administering/assets/download-theme-wireframe.png)

Tap or click **Download Theme Sources** to download a local copy of the site theme as `.zip` file for customization purposes.

## Downloading Template Resources {#downloading-template-resources}

[Site templates](site-templates.md) can contain information in addition to your site content structure and [site theme.](site-themes.md) Site templates can contain wireframe designs or other site-related files for example.

If your site is based on a site template, with the Site rail showing in the sites console, select the root of your site to reveal theme information about the site, including additional site resources.

![Download theme sources](/help/sites-cloud/administering/assets/download-theme-wireframe.png)

Tap or click the button or buttons below the heading **Download additional template resources** to download a local copy of the available files.

## Viewing and Changing Theme Versions {#them-versions}

If your site is based on a site template, it is possible that its theme has already been customized by your front-end developer. Using the Site rail, you can view which version of the site theme is currently deployed and switch to previous versions.

With the Site rail showing in the sites console, select the root of your site to reveal theme information about the site.

![Site versions in the rail](/help/sites-cloud/administering/assets/theme-versions.png)

The current version of the theme is displayed with its commit hash along with timestamp of its last update.

Tap or click on **Select Version** to view previous versions of the theme.

![Select theme version](/help/sites-cloud/administering/assets/select-theme-versions.png)

Tap or click the version you wish to change to and then tap or click **Apply** to make the change.

If AEM detects that a newer version of the theme has been deployed via the front-end pipeline but not applied to your site, a notification icon will display.

![Newer version of theme indicator](/help/sites-cloud/administering/assets/new-theme-version.png)

You can use the **Select Version** button to update to the new theme version.

## Enabling the Front-End Pipeline {#enabling-front-end-pipeline}

If your site was not created using a site template, it is not possible to use the front-end pipeline to customize and deploy its theme.

However you can enable the front-end pipeline for your site using the Site rail.

With the Site rail showing in the sites console, select the root of your site to reveal theme information about the site and then tap or click **Enable Front End Pipeline**.

![Enabling front-end pipeline](/help/sites-cloud/administering/assets/enable-fep.png)

For more information, see the document [Enabling the Front-End Pipeline.](enable-front-end-pipeline.md)
