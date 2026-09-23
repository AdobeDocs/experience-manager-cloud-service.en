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

This guide introduces **Dynamic Media** on **Adobe Experience Manager**, explaining how the system works, the core capabilities it delivers, and how it accelerates the creation, management, and delivery of rich visual media across web, mobile, and marketing channels. **Dynamic Media** enables organizations to serve interactive, responsive, and on-demand imagery and video from a single master asset, reducing production overhead and improving the customer experience across every touchpoint.

**_Prerequisites_**

Before beginning this journey, readers benefit from familiarity with the following areas, because **Dynamic Media** interacts directly with these formats, technologies, and design workflows:

* Basic understanding of image and video formats — required because **Dynamic Media** ingests, transforms, and delivers assets in a variety of encodings.
* Basic understanding of HyperText Markup Language (HTML) and Cascading Style Sheets (CSS) — helpful for embedding and styling **Dynamic Media** deliveries on web pages.
* Basic understanding of design tools such as Adobe Illustrator, Adobe Photoshop, and Adobe XD — useful because source assets for **Dynamic Media** are typically produced in these applications.
* Access to **Dynamic Media** on **Adobe Experience Manager** is helpful, but not required to follow along conceptually.

**_What you can expect to learn_**

_Part I_

* What **Dynamic Media** is and how it supports scalable, high-performance delivery of rich media.
* Practical use cases for **Dynamic Media**, including responsive imagery, interactive video, 360° product spins, and personalized visual experiences for eCommerce and marketing.
* How an asset flows through the **Dynamic Media** system, from ingestion through processing to end-user delivery.

_Part II_

* Anatomy of a **Dynamic Media** Uniform Resource Locator (URL) and how **Dynamic Media** delivers content on demand through its image server.
* Fundamentals of creating **image presets** to render assets at the required dimensions, formats, and quality settings.
* **Image sets** (collections of related product images for alternate views), **spin sets** (sequences of images that create a 360° rotating view of a product), and **mixed media sets** (combinations of images, video, and spin sets in a single interactive viewer).

**_Audience_**

This journey is designed for the following roles that are new to **Dynamic Media** on **Adobe Experience Manager**:

* Administrator
* Business Analyst
* Content Architect
* Content Author
* Designer
* Developer
* Marketer
* Product Manager/Lead

>[!TIP]
>
>For best results, Adobe recommends that you read and view this **Dynamic Media** documentation on a desktop computer, because the visual examples, interactive viewers, and code samples render most clearly on a larger screen.

## What is Dynamic Media and how can it help you? {#dm-journey-a}

**Dynamic Media** is an Adobe solution that enables brands and marketers to deliver rich visual merchandising and marketing assets on demand. Working from a set of **primary source assets** — such as images, video, and 3D — Dynamic Media generates and delivers multiple variations of this rich content **in real time** through its **global, scalable, performance-optimized CDN (Content Delivery Network)**.

### Key Capabilities

Dynamic Media creates and serves interactive viewing experiences, including:

- **Zoom** — high-resolution close-up viewing of product imagery
- **360-degree spin** — rotational product views that let shoppers examine an item from every angle
- **Video** — streaming media delivered alongside static assets

Assets are dynamically scaled for consumption across **web, mobile, and social sites**. Because rendering happens in real time on the CDN, a single master asset can be reused across every channel and device size, eliminating the need to manually produce and store separate versions for each destination. This reduces production overhead and helps ensure a consistent brand experience wherever customers encounter the content.

### Integration with Adobe Experience Manager Assets

Dynamic Media incorporates the workflows of the **Adobe Experience Manager Assets** digital asset management (DAM) solution to simplify and streamline the digital campaign management process. This integration means creative, marketing, and merchandising teams can manage source files, approvals, metadata, and delivery from a unified environment — connecting asset governance directly to omnichannel delivery.

### One file with multiple delivery options

**Adobe Dynamic Media operates on a single core principle: one primary asset file, multiple delivery options.** Instead of duplicating and manually re-versioning media for every channel, device, or web page, Dynamic Media stores a single **primary asset** and generates every rendition on demand from that one source.

