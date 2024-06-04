---
title: Customizing Views of Page Properties
description: Learn how to page properties are viewed and edited by authors.
exl-id: 363b3c2d-f965-485f-bdae-2ea5b4cecb83
feature: Developing
role: "Admin, Architect, Developer"
---
# Customizing Views of Page Properties{#customizing-views-of-page-properties}

Every page has a set of [properties](/help/sites-cloud/authoring/sites-console/page-properties.md) that can be viewed and edited by users. Some are required when creating the page (create view), others can be viewed and edited (edit view) at a later stage. These page properties are defined and made available by the dialog (`cq:dialog`) of the appropriate page component.

The default state for every page property is:

* Hidden in the create view (for example, **Create Page** wizard)

* Available in the edit view (for example, **View Properties**)

Fields must be specifically configured if any change is required. This is done using the appropriate node properties:

* Page property to be available in the create view (for example, **Create Page** wizard):

    * Name: `cq:showOnCreate`
    * Type: `Boolean`

* Page property to be available in the edit view such as the **View**/**Edit**  **Properties** option:

    * Name: `cq:hideOnEdit`
    * Type: `Boolean`

>[!TIP]
>
>See the [Extending Page Properties tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/sites/developing/page-properties-technical-video-develop.html) for a guide to customizing page properties.

## Configuring Your Page Properties {#configuring-your-page-properties}

You can also configure the fields available by configuring the dialog of your page component and applying the appropriate node properties.

For example, by default the [**Create Page** wizard](/help/sites-cloud/authoring/sites-console/creating-pages.md#creating-a-new-page) shows the fields grouped under **More Titles and Description**. To hide these you configure:

1. Create your page component under `/apps`.
1. Create an override (using *dialog diff* provided by the [Sling Resource Merger](/help/implementing/developing/introduction/sling-resource-merger.md)) for the `basic` section of your page component; for example:

   ```xml
   <your-page-component>/cq:dialog/content/items/tabs/items/basic
   ```

1. Set the `path` property on `basic` to point to the override of the basic tab (see the next step as well). For example:

   ```xml
   /apps/demos/components/page/tabs/basic
   ```

1. Create an override of the `basic` - `moretitles` section at the corresponding path; for example:

   ```xml
   /apps/demos/components/page/tabs/basic/items/column/items/moretitles
   ```

1. Apply the appropriate node property:

    * **Name**: `cq:showOnCreate`
    * **Type**: `Boolean`
    * **Value**: `false`

   The **More Titles and Description** section will no longer be shown in the **Create Page** wizard.

>[!NOTE]
>
>When configuring page properties for use with live copies, see [Extending the Multi Site Manager](/help/implementing/developing/extending/msm.md#configuring-msm-locks-on-page-properties) for more details.

## Sample Configuration of Page Properties {#sample-configuration-of-page-properties}

This sample demonstrates the dialog diff technique of the [Sling Resource Merger](/help/implementing/developing/introduction/sling-resource-merger.md) including use of [`sling:orderBefore`](/help/implementing/developing/introduction/sling-resource-merger.md#properties). It also illustrates use of both `cq:showOnCreate` and `cq:hideOnEdit`.

You can find the code of this page on [GitHub](https://github.com/Adobe-Marketing-Cloud/aem-authoring-extension-page-dialog).
