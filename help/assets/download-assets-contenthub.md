---
title: Download assets from Content Hub
description: Learn how to download assets from the Content Hub portal
role: User
exl-id: 96d4ffba-4e3e-4496-9da2-6eb36be8331f
---
# Download assets from the Content Hub {#download-assets}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

<!-- ![Download assets](assets/download-asset.jpg) -->
![Download assets](assets/download-asset-genstudio.jpeg)

>[!AVAILABILITY]
>
>Content Hub guide is now available in PDF format. Download the entire guide and use Adobe Acrobat AI Assistant to answer your queries. 
>
>[!BADGE Content Hub Guide PDF]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/content-hub.pdf"}

The Content Hub lets you download and share your assets. The Content Hub UI displays approved assets. These assets may include images, videos, or any other digital content. The Content Hub enhances accessibility and adaptability for effective asset distribution.  

You can download a single asset or multiple assets or the available renditions of asset(s) using the Content Hub.

## Download single asset {#download-single-asset} 

To download a single asset, execute the following steps: 

1. Select an asset and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]**. The [!UICONTROL Download assets] screen appears.

    ![Download single asset renditions](/help/assets/assets/download-single-asset-renditions.png)

1. Select from the available download options. You can download the original asset or [renditions](/help/assets/download-assets-content-hub.md#renditions-content-hub) available for the selected asset.
1. Click **[!UICONTROL Download]**.

## Download multiple assets {#download-multiple-assets} 

To download multiple assets, execute the following steps: 

1. Select the assets and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]**. The [!UICONTROL Download assets] screen appears listing all the selected assets.
1. [Optional] You can manually exclude the assets, if required. The download button reflects the count of selected items. 
1. Select from the various download options to begin download:

    * **Download [!UICONTROL Originals]**: Select this option to download the selected assets in the original form.
    * **Download [!UICONTROL Renditions only]**: A rendition is the customized version of digital assets, such as images, documents, and so on, designed for different devices and platforms to ensure optimal performance. An asset can have multiple renditions. This option lets you download all the available renditions of the selected assets, if available.
    * **Download [!UICONTROL Originals & All renditions]**: Select this option to download both original and renditions of the selected assets. 

    ![Download multiple renditions](/help/assets/assets/download-multiple-renditions.png)
    
## Download single licensed asset {#download-licensed-asset}

To download a licensed asset, execute the following steps:

1. Select an asset and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]**. The [!UICONTROL Download assets] screen appears.

    ![single-download-dialog-box](/help/assets/assets/asset-dialog-box-for-single-download.png)

1. Select **I have read and accepted the terms & conditions mentioned above**, and then click **Download**.
    
    * [Optional] To view terms & conditions of the licensed asset, select an asset and click ![download](/help/assets/assets/download-icon.svg) on the right pane. Click the terms and conditions link to display the license PDF of the asset.
    * [Optional] The license PDF preview is displayed only if the license is approved in your Assets as a Cloud Service environment. Additionally, [Approve the license PDFs](/help/assets/approve-assets-content-hub.md) of the selected assets to see their previews.

1. Select from the available download options. You can download the original asset or [renditions](/help/assets/download-assets-content-hub.md#renditions-content-hub) available for the selected asset.
1. Click **[!UICONTROL Download]**.

<!--1. On the Content Hub homepage and select the asset.
1. Click ![download](/help/assets/assets/download-icon.svg) in the right pane. The **Download** panel displays the asset renditions.
![single-download-dialog-box](/help/assets/assets/asset-dialog-box-for-single-download.png)
1. [Optional] Click the rendition to preview it.
1. Click the terms and conditions link to display the license PDF of the asset. The license PDF displays only if it is approved in your Assets as a Cloud Service Environment. [Approve the license PDF](/help/assets/approve-assets-content-hub.md) of the asset before downloading to see its preview in the dialog box.
1. Select **I have read and accepted the terms & conditions for this asset**, and then click **Download** to download the asset.

Alternatively, select the asset and click **Download** to download the asset directly.-->

## Download multiple licensed assets{#download-multiple-licensed-assets} 

To download multiple licensed assets, execute the following steps:

1. Select the assets and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]**. The [!UICONTROL Download assets] screen appears.

    ![download-multiple-license](/help/assets/assets/download-multiple-license.png)

1. Select **I have read and accepted the terms & conditions mentioned above**, and then click **Download**.

    To view terms & conditions of a licensed asset, see optional steps mentioned in [Download single licensed asset](#download-licensed-asset).

1. Select from [various download options to begin download](#download-multiple-assets). You can download the original asset or [renditions](/help/assets/download-assets-content-hub.md#renditions-content-hub) available for the selected assets.

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

    





