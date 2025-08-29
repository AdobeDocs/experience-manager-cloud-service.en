---
title: Optimize images using Dynamic Media with OpenAPI Capabilities
description: Learn how to optimize images on the fly before public delivery using the image optimization capabilities of Dynamic Media with OpenAPI Capabilities
role: Admin, user 
feature: Asset Management, Publishing, Collaboration, Asset Processing
---

# Optimize images using Dynamic Media with OpenAPI Capabilities{#Optimize-images-using-Dynamic-Media-with-OpenAPI-Capabilities}
 
[!DNL Dynamic Media with OpenAPI capabilities] offers image optimization capabilities such as [!DNL Smart Crop], [!DNL Image Presets], and [!DNL Smart Imaging]. These capabilities help deliver high-quality, responsive images that load fast across different devices and networks.

## Smart Crop{#smart-crop-using-dynamic-media-with-openapi-capabilities}

[!DNL Smart Crop] is a dynamic sizing capability of [!DNL Dynamic Media with OpenAPI capabilities]. [!DNL Smart Crop] is an advanced image processing technique that uses AI-powered content-aware cropping to intelligently crop images for various screen sizes while preserving the visual context in cropped versions. The AI analyses the image to identify the focal point or intended point of interest, and then automatically crops the image to retain the focal point in all the cropped versions. [!DNL Smart Crop], a key element of responsive design, provides a cost-effective and time-efficient way to crop images. 

