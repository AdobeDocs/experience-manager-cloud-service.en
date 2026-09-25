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

**Dynamic Media on Adobe Experience Manager (AEM) is a comprehensive digital asset delivery solution** that optimizes assets, handles personalization, and delivers consistent, performant, and brand-aligned experiences across every channel and device. Organizations today face an explosion of channels and touchpoints for engaging users — the customer journey now spans physical stores, web, mobile, social media, email, and commerce — and Dynamic Media addresses this complexity from a single source of truth.

## Key tenets of Dynamic Media

The following core capabilities define how Dynamic Media operates and why it scales across enterprise workflows:

* **Single file approach:** With Dynamic Media, you store one primary source file, and all size variants, renditions, and visual transformations are generated and optimized dynamically at the time of delivery. This approach **reduces storage costs, eliminates duplicated derivative assets, and removes workflow complexity** associated with maintaining multiple pre-rendered versions.
* **Global delivery:** **Smart Imaging**, applied during content delivery, reduces image file size and overall page weight without compromising visual quality. It is optimized for network bandwidth conditions and device pixel ratios, ensuring faster load times and better Core Web Vitals across geographies and devices.
* **Artificial Intelligence (AI)-powered:** **Smart Crop**, an AI-powered feature, automates subject-aware cropping for images and video. This eliminates manual cropping effort and scales efficiently for enterprise catalogs where thousands of assets must be adapted to multiple aspect ratios.
* **Video support:** Upload primary source videos into Dynamic Media and stream them adaptively across multiple languages, with support for descriptive audio tracks. Adaptive streaming ensures playback quality automatically matches each viewer's bandwidth and device capabilities.
* **Experience viewer library:** Customize and brand experience viewers for images and videos so they integrate seamlessly into your digital storefronts, product pages, and marketing experiences. These viewers support interactive features such as zoom, pan, hotspots, and 360-degree spin sets.
* **Emerging format support:** Dynamic Media enables the delivery of **3D and panoramic experiences**, extending asset workflows beyond flat images and video to support immersive commerce and product visualization use cases.

## Applying these best practices

As you explore the [Dynamic Media Journey](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dm-journey/dm-journey-part1), reviewing the consolidated list of best practices below helps you fully use its capabilities. Adapt these Dynamic Media best practices to your specific context and project requirements to optimize experiences across channels and devices.

<!-- In Dynamic Media on AEM, there are sets of methods, techniques, and guidelines that can help you maximize the potential of your rich media content. These best practices can lead to optimal results and increase efficiency in your use of Dynamic Media. They represent the most efficient and effective courses of action in a particular situation. They also unlock high value for your audience and deliver high-quality, engaging content. -->

>[!IMPORTANT]
>
>The Dynamic Media best practices in this article can evolve over time as new technologies in Dynamic Media emerge. The information below is current for the latest version of Dynamic Media.

## Ingest assets into Dynamic Media

**Business case:** *Efficiently manage large volumes of assets and ensure that only relevant, approved content is delivered to end users.*

**Dynamic Media** provides two complementary controls — **Selective Sync** and **Selective Publish** — that together let digital asset management (DAM) teams govern exactly which assets enter the delivery pipeline and which ones ultimately reach customer-facing channels. These two capabilities streamline the management of large asset libraries and ensure that only appropriate, authorized content reaches end audiences.

* **Selective Sync:**
Selective Sync is a proactive, ingest-side control that lets administrators choose which assets to sync with Dynamic Media. For example, teams can sync only those folders containing assets that have received final approval — such as folders holding finalized seasonal campaign imagery, region-specific product photography, or legally cleared marketing creative. This workflow ensures that only vetted content enters the Dynamic Media environment, and it helps teams maintain control over which assets they are preparing for delivery to customers.

* **Selective Publish:**
After syncing assets, Selective Publish provides delivery-side control over which assets are visible to end customers. Unlike Selective Sync, which governs what enters Dynamic Media, Selective Publish governs what exits it to public channels. This capability lets teams determine which approved assets are delivered through their channels, ensuring that audiences see only the most relevant, on-brand content at the right moment in a campaign lifecycle.

### Key benefits of Selective Sync and Selective Publish

Together, these two best practices deliver:

* **Tighter governance** over asset visibility across the entire ingest-to-delivery pipeline.
* **Reduced risk** of publishing unapproved, outdated, or off-brand content to live channels.
* **Improved productivity** for DAM, marketing, and merchandising teams by narrowing the working set of assets under active management.
* **Greater brand consistency**, because only reviewed and approved creative reaches customer touchpoints.

As a result, marketing and digital operations teams gain finer-grained governance and productivity over their rich-media content, while reducing the operational overhead of managing assets that are not yet ready for public consumption.

