---
title: Best practices in Dynamic Media
description: Learn about best practices in Dynamic Media when it comes to working with images and video.
contentOwner: Rick Brough
products: Experience Manager as a Cloud Service
topic-tags: introduction,administering
content-type: reference
feature: Video,Renditions,Configuration,Asset Management
role: User, Admin
mini-toc-levels: 4
hide: no
hidefromtoc: no

---
# About best practices in Dynamic Media{#about-dm-best-practices}

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



In Dynamic Media on Adobe Experience Manager as a Cloud Service, there are sets of methods, techniques, and guidelines that can help you maximize the potential of your rich media content. These best practices can lead to optimal results and increase efficiency in your use of Dynamic Media. They represent the most efficient and effective courses of action in a particular situation, unlocking high value for your audience and delivering high-quality, engaging content.

Adapt these Dynamic Media best practices to your specific context and project requirements. 

>[!IMPORTANT]
>
>The Dynamic Media best practices in this article may evolve over time as new technologies in Dynamic Media emerge. The information below is current for the latest version of Dynamic Media.


## Ingest assets into Dynamic Media

Streamline your management of large numbers of assets efficiently and ensure that only the appropriate, authorized content reaches your end-users by using Dynamic Media's **Selective Sync** and **Selective Publish** features.

* **Selective Sync:** A proactive feature that lets you choose which assets to sync with Dynamic Media. For example, you might decide to sync only those folders containing assets that have received final approval. This workflow helps you maintain control over which assets are being prepared for delivery to your customers.

**Selective Publish:** After syncing your assets, Selective Publish gives you control over which assets are visible to your customers. This ability means you can govern which approved assets are actually delivered through your channels, ensuring that your customers see only the best and most relevant content.

These two best practices help you achieve better control, governance, and productivity over your rich-media content. Ready to learn more? Go to [Configure Selective Publish at the folder level in Dyanmic Media](/help/assets/dynamic-media/selective-publishing.md).


## Prepare assets for delivery

### Organize your assets

For efficient asset organization that streamlines workflows, use one or more of the following best practices: 

* **Organize assets in folders:** Organizing assets effectively involves categorizing them into folders, similar to file organization on a computer. Proper naming, structuring subfolders, and file management within these folders are crucial for efficient asset processing. Implementing systematic naming conventions and metadata practices maximizes the utility of your digital asset repository. For detailed guidance on folder management, refer to the "Manage assets" section.
    
    Ready to learn more? Go to [Organize assets in folders](/help/assets/organize-assets.md#organize-using-folders).
* **Organize assets using tags:** Tagging assets enhances searchability, collection creation, and search ranking. Adobe Sensei's AI employs a self-learning algorithm for precise tagging, enabling quick asset retrieval. Adobe Sensei also recognizes and assigns relevant tags&ndash;including custom ones&ndash;to assets, simplifying asset management with automatic, descriptive tagging.

    Ready to learn more? Go to [Organize assets using tags](/help/assets/organize-assets.md#use-tags-to-organize-assets).

* **Organize assets as collections:** Dynamic Media along with Experience Manager Assets allows for the efficient creation, editing, and sharing of asset collections among users. You can establish various collection types, including static lists and dynamic, search-based compilations. These collection types can be shared across diverse locations with customizable access and editing rights.

    Ready to learn more? Go to [Organize assets as collections](/help/assets/manage-collections.md).

* **Organize assets using profiles:** A processing profile automates asset handling in designated folders, streamlining organization. Standardizing metadata, file names, and folder structures allows for consistent and precise application of these profiles as your digital asset collection expands.

    Ready to learn more? Go to [Organize assets using profiles](/help/assets/manage-collections.md).

### Optimize the quality of images

Enhancing image quality requires careful consideration of various factors. It can be a time-intensive process. However, there are some tried-and-true practices that can help you achieve desirable results. Some of those best practices include how to obtain optimal image sizing, image sharpening, and the best image formats to use.

Ready to learn more? Go to [Best practices for optimizing the quality of your images](/help/assets/dynamic-media/best-practices-for-optimizing-the-quality-of-your-images.md).

Because perception of image quality varies from person to person, sometimes a systematic approach to experimentation is essential for achieving desirable results. Adobe Experience Manager aids this process with more than 100 Dynamic Media commands for image enhancement.

Ready to learn more? Watch [Dynamic Media Snapshot (3 minutes, 17 seconds)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-snapshot).

To assess these different commands' impact on image quality, you can upload an image to Dynamic Media, use the tool's interface at the specified URL, and apply the commands you want to try out. 

Ready to try it? Launch [Dynamic Media Snapshot](https://snapshot.scene7.com/)

### Standardize on styles applied to images

Use Image Presets regularly in Dynamic Media to consistently and dynamically adjust image sizes, formats, and properties. Think of an Image Preset as a macro: it's a named set of commands for sizing and formatting. For example, if your site needs product images in various sizes and formats, with specific compression for desktop and mobile, Image Presets automate this process efficiently.

Ready to try it? Go to [Fundamentals of creating image presets to render assets](/help/assets/dynamic-media/dm-journey-part2.md#dm-journey-e)

### Adjust the focus and framing of images and videos

Smart Crop is a feature in Dynamic Media that uses Adobe Sensei, Adobe's AI and machine learning framework, to automate the cropping of images and videos. It intelligently detects and focuses on the main subject or point of interest in an image or video, ensuring that the focal point is maintained across various screen sizes on desktop computers and mobile devices.

A best practice is to create an Image Profile with Smart Crop. In the profile, you can define various screen sizes and let Adobe Sensei do the rest, ensuring that your images and videos are always optimized for the viewer's device.

Ready to learn more? Watch [Using Smart Crop with AEM Assets Dynamic Media (6 minutes, 35 seconds)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use) and [Using Dynamic Media Smart Crop for Video (6 minutes, 22 seconds)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/video/dynamic-media-smart-crop-video)

### Techniques in Dynamic Media to improve SEO rankings



Ready to learn more? Go to [Google image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)


## Deliver assets to customers







See also [Best practices for optimizing the quality of your images](/help/assets/dynamic-media/best-practices-for-optimizing-the-quality-of-your-images.md)







## Video assets in Dynamic Media


