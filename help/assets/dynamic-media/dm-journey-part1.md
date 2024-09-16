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
hide: no
hidefromtoc: no
exl-id: f3472006-d5ae-4f70-af3e-44e73aee85cc
---
# Dynamic Media Journey: The Basics, Part I {#dm-journey-part1}

{{see-also-dm}}

Welcome to the Dynamic Media Journey. 

This journey covers the basics of Dynamic Media, how it works, what it can do for you, and what value it brings to your work and your customers.

**_Prerequisites_**

* Basic understanding of image and video formats
* Basic understanding of HTML and CSS
* Basic understanding of design tools such as Adobe Illustrator, Adobe Photoshop, Adobe XD 
* Access to Dynamic Media on Experience Manager is helpful, but not required

**_What you can expect to learn_**

_Part I_

* What is Dynamic Media and how can it help you?
* Use cases for Dynamic Media
* How an asset flows through the Dynamic Media system

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

Dynamic Media helps you deliver rich visual merchandising and marketing assets on demand. It also helps you create and serve interactive viewing experiences, including zoom, 360-degree spin, and video. Your assets are dynamically scaled for consumption on web, mobile, and social sites. Using a set of primary source assets &ndash; such as images, video, and 3D &ndash; Dynamic Media generates and delivers multiple variations of this rich content, in real time through its global, scalable, performance-optimized CDN (Content Delivery Network).

Dynamic Media incorporates the workflows of the Adobe Experience Manager Assets digital asset management solution to simplify and streamline the digital campaign management process.

### One file with endless possibilities

One of the main points to understand about Dynamic Media is the concept of _One primary asset file with endless possibilities_.

To understand this concept better, think about the way you traditionally work with a single asset, such as an image or a video. You typically create one primary asset. Then, you manually create versions of that same asset for every experience, every device that is needed, every web page, and every property where it is used. With time, that single asset can grow to 20, 30, or more versions, with no version history attached to them. Now, imagine doing that for every image or video that you have. The number of asset versions would quickly become overwhelming to maintain and update, not to mention the increase in storage costs.  

Dynamic Media, however, is fundamentally different from other systems because you use it to deliver your media _dynamically_ from single, primary assets, and from URL calls. The Dynamic Media URL paths that you request include instructions that tell the Adobe publish server how to display the asset when it is delivered to a customer's screen. For example, using the same single primary asset, you can have it delivered instantly in unlimited renditions, changing size, format, resolution, weight, color, crop, and effects such as a zoom view.

This unique delivery method ensures that consistent quality experiences are sent to any screen, regardless of size or bandwidth. Full-size videos are also optimized for all screen types and adaptively streamed to also ensure a consistent, quality user experience.

<!-- As part of building and publishing assets with Dynamic Media, you visually configure the effects that you want to apply to assets. In so doing, you are literally building the URL that correctly tells the publish server how to deliver your primary asset to the screen.  -->

![Adobe Dynamic Media delivers the same primary image to different mediums in different sizes and formats](/help/assets/dynamic-media/assets/dm-oneasset-multioutput.png)
_Adobe Dynamic Media ensures consistent, quality experiences are delivered to any screen, regardless of size or bandwidth._

As you read on, you are going to learn more about why this concept of "one primary asset file, endless possibilities" is important.

### The Content Delivery Network

When you are ready to go live with an image asset or a video asset, it is supported by Dynamic Media's backbone consisting of a powerful, top-tier delivery network. The network serves hundreds of clients around the world every day. The assets are distributed on the Content Delivery Network &ndash; or CDN &ndash; hosted by Akamai. The CDN is a system of computer services networked together that cooperate transparently to deliver content, especially large rich media content, to end users. 

In the CDN system, web content is stored in web caches across the Internet. Then it is delivered from the web cache to end users to make for faster delivery. So, the first time someone downloads a web page, the assets they see are delivered to a CDN cache. They are stored on the server so that the next time someone in the same area accesses the webpage, the same cached content is delivered faster. The content is delivered faster because it is located closer to the user. A CDN makes for faster web page displays, and yet it decreases bandwidth demands on the central server because content is delivered from a cache network, not from a central server in every instance. This optimized flow means a better user experience, leading to increased sales.

<!-- USE AN IMAGE HERE? ![Content delivery network](/help/assets/assets-dm/cdn.png) -->

Historically, the CDN delivers 3.5 petabytes of traffic to customers every month. The system can deliver 52 billion assets in a single day. That number equates to 864,000 images and videos successfully delivered to customers, _every second_.

### Smart Imaging

Dynamic Media already does a great job of optimizing assets and ensuring that each asset loads quickly on mobile and desktop systems, by way of the CDN. To make that happen, image presets are used in Dynamic Media to define the quality of your image. They also define the type of image that you are sending, its sharpness, and other pieces for various parts of your experiences or pages.

