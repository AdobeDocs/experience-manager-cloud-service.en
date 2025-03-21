---
title: Apply Dynamic Media Image Presets
description: Learn how to apply image presets in Dynamic Media.
contentOwner: Rick Brough
feature: Image Presets,Viewers,Renditions
role: User
exl-id: ad21b52e-594f-4421-9b5a-2382d032ec5a
---
# Apply Dynamic Media Image Presets {#applying-image-presets}

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

Image Presets enable assets to dynamically deliver images at different sizes, in different formats, or with other image properties there are generated dynamically. You can choose a preset when you export to reformat images to specifications that your administrator has outlined.

In addition, you can choose an image preset that is responsive (designated by the **[!UICONTROL RESS]** button after you select it).

[Administrators can create and configure image presets](managing-image-presets.md).

>[!NOTE]
>
>Smart imaging works with your existing image presets. It uses intelligence at the last millisecond of delivery to further reduce image file size based on browser or network connection speed. See [Smart Imaging](imaging-faq.md) for more information.

You can apply an image preset to an image anytime you preview it.

**To apply Dynamic Media Image Presets:**

1. Open the asset and in the left rail, select the drop-down list, then select **[!UICONTROL Renditions]**.

   >[!NOTE]
   >
   >* Static renditions appear in the top half ofthepane. Dynamic renditions appear in the lower half. With dynamic renditions only, you can use the URL to display the image. The **[!UICONTROL URL]** button only appears if you select a dynamic rendition. The **[!UICONTROL RESS]** button only appears if you select a responsive image preset.
   >
   >* The system shows numerous renditions when you select **[!UICONTROL Renditions]** in an asset's Detail view. You can increase the number of presets seen. See [Increasing the number of image presets that display](managing-image-presets.md#increasing-or-decreasing-the-number-of-image-presets-that-display).

   ![chlimage_1-208](assets/chlimage_1-208.png)

1. Do any of the following:

    * To preview the image preset, select a dynamic rendition.
    * To display the pop-up window, select **[!UICONTROL URL]**, **[!UICONTROL Embed]**, or **[!UICONTROL RESS]**.

   >[!NOTE]
   >
   >If the asset *and* the image preset are not yet published, the **[!UICONTROL URL]** button (or URL and RESS buttons, if applicable) is not available.
   >
   >Note also that image presets are automatically published on a Dynamic Media S7 server.