To appreciate why this matters, consider the traditional workflow for a single asset such as an image or a video. Teams typically create one primary asset and then manually produce versions of that same asset for every experience, every target device, every web page, and every property where the asset appears. Over time, that single asset can balloon to 20, 30, or more versions — often with no version history attached. Now multiply that effort across every image and video in a library. The volume of asset variants becomes overwhelming to maintain and update, and storage costs climb accordingly.

#### How Dynamic Media is different

Dynamic Media is fundamentally different from traditional systems because marketers and developers use Dynamic Media to deliver media *dynamically* from single, primary assets through URL calls. The **Dynamic Media URL paths** that a client requests contain embedded instructions that tell the Adobe publish server how to display the asset when it is delivered to a customer's screen. As a result, the same single primary asset can be delivered instantly in **unlimited renditions**, with on-the-fly variations such as:

- **Size** — dimensions tailored to the target layout or breakpoint
- **Format** — image or video format optimized for the requesting client
- **Resolution** — pixel density matched to the display

This means teams no longer need to pre-generate and store every possible variant. Instead, the URL itself defines the rendition, and the server produces it in real time.

#### Consistent quality across every screen and bandwidth

This delivery method ensures Adobe Dynamic Media sends consistent, high-quality experiences to any screen, regardless of size or bandwidth. Dynamic Media also optimizes full-size videos for all screen types and **adaptively streams** them, adjusting quality based on the viewer's connection to preserve a smooth, uninterrupted user experience.

<!-- As part of building and publishing assets with Dynamic Media, you visually configure the effects that you want to apply to assets. In so doing, you are literally building the URL that correctly tells the publish server how to deliver your primary asset to the screen.  -->

![Adobe Dynamic Media delivers the same primary image to different mediums in different sizes and formats](/help/assets/dynamic-media/assets/dm-oneasset-multioutput.png)
*Adobe Dynamic Media ensures consistent, quality experiences are delivered to any screen, regardless of size or bandwidth.*

#### Why "one primary asset, multiple delivery options" matters

Consolidating on a single primary asset produces several practical benefits that follow directly from the model:

- **Reduced storage footprint** — one source file replaces dozens of manually produced variants.
- **Faster iteration** — updating the primary asset propagates changes across every downstream rendition automatically.
- **Consistent brand experience** — every device and channel is served from the same authoritative source, eliminating drift between versions.
- **Simplified governance** — a single source of truth is easier to track, audit, and update than a sprawling collection of ad hoc copies.

As the following sections explain, this "one primary asset file, multiple delivery options" concept is the foundation for how Dynamic Media scales media delivery efficiently across web, mobile, and connected experiences.

### The Content Delivery Network

When you are ready to go live with an image or video asset, Dynamic Media's backbone — a powerful, top-tier delivery network serving hundreds of clients worldwide every day — supports it. Dynamic Media distributes assets across a **Content Delivery Network (CDN)** hosted by **Akamai**. The CDN is a distributed network of edge servers that work together seamlessly to deliver content, especially large rich media files, to end users around the globe.

#### How the CDN Works

Web content is stored in web caches positioned across the Internet, then served from the nearest cache directly to end users for faster delivery. The process works as follows:

1. **First request:** When someone downloads a web page for the first time, the assets are delivered to a CDN cache in that geographic region.
2. **Cache storage:** Those assets are stored on the local edge server.
3. **Subsequent requests:** The next time a user in the same area accesses the page, the cached content is delivered from the nearby server rather than the origin.

Content arrives faster because it sits physically closer to the user, reducing network latency and round-trip time. This is the core mechanism that makes CDNs faster than traditional single-origin delivery.

#### Benefits for End Users and Businesses

A CDN delivers measurable advantages:

- **Faster web page displays** through geographically proximate caching
- **Reduced bandwidth demand on the central server**, because content is served from the cache network rather than the origin for every request
- **Improved user experience**, driven by lower latency and quicker asset rendering
- **Increased sales**, as the optimized delivery flow keeps visitors engaged rather than lost to slow load times

#### Performance and Scale

Operating at massive global scale, the CDN historically delivers:

