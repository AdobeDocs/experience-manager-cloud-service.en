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
exl-id: 39e491bb-367d-4c72-b4ca-aab38d513ac5
---
# Dynamic Media best practices{#about-dm-best-practices}

<!--**Organizations today must connect with their customers through an ever-growing array of channels and devices.** The customer experience spans physical stores, websites, mobile apps, social media, email, and e-commerce platforms. This diversity requires organizations to create many more versions of each piece of content. Personalization adds complexity by increasing the number of variations needed for each item. Despite budget constraints for content creation, there's still a need to produce more campaigns in the same timeframe, on a global scale. AEM Dynamic Media offers a comprehensive set of tools to meet these challenges, providing consistent, personalized, high-performance, and optimized brand experiences across all channels and devices. 

Key Features of AEM Dynamic Media:

* **Single File Approach:** Save on storage costs by storing just one master file. AEM Dynamic Media generates all size variations and visual effects on-demand, at the time of delivery, eliminating workflow complexity and last-minute creative changes.
* **Global Reach:** With Smart Imaging, images are automatically optimized during delivery, significantly reducing file size and page weight without sacrificing visual quality. This optimization is tailored for network bandwidth and device pixel ratio.
* **AI-Powered Efficiency:** Smart Crop uses AI to automate the cropping of images and videos, focusing on points of interest. This feature saves countless hours of manual editing and is designed for large-scale enterprise production.
* **Video Made Simple:** Upload a master video file and AEM Dynamic Media will adaptively stream it in multiple languages and with descriptive audio, ensuring a broad reach.
* **Customizable Experience Viewer:** Select, customize, and brand the experience viewers for images and videos with ease. These viewers can be seamlessly integrated into any digital experience.
* **Support for Emerging Formats:** AEM Dynamic Media is also your solution for delivering immersive 3D and panoramic experiences.

In the accompanying guide, you'll find a comprehensive list of best practices for maximizing the benefits of AEM Dynamic Media. As you embark on your Dynamic Media journey, make sure to consult these expert recommendations and resources.

Stage Business Problem Best Practice Recommendation: This section will outline specific business challenges and provide targeted best practices and recommendations to address them effectively. -->

{{see-also-dm}}

Organizations face an explosion of channels and devices for engaging with users. The customer journey spans physical stores, web, mobile, social media, emails, and commerce. To meet this demand, Dynamic Media on Adobe Experience Manager (AEM) offers a comprehensive solution. It optimizes asset delivery, handles personalization, and ensures consistent, performant, and brand-aligned experiences across channels and devices. 

Some of the key tenets of Dynamic Media include the following:

* **Single file approach:** With Dynamic Media, you store one primary source file, and all size variations and visual effects are dynamically created and optimized at the time of delivery. This approach saves storage costs and eliminates workflow complexity.
* **Truly global:** Smart Imaging, applied during content delivery, significantly reduces image size and page weight without compromising visual quality. It's optimized for network bandwidth and device pixel ratios.
* **AI powered:** Smart Crop, an AI-driven feature, automates image and video point-of-interest cropping. It eliminates manual effort and scales efficiently for enterprise use.
* **Easy video:** Upload primary source videos into Dynamic Media and stream them adaptively across multiple languages with descriptive audio.
* **Experience viewer library:** Customize and brand experience viewers for images and videos. These viewers seamlessly integrate into your digital experiences.
* **Emerging format support:** Dynamic Media enables the delivery of 3D and panoramic experiences.

As you explore the [Dynamic Media Journey](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dm-journey/dm-journey-part1), reviewing the consolidated list of best practices below can help you make the most of its capabilities. Adapt these Dynamic Media best practices to your specific context and project requirements so you can optimize your experiences across channels and devices. 

<!-- In Dynamic Media on AEM, there are sets of methods, techniques, and guidelines that can help you maximize the potential of your rich media content. These best practices can lead to optimal results and increase efficiency in your use of Dynamic Media. They represent the most efficient and effective courses of action in a particular situation. They also unlock high value for your audience and deliver high-quality, engaging content. -->

>[!IMPORTANT]
>
>The Dynamic Media best practices in this article may evolve over time as new technologies in Dynamic Media emerge. The information below is current for the latest version of Dynamic Media.


## Ingest assets into Dynamic Media

**Business case:** *Efficiently manage large volumes of assets and ensure that only relevant, approved content is delivered to end users.*

