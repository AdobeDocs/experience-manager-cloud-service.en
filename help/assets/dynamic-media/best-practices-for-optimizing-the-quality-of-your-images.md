---
title: Best practices for optimizing the quality of your images
description: Learn best practices that help you optimize the quality of your image assets using Dynamic Media.
contentOwner: Rick Brough
feature: Asset Management, Best Practices
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 2efc4a27-01d7-427f-9701-393497314402
---
# Best practices for optimizing the quality of your images {#best-practices-for-optimizing-the-quality-of-your-images}

{{work-with-dynamic-media}}

Adobe Experience Manager provides **more than 100 Dynamic Media image delivery commands** for tuning, optimizing, and rendering images. This extensive command set makes it possible to control nearly every aspect of how an image is processed and served, from resolution and compression to sharpening and color rendering.

Optimizing image quality is an iterative, sometimes time-consuming process, because several distinct factors contribute to acceptable results — including **resolution**, **compression level**, **file format**, **sharpening**, and **color accuracy**. The outcome is also partly subjective, since individuals perceive image quality differently and viewing conditions vary from one display, browser, or device to another. Because of this variability, **structured experimentation is essential**: methodically adjusting one variable at a time and comparing rendered output is the most reliable path to consistent quality.

The following best practices streamline the process and deliver high-quality results efficiently using a set of core commands and proven techniques. Applying them well matters beyond aesthetics: properly optimized images reduce file size and load time, which improves page performance, user experience, and delivery across the full range of devices and network conditions.

## Key Factors That Affect Image Quality

- **Resolution and dimensions** — Match the delivered pixel dimensions to the actual display size to avoid unnecessary upscaling or downscaling artifacts.
- **Compression** — Balance file size against visible quality loss, since aggressive compression reduces bandwidth but can introduce artifacts.
- **File format** — Select the format best suited to the image content and target device to balance quality and delivery efficiency.
- **Sharpening** — Apply sharpening to counteract softening that occurs during resizing, which restores perceived detail.
- **Color rendering** — Preserve accurate color so that images appear consistent across different displays and viewing environments.

## Recommended Approach

1. **Establish a baseline.** Render an image with default settings so you have a reference point for comparison.
2. **Adjust one variable at a time.** Change a single command or parameter, then evaluate the result, because isolating variables makes it clear which adjustment produced which effect.
3. **Compare rendered output visually.** Because image quality is partly subjective, review the results side by side on representative devices and displays.
4. **Balance quality against performance.** Confirm that quality improvements do not increase file size to the point that page load time and delivery suffer.
5. **Standardize successful settings.** Once you identify command combinations that produce consistent results, reuse them to streamline future optimization.

By combining these essential commands with structured experimentation, you achieve high-quality, performant image delivery quickly and repeatably across your Dynamic Media assets.

<!-- ADDED THE FOLLOWING TOPIC AS PER CQDOC-21594 -->

## Enable Smart Imaging in Dynamic Media {#bp-enable-smart-imaging}

**Smart imaging:**