- **3.5 petabytes of traffic to customers every month**
- **52 billion assets in a single day**

<!-- USE AN IMAGE HERE? ![Content delivery network](/help/assets/assets-dm/cdn.png) -->
- **864,000 images and videos successfully delivered to customers _every second_**

These figures illustrate the throughput and reliability that Dynamic Media's Akamai-backed CDN brings to rich media distribution.

### Smart Imaging

Dynamic Media already optimizes assets and ensures that each asset loads quickly on mobile and desktop systems using a Content Delivery Network (CDN). To make that happen, Dynamic Media uses **image presets** to define the quality of your image. Image presets also define the type of image that you are sending, its sharpness, and other rendering parameters for different parts of your experiences or pages.

But to add value to Dynamic Media further beyond image presets, there is _Smart Imaging_.

**Smart Imaging delivers a 22% to 47% performance improvement** over standard Dynamic Media delivery, depending on your existing image preset settings and specific end-user characteristics — all while preserving image quality as if the asset were never touched.

#### How Smart Imaging Works

Smart Imaging provides even better image asset delivery performance by automatically optimizing an image's **format** and **file size** based on a customer's **browser capability**. It works with your existing image presets (image presets are discussed in Part II of this journey) and applies intelligence at delivery time.

This intelligence further reduces image file size based on browser and **network connection speed**. In short, Smart Imaging automatically optimizes an image's format and file size based on a customer's browser capability and network speed, adapting each delivery to the specific viewing conditions.

#### Performance and Business Impact

Because image assets make up most of a page's load time, the performance improvement produced by Smart Imaging directly influences several key business indicators. Faster image delivery leads to:

* **Higher conversion** rates
* Increased **time spent on site**
* **Lower site bounce rate**

The causal chain is straightforward: smaller, better-optimized images load faster, faster pages create smoother user experiences, and smoother experiences translate into stronger engagement and revenue outcomes.

#### How to Enable Smart Imaging

![Smart Imaging](/help/assets/dynamic-media/assets/dm-smart-imaging.png)

Adobe Dynamic Media technical support does not turn on Smart Imaging by default because it requires a coordinated effort. Enabling Smart Imaging also requires a complete clearing of your CDN cache, which is then refilled over time — this ensures that previously cached, unoptimized image variants are replaced with the newly optimized deliveries.

To use Smart Imaging, follow these steps:

1. **Submit a technical support ticket** to Adobe Dynamic Media technical support.
2. **Receive a URL parameter** from technical support that lets you preview Smart Imaging behavior before full activation.
3. **Test on any web page or image** to measure the performance gains and file-size savings on your own content.
4. **Request full activation** so that Smart Imaging is turned on for your entire site.

This trial-then-activate approach allows you to validate the expected 22% to 47% performance improvement against your specific presets and audience before committing to a site-wide rollout.

### Adaptive Video Sets

An **Adaptive Video Set** groups multiple encoded versions of the same source video — each rendered at a different **bit rate** and **format** — so that the optimal file can be delivered to any device under any network condition. This is Dynamic Media's solution for streaming video smoothly across phones, tablets, and desktops without the publisher having to manually manage encoding, sizing, or delivery logic.

#### Why Video Delivery Is Complex

When a page contains video, customers typically engage with that content longer and remain on the page longer — a behavior pattern that Adobe has observed through its own analytics. Capturing that engagement, however, requires solving several technical problems at once:

- The **primary source file is large**, often too heavy to serve directly.
- The player must decide **how to size, encode, and deliver** the video so that playback is smooth.
- Playback must remain reliable **regardless of the viewer's device or available bandwidth**.

Dynamic Media addresses these challenges by generating and serving an Adaptive Video Set in place of a single static file.

#### How Adaptive Video Sets Work

1. **Upload the primary video.** You start with your original, high-quality source file and upload it into the system.
2. **Automatic transcoding.** Dynamic Media automatically sizes, or _transcodes_, that source into multiple derivative videos — each encoded at a different resolution and bit rate optimized for a specific class of device or connection speed.
3. **Intelligent delivery at request time.** When a viewer requests the video, Dynamic Media determines **which encoded version, which quality level, and which format** to serve, then streams it to the phone, tablet, or desktop computer.

