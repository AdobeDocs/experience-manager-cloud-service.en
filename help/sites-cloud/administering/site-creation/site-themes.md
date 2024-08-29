---
title: Site Themes
description: Learn how AEM site themes can be used to customize the style and design of your site.
feature: Administering
role: Admin
exl-id: 53d4afb3-d091-47a1-ba12-5bcec99f46b9
solution: Experience Manager Sites
---
# Site Themes {#site-themes}

Learn how AEM site themes can be used to customize the style and design of your site.

## Overview {#overview}

An AEM site theme is a package containing the CSS, JavaScript, and static resources that define the styling of your AEM site and complies with the structure of an AEM site theme.

Sites created with AEM site templates allow for the easy download, customization, and redeployment of the themes.

>[!NOTE]
>
>AEM site themes should not be confused with [AEM site templates](site-templates.md). AEM site themes only contain the styling information for an AEM site. AEM site templates define site structure and initial content, and contain an AEM site theme to allow for [quick site creation](create-site.md).

## Using Site Themes {#using-themes}

Site themes are used in two different ways:

* They are used as part of a site template to define styling when [creating a site.](create-site.md)
* They are downloaded after creating a site based on a site template so a front-end developer can further customize the styling.

>[!TIP]
>
>An end-to-end description of the process of creating a site from a template and customizing its theme can be found in the [Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md).

## Site Theme Structure {#structure}

Site themes are simply packages with a logical structure that clearly reflects the purpose of the package content. For a typical front-end project, Adobe recommends the following structure for a site theme:

* `src/theme.ts`: The main entry point of your JS & CSS theme
* `src/site`: JS & CSS files that apply to the entire site
* `src/components`: JS & CSS files specific to AEM components
* `src/resources`: Static files like icons, logos, and fonts

Depending on specific project needs, your theme structure may vary as long the main entry point, `src/theme.ts`, is preserved.

## Standard Site Theme {#standard-site-theme}

Adobe provides a best-practices reference theme that you can use as a basis for creating your own theme. [The Standard Site Theme is available on GitHub](https://github.com/adobe/aem-site-template-standard/tree/main/theme).

## Developing Site Themes {#developing-themes}

Adobe provides an AEM Site Theme Builder as a set of scripts for creating new site themes.

[The AEM Site Theme Builder is available along with usage documentation on GitHub](https://github.com/adobe/aem-site-theme-builder). Front-end development experience is required for customizing the theme.
