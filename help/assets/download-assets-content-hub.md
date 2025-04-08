---
title: Download assets from Content Hub
description: Learn how to download assets from the Content Hub portal
role: User
exl-id: 96d4ffba-4e3e-4496-9da2-6eb36be8331f
---
# Download assets from the Content Hub {#download-assets}

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

<!-- ![Download assets](assets/download-asset.jpg) -->
![Download assets](assets/download-asset-genstudio.jpeg)

>[!AVAILABILITY]
>
>Content Hub guide is now available in PDF format. Download the entire guide and use Adobe Acrobat AI Assistant to answer your queries. 
>
>[!BADGE Content Hub Guide PDF]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/content-hub.pdf"}

The Content Hub lets you download and share your assets. The Content Hub User Interface displays only approved assets. These assets may include images, videos, or any other digital content. The Content Hub enhances accessibility and adaptability for effective asset distribution.  

You can download single or multiple assets and their available renditions using Content Hub.

See [types of renditions available in Content Hub](#types-of-renditions).

## Download an asset and its renditions {#download-asset-renditions} 

To download an asset and its renditions, execute the following steps: 

1. Click the asset to view its properties.

1. Click ![download](/help/assets/assets/download-icon.svg) to start the download process. The Download panel lists all available asset renditions.

   >[!NOTE]
   >
   >* The renditions display only if their visibility is enabled using the [Configuration](/help/assets/configure-content-hub-ui-options.md#renditions-content-hub) User Interface.
   >* You can download all [static, dynamic, and smart crop renditions](#types-of-renditions) while downloading an asset.

1. Select one or more renditions and click **[!UICONTROL Download]**.

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

Asset renditions are different representations of an asset's original file. These can include thumbnails, optimized versions for web or mobile, watermarked or DRM-protected files, or even dynamic elements like smart crops. They do not need to match the original file type, instead, they serve to represent the asset in various use cases.

Learn more about [view and manage renditions in Experience Manager Assets](/help/assets/renditions.md).

[!DNL Experience Manager Assets] supports the following types of renditions:

* [Static renditions](/help/assets/renditions.md#static-renditions): Static renditions are pre-created versions of digital assets, typically generated during the asset ingestion or modification. They are optimized for specific uses and platforms, such as web thumbnails, mobile-friendly formats for responsive designs, or high-resolution files for printing, providing a streamlined and consistent experience.

* [Dynamic renditions](/help/assets/renditions.md#dynamic-renditions): Dynamic renditions are real-time, customized versions of assets to perform various actions, such as resizing images for different device resolutions or cropping to fit various aspect ratios. These renditions allows you to offer personalized and optimized experiences for wider requirements. Dynamic renditions of assets are created on [!DNL Adobe Experience Manager Assets] author environment.

* [Smart crop](/help/assets/dynamic-media/image-profiles.md#creating-image-profiles): The smart crop focuses solely on the essential part of an asset during the cropping process. Dynamic media smart crop for leverages artificial intelligence powered by Adobe Sensei to track the point of interest, making sure our assets look like their best on all screen sizes. [!DNL Adobe Experience Manager] smart crop displays width and height of an asset renditions along with the title. See more at [using Smart Crop with AEM Assets Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use).

  ![Renditions types](/help/assets/assets/renditions-types.png)

  
>[!NOTE]
> 
> * Dynamic and Smart Crop renditions feature is in Early Adopter phase. To get access to the capability, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).
> * Newly onboarded customers on [Dynamic Media Open API services](/help/assets/dynamic-media-open-apis-overview.md) must revise their existing image presets for approval.



