---
title: Integrate [!DNL AEM Assets] with [!DNL Figma].
description: Learn to integrate [!DNL AEM Assets] with [!DNL Figma] to access and use your organization's assets within your [!DNL Figma] design workflow.
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 530561ca-497b-4331-a014-72c561e1ca84
---

# Integrate [!DNL AEM Assets] with [!DNL Figma]{#integrate-aem-assets-with-figma}

[!DNL AEM Assets] integrates natively with [!DNL Figma], which allows designers to directly access the assets stored in [!DNL AEM Assets] from within the [!DNL Figma] user interface. You can place content managed in [!DNL AEM Assets] in the [!DNL Figma] canvas and then save new or edited content in the [!DNL AEM Assets] repository.

## Before you begin{#prerequisites-for-aem-assets-and-figma-integration}

* Minimum required AEM release version is `19149`.

* You must have valid [!DNL AEM Assets] and [!DNL Figma] licenses to integrate [!DNL AEM Assets] with [!DNL Figma].

## Supported file formats {#supported-file-formats-integration-figma}


* For importing [!DNL AEM] assets into Figma, the supported formats are image assets (JPEG, PNG), video files (MP4, MOV, WebM), Animated files (GIF), and Vector files (SVG).
* For exporting designs from [!DNL Figma] to [!DNL AEM Assets], the supported formats are **PNG**, **PDF**, **JPG**, **SVG**.

## Access [!UICONTROL Adobe Experience Manager (AEM) Assets Connector]{#access-aem-assets-connector}

Execute the following steps to access the [!UICONTROL Adobe Experience Manager (AEM) Assets Connector]:

1. On your [!DNL Figma] home page, click **[!UICONTROL Actions]** from the toolbar at the bottom of the canvas and search for [!DNL Adobe Experience Manager (AEM) Assets Connector] in the search bar available in the dialog box.
1. Select [!DNL Adobe Experience Manager (AEM) Assets Connector] to display the [!DNL Adobe Experience Manager (AEM) Assets Connector] panel. [Import [!DNL AEM] assets into your [!DNL Figma] canvas](#import-aem-assets-into-figma-workflow) using this panel.
![actions](/help/assets/assets/actions-on-figma.png)
Alternatively, access the [[!DNL Adobe Experience Manager (AEM) Assets Connector]](https://www.figma.com/community/plugin/1512561378275712210/adobe-experience-manager-aem-assets-connector) available on [!DNL Figma] community, click **[!UICONTROL Open in...]**, select a recent file or create a new file and click **[!UICONTROL Run]** to access the [!DNL Adobe Experience Manager (AEM) Assets Connector] panel.
![plugin-page-on-figma-community](/help/assets/assets/plugin-page-on-figma-community.png)

>[!NOTE]
>
> [Contact Adobe Support](https://helpx.adobe.com/contact.html) for help if you see a **[!UICONTROL Network Error]** message after logging in to your [!DNL AEM] environment.

## Import [!DNL AEM] assets into [!DNL Figma] canvas{#import-aem-assets-into-figma-workflow}

[Access [!UICONTROL Adobe Experience Manager (AEM) Assets Connector] panel](#access-aem-assets-connector) within your [!DNL Figma] design interface and do the following:

1.  Search for assets in the [!UICONTROL Adobe Experience Manager (AEM) Assets Connector] panel. For more information, see [using Asset Selector](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/asset-selector/overview-asset-selector#using-asset-selector).

1. Drag and drop the asset to the canvas or select the asset and click **[!UICONTROL Select]** to bring the asset on the canvas.

1. Click ![three dots](/help/assets/assets/three-dots.svg) in the folder path to display all parent and child folders in the current hierarchy. Select a folder to navigate to that location. 
![three dots](/help/assets/assets/figma-v2-plugin.png)

1. [Optional] Click **[!UICONTROL Check for updates]**. The assets used in the current Figma document are compared to the assets that exist in AEM. Any updates are listed in a separate window. Click **[!UICONTROL Update]** to get the updated asset from AEM into your Figma document. 

Once your Figma design is ready, you can [export the asset to the AEM Assets repository](#export-figma-design-to-aem-assets-folder). 

## Export assets to [!DNL AEM Assets] repository{#export-figma-design-to-aem-assets-folder}

[Access [!UICONTROL Adobe Experience Manager (AEM) Assets Connector] panel](#access-aem-assets-connector) within your [!DNL Figma] design interface and execute the following steps to export your design to the [!DNL AEM Assets] repository:

1. Navigate to the destination folder where you want to save your [!DNL Figma] design. If you are already inside a folder, click More options (![three dots](/help/assets/assets/three-dots.svg)) in the folder path to select a different destination folder.
1. Optional: Group assets on the canvas to select them as a single unit to upload in your folder.
1. Click ![file upload](/help/assets/assets/upload-icon.svg) **[!UICONTROL Upload]** to display the **[!UICONTROL Upload Asset]** dialog box. 
1. In the dialog box, select either **[!UICONTROL Selected Item]** or **[!UICONTROL Page]**, specify a file or page name, define an export configuration and click **[!UICONTROL Upload]** to upload the selected asset or the entire design to the destination folder. 

   The export configuration comprises the file format, scale, and quality. For example, if you select JPG as the file format, you can also define the image scale and quality. Similarly, if you select PNG as the file format, you can also define the image scale.
   ![upload figma design](/help/assets/assets/upload-figma-design.png)
