---
title: Configuring Bulk Editing of Page Properties
description: Learn how to configure bulk editing so you can edit the properties of multiple pages at once.
exl-id: 0d10c6b9-8643-479d-adc1-4066d227e83d
feature: Developing
role: Admin, Architect, Developer
---
# Configuring Bulk Editing of Page Properties {#configuring-bulk-editing-of-page-properties}

[Bulk editing of page properties](/help/sites-cloud/authoring/sites-console/page-properties.md#from-the-sites-console-multiple-pages) lets you edit the properties of multiple pages at once.

## Considerations {#considerations}

Page properties are not enabled for bulk editing as default. They must be explicitly enabled. When defining the page properties to be available for bulk editing you need to consider certain implications, such as:

* Certain fields are usually unique. You must decide whether it is meaningful to enable such fields for bulk editing, when one value will be applied.
  *  For example, page titles are nearly always unique.
* Certain fields might have multiple values which needs meaningful representation when rendering.
  * For example, a status drop-down labeled **Ready for Publication**. This might have several values before bulk-editing such as **ready**, **in-review**, **in-progress**, and so on.

Because of the possibility of multiple values, it is recommended to only enable the following field types for bulk editing.

* `/libs/granite/ui/components/foundation/form/textfield`
* `/libs/granite/ui/components/foundation/form/textarea`
* `/libs/granite/ui/components/foundation/form/tagspicker`
* `/libs/granite/ui/components/foundation/form/datepicker`
* `/libs/granite/ui/components/foundation/form/pathbrowser`
* `/libs/granite/ui/components/foundation/form/checkbox`

## Enabling a Field {#enabling-a-field}

These steps use the `/apps/core/wcm/components/page/v1/page` from the [WKND sample content](/help/implementing/developing/introduction/develop-wknd-tutorial.md) as an example to enable bulk editing on a field in a development environment.

1. Using CRXDE open your page component.
1. Navigate to the required field within the `cq:dialog` definition.
1. Define the following property on the field node:

    * **Name**: `allowBulkEdit`
    * **Type**: `Boolean`
    * **Value**: `true`

1. Select **Save All** to persist your updates.

## Limitations {#limitations}

Bulk editing of page properties is:

* Not available for pages within a live copy.
* Only available for pages with the same resource type.
