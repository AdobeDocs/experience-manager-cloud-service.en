---
title: Dynamic Media best practices
description: Learn about best practices in Dynamic Media when it comes to working with images and video and best practices for Dynamic Media Viewers.
contentOwner: Rick Brough
products: Experience Manager as a Cloud Service
topic-tags: introduction,administering
content-type: reference
feature: Adaptive Streaming, Best Practices, Smart Imaging, Image Profiles, Rulesets, Viewers, Smart Crop, SEO Optimization, Publishing, Video, Renditions, Asset Management
role: User, Admin
mini-toc-levels: 4
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 39e491bb-367d-4c72-b4ca-aab38d513ac5
---
# Dynamic Media best practices{#about-dm-best-practices}

<!--
**Organizations today must connect with their customers through an ever-growing array of channels and devices.** The customer experience spans physical stores, websites, mobile apps, social media, email, and e-commerce platforms. This diversity requires organizations to create many more versions of each piece of content. Personalization adds complexity by increasing the number of variations needed for each item. Despite budget constraints for content creation, there's still a need to produce more campaigns in the same timeframe, on a global scale. AEM Dynamic Media offers a comprehensive set of tools to meet these challenges, providing consistent, personalized, high-performance, and optimized brand experiences across all channels and devices. 

Key Features of AEM Dynamic Media:

* **Single File Approach:** Save on storage costs by storing just one master file. AEM Dynamic Media generates all size variations and visual effects on-demand, at the time of delivery, eliminating workflow complexity and last-minute creative changes.
* **Global Reach:** With Smart Imaging, images are automatically optimized during delivery, significantly reducing file size and page weight without sacrificing visual quality. This optimization is tailored for network bandwidth and device pixel ratio.
* **AI-Powered Efficiency:** Smart Crop uses AI to automate the cropping of images and videos, focusing on points of interest. This feature saves countless hours of manual editing and is designed for large-scale enterprise production.
* **Video Made Simple:** Upload a master video file and AEM Dynamic Media will adaptively stream it in multiple languages and with descriptive audio, ensuring a broad reach.
* **Customizable Experience Viewer:** Select, customize, and brand the experience viewers for images and videos with ease. These viewers can be seamlessly integrated into any digital experience.
* **Support for Emerging Formats:** AEM Dynamic Media is also your solution for delivering immersive 3D and panoramic experiences.

In the accompanying guide, you'll find a comprehensive list of best practices for maximizing the benefits of AEM Dynamic Media. As you embark on your Dynamic Media journey, make sure to consult these expert recommendations and resources.

Stage Business Problem Best Practice Recommendation: This section will outline specific business challenges and provide targeted best practices and recommendations to address them effectively.
-->



{{see-also-dm}}

Dynamic Media on Adobe Experience Manager (AEM) is a comprehensive solution that optimizes asset delivery, handles personalization, and ensures consistent, performant, and brand-aligned experiences across channels and devices. Organizations today face an explosion of channels and devices for engaging with users, and the customer journey now spans physical stores, web, mobile, social media, emails, and commerce. Delivering the right asset, at the right size, to each of these touchpoints is precisely the challenge Dynamic Media is built to solve.

Some of the key tenets of Dynamic Media include the following:

* **Single file approach:** With Dynamic Media, you store one primary source file, and all size variations and visual effects are dynamically created and optimized at the time of delivery. This approach saves storage costs and eliminates workflow complexity, because teams no longer maintain and manage separate renditions for every channel, device, or resolution.
* **Truly global:** **Smart Imaging**, applied during content delivery, significantly reduces image size and page weight without compromising visual quality. It is optimized for network bandwidth and device pixel ratios, delivering faster-loading experiences that adapt automatically to each viewer's connection and screen.
* **AI powered:** **Smart Crop**, an AI-driven feature, automates image and video point-of-interest cropping. It eliminates manual effort and scales efficiently for enterprise use, ensuring the most important part of each asset stays in frame across every aspect ratio.
* **Easy video:** Upload primary source videos into Dynamic Media and stream them adaptively across multiple languages with descriptive audio. Adaptive streaming adjusts video quality to the viewer's bandwidth for smooth, buffer-free playback.
* **Experience viewer library:** Customize and brand experience viewers for images and videos. These viewers seamlessly integrate into your digital experiences, providing interactive presentation of assets that match your brand look and feel.
* **Emerging format support:** Dynamic Media enables the delivery of 3D and panoramic experiences, supporting immersive, interactive product presentations that extend beyond flat images and standard video.

As you explore the [Dynamic Media Journey](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dm-journey/dm-journey-part1), the consolidated list of best practices below helps you make the most of its capabilities. Adapt these Dynamic Media best practices to your specific context and project requirements so you can optimize your experiences across channels and devices.



<!-- In Dynamic Media on AEM, there are sets of methods, techniques, and guidelines that can help you maximize the potential of your rich media content. These best practices can lead to optimal results and increase efficiency in your use of Dynamic Media. They represent the most efficient and effective courses of action in a particular situation. They also unlock high value for your audience and deliver high-quality, engaging content. -->