But to further add value to Dynamic Media beyond image presets, there is _Smart Imaging_.

Smart Imaging provides even better image asset delivery performance by automatically optimizing an image's format and file size based on a customer's browser capability. It works with your existing image presets (image presets is discussed in Part II of this journey) and uses intelligence at delivery. 

This intelligence further reduces image file size based on browser and network connection speed. Because image assets make up most of a page's load time, the performance improvement can have a thorough impact on key business indicators, such as:

* Higher conversion
* Time spent on site
* Lower site bounce rate

Overall, with smart imaging, you can expect a 22% to 47% performance improvement depending on your existing image preset settings and specific end-user characteristics. All while keeping image quality as if it were never touched.

![Smart Imaging](/help/assets/dynamic-media/assets/dm-smart-imaging.png)
_Smart Imaging automatically optimizes an image's format and file size based on a customer's browser capability and network speed._

Smart imaging is not turned on by default because it requires a coordinated effort between you and Adobe Dynamic Media technical support. Also, enabling Smart Imaging requires a complete clearing of your CDN cache, which is then refilled with time. If you are interested in using Smart Imaging, you can work with Adobe to have it turned on by submitting a technical support ticket. Technical support then gives you a URL parameter that lets you try out, beforehand, smart imaging. You can try it on any of your web pages or images so you can see the performance that you get, and the savings. You can then have smart imaging turned on for your full site.

### Adaptive Video Sets

When there is a video on a page, or a main page, your customers tend to engage with that content longer and stay on the page longer, which is typically a good thing. This behavior is exhibited through analytics that Adobe has done. However, video can be complex. For one thing, you often have a large primary file. It is complicated to determine how to size and deliver video, all to ensure that the experience runs smoothly regardless of the device it is being viewed on, and regardless of bandwidth.

To solve this issue, Dynamic Media gives you the ability to create _Adaptive Video Sets_.

An Adaptive Video Set groups versions of the same video that are encoded at different bit rates and formats.

You start with your original, primary video, which you upload into the system. Dynamic Media automatically sizes, or _transcodes_, that video into multiple videos. Then, at the time of delivery, it intelligently determines which video screen, what quality, and what format to use, and delivers it to either the phone, tablet, or desktop computer.

For example, on an iOS mobile device, it detects a bandwidth such as 4G, 5G, or Wi-Fi. Then, it automatically selects the right encoded video from among the various video bit rates within the Adaptive Video Set. The video is streamed to mobile devices, tablets, or desktop computers.

In addition, video quality is dynamically switched automatically if network conditions change. And, if a customer enters full-screen mode on a desktop, the Adaptive Video Set responds by using a better resolution, improving the customer's viewing experience. 

Using Adaptive Video Sets provides a smooth, high-quality playback for customers playing Dynamic Media video on multiple screens and devices. It truly takes the complexity out of video.

## Use cases for Dynamic Media {#dm-journey-b}

The following are common use-case issues and solutions that Dynamic Media can help you with to drive positive customer engagement, loyalty, conversion, and increased ROI.

### Use case: Primary file approach

One of the most important use cases for Dynamic Media is also one of the most obvious. That is, reducing the weight of pages and experiences, and the size of the content, whether it is an image or a video that is being delivered.

The following shows a typical experience or web page. About 90% of a page is made up of rich media, such as images and videos, which are commonly much heavier files.

![Content page weight](/help/assets/dynamic-media/assets/dm-content-page-weight.png)
_Content page weight of a typical web page._

The remaining 10% is HTML, CSS code, and specific tags. You want to optimize the 90% weight of that page and Dynamic Media helps with that effort. Earlier, you read about the concept of _one primary asset file with endless possibilities_. This approach is significant in reducing overall page weight. The ability to take one primary asset and use it on a product detail page, a thumbnail page, your shopping cart, and your search grid, is a great timesaver. And it ensures consistency across experiences as well.

![Primary file approach](/help/assets/dynamic-media/assets/dm-onefile.png)
_The watch is one primary asset file, but with multiple renditions of it &ndash; not copies &ndash; created on the fly._

Let's look closer at the issues Dynamic Media is solving with the one file and some of the solutions to that approach.

| **Issue** | **Dynamic Media solution** |
|---|---|
| Create and store every asset. | Use a single image file, automatically creating required renditions only at the moment of delivery. |
| High storage costs. | Eliminates the need to create and store multiple copies of an asset. |
| Difficulty maintaining chain of custody. | Guarantees delivery of device-optimized and consistent experiences. |
| No version history. | | 
| Inconsistent brand experiences across devices. | |
| Unnecessary cost of duplicate asset creation. | |

When you think about one file, you are creating an asset for every kind of experience. You might have one starting image, and then you have to create 20, 30, or 40 variations of that image, which you ultimately have to store and pay for that storage.

