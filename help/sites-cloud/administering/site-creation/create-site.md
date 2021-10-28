---
title: Creating a New Site
description: Learn how to use AEM to create a new site using site templates to define the style and structure of your site.
feature: Administering
role: Admin
---

# Creating a New Site {#new-site}

Learn how to use AEM create a new site using site templates to define the style and structure of your site.

## Overview {#overview}

Before content authors can create pages with new content, the site must first be created. This is generally performed by an AEM administrator who defines the initial structure of the site. Site creation through the use of site templates makes the process fast and flexible.

## Planning Site Structure {#structure}

You should take time to consider your site's purpose and planned content well in advance. This will drive how you design the structure of the site. A good site structure supports easy navigation and content discovery for your site visitors as well as supports various AEM features such as [multi site management and translation.](/help/sites-cloud/administering/msm-and-translation.md)

>[!TIP]
>
>[The WKND reference site](https://wknd.site) provides a best-practices implementation of a fully-functional outdoor experiences brand website. Explore it to see how a well-built AEM site is structured.

## Site Templates {#site-templates}

Because site structure is so important to the success of a site, it is convenient to have predefined structures available to quickly deploy a new site based on a set of existing standards. Site templates are a way to combine basic site content into a convenient and reusable package.

Site templates generally contain base site content and structure as well as site styling information to get new site started quickly. Templates are powerful because they are reusable as well as customizable. And since you can have multiple templates available in your AEM installation, you have the flexibility to create different sites to meet various business needs.

>[!TIP]
>
>For further detail on site templates, please review the [Site Templates](site-templates.md) article.

>[!NOTE]
>
>The site template is not to be confused with page templates. Site templates define the overall structure of a site. A page template defines the structure and initial content of an individual page.

## Creating a New Site {#create-site}

Using a template to create a new site is very easy.

1. Sign into your AEM authoring environment and navigate to the Sites console

   * `https://<your-author-environment>.adobeaemcloud.com/sites.html/content`

1. Tap or click **Create** at the top-right of the screen and from the drop-down menu select **Site from template**.

   ![Creating a new site from a template](../assets/create-site-from-template.png)

1. In the Create Site wizard, tap or click on an existing template in the left panel or on **Import** at the top of the left column to import a new template.

   ![Site creation wizard](../assets/site-creation-wizard.png)

   1. If you chose to import, in the file browser, locate the template you wish to use and tap or click **Upload**.

   1. Once uploaded, it appears in the list of available templates. 
   
1. When selecting a template, it reveals information about the template in the right column. With your desired template selected, tap or click **Next**.

   ![Select a template](../assets/select-site-template.png)

1. Provide a title for your site. A site name can be provided or will be generated from the title if omitted.

   * The site title appears in the browsers title bar.
   * The site name becomes part of the URL.
   * The site name must comply with [AEM's page naming conventions.](/help/sites-cloud/authoring/fundamentals/organizing-pages.md#page-name-restrictions-and-best-practices)

1. Tap or click **Create** and the new site is created from the site template.

   ![Details of the new site](../assets/create-site-details.png)

1. In the confirmation dialog that appears, tap or click **Done**.

   ![Success dialog](../assets/success.png)

1. In the sites console, the new sites is visible and can be navigated to explore its basic structure as defined by the template.

   ![New site structure](../assets/new-site.png)

Content authors can now begin authoring!

## Site Customization {#site-customization}

If your site requires customization beyond the templates available you have a number of options.

* If the site structure or initial content needs to be adjusted, [the site template can be customized to meet your requirements.](site-templates.md)
* If the site styling needs to be adjusted, [the site theme can be downloaded and customized.](/help/journey-sites/quick-site/overview.md)
* If the site functionality needs to be adjusted, [the site can be fully customized.](/help/implementing/developing/introduction/develop-wknd-tutorial.md)

Any customization should be undertaken with the support of a development team.
