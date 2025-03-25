---
title: Publish Dynamic Media assets
description: Learn how to publish Dynamic Media video and image assets so you can include them in a web page by way of a URL or embedding code on a web page.
contentOwner: Rick Brough
feature: Asset Management
role: User
exl-id: 8ee759dc-cb8f-4e80-8175-2c3ba06da862
---
# Publish Dynamic Media assets {#publishing-dynamic-media-assets}

You publish your Dynamic Media assets by selecting the assets you have already uploaded and selecting **[!UICONTROL Publish]** or **[!UICONTROL Quick Publish]**. After your Dynamic Media assets are published, they are available to you for including in a web page by way of a URL or by way of embedding code on the page.

You can also instantly publish assets that you upload &ndash; without any user intervention. Or, you can selectively publish those assets. See [Configure Dynamic Media](config-dm.md). Or, you can selectively publish assets to either Dynamic Media or Adobe Experience Manager, mutually exclusive of each other, using **[!UICONTROL Selective Publish]** at the folder level. See [Work with Selective Publish in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md).

In the **[!UICONTROL Card View]**, a small globe icon appears directly below an asset's name and to the left of the date and time to indicate that it is published. In the **[!UICONTROL List View]**, a **[!UICONTROL Published]** column indicates which assets are published or which are not.

>[!NOTE]
>
>If an asset is already published, then you move the asset to another folder, and republish from its new location, the original published asset location is still available, along with the newly republished asset. The original published asset, however, is "lost" to Experience Manager and cannot be unpublished. Therefore, as a best practice, unpublish assets first before you move them to a different folder.

If you intend to publish video assets immediately after encoding them, make sure that encoding is done. When videos are being encoded, the system lets you know that a video processing workflow is in progress. When video encoding is done, you can preview the video renditions. At that point, it is safe for you to publish the videos without incurring any publishing errors.

See also [Link URLs to your web application](linking-urls-to-yourwebapplication.md).

See also [Embed the Dynamic Media Video viewer or Image viewer on a web page](embed-code.md).

>[!NOTE]
>
>* Assets must be published to use the URL. If the assets are not published, copying, and pasting the URL into a web browser does not work.
>* Image presets and viewer presets must be activated and published for live delivery.
>

For detailed information on publishing a set or asset, see [Publishing Assets](/help/assets/manage-digital-assets.md).

## HTTP/2 delivery of Dynamic Media assets {#http-delivery-of-dynamic-media-assets}

Experience Manager now supports the delivery of all Dynamic Media content (images and video) over HTTP/2. That is, a published URL or embed code for the image or video is available to be integrated with any application that accepts a hosted asset. That published asset is then delivered by way of HTTP/2 protocol. This method of delivery improves the way browsers and servers communicate, allowing for better response and load times of all your Dynamic Media assets.

See [HTTP/2 delivery of content frequently asked questions](/help/assets/dynamic-media/http2faq.md).

<!--this md file used to reside under sites-administering-->