Streamline your management of large numbers of assets efficiently. Ensure that only the appropriate, authorized content reaches your end-users by using Dynamic Media's **Selective Sync** and **Selective Publish** features.

* **Selective sync:**
A proactive feature that lets you choose which assets to sync with Dynamic Media. For example, you might decide to sync only those folders containing assets that have received final approval. This workflow helps you maintain control over which assets are being prepared for delivery to your customers.

* **Selective publish:**
After syncing your assets, Selective Publish gives you control over which assets are visible to your customers. This ability means you can govern which approved assets are actually delivered through your channels, ensuring that your customers see only the best and most relevant content.

These two best practices help you achieve better control, governance, and productivity over your rich-media content. 

Want to learn more? Go to [Configure Selective Publish at the folder level in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md).


## Dynamic Media Viewers

Dynamic Media Viewer best practices are essential guidelines designed to optimize the performance, functionality, and user experience of Dynamic Media assets on AEM. These practices ensure that assets are properly synchronized, published, and configured to use the full capabilities of Dynamic Media. 

By following these best practices, you can achieve seamless integration, efficient asset management, and enhanced viewer interactions. Synchronizing assets, using smart cropping, and adhering to JavaScript file inclusion guidelines are all important practices. These recommendations help maintain the integrity and reliability of media delivery across various platforms and devices.