For example, on an iOS mobile device, Dynamic Media detects whether the connection is **4G, 5G, or Wi-Fi**. Based on that signal, it automatically selects the appropriate encoded video from the various bit rates within the Adaptive Video Set and streams it to the device.

#### Automatic Quality Switching

Adaptive Video Sets respond continuously to viewing conditions:

- **Network fluctuations:** When network conditions change mid-playback, the player automatically switches to a different encoded version within the set. This keeps playback continuous and reduces interruptions caused by bandwidth drops.
- **Full-screen viewing on desktop:** When a customer enters full-screen mode, the Adaptive Video Set responds by delivering a higher-resolution encoding, improving the viewing experience at the larger display size.

#### Key Benefits

Using Adaptive Video Sets delivers:

- **Smooth, high-quality playback** for customers watching Dynamic Media video across multiple screens and devices.
- **Simplified video management**, because a single source upload is automatically transcoded into every version needed — eliminating the need to manually create, store, and target separate files for each device or bandwidth scenario.
- **Consistent viewer experience**, since the same Adaptive Video Set adapts on the fly to device capability, connection type, and playback context.

## Use cases for Dynamic Media {#dm-journey-b}

The following are common use-case issues and solutions that Dynamic Media solves to drive positive customer engagement, loyalty, conversion, and increased **Return on Investment (ROI)**.

Dynamic Media addresses recurring challenges faced by marketing, e-commerce, and digital experience teams that must deliver rich visual content at scale across every device, channel, and audience segment. By centralizing image, video, and interactive media production and delivery, Dynamic Media reduces manual production overhead, accelerates time-to-market, and ensures that customers see the right visual experience in the right context — which in turn strengthens engagement and lifts conversion rates.

### Common Dynamic Media Use Cases

- **Responsive, device-optimized imagery** — Automatically deliver images sized, cropped, and compressed for the requesting device and viewport. This eliminates the need to produce and store multiple manual renditions, improves page load performance, and creates a consistent visual experience across desktop, tablet, and mobile.
- **On-demand video delivery and streaming** — Encode, host, and adaptively stream video across channels without third-party video platforms. Adaptive bitrate delivery ensures smooth playback under varying network conditions, which supports higher watch-through rates and richer product storytelling.
- **Interactive viewers and rich media experiences** — Provide zoom, 360-degree spin, image sets, carousels, and video-with-hotspot viewers that let shoppers examine products in detail. Interactive experiences deepen engagement and reduce purchase hesitation, contributing directly to higher conversion.
- **Smart cropping and AI-assisted imaging** — Use intelligent cropping to keep the subject of an image centered across every aspect ratio and channel. This removes repetitive manual editing work and keeps merchandising visuals on-brand at scale.
- **Personalized and contextual visual experiences** — Serve variations of the same asset — different colors, languages, price overlays, or promotional messages — from a single master file. Personalization at the asset level increases relevance for each audience segment and supports loyalty by making experiences feel tailored.
- **Consistent omnichannel delivery** — Publish once and deliver everywhere: web, mobile apps, email, social, in-store screens, and marketplaces. A single source of truth for media prevents inconsistencies that erode brand trust.
- **Faster time-to-market for campaigns** — Reuse master assets with dynamic parameters instead of re-shooting or re-editing for every campaign. Marketing teams can launch, iterate, and localize campaigns more rapidly, which sustains momentum and improves campaign ROI.

Each of these use cases links a concrete production or delivery problem to a measurable business outcome — reduced operational cost, faster launch cycles, stronger customer engagement, higher conversion, and improved long-term loyalty.

### Use case: Primary file approach

#### The page-weight problem

**Approximately 90% of a typical web page's weight comes from rich media** — images and video files that are often significantly heavier than other page components. The remaining **10% is HTML, CSS code, and specific tags**. Reducing page weight and content size — whether for an image or a video — is one of the most important and most obvious use cases for Dynamic Media. Lighter pages load faster, perform better on mobile networks, and deliver a smoother experience across devices, all of which contribute to stronger engagement and conversion outcomes.

