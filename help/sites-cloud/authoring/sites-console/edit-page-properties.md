---
title: Editing Page Properties
description: Learn how to edit the properties of a page and change behavior of the page and how it is managed.
solution: Experience Manager Sites
feature: Authoring
role: User
exl-id: 8fee7e24-bbaa-4cc4-a047-165c9f2cd973
---
# Editing Page Properties {#page-properties}

Learn how to edit [the properties of a page](/help/sites-cloud/authoring/sites-console/page-properties.md) and change behavior of the page and how it is managed.

>[!TIP]
>
>For details on the individual page properties available, please see the document [Page Properties.](/help/sites-cloud/authoring/sites-console/page-properties.md)

## Where to Edit Page Properties {#where}

You can edit page properties from a number of places in AEM.

* [From the **Sites** console](#from-the-sites-console)
* [From the Page Editor](#from-the-page-editor)
* [From the Universal Editor](#from-the-universal-editor)

Using the Sites Console you can also [edit the properties of multiple pages at once.](#editing-multiple-pages)

### From the Sites Console {#from-the-sites-console}

When browsing your content in the **Sites** console, you can use the **Properties** button in the toolbar to edit page properties:

1. Using the [**Sites** console,](/help/sites-cloud/authoring/sites-console/introduction.md) navigate to the location of the page for which you want to view and edit properties.
1. Select the **Properties** option for the required page using either:
   * [Quick actions](/help/sites-cloud/authoring/basic-handling.md#quick-actions)
   * [Selection mode](/help/sites-cloud/authoring/basic-handling.md#selecting-resources)
   * The page properties are shown using the appropriate tabs.
1. Either view or edit the properties as required.
1. Then use **Save** to save your updates followed by **Close** to return to the console.

### From the Page Editor {#from-the-page-editor}

When editing a page using the Page Editor, you can use **Page Information** to define the page properties:

1. In the [Page Editor](/help/sites-cloud/authoring/page-editor/introduction.md), open the page for which you want to edit properties.
1. Select the **Page Information** icon to open the selection menu:
1. Select **Open Properties** and a dialog opens that lets you edit the properties, sorted by the appropriate tab. The following buttons are available at the right of the toolbar:
   * **Cancel**
   * **Save & Close**
1. Use the **Save & Close** button to save the changes.

## From the Universal Editor {#from-the-universal-editor}

When editing a page using the Universal Editor, you can use the **Page Properties** icon to edit the properties:

1. In the [Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md#page-properties), open the page for which you want to edit properties.
1. Select the **Page Properties** icon in the toolbar.
1. The page properties window of AEM opens in a new browser tab just as if you were editing page properties from the [Page Editor.](#from-the-page-editor) The following buttons are available at the right of the toolbar:
   * **Cancel**
   * **Save & Close**
1. Use the **Save & Close** button to save the changes.
1. Return to the browser tab of Universal Editor.

## Editing the Properties of Multiple Pages {#editing-multiple-pages}

From the [**Sites** console](/help/sites-cloud/authoring/sites-console/introduction.md) you can select several pages then use **View Properties** to view and/or edit the page properties. This is referred to as bulk editing of page properties.

You can select multiple pages for bulk editing by various methods, including:

* When browsing the **Sites** console
* After using **Search** to locate a set of pages

After selecting the pages and then clicking or tapping the **Properties** option, the bulk properties are shown:

![Bulk editing page properties](/help/sites-cloud/authoring/assets/page-properties-bulk-edit.png)

You can only bulk edit pages that:

* Share the same resource type
* Are not part of a Live Copy
  * If any of the selected pages are part of a Live Copy, then a message is shown when the properties are opened.

The bulk editing window is divided in half vertically:

* The left side is a list of the pages you selected for bulk editing.
  * You can select/deselect the pages as necessary.
  * By default all are selected.
* The right is a list of [properties available for bulk editing.](/help/implementing/developing/extending/bulk-editor.md)
  * As when viewing properties for a single page, the properties are ordered under tabs.
  * Properties that are available on all selected pages and have been explicitly defined as available to bulk editing are visible.
  * If you reduce the page selection to one page, then all properties are visible.
  * Only properties with a common value are shown.
   * When the field is multi-value (for example, Tags), values will only be shown when *all* are common. If only some are common, they will only be shown when editing.
* Fields that are common, but have different values across the various pages are indicated with a special value such as the text `<Mixed Entries>`.

You can update the values in the fields available on the pages you select. The new values are applied to all selected pages when you select **Done**. When the field is multi-value (for example, Tags), you can either append a new value or remove a common value.

## Property Inheritance {#inheritance}

If the page is based on a blueprint or otherwise inherits content from another page, inheritance is reflected in the **Page Properties** window for the individual field.

![Inherited properties](assets/property-inhertiance.png)

Inherited properties can not be edited. Tap or click the **Cancel inheritance** icon next to a particular field to break its inheritance.

![Cancel inheritance](assets/cancel-inheritance.png)

Confirm the cancellation in the **Cancel inheritance** modal.

![Cancel inheritance confirmation modal](assets/cancel-inheriance-confirmation.png)

Once inheritance is cancelled for a field, it then becomes editable.

![Cancelled inheritance](assets/property-inheritance-broken.png)

To reinstate inheritance, tap or click the **Revert inheritance** icon next to the field.

![Revert inheritance](assets/revert-inheritance.png)

Confirm the reversion in the **Revert inheritance** modal.

![Revert inheritance confirmation modal](assets/revert-inhertiance-confirmation.png)

Select **Synchronize Page after reverting inheritance** to update the field with the latest values in the blueprint. If you do not, the values will be updated the next time the LiveCopy is synchronized.

>[!TIP]
>
>For more information about inheritance, please see the document [Multi Site Manager and Translation](/help/sites-cloud/administering/msm-and-translation.md)
