---
title: Deliver Dynamic Media Assets
description: Learn how to deliver Dynamic Media assets.
feature: Asset Management
role: User
exl-id: 4557b561-b3c4-4d6f-8044-2069bda41613
---
# Deliver Dynamic Media Assets{#delivering-dynamic-media-assets}

How you can deliver your Dynamic Media assets - both video and images - depends on how your website is implemented.

With Dynamic Media, you have several options:

* If your website is hosted on Adobe Experience Manager, then you want to add the Dynamic Media assets directly to your page.
* If your website is not on Experience Manager, then you have the choice of either:

  * Embedding your video or image on your website.
  * Link URLs to your web application. Use linking when you want to deliver a video player as a pop-up or modal window.
  * If your site is responsive, you can [deliver optimized images](/help/assets/dynamic-media/responsive-site.md).

>[!NOTE]
>
>Smart imaging works with your existing image presets. It uses intelligence at the last millisecond of delivery to further reduce image file size based on browser or network connection speed. See [Smart Imaging](/help/assets/dynamic-media/imaging-faq.md) for more information.

For more information, see the following topics:

* [Add Dynamic Media Assets to Web Pages](/help/assets/dynamic-media/adding-dynamic-media-assets-to-pages.md)
* [Embed the Video or Image Viewer on a Web Page](/help/assets/dynamic-media/embed-code.md)
* [Activate hotlink protection in Dynamic Media](/help/assets/dynamic-media/hotlink-protection.md)
* [Link URLs to your Web Application](/help/assets/dynamic-media/linking-urls-to-yourwebapplication.md)
* [Deliver Optimized Images for a Responsive Site](/help/assets/dynamic-media/responsive-site.md)
* [HTTP2 Delivery of Content](/help/assets/dynamic-media/http2faq.md)
* [Invalidate the CDN cache by way of Dynamic Media](/help/assets/dynamic-media/invalidate-cdn-cache-dynamic-media.md)
* [Invalidate the CDN cache by way of Dynamic Media Classic](/help/assets/dynamic-media/invalidate-cdn-cache-dm-classic.md)
* [Use Rulesets to Transform URLs](/help/assets/dynamic-media/using-rulesets-to-transform-urls.md)

## HTTP/2 delivery of Dynamic Media assets {#http-delivery-of-dynamic-media-assets}

Experience Manager now supports the delivery of all Dynamic Media content (images and video) over HTTP/2. That is, a published URL or embed code for the image or video is available to be integrated with any application that accepts a hosted asset. That published asset is then delivered by way of HTTP/2 protocol. This method of delivery improves the way browsers and servers communicate, allowing for better response and load times of all your Dynamic Media assets.

To learn more, see [HTTP/2 Delivery of Content Frequently Asked Questions](/help/assets/dynamic-media/http2faq.md).
