---
title: Import [!DNL Touch UI] metadata schema forms to [!DNL Assets View]
description: This article describes how to import the metadata schema form available in [!DNL Touch UI] to [!DNL Assets View]
contentOwner: AG
feature: Metadata
role: User, Admin
exl-id: fb70a068-3ba3-4459-952d-79155d286c42
---

# Import [!DNL Touch UI] metadata schema forms to [!DNL Assets View] {#import-touch-UI-metadata-forms-to-assets-view}

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

[!DNL Adobe Experience Manager Assets] lets you import metadata forms available in the [!DNL Touch UI] to [!DNL Assets View]. You can assign the imported metadata forms to the [!DNL Assets View] folders.

## Import metadata forms to [!DNL Assets View]{#import-metadata-forms-to-assets-view}

As an administrator, execute the following steps to import the metadata form schema available in [!DNL Touch UI] to [!DNL Assets View]:

1. Navigate to the [!DNL Assets View] home page and click **[!UICONTROL  Metadata Forms]** under **[!UICONTROL Settings]** to open the **[!UICONTROL Metadata Forms]** page displaying the list of metadata forms available in [!DNL Assets View]. 
![metadata forms page](/help/assets/assets/metadata-forms-page.png)
1. Select **[!UICONTROL Import]** to display the **[!UICONTROL Import metadata forms]** table, which includes a list of matadata forms available in [!DNL Touch UI]. The table row includes, metadata form name (under **[!UICONTROL Name]**), folders associated with that form (under **[!UICONTROL Folder Association]**) and an option to preview ![preview](/help/assets/assets/Preview.svg) the form before importing it. Click ![select folder](/help/assets/assets/add-to-folder.svg) to select a folder to assign the corresponding metadata form to it. Click the red circle to view details about unsupported metadata components or mappings in the form that are excluded from the import.
![Import Metadata Forms page](/help/assets/assets/import-metadata-forms-page.png)
 
   >[!NOTE]
   > 
   > In the **[!UICONTROL Import Metadata Forms]** table a **[!UICONTROL Duplicate]** label next to a form name shows that the form is already applied to a folder in [!DNL Assets View]. Importing that duplicate form overrides the existing one applied to the folder. To avoid this override, rename the form before importing it. Click the form name to rename it.

1. Select one or more forms in the table and click **[!UICONTROL Start Import]** to import them into [!DNL Assets View]. The [!DNL Assets View] **[!UICONTROL Metadata Forms]** page opens and displays both recently imported and existing forms in [!DNL Assets View]. You can do the following on this page:
   * Click the column header to sort the table by [!UICONTROL Name], [!UICONTROL Modified], or [!UICONTROL Author]. 
   * Select the imported form and click **[!UICONTROL Remove from folder(s)]**, then verify the folder name in the folder path to confirm that the folder is correctly ported.
   * Select the imported form and click **[!UICONTROL Edit]** to view all the supported configurations of the metadata form. See [Metadata schemas](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/metadata-schemas) for more information about the metadata forms, their components, and fields.
   ![verify metadata forms page](/help/assets/assets/verify-metadata-forms-page.png)

## Verify the imported metadata schema forms{#Verify-the-imported-metadata-schema-forms}

After importing the metadata schema forms from [!DNL Touch UI] to [!DNL Assets View], follow these steps to verify the import: 

1. Navigate to any of the associated folders of the imported metadata form.
1. Navigate to an [asset's details page](/help/assets/navigate-assets-view.md#preview-assets) and verify that the supported metadata components, component fields, and field values are synced  from [!DNL Touch UI]. See [Metadata schemas](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/metadata-schemas) for more information about metadata components, component fields, and the field values.
    
>[!NOTE]
>
> Any changes you make to the metadata fields in [!DNL Assets View] syncs back to the metadata form in [!DNL Touch UI] in real time. However, changes made to the schema forms in [!DNL Touch UI] are not synced to the metada form in [!DNL Assets View].

<!--   
* Open another tab in your browser and navigate to Touch UI and access the **[!UICONTROL Metadata Schema Forms]** page  --> 

