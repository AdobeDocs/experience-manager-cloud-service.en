---
title: Bulk metadata edit in [!DNL Assets View]
description: Learn how you can update a predefined set of standard metadata fields for multiple assets available on the [DNL! Assets View] simultaneously.
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: f5fee1b3-2855-4010-ae4a-216beb20920d
---
# Bulk metadata edit in [!DNL Assets View]{#how-to-edit-the-metadata-of-multiple-assets-simultaneously}

The **[!DNL Bulk Metadata Edit]** capability in [!DNL Assets View] lets you edit a **predefined set of standard metadata fields** across **multiple asset files simultaneously**. Instead of editing each asset one at a time, you select a group of assets and apply the same standardized metadata updates to all of them in a single action.

## What [!DNL Bulk Metadata Edit] Does

[!DNL Bulk Metadata Edit] applies changes to a predefined set of standard metadata properties for many assets at once. This means you can update shared attributes—such as the standard descriptive fields that classify and label your files—across an entire selection in one operation rather than repeating the same edit individually for every asset.

## Key Benefits

Editing metadata in bulk preserves the quality of your asset library at scale. The primary benefits include:

- **Efficiency** — Apply the same metadata values to many assets in a single step, eliminating repetitive per-asset editing.
- **Consistency** — Ensure that the same standard metadata properties are applied uniformly across large collections of assets.
- **Accuracy** — Reduce the manual errors that occur when the same fields are entered separately on each individual asset.
- **Improved searchability and organization** — Standardized metadata ensures assets surface reliably in searches, filters, and browsing views, because consistent field values make assets easier to locate and group.

## When to Use [!DNL Bulk Metadata Edit]

[!DNL Bulk Metadata Edit] is most valuable when working with large sets of related files that share common attributes. Consistent, standardized metadata across large collections of assets keeps the entire library well organized and searchable, so applying uniform standard metadata to many assets at once maintains efficiency, consistency, and accuracy where individual editing would be slow and error-prone.

## Bulk edit asset metadata {#how-to-bulk-edit-the-metadata-of-multiple-assets-on-assets-view}

[!DNL Assets View] lets you update the metadata of up to **100 assets at a time** in a single operation. Execute these steps to bulk edit the metadata of multiple assets:

1. Navigate to **[!DNL Assets View]** and click **[!UICONTROL Assets]**.
1. Browse for specific assets or search them using keywords in the search bar.
1. Select the assets and click **[!UICONTROL Bulk Metadata Edit]** from the top menu.

    ![bulk-metadata-edit](/help/assets/assets/bulk-metadata-edit1.png)

1. On the [!UICONTROL Edit metadata page], edit the following fields in the **[!UICONTROL Properties]** panel: 
    * **[!UICONTROL Status]:** Select a status for the selected assets.
    * **[!UICONTROL Expiration date]:** Set a date after which the assets are no longer valid or needed. 
    * **[!UICONTROL Author]:** Specify the author's name.
    * **[!UICONTROL Keywords]:** Add specific terms or text strings that give high-level information about the assets and directly improve their discoverability in search. Add a keyword and press **Enter** or **return** to add another keyword to the list.
    * **[!UICONTROL Tags]:** Click ![bulk metadata edit](/help/assets/assets/tags-icon.svg) to select tags from the available options. Tags provide more specific information about the assets and enhance their discoverability. Tags already applied to the selected assets display in the **[!UICONTROL Properties]** panel. If you cannot find the relevant tags, create them and assign to the selected assets. See [Manage tags in [!DNL Assets view]](/help/assets/tagging-management-assets-view.md) for details on creating and assigning tags to assets.
    * Click **[!UICONTROL Save]** to apply the above metadata updates to the selected assets. The save behavior differs by field type: **[!UICONTROL Keywords]** and **[!UICONTROL Tags]** are appended to the existing values, so no prior keywords or tags are lost. In contrast, the updated details for **[!UICONTROL Status]**, **[!UICONTROL Expiration date]**, and **[!UICONTROL Author]** override their existing values, because each of these fields holds a single value per asset. 
    ![save-bulk-metadata-edit-properties](/help/assets/assets/save-bulk-metadata-edit-properties2.png)

        >[!NOTE]
        >
        >You can edit the metadata of **100 assets at a time**.

To see the applied metadata updates to an asset, navigate to the [!DNL asset details page] (select asset, and click **[!UICONTROL Details]**) and click ![bulk metadata edit](/help/assets/assets/info-icon-solid-black.svg) to see the asset's metadata in the **[!UICONTROL Information]** panel. 

>[!NOTE]
>
>**[!UICONTROL Status]**, **[!UICONTROL Expiration date]**, **[!UICONTROL Author]**, **[!UICONTROL Keywords]** and **[!UICONTROL Tags]** are standard metadata properties available for bulk metadata editing, regardless of folder-specific metadata. These metadata properties display on the [!UICONTROL asset details page] only if they are included in the metadata form applied to the asset's folder. If you cannot find these standard metadata properties on the [!UICONTROL asset details page], edit the asset folder's metadata form to include them. See [Metadata in [!DNL Assets View]](/help/assets/metadata-assets-view.md) to learn how to create or edit a metadata form and apply it to a folder.


**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in [!DNL Assets view]](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