Then you have to make sure that the right image is used and that may affect your ability to have consistency across your brands. And, if you cannot find an image, you have to go back in and duplicate those assets.

Dynamic Media lets you create variations of images, on the fly, from that one starting image. It lets you be creative with that primary asset and not have to go back and forth with your graphic design artist or photo studio to create additional content. And that is money and time saved.

With the one file approach, you use a single primary file. Then create those versions or renditions that are required across your sites, and properties, and experiences, only at the moment they are delivered or seen by a customer. Such efficiency can greatly decrease the amount of storage needed for your assets, and reduce your overall workflow complexity. And with Dynamic Media's delivery system, it guarantees that every image and video is optimized, loads quickly, and looks great on all screens and devices.

### Use case: Video

Another use case that Dynamic Media solves for is video. Video is complex. It is difficult to manage. Video files are challenging to store and move around because of their inherent file sizes.

| **Issue** | **Dynamic Media solution** |
|---|---|
| Difficult to manage and deliver video optimized for various devices. | Use a single video that automatically sizes for all devices. |
| Videos stall or play in low quality due to user's available bandwidth. | Deliver video through an HTML player that auto-detects available bandwidth and adapts quality to ensure high fidelity and smooth playback. |
| Unfeasible and time-consuming to manually create all versions of a video just to ensure good display and playback across devices. | Eliminate hours of tedious transcoding work with a simplified workflow. |
| | Free up time for higher value work. | 

Customers come to Dynamic Media with the following issues that they are hoping to solve:

"_My business has the video, and the department spent a large amount of money creating it, but shied away from placing it on pages, or delivering it. The reason was because from testing, the quality of the video could not be guaranteed, or even if it was really going to play. And ultimately, that affects the business's brand and potentially its role to conversion._"

Dynamic Media's solution is to take that one primary video file, and let Dynamic Media make all the sizes through its transcoding process. Then, pair that with Dynamic Media's intelligent video player. This workflow guarantees that whether you are using that video on your main landing page, or on a category or product detail page, it is going to be consistent throughout and delivered with high quality.

Here are several more use cases to consider.

### Use case: Single source of truth

| **Issue** | **Dynamic Media solution** |
|---|---|
| Digital assets scattered across the organization, siloed in different teams or business units. | Store and manage all digital assets in a central location. |
| Team members download and create local versions. | Team members use a single primary file to create _and_ deliver all necessary versions across various screen sizes and devices. |
| Single-use assets created for every experience and device. | Eliminates single-use assets, saving time and money creating them. |

### Use case: AI-powered Smart Cropping for rich media

| **Issue** | **Dynamic Media solution** |
|---|---|
| Time-consuming and labor intensive to manually draw, measure, and cut images or videos to highlight the focal point and display appropriately across all screen sizes and devices. | Uses Smart Crop in Dynamic Media, an Adobe Sensei AI capability, to automatically detect the focal point in any image or video, and crop to maintain it. |
| Time lost that could be better spent creating high-impact experiences. | Captures the intended point of interest regardless of screen size. |
| Single-use assets created for every experience and device. | Eliminates tedious manual tasks and delivers high-quality, fast-loading imagery and video that looks good on any device or screen. |

### Use case: Interactive media authoring

| **Issue** | **Dynamic Media solution** |
|---|---|
| Flat and static customer experiences that do not engage, engender loyalty, or drive conversion. | Enables non-technical users to easily and seamlessly dd interactive elements like hot spots, carousels, and spin sets for more dynamic and engaging experiences. |
| Limited return on investment from digital assets and lackluster customer experiences. | Drives conversion and return on investment from rich media experiences. |

## How an asset flows through the Dynamic Media system {#dm-journey-c}

The following shows a typical workflow for Dynamic Media.

![Dynamic Media workflow](/help/assets/dynamic-media/assets/dm-workflow.png)
_How an asset flows through the Dynamic Media system._

You begin with the creation phase with the main goal to have your primary asset at the end. These primary assets could come from photo shoots, from video vendors, or it could be some audio files that you have had created. You can use Adobe's Creative Suite applications such as Adobe InDesign, Adobe Photoshop, Adobe Illustrator to help you work out the content. 

When the creation part is finished, you put the asset into the Authoring solution by uploading the asset into Dynamic Media. Within Dynamic Media, you make sure that you have the right image presets and viewers lined up for your various web pages on your site.

And ultimately, you optimize all of that content and publish it to Dynamic Media servers so that it is available for web, print, email, desktops, and mobile devices.

### Uploading assets into Dynamic Media

When you finish creating a primary asset, you upload it into Dynamic Media. The type of file you upload, and the format and size of the file are important attributes to Dynamic Media. It is at the time of upload that you want to make sure you get the maximum value out of the one file support.

