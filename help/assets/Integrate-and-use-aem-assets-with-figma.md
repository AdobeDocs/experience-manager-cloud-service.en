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

[!DNL AEM Assets] integrates natively with [!DNL Figma], which allows designers to directly access the assets stored in [!DNL AEM Assets] from within the [!DNL Figma] user interface. You can place content managed in [!DNL AEM Assets] in the [!DNL Figma] canvas and then save new or edited content in [!DNL AEM Assets] repository.

## Before you begin{#prerequisites-for-aem-assets-and-figma-integration}

Fulfil the following requirements to integrate [!DNL AEM Assets] with [!DNL Figma]:

1. Access to the following Assets Cloud Service environments: 
    1. Valid AEM Assets and figma licenses

## Access [!UICONTROL Adobe Experience Manager (AEM) Assets Connector]{#access-aem-assets-connector}

Execute the following steps to access the [!UICONTROL Adobe Experience Manager (AEM) Assets Connector]:

1. On your [!DNL Figma] home page, click **[!UICONTROL Actions]** from the toolbar at the bottom of the canvas and search for [!DNL Adobe Experience Manager (AEM) Assets Connector] in the search bar available in the dialog box.
1. Select [!DNL Adobe Experience Manager (AEM) Assets Connector] to display the [!DNL Adobe Experience Manager (AEM) Assets Connector] panel. [Import [!DNL AEM] assets into your [!DNL Figma] canvas](#import-aem-assets-into-figma-workflow) using this panel.
![actions](/help/assets/assets/actions-on-figma.png)
Alternatively, access the [[!DNL Adobe Experience Manager (AEM) Assets Connector] plugin page](https://www.figma.com/community/plugin/1512561378275712210/adobe-experience-manager-aem-assets-connector) available on [!DNL Figma] community, click **[!UICONTROL Open in...]**, select a recent file or create a new file and click **[!UICONTROL Run]** to access the [!DNL Adobe Experience Manager (AEM) Assets Connector] panel.
![plugin-page-on-figma-community](/help/assets/assets/plugin-page-on-figma-community.png)

## Import [!DNL AEM] assets into [!DNL Figma] canvas{#import-aem-assets-into-figma-workflow}

Access [!UICONTROL Adobe Experience Manager (AEM) Assets Connector](#access-aem-assets-connector) panel within your figma design and do the following:

1. Browse your asset's folder or find your assets by searching them using keywords in the seach bar. Click ![filter](/help/assets/assets/filter-icon.svg) to use the filter options, switch view using the view switcher option below the upload option, select a repository from the **[!UICONTROL Repository field]** and select **[!UICONTROL Collections]** to navigate to your collections.
1. Drag and drop the asset to the canavas or select the asset and click [**!UICONTROL Select]** to bring the asset on the canvas.
1. Click ![three dots](/help/assets/assets/three-dots.svg) in the folder path to display all parent and sibling folders in the current hierarchy. Select a folder to navigate to that location. 
![three dots](/help/assets/assets/assets-folder-structure.png)
[Export your final figma design to your [!DNL AEM Assets]](#export-figma-design-to-aem-assets-folder) folder. 

## Export assets to [!DNL AEM Assets] folder{#export-figma-design-to-aem-assets-folder}

Access [!UICONTROL Adobe Experience Manager (AEM) Assets Connector](#access-aem-assets-connector) panel within your figma design and execute the following steps to export your design to [!DNL AEM Assets] folder:

1. Click ![three dots](/help/assets/assets/three-dots.svg) from the folder path to select a destination folder to save your design on the canvas. 
1. Click ![file upload](/help/assets/assets/upload-icon.svg) **[!UICONTROL Upload]** to display the **[!UICONTROL Upload Asset]** dialog box. 
1. On the dialog box, Specify a file name, select a file format, select between **[!UICONTROL Selected Item]** and **[!UICONTROL Page]** and click **[!UICONTROL Upload]** to upload a selected asset or entire design to your destination folder. 



Selected item saves a single selected asset or grouped assets from the canvas while selecting page saves the entire canvas page.



## Important points to note{#Limitations-of-using-aem-assets-into-figma}





----

## Import [!DNL AEM Assets] plugin into [!DNL Figma]{#import-aem-assets-plugin-into-figma}

Execute the following steps to import the [!DNL AEM Assets] plugin into [!DNL Figma]:

1. Navigate to the [[!DNL Figma] community](https://www.figma.com/community) page, click **[!UICONTROL Plugin]**, select **[!UICONTROL Import and export]** and search [!DNL Adobe Experience Manager (AEM) Assets Connector] in the search bar available on the **[!UICONTROL Import & export plugins]** page.
1. Select **[!UICONTROL Adobe Experience Manager (AEM) Assets Connector]** card, click **[!UICONTROL Open in Figma]** and log-in to your [!DNL Figma] account to display your [!DNL Figma] homepage.
1. Click **[!UICONTROL Open in...]** to select a file or create a new file.
1. Click **[!UICONTROL Run]** to display the **[!UICONTROL Adobe Experience Manager (AEM) Assets connector]** panel. Drag and drop the assets from the panel to the canvas to use them in your design.

## Import [!DNL AEM] assets into [!DNL Figma] workflow{#import-aem-assets-into-figma-workflow}

Execute the following steps to import the [!DNL AEM] assets into your [!DNL Figma] design workflow:

1. Open your [!DNL Figma] desktop app.
1. Click Actions from the menu bar at the bottom of the canvas and select **[!UICONTROL Adobe Experience Manager AEM Assets connector]** to select [!DNL AEM] aasets from the panel.
1. Drag and drop the asset on the canvas.

## Export [!DNL Figma] design to [!DNL AEM Assets] folder{#export-figma-design-to-aem-assets-folder}

Execute the following steps to export your [!DNL Figma] design to your [!DNL AEM Assets] folder:

1. Open your [!DNL Figma] desktop app.
1. Click Actions from the menu bar at the bottom of the canvas and select **[!UICONTROL Adobe Experience Manager AEM Assets connector]** to display the folders and assets availabe in your selected AEM Assets repository.
1. Navigate to a folder, click upload to diaplay the Upload Asset dialog box. On the dialog box, Specify a file name, select a file format, select between selected item and page. Selected item saves a single selected asset or grouped assets from the canvas while selecting page saves the entire canvas page.

Change the destination folder location: On the **[!UICONTROL Adobe Experience Manager AEM Assets connector]** panel clcik the three dots from the folder path and select a folder from the availabe options, clcik upload to upload the asset or the page in that folder.