For step-by-step configuration guidance, see [Configure Selective Publish at the folder level in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md).

## Dynamic Media Viewers

Dynamic Media Viewer best practices optimize the performance, functionality, and user experience of Dynamic Media assets on Adobe Experience Manager (AEM). These guidelines cover **asset synchronization**, **publishing**, **smart cropping**, **muted autoplay for video**, **correct JavaScript inclusion**, and **viewer-specific embedding** — the core areas that determine whether a Dynamic Media viewer renders reliably in production.

Following these practices delivers seamless integration, efficient asset management, and consistent viewer interactions across browsers and devices. Synchronizing assets, applying smart cropping, and adhering to JavaScript file inclusion rules each protect the integrity and reliability of media delivery in the runtime environment.

* **Synchronize Viewer Assets:**
Synchronize all viewer assets with Dynamic Media before using the player. Unsynchronized assets are a common root cause of missing icons, broken styling, or non-functional presets at runtime.

  * Access the sample manager page at **`/libs/dam/gui/content/s7dam/samplemanager/samplemanager`**. This page resynchronizes a viewer's assets, including standard icons, CSS files, and presets.
  * If you encounter viewer issues, go to the [Troubleshoot Dynamic Media Viewers](/help/assets/dynamic-media/troubleshoot-dm.md#viewers) article.

* **Publish Assets:**
Publish assets before viewing them in delivery viewers. This ensures the delivery tier can serve the asset when the viewer requests it; unpublished assets are not resolvable by the public viewer runtime.

* **Autoplay Videos Muted:**
For autoplay functionality in videos, use muted video settings. Modern browsers block autoplay of videos that have audio enabled, so muted playback is required for the video to start automatically without user interaction.

* **Smart Cropping:**
Use the **Image v3 component** for smart cropping to enhance image asset presentation and produce focal-point-aware crops across responsive breakpoints.

* **JavaScript File Inclusion:**
Include only the primary viewer JavaScript file on your page. Do not reference additional JavaScript files that the viewer's runtime logic downloads on its own. Specifically, do not directly link to the HTML5 Software Development Kit (SDK) **`Utils.js`** library from the **`/s7viewers`** context path — a pattern known as the **consolidated SDK include**, in which the page hard-codes a direct reference to `Utils.js` rather than letting the viewer load it. The viewer's logic manages the location of `Utils.js` and other runtime viewer libraries, and those locations can change between releases. Adobe does not retain older versions of secondary viewer includes on the server, so directly referencing them breaks viewer functionality in future updates.

* **Embedding Guidelines:**
Use the documentation for embedding guidelines specific to each viewer, because embed code, parameters, and initialization patterns differ by viewer type.
Want to learn more? Go to [Viewers for AEM Assets](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/library/viewers-aem-assets-dmc/c-html5-s7-aem-asset-viewers).

* **SDK Tutorial and Examples:**
Review the [Viewer SDK Tutorial](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/library/c-tutorial) and [HTML5 SDK application examples](https://s7d9.scene7.com/s7sdk/2024.5/docs/jsdoc/index.html) for a thorough understanding of SDK component APIs.

## Prepare assets for delivery



### Organize your assets

**Business case:** *To streamline workflows, efficiently organize assets.*

For efficient asset organization that streamlines workflows, use one or more of the following best practices:

* **Organize assets in folders:**
Effective asset organization starts with categorizing assets into folders, much like file organization on a computer. Proper naming, thoughtful subfolder structuring, and disciplined file management within these folders are crucial for efficient asset processing, because a predictable hierarchy makes assets easier to locate, batch-process, and govern. Implementing systematic **naming conventions** and **metadata practices** maximizes the utility of your digital asset repository as it scales.
Want to learn more? Go to [Organize assets in folders](/help/assets/organize-assets.md#organize-using-folders).
* **Organize assets using tags:**
Tagging assets enhances searchability, collection creation, and search ranking, because well-tagged assets are easier to retrieve, group, and surface in relevant results. **Adobe AI** assigns relevant tags&ndash;including custom ones&ndash;to assets, simplifying asset management with automatic, descriptive tagging that reduces manual effort and keeps metadata consistent across large libraries.
Want to learn more? Go to [Organize assets using tags](/help/assets/organize-assets.md#use-tags-to-organize-assets).
* **Organize assets as collections:**
**Dynamic Media** along with **Experience Manager Assets** enables the efficient creation, editing, and sharing of asset collections among users. Establish multiple collection types, including **static lists** and **dynamic, search-based compilations**. Share these collections across multiple locations and teams with customizable access and editing permissions, which supports controlled collaboration while preserving asset governance.
Want to learn more? Go to [Organize assets as collections](/help/assets/manage-collections.md).
* **Organize assets using profiles:**
A **processing profile** is an automated rule set that handles assets in designated folders, streamlining organization by applying consistent processing—such as renditions, metadata assignments, and naming—whenever assets are added. Because profiles rely on predictable inputs, standardizing metadata, file names, and folder structures ensures consistent and precise application of these profiles as your digital asset collection expands.
Want to learn more? Go to [Organize assets using profiles](/help/assets/organize-assets.md#organize-to-use-profiles).

### Optimize the quality of images

**Business case:** *Obtain good quality images from Dynamic Media.*

Improving image quality in Adobe Experience Manager Dynamic Media depends on several interrelated factors, and the process is often time-intensive. Applying established best practices, however, consistently improves visual output. Key areas to focus on include:

- **Optimal image sizing** — matching pixel dimensions to display context to avoid unnecessary scaling.
- **Image sharpening** — applying the appropriate sharpening technique for the intended output size and medium.
- **Best image formats** — selecting the file format that balances quality, file size, and browser or device compatibility.

For deeper guidance on each of these areas, see [Best practices for optimizing the quality of your images](/help/assets/dynamic-media/best-practices-for-optimizing-the-quality-of-your-images.md).

Because perception of image quality varies from person to person, a systematic, test-driven approach to experimentation is essential for arriving at repeatable, high-quality results. To support this process, **Adobe Experience Manager provides more than 100 Dynamic Media commands for image enhancement** — a breadth of controls that lets teams fine-tune sharpening, color, compression, cropping, resizing, and other rendering behaviors on a per-asset basis.

For a concise overview of these capabilities, watch [Dynamic Media Snapshot](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-snapshot) (3 minutes, 17 seconds).

To evaluate how each command affects the final rendered image, users can upload an image to Dynamic Media, open the tool's interface at the specified URL, and apply the commands they want to test. This hands-on comparison makes it easier to identify the exact parameter combinations that produce the desired visual outcome before publishing at scale.

To experiment directly, launch [Dynamic Media Snapshot](https://snapshot.scene7.com/).

### Standardize on styles applied to images

**Business case:** *Efficiently standardize the style and transformation applied to my image assets.*

Use **Image Presets** regularly in Dynamic Media to consistently and dynamically adjust image sizes, formats, and properties across every channel where your assets appear. An **Image Preset** is a named, reusable set of commands for sizing and formatting — once defined, the preset can be applied on demand so that the same source asset is delivered in the exact rendition required for each surface, without producing and storing multiple derivative files.

In practice, Image Presets control attributes such as:

- **Dimensions** — width, height, and aspect ratio for the delivered rendition.
- **Format** — the output image format best suited to the target device or browser.
- **Image properties** — quality, sharpening, color, and other visual transformations applied at render time.

Because the preset is applied dynamically, the original master asset remains untouched and a single source can generate every required variant on the fly. This ensures visual consistency across storefronts, marketing surfaces, and campaigns while reducing manual production work.

For example, Image Presets automate product image sizing and formatting for both desktop and mobile experiences — the same product photo can be delivered as a large hero image on desktop and an appropriately sized, optimized rendition on mobile, all governed by the same named preset. As a result, teams enforce a uniform look and feel, shorten production cycles, and simplify updates: change the preset once, and every image that uses it inherits the new treatment.

Want to try it? Go to [Fundamentals of creating image presets to render assets](/help/assets/dynamic-media/dm-journey-part2.md#dm-journey-e)

### Adjust the focus and framing of images and videos

**Business case:** *Ensure that the main point of interest of my images or videos remains in focus across devices.*

#### How Smart Crop Works

**Smart Crop** is an automated cropping capability in **Dynamic Media** powered by **Adobe AI**, Adobe's artificial intelligence and machine learning framework. Smart Crop automatically identifies and preserves the primary subject — or point of interest — within an image or video, then re-frames the asset so that focal point stays centered and visible as the viewport changes.

Key capabilities include:

- **Automated subject detection:** Adobe AI analyzes each asset to locate the main visual subject, eliminating manual cropping decisions for every breakpoint.
- **Responsive framing:** The feature maintains the focal point across desktop computers, tablets, and mobile devices, so the viewer always sees the intended composition.
- **Applies to both images and video:** Smart Crop supports still imagery and video content, extending consistent framing behavior across media types.
- **Device-optimized delivery:** Each viewer receives an appropriately cropped rendition matched to their screen, which supports faster perception of the message and stronger visual engagement.

This matters because a single hero image or video often needs to appear across many aspect ratios — wide desktop banners, square social tiles, and tall mobile screens. Without intelligent cropping, the main subject can drift off-frame or be sliced awkwardly. Smart Crop prevents that by making the focal point the anchor of every rendition.

#### Best Practice: Create an Image Profile with Smart Crop

Create an **Image Profile** configured with Smart Crop. In the profile:

1. Define the screen sizes and aspect ratios you need to support.
2. Let Adobe AI handle detection and re-framing for each defined size.
3. Publish once and deliver responsively — the profile ensures every image and video is optimized for the viewer's device without additional manual work.

This approach centralizes cropping logic, reduces production overhead, and keeps brand presentation consistent across every channel.

#### Learn More

Want to learn more? Watch [Using Smart Crop with AEM Assets Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use) (6 minutes, 35 seconds) and [Using Dynamic Media Smart Crop for Video](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/video/dynamic-media-smart-crop-video) (6 minutes, 22 seconds) — both walkthroughs demonstrate Smart Crop inside Adobe Experience Manager (AEM) Assets.

### Improve SEO rankings

**Business case:** *Configure Dynamic Media to get improved SEO rankings.*

Apply the following recommendations consistently so that your images contribute effectively to your overall SEO strategy.

* **Meaningful image file names:**
Use **descriptive, keyword-rich file names** that reflect the image content. For example,

  * use `myCompany-Silver-Wrist-Watch`
  * avoid using `myCompany_Silver_Wrist_Watch` or `myCompanySilverWristWatch`

  Descriptive file names help search engines interpret the image context, which directly improves SEO performance. Google prefers **hyphens** over underscores or spaces in a file name, because hyphens are parsed as word separators while underscores are not. Also, avoid concatenating words in a file name, as concatenated strings obscure the individual keywords that crawlers rely on.
* **Custom domain:** 
Implement a **custom domain** that includes your company or brand name to reinforce brand recognition, domain authority, and user trust. For example,

  * use `http://images.mycompany.com/is/image/companyname/`
  * avoid using `https://s7d1.scene7.com/is/image/folder/AdobeStock_28563982`

  A branded domain surfaces your company name in the URL itself, giving search engines and users an immediate signal of ownership and relevance.
* **SEO-friendly folder structure:**
Organize your images in a folder hierarchy that includes your company or brand name for better indexing, such as `http://images.mycompany.com/is/image/companyname/`. A clean, semantic path helps crawlers understand site architecture and associate assets with the correct brand entity.
* **Dynamic Media rule sets:**
Use **rule sets** to conditionally transform URLs based on factors such as device type, image format, or request context, enhancing both SEO and user experience.
Want to learn more? Go to [Use rule sets to transform URLs](/help/assets/dynamic-media/using-rulesets-to-transform-urls.md).
* **Smart Imaging and Smart Crop:**
Use **Smart Imaging** and **Smart Crop** features in Dynamic Media to serve optimized, responsive images tailored to each device and viewport. These features reduce payload size and accelerate page load times, and because page speed is a confirmed Google ranking signal tied to Core Web Vitals, faster delivery strengthens SEO rankings as a direct downstream effect.
Want to learn more? Go to [Smart Imaging](/help/assets/dynamic-media/imaging-faq.md), or watch [Using Smart Crop with AEM Assets Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use) (6 minutes, 35 seconds).

These best practices align directly with **Google's image SEO best practices**, which emphasize providing context and clarity to search engines through proper naming conventions, structured data, and optimized image delivery. Following Google's own guidance is the most reliable path to sustained image visibility in search results.

Want to learn more? Go to [URL structure best practices for Google](https://developers.google.com/search/docs/crawling-indexing/url-structure) and [Google image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)

### Dynamically enhance images and create visual effects using commands

**Business case:** *Apply rich visual effects to images.*

Dynamic Media provides a suite of Uniform Resource Locator (URL) commands that enhance images and generate visual effects on demand, eliminating the need to store multiple static asset variants. The following sections explain core image-transformation processes and provide working URL examples for each.

#### Effects inside the source image

| Task | What to do |
| --- | --- |
| **Upload and publish your original image** | <ul><li> Upload the original image to Dynamic Media.</li><li> Confirm that the asset is published and reachable through a public URL.</li><li> In this example, a stock image of a watch on a white background (designated as "Image X") is uploaded to Dynamic Media.<br>[https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer](https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer)</li></ul> |
| **Create a mask** | <ul><li> Build a **mask** that defines the subject (the area where the effect is applied) and the background (the area to be altered).<br>[https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer-maskps](https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer-maskps)</li><li> Masks are typically **grayscale images**, where **white represents the subject** and **black represents the background**. Create masks using tools such as Adobe Photoshop.<br>For further guidance, see [Creating and editing a quick mask in Photoshop](https://helpx.adobe.com/in/photoshop/using/create-temporary-quick-mask.html).</li><li> For "Image X," construct a mask that precisely outlines the subject targeted for enhancement — for example, a person or a product object.</li></ul> |
| **Apply Dynamic Media URL commands for effects** |  Once the mask is prepared, apply URL commands to add effects such as an **outer glow** or a **background color change** to "Image X." Two examples follow:<ul><li> **Outer glow effect:**<br>To add an outer glow along the subject's boundary, structure the URL as follows:<br>[https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&effect=-1&pos=100,100&op_blur=75&op_grow=1&opac=25](https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&effect=-1&pos=100,100&op_blur=75&op_grow=1&opac=25)<br>In this URL, the `op_blur`, `op_grow`, and `opac` parameters combine to produce the outer glow — controlling blur radius, growth of the glow beyond the subject edge, and opacity respectively.</li><li> **Background color change:**<br>To swap the background color, supply a different color value in the URL:<br>[https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&maskUse=invert&color=255,255,0](https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&maskUse=invert&color=255,255,0)<br> In this example, `color=255,255,0` sets the background to yellow using standard **RGB (Red, Green, Blue)** values. Substitute any RGB triplet to match brand palettes or seasonal campaigns.</li></ul> |

#### Add an image border

Dynamic Media manipulates images directly through URL parameters, making it a powerful tool for producing dynamic digital experiences without regenerating source assets. The following examples begin with the base image URL: [https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel).

| Task | What to do |
| --- | --- |
| **White border** | To add a white border, use the following URL:<br>[https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10)<br>In this URL, the `extend=10,10,10,10` parameter adds a **10-pixel border on all four sides** (top, right, bottom, left). |
| **Blur along the white border** | To add a blur effect along the white border, structure the URL as follows:<br>[https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&op_blur=60&color=0,0,0](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&op_blur=60&color=0,0,0)<br>In this URL, the `effect=-1` parameter enables the effect layer, and `op_blur=60` sets the blur intensity — higher values produce a softer, more diffuse edge. |
| **Drop shadow effect along the outer boundary** | To add a **drop shadow** along the outer boundary, use this URL:<br>[https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&$shadow$&color=0,0,0](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&$shadow$&color=0,0,0)<br>The `$shadow$` parameter invokes the shadow effect, and `color=0,0,0` sets the shadow color to black for maximum contrast against lighter backgrounds. |

Combine and modify these URL parameters to produce the required visual effects across product imagery, marketing banners, and campaign creative.

#### Create image overlays

To superimpose a logo or icon on an existing image, Dynamic Media provides a direct method using URL commands. The steps are as follows.

| Step | What to do |
| --- | --- |
| **Upload and publish the base image** | First, upload and publish the base image that will receive the overlay. Any published asset can serve as the base.<br>For example, here is a base image:<br>[https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa](https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa). |
| **Upload and publish the logo or icon image** | Next, upload and publish the image that will sit on top of the base. This overlay asset should be a **transparent PNG (Portable Network Graphics)** file containing the logo or icon, so that only the graphic pixels appear and the surrounding area shows the underlying image.<br>The following is a transparent PNG of a star object with transparency effects, used here as the overlay:<br>[https://s7g2.scene7.com/is/image/genaibeta/decorate-star](https://s7g2.scene7.com/is/image/genaibeta/decorate-star) |
| **Apply the Dynamic Media URL** | Now, construct a Dynamic Media URL that composites the base image with the logo or icon image. URL commands handle the layering.<br>The URL structure is as follows:<br>[https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa?layer=1&src=decorate-star&scale=1.25&posN=0.33,-.25&fmt=png](https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa?layer=1&src=decorate-star&scale=1.25&posN=0.33,-.25&fmt=png)<br>where the asset<ul><li> `hotspotRetailBaseImage` is the base image.</li><li> `starxp` is the logo/icon image.</li><li> `layer=1` places the logo or icon as the first layer above the base image.</li><li> `scale=1.25` enlarges the logo/icon by 25 percent relative to its native size.</li><li> `posN=0.33,-.25` sets the normalized position of the logo/icon relative to the base image dimensions.</li><li> `fmt=png` outputs the composite in PNG format, preserving transparency.</li></ul> |

For additional detail, see [src](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/r-src) for more on the `src` command and other Dynamic Media URL commands.


#### Overlaying promotional text

The following steps overlay a promotional text message on an image using Dynamic Media's text operators (which follow rich-text conventions similar to those handled by HTML (HyperText Markup Language) and CSS (Cascading Style Sheets) in web rendering).

| Step | What to do |
| --- | --- |
| **Upload and publish the base image** | First, upload and publish the base image that will carry the text. Any image is acceptable. For example, here is a sample base image:<br>[https://s7g2.scene7.com/is/image/genaibeta/leather-sofa](https://s7g2.scene7.com/is/image/genaibeta/leather-sofa)<br> |
| **Apply Dynamic Media text operators** | Using Dynamic Media, apply text operators to render dynamic text directly onto the image at request time — enabling personalized promotions, localized copy, or A/B-tested headlines without producing new source files. The following sample URL demonstrates this capability:<br>[https://s7g10.scene7.com/is/image/genaibeta/leather-sofa?layer=1&posN=-0.3,-0.455&text=%7b\rtf1\ansi%7b\fonttbl%7b\f0+Arial;%7d%7d%7b\colortbl+\red255\green255\blue255;%7d\copyfit1000\vertalc\qc%7b\cf0\fs42+New+Collection%7d%7d&size=370,70&textAttr=130&bgcolor=FF3333&wid=600&hei=600](https://s7g10.scene7.com/is/image/genaibeta/leather-sofa?layer=1&posN=-0.3,-0.455&text=%7b\rtf1\ansi%7b\fonttbl%7b\f0+Arial;%7d%7d%7b\colortbl+\red255\green255\blue255;%7d\copyfit1000\vertalc\qc%7b\cf0\fs42+New+Collection%7d%7d&size=370,70&textAttr=130&bgcolor=FF3333&wid=600&hei=600) |

#### Resizing and cropping for various use cases

##### Image resizing basics

Image resizing alters an image's **dimensions**, **resolution**, and **file size**. Key considerations include:

* **Pixel composition:**
Digital images consist of tiny dots called **pixels**. Each image contains a fixed pixel count at creation. Resizing adds or subtracts pixels to change the image's dimensions, resolution, and file size.
* **Aspect ratio:**
Preserving the **aspect ratio** (the ratio between width and height) prevents distortion. Whether upscaling (enlarging) or downscaling (shrinking), maintaining the aspect ratio ensures visual consistency across placements.
* **Quality considerations:**
Resizing directly affects image quality. Avoid drastic upscaling because it produces visible pixelation. Instead, reproduce the source at a larger native size and resolution. For smaller renditions, use appropriate tooling to retain sharpness and detail.

##### Cropping versus resizing

Cropping and resizing are complementary Dynamic Media techniques that transform images for varied use cases — including thumbnails, product display images, and hero banners.

* **Cropping:**
Removes part of an image to change its composition and framing. Cropping does not scale the remaining pixels; it focuses attention on a selected region.
* **Resizing:**
Changes the entire image's dimensions, resolution, and file size while preserving the aspect ratio.

The following use case applies both techniques to a living room image:

* **Original living room image:**
    [https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa](https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa)
* **Thumbnail (200 px x 200 px):**
        A smaller rendition suited to quick loading or compact display in grids and catalogs.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&fit=crop)
* **Thumbnail with crop (200 px x 200 px):**
        Cropped to focus on the sofa area.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&cropN=.24,.24,.6,.72&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&cropN=.24,.24,.6,.72&fit=crop)
* **Product display image (800 px x 600 px):**
        Cropped and resized to showcase the sofa on a product detail page.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=800&hei=600&cropN=.24,.24,.6,.72&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=800&hei=600&cropN=.24,.24,.6,.72&fit=crop)
* **Banner (1720 px x 820 px):**
        Derived from the original image, emphasizing the wider room composition suited to hero placements.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=1720&hei=820&cropN=0,.1,1,1&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=1720&hei=820&cropN=0,.1,1,1&fit=crop)

These variations support common presentation contexts including e-commerce listings, hero banners, and thumbnail grids.
For a full list of commands available within a URL, see the [Command reference](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/c-command-reference).

### Deliver GIF images

**Business case:** *Stream GIFs using Dynamic Media*

Dynamic Media supports both uploading and delivering GIF assets, including animated GIFs. The key rule: **to render an animated GIF, replace `is/image` with `is/content` in the URL**. The `is/image` path routes the asset through the image-processing server (which flattens the file to a single frame), while the `is/content` path streams the original asset binary, preserving all animation frames.

For example, if you uploaded `abc.gif`, use the following URL patterns:

#### Static GIF delivery (single-frame render)

This URL path renders a **static view** of the GIF through the image server, allowing standard image modifiers:

```
https://your.domain.com/is/image/yourfolder/abc
```

#### Animated GIF delivery (full animation)

This URL path renders the **animation view** of the GIF by serving the raw content directly:

```
https://your.domain.com/is/content/yourfolder/abc
```

>[!NOTE]
>
>When using `is/content` in the URL path, image transformation commands are not applied to the asset. This is because the `is/content` handler delivers the original, unprocessed binary file rather than routing it through the image server pipeline — which is precisely what preserves the animation, but also means resizing, cropping, format conversion, and other image modifiers will be ignored on this path.

**Choosing the right path:**

- Use `is/image` when you need image transformations (resize, crop, format conversion) and a static frame is acceptable.
- Use `is/content` when preserving the animated playback of the GIF is required, accepting that transformation parameters will not take effect.

### Publish a video for my website

**Business case:** *Quickly publish a video for a marketing site.*

* **Select a video profile:**
  First, in Dynamic Media, select a suitable video profile. Opt for the *Adaptive Video Encoding* profile available in Adobe Experience Manager (AEM) Assets under Video Profiles, which generates multiple renditions of the source at different bitrates and resolutions. These pre-defined encoding settings ensure that the video is optimized for playback across various devices and bandwidth conditions. Alternatively, create a custom Adaptive Video profile tailored to specific delivery requirements.
* **Assign the profile:**
  Assign the chosen video profile to the folders where the video uploads. This step ensures the correct encoding settings are applied automatically at upload, eliminating the need to configure encoding on a per-asset basis.
* **Upload the original video:**
  Upload the original video file. Use a high-resolution master file with strong image quality. Because adaptive encoding derives all output renditions from the source, the fidelity of the original directly determines the maximum quality of every published rendition.
* **Preview and publish:**
  Preview the video to confirm that playback, thumbnails, and encoding output render correctly. Once satisfied, publish it. Publishing activates the video on Adobe's delivery network and makes it accessible to site visitors.
* **Link or embed:**
  After publishing, choose between two delivery options.

    * **Link directly:**
    Use the provided URL to link directly to the video. Hyperlink it appropriately on the marketing site.
    * **Embed the video:**
    Copy the embedded code provided and paste it into the HTML of the web page where the video should appear. Embedding causes the video to play inline within the page, so viewers are not redirected to an external player.

Want to learn more? Go to [Video](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/video).

### Configure videos for optimal quality and engagement

**Business case:** *Set up videos for the best quality and engagement.*

To deliver the highest video quality and maximize viewer engagement, combine the following best-practice strategies within Dynamic Media:

* **Use the built-in HTML5 Video Viewer:**
        The **Dynamic Media HTML5 Video Viewer Presets** function as robust, production-ready video players. These presets eliminate common issues tied to HTML5 video playback across desktop and mobile devices.
        Specifically, the presets resolve challenges such as **adaptive bitrate streaming delivery** and limited desktop browser reach, ensuring consistent playback experiences across a wide range of client environments.
        For detailed guidance, see [Best practice: Using the HTML 5 video viewer](/help/assets/dynamic-media/video.md#best-practice-using-the-html-video-viewer).

* **Use Dynamic Media Video Profiles:**
        **Dynamic Media Video Profiles** enable efficient video management, consistent output quality, and adaptive streaming across delivery channels. As a result, video assets remain uniform in encoding, resolution, and delivery behavior—reducing manual configuration overhead.
        For implementation details, see [Dynamic Media Video Profiles](/help/assets/dynamic-media/video-profiles.md).

* **Follow best practices for video encoding:**
        Apply **video encoding profiles** that preserve the original source video quality and avoid excessive downscaling during the encoding process. This ensures that final output retains visual fidelity, which is critical for viewer retention and brand presentation.
        For technical specifications, see [Best practices for encoding videos](/help/assets/dynamic-media/video.md#best-practices-for-encoding-videos).

* **Adopt adaptive streaming instead of progressive streaming:**
        **Adaptive streaming** dynamically adjusts video quality in real time based on the viewer's internet connection speed and device capabilities.
        It leverages industry-standard protocols such as **HLS (HTTP Live Streaming)** and **DASH (Dynamic Adaptive Streaming over HTTP)** to deliver optimal playback quality under variable network conditions.
        Unlike **progressive streaming**, which delivers video files linearly regardless of bandwidth fluctuations, adaptive streaming minimizes buffering, reduces playback interruptions, and provides a seamless viewing experience across devices. Consequently, adaptive streaming is the preferred method for modern, engagement-focused video delivery.

### Internationalizing videos for multilingual consumption

**Business case:** *Prepare videos for multilingual consumption across global markets.*

Internationalizing videos for multilingual consumption is essential for reaching a global audience. Dynamic Media delivers a built-in workflow that prepares, localizes, and distributes video for viewers worldwide, letting a single source file serve many regions without duplicating production effort.

* **Upload your videos:**
    * First, create a video encoding profile. You can either use the predefined **Adaptive Video Encoding** profile that ships with Dynamic Media or create your own custom profile tuned to your bitrate, resolution, and codec requirements.
    * Associate the video encoding profile with one or more folders where you upload your primary source videos. This ensures every asset dropped into those folders is processed consistently.
    * Upload your primary source videos to these folders. Dynamic Media encodes them automatically based on the assigned video processing profile, producing adaptive renditions for delivery.
    * Dynamic Media primarily supports **short-form videos (up to 30 minutes)** with a minimum resolution **greater than 25 × 25 pixels**. Video files **up to 15 GB each** can be uploaded.

* **Manage your videos:**
    * Organize, browse, and search video assets directly within Adobe Experience Manager (AEM).
    * Preview and publish video assets from a single interface.
    * View the source video alongside its encoded renditions and associated thumbnails to confirm output quality before release.
    * Edit video properties such as title, description, and tags to improve internal discoverability and downstream SEO metadata.

* **Localization:**
    * For each target geography or language, create audio tracks and subtitles so viewers in every market receive natively voiced dialogue and readable captions.
    * Add these audio and subtitle tracks to your videos from the AEM interface, keeping all localized variants attached to a single master asset.
    * When users play the videos, they select their preferred language for audio and subtitles at runtime, eliminating the need to host separate per-language video files.

* **Publishing:**
    * If you use AEM as your Web Content Management (WCM) system, you can add videos directly to your web pages through the native authoring experience.
    * If you use a third-party WCM system, you can link or embed videos on your web pages using URLs or embed codes generated by Dynamic Media.

For additional details on managing localized playback, see [About multiple caption and audio track support for videos in Dynamic Media](/help/assets/dynamic-media/video.md#about-msma).

## Deliver assets to customers



### Optimize image sizes and minimize page load times

**Business case:** *Optimize the size of images for any browser or screen and reduce page load time.*

Dynamic Media **Smart Imaging** is an image-delivery capability that improves performance by automatically optimizing each image's **format**, **size**, and **quality** based on the client browser's capabilities, network conditions, and screen resolution. Because the optimization happens at request time, every visitor receives an image tailored to their specific viewing environment.

Adobe recommends using Smart Imaging's automatic capabilities rather than manually forcing an image format such as `webp` or `avif`. The reasons are as follows:

* **Browser compatibility:**
  Smart Imaging guarantees that the delivered image format is compatible with the user's browser, because it detects browser support signals before selecting a format. This prevents broken images or fallback failures on browsers that do not yet support newer formats.
* **Optimal compression:**
  Smart Imaging selects the best format for compression based on the specific browser, network conditions, and screen resolution. As a result, file sizes shrink without visible quality loss, which reduces bandwidth consumption and speeds up rendering.
* **Modern formats:**
  While `avif` is a newer format that offers better compression than older formats, it is not yet universally supported across all browsers. Smart Imaging serves `avif` only where it is supported and falls back to a compatible format elsewhere, avoiding compatibility gaps.
* **Best practices:**
  To guarantee the best web-optimized format for every request, developers should let Smart Imaging make the format selection automatically rather than manually specifying commands such as `fmt=webp` or `fmt=avif`. This eliminates the need to maintain per-browser rendering logic and keeps delivery aligned with evolving browser support.

Because Smart Imaging adapts delivery to each request in real time, images are served in the most efficient manner possible, tailored to each user's browsing environment. This approach simplifies the delivery pipeline and improves image loading times and overall user experience.

For additional details, refer to [Smart Imaging](/help/assets/dynamic-media/imaging-faq.md).

### Post delivery of assets to customers

**Business case:** *After publishing new content or overwriting existing content, how can it be ensured that the changes appear immediately on the CDN?*

**Purging or invalidating the CDN cache forces Dynamic Media assets to refresh immediately across the delivery network**, rather than waiting for the default **TTL (Time To Live)** — typically set to **ten hours** — to expire naturally.

The **CDN (Content Delivery Network)** caches Dynamic Media assets at geographically distributed edge nodes to deliver them quickly to customers. When updates are published to these assets, the cached copies at those edge nodes would otherwise continue serving the previous version until the TTL expires. As a result, without explicit invalidation, customers may see stale content for hours after a change goes live.

**Cache invalidation solves this in two ways:**

- **Immediate propagation:** Invalidating (or purging) the cache signals the CDN to discard the stored copy, so the next request pulls the updated asset directly from the origin. This ensures changes appear on the website right away.
- **No dependency on TTL expiry:** Teams do not need to wait out the default **ten-hour** window, which is critical for time-sensitive corrections, brand updates, or urgent content replacements.

Depending on the specific use case, the **CDN TTL** settings can also be adjusted — for example, shortening the TTL for frequently updated assets or extending it for stable, long-lived content to balance freshness against origin load.

For detailed procedures, see [Invalidate the CDN cache by way of Dynamic Media](/help/assets/dynamic-media/invalidate-cdn-cache-dynamic-media.md).