---
title: Dynamic Media Journey, Part I
description: The Dynamic Media Journey covers the basics of Dynamic Media, how it works, what it can do for you, and what value it brings to your work and your customers.
contentOwner: Rick Brough
products: Experience Manager as a Cloud Service
topic-tags: introduction,administering
content-type: reference
feature: Image Profiles,Best Practices
role: User, Admin
mini-toc-levels: 4
hidefromtoc: no
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: f3472006-d5ae-4f70-af3e-44e73aee85cc
---
# Dynamic Media Journey: The Basics, Part I {#dm-journey-part1}

{{see-also-dm}}

Welcome to the Dynamic Media Journey.

**Dynamic Media** is a system for storing, rendering, and delivering interactive rich media — including images and video — from a single high-resolution master asset. This journey covers the basics of Dynamic Media, how it works, what it can do for you, and what value it brings to your work and your customers. Because Dynamic Media renders responsive, on-demand variations of an asset rather than requiring you to produce and store each size manually, it enables interactive, high-quality rich media experiences to be delivered consistently and at scale.

**_Prerequisites_**

* Basic understanding of image and video formats
* Basic understanding of HTML and CSS
* Basic understanding of design tools such as Adobe Illustrator, Adobe Photoshop, Adobe XD
* Access to Dynamic Media on Experience Manager is helpful, but not required

**_What you can expect to learn_**

_Part I_

* What is Dynamic Media and how can it help you?
* Use cases for Dynamic Media, including interactive product imagery, zoom and pan, and responsive video delivery
* How an asset flows through the Dynamic Media system — from upload and ingestion to rendering and delivery

_Part II_

* Anatomy of a Dynamic Media URL and how Dynamic Media delivers content
* Fundamentals of creating image presets to render assets
* Image sets, spin sets, and mixed media sets

**_Audience_**
The audience that best fits readers of this journey are the following who are new to Dynamic Media on Experience Manager:

* Administrator
* Business Analyst
* Content Architect
* Content Author
* Designer
* Developer
* Marketing
* Product Manager/Owner

>[!TIP]
>
>For best results, Adobe recommends that you read and view this Dynamic Media Journey on a desktop computer.

## What is Dynamic Media and how can it help you? {#dm-journey-a}

**Dynamic Media delivers rich visual merchandising and marketing assets on demand**, generating multiple channel-ready variations from a single set of source files. It also creates and serves interactive viewing experiences directly to shoppers and site visitors.

### Key capabilities

Dynamic Media produces and delivers interactive experiences that increase engagement and reduce the need to store separate files for every use case:

- **Zoom** – close, high-resolution inspection of product detail
- **360-degree spin** – interactive rotation for a complete view of an item
- **Video** – streaming playback optimized for each viewing context

Assets are dynamically scaled for consumption across **web, mobile, and social** channels, ensuring each viewer receives an appropriately sized rendition without manual resizing or duplicate uploads.

### How Dynamic Media works

Using a set of primary source assets – such as **images**, **video**, and **3D** – Dynamic Media generates and delivers multiple variations of this rich content in real time. A single source asset therefore produces every device- and channel-specific rendition automatically, which eliminates repetitive production work and keeps every variant consistent with the original.

Delivery occurs through a **global, scalable, performance-optimized CDN (Content Delivery Network)**. Because a CDN caches and serves content from locations close to each user, this architecture supports fast load times and consistent visual quality regardless of where the audience is located.

Dynamic Media incorporates the workflows of the **Adobe Experience Manager Assets** digital asset management solution to simplify and streamline the digital campaign management process. This integration connects asset creation, management, and delivery in one system, so teams can move approved assets from production to publication without switching tools or rebuilding content for each channel.

### One file with endless possibilities

**Adobe Dynamic Media is built on a single principle: one primary asset file, endless possibilities.** From a single source file, Dynamic Media delivers unlimited on-demand renditions of an image or video, eliminating the need to manually produce and store separate copies for every device, page, and experience.

#### The traditional problem: version sprawl

To understand why this matters, consider the conventional workflow for a single asset such as an image or a video. You create one primary asset. You then manually create versions of that same asset for every experience, every device, every web page, and every property where it is used. Over time, that single asset can grow to **20, 30, or more versions**, none of which carry version history.

