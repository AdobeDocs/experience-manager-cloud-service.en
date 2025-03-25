---
title: Manage Image Presets
description: Learn about Image Presets and how to create, modify, and manage them.
contentOwner: Rick Brough
feature: Image Presets,Viewers,Renditions
role: User
exl-id: a53f40ab-0e27-45f8-9142-781c077a04cc
---
# Manage Image Presets{#managing-image-presets}

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

Image Presets enable Adobe Experience Manager Assets to deliver images dynamically at different sizes, in different formats, or with other image properties that are generated dynamically. Each Image Preset represents a predefined collection of sizing and formatting commands for displaying images. When you create an Image Preset, you choose a size for image delivery. You also choose formatting commands so that the appearance of the image is optimized when the image is delivered for viewing.

Administrators can create presets for exporting assets. Users can choose a preset when they export images, which also reformat images to the specifications that the administrator specifies.

You can also create Image Presets that are responsive. If you apply a responsive Image Preset to your assets, they change depending on the device or screen size they are viewed on. You can configure Image Presets to use CMYK in the color space in addition to RGB or Gray.

This section describes how to create, modify, and generally manage Image Presets. You can apply an Image Preset to an image anytime you preview it. See [Apply Image Presets](/help/assets/dynamic-media/image-presets.md).

>[!NOTE]
>
>Smart imaging works with your existing Image Presets and uses intelligence at the last millisecond of delivery to reduce image file size further based on browser or network connection speed. See [Smart Imaging](/help/assets/dynamic-media/imaging-faq.md) for more information.

## Learn about Image Presets {#understanding-image-presets}

Like a macro, an Image Preset is a predefined collection of sizing and formatting commands saved under a name. To understand how Image Presets work, suppose that your website requires each product image to appear in different sizes, different formats, and compression rates for desktop and mobile delivery.

You could create two Image Presets: 500 x 500 pixels for desktop and 150 x 150 pixels for mobile. You create two Image Presets, one called `Enlarge` to display images at 500x500 pixels and one called `Thumbnail` to display images at 150 x 150 pixels. To deliver images at the `Enlarge` and `Thumbnail` size, Experience Manager finds the definition of the `Enlarge Image Preset` and `Thumbnail Image Preset`. Then Experience Manager dynamically generates an image at the size and formatting specifications of each Image Preset.

Images that are reduced in size when they are delivered dynamically can lose sharpness and detail. For this reason, each Image Preset contains formatting controls for optimizing an image when it is delivered at a particular size. These controls make sure that your images are sharp and clear when they are delivered to your web site or application.

Administrators can create Image Presets. To create an Image Preset, you can start from scratch or you can start from an existing one and save it under a new name.

## Manage Image Presets {#managing-image-presets-1}

You manage your Image Presets in Experience Manager by selecting the Experience Manager logo to access the global navigation console and then selecting the Tools icon and navigating to **[!UICONTROL Assets]** > **[!UICONTROL Image Presets]**.

![6_5_tools-assets-imagepresets](assets/6_5_tools-assets-imagepresets.png)

