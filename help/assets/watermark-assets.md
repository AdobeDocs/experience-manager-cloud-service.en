---
title: How to watermark your assets in AEM?
description: Learn how to add a digital watermark to your assets in AEM. Watermarks can help users verify the authenticity and copyright ownership of the assets.
contentOwner: AG
feature: Asset Management,Publishing
role: User, Admin
exl-id: 210f8925-bd15-4b4a-8714-5a1486eeb49e
---
# Watermark your assets {#watermark-assets}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/watermarking.html)                  |
| AEM as a Cloud Service     | This article         |

[!DNL Adobe Experience Manager Assets] lets you add a digital watermark to images and videos. [!DNL Assets] supports applying an image as a watermark to other image files. Watermarks can help users verify the authenticity and copyright ownership of the assets. Also, a watermark can be used to indicate a document's state like confidential, draft, validity, and so on.

To configure [!DNL Experience Manager] to watermark assets:

1. A PNG file is applied as a watermark. Upload this file to your DAM repository.

1. Navigate to **[!UICONTROL Tools > Assets > Assets Configurations]**.

1. Click **[!UICONTROL System Watermarking Profile]**.

1.  On the [!UICONTROL System Watermarking Profile page], specify the image path uploaded  to your DAM repository in step 1.

1. Specify the watermark scale, ranging from 0.0 to 1.0, relative to rendition width, in the **[!UICONTROL Scale]** field.

1. Click **[!UICONTROL Save]**.
   
   ![Asset Duplication Detector](assets/system-watermarking-profile.png)

   >[!NOTE]
   >
   >If you have configured System Watermarking Profile using `com.adobe.cq.assetcompute.impl.profile.WatermarkingProfileServiceImpl.cfg.json` configuration file (OSGi configuration), you can continue to use it, however, Adobe recommends using the new method.

   
1. [Create a processing profile](/help/assets/asset-microservices-configure-and-use.md#create-custom-profile) to use asset microservices to apply the watermark.

   ![Asset processing profile to create watermark](assets/watermark-processing-profile.png)

   Ensure that you enable the **[!UICONTROL Watermark]** toggle while creating the processing profile.

1. [Apply the processing profiles to a folder](/help/assets/asset-microservices-configure-and-use.md#use-profiles) to create watermarked assets.

## Tips and limitations {#tips-limitations-bestpractices}

* You can use a single configuration to watermark all your assets. Only one image is used for watermarking and its width is fixed.
* You can place the watermark at the center without tiling.
* Text-based watermarks are not supported.

**See also**

* [Translate Assets](translate-assets.md)
* [Assets HTTP API](mac-api-assets.md)
* [Assets supported file formats](file-format-support.md)
* [Search assets](search-assets.md)
* [Connected assets](use-assets-across-connected-assets-instances.md)
* [Asset reports](asset-reports.md)
* [Metadata schemas](metadata-schemas.md)
* [Download assets](download-assets-from-aem.md)
* [Manage metadata](manage-metadata.md)
* [Search facets](search-facets.md)
* [Manage collections](manage-collections.md)
* [Bulk metadata import](metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

>[!MORELIKETHIS]
>
>* [Asset microservices overview](/help/assets/asset-microservices-overview.md).
>* [Use asset microservices with processing profiles](/help/assets/asset-microservices-configure-and-use.md).
