---
title: Quick Publish to AEM and Dynamic Media
description: Quick Publish in Assets view enables you to publish assets to AEM and Dynamic Media simultaneously or separately. You can select assets and folders and choose to publish to Dynamic Media or AEM.
exl-id: 147c1c35-0d81-4458-b4ed-7541d2b0dd54
feature: Publishing, Dynamic Media
role: User
---
# Publish Assets to AEM and Dynamic Media{#Publish-Assets-to-AEM-and-Dynamic-Media}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

Experience Manager Assets enables you to quickly publish assets to Experience Manager and Dynamic Media using the Assets view. This ensures that you manage your assets and then publish them using the [Assets view without switching to the Admin view](/help/assets/overview.md##persona-based-experiences). 

Experience Manager Assets view provides the flexibility to publish assets to AEM or Dynamic Media, or both at the same time. You can publish assets while uploading, browsing, and searching assets. All these options to publish assets are explained within this article in detail.

## Before you begin {#before-you-begin}

Configure these settings to view the publish options for AEM and Dynamic Media: 

* To view the publish options for Dynamic Media, configure the following settings using the Admin view:

   * [Create a Dynamic Media Cloud configuration](/help/assets/dynamic-media/config-dm.md#configuring-dynamic-media-cloud-services).
   * Set the Dynamic Media Publish mode at the folder-level. You can configure these settings while creating the Dynamic Media Cloud configuraton as well. To overwrite those settings at the folder-level, see [Configure Selective Publish at the folder level in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md). 

* To view the publish options for AEM, you must configure the AEM publish endpoint for your environment.

## Publish Assets during upload {#piblish-assets-during-upload}

You can publish assets to AEM and Dynamic Media while uploading assets to a folder. The publish options that display depend on the Dynamic Media publish mode settings of the folder where the assets are being uploaded. Dynamic Media publish mode can be set to: 

* **Upon activaton:** When assets are uploaded to this folder, you must explicitly publish the asset first before a URL/Embed link is provided. 

* **Immediate:** When assets are uploaded to this folder, the system ingests the assets into Experience Manager and provides the URL/Embed instantly. 
* **Selective Publish:** Assets are published to your choice of either Experience Manager or to Dynamic Media for delivery in the public domain. 

### Dynamic Media Publish Mode set to Upon Activation {#dynamic-media-publish-mode-set-to-upon-activation}

To publish assets while uploading them to a folder whose Dynamic Media Publish Mode is set to **Upon Activation**: 

1. Click **Add Assets** > **Browse** > **Browse Files** to navigate to the appropriate folder to upload assets. The **Publish Options** section displays the **DM Publish Mode** as **Upon Activation**. 
![Upload image upon activation](/help/assets/assets/upload-uactivation.svg)
2. Select **Publish to AEM and Dynamic Media** and click **Upload**. The assets are published to AEM and Dynamic Media at the same time. To see the updated publish status for these assets, see [Check Publish status](#check-publish-status). 

### Dynamic Media Publish Mode set to Immediate {#dynamic-media-publish-mode-set-to-immediate}

 To publish assets while uploading them to a folder hwose Dynamic Media Publish Mode is set to **Immediate**: 

 1. Click **Add Assets** > **Browse** > **Browse Files** to navigate to the appropriate folder to upload assets. The **Publish Options** section displays the **DM Publish Mode** as **Immediate**. 
![file upload image - immediate mode](/help/assets/assets/resized-image-pdf-svg-new.svg)


    As the Dynamic Media Publish Mode is **Immediate**, the uploaded assets are automatically published to Dynamic Media when you click **Upload**. 

 2. Select **Publish to AEM** to publish the uploaded assets to AEM and click Upload. 
 
     If you select **Publish to AEM**, the assets are published to AEM and Dynamic Media, else the assets are published to Dynamic Media. 
     
     To see the updated publish status for these assets, see [Check Publish status](#check-publish-status). 

### Dynamic Media Publish Mode set to Selective Publish {#dynamic-media-publish-mode-set-to-selective-publish}

 To publish assets during upload to a folder with Dynamic Media Publish Mode set to **Selective Publish**:

  1. Click **Add Assets** > **Browse** > **Browse Files** to navigate to the appropriate folder to upload assets. The **Publish Options** section displays the **DM Publish Mode** as **Selective Publish**. 
  ![upload image-selective piblish mode](/help/assets/assets/upload-selective.svg)

  2. Select **Publish to AEM**, **Publish to Dynamic Media**, or both as per your requirements and click **Upload**. 
 
     The assets are published to AEM and Dynamic Media based on your selection. 
     
     To see the updated publish status for these assets, see [Check Publish status](#check-publish-status).

## Publish assets using asset browse page {#publish-assets-using-asset-browse-page}

 To publish assets using the asset browse page: 

 1. Click **Assets** in the **Assets Management** section available in the left pane. 
 2. Select one or more assets or folders that you need to publish and click **Publish**.
 3. Select **AEM** and click **Publish** to publish assets to AEM and Dynamic Media.
![assets browse](/help/assets/assets/browse-uactivation-immediate.svg) 
You cannot publish a folder that has the Dynamic Media Publish Mode set to **Selective Publishing.** All other selected folders or assets get published to AEM and Dynamic Media after selecting AEM. 
![assets browse](/help/assets/assets/browse-selective123.svg)

## Publish assets using search results page {#publish-assets-using-search-results-page}

 To publish assets using the asset search results page:

 1. Specify the criteria in the search bar and click the search icon to view the results.
 2. Select the assets that you need to publish and click **Publish.**
 3. Select AEM, Dynamic Media, or both as per your requirements and click **Publish.** 
![search image](/help/assets/assets/search-mode.svg)
The option to publish to Dynamic Media on the search results page depends on the Dynamic Media Publish Mode set on the folder where the asset is available in the repository.

    >[!NOTE]
    >
    >If you select a folder and click **Publish** from the search results page then Experience Manager Assets displays an option to publish assets to AEM and not Dynamic Media irrespective of the Dynamic Media Publish Mode settings for the folder. 

## Check Publish status {#check-publish-status}

To check the published status for an asset or a folder:

1. Click **[!UICONTROL Assets]** in the **[!UICONTROL Assets Management]** section available in the left pane. 
2. Switch to List view using the View Switcher. You can view asset properties, such as AEM publish, Dynamic Media Publish, title, size, dimensions, and so on.  
If an asset or folder is not published, the status for columns **AEM Publish** and **Dynamic Media Publish** is displayed as **N/A.** 
![check publish status1](/help/assets/assets/check-publish-status1.png)
  If you cannot view the AEM Publish and Dynamic Media Publish columns in the List view: 
   1. Click ![settings](/help/assets/assets/settings-icon.svg) and select **AEM Publish** and **Dynamic Media Publish** columns from the **Configurable Columns** dialog. 
   2. Click **Confirm.** Experience Manager Assets adds the selected columns to the List view. 
   
      ![check publish status2](/help/assets/assets/check-publish-status2.png)

You can also check an asset publish status by selecting an asset and clicking **Details.** The details are available in the **Publish** section available in the right pane. The **Publish** section lists the date when the assets are published to Dynamic Media and AEM. If you need to view the time when the assets are published, you can navigate to List view and view those details. 

![check publish status 3](/help/assets/assets/check-publish-status3.png)

## Limitations {#limitations}

 The following capabilities are out of scope for now while publishing assets to AEM and Dynamic Media: 
 
 * Publish assets to AEM and Dynamic Media from the Asset details page. 
 * Visualize the endpoints where the assets are published using the Quick Publish wizard. 
 * Add or delete more assets in the Quick Publish wizard. 
 * A page to view published assets. 
 * An ability to copy or paste Dynamic Media URL at an asset level (if the assets are published to Dynamic Media). 
 * Ability to publish references (assets, tags, and so on) while publishing to AEM. 
 * Ability to overwrite Dynamic Media sync status at folder-level. 
 * Ability to overwrite Dynamic Media Publish mode at folder-level
 * Manage Publication is not yet supported.
