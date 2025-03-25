---
title: Embed the Dynamic Media Video or Image viewer on a web page
description: Learn how to embed Dynamic Media video or image assets on a web page.
contentOwner: Rick Brough
feature: Asset Management
role: User
exl-id: 76335781-e39f-4aae-967f-5af8634d8f61
---
# Embed the Dynamic Media Video, Image viewer, or Dimensional viewer on a web page {#embedding-the-video-or-image-viewer-on-a-web-page}

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

Use the **[!UICONTROL Embed Code]** feature when you want to play the video or view an asset embedded on a web page. You copy the embed code to the clipboard so you can paste it in your web pages. Editing of the code is not permitted in the **[!UICONTROL Embed Code]** dialog box.

You embed URLs only if you are _not_ using Adobe Experience Manager as your WCM. If you are using Experience Manager as your WCM, [you add the assets directly on your page](adding-dynamic-media-assets-to-pages.md).

See [Link URLs to your Web Application](linking-urls-to-yourwebapplication.md).

See [Deliver Optimized Images for a Responsive Site](responsive-site.md).

>[!NOTE]
>
>The embed code is not available to copy until you have published the selected asset. In addition, you must also publish the viewer preset or image preset.
>
>See [Publish Assets](publishing-dynamicmedia-assets.md).
>
>See [Publish Viewer Presets](managing-viewer-presets.md#publishing-viewer-presets).
>
>See [Publish Image Presets](managing-image-presets.md#publishing-image-presets).

**To embed the Dynamic Media Video or Image viewer on a web page:**

1. Navigate to the *published* video or image asset whose embed code you want to copy.

   Remember that the embed code is only available to copy *after* you have first *published* the assets. In addition, the viewer preset or image preset must also be published.

   See [Publish Assets](publishing-dynamicmedia-assets.md).

   See [Publish Viewer Presets](managing-viewer-presets.md#publishing-viewer-presets).

   See [Publish Image Presets](managing-image-presets.md#publishing-image-presets).

1. In the left rail, select the drop-down list and select **[!UICONTROL Viewers]**.
1. In the left rail, select a viewer preset name. The viewer preset is applied to the asset.
1. Select **[!UICONTROL Embed]**.
1. In the **[!UICONTROL Embed Code]** dialog box, copy the entire code to the clipboard, and then select **[!UICONTROL Close]**.
1. Paste the embed code into your web pages.

## Use HTTP/2 to deliver your Dynamic Media assets {#using-http-to-deliver-your-dynamic-media-assets}

HTTP/2 is the new, updated web protocol that improves the way browsers and servers communicate. It provides faster transfer of information and reduces the amount of processing power that is needed. Delivery of Dynamic Media assets can now be over HTTP/2 which provides better response and load times.

See [HTTP2 Delivery of Content](http2faq.md) for complete details on getting started using HTTP/2 with your Dynamic Media account.
