---
title: Publish Dynamic Media assets
description: Learn how to publish Dynamic Media video and image assets so you can include them in a web page by way of a URL or embedding code on a web page.
contentOwner: Rick Brough
feature: Asset Management
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 8ee759dc-cb8f-4e80-8175-2c3ba06da862
---
# Publish Dynamic Media assets {#publishing-dynamic-media-assets}

Publishing makes your Dynamic Media assets available for delivery on a web page through a **URL** or through **embed code**. To publish, select the assets you have already uploaded, then choose **[!UICONTROL Publish]** or **[!UICONTROL Quick Publish]**. After your Dynamic Media assets are published, those assets become available for inclusion on any web page by way of a URL or by way of embedding code on the page.

## Publishing options

You control when and where assets publish. The available options are:

* **Instant publish** – Automatically publish assets as you upload them, without any user intervention.
* **Selective publish** – Publish only the specific assets you choose. See [Configure Dynamic Media](config-dm.md).
* **Selective Publish at the folder level** – Publish assets to either Dynamic Media or Adobe Experience Manager, mutually exclusive of each other, using **[!UICONTROL Selective Publish]**. See [Work with Selective Publish in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md).

## How to identify a published asset

The publishing status of an asset is visible directly in the interface, so you can confirm delivery readiness at a glance:

* **[!UICONTROL Card View]** – A small globe icon appears directly below the asset's name and to the left of the date and time, indicating that the asset is published.
* **[!UICONTROL List View]** – A **[!UICONTROL Published]** column indicates which assets are published and which are not.

>[!NOTE]
>
>If an asset is already published, then you move the asset to another folder, and republish from its new location, the original published asset location is still available, along with the newly republished asset. The original published asset, however, is "lost" to Experience Manager and cannot be unpublished. Because the original published location cannot be reversed once the asset moves, follow this best practice: unpublish assets first before you move them to a different folder.

## Publishing video assets after encoding

If you intend to publish video assets immediately after encoding them, complete these steps in order to avoid publishing errors:

1. Confirm that encoding is done. While videos are being encoded, the system displays a notification that a video processing workflow is in progress.
2. Wait for video encoding to finish. When video encoding is done, you can preview the video renditions.
3. Publish the videos. At that point, it is safe to publish the videos without incurring any publishing errors, because the renditions required for delivery are fully generated.

See also [Link URLs to your web application](linking-urls-to-yourwebapplication.md).

See also [Embed the Dynamic Media Video viewer or Image viewer on a web page](embed-code.md).

>[!NOTE]
>
>* Assets must be published to use the URL. If the assets are not published, copying and pasting the URL into a web browser does not work.
>* Image presets and viewer presets must be activated and published for live delivery.
>

For detailed information on publishing a set or asset, see [Publishing Assets](/help/assets/manage-digital-assets.md).

## HTTP/2 delivery of Dynamic Media assets {#http-delivery-of-dynamic-media-assets}

Experience Manager delivers all **Dynamic Media** content — including **images and video** — over **HTTP/2 (Hypertext Transfer Protocol version 2)**, the modern web transport protocol. A published URL or embed code for each image or video integrates with any application that accepts a hosted asset. Experience Manager then delivers that published asset over the HTTP/2 protocol.

### How HTTP/2 delivery works

HTTP/2 improves the way browsers and servers communicate, resulting in better response and load times for all your Dynamic Media assets. As the successor to HTTP/1.1, HTTP/2 is widely adopted across modern browsers and content delivery infrastructure. It enhances communication through capabilities such as request multiplexing over a single connection and header compression, which reduce the overhead that previously slowed asset delivery. Because Dynamic Media assets — high-resolution images and video in particular — are often requested in large numbers on a single page, these efficiencies translate directly into faster, more responsive rendering for end users.

### Benefits of HTTP/2 delivery

Delivering Dynamic Media assets over HTTP/2 provides the following advantages:

- **Faster load times** for images and video across your Dynamic Media assets.
- **Improved response times** through more efficient browser-to-server communication.
- **Seamless integration**, since the published URL or embed code works with any application that accepts a hosted asset.
- **Broad compatibility**, as HTTP/2 is supported by modern browsers and delivery networks.

See [HTTP/2 delivery of content frequently asked questions](/help/assets/dynamic-media/http2faq.md).

<!--this md file used to reside under sites-administering-->