![Content page weight](/help/assets/dynamic-media/assets/dm-content-page-weight.png)
_Content page weight of a typical web page._

Because rich media dominates page weight, optimizing that 90% is where Dynamic Media focuses. The core concept is **one primary asset file with multiple delivery options**, and this approach is central to reducing overall page weight.

<!-- **The Value of Renditioning??? or Demo portion** -->

#### The single primary file approach

A single primary asset can power many surfaces at once. For example, one product image can be reused on:

- The product detail page
- A thumbnail page
- The shopping cart
- The search grid

![Primary file approach](/help/assets/dynamic-media/assets/dm-onefile.png)
_The watch is one primary asset file, but with multiple renditions of it &ndash; not copies &ndash; created on the fly._

This reuse is highly efficient and ensures visual consistency across every experience where the asset appears.

#### Issues Dynamic Media solves with the single-file approach

| **Issue** | **Dynamic Media solution** |
|---|---|
| Create and store every asset. | Use a single image file, automatically creating required renditions only at the moment of delivery. |
| High storage costs. | Eliminates the need to create and store multiple copies of an asset. |
| Difficulty maintaining chain of custody. | Guarantees delivery of device-optimized and consistent experiences. |
| No version history. | Maintains a single source of truth, so every rendition traces back to one primary asset and updates propagate everywhere it is used. |
| Inconsistent brand experiences across devices. | Delivers device-optimized renditions from one master file, ensuring the brand looks the same across screens, resolutions, and form factors. |
| Unnecessary cost of duplicate asset creation. | Generates variations dynamically at delivery, removing the need to commission, approve, and store duplicates of the same asset. |

#### Why duplicating assets creates hidden costs

When teams create a separate asset for every kind of experience, one starting image typically becomes 20, 30, or 40 stored variations — each of which must be paid for and managed. Teams then have to ensure that the correct image is used in each context, which directly affects brand consistency. When an image cannot be located, teams end up duplicating assets again, compounding both storage and coordination costs.

#### Benefits of the one-file approach

Dynamic Media creates variations of images dynamically from that one starting image. Creative teams can work flexibly with the primary asset without repeatedly coordinating with the graphic design team or the photo studio to generate additional content. This directly reduces production costs and shortens time-to-market, because renditions are produced on demand rather than pre-built and warehoused.

With the one-file approach, a single primary file powers every downstream version. Renditions required across sites, properties, and customer experiences are generated only at the moment they are delivered to a customer. This efficiency substantially decreases the storage footprint required for assets and reduces overall workflow complexity. Dynamic Media's delivery system guarantees that every image and video is optimized, loads quickly, and looks great on all screens and devices.

### Use case: Video

Dynamic Media addresses one of digital commerce's most demanding asset types: **video**. Video assets are inherently complex to manage, store, and distribute because of their large file sizes, multiple format requirements, and the need to render smoothly across a wide range of devices, screen resolutions, and network conditions. Without an automated pipeline, teams typically face manual transcoding, inconsistent playback quality, and slow load times — all of which directly impact brand perception and conversion.

| **Issue** | **Dynamic Media solution** |
|---|---|
| Difficult to manage and deliver video optimized for various devices. | Use a **single master video** that automatically sizes and reformats for all devices, screen resolutions, and orientations. |
| Videos stall or play in low quality due to the user's available bandwidth. | Deliver video through an **HTML5 player** that **auto-detects available bandwidth** and dynamically adapts stream quality (adaptive bitrate streaming) to ensure high fidelity and smooth, uninterrupted playback. |
| Unfeasible and time-consuming to manually create all versions of a video just to ensure good display and playback across devices. | Eliminate hours of tedious **transcoding** work — the process of converting a source video into multiple encoded formats and resolutions — with a simplified, automated workflow. |
| | **Free up team capacity for higher-value creative and strategic work**, since production teams no longer have to hand-produce device-specific renditions. |

Customers come to Dynamic Media with the following issues that they are hoping to solve:

"_My business has the video, but avoided delivering it. Testing showed the video quality was inconsistent. This affects the brand and conversion._"

Inconsistent playback erodes user trust and increases bounce rates, because visitors interpret stalled or low-quality video as a signal of poor product or brand quality. Dynamic Media's solution is to take that one primary video file and let Dynamic Media generate all the required sizes and encodings through its automated **transcoding** process. That output is then paired with Dynamic Media's **intelligent video player**, which selects the optimal rendition in real time based on device and connection.

As a result, this workflow guarantees consistent, high-quality playback wherever the video appears — whether on the main landing page, a category page, or a product detail page — helping preserve brand integrity and supporting stronger conversion performance across the customer journey.

Here are several more use cases to consider.

### Use case: Single source of truth

| **Issue** | **Dynamic Media solution** |
|---|---|
| Digital assets scattered across the organization, siloed in different teams or business units. | Store and manage all digital assets in a **single central repository**, giving every team one authoritative source. |
| Team members download and create local versions. | Team members work from **one primary master file** to create _and_ deliver every version needed across screen sizes and devices. |
| Single-use assets created for every experience and device. | **Eliminates single-use assets**, which reduces duplicated production work and lowers the time and cost of creating them. |

### Use case: AI-powered Smart Cropping for rich media

| **Issue** | **Dynamic Media solution** |
|---|---|
| Time-consuming and labor intensive to manually crop, resize, and reframe images or videos to highlight the focal point and display appropriately across all screen sizes and devices. | Uses **Smart Crop** in Dynamic Media, an Adobe Artificial Intelligence (AI) capability, to automatically identify the focal point—the visual subject or point of interest—in any image or video, then intelligently crops around it to preserve that focus across every rendition. |
| Time lost that could be better spent creating high-impact experiences. | Captures the intended point of interest regardless of screen size, so creative teams can redirect effort toward designing high-impact campaigns rather than reformatting assets. |
| Single-use assets created for every experience and device. | Eliminates repetitive manual production work while delivering high-quality, fast-loading imagery and video that supports stronger engagement and conversion, rendering sharply and consistently across desktops, tablets, mobile phones, and other screen sizes. |

### Use case: Interactive media authoring

| **Issue** | **Dynamic Media solution** |
|---|---|
| **Flat and static customer experiences** that fail to engage audiences, build loyalty, or drive conversion. | Empowers non-technical users to easily and seamlessly add interactive elements such as **hot spots**, **carousels**, and **spin sets**, producing more dynamic, engaging shopping and browsing experiences without developer involvement. |
| **Limited return on investment** from underused digital assets and lackluster customer experiences. | Drives higher conversion rates and stronger return on investment by transforming static digital assets into interactive rich media experiences that hold shopper attention, encourage product exploration, and reduce reliance on additional creative production. |

## How an asset flows through the Dynamic Media system {#dm-journey-c}

A typical **Dynamic Media** workflow moves an asset through three sequential phases: **(1) Creation**, **(2) Authoring/Upload**, and **(3) Optimization and Publishing**. The end result is a single **primary asset** delivered dynamically across web, print, email, desktop, and mobile channels from centralized **Dynamic Media servers**.

_How an asset flows through the Dynamic Media system._

**1. Creation phase — producing the primary asset**

The workflow begins in the creation phase, where the goal is to produce a high-quality **primary asset**. These primary assets typically originate from:

![Dynamic Media workflow](/help/assets/dynamic-media/assets/dm-workflow.png)

- Professional photo shoots
- Video vendors and production partners
- Audio files produced for the project

**Adobe Creative Suite** applications support this stage, including **Adobe InDesign**, **Adobe Photoshop**, and **Adobe Illustrator**, which are used to design, retouch, and finalize the source content before it enters the Dynamic Media system.

**2. Authoring phase — uploading into Dynamic Media**

Once creation is complete, the finished asset is uploaded into the Authoring solution within **Dynamic Media**. During this phase, the correct **image presets** and **viewers** are configured and aligned with the various web pages on the site, so that each asset renders with the appropriate size, quality, and interactive behavior for its intended placement.

**3. Publishing phase — optimization and multi-channel delivery**

