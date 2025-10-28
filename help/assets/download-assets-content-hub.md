---
title: Download assets from Content Hub
description: Learn how to download one or more assets and their renditions from the Content Hub portal.
role: User
exl-id: 96d4ffba-4e3e-4496-9da2-6eb36be8331f
---
# Download assets from Content Hub {#download-assets}

The [!DNL Content Hub] lets you download and share your assets. The [!DNL Content Hub] User Interface displays only approved assets. These assets may include images, videos, or any other digital content. The [!DNL Content Hub] enhances accessibility and adaptability for effective asset distribution.  

You can download single or multiple assets and their available renditions using [!DNL Content Hub].

See the [types of renditions available in Content Hub](#types-of-renditions).

## Download one or more assets and their renditions {#download-asset-renditions}

To download one or more assets and their renditions, execute the following steps: 

* To download a single asset and its renditions:
   1. Select ![download](/help/assets/assets/download-icon.svg) available on the asset card to preview the asset and its available renditions.
   1. Select the available renditions and click the **[!UICONTROL Download]** option in the dialog box to download the selected renditions as a ZIP file. If the dialog box displays an asset license (for licensed asset), accept the licensing terms and conditions and click **[!UICONTROL Download]**. 
![download an asset](/help/assets/assets/download-an-asset-CH-from-asset-card.png)
    Alternatively, click the asset thumbnail and then click ![download](/help/assets/assets/download-icon.svg) to select and view the available renditions on the dialog box before downloading them.

* To download multiple assets and their renditions:
   1. Select the assets, click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** and review the list of selected assets in the **[!UICONTROL Download assets]** dialog box. Click ![unselect](/help/assets/assets/Close.svg) next to an asset to unselect it from the list. 
   1. Select one or more renditions to download them as a ZIP file. Selecting **[!UICONTROL Smart Crop]** and **[!UICONTROL Static Renditions]** downloads all available static and smart crop renditions of each selected asset.
   1. Optional: Unselect **[!UICONTROL Create a separate folder for each asset]** to download the selected assets and their renditions as a flat hierarchy within a folder in the zip file. By default, [!DNL Content Hub] downloads the selected assets and their renditions in separate folders within a zip file.
  
      >[!NOTE]
      >
      > * Content Hub saves your selection (**[!UICONTROL Create a separate folder for each asset]**) as your preference and retains it for future downloads.
      > * **[!UICONTROL Create a separate folder for each asset]** option is available only for authenticated [!DNL Content Hub] users. [!DNL Content Hub] enables public users to download assets as individual assets.

   1. Click **[!UICONTROL Download]** to download your selected assets and their renditions. 
![download multiple assets](/help/assets/assets/bulk-asset-download-content-hub.png)

You can continue using [!DNL Content Hub] while the download is in progress. Content Hub does not interrupt your workflow during the download process.
![download multiple assets](/help/assets/assets/download-assets-notification-ch.png)
If **[!UICONTROL Download assets]** dialog box displays assets licenses, then select each license from the left pane ([!UICONTROL T&C Documents] section) to preview the license and display the selected assets associated with the license in the middle pane of the dialog box. After reviewing each license, select the renditions, click **[!UICONTROL I have read and accepted the terms & conditions mentioned above]** and select **[!UICONTROL Download]** to download them.
![download multiple assets](/help/assets/assets/download-multiple-licensed-assets-CH.png)

   >[!NOTE]
   >
   >* The renditions display only if their visibility is enabled using the [[!UICONTROL Configuration]](/help/assets/configure-content-hub-ui-options.md#renditions-content-hub) User Interface.
   >* The users with access to [[!DNL Dynamic Media with Open API capabilities]](/help/assets/dynamic-media-open-apis-overview.md) can view and download dynamic and smart crop renditions.
   >* The preview of the license displays only if the asset is approved using [!DNL Assets as a Cloud Service] authoring environment. For more information, see [Manage licensed assets on Content Hub](/help/assets/manage-licensed-assets-on-content-hub.md).

<!--

## Download an asset and its renditions {#download-asset-renditions} 

To download an asset and its renditions, execute the following steps: 

1. Click the asset to view its properties.

1. Click ![download](/help/assets/assets/download-icon.svg) to see the list of available asset renditions in the **[!UICONTROL Download]** panel.

   >[!NOTE]
   >
   >* The renditions display only if their visibility is enabled using the [Configuration](/help/assets/configure-content-hub-ui-options.md#renditions-content-hub) User Interface.
   >* You can download all [static, dynamic, and smart crop renditions](#types-of-renditions) while downloading an asset.

1. Select one or more renditions and click **[!UICONTROL Download]** to download the selected renditions as a zip file. 
While downloading a licensed asset, select **[!UICONTROL I have read and accepted the terms & conditions mentioned above]** before clicking **[!UICONTROL Download]**. You can also click **[!UICONTROL terms & conditions]** to view the asset license. The preview of the license displays only if the asset is approved using Assets as a Cloud Service authoring environment. For more information, see [Manage licensed assets on Content Hub](/help/assets/manage-licensed-assets-on-content-hub.md).

   ![Download single asset renditions](/help/assets/assets/download-single-asset-renditions.png)


If you are downloading a licensed asset, select **[!UICONTROL I have read and accepted the terms & conditions mentioned above]** and then click **[!UICONTROL Download]**. You can also click **[!UICONTROL terms & conditions]** to view the asset license. The preview of the license displays only if the asset is approved using Assets as a Cloud Service authoring environment. For more information, see [Manage licensed assets on Content Hub](/help/assets/manage-licensed-assets-on-content-hub.md).

>[!NOTE]
>
> The users with access to [Dynamic Media with Open API capabilities](/help/assets/dynamic-media-open-apis-overview.md) can view and download dynamic and smart crop renditions.

## Download multiple assets and their renditions {#download-multiple-assets-renditions} 

To download multiple assets and their renditions, execute the following steps: 

1. Select the assets and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]**. The [!UICONTROL Download assets] screen displays listing all the selected assets. 
1. Click **[!UICONTROL Download]** to select from the various download options to begin download:

    * **Download [!UICONTROL Originals]**: Select this option to download the selected assets in the original form.
    * **Download [!UICONTROL Static Renditions only]**: Select this option to download all available static renditions of assets except the original assets.
    * **Download [!UICONTROL Originals & Static Renditions]**: Select this option to download both original and static renditions of the selected assets. 

      ![Download multiple renditions](/help/assets/assets/download-multiple-renditions.png)

      >[!NOTE]
      >
      >* The renditions display only if their visibility is enabled using the [Configuration](/help/assets/configure-content-hub-ui-options.md#renditions-content-hub) User Interface.
      >* You can only download [static renditions](#types-of-renditions) while downloading multiple assets.

    If any of the selected asset is a licensed asset, click the license of the asset in left pane to see its preview, which enables you to select **[!UICONTROL I have read and accepted the terms & conditions mentioned above]** and then click **[!UICONTROL Download]**. The preview of the license displays only if the asset is approved using Assets as a Cloud Service authoring environment. For more information, see [Manage licensed assets on Content Hub](/help/assets/manage-licensed-assets-on-content-hub.md).

    <!--![download-multiple-license](/help/assets/assets/download-multiple-license.png)-->
    
<!--1. On the Content Hub homepage, select the asset and click **Download**. The **Download assets** dialog box displays a license or list of licenses associated with the selected assets in the left pane. 
1. Click a license in the left pane to see its PDF in the middle pane and the associated assets with it in the right pane. The license PDF preview is displayed only if the license is approved in your Assets as a Cloud Service environment. [Approve the license PDFs](/help/assets/approve-assets-content-hub.md) of the selected assets to see their previews.
1. Optional: Click ![remove-icon](/help/assets/assets/remove-icon.svg) to remove a license from the dialog box.
1. Select **I have read and accept all the terms and conditions mentioned above.** 
1. Click **Download** to download the selected assets.-->

<!---This dialog box displays the list of licenses associated with the selected assets in the left pane. Select a license to preview its terms and conditions (in pdf format) in the middle pane and the preview of the associated assets to the license in the right. Reviewed licenses are highlighted in light blue.


The dialog box that displays depends on whether the download list includes expired assets or only non-expired assets. <br/>
**Download expired assets dialog box:** This dialog box displays the expired assets' preview along with their expiry date in the left pane. The expired assets' count out of total selected displays in the right pane. Click **Proceed with all assets** to download expired assets with other assets (if present). The Download assets dialog box displays. See the [Download assets dialog box](#Download-asset-dialog-box) to proceed further.
    
    >[!NOTE]
    >
    >[Enable the download option for expired assets](/help/assets/configure-content-hub-ui-options.md#expired-assets-content-hub) to download them. Only expired assets that have enabled downloading are available for download.

   <a id="Download-asset-dialog-box"></a> **Download assets dialog box:** This dialog box displays the list of licenses associated with the selected assets in the left pane. Select a license to preview its terms and conditions (in pdf format) in the middle pane and the associated assets' preview and their count in the right pane. Reviewed licenses are highlighted in light blue.

    >[!NOTE]
    >
    > The **Download Asset dialog box** previews licensing terms and conditions only for approved licenses. [Approve the assets' licenses](/help/assets/approve-assets-content-hub.md) before downloading them to preview their licensing terms in the **Download Asset dialog box**.

1. Click  ![remove-icon](/help/assets/assets/remove-icon.svg) to remove a license from the download dialog box. 

1. Accept the terms and conditions and then click **Download** to download assets associated with the available licenses in the left pane.-->
<!--![download-multiple-license](/help/assets/assets/download-multiple-license.png)-->

<!---
### Download non-licensed Assets {#download-non-licensed-assets}

 To download non-licensed assets, select the assets and click ![download](/help/assets/assets/download-icon.svg) from the top rail.-->
   
## Types of renditions {#types-of-renditions} 

Asset renditions are different representations of an asset's original file. These renditions can include thumbnails, optimized versions for web or mobile, watermarked or DRM-protected files, or even dynamic elements like smart crops. They do not need to match the original file type, instead, they serve to represent the asset in various use cases.

Learn more about [view and manage renditions in [!DNL Experience Manager Assets]](/help/assets/renditions.md).

[!DNL Experience Manager Assets] supports the following types of renditions:

* [Static renditions](/help/assets/renditions.md#static-renditions): Static renditions are pre-created versions of digital assets, typically generated during the asset ingestion or modification. They are optimized for specific uses and platforms, such as web thumbnails, mobile-friendly formats for responsive designs, or high-resolution files for printing, providing a streamlined and consistent experience.

* [Dynamic renditions](/help/assets/renditions.md#dynamic-renditions): Dynamic renditions are real-time, customized versions of assets to perform various actions, such as resizing images for different device resolutions or cropping to fit various aspect ratios. These renditions allow you to offer personalized and optimized experiences for wider requirements. Dynamic renditions of assets are created on [!DNL Adobe Experience Manager Assets] author environment. For information on steps required to enable Dynamic renditions, see [Enable Dynamic renditions](#enable-dynamic-media-renditions).

* [Smart crop](/help/assets/dynamic-media/image-profiles.md#creating-image-profiles): The smart crop focuses solely on the essential part of an asset during the cropping process. Dynamic Media smart crop leverages artificial intelligence powered by Adobe Sensei to track the point of interest, making sure our assets look their best on all screen sizes. [!DNL Adobe Experience Manager] smart crop displays width and height of an asset renditions along with the title. See more at [using Smart Crop with AEM Assets Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use).

   Smart Crop renditions display and are available for download only if you have access to [Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md). Smart Crop renditions are available only for image assets.

  ![Renditions types](/help/assets/assets/renditions-types.png)

  >[!NOTE]
  > 
  > The Download panel displays only custom static renditions. The default `cq5dam.*` thumbnails do not display in Content Hub.

### Enable Dynamic renditions {#enable-dynamic-media-renditions}

To enable Dynamic renditions:

1. Ensure that you have access to [Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md).

   Once you have access to Dynamic Media with OpenAPI capabilities, all assets marked as `Approved` are available for public delivery using Dynamic Media.

1. Set the [approval target of the asset](/help/assets/approve-assets-content-hub.md#set-approval-target) to Content Hub to approve assets only for Content Hub.

1. Enable  the **[!UICONTROL Enable availability of renditions]** toggle available in the **[!UICONTROL Renditions]** tab of the [Configuration](/help/assets/configure-content-hub-ui-options.md#access-configuration-options-content-hub) User Interface.

1. Re-save the existing image presets to make them available on Content Hub. It is applicable only if you have newly onboarded to Dynamic Media with OpenAPI.

   To re-save the existing image presets, navigate to the Admin view and select **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Image Presets]**. Select a preset, click **[!UICONTROL Edit]** and then click **[!UICONTROL Save]**.


  
   >[!NOTE]
   > 
   > Dynamic renditions are available only for image assets.



