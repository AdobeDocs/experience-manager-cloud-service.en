---
title: Upload your brand approved assets to [!DNL Content Hub]
description: Learn how to upload your brand approved assets to Content Hub
role: User
exl-id: f1be7cfc-1803-4c17-bb58-947104aa883c
---
# Upload brand approved assets to Content Hub {#upload-brand-approved-assets-content-hub}

>[!CONTEXTUALHELP]
>id="upload_assets_content_hub"
>title="Upload brand approved assets to Content Hub"
>abstract="Add approved assets to Content Hub either from local file system or import assets from OneDrive or Dropbox data sources. All assets display at the top-level in Content Hub irrespective of the folder structure to enhance search capabilities."

[Content Hub users with rights to add assets](/help/assets/deploy-content-hub.md#onboard-content-hub-users-add-assets) can add assets to the Content Hub either from local file system or import assets from OneDrive or Dropbox data sources. All assets display at the top-level in Content Hub irrespective of the folder structure available on your local file system or OneDrive and Dropbox data sources to enhance the search capabilities.

>[!VIDEO](https://video.tv.adobe.com/v/3432980/?learn=on){transcript=true}

The assets marked as `Approved` in Assets as a Cloud Service are automatically available in Content Hub. For more information, see [Approve assets for Content Hub](/help/assets/approve-assets-content-hub.md).

To further enhance asset search, Content Hub allows you to:

* Define key details relevant to your asset upload, such as campaign name, keywords, channels, and so on. 

* Automatically generate more properties for each asset upon successful upload, such as, file size, format, resolution, and some other properties.

* Use the artificial intelligence provided by [Adobe AI](https://business.adobe.com/ai/adobe-genai.html) to automatically apply relevant tags to all your uploaded assets. These tags, aptly named Smart Tags, increase the content velocity of your projects by helping you find relevant assets quickly.

Ensure that you only upload your [brand approved assets to the Content Hub](/help/assets/approve-assets.md).

![Upload brand approved assets](assets/upload-brand-approved-assets.png)

## Prerequisites {#prerequisites-add-assets}

[Content Hub users with rights to add assets](/help/assets/deploy-content-hub.md#onboard-content-hub-users-add-assets) can upload assets to Content Hub.

## Add assets to Content Hub from local file system {#add-assets-local-file-system}

To add assets to Content Hub, perform the following steps:

1. Click **[!UICONTROL Add Assets]** to view the **[!UICONTROL Add your approved assets]** dialog box that enables you to create an upload.

1. In the **[!UICONTROL Drag files or folders here]** section available in the right pane, you can either drag the assets from the local file system or click **[!UICONTROL Browse]** to manually select files or folders available on the local file system. This list of files that are part of your upload are available as a list. 

   
   You can also preview selected images using the thumbnails and click the X icon to remove any particular image from the list. The X icon displays only when you hover your mouse over the image name or size. You can also click **[!UICONTROL Remove all]** to delete all items from your upload list.

   To finish the upload process and enable the **[!UICONTROL Upload button]**, you must group your assets under a Campaign name.
   
   ![Upload assets to Content Hub](assets/upload-assets-content-hub.png)

1. Define the name for your upload using the **[!UICONTROL Campaign name]** field. You can use an existing name or create a new one. The Content Hub provides you with more options as you type the name. <!--You can define multiple Campaign names for your upload. While you are typing a name, either click anywhere else within the dialog box or press the `,` (Comma) key to register the name.-->

   As a best practice, Adobe recommends specifying values in the rest of the fields as well as it creates an enhanced search experience for your uploaded assets.

1. Similarly, define values for the **[!UICONTROL Keywords]**, **[!UICONTROL Channels]**, **[!UICONTROL Timeframe]**, and **[!UICONTROL Region]** fields. Tagging and grouping assets by keywords, channels, and location enables everyone who uses your approved company content to find these assets and keep it organized.

1. Click **[!UICONTROL Upload]** to upload assets to the Content Hub. [!UICONTROL Review details] confirmation box appears. Click [!UICONTROL Continue].

1. Assets start uploading. Click [!UICONTROL New Upload] to restart the upload procedure. Click [!UICONTROL Done] to complete uploading.

Administrators can also configure the mandatory and optional fields that display while uploading assets, such as Campaign name, Keywords, Channels, and so on. For more information, see [Configure the Content Hub user interface](configure-content-hub-ui-options.md#configure-upload-options-content-hub).

## Manage assets uploaded using Content Hub {#manage-assets-uploaded-using-content-hub}

[Content Hub users with rights to add assets](/help/assets/deploy-content-hub.md#onboard-content-hub-users-add-assets) can [add assets to the Content Hub](/help/assets/upload-brand-approved-assets.md) either from local file system or import assets from OneDrive or Dropbox data sources. All assets display at the top-level in Content Hub irrespective of the folder structure available on your local file system or OneDrive and Dropbox data sources to enhance the search capabilities.

The display of assets uploaded using Content Hub depends on if you have [enabled the Auto-approval toggle](/help/assets/configure-content-hub-ui-options.md#configure-import-options-content-hub):

* If the **[!UICONTROL Auto-approval]** toggle is enabled, the assets that you upload using Content Hub are automatically available.

* If the **[!UICONTROL Auto-approval]** toggle is disabled, the assets that you upload using Content Hub do not display automatically. The assets are available in the `hydrated-assets` folder of your Assets as a Cloud Service environment. Navigate to the folder and [bulk edit](#bulk-approve-assets-content-hub) the status of those assets to `Approved` for those assets to display in Content Hub.

![Content Hub approval process](/help/assets/assets/content-hub-approval.png)

## Frequently asked questions {#faqs-content-hub-upload-assets}

### What types of assets can I upload to Content Hub and from where? {#asset-types-upload-to-content-hub}

Content Hub users with rights to add assets can upload brand approved assets from their local file system. All uploaded assets, regardless of their original folder structure, are displayed at the top-level in Content Hub to enhance search capabilities.

### How does Content Hub enhance asset search and organization? {#search-content-hub}

Content Hub enhances asset search and organization by allowing users to define key details for each upload, such as campaign name, keywords, channels, timeframe, and region. It also automatically generates additional properties for each asset (such as file size, format, and resolution) and uses Adobe AI to apply Smart Tags, making it easier and faster to find relevant assets.

### How to upload assets from my local file system to Content Hub? {#upload-assets-content-hub}

To upload assets from your local file system, click **Add Assets** to open the upload dialog. You can drag and drop files or folders, or manually browse to select them. You must group your assets under a campaign name, and it is recommended to fill in other fields like keywords, channels, timeframe, and region for better organization. Once ready, click **Upload**, review the details, and confirm to start uploading.

### How does the asset approval process work in Content Hub? {#asset-approval-content-hub}

If the Auto-approval toggle is enabled, assets uploaded using Content Hub are automatically available. If it is disabled, uploaded assets are placed in the **hydrated-assets** folder in Assets as a Cloud Service, and you need to manually bulk edit their status to **Approved** to make them display in Content Hub.

### Can I configure the fields that are mandatory or optional while uploading assets to Content Hub? {#available-fields-while-uploading-assets-to-content-hub}

Administrators can use the Configuration User Interface to define the fields that are mandatory or optional while uploading assets to Content Hub.

### What should I do if my uploaded assets do not display automatically in Content Hub? {#assets-do-not-display-in-content-hub}

If assets do not display automatically, it means the Auto-approval toggle is disabled. The assets are located in the **hydrated-assets** folder of your Assets as a Cloud Service environment. You need to bulk edit their status to **Approved** for them to appear in Content Hub.