>[!IMPORTANT]
>
>The Dynamic Media best practices in this article may evolve over time as new technologies in Dynamic Media emerge. The information below is current for the latest version of Dynamic Media.

## Ingest assets into Dynamic Media

**Business case:** *Efficiently manage large volumes of assets and ensure that only relevant, approved content is delivered to end users.*

Dynamic Media provides two complementary controls for managing large asset libraries: **Selective Sync** and **Selective Publish**. Together, these features let you manage large numbers of assets efficiently while ensuring that only the appropriate, authorized content reaches your end users. Selective Sync governs which assets enter the delivery pipeline, and Selective Publish governs which of those assets become visible to customers.

* **Selective Sync — control which assets enter the delivery pipeline:**
Selective Sync is a proactive feature that lets you choose which assets to sync with Dynamic Media. For example, you can sync only those folders containing assets that have received final approval, or exclude drafts, works-in-progress, and rejected variants from ever reaching the delivery layer. This staged workflow keeps you in control over which assets are being prepared for delivery to your customers, because assets that are not synced cannot be inadvertently published or served.

* **Selective Publish — control which synced assets customers see:**
After syncing your assets, Selective Publish gives you control over which assets are visible to your customers. This ability means you govern which approved assets are actually delivered through your channels. As a result, customers see only the best and most relevant content, while unapproved or superseded assets remain hidden from public-facing channels even if they exist within Dynamic Media.

Used together, **Selective Sync** and **Selective Publish** deliver better control, governance, and productivity over your rich-media content, reducing the risk of unapproved assets reaching end users and streamlining the approval-to-delivery process.

For step-by-step configuration guidance, see [Configure Selective Publish at the folder level in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md).

## Dynamic Media Viewers

Dynamic Media Viewer best practices are essential guidelines that optimize the performance, functionality, and user experience of Dynamic Media assets on Adobe Experience Manager (AEM). The core best practices are: **synchronizing viewer assets**, **publishing assets before delivery**, **using muted autoplay for videos**, **applying smart cropping**, **following JavaScript file inclusion rules**, and **adhering to viewer-specific embedding guidelines**. These practices ensure that assets are properly synchronized, published, and configured to use the full capabilities of Dynamic Media.

By following these best practices, you achieve seamless integration, efficient asset management, and enhanced viewer interactions. Synchronizing assets, using smart cropping, and adhering to JavaScript file inclusion guidelines are all critical practices. These practices maintain the integrity and reliability of media delivery across desktop, mobile, and tablet devices.

