---
title: Optimize images using Dynamic Media with OpenAPI Capabilities
description: Learn how to optimize images on the fly before public delivery using the image optimization capabilities of Dynamic Media with OpenAPI Capabilities
role: Admin
feature: Asset Management, Publishing, Collaboration, Asset Processing
exl-id: 7822732b-e2b9-4b35-b92b-cb7b31d84489
---
# Optimize images using Dynamic Media with OpenAPI Capabilities{#Optimize-images-using-Dynamic-Media-with-OpenAPI-Capabilities}
 
[!DNL Dynamic Media with OpenAPI capabilities] offers image optimization capabilities such as [!DNL Smart Crop], [!DNL Image Presets], and [!DNL Smart Imaging]. These capabilities help deliver high-quality, responsive images that load fast across different devices and networks.

## Smart Crop{#smart-crop-using-dynamic-media-with-openapi-capabilities}

[Smart Crop](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=smartcrop&t=request) is a dynamic sizing capability of [!DNL Dynamic Media with OpenAPI capabilities]. [!DNL Smart Crop] is an advanced image processing technique that uses AI-powered content-aware cropping to intelligently crop images for various screen sizes while preserving the visual context in cropped versions. The AI analyses the image to identify the focal point or intended point of interest, and then automatically crops the image to retain the focal point in all the cropped versions. [!DNL Smart Crop], a key element of responsive design, provides a cost-effective and time-efficient way to crop images. 

