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

The Content Hub lets you download and share your assets. These assets may include images, videos, or any other digital content. The Content Hub enhances accessibility and adaptability for effective asset distribution.  

You can download single asset or multiple assets using the Content Hub. The original versions of the asset are downloaded.

## Prerequisites {#prerequisites}

[Content Hub users](deploy-content-hub.md#onboard-content-hub-users) can perform actions mentioned in this article.

## Download asset {#download-single-asset} 

[Approve asset's license](/help/assets/approve-assets-content-hub.md) before downloading.

### Single Download {#single-download-asset} 

Select an asset and click ![download](/help/assets/assets/download-icon.svg) from the top rail. The Download asset dialog box displays the asset's license. Accept the licensing terms and conditions and click **Download**.
Alternatively, click ![download](/help/assets/assets/download-icon.svg) in the asset card to download the asset. 

### Multi Download {#multi-download} 

1. Select the assets and click ![download](/help/assets/assets/download-icon.svg) from the top rail. The dialog box that displays depends on whether the download list includes expired assets or only non-expired assets.

   #### Download expired assets dialog box{#download-dialog-box-expired-assets} 

    This dialog box displays the expired assets' preview along with their expiry date on the left pane and the expired assets' count out of total selected on the right pane. Click **Proceed with all assets** to download expired assets with other assets (if present). The Download assets dialog box displays. See [Download assets dialog box](#download-asset-dialog-box) to proceed further.
    
    >[!NOTE]
    >
    >Expired assets with downloading disabled can't be downloaded. [Enable download for expired assets](/help/assets/configure-content-hub-ui-options.md#expired-assets-content-hub) to download them.

   #### Download assets dialog box {#download-asset-dialog-box}
 
    This dialog box displays the list of licenses associated with the selected assets in the left pane. Select a license to preview its terms and conditions (in pdf format) in the middle pane and the associated assets' preview and their count in the right pane. Reviewed licenses are highlighted in light blue.

    >[!NOTE]
    >
    >Unapproved licenses don't preview the licencing terms in the **Download asset dialog box**. [Approve asset's license](/help/assets/approve-assets-content-hub.md#approve-assets-for-content-hub) before downloading to preview the licensing terms.

1. Click  ![remove-icon](/help/assets/assets/remove-icon.svg) to remove a license from the download dialog box. 
1. Accept the terms and conditions and then click **Download** to download assets associated with the available licenses in the left pane.
![download-multiple-license](/help/assets/assets/download-multiple-license.png)

### Download non-licensed assets {#download-non-licensed-assets}

 To download non-licensed assets, select the assets and click ![download](/help/assets/assets/download-icon.svg) from the top rail.

    





