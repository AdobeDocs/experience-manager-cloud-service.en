---
title: View and manage renditions in Experience Manager Assets
description: Learn how AEM Assets and Dynamic Media simplify effective image management with static and dynamic image renditions.
exl-id: 006dc493-c400-4d0f-b314-c1978582b7fb
feature: Renditions
role: User
---
# View and manage renditions in Experience Manager Assets{#renditions}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

Renditions in Adobe Experience Manager (AEM) are customized versions of digital assets, such as images, designed for different devices and platforms to ensure optimal performance. AEM facilitates easy creation and management of these renditions, enhancing user experience. You can create thumbnails, optimize images for web or mobile, add watermarks, view and download dynamic renditions or smart crop renditions, and do much more.

Dynamic Media image presets, and Smart Crop renditions promote systematic image management that aligns with brand standards, maximizing brand cohesion. This simplifies the process of quickly locating and using dynamic image renditions as needed without any admin access.

Renditions are classified as static and dynamic, each type presenting unique features and capabilities that are discussed further in detail.

## Static renditions {#static-renditions}

Static renditions are pre-generated versions of digital assets, usually created during asset ingestion or modification. These renditions are optimized for specific purposes and platforms, such as web thumbnails, mobile-friendly formats for responsive design, or high-resolution versions for printing, ensuring an efficient and consistent experience.
Learn [how to view and download](#view-dynamic-renditions) static renditions in [!DNL Experience Manager Assets].

## Dynamic renditions {#dynamic-renditions}

Dynamic renditions are customized versions of assets created in real-time to meet specific needs, such as resizing images based on device resolution or cropping to fit different aspect ratios.
These renditions enable organizations to deliver personalized and optimized experiences to diverse audience needs. You can view and download dynamic renditions in [!DNL Experience Manager Assets].

## Dynamic Media renditions {#dynamic-media-renditions}

Access Dynamic Media renditions from the Assets view.

### Before you begin

* You must be a licensed AEM Dynamic Media user.
* Use [!UICONTROL Admin view] to set up: 
    * [Smart Crop Image Profiles](/help/assets/dynamic-media/image-profiles.md#creating-image-profiles) 
    * [Image presets](/help/assets/dynamic-media/managing-image-presets.md)

    You can [switch the view](/help/assets/assets-view-introduction.md#how-to-access-assets-view) later to preview dynamic renditions in the Assets view.
* Publish assets to Dynamic Media to make their Dynamic Media renditions available in Assets View. See [Publish Assets to AEM and Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/assets-view/publish-assets-to-aem-and-dm) for the publishing information.


### View and download Dynamic Media renditions {#view-download-dm-renditions}

To view or download dynamic renditions of images in Experience Manager Assets, follow these steps:

1. Go to **[!UICONTROL Assets Management]** > **[!UICONTROL Assets]**.

1. Navigate to the applicable asset folder.

1. Click the asset you need to view and click **[!UICONTROL Details]**.

1. In the right menu, click **[!UICONTROL Dynamic Media]** icon. The **[!UICONTROL Dynamic Media]** panel displays Dynamic Media and Smart Crop renditions.

    ![dynamic renditions](/help/assets/assets/dm-scene7-renditions.png)
    <!-- ![dynamic renditions](assets/preset_smart_crop_view.png) -->

1. Select the rendition to preview and click **Copy URL** to copy the URL of the selected rendition. Click **Download Rendition** to download the renditions of image assets.
1. Select the Smart Crop rendition to preview and click **Copy URL** to copy the URL of the selected rendition.
1. Click ![download icon](assets/do-not-localize/download-icon.png) to download all available smart crop renditions as a single zip file.
![download icon](/help/assets/assets/smartcrop-rendition.png)

   >[!NOTE]
   >
   >These renditions are available only for image assets.

## Dynamic Media with OpenAPI Capabilities renditions {#dm-with-openapi-renditions}

Access Dynamic Media with OpenAPI Capabilities renditions from Assets view.

### Before you begin

* You must be a licensed AEM Dynamic Media user.
* Assets within the repository must be approved and licensed. See [Approve assets in Experience Manager ](/help/assets/approve-assets.md#copy-delivery-url-approved-assets) to approve the assets.

### View Dynamic Media with OpenAPI Capabilities renditions {#view-download-dm-with-openapi-renditions}

1. Select the asset and click **Details**.
1. Click the Dynamic Media icon available in the right pane. The Dynamic Media panel diaplays the Dynamic Media with OpenAPI Capabilities rendition for all asset types. 
![download icon](/help/assets/assets/dm-with-openapi-copy-url.png)
1. Select **Dynamic Media with OpenAPI** option and then click **Copy URL** to copy the delivery URL of the asset.


