---
title: Integrate and use [!DNL AEM Assets] into [!DNL Figma].
description: Learn to integrate [!DNL AEM Assets] with [!DNL Figma] to access and use your organization's assets within your [!DNL Figma] design workflow.
hide: no
role: User
---

# Integrate and use [!DNL AEM Assets] into [!DNL Figma]{#integrate-and-use-aem-assets-into-figma}

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

[!DNL AEM Assets] integrates natively with [!DNL Figma], which allows designers to directly access the assets stored in [!DNL AEM Assets] from within the [!DNL Figma] user interface. You can place content managed in [!DNL AEM Assets] in the [!DNL Figma] canvas and then save new or edited content in the [!DNL AEM Assets] repository.

## Before you begin{#prerequisites-for-aem-assets-and-figma-integration}

You must have access to valid [!DNL AEM Assets] and [!DNL Figma] license to integrate [!DNL AEM Assets] with [!DNL Figma].

## Access [!UICONTROL Adobe Experience Manager (AEM) Assets Connector]{#access-aem-assets-connector}

Execute the following steps to access the [!UICONTROL Adobe Experience Manager (AEM) Assets Connector]:

1. On your [!DNL Figma] home page, click **[!UICONTROL Actions]** from the toolbar at the bottom of the canvas and search for [!DNL Adobe Experience Manager (AEM) Assets Connector] in the search bar available in the dialog box.
1. Select [!DNL Adobe Experience Manager (AEM) Assets Connector] to display the [!DNL Adobe Experience Manager (AEM) Assets Connector] panel. [Import [!DNL AEM] assets into your [!DNL Figma] canvas](#import-aem-assets-into-figma-workflow) using this panel.
![actions](/help/assets/assets/actions-on-figma.png)
Alternatively, access the [[!DNL Adobe Experience Manager (AEM) Assets Connector] plugin page](https://www.figma.com/community/plugin/1512561378275712210/adobe-experience-manager-aem-assets-connector) available on [!DNL Figma] community, click **[!UICONTROL Open in...]**, select a recent file or create a new file and click **[!UICONTROL Run]** to access the [!DNL Adobe Experience Manager (AEM) Assets Connector] panel.
![plugin-page-on-figma-community](/help/assets/assets/plugin-page-on-figma-community.png)

>[!NOTE]
>
> [Contact Adobe Support](https://helpx.adobe.com/contact.html) for help if you see a **[!UICONTROL Network Error]** message after logging in to your [!DNL AEM] environment.

## Import [!DNL AEM] assets into [!DNL Figma] canvas{#import-aem-assets-into-figma-workflow}

Access [!UICONTROL Adobe Experience Manager ([!DNL AEM]) Assets Connector](#access-aem-assets-connector) panel within your [!DNL Figma] design interface and do the following:

1. Browse your asset's folder or find your assets by searching them using keywords in the search bar. Click ![filter](/help/assets/assets/filter-icon.svg) to use the filter options, switch view using the view switcher option below the upload option, select a repository from the **[!UICONTROL Repository field]** and select **[!UICONTROL Collections]** to navigate to your collections.
1. Drag and drop the asset to the canvas or select the asset and click [**!UICONTROL Select]** to bring the asset on the canvas.
1. Click ![three dots](/help/assets/assets/three-dots.svg) in the folder path to display all parent and sibling folders in the current hierarchy. Select a folder to navigate to that location. 
![three dots](/help/assets/assets/assets-folder-structure.png)
[Export your final [!DNL Figma] design to your [!DNL AEM Assets]](#export-figma-design-to-aem-assets-folder) folder. 

## Export assets to [!DNL AEM Assets] folder{#export-figma-design-to-aem-assets-folder}

Access to [!UICONTROL Adobe Experience Manager (AEM) Assets Connector](#access-aem-assets-connector) panel within your [!DNL Figma] design interface and execute the following steps to export your design to the [!DNL AEM Assets] folder:

1. Navigate to the destination folder where you want to save your [!DNL Figma] design. If you're already inside a folder, click ![three dots](/help/assets/assets/three-dots.svg) in the folder path to select a different destination folder.
1. Click ![file upload](/help/assets/assets/upload-icon.svg) **[!UICONTROL Upload]** to display the **[!UICONTROL Upload Asset]** dialog box. 
1. In the dialog box, specify a file name, choose a file format, select either **[!UICONTROL Selected Item]** or **[!UICONTROL Page]**, and click **[!UICONTROL Upload]** to upload the selected asset or the entire design to the destination folder.
![upload figma design](/help/assets/assets/upload-figma-design.png)

## Important points to note{#Limitations-of-using-aem-assets-into-figma}

This integration currently has the following limitations:

* For importing [!DNL AEM] assets into Figma, the supported formats are **JPEG**, **PNG**.
* For exporting designs from [!DNL Figma] to [!DNL AEM Assets], the supported formats are **PNG**, **PDF**, **JPG**, **SVG**.



