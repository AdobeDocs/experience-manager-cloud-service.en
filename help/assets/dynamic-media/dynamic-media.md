---
title: Work with Dynamic Media
description: Learn about what Dynamic Media is and you can use Dynamic Media to deliver assets for consumption on web, mobile, and social sites.
contentOwner: Rick Brough
feature: Dynamic Media,Asset Management
role: Admin,User
exl-id: 3ec3cb85-88ce-4277-a45c-30e52c75ed42
---
# Work with Dynamic Media {#working-with-dynamic-media}

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

[Dynamic Media](https://business.adobe.com/products/experience-manager/assets/dynamic-media.html) helps deliver rich visual merchandising and marketing assets on demand, automatically scaled for consumption on web, mobile, and social sites. Using a set of primary source assets, Dynamic Media generates and delivers multiple variations of rich content in real time through its global, scalable, performance-optimized network.

Dynamic Media serves interactive viewing experiences, including zoom, 360° spin, and video. Dynamic Media uniquely incorporates the workflows of the Adobe Experience Manager digital asset management (Assets) solution to simplify and streamline the digital campaign management process.

<!-- >[!NOTE]
>
>A Community article is available on [Working with Adobe Experience Manager and Dynamic Media](https://helpx.adobe.com/experience-manager/using/aem_dynamic_media.html). -->

## What is Dynamic Media?

Dynamic Media in Adobe Experience Manager (AEM) as a Cloud Service is a powerful solution designed to help you manage, deliver, and optimize rich media assets like images and videos across digital platforms. It transforms static media into dynamic, engaging experiences by allowing real-time modifications, such as resizing, cropping, and adjusting quality based on the user's device or screen size. With Dynamic Media, your assets automatically adapt to provide the best visual experience, whether users are on a desktop, mobile, or tablet.

A major benefit of Dynamic Media is its ability to streamline media management. You don't need to create multiple versions of images or videos—Dynamic Media handles it all by delivering the most appropriate format for each situation. For instance, e-commerce businesses can take advantage of 360-degree product views or zoomable images to create interactive experiences, while content-heavy websites can ensure fast, high-quality video streaming. This results in faster load times and more engaging user experiences, which ultimately leads to higher customer satisfaction and better conversion rates.

Dynamic Media integrates seamlessly with your digital asset management (DAM) system in AEM, giving you a single platform to store, organize, and deploy your media. This centralized approach simplifies collaboration across teams and provides real-time insights into asset performance. Whether you are focused on delivering captivating visuals or enhancing media-driven user interactions, Dynamic Media helps optimize your content for any channel, making it an essential tool for businesses aiming to elevate their digital presence.

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
* [Using Quick views to create custom pop-up Windows&reg;](custom-pop-ups.md)

See also [Set up Dynamic Media](administering-dynamic-media.md).

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

### Dynamic Media image sets, spins sets, mixed media sets {#image-sets-spins-sets-mixed-media-sets}

Image sets, spin sets, and mixed media sets are available if Dynamic Media is enabled.

![chlimage_1-359](assets/chlimage_1-359.png)

### Dynamic Media-enabled PTIFF renditions {#ptiff-renditions}

Dynamic Media-enabled assets include `pyramid.tiffs`.

![chlimage_1-360](assets/chlimage_1-360.png)

### Dynamic Media asset views change {#asset-views-change}

With Dynamic Media enabled, you can zoom in and out by clicking the `+` and `-` buttons. You can also select to zoom into certain area. Revert brings you to the original version and you can make the image full screen by clicking the diagonal arrows. Dynamic Media enabled appears like the following:

![chlimage_1-361](assets/chlimage_1-361.png)

With Dynamic Media disabled you can zoom in and out and revert to the original size:

![chlimage_1-362](assets/chlimage_1-362.png)