* **Synchronize Viewer Assets:**
Ensure that all viewer assets are synchronized with Dynamic Media before using the player.

  * Access the sample manager page at `/libs/dam/gui/content/s7dam/samplemanager/samplemanager`. This page lets you resynchronize a viewer's assets, including out-of-the-box icons, Cascading Style Sheets (CSS) files, and presets.
  * If you encounter any viewer issues, go to the [Troubleshoot Dynamic Media Viewers](/help/assets/dynamic-media/troubleshoot-dm.md#viewers) article.

* **Publish Assets:**
Make sure that assets are published before viewing them in delivery viewers. Unpublished assets do not render correctly in the delivery environment.
* **Autoplay Videos Muted:**
For autoplay functionality in videos, use muted video settings. This is because modern browsers block the autoplay of videos with sound, so muting the video ensures autoplay executes reliably across supported browsers.
* **Smart Cropping:**
Use the **Image v3 component** for smart cropping to enhance image asset presentation. Smart cropping automatically preserves the focal point of an image across multiple aspect ratios.
* **JavaScript File Inclusion:**
Only include the primary viewer JavaScript file on your page. Avoid referencing additional JavaScript files that the viewer's runtime logic may download. Specifically, do not directly link to the **HTML5 SDK** `Utils.js` library from the `/s7viewers` context path (known as the consolidated SDK include). The viewer's logic manages the location of **`Utils.js`** or similar runtime viewer libraries, and this location can change between releases. Adobe does not retain older versions of secondary viewer includes on the server. As a result, directly referencing these secondary files breaks viewer functionality after future updates.
* **Embedding Guidelines:**
Use the documentation for embedding guidelines that are specific to each viewer, because embedding requirements differ from one viewer type to another.
For additional details, refer to [Viewers for AEM Assets](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/library/viewers-aem-assets-dmc/c-html5-s7-aem-asset-viewers).
* **SDK Tutorial and Examples:**
Review the [Viewer SDK Tutorial](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/library/c-tutorial) and [HTML5 SDK application examples](https://s7d9.scene7.com/s7sdk/2024.5/docs/jsdoc/index.html) for a thorough understanding of SDK component Application Programming Interfaces (APIs).

## Prepare assets for delivery



### Organize your assets

**Business case:** *Efficiently organize assets to streamline workflows.*

For efficient asset organization that streamlines workflows, use one or more of the following best practices:

* **Organize assets in folders:**
Organizing assets effectively involves categorizing them into folders, similar to file organization on a computer. Proper naming, structuring subfolders, and file management within these folders directly determine how efficiently assets can be located, processed, and reused. Implementing systematic **naming conventions** and consistent **metadata** practices maximizes the utility of your digital asset repository, because standardized structures let both users and automated systems retrieve the right file quickly.
Want to learn more? Go to [Organize assets in folders](/help/assets/organize-assets.md#organize-using-folders).
* **Organize assets using tags:**
**Tagging assets** directly improves searchability, streamlines collection creation, and boosts search ranking, because descriptive tags give each asset multiple retrieval pathways. **Adobe AI** employs a self-learning algorithm for precise tagging that enables quick asset retrieval. Adobe AI also recognizes and assigns relevant tags&ndash;including custom ones&ndash;to assets, simplifying asset management with automatic, descriptive tagging.
Want to learn more? Go to [Organize assets using tags](/help/assets/organize-assets.md#use-tags-to-organize-assets).
* **Organize assets as collections:**
**Dynamic Media** together with **Experience Manager Assets** enables the efficient creation, editing, and sharing of asset collections among users, making it easier for teams to reuse approved content across projects. You can establish various collection types, including **static lists** and **dynamic, search-based compilations**. These collection types can be shared across diverse locations with customizable access and editing rights.
Want to learn more? Go to [Organize assets as collections](/help/assets/manage-collections.md).
* **Organize assets using profiles:**
A **processing profile** automates asset handling in designated folders, which streamlines organization by applying the same rules to every file that enters a folder. Standardizing **metadata, file names, and folder structures** allows for consistent and precise application of these profiles as your digital asset collection expands.
Want to learn more? Go to [Organize assets using profiles](/help/assets/organize-assets.md#organize-to-use-profiles).

### Optimize the quality of images

**Business case:** *Obtain good quality images from Dynamic Media.*

Adobe Experience Manager Dynamic Media provides **more than 100 Dynamic Media commands** for image enhancement, giving you precise control over how images render across delivery channels. Optimizing image quality depends primarily on three technical factors: **sizing, sharpening, and format selection**. While tuning these settings can be time-intensive, proven best practices deliver consistent, high-quality results.

#### Best practices for image quality

Focus on these core areas to achieve optimal image quality in Dynamic Media:

- **Optimal image sizing** — deliver images at the correct dimensions to preserve clarity and reduce unnecessary file weight.
- **Image sharpening** — apply appropriate sharpening to keep detail crisp after resizing and compression.
- **Best image formats** — choose the format best suited to each use case to balance quality and performance.

For detailed guidance, see [Best practices for optimizing the quality of your images](/help/assets/dynamic-media/best-practices-for-optimizing-the-quality-of-your-images.md).

#### Why a systematic testing approach matters

Perception of image quality varies from person to person, so a systematic approach to experimentation is essential for achieving reliable, repeatable results. Because visual quality is subjective, testing commands directly against your own images removes guesswork and lets you validate results before deployment. Adobe Experience Manager supports this process with its extensive library of **more than 100 Dynamic Media commands** for image enhancement.

Watch [Dynamic Media Snapshot](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-snapshot) (3 minutes, 17 seconds) for a walkthrough.

#### How to test commands on your images

To assess how different commands affect image quality, follow these steps:

1. Upload an image to Dynamic Media.
2. Open the tool's interface at the specified URL.
3. Apply the commands you want to evaluate and compare the results directly.

Launch [Dynamic Media Snapshot](https://snapshot.scene7.com/) to try it.

### Standardize on styles applied to images

**Business case:** *Efficiently standardize the style and transformation applied to my image assets.*

An **Image Preset** in Dynamic Media is a named, reusable set of commands that automatically sizes and formats your image assets. Applying Image Presets regularly consistently and dynamically adjusts your images across every rendering, so you never manually reprocess the same asset for each device or context.

Think of an Image Preset as a macro. It bundles your sizing and formatting rules into a single named configuration that renders on demand.

#### What an Image Preset controls

Each Image Preset can standardize:

- **Image size** — width, height, and scaling dimensions for the delivered asset.
- **Format** — the output file format used for delivery.
- **Properties** — additional transformations such as compression and quality settings.

#### How Image Presets work

Because an Image Preset is a named set of commands for sizing and formatting, it ensures every asset renders identically wherever the preset is applied. This eliminates inconsistent one-off edits and guarantees that the same style and transformation are enforced across your entire asset library.

#### A common use case

If your site needs product images in various sizes and formats — with specific compression tuned separately for desktop and mobile — Image Presets automate this process efficiently. Rather than exporting multiple variants of each product image by hand, you define the rules once and Dynamic Media generates the correct rendition dynamically. This reduces manual effort, keeps your visual presentation uniform, and speeds delivery across viewing contexts.

Get started with Image Presets: go to [Fundamentals of creating image presets to render assets](/help/assets/dynamic-media/dm-journey-part2.md#dm-journey-e).

### Adjust the focus and framing of images and videos

**Business case:** *Ensure that the main point of interest of images or videos remains in focus across all devices.*

**Smart Crop** is a feature in **Dynamic Media** that uses **Adobe AI**, Adobe's artificial intelligence and machine learning framework, to automate the cropping of images and videos. Smart Crop intelligently detects and focuses on the main subject or point of interest in an image or video, then keeps that focal point centered as the media is served to different screens.

#### How Smart Crop works

Smart Crop analyzes each image or video, identifies the primary subject, and automatically frames the crop around it. This detection maintains the focal point across various screen sizes on both desktop computers and mobile devices. Because viewers access content on displays with widely different dimensions and aspect ratios, this automation removes the need to manually crop separate versions for each device, delivering a consistent, subject-focused experience wherever the content appears.

#### Best practice: Create an Image Profile with Smart Crop

The recommended approach is to create an **Image Profile** with Smart Crop enabled:

1. Create an Image Profile and apply Smart Crop.
2. Define the various screen sizes you need to support within the profile.
3. Apply the profile so **Adobe AI** automatically generates the optimized crops for each defined size.

With this configuration, images and videos are consistently optimized for the viewer's device, ensuring the intended point of interest remains in focus.

#### Learn more

Additional resources on configuring and applying Smart Crop:

- [Using Smart Crop with AEM Assets Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use) — Adobe Experience Manager (AEM) Assets (6 minutes, 35 seconds)
- [Using Dynamic Media Smart Crop for Video](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/video/dynamic-media-smart-crop-video) (6 minutes, 22 seconds)

### Improve SEO rankings

**Business case:** *Configure Dynamic Media to get improved Search Engine Optimization (SEO) rankings.*

Use the following recommendations regularly to ensure that your images contribute effectively to your overall SEO strategy.

* **Meaningful image file names:**
Use descriptive file names that reflect the image content. For example,

  * use `myCompany-Silver-Wrist-Watch`
  * *avoid* `myCompany_Silver_Wrist_Watch` or `myCompanySilverWristWatch`

  Descriptive file names help search engines understand the image context and improve SEO, because crawlers use file names as a signal for image content and relevance. **Google prefers hyphens** over underscores or spaces in a file name, because hyphens are interpreted as word separators while underscores are not. Also, avoid concatenating words in a file name, since joined words cannot be parsed into distinct keywords by search engines.
* **Custom domain:** 
Implement a custom domain that includes your company or brand name to reinforce brand recognition and trust, because a branded image URL signals ownership and authority to both users and search engines. For example,

  * use `http://images.mycompany.com/is/image/companyname/`
  * *avoid* `https://s7d1.scene7.com/is/image/folder/AdobeStock_28563982`

* **SEO-friendly folder structure:**
Organize your images in a folder structure that includes your company name or brand for better indexing, because a consistent, brand-aligned URL path helps search engines associate images with your domain, like `http://images.mycompany.com/is/image/companyname/`.
* **Dynamic Media rule sets:**
Learn how you can conditionally transform URLs based on various factors, enhancing SEO and user experience.
Want to learn more? Go to [Use rule sets to transform URLs](/help/assets/dynamic-media/using-rulesets-to-transform-urls.md).
* **Smart Imaging and Smart Crop:**
Use Smart Imaging and Smart Crop features in Dynamic Media to serve optimized and responsive images. As a result, page load times decrease and SEO rankings improve, because faster, responsive images directly enhance Core Web Vitals and the overall user experience that search engines reward.
Want to learn more? Go to [Smart Imaging](/help/assets/dynamic-media/imaging-faq.md), or watch [Using Smart Crop with AEM Assets Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use) (6 minutes, 35 seconds), which demonstrates Smart Crop within Adobe Experience Manager (AEM) Assets Dynamic Media.

These best practices align directly with Google's image SEO best practices, reinforcing their reliability as an authoritative approach to image optimization. Such practices emphasize the importance of providing context and clarity to search engines through proper naming conventions, structured data, and optimized image delivery. Consistent naming, branded URL structures, and responsive delivery work together to make images more discoverable, more crawlable, and more likely to rank in image search results.

Want to learn more? Go to [URL structure best practices for Google](https://developers.google.com/search/docs/crawling-indexing/url-structure) and [Google image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)

### Dynamically enhance images and create visual effects using commands

**Business case:** *Apply rich visual effects to images.*

Dynamic Media offers a suite of commands for enhancing images and creating visual effects dynamically, eliminating the need to store and manage multiple static asset variations. The following are some brief explanations of a few of these processes and some examples to guide you:

#### Effects inside the source image

| Task | What to do |
| --- | --- |
| **Upload and publish your original image** | <ul><li> Start by uploading the original image to Dynamic Media.</li><li> Make sure that it is published and accessible through a URL (Uniform Resource Locator).</li><li> In this example, a stock image of a watch with a white background (let's call it "Image X") is uploaded to Dynamic Media.<br>[https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer](https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer)</li></ul> |
| **Create a mask** | <ul><li> Develop a mask that defines the subject (the area where you want to apply effects) and the background (the area you want to change).<br>[https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer-maskps](https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer-maskps)</li><li> Masks are typically grayscale images, where **white represents the subject** and **black represents the background**. You can create masks using tools like Adobe Photoshop.<br>For detailed guidance, see [Creating and editing a quick mask in Photoshop](https://helpx.adobe.com/in/photoshop/using/create-temporary-quick-mask.html).</li><li> For "Image X," create a mask that precisely outlines the subject you want to enhance. For example, a person, an object, and so on.</li></ul> |
| **Apply Dynamic Media URL commands for effects** |  After you have your mask, use URL commands to apply effects like an outer glow or change the background color to "Image X." Here are two examples:<ul><li> **Outer glow effect:**<br>To add an outer glow effect along the subject's boundary, edit the URL like this:<br>[https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&effect=-1&pos=100,100&op_blur=75&op_grow=1&opac=25](https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&effect=-1&pos=100,100&op_blur=75&op_grow=1&opac=25)<br>In this URL, the `op_blur`, `op_grow`, and `opac` parameters create the outer glow effect, because `op_blur` softens the edge, `op_grow` expands the glow outward from the subject boundary, and `opac` controls its opacity.</li><li> **Background color change:**<br>To change the background color, use the URL with a different background color value:<br>[https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&maskUse=invert&color=255,255,0](https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&maskUse=invert&color=255,255,0)<br> In this example, `color=255,255,0` sets the background color to yellow. Edit the background to a specific color for visual impact.</li></ul> |

#### Add an image border

Dynamic Media manipulates images directly through URLs, which makes it a powerful tool for creating dynamic digital experiences on demand. The following are some examples. Let's start with the following original image URL: [https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel).

| Task | What to do |
| --- | --- |
| **White border** | To add a white border, use the following URL:<br>[https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10)<br>In this URL, the **`extend=10,10,10,10`** parameter specifies a **border size of ten pixels on all sides**. |
| **Blur along the white border** | To add a blur effect along the white border, edit the URL as follows:<br>[https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&op_blur=60&color=0,0,0](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&op_blur=60&color=0,0,0)<br>In this URL, the **`effect=-1`** parameter applies the blur effect, and **`op_blur=60`** controls the blur intensity. |
| **Drop shadow effect along the outer boundary** | To add a drop shadow effect along the outer boundary, use this URL:<br>[https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&$shadow$&color=0,0,0](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&$shadow$&color=0,0,0)<br>The **`$shadow$`** parameter creates the shadow effect, and **`color=0,0,0`** sets the shadow color to black.  |

Adjust these URL parameters to achieve the desired visual effects.

#### Create image overlays

Dynamic Media lets you composite one image on top of another directly through URL commands, allowing you to build layered visuals such as logos, badges, watermarks, or promotional labels without producing a separate merged asset for each combination. An overlay works by referencing a base (background) image and specifying an additional image to place on top of it, along with parameters that control its position, size, and blending.

The general approach is:

1. **Publish both images to Dynamic Media.** Confirm that the base image and the overlay image are each published and accessible through their own URLs.
2. **Reference the base image in the URL.** Begin the request with the base image path, just as you would for any Dynamic Media command.
3. **Add the overlay image using layer parameters.** Append the overlay image reference and control its placement, using position parameters to set where the overlay sits relative to the base image and sizing parameters to scale it.
4. **Refine appearance and blending.** Adjust opacity and blending so the overlay integrates cleanly with the base image, for example to reduce a watermark's visibility or align a badge to a corner.

Because both images are combined at request time rather than in a pre-rendered file, a single base image can be reused with many different overlays, which keeps asset libraries smaller and makes campaign updates faster. Adjust these overlay parameters to position and blend the layered image for the desired result.

If you are looking to superimpose a logo or icon on an existing image, Dynamic Media provides a straightforward way to achieve this using URL (Uniform Resource Locator) commands. Let's break down the steps.

| Step | What to do |
| --- | --- |
| **Upload and publish the base image** | First, upload and publish the base image on which you want to superimpose the logo or icon. You can use any image as your base.<br>For example, here is a base image:<br>[https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa](https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa). |
| **Upload and publish the logo or icon image** | Next, upload and publish the image that you want to superimpose over the base image. This image should be a transparent PNG (Portable Network Graphics) with the logo or icon you want to overlay, because transparency lets the underlying base image show through around the overlaid object.<br>Here is the transparent PNG image of a star object with transparency effects that is going to be superimposed:<br>[https://s7g2.scene7.com/is/image/genaibeta/decorate-star](https://s7g2.scene7.com/is/image/genaibeta/decorate-star) |
| **Apply the Dynamic Media URL** | Now, create a Dynamic Media URL that combines the base image and the logo or icon image. You can use URL commands to achieve this effect.<br>The URL structure looks something like this:<br>[https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa?layer=1&src=decorate-star&scale=1.25&posN=0.33,-.25&fmt=png](https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa?layer=1&src=decorate-star&scale=1.25&posN=0.33,-.25&fmt=png)<br>where the asset<ul><li> `decorative-room-sofa` is the base image.</li><li> `decorate-star` is the logo/icon image.</li><li> `layer=1` specifies that the logo or icon is layered over the base image, so it renders on top of the base image.</li><li> `scale=1.25` adjusts the size of the logo/icon.</li><li> `posN=0.33,-.25` determines the position of the logo/icon relative to the base image.</li><li> `fmt=png` ensures that the output is in PNG format.</li></ul> |

For more details on the `src` command and other Dynamic Media URL commands, refer to the official [src](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/r-src) reference documentation.

#### Overlaying promotional text

The following are the steps for overlaying a promotional text message on an image using HTML (HyperText Markup Language) and CSS (Cascading Style Sheets).

| Step | What to do |
| --- | --- |
| **Upload and publish the base image** | First, upload and publish the base image on which you want to superimpose the text. You can use any image you like. For example, here's a sample base image:<br>[https://s7g2.scene7.com/is/image/genaibeta/leather-sofa](https://s7g2.scene7.com/is/image/genaibeta/leather-sofa)<br> |
| **Apply Dynamic Media text operators** | Using Dynamic Media, you can apply text operators to overlay dynamic text directly onto the image. The following sample URL demonstrates this ability:<br>[https://s7g10.scene7.com/is/image/genaibeta/leather-sofa?layer=1&posN=-0.3,-0.455&text=%7b\rtf1\ansi%7b\fonttbl%7b\f0+Arial;%7d%7d%7b\colortbl+\red255\green255\blue255;%7d\copyfit1000\vertalc\qc%7b\cf0\fs42+New+Collection%7d%7d&size=370,70&textAttr=130&bgcolor=FF3333&wid=600&hei=600](https://s7g10.scene7.com/is/image/genaibeta/leather-sofa?layer=1&posN=-0.3,-0.455&text=%7b\rtf1\ansi%7b\fonttbl%7b\f0+Arial;%7d%7d%7b\colortbl+\red255\green255\blue255;%7d\copyfit1000\vertalc\qc%7b\cf0\fs42+New+Collection%7d%7d&size=370,70&textAttr=130&bgcolor=FF3333&wid=600&hei=600) |

#### Resizing and cropping for various use cases

##### Image resizing basics

Image resizing alters an image's dimensions, resolution, and file size. Key points to consider include:

* **Pixel composition:**
Digital images consist of tiny dots called pixels. When an image is created, it has a specific number of pixels. Resizing adds or subtracts pixels to change the image's dimensions, resolution, and file size.
* **Aspect ratio:**
Maintaining the aspect ratio (the relationship between width and height) is crucial to prevent distortion. Whether you are upscaling (making an image larger) or downscaling (making it smaller), preserving the aspect ratio ensures visual consistency.
* **Quality considerations:**
Resizing directly impacts image quality. Avoid drastic upscaling, because it leads to pixelation. Instead, reproduce the image at a larger size and resolution. For smaller images, use the appropriate tools to maintain resolution.

##### Cropping versus resizing

Cropping and resizing are techniques in Dynamic Media that let you transform images to suit various use cases, whether it is creating thumbnails, product display images, or banners.

* **Cropping:**
Removes part of an image to alter its composition and framing. Cropping preserves the overall dimensions while focusing on a specific area.
* **Resizing:**
Adjusts the entire image's dimensions, resolution, and file size while maintaining the aspect ratio.

The following use case demonstrates cropping and resizing applied to a living room image, illustrating how each technique adapts the same asset for different presentation needs.

##### Image Renditions from a Single Source

All renditions below are generated on demand from **one master image** using Adobe Dynamic Media (Scene7) URL commands. Because each variation is derived dynamically from the same source, there is **no need to store multiple files** — the delivery parameters appended to the URL control size, cropping, and fit.

* **Original living room image:**
    The unmodified master asset from which every rendition is derived.
    [https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa](https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa)

* **Thumbnail (200 px x 200 px):**
        A **200 x 200 pixel** rendition produced with the `wid` (width) and `hei` (height) commands. This smaller, lower-payload version loads quickly, making it ideal for image grids, previews, and listing pages where fast rendering matters.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&fit=crop)

* **Thumbnail with crop (200 px x 200 px):**
        A **200 x 200 pixel** thumbnail cropped to focus on the sofa. The `cropN` command uses **normalized coordinates** (`.24,.24,.6,.72`), where the first two values set the crop origin and the last two set its width and height as fractions of the full image. This isolates the sofa region before scaling, so the subject remains prominent even at small sizes.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&cropN=.24,.24,.6,.72&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&cropN=.24,.24,.6,.72&fit=crop)

* **Product display image (800 px x 600 px):**
        An **800 x 600 pixel** rendition that applies the same `cropN=.24,.24,.6,.72` framing at a larger size, then resizes for a detailed product view. This makes it suitable for showcasing the sofa on product detail pages, where clarity and subject focus are required.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=800&hei=600&cropN=.24,.24,.6,.72&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=800&hei=600&cropN=.24,.24,.6,.72&fit=crop)

* **Banner (1720 px x 820 px):**
        A wide **1720 x 820 pixel** banner derived from the original, using `cropN=0,.1,1,1` to trim the top of the frame while retaining the full width. This produces a landscape composition that emphasizes the overall room, making it well suited for hero banners and page headers.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=1720&hei=820&cropN=0,.1,1,1&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=1720&hei=820&cropN=0,.1,1,1&fit=crop)

Each rendition above demonstrates how a single master image serves multiple presentation needs — thumbnails, cropped previews, product views, and banners — by adjusting URL commands alone. The full set of image-serving commands, including additional sizing, cropping, and fit options, is documented in the [Command reference](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/c-command-reference).

### Deliver GIF images

**Business case:** *Stream GIFs using Dynamic Media*

You can upload and deliver Graphics Interchange Format (GIF) images through Dynamic Media. **To render an animated GIF, replace `is/image` with `is/content` in the URL path.** This single change switches the delivery mode from a static image to the full animation.

The two path prefixes serve distinct roles:

* **`is/image`** routes the asset through the image-rendering pipeline, producing a **static view** of the GIF (the first frame is served as a still image).
* **`is/content`** streams the original file directly, producing the **animated view** of the GIF.

#### Static versus animated delivery

For example, if you uploaded `abc.gif`, use the following URL paths:

* This URL path renders a **static view** of the GIF:

  ```
  https://<your-server>/is/image/<company>/abc.gif
  ```

* This URL path renders the **animation view** of the GIF:

  ```
  https://<your-server>/is/content/<company>/abc.gif
  ```

#### Important limitation

>[!NOTE]
>
>When using `is/content` in the URL path, image transformation commands are not applied to the asset. This occurs because `is/content` streams the original file directly rather than routing it through the image-rendering pipeline. As a result, transformation commands such as sizing, cropping, and format conversion are ignored when the GIF is delivered through `is/content`. If you need those transformations, use `is/image`, but note that this returns only the static, non-animated view.

### Publish a video for my website

**Business case:** *Quickly publish a video for a marketing site.*

* **Step 1 — Select a video profile:**
  First, in Dynamic Media, select a suitable video profile. You can opt for the *Adaptive Video Encoding* profile available in Adobe Experience Manager (AEM) Assets under Video Profiles. These pre-defined encoding settings ensure that your video is optimized for playback across various devices and bandwidth conditions. Adaptive encoding works by generating multiple renditions of the source video, so the player can automatically serve the resolution best suited to each viewer's screen and connection speed. Alternatively, you can create your own Adaptive Video profile to tailor these settings.
* **Step 2 — Assign the profile:**
  Assign the chosen video profile to the folders where your video is going to be uploaded. This step ensures that the correct encoding settings are applied automatically during the upload process, because Dynamic Media references the folder-level profile when it processes each new asset.
* **Step 3 — Upload the original video:**
  Upload the original video file. Ensure it is a high-resolution video with good quality. The better the source video, the better the final result, since adaptive encoding derives every playback rendition from the original file.
* **Step 4 — Preview and publish:**
  Preview the video to confirm that everything looks as expected. Once satisfied, publish the video. This step makes the video accessible to your audience by activating its delivery through Dynamic Media.
* **Step 5 — Link or embed:**
  After publishing, you have two options for adding the video to your marketing site.

    * **Link directly:**
    Use the provided URL to link directly to the video. Hyperlink it appropriately on your marketing site so visitors can open the video from your pages.
    * **Embed the video:**
    Copy the embedded code provided and paste it into the HTML of your web page where you want the video to appear. This allows the video to play directly on your site, giving visitors an inline viewing experience without leaving the page and keeping engagement on your marketing content.

Want to learn more? Go to [Video](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/video).

### Configure videos for optimal quality and engagement

**Business case:** *Set up videos for the best quality and engagement.*

To ensure the best quality and engagement for your videos, implement the following best-practice strategies:

* **Use the built-in HTML5 Video Viewer:**
        The Dynamic Media HTML5 Video Viewer Presets are robust video players that eliminate common issues associated with HTML5 video playback and mobile devices.
        These presets address challenges like adaptive bitrate streaming delivery and limited desktop browser reach.
        For details, see [Best practice: Using the HTML 5 video viewer](/help/assets/dynamic-media/video.md#best-practice-using-the-html-video-viewer).

* **Use Dynamic Media Video Profiles:**
        Dynamic Media Video Profiles ensure efficient video management, consistent quality, and adaptive streaming.
        For details, see [Dynamic Media Video Profiles](/help/assets/dynamic-media/video-profiles.md).

* **Follow Best Practices for Video Encoding:**
        Apply video encoding profiles that preserve the original video quality without excessive downscaling during encoding. This retains visual fidelity and prevents the quality loss that degrades viewer engagement.
        For details, see [Best practices for encoding videos](/help/assets/dynamic-media/video.md#best-practices-for-encoding-videos).

* **Adopt adaptive streaming instead of progressive streaming:**
        Adaptive streaming automatically adjusts video quality in real time based on the viewer's Internet connection speed and device capabilities, so playback stays smooth as network conditions change.
        It uses protocols like **HLS (HTTP Live Streaming)** or **DASH (`Dynamic Adaptive Streaming over HTTP`)** to ensure optimal playback quality.
        Unlike progressive streaming, which delivers a single fixed-quality file linearly regardless of network conditions, adaptive streaming minimizes buffering and delivers a seamless viewing experience across devices.

### Internationalizing videos for multilingual consumption

**Business case:** *Make videos ready for multilingual consumption.*

Internationalizing videos for multilingual consumption is essential for reaching a global audience and delivering content that resonates across regions and languages. Dynamic Media provides a comprehensive set of features that enable you to achieve this goal.

* **Upload your videos:**
     * First, create a video encoding profile. You can either use the predefined Adaptive Video Encoding profile that comes with Dynamic Media or create your own custom profile.
     * Associate the video processing profile with one or more folders where you upload your primary source videos.
     * Upload your primary source videos to these folders. As a result, Dynamic Media automatically encodes each video based on the assigned video processing profile.
     * Dynamic Media primarily supports **short-form videos of up to 30 minutes**, with a **minimum resolution greater than 25 &times; 25**. You can upload **video files up to 15 GB each**1.

* **Manage your videos:**
     * Organize, browse, and search video assets within Adobe Experience Manager (AEM).
     * Preview and publish video assets.
     * View the source video and its encoded renditions along with associated thumbnails.
     * Edit video properties, such as title, description, and tags2.

* **Localization:**
     * For each target geography/language, create audio tracks and subtitles.
     * Add these audio and subtitle tracks to your videos from the AEM interface.
     * As users play the videos, they can select their preferred language for audio and subtitles, ensuring each viewer receives content in the language most relevant to them.

* **Publishing:**
     * If you are using AEM as your Web Content Management (WCM) system, you can directly add videos to your web pages.
     * If you are using a third-party WCM system, you can link or embed videos on your web pages using URLs or embed codes, providing flexibility regardless of your publishing platform.

Want to learn more? Go to [About multiple caption and audio track support for videos in Dynamic Media](/help/assets/dynamic-media/video.md#about-msma).

## Deliver assets to customers



### Optimize image sizes and minimize page load times

**Business case:** *Optimize the size of images for any browser or screen and reduce page load time.*

**Dynamic Media Smart Imaging automatically optimizes** the image's format, size, and quality based on each client's browser capabilities, enhancing image delivery performance without manual configuration.

Adobe recommends that you use Smart Imaging's capabilities rather than manually setting the image format to `webp` or `avif`. Smart Imaging is the recommended approach for the following reasons:

* **Browser compatibility:**
  Smart Imaging ensures that the delivered image format is compatible with the user's browser.
* **Optimal compression:**
  It selects the best format for compression based on the specific browser, network conditions, and screen resolution, ensuring each user receives an image sized appropriately for their device.
* **Modern formats:**
  While **`avif`** (AV1 Image File Format) is a newer format offering better compression than older formats, it is not universally supported across all browsers yet, and **`webp`** enjoys broader compatibility.
* **Best practices:**
  To guarantee the best web-optimized format, you can trust Smart Imaging to make the format selection rather than manually using the commands **`fmt=webp`** or **`fmt=avif`**.

By relying on Smart Imaging, you ensure that your images are delivered in the most efficient manner possible, tailored to each user's browsing environment. Because Smart Imaging matches each delivered image to the specific browser, network conditions, and screen resolution, it simplifies the delivery process and can improve image loading times and overall user experience.

For additional detail, see [Smart Imaging](/help/assets/dynamic-media/imaging-faq.md).

### Post delivery of assets to customers

**Business case:** *After publishing new content or overwriting existing content, how can it be ensured that the changes appear immediately on the CDN?*

To make published or overwritten Dynamic Media assets appear immediately on the website, **purge or invalidate the CDN (Content Delivery Network) cache**. The **CDN caches Dynamic Media assets** to deliver them quickly to customers, so when updates are made to these assets, the changes must take effect immediately on the website.

Purging or invalidating the CDN cache updates assets delivered by Dynamic Media quickly. This works because clearing the cached copy forces the CDN to retrieve and serve the newly published version on the next request, rather than continuing to serve the stale cached copy. As a result, this approach eliminates the need to wait for the cache to expire based on the **TTL (Time To Live)** value, which is typically set to **ten hours**.

You control how quickly updated assets reach customers through two mechanisms:

- **Purge or invalidate the CDN cache** — forces immediate delivery of newly published or overwritten assets.
- **Adjust the CDN TTL (Time to Live) settings** — depending on your specific use case, tune how long assets remain cached before expiring.

For detailed steps, see [Invalidate the CDN cache by way of Dynamic Media](/help/assets/dynamic-media/invalidate-cdn-cache-dynamic-media.md).
