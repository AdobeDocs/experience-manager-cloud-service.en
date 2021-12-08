---
title: Work with Dynamic Media
description: Learn how to use Dynamic Media to deliver assets for consumption on web, mobile, and social sites.
role: Admin,User
exl-id: 3ec3cb85-88ce-4277-a45c-30e52c75ed42
---
# Work with Dynamic Media {#working-with-dynamic-media}

[Dynamic Media](https://business.adobe.com/products/experience-manager/assets/dynamic-media.html) helps deliver rich visual merchandising and marketing assets on demand, automatically scaled for consumption on web, mobile, and social sites. Using a set of primary source assets, Dynamic Media generates and delivers multiple variations of rich content in real time through its global, scalable, performance-optimized network.

Dynamic Media serves interactive viewing experiences, including zoom, 360° spin, and video. Dynamic Media uniquely incorporates the workflows of the Adobe Experience Manager digital asset management (Assets) solution to simplify and streamline the digital campaign management process.

<!-- >[!NOTE]
>
>A Community article is available on [Working with Adobe Experience Manager and Dynamic Media](https://helpx.adobe.com/experience-manager/using/aem_dynamic_media.html). -->

## What you can do with Dynamic Media {#what-you-can-do-with-dynamic-media}

Dynamic Media lets you manage your assets before publishing them. How to work with assets in general is covered in detail in [Working with Digital Assets](/help/assets/manage-digital-assets.md). General topics include uploading, downloading, editing, and publishing assets; viewing and editing properties, and searching for assets.

Dynamic Media-only features include the following:

* [Carousel Banners](carousel-banners.md)
* [Image Sets](image-sets.md)
* [Interactive Images](interactive-images.md)
* [Interactive Videos](interactive-videos.md)
* [Mixed Media Sets](mixed-media-sets.md)
* [Panoramic Images](panoramic-images.md)

* [Spin Sets](spin-sets.md)
* [Video](video.md)
* [Delivering Dynamic Media Assets](delivering-dynamic-media-assets.md)
* [Managing Assets](managing-assets.md)
* [Using Quick views to create custom pop-up Windows®](custom-pop-ups.md)

See also [Setting up Dynamic Media](administering-dynamic-media.md).

<!-- 

OBSOLETE UNTIL INTEGRATING SCENE7 TOPIC GETS A MAJOR UPDATE
>[!NOTE]
>
>To understand the differences between using Dynamic Media and integrating Dynamic Media Classic with AEM, see [Dynamic Media Classic integration versus Dynamic Media](/help/sites-cloud/administering/integrating-scene7.md#aem-scene-integration-versus-dynamic-media).

-->

## Dynamic Media enabled versus Dynamic Media disabled {#dynamic-media-on-versus-dynamic-media-off}

You can tell whether Dynamic Media is enabled (turned on) by the following characteristics:

* Dynamic renditions are available when downloading or previewing assets.
* Image sets, spin sets, mixed media sets are available.
* PTIFF renditions are created.

When you click an image asset, the view of the asset is different with Dynamic Media enabled. Dynamic Media uses the on-demand HTML5 viewers.

### Dynamic renditions {#dynamic-renditions}

Dynamic renditions such as image and viewer presets (under **[!UICONTROL Dynamic]**) are available when Dynamic Media is enabled.

![chlimage_1-358](assets/chlimage_1-358.png)

### Image sets, spins sets, mixed media sets {#image-sets-spins-sets-mixed-media-sets}

Image sets, spin sets, and mixed media sets are available if Dynamic Media is enabled.

![chlimage_1-359](assets/chlimage_1-359.png)

### PTIFF renditions {#ptiff-renditions}

Dynamic Media enabled assets include `pyramid.tiffs`.

![chlimage_1-360](assets/chlimage_1-360.png)

### Asset views change {#asset-views-change}

With Dynamic Media enabled, you can zoom in and out by clicking the `+` and `-` buttons. You can also click/tap to zoom into certain area. Revert brings you to the original version and you can make the image full screen by clicking the diagonal arrows. Dynamic Media enabled appears like the following:

![chlimage_1-361](assets/chlimage_1-361.png)

With Dynamic Media disabled you can zoom in and out and revert to the original size:

![chlimage_1-362](assets/chlimage_1-362.png)