Now multiply that effort across your entire library of images and videos. Because each new experience demands another hand-made copy, the number of asset versions quickly becomes overwhelming to maintain and update. This proliferation directly drives up storage costs and increases the risk of inconsistent, outdated assets appearing across channels.

#### How Dynamic Media works differently

Dynamic Media is fundamentally different from traditional systems because it delivers media _dynamically_ from **single primary assets** through **URL calls**. Each Dynamic Media URL path you request includes instructions that tell the Adobe publish server how to render the asset at the moment of delivery to a customer's screen. Because the transformation happens at request time rather than in advance, one primary asset can be delivered instantly in unlimited renditions.

From that same single primary asset, Dynamic Media can adjust:

- **Size** — dimensions tailored to the target layout or device
- **Format** — the appropriate file type for the delivery context
- **Resolution** — sharpness matched to the screen
- **Weight** — file size optimized for available bandwidth
- **Color** — color adjustments as needed
- **Crop** — framing for different placements and aspect ratios
- **Effects** — interactive treatments such as a zoom view

<!-- As part of building and publishing assets with Dynamic Media, you visually configure the effects that you want to apply to assets. In so doing, you are literally building the URL that correctly tells the publish server how to deliver your primary asset to the screen.  -->

![Adobe Dynamic Media delivers the same primary image to different mediums in different sizes and formats](/help/assets/dynamic-media/assets/dm-oneasset-multioutput.png)

_Adobe Dynamic Media ensures consistent, quality experiences are delivered to any screen, regardless of size or bandwidth._

This on-demand delivery method ensures consistent, quality experiences reach any screen, regardless of size or bandwidth. Full-size videos are optimized for all screen types and adaptively streamed, so playback adjusts to the viewer's connection and device to preserve a consistent, quality user experience.

#### Why this matters

The "one primary asset file, endless possibilities" model streamlines asset management, reduces storage overhead, and guarantees brand consistency across every channel. By managing a single source of truth and generating renditions dynamically, teams update once and deliver everywhere—removing the manual, error-prone work of maintaining dozens of static versions per asset.

### The Content Delivery Network

<!-- USE AN IMAGE HERE? ![Content delivery network](/help/assets/assets-dm/cdn.png) -->

When an administrator is ready to publish an image or video asset, that asset is supported by Dynamic Media's backbone: a powerful, top-tier delivery network that serves hundreds of clients around the world every day. Assets are distributed across the **Content Delivery Network (CDN)**, hosted by **Akamai**. The CDN is a distributed network of servers that cooperate transparently to deliver content — especially large, rich media content such as high-resolution images and streaming video — to end users worldwide.

#### How the CDN Works

Within the CDN system, web content is stored in web caches positioned across the Internet, then delivered from the nearest cache to end users for faster performance. This model relies on edge caching, a widely used approach in which copies of content are held on servers close to the audiences that request them.

- **First request:** The first time someone downloads a web page, the assets they see are delivered to a CDN cache and stored on that server.
- **Subsequent requests:** The next time someone in the same geographic area accesses the webpage, the identical cached content is delivered far more quickly.

Because the cached content is located physically closer to the user, it reaches them faster. A CDN therefore accelerates web page displays while simultaneously reducing bandwidth demands on the central server, since content is served from the cache network rather than from a single central server in every instance. This optimized flow directly improves the user experience — faster-loading pages reduce abandonment and friction — which in turn drives increased sales and conversions.

#### CDN Performance at Scale

The scale of this delivery network underscores its enterprise-grade reliability:

- The CDN historically delivers **3.5 petabytes of traffic** to customers every month.
- The system can deliver **52 billion assets** in a single day.
- That volume equates to **864,000 images and videos** successfully delivered to customers _every second_.

These figures demonstrate the throughput required to serve rich media reliably to a global audience without straining any single origin server.

### Smart Imaging

Dynamic Media already optimizes assets and ensures that each asset loads quickly on mobile and desktop systems by way of the **content delivery network (CDN)**. To make that happen, **image presets** are used in Dynamic Media to define the quality of your image. They also define the type of image you are sending, its sharpness, and other characteristics for various parts of your experiences or pages.