* **Synchronize Viewer Assets:**
Ensure that all viewer assets are synchronized with Dynamic Media before using the player. 

  * Access the sample manager page at `/libs/dam/gui/content/s7dam/samplemanager/samplemanager`. This page lets you resynchronize a viewer's assets, including out-of-the-box icons, CSS files, and presets.
  * If you encounter any viewer issues, go to the [Troubleshoot Dynamic Media Viewers](/help/assets/dynamic-media/troubleshoot-dm.md#viewers) article. 

* **Publish Assets:**
Make sure that assets are published before viewing them in delivery viewers.
* **Autoplay Videos Muted:**
For autoplay functionality in videos, use muted video settings because browsers restrict playing videos with volume.
* **Smart Cropping:**
Use the Image v3 component for smart cropping to enhance image asset presentation.
* **JavaScript File Inclusion:**
Only include the primary viewer JavaScript file on your page. Avoid referencing additional JavaScript files that the viewer's runtime logic may download. Specifically, do not directly link to the HTML5 SDK `Utils.js` library from the `/s7viewers` context path (known as consolidated SDK include). The viewer's logic manages the location of `Utils.js` or similar runtime viewer libraries, which can change between releases. Adobe does not retain older versions of secondary viewer includes on the server, so directly referencing them can break viewer functionality in future updates.
* **Embedding Guidelines:**
Use the documentation for embedding guidelines that are specific to each viewer. 
Want to learn more? Go to [Viewers for AEM Assets](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/library/viewers-aem-assets-dmc/c-html5-s7-aem-asset-viewers).
* **SDK Tutorial and Examples:**
Review the [Viewer SDK Tutorial](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/library/c-tutorial) and [HTML5 SDK application examples](https://s7d9.scene7.com/s7sdk/2024.5/docs/jsdoc/index.html) for a thorough understanding of SDK component APIs.


## Prepare assets for delivery

### Organize your assets

**Business case:** *Efficiently organize assets to streamline workflows.*

For efficient asset organization that streamlines workflows, use one or more of the following best practices: 

* **Organize assets in folders:**
Organizing assets effectively involves categorizing them into folders, similar to file organization on a computer. Proper naming, structuring subfolders, and file management within these folders are crucial for efficient asset processing. Implementing systematic naming conventions and metadata practices maximizes the utility of your digital asset repository.
Want to learn more? Go to [Organize assets in folders](/help/assets/organize-assets.md#organize-using-folders).
* **Organize assets using tags:**
Tagging assets enhances searchability, collection creation, and search ranking. Adobe Sensei's AI employs a self-learning algorithm for precise tagging, enabling quick asset retrieval. Adobe Sensei also recognizes and assigns relevant tags&ndash;including custom ones&ndash;to assets, simplifying asset management with automatic, descriptive tagging.
Want to learn more? Go to [Organize assets using tags](/help/assets/organize-assets.md#use-tags-to-organize-assets).
* **Organize assets as collections:**
Dynamic Media along with Experience Manager Assets allows for the efficient creation, editing, and sharing of asset collections among users. You can establish various collection types, including static lists and dynamic, search-based compilations. These collection types can be shared across diverse locations with customizable access and editing rights.
Want to learn more? Go to [Organize assets as collections](/help/assets/manage-collections.md).
* **Organize assets using profiles:**
A processing profile automates asset handling in designated folders, streamlining organization. Standardizing metadata, file names, and folder structures allows for consistent and precise application of these profiles as your digital asset collection expands.
Want to learn more? Go to [Organize assets using profiles](/help/assets/organize-assets.md#organize-to-use-profiles).

 

### Optimize the quality of images

**Business case:** *Obtain good quality images from Dynamic Media.*

Enhancing image quality requires careful consideration of various factors. It can be a time-intensive process. However, there are some tried-and-true practices that can help you achieve desirable results. Some of those best practices include how to obtain optimal image sizing, image sharpening, and the best image formats to use.

Want to learn more? Go to [Best practices for optimizing the quality of your images](/help/assets/dynamic-media/best-practices-for-optimizing-the-quality-of-your-images.md).

Because perception of image quality varies from person to person, sometimes a systematic approach to experimentation is essential for achieving desirable results. Adobe Experience Manager aids this process with more than 100 Dynamic Media commands for image enhancement.

Want to learn more? Watch [Dynamic Media Snapshot](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-snapshot) (3 minutes, 17 seconds).

To assess these different commands' impact on image quality, you can upload an image to Dynamic Media, use the tool's interface at the specified URL, and apply the commands you want to try out. 

Want to try it? Launch [Dynamic Media Snapshot](https://snapshot.scene7.com/)

### Standardize on styles applied to images

**Business case:** *Efficiently standardize the style and transformation applied to my image assets.*

Use Image Presets regularly in Dynamic Media so you can consistently and dynamically adjust image sizes, formats, and properties. Think of an Image Preset as a macro: it's a named set of commands for sizing and formatting. For example, if your site needs product images in various sizes and formats, with specific compression for desktop and mobile, Image Presets automate this process efficiently.

Want to try it? Go to [Fundamentals of creating image presets to render assets](/help/assets/dynamic-media/dm-journey-part2.md#dm-journey-e)

### Adjust the focus and framing of images and videos

**Business case:** *Ensure that the main point of interest of my images or videos remains in focus across devices.*

Smart Crop is a feature in Dynamic Media that uses Adobe Sensei, Adobe's AI and machine learning framework, to automate the cropping of images and videos. It intelligently detects and focuses on the main subject or point of interest in an image or video. This intelligence ensures that the focal point is maintained across various screen sizes on desktop computers and mobile devices.

A best practice is to create an Image Profile with Smart Crop. In the profile, you can define various screen sizes and let Adobe Sensei do the rest, ensuring that your images and videos are always optimized for the viewer's device.

Want to learn more? Watch [Using Smart Crop with AEM Assets Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use) (6 minutes, 35 seconds) and [Using Dynamic Media Smart Crop for Video](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/video/dynamic-media-smart-crop-video) (6 minutes, 22 seconds).

### Improve SEO rankings

**Business case:** *Configure Dynamic Media to get improved SEO rankings.*

Use the following recommendations regularly to ensure that your images contribute effectively to your overall SEO strategy.

* **Meaningful image file names:**
Use descriptive file names that reflect the image content. For example,

  * use `myCompany-Silver-Wrist-Watch`
  * *avoid* `myCompany_Silver_Wrist_Watch` or `myCompanySilverWristWatch`

  Doing so helps search engines understand the image context and improves SEO. Google prefers hyphens over underscores or spaces in a file name. Also, avoid concatenating words in a file name.
* **Custom domain:** 
Implement a custom domain that includes your company or brand name to reinforce brand recognition and trust. For example,

  * use `http://images.mycompany.com/is/image/companyname/`
  * *avoid* `https://s7d1.scene7.com/is/image/folder/AdobeStock_28563982`

* **SEO-friendly folder structure:**
Organize your images in a folder structure that includes your company name or brand for better indexing, like `http://images.mycompany.com/is/image/companyname/`.
* **Dynamic Media rule sets:**
Learn how you can conditionally transform URLs based on various factors, enhancing SEO and user experience.
Want to learn more? Go to [Use rule sets to transform URLs](/help/assets/dynamic-media/using-rulesets-to-transform-urls.md).
* **Smart Imaging and Smart Crop:**
Use Smart Imaging and Smart Crop features in Dynamic Media to serve optimized and responsive images. Doing so not only improves page load times but also contributes positively to SEO rankings.
Want to learn more? Go to [Smart Imaging](/help/assets/dynamic-media/imaging-faq.md), or watch [Using Smart Crop with AEM Assets Dynamic Media](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use) (6 minutes, 35 seconds).

Remember, these best practices align well with Google's image SEO best practices. Such practices emphasize the importance of providing context and clarity to search engines through proper naming conventions, structured data, and optimized image delivery. 

Want to learn more? Go to [URL structure best practices for Google](https://developers.google.com/search/docs/crawling-indexing/url-structure) and [Google image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)

### Dynamically enhance images and create visual effects using commands

**Business case:** *Apply rich visual effects to images.*

Dynamic Media offers a suite of commands for enhancing images and creating visual effects dynamically, without the need for multiple static assets. The following are some brief explanations of a few of these processes and some examples to guide you:

#### Effects inside the source image

| Task | What to do |
| --- | --- |
| **Upload and publish your original image** | <ul><li> Start by uploading the original image to Dynamic Media.</li><li> Make sure that it is published and accessible through a URL.</li><li> In this example, a stock image of a watch with a white background (let's call it "Image X") is uploaded to Dynamic Media.<br>[https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer](https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer)</li></ul> |
| **Create a mask** | <ul><li> Develop a mask that defines the subject (the area where you want to apply effects) and the background (the area you want to change).<br>[https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer-maskps](https://s7g2.scene7.com/is/image/genaibeta/watch-silver-offer-maskps)</li><li> Masks are typically grayscale images, where white represents the subject, and black represents the background. You can create masks using tools like Adobe Photoshop.<br>Want to learn more? Go to [Creating and editing a quick mask in Photoshop](https://helpx.adobe.com/in/photoshop/using/create-temporary-quick-mask.html).</li><li> For "Image X," create a mask that precisely outlines the subject you want to enhance. For example, a person, an object, and so on.</li></ul> | 
| **Apply Dynamic Media URL commands for effects** |  After you have your mask, use URL commands to apply effects like an outer glow or change the background color to "Image X." Here are two examples:<ul><li> **Outer glow effect:**<br>To add an outer glow effect along the subject's boundary, edit the URL like this:<br>[https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&effect=-1&pos=100,100&op_blur=75&op_grow=1&opac=25](https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&effect=-1&pos=100,100&op_blur=75&op_grow=1&opac=25)<br>In this URL, the `op_blur`, `op_grow`, and `opac` parameters create the outer glow effect.</li><li> **Background color change:**<br>To change the background color, use the URL with a different background color value:<br>[https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&maskUse=invert&color=255,255,0](https://s7g10.scene7.com/is/image/genaibeta/watch-silver-offer?mask=watch-silver-offer-maskps&maskUse=invert&maskUse=invert&color=255,255,0)<br> In this example, `color=255,255,0` sets the background color to yellow. Edit the background to a specific color for visual impact.</li></ul> |

#### Add an image border

Dynamic Media lets you manipulate images directly through URLs, making it a powerful tool for creating dynamic digital experiences. The following are some examples. Let's start with the following original image URL: [https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel).

| Task | What to do |
| --- | --- |
| **White border** | To add a white border, use the following URL:<br>[https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10)<br>In this URL, the `extend=10,10,10,10` parameter specifies the border size of ten pixels on all sides. | 
| **Blur along the white border** | To add a blur effect along the white border, you can edit the URL as follows:<br>[https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&op_blur=60&color=0,0,0](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&op_blur=60&color=0,0,0)<br>In this URL, the `effect=-1` parameter applies the blur effect, and `op_blur=60` controls the blur intensity. |
| **Drop shadow effect along the outer boundary** | To add a drop shadow effect along the outer boundary, use this URL:<br>[https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&$shadow$&color=0,0,0](https://s7g2.scene7.com/is/image/genaibeta/ocean-facing-hotel?size=400,400&extend=10,10,10,10&effect=-1&$shadow$&color=0,0,0)<br>The `$shadow$` parameter creates the shadow effect, and `color=0,0,0` sets the shadow color to black.  |

Feel free to experiment with these URLs to achieve the desired visual effects.

#### Create image overlays

If you are looking to superimpose a logo or icon on an existing image, Dynamic Media provides a straightforward way to achieve this using URL commands. Let's break down the steps.

| Step | What to do |
| --- | --- |
| **Upload and publish the base image** | First, upload and publish the base image on which you want to superimpose the logo or icon. You can use any image as your base.<br>For example, here is a base image:<br>[https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa](https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa). | 
| **Upload and publish the logo or icon image** | Next, upload and publish the image that you want to superimpose over the base image. This image should be a transparent PNG with the logo or icon you want to overlay.<br>Here is the transparent PNG image of a star object with transparency effects that is going to be superimposed:<br>[https://s7g2.scene7.com/is/image/genaibeta/decorate-star](https://s7g2.scene7.com/is/image/genaibeta/decorate-star) |
| **Apply the Dynamic Media URL** | Now, create a Dynamic Media URL that combines the base image and the logo or icon image. You can use URL commands to achieve this effect.<br>The URL structure looks something like this:<br>[https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa?layer=1&src=decorate-star&scale=1.25&posN=0.33,-.25&fmt=png](https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa?layer=1&src=decorate-star&scale=1.25&posN=0.33,-.25&fmt=png)<br>where the asset<ul><li> `hotspotRetailBaseImage` is the base image.</li><li> `starxp` is the logo/icon image.</li><li> `layer=1` specifies that the logo or icon should be layered over the base image.</li><li> `scale=1.25` adjusts the size of the logo/icon.</li><li> `posN=0.33,-.25` determines the position of the logo/icon relative to the base image.</li><li> `fmt=png` ensures that the output is in PNG format.</li></ul> |

What to learn more? Go to [src](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/r-src) for more details on the `src` command and other Dynamic Media URL commands.


#### Overlaying promotional text

The following are the steps for overlaying a promotional text message on an image using HTML and CSS.

| Step | What to do |
| --- | --- |
| **Upload and publish the base image** | First, upload and publish the base image on which you want to superimpose the text. You can use any image you like. For example, here's a sample base image:<br>[https://s7g2.scene7.com/is/image/genaibeta/leather-sofa](https://s7g2.scene7.com/is/image/genaibeta/leather-sofa)<br> |
| **Apply Dynamic Media text operators** | Using Dynamic Media, you can apply text operators to overlay dynamic text directly onto the image. The following sample URL demonstrates this ability:<br>[https://s7g10.scene7.com/is/image/genaibeta/leather-sofa?layer=1&posN=-0.3,-0.455&text=%7b\rtf1\ansi%7b\fonttbl%7b\f0+Arial;%7d%7d%7b\colortbl+\red255\green255\blue255;%7d\copyfit1000\vertalc\qc%7b\cf0\fs42+New+Collection%7d%7d&size=370,70&textAttr=130&bgcolor=FF3333&wid=600&hei=600](https://s7g10.scene7.com/is/image/genaibeta/leather-sofa?layer=1&posN=-0.3,-0.455&text=%7b\rtf1\ansi%7b\fonttbl%7b\f0+Arial;%7d%7d%7b\colortbl+\red255\green255\blue255;%7d\copyfit1000\vertalc\qc%7b\cf0\fs42+New+Collection%7d%7d&size=370,70&textAttr=130&bgcolor=FF3333&wid=600&hei=600) |

#### Resizing and cropping for various use cases

##### Image resizing basics

Image resizing involves altering an image's dimensions, resolution, and file size. Here are some key points to consider:

* **Pixel composition:**
Digital images consist of tiny dots called pixels. When an image is created, it has a specific number of pixels. Resizing involves adding or subtracting pixels to change the image's dimensions, resolution, and file size.
* **Aspect ratio:**
Maintaining the aspect ratio (the relationship between width and height) is crucial to prevent distortion. Whether you're making an image larger (upscaling) or smaller (downscaling), preserving the aspect ratio ensures visual consistency.
* **Quality considerations:**
Resizing can impact image quality. Avoid drastic upscaling, as it may lead to pixelation. Instead, consider reproducing the image at a larger size and resolution. For smaller images, use the appropriate tools to maintain resolution.

##### Cropping versus resizing

Cropping and resizing are techniques in Dynamic Media that let you transform images to suit various use cases, whether it's creating thumbnails, product display images, or banners.

* **Cropping:**
Involves removing part of an image to alter its composition and framing. It does not change the overall dimensions but focuses on a specific area.
* **Resizing:**
Adjusts the entire image's dimensions, resolution, and file size while maintaining the aspect ratio.

Let's explore a use case that involves the following living room image:

* **Original living room image:**
    [https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa](https://s7g2.scene7.com/is/image/genaibeta/decorative-room-sofa)
* **Thumbnail (200 px x 200 px):**
        A smaller version suitable for quick loading or display.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&fit=crop)
* **Thumbnail with crop (200 px x 200 px):**
        Cropped to focus on the sofa area.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&cropN=.24,.24,.6,.72&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=200&hei=200&cropN=.24,.24,.6,.72&fit=crop)
* **Product display image (800 px x 600 px):**
        Cropped and resized for showcasing the sofa.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=800&hei=600&cropN=.24,.24,.6,.72&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=800&hei=600&cropN=.24,.24,.6,.72&fit=crop)
* **Banner (1720 px x 820 px):**
        Derived from the original image, emphasizing the room.
        [https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=1720&hei=820&cropN=0,.1,1,1&fit=crop](https://s7g10.scene7.com/is/image/genaibeta/decorative-room-sofa?wid=1720&hei=820&cropN=0,.1,1,1&fit=crop)

Feel free to explore these variations for your specific needs.
Want to learn more about the commands available within a URL? Go to [Command reference](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/c-command-reference).

### Deliver GIF images

**Business case:** *Stream GIFs using Dynamic Media*

You can upload and deliver GIFs through Dynamic Media. To render an animated GIF, replace `is/image` with `is/content` in the URL. For example, if you uploaded `abc.gif`, use the following:

* This URL path renders a static view of the GIF:

  ```
  https://your.domain.com/is/image/yourfolder/abc
  ```

* This URL path renders the animation view of the GIF:

  ```
  https://your.domain.com/is/content/yourfolder/abc
  ```

>[!NOTE]
>
>When using `is/content` in the URL path, image transformation commands are not applied to the asset.

### Publish a video for my website

**Business case:** *Quickly publish a video for a marketing site.*

* **Select a video profile:** 
  First, in Dynamic Media, you should select a suitable video profile. You can opt for the *Adaptive Video Encoding* profile available in AEM Assets under Video Profiles. These pre-defined encoding settings ensure that your video is optimized for playback across various devices and bandwidth conditions. Alternatively, you can create your own Adaptive Video profile.
* **Assign the profile:**
  Assign the chosen video profile to the folders where your video is going to be uploaded. This step ensures that the correct encoding settings are applied during the upload process.
* **Upload the original video:**
  Upload the original video file. Make sure it's a high-resolution video with good quality. The better the source video, the better the final result.
* **Preview and publish:**
  Preview the video so you can ensure that everything looks as expected. Once satisfied, go ahead and publish it. This step makes the video accessible to your audience.
* **Link or embed:**
  After publishing, you have two options.

    * **Link directly:**
    Use the provided URL to link directly to the video. Hyperlink it appropriately on your marketing site.
    * **Embed the video:**
    Copy the embed code provided and paste it into the HTML of your web page where you want the video to appear. Doing so allows the video to play directly on your site.

Want to learn more? Go to [Video](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/video). 

### Configure videos for optimal quality and engagement

**Business case:** *Set up videos for the best quality and engagement.*

To ensure the best quality and engagement for your videos, consider implementing a combination of the following best practice strategies:

* **Use the built-in HTML5 Video Viewer:**
        The Dynamic Media HTML5 Video Viewer Presets are robust video players. Use them to avoid common issues associated with HTML5 video playback and mobile devices.
        These presets address challenges like adaptive bitrate streaming delivery and limited desktop browser reach.
        Want to learn more? Go to [Best practice: Using the HTML 5 video viewer](/help/assets/dynamic-media/video.md#best-practice-using-the-html-video-viewer).

* **Use Dynamic Media Video Profiles:**
        Video profiles in Dynamic Media help with efficient video management, consistent quality, and adaptive streaming.
        Want to learn more? Go to [Dynamic Media Video Profiles](/help/assets/dynamic-media/video-profiles.md).

* **Follow Best Practices for Video Encoding:**
        Apply video encoding profiles that maintain the original video quality without excessive downscaling during encoding.
        Want to learn more? Go to [Best practices for encoding videos](/help/assets/dynamic-media/video.md#best-practices-for-encoding-videos).

* **Adopt adaptive streaming instead of progressive streaming:**
        Adaptive streaming adjusts video quality based on the viewer's Internet connection speed and device capabilities.
        It uses protocols like HLS (HTTP Live Streaming) or DASH (`Dynamic Adaptive Streaming over HTTP`) to ensure optimal playback quality.
        Unlike progressive streaming, which delivers videos linearly, adaptive streaming minimizes buffering and offers a seamless viewing experience.

### Internationalizing videos for multilingual consumption

**Business case:** *Make videos ready for multilingual consumption.*

Internationalizing videos for multilingual consumption is essential for reaching a global audience. Dynamic Media provides features that can help you achieve this goal.

* **Upload your videos:**
     * First, create a video encoding profile. You can either use the predefined Adaptive Video Encoding profile that comes with Dynamic Media or create your own custom profile.
     * Associate the video processing profile with one or more folders where you upload your primary source videos.
     * Upload your primary source videos to these folders. Dynamic Media encodes them based on the assigned video processing profile.
     * Dynamic Media primarily supports short-form videos (up to 30 minutes) with a minimum resolution greater than 25 &times; 25. Video files up to 15 GB each can be uploaded1.

* **Manage your videos:**
     * Organize, browse, and search video assets within AEM.
     * Preview and publish video assets.
     * View the source video and its encoded renditions along with associated thumbnails.
     * Edit video properties such as title, description, and tags2.

* **Localization:**
     * For each target geography/language, create audio tracks and subtitles.
     * Add these audio and subtitle tracks to your videos from the AEM interface.
     * As users play the videos, they can select their preferred language for audio and subtitles.

* **Publishing:**
     * If you are using AEM as your Web Content Management (WCM) system, you can directly add videos to your web pages.
     * If you are using a third-party WCM system, you can link or embed videos on your web pages using URLs or embed codes.

Want to learn more? Go to [About multiple caption and audio track support for videos in Dynamic Media](/help/assets/dynamic-media/video.md#about-msma) or watch [Add multiple captions and audio tracks to a video](https://delivery-p106302-e1008131.adobeaemcloud.com/adobe/assets/urn:aaid:aem:daf9a222-9f7f-4333-b167-98cb4c63a1f8/play) (1 minutes, 41 seconds). 


## Deliver assets to customers

### Optimize image sizes and minimize page load times

**Business case:** *Optimize the size of images for any browser or screen and reduce page load time.*

Dynamic Media Smart Imaging is a powerful tool that enhances image delivery performance by automatically optimizing the image's format, size, and quality based on the client's browser capabilities. 

Adobe recommends that you use Smart Imaging's capabilities rather than manually setting the image format to `webp` or `avif`. Here's why:

* **Browser compatibility:**
  Smart Imaging ensures that the delivered image format is compatible with the user's browser.
* **Optimal compression:**
  It selects the best format for compression based on the specific browser, network conditions, and screen resolution.
* **Modern formats:**
  While `avif` is a newer format offering better compression, it is not universally supported across all browsers yet.
* **Best practices:**
  To guarantee the best web-optimized format, you can trust Smart Imaging to make the format selection rather than manually using the commands `fmt=webp` or `fmt=avif`.

By relying on Smart Imaging, you can ensure that your images are delivered in the most efficient manner possible, tailored to each user's browsing environment. This approach simplifies the process and can lead to improved performance in terms of image loading times and overall user experience.

Want to learn more? Go to [Smart Imaging](/help/assets/dynamic-media/imaging-faq.md).

### Post delivery of assets to customers

**Business case:** *After publishing new content or overwriting existing content, how can it be ensured that the changes appear immediately on the CDN?*

The CDN (Content Delivery Network) caches Dynamic Media assets for quick delivery to customers. When updates are made to these assets, it is important for the changes to take effect immediately on the website. By purging or invalidating the CDN cache, assets delivered by Dynamic Media can be updated quickly. This approach eliminates the need to wait for the cache to expire based on the TTL (Time To Live) value, which is typically set to ten hours. Depending on your specific use case, you can update the CDN TTL (Time to Live) settings accordingly.

Want to learn more? Go to [Invalidate the CDN cache by way of Dynamic Media](/help/assets/dynamic-media/invalidate-cdn-cache-dynamic-media.md).