>[!NOTE]
>
>Any Image Presets that you create are also available as dynamic renditions when you preview or deliver assets.
>
>You do *not* need to publish Image Presets as Image Presets are automatically published.
>
>See [Publish Image Presets](#publishing-image-presets).

>[!NOTE] 
>
>The system shows various renditions when you select **[!UICONTROL Renditions]** in an asset's Detail View. You can increase or decrease the number of Image Presets that display. See [Increase the number of image presets that are displayed](#increasing-or-decreasing-the-number-of-image-presets-that-display).

### Adobe Illustrator (AI), PostScript&reg; (EPS), and PDF file formats {#adobe-illustrator-ai-postscript-eps-and-pdf-file-formats}

If you intend to support the ingestion of AI, EPS, and PDF files so that you can generate dynamic renditions of these file formats, review the following information before you create Image Presets.

Adobe Illustrator's file format is a variant of PDF. The main differences, in the context of Experience Manager Assets, are the following:

* Adobe Illustrator documents consist of a single page with multiple layers. Each layer is extracted as a PNG subasset under the main Illustrator asset.
* PDF documents consist of one or more pages. Each page is extracted as a single page PDF subasset under the main multi-page PDF document.

The `Create Sub Asset process` component creates the subassets within the overall `DAM Update Asset` workflow. To see this process component within the workflow, navigate to **[!UICONTROL Tools]** > **[!UICONTROL Workflow]** > **[!UICONTROL Models]** > **[!UICONTROL DAM Update Asset]** > **[!UICONTROL Edit]**.

<!-- See also [Viewing pages of a multi-page file](/help/assets/manage-linked-subassets.md#view-pages-of-a-multi-page-file). -->

You can view the subassets or the pages when you open the asset, select the Content menu, and select **[!UICONTROL Subassets]** or **[!UICONTROL Pages]**. The subassets are real assets. The `Create Sub Asset` workflow component extracts the PDF pages. They are then stored as `page1.pdf`, `page2.pdf`, and so on, below the main asset. After they are stored, the `DAM Update Asset` workflow processes them.

To use Dynamic Media to preview and generate dynamic renditions for AI, EPS or PDF files, the following processing steps are required:

1. In the `DAM Update Asset` workflow, the `Rasterize PDF/AI Image Preview Rendition` process component rasterizes the first page of the original asset &ndash; using the configured resolution &ndash; into a `cqdam.preview.png` rendition.

1. The `Dynamic Media Process Image Assets` process component within the workflow optimizes the `cqdam.preview.png` rendition into a PTIFF.

>[!NOTE]
>
>In the DAM Update Asset workflow, the **[!UICONTROL EPS thumbnails]** step generates thumbnails for EPS files.

#### PDF/AI/EPS asset metadata properties {#pdf-ai-eps-asset-metadata-properties}

| **Metadata property** |**Description** |
|---|---|
| `dam:Physicalwidthininches` |Document width in inches. |
| `dam:Physicalheightininches` |Document height in inches. |

You access `Rasterize PDF/AI Image Preview Rendition` process component options by way of the `DAM Update Asset` workflow.

Select Adobe Experience Manager in the upper left, the click **[!UICONTROL Tools]** > **[!UICONTROL Workflow]** > **[!UICONTROL Models]**. On the Workflow Models page, select **[!UICONTROL DAM Update Asset]**, then on the toolbar select **[!UICONTROL Edit]**. On the DAM Update Asset workflow page, double-select the `Rasterize PDF/AI Image Preview Rendition` process component to open its Step Properties dialog box.

#### Rasterize PDF/AI Image Preview Rendition options {#rasterize-pdf-ai-image-preview-rendition-options}

![Arguments to rasterize PDF or AI workflow](assets/rasterize_pdf_ai_image_preview.png)

Arguments to rasterize PDF or AI workflow

|Process Argument | Default setting | Description |
|---|---|---|
| Mime Types | application/pdf<br>application/postscript<br>application/illustrator| List of document mime-types that are considered to be PDF or Illustrator documents. |
| Max Width | 2048 | Maximum width of the generated preview rendition, in pixels.|
| Max Height | 2048| Maximum height of the generated preview rendition, in pixels. |
| Resolution | 72 | Resolution to rasterize the first page, in ppi (pixels per inch). |

Using the default process arguments, the first page of a PDF/AI document is rasterized at 72 ppi and the generated preview image is sized at 2048 x 2048 pixels. For a typical deployment, you can increase the resolution to a minimum of 150 ppi or more. For example, a US letter size document at 300 ppi requires a maximum width and height of 2550 x 3300 pixels, respectively.

Max Width and Max Height limit the resolution at which to rasterize. For example, if the maximums are unchanged, and Resolution is set to 300 ppi, a US Letter document is rasterized at 186 ppi. That is, the document is 1581 x 2046 pixels.

The `Rasterize PDF/AI Image Preview Rendition` process component has a maximum defined to ensure that it does not create overly large images in memory. Such large images can overflow the memory provided to the JVM (Java&trade; Virtual Machine). Care must be taken to provide the JVM with enough memory to manage the configured number of parallel workflows, with each having the potential to create an image at the maximum configured size.

### InDesign (INDD) file format {#indesign-indd-file-format}

If you intend to support the ingestion of INDD files so that you can generate dynamic rendition of this file format, review the following information before you create Image Presets.

For InDesign files, sub assets are extracted only if the Adobe InDesign Server is integrated with Experience Manager. Referenced assets are linked based on their metadata. InDesign Server is not required for linking. However, the referenced assets must be present within Experience Manager before the InDesign files are processed for the links to be created between the InDesign files and the referenced assets.

<!-- See [Integrate Experience Manager Assets with InDesign Server](/help/assets/indesign.md). -->

The Media Extraction process component in the `DAM Update Asset` workflow runs several pre-configured Extend Scripts to process InDesign files.

![The ExtendScript paths in the arguments of Media Extraction process](/help/assets/dynamic-media/assets/6_5_mediaextractionprocess.png)

The ExtendScript paths in the arguments of the Media Extraction process component in the DAM Update Asset workflow.

The following scripts are used by Dynamic Media integration:


|ExtendScript name | Default | Description |
|---|---|---|
| ThumbnailExport.jsx | Yes  | Generates a 300 PPI `thumbnail.jpg` rendition that is optimized and turned into a PTIFF rendition by `Dynamic Media Process Image Assets` process component.  |
| JPEGPagesExport.jsx | Yes | Generates a 300 PPI JPEG subasset for each page. The JPEG subasset is a real asset stored under the InDesign asset. The `DAM Update Asset` workflow optimizes and converts it into a PTIFF. |
| PDFPagesExport.jsx | No | Generates a PDF subasset for each page. The PDF subasset gets processed as described earlier. Because the PDF contains a single page only, no subassets are generated. |

### Configure the image thumbnail size {#configuring-image-thumbnail-size}

You can configure the size of thumbnails by configuring those settings in the **[!UICONTROL DAM Update Asset]** workflow. There are two steps in the workflow where you can configure the thumbnail size of image assets. One (**[!UICONTROL Dynamic Media Process Image Assets]**) is used for dynamic image assets. The other (**[!UICONTROL Process Thumbnails]**) is used for static thumbnail generation or when all other processes fail to generate thumbnails. Regardless, *both* must have the same settings.

The **[!UICONTROL Dynamic Media Process Image Assets]** step uses the image server to generate thumbnails, independently of the configuration applied to the **[!UICONTROL Process Thumbnails]** step. Generating thumbnails through the **[!UICONTROL Process Thumbnails]** step is the slowest and most memory intensive way to create thumbnails.

Thumbnail sizing is defined in the following format: **[!UICONTROL width:height:center]**, for example, `80:80:false`. The width and height determine the size in pixels of the thumbnail. The center value is either false or true. If set to true, it indicates that the thumbnail image has exactly the size given in the configuration. If the resized image is smaller, it is centered within the thumbnail.

>[!NOTE]
>
>* Thumbnail sizes for EPS files are configured in the **[!UICONTROL EPS thumbnails]** step, in the **[!UICONTROL Arguments]** tab under Thumbnails.
>
>* Thumbnail sizes for videos are configured in the **[!UICONTROL FFmpeg thumbnails]** step, in the **[!UICONTROL Process]** tab under **[!UICONTROL Arguments]**.
>

**To configure the image thumbnail size:**

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Workflow]** > **[!UICONTROL Models]** > **[!UICONTROL DAM Update Asset]** > **[!UICONTROL Edit]**.
1. Select the **[!UICONTROL Dynamic Media Process Image Assets]** step and select the **[!UICONTROL Thumbnails]** tab. Change the thumbnail size, as needed, then select **[!UICONTROL OK]**.

   ![6_5_dynamicmediaprocessimageassets-thumbnailstab](assets/6_5_dynamicmediaprocessimageassets-thumbnailstab.png)

1. Select the **[!UICONTROL Process Thumbnails]** step, then select the **[!UICONTROL Thumbnails]** tab. Change the thumbnail size, as needed, then select **[!UICONTROL OK]**.

   >[!NOTE]
   >
   >The values in the thumbnails argument in the **[!UICONTROL Process Thumbnails]** step must match the thumbnails argument in the **[!UICONTROL Dynamic Media Process Image Assets]** step.

1. Select **[!UICONTROL Save]** to save the changes to the workflow.

### Increase or decrease the number of image presets that are displayed {#increasing-or-decreasing-the-number-of-image-presets-that-display}

Image presets you create are available as dynamic renditions when you preview assets. Experience Manager shows various dynamic renditions when viewing an asset from **[!UICONTROL Detail View > Renditions]**. You can increase or decrease the limit of renditions that are displayed.

**To increase or decrease the number of image presets that are displayed:**

1. Navigate to CRXDE Lite ([https://localhost:4502/crx/de](https://localhost:4502/crx/de)).
1. Navigate to the image preset listing node at `/libs/dam/gui/coral/content/commons/sidepanels/imagepresetsdetail/imgagepresetslist`

   ![increase_decreasethenumberofimagepresetsthatdisplay](assets/increase_decreasethenumberofimagepresetsthatdisplay.png)

1. In the **[!UICONTROL limit]** property, change the **[!UICONTROL Value]**, which is set to 15 by default, to the desired number.
1. Navigate to the image preset datasource at `/libs/dam/gui/coral/content/commons/sidepanels/imagepresetsdetail/imgagepresetslist/datasource`

   ![chlimage_1-495](assets/chlimage_1-495.png)

1. In the limit property, change the number to the desired number, for example, `{empty requestPathInfo.selectors[1] ? "20" : requestPathInfo.selectors[1]}`
1. Select **[!UICONTROL Save All]**.

### Create Image Presets {#creating-image-presets}

Create Image Presets so you can apply settings consistently across images when you preview or publish.

>[!NOTE]
>
>If using Internet Explorer 9, creating a preset does not appear in the preset list immediately after saving. To work around this issue, disable the cache for IE9.

If you intend to support the ingestion of AI, PDF, and EPS files so that you can generate dynamic rendition of these file formats, review the following information before you create Image Presets.

See [Adobe Illustrator (AI), PostScript&reg; (EPS), and PDF file formats](#adobe-illustrator-ai-postscript-eps-and-pdf-file-formats).

If you intend to support the ingestion of INDD files so that you can generate dynamic rendition of this file format, review the following information before you create Image Presets.

See [InDesign (INDD) file format](#indesign-indd-file-format).

**To create image presets:**

1. In Experience Manager, select the Experience Manager logo to access the global navigation console, then go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Image Presets]**.
1. Select **[!UICONTROL Create]**.

   ![chlimage_1-496](assets/chlimage_1-496.png)

   >[!NOTE]
   >
   >To make this Image Preset responsive, erase the values in the **[!UICONTROL width]** and **[!UICONTROL height]** fields and leave them blank.

1. In the **[!UICONTROL Edit Image Preset]** window, enter values into the **[!UICONTROL Basic]** and **[!UICONTROL Advanced]** tabs as appropriate, including a name. The options are outlined in [Image Preset Options](#image-preset-options). Presets appear in the left pane and can be used on-the-fly with other assets.

   ![6_5_imagepreset-edit](assets/6_5_imagepreset-edit.png)

1. Select **[!UICONTROL Save]**.

### Creating a responsive Image Preset {#creating-a-responsive-image-preset}

To create a responsive Image Preset, perform the steps in [Create image presets](#creating-image-presets). When entering the height and width in the **[!UICONTROL Edit Image Preset]** window, erase the values and leave them blank.

Leaving them blank tells Experience Manager that this Image Preset is responsive. You can adjust the other values as appropriate.

>[!NOTE]
>
>To see the **[!UICONTROL URL]** and **[!UICONTROL RESS]** buttons when applying an Image Preset to an asset, the asset must be published.
>
>![chlimage_1-79](assets/chlimage_1-498.png)
>
>Image presets and image assets are automatically published.

### Image Preset options {#image-preset-options}

When you create or edit Image Presets, you have the options described in this section. In addition, Adobe recommends these "best practice" option choices to start:

* **[!UICONTROL Format]** (**[!UICONTROL Basic]** tab) - Select **[!UICONTROL JPEG]** or another format that meets your requirements. All web browsers support the JPEG image format; it offers a good balance between small files sizes and image quality. However, JPEG format images use a lossy compression scheme that can introduce unwanted image artifacts if the compression setting is too low. For that reason, Adobe recommends setting the compression quality to 75. This setting offers a good balance between image quality and small file size.

* **[!UICONTROL Enable Simple Sharpening]** - Do not select **[!UICONTROL Enable Simple Sharpening]** (this sharpening filter offers less control than Unsharp Masking settings).

* **[!UICONTROL Sharpening: Resampling Mode]** - Select **[!UICONTROL Sharp2]**.

#### Basic tab options {#basic-tab-options}

| Field | Description |
| --- | --- |
| **Name** | Enter a descriptive name without any blank spaces. To help users identify this Image Preset, include the image-size specification in the name. |
| **Width and Height** | Enter in pixels the size at which the image is delivered. Width and height must be larger than 0 pixels. If either value is 0, then no preset is created. If both values are blank, a responsive Image Preset is created. |
| **Format** | Choose a format from the menu.<br>Choosing **JPEG** offers the following other options:<br>&bull; **Quality** - The JPEG quality scale is 1-100. The scale is visible when you drag the slider.<br>&bull; **Enable JPG Chrominance Downsampling** - Because the eye is less sensitive to high-frequency color information than high-frequency luminance, JPEG images divide image information into luminance and color components. When a JPEG image is compressed, the luminance component is left at full resolution, while the color components are downsampled by averaging together groups of pixels. Downsampling reduces the data volume to half or one-third with minimal impact on perceived quality. Downsampling is not applicable to grayscale images. This technique reduces the amount of compression useful for images with high contrast (for example, images with overlaid text).<br><br>Choosing **GIF** or **GIF with alpha** provides these additional **GIF Color Quantization** options:<br>&bull; **Type** - Select **Adaptive** (default), **Web**, or **Macintosh**. If you select **GIF with Alpha**, the Macintosh option is not available.<br>&bull; **Dither** - Select **Diffuse** or **Off**.<br>&bull; **Number of Colors** - Enter a number 2 - 256.<br>&bull; **Color List** - Enter a comma-separated list. For example, for white, gray, and black, enter `000000,888888,ffffff`.<br><br>Choosing **PDF**, **TIFF**, or **TIFF with alpha** provides this additional option:<br>&bull; **Compression** - Select a compression algorithm. Algorithm options for PDF are **None**, **Zip**, and **Jpeg**; for TIFF they are **None**, **LZW**, **Jpeg**, and **Zip**; and for TIFF with Alpha are **None**, **LZW**, and **Zip**.<br><br>Choosing **PNG**, **PNG with Alpha**, or **EPS** provides no additional options. |
| **Sharpening** | Select **Enable Simple Sharpening** to apply a basic sharpening filter to the image after all scaling takes place. Sharpening can help compensate for blurriness that can result when you display an image at a different size. |

#### Advanced tab options {#advanced-tab-options}

<table>
 <tbody>
  <tr>
   <td><strong>Field</strong></td>
   <td><strong>Description</strong></td>
  </tr>
  <tr>
   <td><strong>Color Space</strong></td>
   <td>Select <strong>RGB, CMYK,</strong> or <strong>Grayscale</strong> for the color space.</td>
  </tr>
  <tr>
   <td><strong>Color Profile</strong></td>
   <td>Select the output color space profile that you want the asset converted to if it is different from the working profile.</td>
  </tr>
  <tr>
   <td><strong>Render Intent</strong></td>
   <td>You can override the default rendering intent. Rendering intents determine what happens to colors that cannot be reproduced in the target color profile (out of gamut). The Render Intent is ignored if it is not compatible with the ICC profile.
    <ul>
     <li>Select <strong>Perceptual</strong> to compress the total gamut from one color space into another color space when one or more colors in the original image is out of the gamut of the destination color space.</li>
     <li>Select <strong>Relative Colorimetric</strong> when a color in the current color space is out of gamut in the target color space. And you want to map it to the closest target color gamut without altering other colors. </li>
     <li>Select <strong>Saturation</strong> if you want to reproduce the original image color saturation when converting into the target color space. </li>
     <li>Select <strong>Absolute Colorimetric</strong> to match colors exactly with no adjustment for white point or black point that would alter the image's brightness.</li>
    </ul> </td>
  </tr>
  <tr>
   <td><strong>Blackpoint Compensation</strong></td>
   <td>Select this option if the output profile supports this feature. Blackpoint compensation is ignored if it is not compatible with the specified ICC profile.</td>
  </tr>
  <tr>
   <td><strong>Dithering</strong></td>
   <td>Select this option to avoid or reduce possible color banding artifacts. </td>
  </tr>
  <tr>
   <td><strong>Sharpening Type</strong></td>
   <td><p>Select <strong>None</strong>, <strong>Sharpen</strong>, or <strong>Unsharp Mask</strong>. </p>
    <ul>
     <li>Select <strong>None</strong> if you want to disable sharpening.</li>
     <li>Select <strong>Sharpen </strong>to apply a basic sharpening filter to the image after all scaling takes place. Sharpening can help compensate for blurriness that can result when you display an image at a different size. </li>
     <li>Select<strong> Unsharp Mask</strong> if you want to fine-tune a sharpening filter effect on the final downsampled image. You can control the intensity of the effect, radius of the effect (measured in pixels) and a threshold of contrast that is ignored. This effect uses the same options as Photoshop's "Unsharp Mask" filter.</li>
    </ul> <p>In <strong>Unsharp Mask</strong>, you have the following options:</p>
    <ul>
     <li><strong>Amount</strong> - Controls the amount of contrast applied to edge pixels. The default real number value is 1.0. For high-resolution images, you can increase it to as high as 5.0. Think of Amount as a measure of filter intensity.</li>
     <li><strong>Radius</strong> - Determines the number of pixels surrounding the edge pixels that affect the sharpening. For high-resolution images, enter a real number from 1 through 2. A low value sharpens only the edge pixels; a high value sharpens a wider band of pixels. The correct value depends on the size of the image.</li>
     <li><strong>Threshold</strong> - Determines the range of contrast to ignore when the Unsharp Mask filter is applied. In other words, this option defines how much sharpened pixels must differ from the surrounding area to be considered edge pixels and sharpened. To avoid introducing noise, experiment with integer values from 2 through 20. </li>
     <li><strong>Apply to</strong> - Determines whether the unsharpening applies to each color or brightness.</li>
    </ul>
    <div>
      Sharpening is described in
     <a href="https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-image-sharpening-feature-video-use#dynamic-media">Using Image Sharpening with Experience Manager Dynamic Media</a> video, in <a href="https://experienceleague.adobe.com/en/docs/dynamic-media-classic/using/master-files/sharpening-image#master-files">Sharpening an image</a> online Help topic, and in <a href="https://experienceleague.adobe.com/docs/dynamic-media-classic/assets/s7_sharpening_images.pdf">Best practices for sharpening images in Dynamic Media Classic</a> downloadable PDF.
    </div> </td>
  </tr>
  <tr>
   <td><strong>Resampling Mode</strong></td>
   <td>Select a <strong>Resampling mode</strong> option. These options sharpen the image when it is downsampled:
    <ul>
     <li><strong>Bi-Linear</strong> - The fastest resampling method. Some aliasing artifacts are noticeable.</li>
     <li><strong>Bi-Cubic</strong> - Increases CPU usage but yields sharper images with less noticeable aliasing artifacts.</li>
     <li><strong>Sharp2</strong> - Can produce slightly sharper results than Bi-Cubic, but at an even higher CPU cost.</li>
     <li><strong>Bi-Sharp</strong> - Selects Photoshop default resampler for reducing image size, which is called <strong>bicubic sharper</strong> in Adobe Photoshop.</li>
     <li><strong>Each Color</strong> and <strong>Brightness</strong> - each method can be based on color or brightness. By default <strong>Each Color</strong> is selected.</li>
    </ul> </td>
  </tr>
  <tr>
   <td><strong>Print resolution</strong></td>
   <td>Select a resolution for printing this image; 72 pixels is the default.</td>
  </tr>
  <tr>
   <td><strong>Image Modifier</strong></td>
   <td><p>Beyond the common image settings available in the UI, Dynamic Media supports numerous advanced image modifications that you can specify in the <strong>Image Modifiers</strong> field. These parameters are defined in the <a href="https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/syntax-and-features/image-serving-http/c-command-overview">Image Server Protocol command reference</a>.</p> <p>Important: The following functionality listed in the API is not supported:</p>
    <ul>
     <li>Basic templating and text rendering commands: <code>text= textAngle= textAttr= textFlowPath= textFlowXPath= textPath=</code> and <code>textPs=</code></li>
     <li>Localization commands: <code>locale=</code> and <code>req=xlate</code></li>
     <li><code>req=set</code> is not available for general usage.</li>
     <li><code>req=mbrset</code></li>
     <li><code>req=saveToFile</code></li>
     <li><code>req=targets</code></li>
     <li><code>template=</code></li>
     <li>Non-core Dynamic Media services: SVG, Image Rendering, and Web-to-Print</li>
    </ul> </td>
  </tr>
 </tbody>
</table>

### Define Image Preset options with image modifiers {#defining-image-preset-options-with-image-modifiers}

In addition to the options available in the Basic and Advanced tabs, you can define image modifiers to give you more options when defining Image Presets. Image Rendering relies on the Dynamic Media Image Rendering API and is defined in detail in the [HTTP Protocol Reference](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-rendering-api/http-protocol-reference/c-ir-introduction#image-rendering-api).

The following are some basic examples of what you can do with image modifiers.

>[!NOTE]
>
>Some image modifiers [cannot be used in Experience Manager](#advanced-tab-options).

* [op_invert](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/r-op-invert) - Inverts each color component for a negative image effect.

  ```xml {.line-numbers}
  &op_invert=1
  ```

  ![6_5_imagepreset-edit-invert](assets/6_5_imagepreset-edit-invert.png)

* [op_blur](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/r-op-blur) - Applies a blur filter to the image.

  ```xml {.line-numbers}
  &op_blur=7
  ```

  ![6_5_imagepreset-edit-blur](assets/6_5_imagepreset-edit-blur.png)

* Combined commands - op_blur and op-invert

  ```xml {.line-numbers}
  &op_invert=1&op_blur=7
  ```

  ![chlimage_1-80](assets/chlimage_1-501.png)

* [op_brightness](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/r-op-brightness) - Decreases or increases the brightness.

  ```xml {.line-numbers}
  &op_brightness=58
  ```

  ![6_5_imagepreset-edit-brightness](assets/6_5_imagepreset-edit-brightness.png)

* [opac](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/r-opac) - Adjusts image opacity. Lets you decrease the foreground opacity.

  ```xml {.line-numbers}
  opac=29
  ```

  ![6_5_imagepreset-edit-opacity](assets/6_5_imagepreset-edit-opacity.png)

### Edit image presets {#modifying-image-presets}

1. In Experience Manager, select the Experience Manager logo to access the global navigation console, then go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Image Presets]**.

   ![6_5_imagepreset-editpreset](assets/6_5_imagepreset-editpreset.png)

1. Select a preset and then select **[!UICONTROL Edit]**. The **[!UICONTROL Edit Image Preset]** window opens.
1. Make changes and select **[!UICONTROL Save]** to save your changes or **[!UICONTROL Cancel]** to cancel your changes.

### Publish image presets {#publishing-image-presets}

Image presets are automatically published for you.

### Delete image presets {#deleting-image-presets}

1. In Experience Manager, select the Experience Manager logo to access the global navigation console and select the Tools icon.
1. Navigate to **[!UICONTROL Assets]** > **[!UICONTROL Image Presets]**.
1. Select a preset, and then select **[!UICONTROL Delete]**. Dynamic Media confirms that you want to delete it. Select **[!UICONTROL Delete]** to remove or select **[!UICONTROL Cancel]** to return to Image Presets.