Beyond image presets, **Smart Imaging** delivers additional value. With Smart Imaging enabled, you can expect a **22% to 47% performance improvement**, depending on your existing image preset settings and specific end-user characteristics — all while keeping image quality as if it were never touched.

#### How Smart Imaging Works

**Smart Imaging automatically optimizes an image's format and file size based on a customer's browser capability and network speed.** It works with your existing image presets (image presets are discussed in Part II of this journey) and applies intelligence at the point of delivery.

This intelligence further reduces image file size based on browser capability and network connection speed. Because modern browsers support more efficient image formats than older ones, Smart Imaging selects the most optimal format each browser can render, then compresses accordingly. This happens dynamically at delivery, so no manual re-processing of your presets is required.

#### Business Impact of Smart Imaging

Because image assets make up most of a page's load time, faster image delivery reduces overall page load time. As a result, this performance improvement directly influences key business indicators, including:

* **Higher conversion** — faster pages reduce friction that causes users to abandon before completing an action.
* **Increased time spent on site** — quicker load times keep visitors engaged rather than waiting.
* **Lower site bounce rate** — pages that render quickly are less likely to be abandoned on arrival.

Overall, the **22% to 47% performance improvement** is achieved without any perceptible loss in image quality.

#### How to Enable Smart Imaging

![Smart Imaging](/help/assets/dynamic-media/assets/dm-smart-imaging.png)

_Smart Imaging automatically optimizes an image's format and file size based on a customer's browser capability and network speed._

Smart Imaging is not turned on by default because it requires a coordinated effort between you and Adobe Dynamic Media technical support. In addition, enabling Smart Imaging requires a complete clearing of your CDN cache, which is then refilled over time. To enable Smart Imaging:

1. **Submit a technical support ticket** to Adobe indicating your interest in using Smart Imaging.
2. **Receive a URL parameter** from technical support that lets you try out Smart Imaging beforehand.
3. **Test the parameter** on any of your web pages or images to observe the performance gains and file-size savings firsthand.
4. **Request full activation** so that Smart Imaging is turned on for your entire site.

This staged approach lets you validate the performance improvement on real pages before committing to a full CDN cache clearing, ensuring the results meet your expectations across your specific browser and network conditions.

### Adaptive Video Sets

An **Adaptive Video Set** groups versions of the same video that are **encoded at different bit rates and formats**, an approach known as **adaptive bitrate streaming**. Dynamic Media uses these sets to deliver the right version of a video to each viewer automatically, based on their device and network conditions.

Video is one of the most powerful forms of on-page content. When a video appears on a page, or on a main page, customers tend to engage with that content longer and stay on the page longer, which improves engagement — a behavior Adobe's analytics confirm. However, delivering video is technically complex, because a single large primary file must be adapted to many playback conditions. Determining how to size and deliver that video — so the experience runs smoothly regardless of the device it is viewed on and regardless of available bandwidth — is a significant challenge. Adaptive Video Sets solve this problem.

#### How Adaptive Video Sets Work

Dynamic Media builds an Adaptive Video Set through a straightforward, automated process:

1. **Upload the primary video.** You start with your original, primary video, which you upload into the system.
2. **Automatic transcoding.** Dynamic Media automatically sizes, or **transcodes**, that primary video into multiple videos at different bit rates and formats.
3. **Intelligent delivery.** At the time of delivery, Dynamic Media intelligently determines which video, what quality, and what format to use, then delivers it to the phone, tablet, or desktop computer.

This automated pipeline ensures that a single uploaded file becomes a full library of optimized renditions, ready to match any playback scenario without manual encoding work.

#### Adaptive Playback Across Devices and Networks

Adaptive Video Sets adjust delivery in real time to match both the device and the connection quality. For example, on an iOS mobile device, Dynamic Media detects the available bandwidth — such as **4G, 5G, or Wi-Fi** — and then automatically selects the correctly encoded video from among the various video bit rates within the Adaptive Video Set. The video is streamed to mobile devices, tablets, or desktop computers.

Playback also adapts continuously during viewing:

- **Dynamic quality switching:** Video quality is dynamically switched automatically when network conditions change. As a result, viewers on a weakening connection receive a lower bit rate to avoid buffering, while viewers on a stronger connection receive higher quality — keeping playback smooth without interruption.
- **Full-screen optimization:** If a customer enters full-screen mode on a desktop, the Adaptive Video Set responds by using a better resolution, improving the customer's viewing experience because a larger display benefits from a higher-quality rendition.

Using Adaptive Video Sets provides smooth, high-quality playback for customers viewing Dynamic Media video across multiple screens and devices. This delivers a consistent, professional viewing experience whether the audience is on a phone, tablet, or desktop, and it reduces buffering and quality issues that can drive viewers away. This removes the technical complexity of video delivery from the workflow.

## Use cases for Dynamic Media {#dm-journey-b}

**Dynamic Media** is a capability for managing, enhancing, and delivering rich media—including images, video, and interactive content—consistently across web, mobile, and social channels. It addresses common media-delivery challenges by automatically optimizing and serving the right asset for each device and context. Solving these challenges drives positive customer engagement, loyalty, conversion, and increased **return on investment (ROI)**, because faster, richer, and more relevant visual experiences directly influence how customers browse, evaluate, and purchase.

The following are common use-case issues and solutions that Dynamic Media resolves.

### Common Dynamic Media use cases

- **Responsive imaging across devices** — Delivering large, unoptimized images slows page load and frustrates shoppers. Dynamic Media automatically resizes, crops, and compresses images to match each device and screen size, which improves page performance and reduces bounce rates.
- **Video delivery and playback** — Hosting and streaming high-quality video reliably across browsers and mobile devices is complex. Dynamic Media encodes and adaptively streams video so playback remains smooth regardless of connection speed, increasing engagement with product and marketing content.
- **Interactive viewers and zoom** — Static product photos limit how much detail a customer can inspect. Dynamic Media provides interactive viewers with high-resolution zoom, spin sets, and image sets, giving shoppers a closer look that builds purchase confidence and reduces returns.
- **On-demand image and asset variations** — Creating and storing every image crop, size, and format manually is time-consuming and error-prone. Dynamic Media generates renditions on demand from a single master asset, which streamlines production workflows and ensures visual consistency.
- **Personalized and contextual media** — Serving the same generic imagery to every visitor reduces relevance. Dynamic Media supports rules-based and contextual delivery so the most appropriate media appears for each audience, supporting higher conversion and stronger brand loyalty.
- **Scalable delivery and workflow efficiency** — Managing rich media at scale strains creative and IT teams. Dynamic Media centralizes assets and automates delivery, freeing teams to focus on strategy while maintaining fast, reliable media across all channels.

Together, these solutions help organizations improve customer engagement, strengthen loyalty, lift conversion, and increase overall return on investment (ROI).

### Use case: Primary file approach

One of the most important use cases for Dynamic Media is also one of the most obvious: reducing the weight of pages and experiences, and the size of the content being delivered — whether it is an image or a video.

#### How one primary file reduces page weight

**About 90% of a typical web page is made up of rich media**, such as images and videos, which are commonly much heavier files. The remaining **10%** consists of **HTML**, **CSS (Cascading Style Sheets)** code, and specific tags. Because rich media dominates the payload, optimizing that 90% delivers the greatest reduction in overall page weight — and **Dynamic Media directly optimizes that 90%, reducing file size at the moment of delivery.**

![Content page weight](/help/assets/dynamic-media/assets/dm-content-page-weight.png)

_Content page weight of a typical web page._

Earlier, you read about the concept of _one primary asset file with endless possibilities_. **This approach is a decisive lever for reducing overall page weight**, because a single primary asset can be reused on a product detail page, a thumbnail page, the shopping cart, and the search grid. The result is a significant time savings and — just as important — guaranteed consistency across every experience.

![Primary file approach](/help/assets/dynamic-media/assets/dm-onefile.png)

_The watch is one primary asset file, but with multiple renditions of it &ndash; not copies &ndash; created on the fly._

Let's look closer at the issues Dynamic Media solves with the one file, and the solutions that approach provides.

#### Issues solved by the one-file approach

