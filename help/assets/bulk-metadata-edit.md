---
title: Bulk metadata edit in Assets View
description: Learn how you can update a predefined set of standard metadata fields for multiple assets available on the Assets View simultaneously.
exl-id: f5fee1b3-2855-4010-ae4a-216beb20920d
---
# Bulk metadata edit in Assets View{#how-to-edit-the-metadata-of-multiple-assets-simultaneously}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

The **Bulk Metadata Edit** feature within the Assets View allows users to edit a predefined set of standard metadata fields for multiple asset files simultaneously. Select multiple assets and bulk update their predefined set of standard metadata at once rather than updating those standard metadata for each asset individually. This feature enhances the efficiency, consistency, and accuracy of standard metadata properties across a large set of assets, improving asset searchability and organization.  

## Bulk edit asset metadata {#how-to-bulk-edit-the-metadata-of-multiple-assets-on-assets-view}

Execute these steps to bulk edit the metadata of multiple assets at a time:

1. On the Assets View, click **Assets**.
1. Browse for specific assets or search them using keywords in the search bar.   
1. Select the assets and click **Bulk Metadata Edit** from the top menu. 
![bulk-metadata-edit](/help/assets/assets/bulk-metadata-edit1.png)
1. On the Edit metadata page, edit the following fields in the **Properties** panel: 
    * **Status:** Select a status for the selected assets.
    * **Expiration date:** Set a date after which the assets are no longer valid or needed. 
    * **Author:** Specify the author's name.
    * **Keywords:** Add specific terms or text strings that provide a high-level information about the assets to enhance their discoverability. Add a keyword and press Enter or return to add another keyword to the list.
    * **Tags:** Click ![tags icon](/help/assets/assets/tags-icon.svg) to select tags from the available options. Tags provide more specific information about the assets and enhance their discoverability. Tags already applied to the selected assets displays in the **Properties** panel. If you can't find the relevant tags, create them and assign to the selected assets. See [Manage tags in Assets view](/help/assets/tagging-management-assets-view.md) for details on creating and assigning tags to assets.
    * Click **Save** to apply the above metadata updates to the selected assets. Once saved, Keywords and Tags are appended while the updated details for Status, Expiration date and Author overrides their existing details. 
    ![save-bulk-metadata-edit-properties](/help/assets/assets/save-bulk-metadata-edit-properties2.png)

        >[!NOTE]
        >
        >You can edit the metadata of 100 assets at a time.

To see the applied metadata updates to an asset, navigate to the asset details page (select asset, and click **Details**) and click ![](/help/assets/assets/info-icon-solid-black.svg) to see the asset's metadata in the **Information** panel. 

>[!NOTE]
>
>**Status**, **Expiration date**, **Author**, **Keywords** and **Tags** are standard metadata properties available for bulk metadata editing, regardless of folder-specific metadata. These metadata properties display on the asset details page only if they are included in the metadata form applied to the asset's folder. If you can't find these standard metadata properties on the asset details page, edit the asset folder's metadata form to include them. See [Metadata in Assets View](/help/assets/metadata-assets-view.md) to learn how to create or edit a metadata form and apply it to a folder.