For example, the watch image below is 4560 x 3020 pixels. And while you may never use an image that size, you can still upload it. The larger the image, the better the quality that Dynamic Media can deliver, even down to a thumbnail rendition. Remember: you can easily _decrease_ the resolution of an existing image. But if you try to _increase_ the resolution of an image, the result is likely going to be unsatisfactory.

![Recommended formats to upload into Dynamic Media](/help/assets/dynamic-media/assets/dm-upload-formats.png)
_Considerations for asset uploads._

Adobe recommends that you upload assets in a lossless format. Generally, it is best to avoid JPEG because when you deliver JPEG or when you continue to save JPEG, you start to lose image quality over time. You want to start with the highest resolution images in a lossless format that you can live with. That format is typically a TIFF or PNG file.

Regarding color space, when you think about a digital channel or web view, you typically think about RGB (Red, Green, Blue).

Most would never think about delivering something in CMYK or why you might even want to deliver in CMYK. The reason is because that color space is most often used for delivering printed items. But, Dynamic Media can deliver in both color spaces.

There are many customers who still do print, such as warehouse wholesale clubs. And there are grocery stores who often print flyers on a weekly basis. Such customers require that their images be in both color spaces. Traditionally, that would require two different images: one in RGB and one in CMYK. However, you can upload CMYK assets directly into Dynamic Media, and have Dynamic Media deliver RGB assets through an image preset, or through a color profile, automatically. There is no need to create multiple versions of a file, thus maintaining the concept of _one primary asset file with endless possibilities_.

<!-- **The Value of Renditioning??? or Demo portion** -->

### Publish and preview assets

After you upload assets into Dynamic Media, it is a good practice to _publish_ them by selecting the assets, and then clicking **[!UICONTROL Publish]** or **[!UICONTROL Quick Publish]** in Dynamic Media. Publishing assets is necessary if you intend to use them in any experience. After assets are published, they are available to you for including in a web page using a Dynamic Media-generated URL that you copy, or by way of embedding code on the page.

Besides manually publishing assets, you can configure Dynamic Media so that you instantly publish assets - without any user intervention - at the time of upload.

Following upload, there are different ways to preview an asset's renditions in Dynamic Media. Previewing renditions can help give you an idea of what a customer sees. A common preview method is to select an asset and then view its Renditions by selecting an _image preset_ as seen in the following.

![Previewing a rendition of an asset based on the Large image preset](/help/assets/dynamic-media/assets/dm-image-preset-with-url.png)
_Previewing a rendition of an asset based on the selected "Large" image preset. The URL button was clicked. The resulting URL path contains the "Large" image preset name and can be used in a web page._

The URL above is live! [Try it](http://s7d1.scene7.com/is/image/jpearldemo/AdobeStock_28563982?$Large$){target="_blank"}.

Another method to preview an asset is to select the image asset and then select a _Viewers_ preset as seen in the following.

![Previewing an asset based on the Zoom Vertical Light viewer preset](/help/assets/dynamic-media/assets/dm-viewer-preset.png)
_Previewing an asset based on the selected "ZoomVertical_light" viewer preset. The mouse pointer (`+`) was moved over the watch to zoom in. Notice the URL and Embed buttons._

The rendition above is live! [Try it](https://s7d1.scene7.com/s7viewers/html5/ZoomVerticalViewer.html?asset=jpearldemo/AdobeStock_28563982&config=jpearldemo/ZoomVertical_light){target="_blank"}.

## Optional - Learn more

Part I of this journey covered the basics of various Dynamic Media topics. If you want to learn more about what you read, use the materials below to explore concepts in greater detail. Otherwise, you can continue with Part II of your journey. See [What's next in this Dynamic Media Journey](#whats-next). 

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
* [Work with Selective Publish in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md) -->

_Dynamic Media tutorials_

* [Use Dynamic Media with Experience Manager Assets](https://experienceleague.adobe.com/docs/experience-manager-learn/assets/dynamic-media/dynamic-media-overview-feature-video-use.html)
* [Adobe Experience Manager content library](https://experienceleague.adobe.com/?lang=en#recommended/solutions/experience-manager) (search on _Dynamic Media_)

_Dynamic Media viewers_

* [Live Demos](https://landing.adobe.com/en/na/dynamic-media/ctir-2755/live-demos.html) of each viewer

## What's next in this Dynamic Media Journey {#whats-next}

In part II on this journey, you closely examine Dynamic Media URLs to better understand what is going on when an asset is delivered. You also learn more about the fundamentals behind creating image presets to render assets, and learn about Image sets, Spin sets, and Mixed Media sets and how they are created. 

Take me to [Dynamic Media Journey: The Basics, Part II](/help/assets/dynamic-media/dm-journey-part2.md#dm-journey-d).

<!-- Live as of April 28 2022. LEAVE IN HERE https://landing.adobe.com/en/na/dynamic-media/ctir-2755/index.html -->