In the final phase, the content is optimized and published to **Dynamic Media servers**. This optimization prepares the asset for dynamic delivery, which enables a single master file to be reused efficiently across every output channel. Once published, the asset becomes available for delivery to:

- **Web** pages and responsive sites
- **Print** production
- **Email** campaigns
- **Desktop** experiences
- **Mobile** devices

This centralized publish-once, deliver-anywhere model ensures visual consistency across channels while reducing the need to store and manage separate renditions for each destination.

### Uploading Assets into Dynamic Media

After creating a primary asset, upload it into Dynamic Media. The **file type, format, and size** are critical attributes that determine how Dynamic Media processes and delivers the asset. At the time of upload, ensure you extract the maximum value from the **one-file support** model.

For example, the watch image below measures **4560 x 3020 pixels**. Even if you never intend to display an image at that full size, you should still upload it at the highest available resolution. The larger the source image, the better the quality Dynamic Media can deliver across every rendition — down to the smallest thumbnail — because Dynamic Media can downsample from a high-resolution master without introducing artifacts. Remember this key principle: you can easily _decrease_ the resolution of an existing image, but attempting to _increase_ the resolution of a low-resolution image produces unsatisfactory, pixelated results.

#### Considerations for Asset Uploads

![Recommended formats to upload into Dynamic Media](/help/assets/dynamic-media/assets/dm-upload-formats.png)

**Recommended file formats:** Adobe recommends uploading assets in a **lossless format**. Avoid **JPEG** as a source format because each time you deliver or save a JPEG, image quality degrades due to its lossy compression. Instead, begin with the highest-resolution images in a lossless format. The preferred formats are typically:

- **TIFF** (Tagged Image File Format)
- **PNG** (Portable Network Graphics)

**Color space considerations:** When planning for digital channels or web delivery, the default color space is **RGB (Red, Green, Blue)**, which corresponds to how screens render color using light.

Most users do not consider delivering assets in **CMYK (Cyan, Magenta, Yellow, Key/Black)** or why they would need to. CMYK is the standard color space for printed materials because it corresponds to the inks used in offset and digital printing presses. However, Dynamic Media supports delivery in both color spaces.

Many customers still rely on print production, including:

- **Warehouse wholesale clubs** producing member catalogs
- **Grocery stores** printing weekly flyers and circulars

These customers require their images in both RGB and CMYK. Traditionally, meeting this requirement meant maintaining two separate files: one RGB version and one CMYK version. With Dynamic Media, however, you can upload CMYK assets directly, and Dynamic Media will automatically deliver RGB assets through an image preset or a color profile. This eliminates the need to create and manage multiple versions of the same file, preserving the core principle of **one primary asset file with multiple delivery options**.

### Publish and preview assets

#### Publish assets in Dynamic Media

After you upload assets into Dynamic Media, publish them so they become deliverable to any customer-facing experience. To publish manually:

1. Select the uploaded assets in Dynamic Media.
2. Click **[!UICONTROL Publish]** or **[!UICONTROL Quick Publish]**.

Publishing is required whenever you intend to use assets in any experience, because unpublished assets are not served through Dynamic Media's delivery layer and therefore cannot be referenced from a live web page. Once assets are published, as a result they become available for inclusion in a web page in two ways:

- Copy the **Dynamic Media-generated URL** and reference it directly.
- Copy the **embed code** and paste it into the page markup.

#### Automatic publishing on upload

Beyond the manual workflow, Dynamic Media supports automatic publishing. You can configure Dynamic Media to instantly publish assets at the moment of upload, without any user intervention. This eliminates the manual publish step and shortens the time between ingesting a new asset and having it available for web delivery.

#### Preview asset renditions

After upload, Dynamic Media offers multiple ways to preview an asset's renditions. Previewing shows you what a customer sees before the asset is embedded in production, which helps validate cropping, sizing, viewer behavior, and overall visual quality.

##### Preview with an image preset

A common preview method uses **image presets**:

1. Select an asset in Dynamic Media.
2. Open its **Renditions**.
3. Choose an **image preset** (for example, "Large").

