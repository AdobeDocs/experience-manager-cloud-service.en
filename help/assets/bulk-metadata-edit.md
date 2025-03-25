---
title: Bulk metadata edit in [DNL! Assets View]
description: Learn how you can update a predefined set of standard metadata fields for multiple assets available on the [DNL! Assets View] simultaneously.
exl-id: f5fee1b3-2855-4010-ae4a-216beb20920d
---
# Bulk metadata edit in [!DNL Assets View]{#how-to-edit-the-metadata-of-multiple-assets-simultaneously}

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

The **[!DNL Bulk Metadata Edit]** capability of [!DNL Assets View] enables you to edit a predefined set of standard metadata fields for multiple asset files simultaneously. Select multiple assets and bulk update their predefined set of standard metadata at once rather than updating those standard metadata for each asset individually. This capability to bulk edit the standard set of metadata properties for multiple assets at once maintains the efficiency, consistency, and accuracy of those standard metadata properties across the large set of assets, improving the searchability and organization of those assets.  

## Bulk edit asset metadata {#how-to-bulk-edit-the-metadata-of-multiple-assets-on-assets-view}

Execute these steps to bulk edit the metadata of multiple assets at a time:

1. Navigate to **[!DNL Assets View]** and click **[!UICONTROL Assets]**.
1. Browse for specific assets or search them using keywords in the search bar.   
1. Select the assets and click **[!UICONTROL Bulk Metadata Edit]** from the top menu. 
![bulk-metadata-edit](/help/assets/assets/bulk-metadata-edit1.png)
1. On the [!UICONTROL Edit metadata page], edit the following fields in the **[!UICONTROL Properties]** panel: 
    * **[!UICONTROL Status]:** Select a status for the selected assets.
    * **[!UICONTROL Expiration date]:** Set a date after which the assets are no longer valid or needed. 
    * **[!UICONTROL Author]:** Specify the author's name.
    * **[!UICONTROL Keywords]:** Add specific terms or text strings that provide a high-level information about the assets to enhance their discoverability. Add a keyword and press **Enter** or **return** to add another keyword to the list.
    * **[!UICONTROL Tags]:** Click ![tags icon](/help/assets/assets/tags-icon.svg) to select tags from the available options. Tags provide more specific information about the assets and enhance their discoverability. Tags already applied to the selected assets displays in the **[!UICONTROL Properties]** panel. If you cannot find the relevant tags, create them and assign to the selected assets. See [Manage tags in [!DNL Assets view]](/help/assets/tagging-management-assets-view.md) for details on creating and assigning tags to assets.
    * Click **[!UICONTROL Save]** to apply the above metadata updates to the selected assets. Once saved, **[!UICONTROL Keywords]** and **[!UICONTROL Tags]** are appended while the updated details for **[!UICONTROL Status]**, **[!UICONTROL Expiration date]** and **[!UICONTROL Author]** overrides their existing details. 
    ![save-bulk-metadata-edit-properties](/help/assets/assets/save-bulk-metadata-edit-properties2.png)

        >[!NOTE]
        >
        >You can edit the metadata of 100 assets at a time.

To see the applied metadata updates to an asset, navigate to the [!DNL asset details page] (select asset, and click **[!UICONTROL Details]**) and click ![](/help/assets/assets/info-icon-solid-black.svg) to see the asset's metadata in the **[!UICONTROL Information]** panel. 

>[!NOTE]
>
>**[!UICONTROL Status]**, **[!UICONTROL Expiration date]**, **[!UICONTROL Author]**, **[!UICONTROL Keywords]** and **[!UICONTROL Tags]** are standard metadata properties available for bulk metadata editing, regardless of folder-specific metadata. These metadata properties display on the [!UICONTROL asset details page] only if they are included in the metadata form applied to the asset's folder. If you cannot find these standard metadata properties on the [!UICONTROL asset details page], edit the asset folder's metadata form to include them. See [Metadata in [!DNL Assets View]](/help/assets/metadata-assets-view.md) to learn how to create or edit a metadata form and apply it to a folder.
