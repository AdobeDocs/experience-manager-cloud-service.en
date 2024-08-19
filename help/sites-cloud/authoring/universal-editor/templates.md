---
title: Using Page Templates with the Universal Editor
description: Learn how to create and use page templates with the Universal Editor.
solution: Experience Manager Sites
feature: Authoring
role: User
---

# Using Page Templates with the Universal Editor {#page-templates}

Learn how to create and use page templates with the Universal Editor.

## What are Page Templates? {#what-are}

Branding and marketing guidelines often dictate particular layouts for your content pages. It is also often a practical reality that many of your pages will share the same structure and layout. To save your content authors time, pages can be created from templates.

Page templates serve as master copies of your page layouts. When you create a page from a template, the content of the template is copied to the new page, helping to predefine the layout and initial content of the page for the content author, saving them time.

## Creating a Page Template {#creating}

You can create a page template by creating a new page or by using an existing page to serve as the template. In both cases, you use the [**Sites** Console.](/help/sites-cloud/authoring/sites-console/introduction.md)

### Creating a New Template {#create-new}

1. Use the **Sites** console to navigate to the location where you wish to create the new page that will serve as your template and [create the page as you would any other.](/help/sites-cloud/authoring/sites-console/creating-pages.md)

1. Once the page is created and you return to the console, select the page and then tap or click the [**Properties** icon](/help/sites-cloud/authoring/sites-console/page-properties.md) in the toolbar.

1. On the **Advanced** tab of the properties dialog under the **Template Settings** section, select the toggle **Use as Template**.

1. In the **Template Name** field, provide a descriptive name.

   * This is the name that will show creating new content pages and you select a template on which to base the new page.

1. Tap or click **Save &amp; Close**.

Your new page can now be used as a template when creating new pages.

### Using an Existing Page as a Template {#existing-page}

1. Use the **Sites** console to [navigate to the location of the page](/help/sites-cloud/authoring/sites-console/introduction.md#selecting-resources) you would like to use as a template.

1. Select the page and then tap or click the [**Properties** icon](/help/sites-cloud/authoring/sites-console/page-properties.md) in the toolbar.

1. On the **Advanced** tab of the properties dialog under the **Template Settings** section, select the toggle **Use as Template**.

1. In the **Template Name** field, provide a descriptive name.

   * This is the name that will show creating new content pages and you select a template on which to base the new page.

1. Tap or click **Save &amp; Close**.

The selected page can now be used as a template when creating new pages.

## Creating a Page from a Template {#creating-from-template}

Creating a page from a template for use with the Universal Editor is the same workflow as when [creating the page as you would any other.](/help/sites-cloud/authoring/sites-console/creating-pages.md)

1. Use the **Sites** console to [navigate to the location](/help/sites-cloud/authoring/sites-console/introduction.md#selecting-resources) where you wish to create the new page.

1. Tap or click **Create** -&gt; **Page**.

1. On the **Template** tab of the **Create Page** wizard, you can select on which template you wish to base your new page. Tap or click the desired template to select it and then tap or click **Next**.

Complete the wizard as you would for any other page and you have created your new page based on the selected template.

## Universal Editor and the Page Editor {#page-vs-universal}

Page templates for the Universal Editor solve the same problem as [page templates for the AEM Page Editor:](/help/sites-cloud/authoring/sites-console/templates.md) to be able to reuse content to create pages quickly based on a set of pre-defined layouts. However they solve the problem in very different ways. If you are a user of the Page Editor, please be aware of these differences.

* Pages created from pages templates for the Universal Editor are independent copies of the template.
* Therefore if the template changes, the resulting pages do not change.
* The content author can modify and update the content of the resulting page as necessary with no restrictions from the template.