See the [Dynamic Media Image Profiles](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles) article to learn how to [create Smart Crop renditions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles#creating-image-profiles) in [!DNL Admin View], [apply them to folders](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles#applying-an-image-profile-to-folders), or [edit renditions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles#editing-the-smart-crop-or-smart-swatch-of-a-single-image) already applied to an image or a folder. Learn to create a [!DNL Smart Crop] step by step in this [video](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use).

The [!DNL Smart Crop] parameter expects that named-smartcrop-profiles exist and have been applied to the asset. See [Smart Crop profiles](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=smartcrop&t=request) to learn more about the [!DNL Smart Crop] parameter and how named [!DNL Smart Crop] profiles are applied.

>[!IMPORTANT]
>
> You can create [!DNL Smart Crop] renditions only in the Admin view. 

## Image presets{#image-presets-using-dynamic-media-with-openapi-capabilities}

Transform images on the fly using [Image Presets](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=preset&t=request) capability in [!DNL Dynamic Media with OpenAPI capabilities]. An [!DNL image preset] is a predefined set of sizing and formatting rules for an output image.

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

* [Use presets in image delivery URL to create its renditions on-the-fly before delivering it to the end user](#use-presets-in-delivery-urls)
* [Use presets during authoring in AEM Sites](#use-presets-during-authoring-in-aem-sites)

#### Use presets in image delivery URL{#use-presets-in-delivery-urls}

Presets make your delivery URLs shorter and easier to use.  Each preset name serves as a unique identifier in the delivery URL. Instead of adding multiple modifiers to an asset's delivery URL, reference the preset name to generate its rendition instantly. [Learn to appply Dynamic Media Image Presets to your image](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-presets).
The following example compares a URL with a preset to a URL without a preset.

**URL without a preset (long URL)**:

```
https://delivery-p30902-e145436-cmstg.adobeaemcloud.com/adobe/assets/urn:aaid:aem:393d5579-5be2-49a5-ac5f-8fed72bfb614/as/AdobeStock_63266433.avif?width=400&height=300&fit=crop&qualit=85&sharpen=true
```

**URL with a preset (short URL)**: 

```
https://delivery-p30902-e145436-cmstg.adobeaemcloud.com/adobe/assets/urn:aaid:aem:393d5579-5be2-49a5-ac5f-8fed72bfb614/as/AdobeStock_63266433.avif?preset=thumbnail
```

The preset thumbnail bundles the same image modifier settings.

#### Use presets during authoring in AEM Sites{#use-presets-during-authoring-in-aem-sites}

Authors can select [!DNL Image Presets] during page editing in [!DNL AEM Sites] authoring page when [!DNL Dynamic Media] support is enabled. 
Execute the following steps to use image presets in your authoring page:
1. Navigate to your Sites authoring page. 
1. Execute the steps in [Access remote assets in AEM Page Editor](/help/assets/integrate-remote-approved-assets-with-sites.md#access-remote-assets-in-aem-page-editor) section to use the [!DNL Asset Selector] panel for selecting an asset.
1. In the [!DNL asset selector] panel, scroll down to **[!UICONTROL Preset type]**, and specify `Preset=Preset Name` in the **[!UICONTROL Image Modifiers]** field and click **[!UICONTROL Done]**.
![preset](/help/assets/assets/preset-in-asset-selector-panel.png)

## Smart Imaging{#use-smart-imaging-using-dynamic-media-with-openapi-capabilities}

When you use [!DNL Dynamic Media with OpenAPI capabilities] for image delivery, images are automatically optimized through [Smart imaging](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/). Optimized delivery ensures images load faster, have maximum visual quality, and minimal file size. This results in the fastest page loads and consistently high visual quality across devices and networks, while consuming minimal bandwidth, making your website faster and more responsive.

[!DNL Smart Imaging] includes the following capabilities:

* [Auto format conversion](#auto-format-conversion)
* [Network bandwidth optimisation](#network-bandwidth-optimisation) 

### Auto format conversion{#auto-format-conversion}

[!DNL Dynamic Media with OpenAPI] [automatically converts images to modern, web-optimized formats such as AVIF or WEBP](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=auto-format&t=request). The conversion depends on the browser's capabilities and [license-entitlement](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dm-prime-ultimate), regardless of the requested format.

AVIF and WEBP formats provide better compression, making images smaller and faster to deliver and load. AVIF is used as the default format as it handles all the browser capabilities. 

[!DNL Dynamic Media with OpenAPI] uses the `auto-format` query parameter to control the behaviour of browser for coverting an image to various formats for optimized delivery. Auto format conversion includes **auto promotion** and **auto demotion**. When the system promotes a web-optimized format (AVIF or WEBP) over JPEG or PNG for delivery, it is called auto-promotion.

By default, the `auto-format` query parameter is set to `true`. When `auto-format` is enabled (true), the system ignores the requested format and automatically selects a web-optimized format (AVIF or WEBP) based on image characteristics, browser capabilities, and [license-entitlement](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dm-prime-ultimate). 

When `auto-format` is true, the system delivers the image format in the following sequence:

* ***AVIF***: AVIF is delivered if the browser supports it and the license allows it. This is called as auto promotion.
* ***WEBP***: WEBP is delivered if AVIF is not supported or licensed. This is also auto promotion.
* ***JPEG***: JPEG is delivered only when AVIF and WEBP are unsupported, and the image has no alpha channel (transparency). This is called as auto demotion.
* ***PNG***: PNG is delivered when the browser does not support modern formats and the image has alpha channel (transparency). This is also called auto demotion.

Disable `auto-format` by setting the query parameter to `false`, then specify the required format to get the image delivered in that format.

### Network bandwidth optimisation{#network-bandwidth-optimisation}

Images are automatically optimized based on the client's network conditions to ensure faster delivery and smooth loading. The [Quality](#quality-parameter) and [Max-quality](#max-quality-parameter) parameters automatically adjusts the quality by controlling the image compression levels, with values ranging from 1 to 100. 

See the following key behaviors of `quality` and `max-quality `parameters:

* If both [!DNL quality] and [!DNL max-quality] are specified, [!DNL quality] takes precedence.
* If only [!DNL quality] is specified, the quality is delivered regardless of load time based on network speed.
* If only [!DNL max-quality] is specified, the image quality adjusts automatically based on network conditions, delivering the best possible quality up to the specified [!DNL max-quality] value.
* If neither is specified, the system applies dynamic optimization with a default `max-quality` of `85`.

#### Quality parameter{#quality-parameter}

The quality parameter prioritizes image quality over loading speed. It fixes the output image quality to the requested value (between 1 and 100) and ignores network conditions. Learn more about the [quality parameter](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=quality&t=request).

#### Max-quality parameter{#max-quality-parameter}

Max-quality balances image quality and load time based on the client's network speed. It prioritizes faster load times by lowering image quality on slower networks, while still delivering the highest possible quality (1–100) for the given network conditions. Learn more about the [max-quality parameter](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=quality&t=request).
