---
title: Templates to Create Pages that are Editable with the Universal Editor
description: Learn how to create templates that can be used to create pages that are editable with the Universal Editor, saving time and ensuring consistent branding.
solution: Experience Manager Sites
feature: Authoring
role: User
exl-id: f0d60086-e92e-4492-ad50-bef84fed2a82
---

# Templates to Create Pages that are Editable with the Universal Editor {#page-templates}

Learn how to create templates that can be used to create pages that are editable with the Universal Editor, saving time and ensuring consistent branding.

>[!NOTE]
>
>[Templates are also available for creating pages that are editable with the Page Editor](/help/sites-cloud/authoring/page-editor/templates.md).

## What are Page Templates? {#what-are}

Branding and marketing guidelines often dictate particular layouts for your content pages. It is also often a practical reality that many of your pages will share the same structure and layout. To save your content authors time, pages can be created from templates.

Page templates serve as master copies of your page layouts. When you create a page from a template, the initial content of the template is copied to the new page, helping to predefine the basic layout and content of the page for the content author, saving them time.

## Enabling Page Templates {#enabling-templates}

In order to use templates to creating pages that are editable with the Universal Editor, you must enable the option.

First enable editable templates for your site's configuration.

1. Use the **Sites** console and [select the root of your site](/help/sites-cloud/authoring/sites-console/introduction.md#selecting-resources).
1. Once the site root is selected, tap or click the [**Properties** icon](/help/sites-cloud/authoring/sites-console/page-properties.md) in the toolbar.
1. On the **Advanced** tab of the properties dialog take note of the value in the **Cloud Configuration** field.
1. From the main navigation, choose **Tools** -&gt; **General** -&gt; **Configuration Browser**.
1. In the **[Configuration Browser](/help/implementing/developing/introduction/configurations.md)**, select the configuration you noted in the previous step and tap or click **Properties** in the toolbar.
1. In the **Configuration Properties** window, check the option **Editable Templates**.
1. Tap or click **Save &amp; Close**.

Once the configuration is enabled, you must allow templates for your site.

1. Use the **Sites** console and [select the root of your site](/help/sites-cloud/authoring/sites-console/introduction.md#selecting-resources).
1. Once the site root is selected, tap or click the [**Properties** icon](/help/sites-cloud/authoring/sites-console/page-properties.md) in the toolbar.
1. On the **Advanced** tab of the properties dialog under the **Template Settings** section, tap or click the **Add** button.
1. In the new, empty field that appears under **Allowed Templates**, add the path `/conf/<site>/settings/wcm/templates/.*`.
1. Tap or click **Save &amp; Close**.

You can now use templates to create pages for your site. This task must only be done once every site/configuration where you wish to use templates when creating pages that are editable with the Universal Editor.

## Creating a New Template {#create-new}

You can either [create a new page](/help/sites-cloud/authoring/sites-console/creating-pages.md) to serve as a template or use an existing page as the base of a template.

1. Use the **Sites** console to [navigate to the new or existing page](/help/sites-cloud/authoring/sites-console/introduction.md#selecting-resources) that you wish to use as a template and tap or click it to select it.

1. Once the page is selected, tap or click the [**Properties** icon](/help/sites-cloud/authoring/sites-console/page-properties.md) in the toolbar.

1. On the **Advanced** tab of the properties dialog under the **Template Settings** section, select the toggle **Use Page as Template**.

1. Tap or click **Save &amp; Close**.

Your new page can now be used as a template when creating new pages.

## Creating a Page from a Template {#creating-from-template}

Creating a page from a template that is editable with the Universal Editor is the same workflow as [creating any other page](/help/sites-cloud/authoring/sites-console/creating-pages.md).

1. Use the **Sites** console to [navigate to the location](/help/sites-cloud/authoring/sites-console/introduction.md#selecting-resources) where you wish to create the new page.

1. Tap or click **Create** -&gt; **Page**.

1. On the **Template** tab of the **Create Page** wizard, you can select on which template you wish to base your new page. Tap or click the desired template to select it and then tap or click **Next**.

Complete the wizard as you would for any other page and you have created your new page based on the selected template.

## Pages and Templates {#pages-vs-templates}

Page templates only define the initial content of pages. Pages are then entirely editable with the Universal Editor.

* Pages created from pages templates are independent copies of the template.
* If the template changes, the existing pages based on that template do not change.
* The content author can modify and update the content of the resulting page as necessary with no restrictions from the template.

## Editable Templates {#editable-templates}

Pages created with the [Page Editor](/help/sites-cloud/authoring/page-editor/introduction.md) can also be based on templates. Templates used to create pages for the Universal Editor and the Page Editor both leverage AEM's [editable templates](/help/implementing/developing/components/templates.md).

Templates used to create pages editable with the Page Editor make use of all features of editable templates. Templates usd to create pages editable with the Universal Editor only use the initial content feature.