| **Issue** | **Dynamic Media solution** |
|---|---|
| Create and store every asset. | Use a single image file, automatically creating required renditions only at the moment of delivery. |
| High storage costs. | Eliminates the need to create and store multiple copies of an asset. |
| Difficulty maintaining chain of custody. | Guarantees delivery of device-optimized and consistent experiences. |
| No version history. | Maintains a single source of truth from which every rendition derives, so there is no fragmented trail of duplicate files to track. |
| Inconsistent brand experiences across devices. | Delivers uniform, brand-accurate renditions optimized for each screen and device. |
| Unnecessary cost of duplicate asset creation. | Removes the manual duplication step entirely, since variations are generated on demand rather than produced and stored in advance. |

When you rely on stored copies instead of one file, you must build an asset for every kind of experience. A single starting image can require 20, 30, or 40 variations — each of which you then have to store and pay for. You also have to ensure the right image is used, which can undermine brand consistency, and if you cannot find a given asset, you are forced back in to duplicate it.

Dynamic Media eliminates that cycle. It creates variations of images on the fly from one starting image, letting you be creative with that primary asset without returning to a graphic design artist or photo studio to produce additional content. That is money and time saved.

#### Benefits of the one-file approach

With the one-file approach, you use a single primary file and then generate the versions or renditions required across your sites, properties, and experiences only at the moment they are delivered to a customer. This efficiency produces several concrete advantages:

- **Lower storage requirements** — renditions are generated on demand rather than created and stored in advance.
- **Reduced workflow complexity** — a single source asset removes the need to manage dozens of duplicate files.
- **Consistent brand experiences** — every rendition derives from the same primary file, ensuring visual uniformity across channels.
- **Optimized delivery on every device** — Dynamic Media's delivery system automatically sizes and compresses each image and video for the requesting screen, so assets load quickly and look great on all devices.

Because renditions are produced at the point of delivery and matched to the device requesting them, every image and video arrives optimized — loading quickly and rendering cleanly across desktops, tablets, and phones.

### Use case: Video

Dynamic Media solves the core challenges of video by taking a single source file and automatically optimizing it for every device, network condition, and page placement. Video is one of the most complex asset types to manage: video files carry large inherent file sizes, which makes them difficult to store, move, and deliver reliably. Because viewers access content across a wide range of screen sizes and connection speeds, delivering high-quality video consistently is a persistent technical hurdle.

#### Common Video Delivery Challenges Dynamic Media Solves

| **Issue** | **Dynamic Media solution** |
|---|---|
| Difficult to manage and deliver video optimized for various devices. | Use a single video that automatically sizes for all devices. |
| Videos stall or play in low quality due to user's available bandwidth. | Deliver video through an **HTML5 (HyperText Markup Language) player** that automatically detects available bandwidth and applies **adaptive bitrate streaming**, ensuring high fidelity and smooth playback while eliminating stalls and buffering. |
| Unfeasible and time-consuming to manually create all versions of a video just to ensure good display and playback across devices. | Eliminate hours of tedious **transcoding** work with a simplified workflow. |
| | Free up time for higher value work, allowing teams to focus on strategy and content creation rather than manual encoding tasks. |

Customers come to Dynamic Media with the following issues that they are hoping to solve. As one representative account illustrates, uncertainty about playback quality can cause organizations to withhold video they have already invested in producing:

"_My business has the video, and the department spent a large amount of money creating it, but shied away from placing it on pages, or delivering it. The reason was because from testing, the quality of the video could not be guaranteed, or even if it was really going to play. And ultimately, that affects the business's brand and potentially its role to conversion._"

#### How Dynamic Media Delivers Consistent Video Quality

Dynamic Media's solution takes that one primary video file and generates all required sizes through its **transcoding process**. It then pairs that output with Dynamic Media's **intelligent video player**. This workflow guarantees a consistent, high-quality experience across every placement. Whether marketers place the video on a main landing page, a category page, or a product detail page, the video renders consistently and delivers **high quality** across every touchpoint. As a result, brands avoid the playback failures and quality inconsistencies that can undermine both user trust and conversion.

Dynamic Media addresses additional use cases beyond video.

