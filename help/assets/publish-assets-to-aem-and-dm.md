---
title: Quick Publish to [!DNL AEM and Dynamic Media]
description: Quick Publish in [!DNL Assets view] enables you to publish assets to [!DNL AEM and Dynamic Media] simultaneously or separately. You can select assets and folders and choose to publish to [!DNL Dynamic Media] or [!DNL AEM].
exl-id: 147c1c35-0d81-4458-b4ed-7541d2b0dd54
feature: Publishing
role: User
---
# Publish Assets to [!DNL AEM and Dynamic Media]{#Publish-Assets-to-AEM-and-Dynamic-Media}

[!DNL Experience Manager Assets] enables you to quickly publish assets to [!DNL Experience Manager] and [!DNL Dynamic Media] using the [!DNL Assets view]. This ensures that you manage your assets and then publish them using the [[!DNL Assets view] without switching to the [!DNL Admin view]](/help/assets/overview.md##persona-based-experiences). 

[!DNL Experience Manager Assets view] provides the flexibility to publish assets to [!DNL AEM] or [!DNL Dynamic Media], or both at the same time. You can publish assets while uploading, browsing, and searching assets. All these options to publish assets are explained within this article in detail.

## Before you begin {#before-you-begin}

Configure these settings to view the publish options for [!DNL AEM and Dynamic Media]: 

* To view the publish options for [!DNL Dynamic Media], configure the following settings using the Admin view:

   * [Create a [!DNL Dynamic Media] Cloud configuration](/help/assets/dynamic-media/config-dm.md#configuring-dynamic-media-cloud-services).
   * Set the [!DNL Dynamic Media] Publish mode at the folder-level. You can configure these settings while creating the [!DNL Dynamic Media] Cloud configuraton as well. To overwrite those settings at the folder-level, see [Configure Selective Publish at the folder level in [!DNL Dynamic Media]](/help/assets/dynamic-media/selective-publishing.md). 

* To view the publish options for [!DNL AEM], you must configure the [!DNL AEM] publish endpoint for your environment.

## Publish Assets during upload {#piblish-assets-during-upload}

You can publish assets to [!DNL AEM and Dynamic Media] while uploading assets to a folder. The publish options that display depend on the [!DNL Dynamic Media] publish mode settings of the folder where the assets are being uploaded. [!DNL Dynamic Media] publish mode can be set to: 

* **[!UICONTROL Upon activaton]:** When assets are uploaded to this folder, you must explicitly publish the asset first before a URL/Embed link is provided. 

* **[!UICONTROL Immediate]:** When assets are uploaded to this folder, the system ingests the assets into Experience Manager and provides the URL/Embed instantly. 
* **[!UICONTROL Selective Publish]:** Assets are published to your choice of either [!DNL Experience Manager] or to [!DNL Dynamic Media] for delivery in the public domain. 

### [!UICONTROL Dynamic Media Publish Mode] set to [!UICONTROL Upon Activation] {#dynamic-media-publish-mode-set-to-upon-activation}

To publish assets while uploading them to a folder whose [!DNL Dynamic Media Publish Mode] is set to **[!UICONTROL Upon Activation]**: 

1. Click **[!UICONTROL Add Assets]** > **[!UICONTROL Browse]** > **[!UICONTROL Browse Files]** to navigate to the appropriate folder to upload assets. The **[!UICONTROL Publish Options]** section displays the **[!UICONTROL DM Publish Mode]** as **[!UICONTROL Upon Activation]**. 

   ![Upload image upon activation](/help/assets/assets/upload-uactivation.svg)

1. Select **[!UICONTROL Publish to AEM and Dynamic Media]** and click **[!UICONTROL Upload]**. The assets are published to [!DNL AEM and Dynamic Media] at the same time. To see the updated publish status for these assets, see [Check Publish status](#check-publish-status). 

### [!UICONTROL Dynamic Media Publish Mode] set to [!UICONTROL Immediate] {#dynamic-media-publish-mode-set-to-immediate}

To publish assets while uploading them to a folder whose [!UICONTROL Dynamic Media Publish Mode] is set to **[!UICONTROL Immediate]**: 

1. Click **[!UICONTROL Add Assets]** > **[!UICONTROL Browse]** > **[!UICONTROL Browse Files]** to navigate to the appropriate folder to upload assets. The **[!UICONTROL Publish Options]** section displays the **[!UICONTROL DM Publish Mode]** as **[!UICONTROL Immediate]**. 

   ![file upload image - immediate mode](/help/assets/assets/resized-image-pdf-svg-new.svg)

   As the [!UICONTROL Dynamic Media Publish Mode] is **[!UICONTROL Immediate]**, the uploaded assets are automatically published to [!DNL Dynamic Media] when you click **[!UICONTROL Upload]**. 

1. Select **Publish to AEM** to publish the uploaded assets to [!DNL AEM] and click **[!UICONTROL Upload]**.
 
     If you select **Publish to AEM**, the assets are published to [!DNL AEM and Dynamic Media], else the assets are published to [!DNL Dynamic Media]. 
     
     To see the updated publish status for these assets, see [Check Publish status](#check-publish-status). 

### [!UICONTROL Dynamic Media Publish Mode] set to [!UICONTROL Selective Publish] {#dynamic-media-publish-mode-set-to-selective-publish}

To publish assets during upload to a folder with [!UICONTROL Dynamic Media Publish Mode] set to **[!UICONTROL Selective Publish]**:

1. Click **[!UICONTROL Add Assets]** > **[!UICONTROL Browse]** > **[!UICONTROL Browse Files]** to navigate to the appropriate folder to upload assets. The **[!UICONTROL Publish Options]** section displays the **[!UICONTROL DM Publish Mode]** as **[!UICONTROL Selective Publish]**. 

  ![upload image-selective piblish mode](/help/assets/assets/upload-selective.svg)

1. Select **[!UICONTROL Publish to AEM]**, **[!UICONTROL Publish to Dynamic Media]**, or both as per your requirements and click **Upload**. 
 
   The assets are published to [!DNL AEM and Dynamic Media] based on your selection. 
     
   To see the updated publish status for these assets, see [Check Publish status](#check-publish-status).

## Publish assets using asset browse page {#publish-assets-using-asset-browse-page}

To publish assets using the asset browse page: 

1. Click **[!UICONTROL Assets]** in the **[!UICONTROL Assets Management]** section available in the left pane. 
1. Select one or more assets or folders that you need to publish and click **[!UICONTROL Publish]**.
1. Select **[!UICONTROL AEM]** and click **[!UICONTROL Publish]** to publish assets to [!DNL AEM and Dynamic Media].

   ![assets browse](/help/assets/assets/browse-uactivation-immediate.svg) 

   You cannot publish a folder that has the [!DNL Dynamic Media] Publish Mode set to **[!UICONTROL Selective Publishing]**. All other selected folders or assets get published to [!DNL AEM and Dynamic Media] after selecting [!DNL AEM]. 

   ![assets browse](/help/assets/assets/browse-selective123.svg)

## Publish assets using search results page {#publish-assets-using-search-results-page}

To publish assets using the asset search results page:

1. Specify the criteria in the search bar and click the search icon to view the results.
1. Select the assets that you need to publish and click **[!UICONTROL Publish].**
1. Select [!DNL AEM, Dynamic Media], or both as per your requirements and click **[!UICONTROL Publish]**. 

   ![search image](/help/assets/assets/search-mode.svg)

   The option to publish to [!DNL Dynamic Media] on the search results page depends on the [!DNL Dynamic Media] Publish Mode set on the folder where the asset is available in the repository.

   >[!NOTE]
   >
   >If you select a folder and click **[!UICONTROL Publish]** from the search results page then [!DNL Experience Manager Assets] displays an option to publish assets to [!DNL AEM] and not [!DNL Dynamic Media] irrespective of the [!DNL Dynamic Media] Publish Mode settings for the folder. 

## Check Publish status {#check-publish-status}

To check the published status for an asset or a folder:

1. Click **[!UICONTROL Assets]** in the **[!UICONTROL Assets Management]** section available in the left pane. 
1. Switch to List view using the View Switcher. You can view asset properties, such as [!UICONTROL AEM publish], [!UICONTROL Dynamic Media Publish], [!UICONTROL title], [!UICONTROL size], [!UICONTROL dimensions], and so on.

   If an asset or folder is not published, the status for columns **[!UICONTROL AEM Publish]** and **[!UICONTROL Dynamic Media Publish]** is displayed as **[!UICONTROL N/A]**. 

   ![check publish status1](/help/assets/assets/check-publish-status1.png)

   If you cannot view the [!DNL AEM] Publish and [!DNL Dynamic Media] Publish columns in the List view: 
   
   1. Click ![settings](/help/assets/assets/settings-icon.svg) and select **[!UICONTROL AEM Publish]** and **[!UICONTROL Dynamic Media Publish]** columns from the **[!UICONTROL Configurable Columns]** dialog. 
   1. Click **[!UICONTROL Confirm]**. [!DNL Experience Manager Assets] adds the selected columns to the List view. 
   
      ![check publish status2](/help/assets/assets/check-publish-status2.png)

You can also check an asset publish status by selecting an asset and clicking **[!UICONTROL Details]**. The details are available in the **[!UICONTROL Publish]** section available in the right pane. The **[!UICONTROL Publish]** section lists the date when the assets are published to [!DNL Dynamic Media] and [!DNL AEM]. If you need to view the time when the assets are published, you can navigate to List view and view those details. 

![check publish status 3](/help/assets/assets/check-publish-status3.png)

## Limitations {#limitations}

The following capabilities are out of scope for now while publishing assets to [!DNL AEM and Dynamic Media]: 

* Publish assets to [!DNL AEM and Dynamic Media] from the [!DNL Asset details page]. 
* Visualize the endpoints where the assets are published using the Quick Publish wizard. 
* Add or delete more assets in the Quick Publish wizard. 
* A page to view published assets. 
* An ability to copy or paste [!DNL Dynamic Media] URL at an asset level (if the assets are published to [!DNL Dynamic Media]). 
* Ability to publish references (assets, tags, and so on) while publishing to [!DNL AEM]. 
* Ability to overwrite [!DNL Dynamic Media] sync status at folder-level. 
* Ability to overwrite [!DNL Dynamic Media] Publish mode at folder-level
* Manage Publication is not yet supported.
