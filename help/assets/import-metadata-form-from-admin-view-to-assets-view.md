---
title: Import [!DNL Admin View] metadata forms to [!DNL Assets View]
description: This article describes how to import the metadata form available in [!DNL Admin View] to [!DNL Assets View]
contentOwner: AG
feature: Metadata
role: User, Admin
exl-id: fb70a068-3ba3-4459-952d-79155d286c42
---

# Import [!DNL Admin View] metadata forms to [!DNL Assets View] {#import-admin-view-metadata-forms-to-assets-view}

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

[!DNL Adobe Experience Manager Assets] lets you import metadata forms and their associated folders from [!DNL Admin View] to [!DNL Assets View].

## Before you begin{#prerequisites-for-importing-metadata-forms-to-assets-view}

Ensure you have admin rights to import the metadata forms and their associated folders from [!DNL Admin View] to [!DNL Assets View].

## Import metadata forms to [!DNL Assets View]{#import-metadata-forms-to-assets-view}

As an administrator, execute the following steps to import the metadata forms available in [!DNL Admin View] to [!DNL Assets View]:

1. Navigate to the [!DNL Assets View] home page and click **[!UICONTROL  Metadata Forms]** under **[!UICONTROL Settings]** to open the **[!UICONTROL Metadata Forms]** page displaying the list of metadata forms available in [!DNL Assets View]. 
![metadata forms page](/help/assets/assets/metadata-forms-page.png)
1. Select **[!UICONTROL Import]**, a processing message displays (for example, *Processing 2 metadata forms ... Please wait.*) while the import is in progress. After the processing is complete, the **[!UICONTROL Import metadata forms]** table displays, which includes a list of metadata forms available in [!DNL Admin View]. The table row includes, metadata form name (under **[!UICONTROL Name]**), folders associated with that form (under **[!UICONTROL Folder Association]**) and an option to preview ![preview](/help/assets/assets/Preview.svg) the form before importing it. 
![Import Metadata Forms page](/help/assets/assets/import-metadata-forms-page.png)
    
   >[!NOTE]
   > 
   > In the **[!UICONTROL Import Metadata Forms]**, table a **[!UICONTROL Duplicate]** label next to a form name shows that the form is already applied to a folder in [!DNL Assets View]. Importing that duplicate form overrides the existing one applied to the folder. To avoid this override, rename the form before importing it. Click the form name to rename it.
1. Click ![select folder](/help/assets/assets/x.svg) next to a folder name (under [!UICONTROL Folder Association]) to remove the corresponding metadata form from that folder.
1. Click ![select folder](/help/assets/assets/add-to-folder.svg) to select a folder to assign the corresponding metadata form to it. 
1. Click the red circle to view details about unsupported metadata components or mappings in the form that are excluded from the import.
![Import Metadata Forms page](/help/assets/assets/unsupported-import-elements.png)
1. Select one or more forms in the table and click **[!UICONTROL Start Import]** to import the metadata forms and its associated folders into [!DNL Assets View]. A processing message displays (for example, *Importing 3 metadata forms. Please wait!*). Once the import is complete, a success message confirms that the forms are imported successfully and the **[!UICONTROL Metadata Forms]** page (of [!DNL Assets View]) displays both recently imported and existing forms available in [!DNL Assets View]. You can do the following on this page:
   * Click the column header to sort the table by [!UICONTROL Name], [!UICONTROL Modified], or [!UICONTROL Author]. 
   * Select the imported form and click **[!UICONTROL Remove from folder(s)]**, then verify the folder name in the folder path to confirm that the folder is correctly ported.
   ![verify metadata forms page](/help/assets/assets/confirm-ported-folder.png)
   * Select the imported form and click **[!UICONTROL Edit]** to view all the supported configurations of the metadata form. See [Setup Metadata Forms](https://experienceleague.adobe.com/en/docs/experience-manager-assets-essentials/help/metadata#metadata-forms) for more information about the metadata forms, their components, and fields.
   ![verify metadata forms page](/help/assets/assets/verify-metadata-forms-page.png)

## Verify the imported metadata forms{#Verify-the-imported-metadata-forms}

After importing the metadata forms from [!DNL Admin View] to [!DNL Assets View], follow these steps to verify the import: 

1. Navigate to any of the associated folders of the imported metadata form.
1. Navigate to an [asset's details page](/help/assets/navigate-assets-view.md#preview-assets) and verify that the supported metadata components, component fields, and field values are synced from [!DNL Admin View]. See [Metadata in Assets Essentials](https://experienceleague.adobe.com/en/docs/experience-manager-assets-essentials/help/metadata) article for more information about metadata components, component fields, and the field values.

   >[!NOTE]
   >
   > In [[!DNL Assets View] details page](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/assets-view/metadata-assets-view#metadata-forms) or [[!DNL Admin View] properties page](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/administer/metadata-schemas), changes to the metadata property values are automatically synced between the two interfaces. However, structural changes in the form, such as adding or removing fields, or other modifications, are not synced.