See the [Dynamic Media Image Profiles](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles) article to learn how to [create Smart Crop renditions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles#creating-image-profiles) in [!DNL Admin View], [apply them to folders](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles#applying-an-image-profile-to-folders), or [edit renditions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles#editing-the-smart-crop-or-smart-swatch-of-a-single-image) already applied to an image or a folder. Learn to create a [!DNL Smart Crop] step by step in this [video](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use).

The [!DNL Smart Crop] parameter expects that named-smartcrop-profiles exist and have been applied to the asset. See [Smart Crop profiles](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=smartcrop&t=request) to learn more about the [!DNL Smart Crop] parameter and how named [!DNL Smart Crop] profiles are applied.

>[!IMPORTANT]
>
> You can create [!DNL Smart Crop] renditions only in the Admin view. 

## Image presets{#image-presets-using-dynamic-media-with-openapi-capabilities}

Transform images on the fly using [!DNL Image Presets] capability in [!DNL Dynamic Media with OpenAPI capabilities]. An [image preset](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=preset&t=request) is a predefined set of sizing and formatting rules for an output image.

[!DNL Dynamic Media with OpenAPI capabilities] uses preset names to transform an image on the fly and generate its rendition instantly. When you request an image through a [!DNL Dynamic Media with OpenAPI] delivery URL that includes a preset parameter, [!DNL DM with OpenAPI] applies the preset's transformations, creates the rendition on demand, and delivers it to the user.

You can apply a single preset to multiple images through their [!DNL Dynamic Media with OpenAPI] delivery URLs. This ensures consistent formatting across assets without manually editing each one.

See [managing Image Presets](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/managing-image-presets) article to learn [how to create image presets in Admin View](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/managing-image-presets#creating-image-presets), and [how to create responsive image presets](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/managing-image-presets#creating-a-responsive-image-preset) that automatically adapt assets to fit different screen sizes.

### Benefits of using Image presets{#benefits-of-image-presets}

[!DNL Image Presets] provide several advantages for managing and delivering images in [!DNL Dynamic Media with OpenAPI]. Some of the key benefits include the following:

* Presets make image delivery URLs shorter. Instead of adding multiple image modifiers that make the delivery URL longer, use a single preset. Shorter URLs are easier to manage and ensure consistent image delivery across websites, mobile apps, emails, and other channels.
* Image presets create just-in-time renditions from a source image file. This on-demand rendition generation capability eliminates the need to create and store multiple static renditions of the same file, saving both time and storage.
* Apply a single preset to a large set of assets at once, avoiding manual edits to each asset individually, ensuring consistent formatting, and enabling scalability.
* When you update a preset's parameters, all images using that preset are reformatted automatically. This streamlines editing by centralizing formatting updates, eliminating the need to re-edit individual assets or web code.
* Improves efficiency and performance with dynamic renditions cached by the CDN, resulting in faster loading and optimized performance across devices and networks.

### Use Image presets{#use-image-presets-using-dynamic-media-with-openapi-capabilities}

After creating the [!DNL Image Presets], you can use them for the following workflows:

* **[Use presets in image delivery URL to create its renditions on-the-fly before delivering it to the end user](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/linking-urls-to-yourwebapplication)**  
Presets make your delivery URLs shorter and easier to use.  Each preset name serves as a unique identifier in the delivery URL. Instead of adding multiple modifiers to an asset's delivery URL, reference the preset name to generate its rendition instantly. [Learn to appply Dynamic Media Image Presets to your image](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-presets).
The following example compares a URL with a preset to a URL without a preset.

  **URL without a preset (long URL)**:

  `https://delivery-p30902-e145436-cmstg.adobeaemcloud.com/adobe/assets/urn:aaid:aem:393d5579-5be2-49a5-ac5f-8fed72bfb614/as/AdobeStock_63266433.avif?width=400&height=300&fit=crop&qualit=85&sharpen=true`

  **URL with a preset (short URL)**: 

  `https://delivery-p30902-e145436-cmstg.adobeaemcloud.com/adobe/assets/urn:aaid:aem:393d5579-5be2-49a5-ac5f-8fed72bfb614/as/AdobeStock_63266433.avif?preset=thumbnail`
The preset thumbnail bundles the same image modifier settings.
</br>
* **Use presets during authoring in AEM Sites**
Authors can select [!DNL Image Presets] during page editing in [!DNL AEM Sites] authoring page when [!DNL Dynamic Media] support is enabled. 
Execute the following steps to use image presets in your authoring page:
  1. Navigate to your Sites authoring page. 
  1. Execute the steps in [Access remote assets in AEM Page Editor](/help/assets/integrate-remote-approved-assets-with-sites.md#access-remote-assets-in-aem-page-editor) section to use the [!DNL Asset Selector] panel for selecting an asset.
  1. In the [!DNL asset selector] panel, scroll down to **[!UICONTROL  Preset type]**, and specify `Preset=Preset Name` in the **[!UICONTROL Image Modifiers]** field.
![preset](/help/assets/assets/preset-in-asset-selector-panel.png)

## Smart Imaging{#use-smart-imaging-using-dynamic-media-with-openapi-capabilities}

[Smart imaging](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/) automatically optimizes the image delivery to provide the best balance of visual quality, image size, and response time. This results in faster page loads, reduced bandwidth usage, and a consistently high-quality experience across devices and network conditions. [!DNL Smart Imaging] includes the following capabilities:

* [Auto Format Conversion](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=auto-format&t=request): [!DNL Dynamic Media with OpenAPI] converts images to modern, web-optimized formats including AVIF or WEBP automatically based on browser capabilities and [license-entitlement](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dm-prime-ultimate), irrespective of the requested format. AVIF and WEBP formats provide better compression, making images smaller and faster to deliver and load.
[!DNL DM with OpenAPI] uses AVIF as the default format. AVIF handles all the browser capabilities. 
[!DNL Dynamic Media with OpenAPI] uses the `auto-format` query parameter to control the behaviour of browser for coverting an image to various formats.

**Auto promotion:** By default the `auto-format` query parameter is set to `true`. When `auto-format` is `true`, the requested format is ignored and a web-optimized format(AVIF or WEBP) based on image-characteristics, browser capabilities, and [license-entitlement](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dm-prime-ultimate) is selected automatically. 

When auto-format is true (enabled), the system auto-optimizes and delivers AVIF if supported (and licensed), otherwise delivers WEBP. JPEG is delivered only when the browser doesn't support AVIF or WEBP and the image doesn't have an alpha channel (transparency).

**Auto demotion:** The user can disable the default setting for auto format conversion and set the `auto-format` query parameter to `false`.

</br>

* **Automatic Quality Adjustment**: Image quality-factor is automatically applied based on the client's network conditions, ensuring faster image delivery and loading under all conditions.

  * **Quality parameter**: The quality parameter ensures the best image quality, regardless of load time, on the client's current network speed.
  The quality parameter sets a fixed compression level for the output image, with values ranging from 1 to 100. 
  Learn more about the [quality parameter](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=quality&t=request).

  * **Max-quality parameter**: The max-quality parameter enables faster image delivery while ensuring the best possible quality based on the client's current network speed. It has the following key properties:
    * ***Prioritizes load time***: It reduces image quality when the network is slow to load images faster.
    * ***Maintains best quality***: Even when reduced, the image quality is still the highest allowed between 1–100 for that network speed.
    
    Learn more about the [max-quality parameter](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=quality&t=request).

  The following summarizes both the parameters:

  * If both [!DNL quality] and [!DNL max-quality] are specified, [!DNL quality] takes precedence.
  * If only [!DNL quality] is specified, the quality is delivered regardless of load time for an existing network speed.
  * If only [!DNL max-quality] is specified, the output quality dynamically adjusts based on network conditions, capped at the [!DNL max-quality] value.
  * If neither is specified, the system applies dynamic optimization with a default max-quality of 85.

---





A higher value results in better visual quality but a larger file size, while a lower value reduces file size and image quality. For example, setting quality=85 ensures that the image is always delivered at 85 quality, regardless of network conditions. Learn more about the [quality parameter](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=quality&t=request). 
The max-quality parameter, on the other hand, enables adaptive delivery based on the client's network conditions. It defines the maximum allowed quality (1–100), but the actual delivered quality may be reduced below this value if the network is slow, ensuring faster load times. For instance, if max-quality=85 is specified, images are delivered at 85 quality on fast networks but at a lower quality on slower networks to optimize performance. Learn more about the [max-quality parameter](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=quality&t=request).
  
  * If both [!DNL quality] and [!DNL max-quality] are specified, [!DNL quality] takes precedence.
  * If only [!DNL quality] is specified, that value is used.
  * If only [!DNL max-quality] is specified, the output quality dynamically adjusts based on network conditions, capped at the [!DNL max-quality] value.
  * If neither is specified, the system applies dynamic optimization with a default max-quality of 85.