### Use case: Single source of truth

A **single source of truth** consolidates every digital asset into one authoritative location, giving teams a consistent, up-to-date foundation for all content across channels.

| **Issue** | **Dynamic Media solution** |
|---|---|
| Digital assets scattered across the organization, siloed in different teams or business units. | Store and manage all digital assets in a **single, central location**. |
| Team members download and create local versions. | Team members use a **single primary source file** to create _and_ deliver every version needed across various screen sizes and devices, ensuring brand consistency. |
| Single-use assets created for every experience and device. | Eliminates single-use assets, **saving time and money** because one source file serves every experience. |

### Use case: AI-powered Smart Cropping for rich media

| **Issue** | **Dynamic Media solution** |
|---|---|
| Time-consuming and labor intensive to manually draw, measure, and cut images or videos to highlight the focal point and deliver responsively across all screen sizes and devices. | Uses **Smart Crop** in Dynamic Media, an **Adobe AI capability**, to automatically detect the focal point in any image or video and crop around it, preserving that focus. |
| Time lost that could be better spent creating high-impact experiences. | Preserves the intended point of interest at any screen size. |
| Single-use assets created for every experience and device. | Eliminates manual tasks, so teams deliver high-quality, fast-loading imagery and video optimized for any device or screen. |

### Use case: Interactive media authoring

| **Issue** | **Dynamic Media solution** |
|---|---|
| Flat and static customer experiences fail to engage shoppers, and because they do not hold attention, they weaken loyalty and reduce conversion. | Empowers non-technical users — including marketers and merchandisers — to easily and seamlessly add interactive elements such as **hot spots**, **carousels**, and **spin sets**, transforming static product pages into interactive, exploratory experiences that hold attention and encourage discovery. |
| Limited return on investment from underused digital assets, resulting in lackluster customer experiences that leave the full value of rich media untapped. | Drives conversion and return on investment by turning digital assets into interactive rich media that lets customers examine products closely, which builds purchase confidence and maximizes the value extracted from each asset. |

## How an asset flows through the Dynamic Media system {#dm-journey-c}

A typical **Adobe Dynamic Media** workflow moves an asset through three sequential phases: **Creation**, **Authoring**, and **Publishing**. Each phase builds on the previous one, ultimately delivering optimized content across every major channel.

![Dynamic Media workflow](/help/assets/dynamic-media/assets/dm-workflow.png)

_How an asset flows through the Dynamic Media system._

### Phase 1: Creation — Producing the Primary Asset

The workflow begins with the **creation phase**, whose primary goal is to finish with a completed **primary asset**. Primary assets typically originate from one of the following sources:

- **Photo shoots**, producing high-resolution imagery
- **Video vendors**, supplying video content
- **Audio files** created specifically for the project

Adobe Creative Suite applications support this phase, including **Adobe InDesign**, **Adobe Photoshop**, and **Adobe Illustrator**, which help produce and refine the content before it enters the system.

### Phase 2: Authoring — Uploading and Configuring in Dynamic Media

Once creation is complete, the asset moves into the **Authoring solution** by being uploaded into Dynamic Media. Within Dynamic Media, the key configuration step is aligning the correct **image presets** and **viewers** with the various web pages across the site. This ensures each asset renders correctly and is presented in the appropriate interactive experience for its intended page.

### Phase 3: Publishing — Optimizing and Delivering to Servers

In the final phase, the content is optimized and published to the **Dynamic Media servers**, making the asset available for delivery. As a result, the published content is ready to serve across every major channel:

- **Web**
- **Print**
- **Email**
- **Desktops**
- **Mobile devices**

Publishing to the Dynamic Media servers is what makes the optimized asset accessible to end users, completing the journey from initial creation through authoring to multi-channel delivery.

### Uploading Assets into Dynamic Media

**Adobe recommends uploading assets in a lossless format** to maximize the value of Dynamic Media's single-file support. When you finish creating a primary asset, you upload it into Dynamic Media, where the file type, format, and size are critical attributes. Upload is the moment to ensure you extract the maximum value from **one primary asset file**, because Dynamic Media generates every rendition and delivery variation from that original.

