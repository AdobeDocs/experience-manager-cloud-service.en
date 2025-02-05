---
title: Organizing Pages
description: Learn how to organize your website with AEM.
exl-id: c57096ca-34fe-4b19-98e0-8f3cd43cf24e
solution: Experience Manager Sites
feature: Authoring
role: User
---

# Organizing Pages {#creating-and-organizing-pages}

Learn how to organize your website with AEM. Once you understand how you need to organize your pages, you can [create new pages](/help/sites-cloud/authoring/sites-console/creating-pages.md) and [manage exiting pages](/help/sites-cloud/authoring/sites-console/managing-pages.md).

{{edge-delivery-authoring}}

## Organizing your Site {#organizing-your-site}

As an author, you need to organize your site within AEM. This involves creating and naming your content pages so that:

* You can easily find them on the author environment
* Visitors to your site can easily browse them on the publish environment

You can also use [folders](#creating-a-new-folder) to help organize your content.

The structure of a website can be thought of as a tree that holds your content pages. The names of these content pages are used to form the URLs, whereas the titles are shown when the page content is viewed.

The following shows an example from the [WKND Tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/overview.html) site, where an article about skateparks (`la-skateparks`) is accessed:

`http://<host>:<port>/editor.html/content/wknd/en/sports/la-skateparks.html`

```xml
 /content
 /wknd
  /en
   /music
    /...
   /sports
    /la-skateparks
    /five-gyms-la
    /mountain-bike-routes
   /shopping
    /...
   /art
    /...
   /...
```

This structure can be viewed From the [**Sites** console](/help/sites-cloud/authoring/sites-console/introduction.md), where you can navigate through the pages of your website and perform actions on the pages.

## Page Naming Conventions {#page-naming-conventions}

When creating a page there are two keys fields:

* **[Title](#title)**:
  * This is displayed to the user in the console and shown at the top of the page content when editing.
  * This field is mandatory.
* **[Name](#name)**:
  * This is used to generate the URI.
  * User input for this field is optional. If not specified, the name is derived from the title. See the following section [Page Name Restrictions and Best Practices](#page-name-restrictions-and-best-practices) for details.

### Page Name Restrictions and Best Practices {#page-name-restrictions-and-best-practices}

The page **Title** and **Name** can be created separately but are related:

* When creating a page, only the **Title** field is required. If no **Name** is provided at page creation, AEM will generate a name from the first 64 characters of the title (observing the validation set out below). Only the first 64 characters are used to support the best practice of short page names.
* If a page name is manually specified by the author, the 64 character limit does not apply, however other technical limitations on the page name length may.

>[!TIP]
>
>When defining a page name, a good rule-of-thumb is to keep the page name as brief but as expressive and memorable as possible to make it easy to understand for the reader. See the [W3C style guide](https://www.w3.org/Provider/Style/TITLE.html) for the `title` element for more information.
>
>Also keep in mind that some browsers (for example, older versions of IE) can only accept URLs up to a certain length, so there is also technical reason to keep page names short.

When creating a page, AEM [validates the page name according to the conventions](/help/implementing/developing/introduction/naming-conventions.md) imposed by AEM and the JCR.

The minimum allowed characters are:

* `a` through `z`
* `A` through `Z`
* `0` through `9`
* `_` (underscore)
* `-` (hyphen/minus)

Full details of all characters allowed can be found in [the naming conventions](/help/implementing/developing/introduction/naming-conventions.md).

>[!NOTE]
>
>Page names are limited to 150 characters.

### Title {#title}

If you supply only a page **Title** when creating a page, AEM derives the page **Name** from this string and [validate the name according to the conventions](/help/implementing/developing/introduction/naming-conventions.md) imposed by AEM and JCR.

A **Title** field containing invalid characters is accepted, but the name derived has the invalid characters substituted. For example:

| Title |Derived Name |
|---|---|
|Schön|`schoen.html`|
|SC%&&#42;ç+|`sc---c-.html` |

### Name {#name}

When you supply a page **Name** when creating a page, AEM [validates the name according to the conventions](/help/implementing/developing/introduction/naming-conventions.md) imposed by AEM and JCR. You cannot submit invalid characters in the **Name** field. When AEM detects invalid characters, the field is highlighted with an explanatory message.

![Example of entering an invalid page name](/help/sites-cloud/authoring/assets/organizing-invalid-name.png)

>[!TIP]
>
>You should avoid using a two-letter code as defined by ISO-639-1 as a page name, unless it is a language root.
>
>See [Preparing Content for Translation](/help/sites-cloud/administering/translation/preparation.md) for more information.

## Templates {#templates}

In AEM, a [template](/help/sites-cloud/authoring/page-editor/templates.md) is a specialized type of page used as the basis for any new page being created.

The template defines the structure of a page including a thumbnail image and other properties. For example, you may have separate templates for product pages, sitemaps, and contact information. Templates are comprised of [components](#components).

AEM comes with several templates provided out-of-the-box. The templates available depend on the individual website. The key fields are:

* **Title** - The title displayed on the resulting web-page
* **Name** - Used when naming the page
* **Template** - A list of templates available for use when generating the new page

## Components {#components}

[Components](/help/implementing/developing/components/overview.md) are the elements provided by AEM so that you can add specific types of content. AEM comes with a range of out-of-the-box components, called [the Core Components](/help/implementing/developing/components/overview.md#core-components), that provide comprehensive functionality. Some examples of the components are:

* Text
* Image
* Title
* Carousel
* And many more

Once you have created and opened a page you can [add content using the components](/help/sites-cloud/authoring/page-editor/edit-content.md#inserting-a-component), which are available from the [component browser](/help/sites-cloud/authoring/page-editor/editor-side-panel.md#components-browser).

>[!TIP]
>
>The [Components Console](/help/sites-cloud/authoring/components-console.md) give an overview of the components on your instance.
