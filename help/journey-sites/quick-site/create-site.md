---
title: Create Site from Template
description: Learn how to quickly create a new AEM site using a site template.
index: no
hide: yes
hidefromtoc: yes
---

# Create Site from Template {#create-site-from-template}

Learn how to quickly create a new AEM site using a site template.

>[!CAUTION]
>
>The Quick Site Creation tool is currently a tech preview. It is made available for testing and evaluation purposes and is not intended for production use unless agreed with Adobe Support.

## The Story So Far {#story-so-far}

In the previous document of the AEM Quick Site Creation journey, [Understand Cloud Manager and the Quick Site Creation Workflow,](cloud-manager.md) you learned about Cloud Manager and how it ties together the new Quick Site Creation process and you should now:

* Understand how AEM Sites and the Cloud Manager work together to facilitate front-end development
* See how the front-end customization step is entirely decoupled from AEM and requires no AEM knowledge.

This article builds on those fundamentals so you can take the first configuration step and create a new site form a template which you can then later customize using front-end tools.

## Objective {#objective}

This document helps you understand how to quickly create a new AEM site using a site template. After reading you should:

* Understand how to obtain AEM Site templates.
* Learn how to create a new site using a template.
* See how to download the template from your new site to provide to the front-end developer.

## Site Templates {#site-templates}

Site templates are a simple way to combine basic site content into a convenient and reusable package. Site templates generally contain base site content and structure as well as site styling information to get new site started quickly. The actual structure is as follows:

* `files`: Folder with the UI kit XD file and possibly other files.
* `previews`: Folder with screenshots of the site template.
* `site`: Content package of the content that is copied for each site created from this template (templates, pages, etc.).
* `theme`: Sources of the template theme to modify how the site looks (CSS, JS, etc.).

Templates are powerful because they are reusable so that your content authors can quickly create a site. And since you can have multiple templates available in your AEM installation, you have the flexibility to meet various business needs.

>[!TIP]
>
>The site template is not to be confused with page templates. Site templates described here define the overall structure of a site. A page template defines the structure and initial content of an individual page.

## Obtaining a Site Template {#obtaining-template}

The simplest way to get started is to [download the latest AEM Standard Site Template from its GitHub repository.](https://github.com/adobe/aem-site-template-standard)

Once downloaded you can upload it to your AEM environment.

>[!TIP]
>
>The AEM Standard Site Template can be customized to meet your project's needs. However this topic is beyond the scope of this journey. Please refer to the GitHub documentation of the Standard Site Template for more information.

>[!TIP]
>
>You can also choose to build the template from source as part of your project workflow. However this topic is beyond the scope of this journey. Please refer to the GitHub documentation of the Standard Site Template for more information.

## Installing a Site Template {#installing-template}

Using a template to create a new site is very easy.

1. Sign into your AEM authoring environment and navigate to the Sites console

   * `https://<your-author-environment>.adobeaemcloud.com/sites.html/content`

1. Tap or click **Create** at the top-right of the screen and from the drop-down menu select **Site from template**.

   ![Creating a new site from a template](assets/create-site-from-template.png)

1. In the Create Site wizard, tap or click on **Import** at the top of the left column.

   ![Site creation wizard](assets/site-creation-wizard.png)

1. In the file browser, locate the template [you downloaded previously](#obtaining-template) and tap or click **Upload**.

1. Once uploaded, it appears in the list of available templates. Tap or click on it to select it (which also reveals information about the template in the right column) and then tap or click **Next**.

   ![Select a template](assets/select-site-template.png)

1. Provide a title for your site. A site name can be provided or will be generated from the title if omitted.

   * The site title appears in the browsers title bar.
   * The site name becomes part of the URL.

1. Tap or click **Create** and the new site is created from the site template.

   ![Details of the new site](assets/create-site-details.png)

1. In the confirmation dialog that appears, tap or click **Done**.

   ![Success dialog](assets/success.png)

1. In the sites console, the new sites is visible and can be navigated to explore its basic structure as defined by the template.

   ![New site structure](assets/new-site.png)

Content authors can now begin authoring.

## Example Page {#example-page}

The front-end developer may not be familiar with the details of your content. Therefore it is a good idea to provide the developer with a path to typical content that can be used as a base of reference as the theme is customized. A typical example is the home page for the master language of the site.

1. In the sites browser, navigate to the home page of the master language of the site and then tap or click the page to select it and then tap or click **Edit** in the menu bar.

   ![Typical home page](assets/home-page-in-console.png)

1. In the editor, select the **Page Information** button in the toolbar and then **View as published**.

   ![Editing the home page](assets/home-page-edit.png)

1. In the tab that opens, copy the path of the content from the address bar. It will look something like `/content/<your-site>/en/home.html?wcmmode=disabled`.

   ![Home page](assets/home-page.png)

1. Save the path to later provide to the front-end developer.

## Download the Theme {#download-theme}

Now that the site has been created, the theme of the site as generated by the template can be downloaded and provided to the front-end developer for customization.

1. On the sites console, show the **Site** rail.

   ![Show sites rail](assets/show-site-rail.png)

1. Tap or click the root of your new site and then tap or click **Download Theme Sources** in the site rail.

   ![Download theme sources](assets/download-theme-sources.png)

You now have a copy of the theme source files in your download files.

## Set Up Proxy User {#proxy-user}

In order for the front-end developer to preview the customizations using actual AEM content from your site, you must set up a proxy user.

1. In AEM from main navigation go to **Tools** -&gt; **Security** -&gt; **Users**.
1. In the user management console, tap or click **Create**.

   ![User management console](assets/user-management-console.png)
1. In the **Create New User** window you must at a minimum provide:
   * **ID** - Take note of this value as you must provide it to the front-end developer.
   * **Password** - Save this value securely in a password vault as you must provide it to the front-end developer.

   ![New user details](assets/new-user-details.png)

1. On the **Groups** tab, add the proxy user to the `contributors` group.
   * Typing in the term `contributors` triggers AEM's auto-completion feature for simple selection of the group.

   ![Add to group](assets/add-to-group.png)

1. Tap or click **Save &amp; Close**.

You now have completed the configuration and have all the information that the front-end developer needs.

## Handover to Front-End Developer {#handover}

You can now provide the front-end developer the necessary information to begin customization.

* The git credentials you saved [when setting up the pipeline](pipeline-setup.md#repo-access)
* A [path to typical content](#example-page)
* The theme source that [you just downloaded](#download-theme)
* The [proxy user credentials](#proxy-user)
* Your front-end design requirements

Content authors can continue to create content on the site as the front-end developer starts customizing the theme in the next step of the journey.

## What's Next {#what-is-next}

Now that you have completed this part of the AEM Quick Site Creation journey you should:

* Understand how to obtain AEM Site templates.
* Learn how to create a new site using a template.
* See how to download the template from your new site to provide to the front-end developer.

Build on this knowledge and continue your AEM Quick Site Creation journey by next reviewing the document [Set Up Your Pipeline,](pipeline-setup.md) where you will create a front-end pipeline to manage the customization of your site's theme.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the Quick Site Creation journey by reviewing the document [Set Up Your Pipeline,](pipeline-setup.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the journey.

* [AEM Standard Site Template](https://github.com/adobe/aem-site-template-standard) - This is the GitHub repository of the AEM Standard Site template.
* [Creating and Organizing Pages](/help/sites-cloud/authoring/fundamentals/organizing-pages.md) - This guide details how to manage pages of your AEM Site if you wish to customize it further after creating it from the template.
