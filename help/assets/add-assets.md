---
title: Add your digital assets to Adobe Experience Manager
description: Add your digital assets to Adobe Experience Manager as a Cloud Service
---

# Add digital assets to Adobe Experience Manager {#add-assets-to-experience-manager}

Adobe Experience Manager enriches the binary content of the uploaded digital files with rich metadata, smart tags, renditions, and other Digital Asset Management (DAM) services. You can upload various types of files, such as images, documents, and raw image files, from your local folder or a network drive to Experience Manager Assets.

A number of upload methods are provided. In addition to the most commonly used browser upload, other methods of adding assets to the Experience Manager repository exist, including desktop clients, like Adobe Asset Link or Experience Manager desktop app, upload and ingestion scripts that customers would create, and automated ingestion integrations added as AEM extensions.

We will focus on upload methods for end users here, and provide links to articles describing technical aspects of asset upload and ingestion using Experience Manager APIs and SDKs.

While you can upload and manage any binary file in Experience Manager, most commonly used file formats have support for additional services, like metadata extraction or preview/rendition generation. Refer to [supported file formats](file-format-support.md) for details.

You can also choose to have additional processing done on the uploaded assets. A number of asset processing profiles can be configured on the folder, into which assets are uploaded, to add specific metadata, renditions or image processing services. See [Additional processing](#additional-processing) below for more information.

>[!NOTE]
>
>Experience Manager as a Cloud Service leverages a new way of uploading assets - direct binary upload. It is supported by default by the out of the box product capabilities and clients, like AEM user interface, Adobe Asset Link, AEM desktop app, and thus transparent to the end users.
>
>Upload code that is customized or extended by customers technical teams needs to use the new upload APIs and protocols.

## Upload assets {#upload-assets}

To upload a file (or multiple files), you can either select them on your desktop and drag and drop into the user interface (web browser) to the destination folder. Alternatively, you can initiate upload from from the user interface.

1. In the Assets user interface, navigate to the location where you want to add digital assets.
1. To upload the assets, do one of the following:

    * On the toolbar, tap the **[!UICONTROL Create]** icon. Then, on the menu, then tap **[!UICONTROL Files]**. You can rename the file in the presented dialog if needed.
    * In a browser that supports HTML5, drag the assets directly on the Assets user interface. The dialog to rename file is not displayed.

   ![create_menu](assets/create_menu.png)

   To select multiple files, press the Ctrl or Command key and select the assets in the file picker dialog. When using an iPad, you can select only one file at a time.

<!-- #ENGCHECK do we support pausing? I couldn't get pause to show with 1.5GB upload.... If not, this should be removed#

   You can pause the uploading of large assets (greater than 500 MB) and resume it later from the same page. Tap the **[!UICONTROL Pause]** icon beside progress bar that appears when an upload starts.

   ![chlimage_1-211](assets/chlimage_1-211.png)

   The size above which an asset is considered a large asset is configurable. For example, you can configure the system to consider assets above 1000 MB (instead of 500 MB) as large assets. In this case, **[!UICONTROL Pause]** appears on the progress bar when assets of size greater than 1000 MB are uploaded.

   The Pause button does not show if a file greater than 1000 MB is uploaded with a file less than 1000 MB. However, if you cancel the less than 1000 MB file upload, the **[!UICONTROL Pause]** button appears.

   To modify the size limit, configure the `chunkUploadMinFileSize` property of the `fileupload`node in the CRX repository.

   When you click the **[!UICONTROL Pause]** icon, it toggles to a **[!UICONTROL Play]** icon. To resume uploading, click the **[!UICONTROL Play]** icon.

   ![chlimage_1-212](assets/chlimage_1-212.png)
-->

1. To cancel an ongoing upload, click close (`X`) next to the progress bar. When you cancel the upload operation, AEM Assets deletes the partially uploaded portion of the asset.

   If you cancel the upload operation before the files are uploaded, AEM Assets stops uploading the current file and refreshes the content. However, files that are already uploaded are not deleted.


<!-- #ENGCHECK do we support pausing? I couldn't get pause to show with 1.5GB upload.... If not, this should be removed#
   The ability to resume uploading is especially helpful in low-bandwidth scenarios and network glitches, where it takes a long time to upload a large asset. You can pause the upload operation and continue later when the situation improves. When you resume, uploading starts from the point where you paused it.
-->

<!-- #ENGCHECK assuming this is not relevant? remove after confirming#
   During the upload operation, AEM saves the portions of the asset being uploaded as chunks of data in the CRX repository. When the upload completes, AEM consolidates these chunks into a single block of data in the repository.

   To configure the cleanup task for the unfinished chunk upload jobs, go to `https://[aem_server]:[port]/system/console/configMgr/org.apache.sling.servlets.post.impl.helper.ChunkCleanUpTask`.
-->


 1. The upload progress dialog in AEM Assets displays the count of successfully uploaded files and the files that failed to upload.

   In addition, the Assets user interface displays the most recent asset that you upload or the folder that you created first.

>[!NOTE]
>
>To upload nested folder hierarchies to AEM, see [bulk upload of assets](#bulk-upload).

<!-- #ENGCHECK I'm assuming this is no longer relevant.... If yes, this should be removed#

### Serial uploads {#serialuploads}

Uploading numerous assets in bulk consumes significant I/O resources, which may adversely impact the performance of your AEM Assets instance. In particular, if you have a slow internet connection, the time to upload drastically increases due to a spike in disk I/O. Moreover, your web browser may introduce additional restrictions to the number of POST requests AEM Assets can handle for concurrent asset uploads. As a result, the upload operation fails or terminate prematurely. In other words, AEM assets may miss some files while ingesting a bunch of files or altogether fail to ingest any file.

To overcome this situation, AEM Assets ingests one asset at a time (serial upload) during a bulk upload operation, instead of the concurrently ingesting all the assets.

Serial uploading of assets is enabled by default. To disable the feature and allow concurrent uploading, overlay the `fileupload` node in Crx-de and set the value of the `parallelUploads` property to `true`.

### Streamed uploads {#streamed-uploads}

If you upload many assets to AEM, the I/O requests to server increase drastically, which reduces the upload efficiency and can even cause some upload task to time out. AEM Assets supports streamed uploading of assets. Streamed uploading reduces the disk I/O during the upload operation by avoiding asset storage in a temporary folder on the server before copying it to the repository. Instead, the data is transferred directly to the repository. This way, the time to upload large assets and the possibility of timeouts is reduced. Streamed upload is enabled by default in AEM Assets.

>[!NOTE]
>
>Streaming upload is disabled for AEM running on JEE server with servlet-api version lower than 3.1.
-->

### Handling uploads when asset already exists {#handling-upload-existing-file}

If you upload an asset with the same name as that of an asset already available at the location where you are uploading the asset, a warning dialog is displayed.

You can choose to replace an existing asset, create another version, or keep both by renaming the new asset that is uploaded. If you replace an existing asset, the metadata for the asset and any prior modifications (for example annotations, cropping, and so on) you made to the existing asset are deleted. If you choose to keep both assets, the new asset is renamed with the number `1` appended to its name.

>[!NOTE]
>
>When you select **[!UICONTROL Replace]** in the [!UICONTROL Name Conflict] dialog, the asset ID is regenerated for the new asset. This ID is different from the ID of the previous asset.
>
>If Asset Insights is enabled to track impressions/clicks with Adobe Analytics, the regenerated asset ID invalidates the data-captured for the asset on Analytics.

To retain the duplicate asset in AEM Assets, tap/click **[!UICONTROL Keep]**. To delete the duplicate asset you uploaded, tap/click **[!UICONTROL Delete]**.

### File name handling and forbidden characters {#filename-handling}

AEM Assets prevents you from uploading assets with the forbidden characters in their filenames. If you try to upload an asset with file name containing a disallowed character or more, AEM Assets displays a warning message and stops the upload until you remove these characters or upload with an allowed name.

To suit specific file naming conventions for your organization, the [!UICONTROL Upload Assets] dialog lets you specify long names for the files that you upload.

However, the following (space-separated list of) characters are not supported:

* asset file name must not contain `* / : [ \\ ] | # % { } ? &`
* asset folder name must not contain `* / : [ \\ ] | # % { } ? \" . ^ ; + & \t`

## Bulk upload of assets {#bulk-upload}

To upload larger number of files, especially if they exist in a nested folder hierarchy on disk, the following approaches can be used:

* Use a custom upload script or tool that leverages [asset upload APIs](developer-reference-material-apis.md#asset-upload-technical). Such a custom tool can add additional handling of assets (for example, translate metadata or rename files), if required.
* Use [Experience Manager desktop app](https://docs.adobe.com/content/help/en/experience-manager-desktop-app/using/using.html) to upload nested folder hierarchies.

>[!NOTE]
>
>Bulk upload as a part of content migration from other systems when setting up and deploying to Experience Manager requires careful planning, consideration, and choice of tools. See the [deployment guide](/help/implementing/deploying/overview.md) for guidance on content migration approaches.

## Upload assets using desktop clients {#upload-assets-desktop-clients}

In addition to web browser user interface, Experience Manager supports other clients on desktop. They also provide upload experience without the need to go to the web browser.

* [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html) provides access to assets from AEM in Adobe Photoshop, Adobe Illustrator, and Adobe InDesign desktop applications. You can upload the currently open document into AEM directly from Adobe Asset Link user interface from within these desktop applications.
* [Experience Manager desktop app](https://docs.adobe.com/content/help/en/experience-manager-desktop-app/using/using.html) simplifies working with assets on desktop, independent on their file type or native application that handles them. It is particularly useful to upload files in nested folder hierarchies from your local file system, as browser upload only supports uploading flat file lists.

## Additional processing {#additional-processing}

In order to have additional processing done on the uploaded assets, you can use asset processing profiles profiles  on the folder, into which assets are uploaded. They are available in the folder **[!UICONTROL Properties]** dialog.

![assets-folder-properties](assets/assets-folder-properties.png)

The following profiles are available:

* [Metadata profiles](metadata-profiles.md) allow you to apply default metadata properties to assets uploaded into that folder
* [Processing profiles](asset-microservices-configure-and-use.md#processing-profiles) allow you to apply rendition processing and generate renditions in addition to the default ones

Additionally, if Dynamic Media is enabled in your environment:

* [Dynamic Media Image profiles](dynamic-media/image-profiles.md) allow you to apply specific cropping (**[!UICONTROL Smart Cropping]** and pixel cropping) and sharpening configuration to the uploaded assets.
* [Dynamic Media Video profiles](dynamic-media/video-profiles.md) allow you to apply specific video encoding profiles (resolution, format, parameters).

>[!NOTE]
>
>Dynamic Media cropping and other operations on assets are non-destructive, that is, they do not change the uploaded original, but instead provide parameters for cropping or media transformation to be done when delivering the assets

For folders that have a processing profile assigned, the profile name appears on the thumbnail in the card view. In the list view, the profile name appears in the **[!UICONTROL Processing Profile]** column.

## Upload or ingest assets using APIs {#upload-using-apis}

Technical details of the upload APIs and protocol, and links to open-source SDK and sample clients is provided in [asset upload](developer-reference-material-apis.md#asset-upload-technical) section of the developer reference.

>[!MORELIKETHIS]
>
>* [Adobe Experience Manager desktop app](https://docs.adobe.com/content/help/en/experience-manager-desktop-app/using/introduction.html)
>* [Adobe Asset Link](https://www.adobe.com/creativecloud/business/enterprise/adobe-asset-link.html)
>* [Adobe Asset Link documentation](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html)
>* [Technical reference for asset upload](developer-reference-material-apis.md#asset-upload-technical)