For example, the watch image referenced below measures **4560 x 3020 pixels**. Even if you never publish an image at that full size, you can still upload it. **The larger the source image, the higher the quality Dynamic Media can deliver — down to the smallest thumbnail rendition** — because Dynamic Media scales down from the original rather than up.

Remember this rule: you can easily **decrease** the resolution of an existing image, but increasing the resolution produces poor results. If you attempt to **increase** the resolution of an image, the result is unsatisfactory because upscaling cannot recover detail that was never captured in the original file.

![Recommended formats to upload into Dynamic Media](/help/assets/dynamic-media/assets/dm-upload-formats.png)

#### Considerations for Asset Uploads

**Adobe recommends starting with the highest-resolution images in a lossless format** that you can practically work with. Key guidance for uploads includes:

- **Use a lossless format.** The preferred formats are **TIFF** or **PNG**, which preserve full image quality.
- **Avoid JPEG.** JPEG uses lossy compression, so each time you deliver a JPEG or re-save a JPEG, image quality degrades further over time. This cumulative loss is why lossless formats are the safer starting point.
- **Upload the largest quality you can maintain.** A higher-resolution source gives Dynamic Media more data to work from for every downstream rendition.

#### Color Space: RGB vs. CMYK

For digital channels and web views, you typically think in terms of **RGB (Red, Green, Blue)**, the standard color space for on-screen delivery.

By contrast, **CMYK (Cyan, Magenta, Yellow, Key/Black)** is the color space most often used for delivering printed items. Many people never consider delivering in CMYK — but **Dynamic Media can deliver in both color spaces**.

This matters because many customers still produce printed materials. Warehouse wholesale clubs and grocery stores, for instance, often print flyers on a weekly basis. Such customers require their images in **both RGB and CMYK**. Traditionally, meeting that requirement meant maintaining two separate images: one in RGB and one in CMYK.

Dynamic Media eliminates this duplication. You can upload **CMYK assets directly into Dynamic Media** and have Dynamic Media automatically deliver **RGB assets through an image preset or a color profile**. As a result, there is no need to create multiple versions of a file, which preserves the core principle of **one primary asset file with endless possibilities**.

<!-- **The Value of Renditioning??? or Demo portion** -->

### Publish and preview assets

Publishing is required before uploaded assets can be used in any Dynamic Media experience, because unpublished assets are not accessible through Dynamic Media delivery. As a best practice, publish assets immediately after uploading them.

#### Publishing assets

To publish assets manually in Dynamic Media:

1. Select the assets you want to make available.
2. Click **[!UICONTROL Publish]** or **[!UICONTROL Quick Publish]** in Dynamic Media.

After assets are published, they are available for inclusion in a web page in two ways:

- **Copy a Dynamic Media-generated URL (Uniform Resource Locator)** and reference it directly on the page.
- **Embed the provided code** on the page.

##### Automatic publishing on upload

Besides manually publishing assets, you can configure Dynamic Media to publish assets automatically—without any user intervention—at the time of upload. Automatic publishing eliminates the manual selection and publish step, which streamlines high-volume workflows and ensures newly uploaded assets are immediately ready for delivery.

#### Previewing asset renditions

Following upload, Dynamic Media provides multiple ways to preview an asset's renditions. Previewing renditions shows how the asset appears to the end customer before it is used in a live experience. There are two common preview methods.

##### Method 1: Preview with an image preset

To preview a rendition using an image preset:

1. Select an asset.
2. View its **Renditions** by selecting an _image preset_, as shown below.

![Previewing a rendition of an asset based on the Large image preset](/help/assets/dynamic-media/assets/dm-image-preset-with-url.png)

_Previewing a rendition of an asset based on the selected "Large" image preset. The URL button was clicked. The resulting URL path contains the "Large" image preset name and can be used in a web page._