The resulting URL path contains the image preset name (such as "Large") and is the same URL you use in a web page.

![Previewing a rendition of an asset based on the Large image preset](/help/assets/dynamic-media/assets/dm-image-preset-with-url.png)
_Previewing a rendition of an asset based on the selected "Large" image preset. The resulting URL path contains the "Large" image preset name and is used in a web page._

The URL above is live! [Try it](http://s7d1.scene7.com/is/image/jpearldemo/AdobeStock_28563982?$Large$){target="_blank"}.

##### Preview with a viewer preset

Another method to preview an asset uses **viewer presets**, which render the asset inside an interactive HTML5 viewer:

1. Select the image asset.
2. Choose a **Viewers** preset (for example, "ZoomVertical_light").
3. Use the URL and Embed buttons to copy the delivery URL or the embed snippet.

![Previewing an asset based on the Zoom Vertical Light viewer preset](/help/assets/dynamic-media/assets/dm-viewer-preset.png)
_Previewing an asset based on the selected "ZoomVertical_light" viewer preset. The mouse pointer (`+`) was moved over the watch to zoom in. Notice the URL and Embed buttons._

The rendition above is live! [Try it](https://s7d1.scene7.com/s7viewers/html5/ZoomVerticalViewer.html?asset=jpearldemo/AdobeStock_28563982&config=jpearldemo/ZoomVertical_light){target="_blank"}.

## Optional - Learn more

Part I of this documentation covered the fundamentals of Dynamic Media in Adobe Experience Manager, a capability designed to deliver responsive, interactive rich media — including images, sets, and video — across web, mobile, and connected channels. To deepen your understanding of the concepts introduced in Part I, use the curated resources below. These supplementary materials expand on Dynamic Media workflows, configuration, and delivery patterns in greater technical detail. Otherwise, continue with Part II of this documentation. See [What's next in this Dynamic Media Journey](#whats-next).

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

_Dynamic Media tutorials_

* [Use Dynamic Media with Experience Manager Assets](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/dynamic-media-overview-feature-video-use) — feature videos and guided walkthroughs demonstrating how to enable, configure, and apply Dynamic Media capabilities directly within Adobe Experience Manager Assets, including asset ingestion, image presets, and dynamic delivery.
* [Adobe Experience Manager content library](https://experienceleague.adobe.com/?lang=en#recommended/solutions/experience-manager) (search on _Dynamic Media_) — a broader Experience League learning hub where you can filter recommended tutorials, courses, and articles by searching for _Dynamic Media_ to find role-based learning paths for administrators, developers, and marketers.

_Dynamic Media viewers_

* [Live Demos](https://landing.adobe.com/en/na/dynamic-media/ctir-2755/live-demos.html) of each viewer — interactive, working demonstrations of each Dynamic Media viewer type (such as zoom, spin, video, and carousel viewers), useful for evaluating viewer appearance, user interaction, and behavior before implementing them on production sites.

## What's next in this Dynamic Media documentation {#whats-next}

Part II of this documentation continues the Dynamic Media journey with a deeper technical focus on asset delivery and multi-asset viewer experiences. Specifically, Part II covers:

- **Dynamic Media URLs** — a close examination of URL structure and parameters, so you understand exactly what happens behind the scenes when an asset is requested and delivered.
- **Image presets** — the fundamentals of creating presets that dynamically render assets at the size, format, and quality required by each delivery context.
- **Image Sets** — how to create sets that let users view a product or asset from multiple angles or variations within a single interactive viewer.
- **Spin Sets** — how to assemble sequences of images that produce a 360-degree rotational viewing experience.
- **Mixed Media Sets** — how to combine different asset types, such as images, spin sets, and video, into a unified viewer.

Together, these topics build directly on the foundational concepts introduced in Part I and prepare you to configure richer, more interactive Dynamic Media experiences.

Continue to [Dynamic Media: The Basics, Part II](/help/assets/dynamic-media/dm-journey-part2.md#dm-journey-d).

<!-- Live as of April 28 2022. LEAVE IN HERE https://landing.adobe.com/en/na/dynamic-media/ctir-2755/index.html -->