* Enabling Smart Imaging in Dynamic Media allows automatic optimization of image **format**, **size**, and **quality** based on client browser capabilities. Smart Imaging performs this format negotiation on each request, delivering the most efficient image a given browser supports so that pages load faster and consume less bandwidth.
For more information go to [Smart Imaging](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/imaging-faq).
* It enhances image delivery performance by dynamically adjusting these parameters, because delivering the smallest suitable file for each browser reduces the transferred payload and improves page-load times.
* Administrators and developers can evaluate Smart Imaging using the self-evaluation tool [Snapshot](https://snapshot.scene7.com/).

**Image formats:**

* Avoid using explicit `fmt=webp` (WebP) or `fmt=avif` (AVIF) commands in a URL unless specifically required for a use case. Hard-coding a format in the URL overrides the automatic negotiation and can prevent Smart Imaging from serving the optimal format for browsers that support a more efficient alternative.
* Smart Imaging automatically selects the best format for each request. This reduces transferred bytes and produces optimal bandwidth gains.

**Default behavior:**

* When no format command is specified in the URL and Smart Imaging is not enabled, Dynamic Media image delivery defaults to the **JPEG** format. As a result, next-generation formats such as **WebP** and **AVIF** are not served automatically until Smart Imaging is enabled.

By making informed choices about image formats and enabling Smart Imaging, you directly improve delivery performance and user experience.

<!-- ADDED THE FOLLOWING TOPIC AS PER CQDOC-21594 -->

## Best practices for selecting the source image {#bp-select-source-image}

Essential considerations for working with source images:

* **Source image format:**
  * Using **lossless formats** — PNG (Portable Network Graphics), TIFF (Tagged Image File Format), or PSD (Photoshop Document) — keeps image quality high and eliminates compression artifacts, the visible distortions introduced by lossy formats such as JPEG.
  * These formats preserve all of the original pixel data. This makes them ideal for editing, retouching, and repeated re-saving, because no quality is lost each time the file is processed.
* **Source image size:**
  * Starting with a **high-resolution image** provides more detail and greater flexibility, because upscaling a small image cannot recover detail that was never captured.
  * When images need to be displayed at different sizes (for example, across devices or screen resolutions), a larger source image allows for better scaling and sharper results at every target dimension.
  * For images that support zoom, such as product photos where customers inspect fine details, aim for dimensions of **around 2,000 pixels or more on the longest side**.
  * Logos or banners that do not require zoom can be uploaded in the largest size needed for their intended use.

Making these choices at the source level directly determines the quality of the final visual content, since every downstream resize, crop, and compression step inherits the strengths or weaknesses of the original file.

<!--
 REMOVED TOPIC AS PER CQDOC-21594
## Best practices for image format (`&fmt=`) {#best-practices-for-image-format-fmt}

* JPG or PNG are the best choices to deliver images in good quality and with manageable size and weight.
* If no format command is supplied in the URL, Dynamic Media Image Delivery defaults to JPG for delivery.
* JPG compresses at a ratio of 10:1 and usually produces smaller image file sizes. PNG compresses at a ratio of about 2:1, except when images contain a white background. Typically though, PNG file sizes are larger than JPG files.
* JPG uses lossy compression, meaning that picture elements (pixels) are dropped during compression. PNG on the other hand uses lossless compression.
* JPG often compresses photographic images with better fidelity than synthetic images with sharp edges and contrast.
* If your images contain transparency, use PNG because JPG does not support transparency.

As a best practice for image format, start with the most common setting `&fmt=JPG`.
-->

## Best practices for image size {#best-practices-for-image-size}

Dynamically reducing image size is one of the most common tasks in image delivery. It involves specifying the target dimensions and, optionally, selecting which downsampling mode is used to downscale the image. The recommended best-practice URL pattern is **`&wid=<value>&hei=<value>&resMode=sharp2`** (or **`&hei=<value>&resMode=sharp2`** when only height is set), which delivers the highest visual quality for resized images.

### Sizing parameters

For image sizing, use **`&wid=<value>`** and **`&hei=<value>`**:

* **`&wid=<value>`** sets the image width.
* **`&hei=<value>`** sets the image height.
* When only one dimension is specified, these parameters automatically calculate the other dimension in accordance with the image's aspect ratio, preserving the original proportions and preventing distortion.

### Downsampling mode (resMode)

**`&resMode=<value>`** controls the algorithm used for downsampling — the process of reducing an image's pixel dimensions. The choice of algorithm directly affects the sharpness and quality of the final scaled image.

* **Start with `&resMode=sharp2`.** This value provides the best image quality because it preserves edge detail and fine texture when scaling images down, producing crisp, artifact-free results.
* **`&resMode=bilin`** (bilinear) is faster, but because it averages pixels more simply, it frequently produces aliasing artifacts — visible jagged edges, moiré patterns, and loss of fine detail. As a result, `bilin` trades image quality for processing speed.

**Unlike** `bilin`, the `sharp2` mode prioritizes visual fidelity, making it the preferred choice for delivering high-quality resized images.

### Recommended best practice

As a best practice for image sizing, use **`&wid=<value>&hei=<value>&resMode=sharp2`** or **`&hei=<value>&resMode=sharp2`**. This combination sets the target dimensions, maintains the correct aspect ratio, and applies the highest-quality downsampling algorithm.

## Best practices for image sharpening {#best-practices-for-image-sharpening}

Image sharpening is the most complex aspect of controlling images on your website, and where many mistakes are made. To learn more about how sharpening and unsharp masking works in Experience Manager, refer to the following helpful resources:

* Best practices white paper [Adobe Dynamic Media Classic Image Quality and Sharpening Best Practices](/help/assets/dynamic-media/assets/sharpening_images.pdf) applies to Experience Manager as well.

* Watch [Use Image Sharpening with Experience Manager - Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-image-sharpening-feature-video-use#dynamic-media).

In Experience Manager, you can sharpen images during ingestion, delivery, or both. As a best practice, sharpen images using only one method—not both. Sharpening images on delivery through a URL delivers the best results in most workflows, because it lets you tune sharpening to the final rendered size rather than baking it into the ingested asset.

There are two image sharpening methods that you can use:

* **Simple sharpening (`&op_sharpen`)** &ndash; Similar to the Adobe Photoshop sharpen filter, it applies basic sharpening after dynamic resizing. This method is not user-configurable; avoid using `&op_sharpen` unless required.
* **Unsharp masking (`&op_USM`)** &ndash; Unsharp masking is an industry standard sharpening filter that increases edge contrast to make an image appear crisper. The best practice is to sharpen images with unsharp masking following the guidelines below. Unsharp masking lets you control the following three parameters:

  * `&op_sharpen=`amount,radius,threshold

    * **[!UICONTROL amount]** (**0-5**, strength of the effect.)
    * **[!UICONTROL radius]** (**0-250**, width of the "sharpening lines" drawn around the sharpened object, as measured in pixels.)

    The **radius** and **amount** parameters have opposing effects: because reducing the radius weakens the effect, you can compensate by increasing the amount. Radius allows finer control because a lower value sharpens only the edge pixels, whereas a higher value sharpens a wider band of pixels, producing a more pronounced halo.

    * **[!UICONTROL threshold]** (**0-255**, sensitivity of effect.)

    This parameter determines how different the sharpened pixels must be from the surrounding area before they are considered edge pixels and the filter sharpens them. The **[!UICONTROL threshold]** parameter helps to avoid over-sharpening areas with similar colors, such as skin tones. For example, a threshold value of **12** ignores slight variations in skin tone brightness to avoid adding "noise," while still adding edge contrast to high contrast areas, such as where eyelashes meet skin.

    For more information about how you set these three parameters, including best practices to use with the filter, see the following resources:

    * Best practices white paper [Adobe Dynamic Media Classic Image Quality and Sharpening Best Practices](/help/assets/dynamic-media/assets/sharpening_images.pdf) applies to Experience Manager as well.

    * Watch [Use Image Sharpening with Experience Manager - Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-image-sharpening-feature-video-use#dynamic-media).

    * Experience Manager also lets you control a fourth parameter: **monochrome (0,1)**. This parameter determines if unsharp masking is applied to each color component separately using the value **0** or to the image brightness/intensity using the value **1**.

As a best practice, start with the unsharp mask radius parameter. Radius settings that you can start with are the following:

* **[!UICONTROL Website]**: **0.2-0.3 pixels**
* **[!UICONTROL Photographic printing (250-300 ppi)]**: **0.3-0.5 pixels**
* **[!UICONTROL Offset printing (266-300 ppi)]**: **0.7-1.0 pixels**
* **[!UICONTROL Canvas printing (150 ppi)]**: **1.5-2.0 pixels**

Follow these steps to refine the sharpening:

1. Gradually increase the amount from **1.75 to 4**.
2. If sharpening is still not satisfactory, increase the radius by a decimal point.
3. Run the amount again from **1.75 to 4**.
4. Repeat as necessary until the result is satisfactory.

Leave the monochrome parameter setting at **0**.

### Best practices for JPEG compression (`&qlt=`) {#best-practices-for-jpef-compression-qlt}

* **The recommended best-practice setting for JPG compression is `&qlt=85,0`.** This value balances high visual quality against a controlled file size for the majority of images.
* This parameter controls JPG encoding quality. A **higher value** means a higher-quality image but a larger file size; a **lower value** means a lower-quality image but a smaller file size. The valid range is **0–100**.
* To optimize for quality, do not set the parameter value to **100**. The difference between a setting of **90 or 95** and **100** is almost imperceptible to the human eye. Because of this, a setting of **100** unnecessarily inflates the image file size without a perceptible visual gain. Therefore, to optimize for quality while avoiding oversized files, set the `qlt= value` to **90 or 95**.
* To optimize for a small file size while keeping image quality at an acceptable level, set the `qlt= value` to **80**. Values below **70–75** introduce significant, visible degradation such as blocking artifacts, banding, and loss of fine detail, so they are not recommended for production imagery.
* As a general best practice, set the `qlt= value` to **85**, which provides a reliable middle ground between quality and file size across a wide range of image content.
* **Using the chroma flag in `qlt=`**

  * The `qlt=` parameter has a second setting that controls **RGB chromaticity downsampling** — a compression technique that reduces the resolution of color (chroma) information while preserving luminance detail. Turn downsampling **on** using the value **`,1`** or **off** using the value **`,0`**.
  * For most workflows, start with RGB chromaticity downsampling turned **off** (**`,0`**). This setting delivers better image quality because it preserves full-resolution color data, which matters most for synthetic images with sharp edges, high contrast, and fine color transitions where downsampling artifacts would otherwise be visible.

As a best practice for JPG compression, use **`&qlt=85,0`**.

## Best practices for JPEG sizing (`&jpegSize=`) {#best-practices-for-jpeg-sizing-jpegsize}

The `&jpegSize=` parameter guarantees that a delivered image does not exceed a specified maximum size, making it essential for delivering JPEG images to **devices with limited memory**. By enforcing an upper bound on file size, it prevents oversized images from overwhelming the available memory on constrained clients.

### How `&jpegSize=` works

* **Set `&jpegSize=` in kilobytes** using the syntax `jpegSize=<size_in_kilobytes>`. This value defines the **maximum allowed file size** for image delivery.
* `&jpegSize=` works in combination with the **JPEG quality (compression) parameter** `&qlt=`. When the JPEG response at the specified `&qlt=` value does **not** exceed the `jpegSize` limit, the image is returned with `&qlt=` exactly as defined, preserving the requested quality.
* If the image **does** exceed the `jpegSize` limit at the specified `&qlt=`, the system incrementally decreases `&qlt=` until the image fits within the maximum allowed size. As a result, quality is reduced only as much as necessary to satisfy the size constraint, ensuring compatibility with the target device.
* If the system determines that the image **cannot** be reduced to fit within the maximum allowed size, it returns an error rather than delivering a non-compliant image.

### Best practice for limited-memory devices

As a best practice, **set `&jpegSize=` and pair it with `&qlt=`** when delivering JPEG images to devices with limited memory. This combination lets you specify both the target quality and the hard size ceiling, so the system delivers the highest possible quality that still fits within the device's memory limits.

## Best practices summary {#best-practices-summary}

To achieve **high image quality with a small file size**, start with the following recommended combination of Dynamic Media Image Serving parameters:

`fmt=jpg&qlt=85,0&resMode=sharp2&op_usm=1.75,0.3,2,0`

This combination produces excellent results under most circumstances and serves as a reliable baseline for the majority of images. The `op_usm` value applies **unsharp mask (USM)** sharpening, where the parameters control the amount, radius, threshold, and monochrome behavior of the effect.

### Fine-tuning sharpening (unsharp masking)

If an image requires further optimization, adjust the **unsharp mask (USM)** parameters gradually using the following procedure:

1. Set the **radius to 0.2 or 0.3** as your starting point.
2. Increase the **amount from 1.75 up to a maximum of 4** — equivalent to **400% in Adobe Photoshop**.
3. Review the rendered image to confirm the desired result is achieved.
4. If the sharpening result is still not satisfactory, increase the **radius in decimal increments**.
5. For every decimal increment of the radius, restart the amount at **1.75** and gradually increase it to **4**.
6. Repeat steps 4 and 5 until the desired result is achieved.

While the values above represent an approach that creative studios have validated, you can start with other values and follow other strategies. Whether the results are satisfactory is a subjective matter, so **structured, iterative experimentation is essential** to arrive at the best balance between sharpness, quality, and file size for each image.

### Workflow optimization tips

As you experiment, the following general suggestions help optimize your workflow:

* **Test parameters in real time on a URL.** Adjusting values directly in the URL lets you preview the effect immediately and iterate quickly.
* **Group commands into an image preset.** Dynamic Media Image Serving commands can be grouped into an image preset. An image preset is a set of URL command macros assigned a custom preset name, such as `$thumb_low$` and `&product_high$`. Referencing the custom preset name in a URL path calls these presets. This functionality helps you manage commands and quality settings for different image usage patterns across your website, promotes consistent settings through reuse, and shortens the overall length of URLs.
* **Use advanced tuning options in Experience Manager.** Experience Manager also provides more advanced ways to tune image quality, such as applying sharpening on ingestion. To tune and optimize rendering results, [Adobe's consulting services](https://business.adobe.com/customers/consulting-services/main.html) can provide customized insight and best practices.