The URL above is live. [Try it](http://s7d1.scene7.com/is/image/jpearldemo/AdobeStock_28563982?$Large$){target="_blank"}.

##### Method 2: Preview with a Viewers preset

To preview an asset using a Viewers preset:

1. Select the image asset.
2. Select a _Viewers_ preset, as shown below.

![Previewing an asset based on the Zoom Vertical Light viewer preset](/help/assets/dynamic-media/assets/dm-viewer-preset.png)

_Previewing an asset based on the selected "ZoomVertical_light" viewer preset. The mouse pointer (`+`) was moved over the watch to zoom in. Notice the URL and Embed buttons._

The rendition above is live. [Try it](https://s7d1.scene7.com/s7viewers/html5/ZoomVerticalViewer.html?asset=jpearldemo/AdobeStock_28563982&config=jpearldemo/ZoomVertical_light){target="_blank"}.

## Optional - Learn more

<!--
_Dynamic Media Help topics_

* [Work with Dynamic Media in Experience Manager](/help/assets/dynamic-media/dynamic-media.md)
* [About Smart Imaging](/help/assets/dynamic-media/imaging-faq.md)
* [How to create Adaptive Video Sets](/help/assets/dynamic-media/video.md)
* [Best practices for optimizing the quality of your images](/help/assets/dynamic-media/best-practices-for-optimizing-the-quality-of-your-images.md)
* [How to upload assets](/help/assets/add-assets.md#upload-assets)
* [How to preview assets](/help/assets/dynamic-media/previewing-assets.md)
* [How to preview 3D assets](/help/assets/dynamic-media/previewing-3d-assets.md)
* [How to deliver Dynamic Media Assets](/help/assets/dynamic-media/delivering-dynamic-media-assets.md)
* [How to publish assets](/help/assets/dynamic-media/publishing-dynamicmedia-assets.md)
* [Work with Selective Publish in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md)
-->

Part I of this journey covered the fundamentals of Dynamic Media, including asset delivery, interactive viewers, and integration with Adobe Experience Manager (AEM). To explore these Dynamic Media concepts in greater depth, use the curated resources below. Otherwise, you can continue directly with Part II of this journey. See [What's next in this Dynamic Media Journey](#whats-next).

These supplementary materials expand on the core topics introduced in Part I, providing deeper technical explanation, guided walkthroughs, and live examples that reinforce practical understanding.

### Dynamic Media Tutorials

* [Use Dynamic Media with Experience Manager Assets](https://experienceleague.adobe.com/docs/experience-manager-learn/assets/dynamic-media/dynamic-media-overview-feature-video-use.html) — a feature-focused overview demonstrating how Dynamic Media works within Adobe Experience Manager (AEM) Assets to deliver rich, responsive media experiences.
* [Adobe Experience Manager content library](https://experienceleague.adobe.com/?lang=en#recommended/solutions/experience-manager) — the comprehensive Adobe Experience Manager (AEM) learning hub. Search on _Dynamic Media_ to surface additional tutorials, articles, and reference documentation.

### Dynamic Media Viewers

* [Live Demos](https://landing.adobe.com/en/na/dynamic-media/ctir-2755/live-demos.html) of each viewer — interactive demonstrations that showcase how each Dynamic Media viewer renders and behaves in a real browser environment, so you can evaluate viewer capabilities and appearance before implementation.

## What's next in this Dynamic Media Journey {#whats-next}

Part II of this journey examines **Dynamic Media URLs** in detail, explaining how an asset is processed and delivered to the requesting browser or application. Understanding the structure of these URLs clarifies exactly how Dynamic Media generates and serves each rendition on demand.

Part II covers the following core topics:

- **Dynamic Media URLs** — a close look at URL syntax to understand what happens during asset delivery.
- **Image presets** — the fundamentals behind creating image presets that render assets at specific sizes, formats, and quality settings.
- **Image sets** — collections that let viewers browse multiple related images of a product or subject.
- **Spin sets** — sets that enable interactive 360-degree rotation of an asset.
- **Mixed Media sets** — sets that combine images, spin sets, and video into a single unified viewing experience.

Because image presets and these viewer sets determine how assets appear across devices and channels, mastering their creation is essential to delivering consistent, responsive visual experiences at scale.

Take me to [Dynamic Media Journey: The Basics, Part II](/help/assets/dynamic-media/dm-journey-part2.md#dm-journey-d).

<!-- Live as of April 28 2022. LEAVE IN HERE https://landing.adobe.com/en/na/dynamic-media/ctir-2755/index.html -->
