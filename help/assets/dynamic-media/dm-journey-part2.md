---
title: Journey into Dynamic Media, Part II
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
exl-id: cdca41ad-a2cd-4f68-aaa4-5eec33c30f0b
---
# Dynamic Media Journey: The Basics, part II  {#dm-journey-part2}

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

{{see-also-dm}}

Welcome to Dynamic Media Journey: The Basics, Part II where you can expect to learn the following:

* Anatomy of a Dynamic Media URL and how Dynamic Media delivers content.
* Fundamentals of creating image presets to render assets.
* Image sets, spin sets, and mixed media sets.

See also [Dynamic Media Journey; The Basics, Part I](/help/assets/dynamic-media/dm-journey-part1.md).

>[!TIP]
>
>For best results, Adobe recommends that you read and view this Dynamic Media Journey on a desktop computer.

## Anatomy of a Dynamic Media URL and how Dynamic Media delivers content {#dm-journey-d}

After your Dynamic Media assets are uploaded and published, you can copy an asset's generated URL and paste it into your browser to see how the asset will appear to a customer. The following copied URL for a watch image is broken down by color to make it easier to read and understand.

![Anatomy of a Dynamic Media URL](/help/assets/dynamic-media/assets/dm-colored-url.png)
_Anatomy of a Dynamic Media URL._

The first part of the URL in red is referencing the server domain itself. In this case, Dynamic Media is running on a generic server domain, which is `https://s7d1.scene7.com/is/image/`. It is easy to be able to look at a set of images and understand whether they are being served by Dynamic Media just by looking at the server domain. The URL is going to be fairly consistent. There are, however, some Dynamic Media customers that have switched over to a dedicated server domain where it might be `name-of-your-company.scene7.com`. A dedicated server domain is required for Smart Imaging.

The account name is the portion in purple. In this case, the account is called `jpearldemo`.

The asset ID or name, `AdobeStock_28563982` is in green. Notice that the asset has _no_ file extension such as `.png` or `.jpg`. When assets are ingested into Dynamic Media, the file extension is stripped out and a different kind of file is created: a pyramid-TIFF file. The pyramic-TIFF allows Dynamic Media to quickly create renditions on-the-fly.

And finally, there are some image processing parameters, `?wid=1000&fmt=jpeg&qlt=85`, shown in yellow on the end.

The entire URL path is live. [Try it](https://s7d1.scene7.com/is/image/jpearldemo/AdobeStock_28563982?wid=1000&fmt=jpeg&qlt=85){target="_blank"}.

With your browser window still open to the Dynamic Media URL and the watch image, let's look closer at how you can create renditions of the image just by changing the URL.

### Rendering the watch image through the URL

Begin by manually deleting only the image processing rules in the URL path; leave the server name, account name, and the asset ID or image name. [Try it](https://s7d1.scene7.com/is/image/jpearldemo/AdobeStock_28563982){target="_blank"}.

Now add an image processing parameter to the end of the URL. In the URL field, to the right of the image name, type `?wid=500`, then press **[!UICONTROL Enter]**. [Try it](https://s7d1.scene7.com/is/image/jpearldemo/AdobeStock%5F28563982?wid=500){target="_blank"}.

Notice that a new rendition of the watch is generated. A key take away to understand from this simple exercise of changing the image's width, is that the image seen is generated 100% dynamically.

Now change the width value of `500` pixels to `1000` pixels, and then press **[!UICONTROL Enter]**. [Try it](https://s7d1.scene7.com/is/image/jpearldemo/AdobeStock%5F28563982?wid=1000){target="_blank}. 
The moment you press **[!UICONTROL Enter]**, the browser goes back to the Dynamic Media Image Server. It generates a brand-new rendition of the watch, based on the new width value you just entered, then delivers the new image back to the browser, and caches it. 

Dynamic Media has numerous image processing parameters that you can use to fine-tune your image assets on web pages. You can [see a list of them here](https://experienceleague.adobe.com/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/c-command-reference.html?lang=en). 

Now try adding a rotation parameter to the watch image. And the end of the URL path, immediately following `wid=1000`, type `&rotate=90`, and then press **[!UICONTROL Enter]**. [Try it](https://s7d1.scene7.com/is/image/jpearldemo/AdobeStock%5F28563982?wid=1000&rotate=90){target="_blank"}.

The watch is still slightly skewed to the left. Change the rotate value of `90` to `92`, and then press **[!UICONTROL Enter]**. [Try it](https://s7d1.scene7.com/is/image/jpearldemo/AdobeStock%5F28563982?wid=1000&rotate=9){target="_blank"}.

Again, the moment you press **[!UICONTROL Enter]**, a new rendition of the watch is generated nearly instantaneously. You can see the kind of performance that you get, which explains why Dynamic Media can deliver more than 800,000 image requests, _per second_, on a busy weekend, or major holiday.

While it is possible to change image processing parameters in a URL on an image-by-image basis, it is not an efficient method, especially if you have tens of thousands of images that make up your website. A much better approach is using image presets.  

## Fundamentals of creating image presets to render assets {#dm-journey-e}

There are multiple ways and places where you are going to want to create an image or have an image be available. Traditionally, a Creative goes into Adobe Photoshop, and saves out each of these different renditions as static images.

![Static images](/help/assets/dynamic-media/assets/dm-static-images.png)
_Good: static images, each one manually created._

Now imagine the Creative Director looks at the images and says, 

_"I really wanted this shot so that the large hand is pointing at the four, and the small hand is pointing at the 1 to make the watch dial easier to see."_

The creative would have to reshoot all new static images again.

But, with Dynamic Media, if you have different image presets, you can use those images wherever you need them. The image presets enforce standards.

![Primary file approach](/help/assets/dynamic-media/assets/dm-onefile.png)
_Best: one file with multiple renditions created on the fly using image presets, such as `Search_Grid` and `Thumbnail`._

| **Why use image presets?** | |
|---|---|
| Standards | Image presets enforce a standard image processing treatment on any image that it is requested with. |
| Change management | If you must change image processing, you simply edit the parameter of the existing image preset. The updated definition is automatically propagated out to all requests. |

Every place that you need to have a particular type of image, for example, 

* a product detail page,
* search grid,
* thumbnail,
* shopping card, or
* hero image

You want that image delivered with the same parameters wherever they are going to be used.

For a moment, let's look at how an image preset is created in Dynamic Media.

![Creating an image preset starting with the Basic tab](/help/assets/dynamic-media/assets/dm-image-preset-basictab.png)
_Creating an image preset starting with the Basic tab._

In the example above, you can see that a new image preset was created with the name _Medium_. Dynamic Media uses an example, out-of-the-box image &ndash; the backpack &ndash; to help you see characteristics of the image preset as you create it. 

The _Medium_ image preset has a width of 500 pixels and a height of 800 pixels. In Part I of this Journey, you read about delivering assets in different formats. From the **[!UICONTROL Format]** pull-down menu, you can choose to deliver assets as JPEG, PNG, TIFF, or several other formats. You have flexibility here.

Selecting the **[!UICONTROL Advanced]** tab gives you options for the asset's color space. Depending on the format you selected in the **[!UICONTROL Basic]** tab &ndash; in the example above, JPEG was selected &ndash; you can deliver assets in RGB, Grayscale, or CMYK. From the **[!UICONTROL Color Profile]** pull-down menu, you can select how to deliver a CMYK image asset to be used for print. Notice, too, that there are additional parameters you can apply for sharpening your images. In this case, **[!UICONTROL Unsharp Mask]** was applied.

![Creating an image preset by selecting options from the Advanced tab](/help/assets/dynamic-media/assets/dm-image-preset-advancedtab.png)
_Creating an image preset by selecting options from the Advanced tab._

You recall in [Anatomy of a Dynamic Media URL](#dm-journey-d) earlier, that you read about the Dynamic Media URL and how that is built. The **[!UICONTROL Image Modifier]** text box is where you can type any additional image processing parameters that you want. The parameters get included in the preset name of the URL when your images are delivered, using the preset. In the screenshot above, the parameter `bgc=451B15` was added. That is, a dark brown background color was added.

You can think of an image preset as a recipe for your images. It is going to deliver any images that use the preset, consistently, every time; it's going to be the same. The parameter `&op_brightness=+10` was also added to increase the brightness slightly.  

When you are finished, you save the preset, and now it is available for all images that you have. In this case, you want to apply the _Medium_ image preset to an image of a bowl of liquid chocolate.

![Applying the image preset *Medium* to generate a rendition of an image](/help/assets/dynamic-media/assets/dm-medium-image-preset.png)
_Applying the image preset Medium to generate a rendition of an image._

You copy the URL, then paste it into your browser to check the appearance of the image. [Try it](http://s7d1.scene7.com/is/image/jpearldemo/AdobeStock_74043302?$Medium$){target="_blank"}. 

In your browser, notice the name of the image preset _Medium_ in the full URL path.

You can see the kind of clarity that is displayed in the image. That quality is partially due to the way the bowl of chocolate was shot. Also, it's partially because with Dynamic Media, you can store larger images than what is being delivered to digital channels.

If everything looks satisfactory for your bowl of chocolate, you paste the URL into your web pages where you want the image to appear on your website.

If you look again at the watch image below, you can see that there is a `Cart` image preset, a `Grid` preset, a `Large` preset, a `PDP-page` (Product Detail Page) preset, and several others.

![Static and dynamic image presets](/help/assets/dynamic-media/assets/dm-image-presets.png)
_Static and Dynamic image presets. The watch image was rendered using the `PDP-page` image preset._

But what if you have to change an image on your website? For example, suppose you have done some testing, and found that the image of 120 x 120 (the `Cart` image preset) is not being received as you thought. You must make the image larger by increasing the width to 175 pixels and increasing the height to 175 pixels. Traditionally, you would have to go into Adobe Photoshop and re-create all of those cart images. But with Dynamic Media, you simply edit the image preset by updating the Width and Height values to 175 and save your preset, as seen in the example below.

![Editing an image preset](/help/assets/dynamic-media/assets/dm-edit-image-preset.png)
_Editing the Width and Height of the `Cart` image preset._

After you change your image preset, and flush out the cache, all the images get updated, and all the URLs that are being used with that preset, do _not_ change anywhere. That means no broken links and no webpage redirects are necessary.

## Image sets, Spin sets, and Mixed Media sets {#dm-journey-f}

Some of the more popular uses of Dynamic Media, is the ability for you to create Image sets, Spin sets, and Mixed Media sets.

Image sets are typically made up of a series of image assets that are presented as a single entity. These kinds of sets give users an integrated viewing experience, where users can see different views of an item by clicking a thumbnail image. Image sets let you present alternative views of something and the viewer offers zooming tools for examining images closely. [View an image set called "Running" that uses the Flyout viewer](https://s7d1.scene7.com/s7viewers/html5/FlyoutViewer.html?asset=jpearldemo/Running).

Here inside Dynamic Media you can see several images of running shoes. It is a product line series that sales and marketing want customers to view as a single presentation; an Image set.

![Creating an image set](/help/assets/dynamic-media/assets/dm-create-image-set.png)
_The start of creating an Image set._

To create the Image set, you choose **[!UICONTROL Image Set]** from the **[!UICONTROL Create]** pull-down menu. Notice on the menu that there are also options to create a **[!UICONTROL Mixed Media Set]**, a **[!UICONTROL Spin Set]**, and a **[!UICONTROL Carousel Set]**. You create those sets in much the same way as an Image set. 

A Mixed Media set can contain images, swatch sets, spin sets, videos, and Adaptive Video sets. [Try it](https://s7d9.scene7.com/s7viewers/html5/MixedMediaViewer.html?asset=Scene7SharedAssets/Mixed_Media_Set_Sample). A Spin set simulates the real-world act of turning an object to examine it. Spin sets make it possible to view key visual details from any angle. [Try it](https://s7d9.scene7.com/s7viewers/html5/SpinViewer.html?asset=Scene7SharedAssets/SpinSet_Sample&stagesize=500,400){target="_blank"}.

Creating an Image set is straightforward. You simply add the image assets that you want to include in the set.

![Creating an image set](/help/assets/dynamic-media/assets/dm-create-image-set-add-assets.png)
_The Image Set Editor lets you add image assets and reorder their appearance in the set._

You are required to give the set a name. Choose the name carefully because you cannot edit it later! In the example above, the set is called `Running`. When you are done, you save the set.

And here is the `Running` Image set in Experience Manager Assets.

![The Running image set in Experience Manager Assets, Card View](/help/assets/dynamic-media/assets/dm-image-set.png)
_The `Running` Image set in Experience Manager Assets, Card View._

Whether you have created an Image set, a Mixed Media set, a Spin set, or any other interactive media, after you create the set, you want to see how it appears and behaves for a customer. Dynamic Media has numerous built-in viewers that let you do just that.

You begin by selecting the built Image set to open it in a preview as seen in the following example.

![The Running image set in preview with the Viewers option selected](/help/assets/dynamic-media/assets/dm-image-set-viewer.png)
_The `Running` Image set in preview with Viewers option selected._

Notice in the preview that you can select the running shoe swatches and zoom in and out on the shoes. To apply a viewer to the set, you select **[!UICONTROL Viewers]** from the pull-down menu.

![The Running image set with the Flyout viewer applied to it](/help/assets/dynamic-media/assets/dm-image-set-flyout-viewer.png)
_The `Running` Image set with the Flyout viewer applied to it._

In this case, the `Flyout` viewer was selected. At this point, you can preview the image set in the viewer. But, it is best to see it in your browser, just how a customer sees it. You select **[!UICONTROL URL]** in the lower left, then copy the URL and paste it into your browser. [Try it](https://s7d1.scene7.com/s7viewers/html5/FlyoutViewer.html?asset=jpearldemo/Running&config=jpearldemo/Flyout){target="_blank"}.   

The single URL lets you use the image set and viewer where you need them on your website. You may have noticed in the previous example that **[!UICONTROL Embed]** is to the right of the URL button. By selecting **[!UICONTROL Embed]**, you can copy the code for this image set/viewer, and add it into a web page or an Experience Manager Sites component.

The Flyout viewer is a default, out-of-box viewer whose properties you can edit. Or, just like creating an image preset, you can create your own, custom viewer.

Now, supposed your sales and marketing team does not like the Flyout viewer. They like the zoom feature but they want customers to see the zoom effect directly over the shoes. In such case, you simply apply the InlineZoom viewer to the image set and copy and paste its URL in your browser to see how it behaves. [Try it](https://s7d1.scene7.com/s7viewers/html5/FlyoutViewer.html?asset=jpearldemo/Running&config=jpearldemo/InlineZoom){target="_blank"}.

When you move the mouse pointer over the shoe, you zoom in to that image, and you can see more detail as you move the pointer around. And the reason for that is simply the size of the image that was initially uploaded into Dynamic Media.

As you consider living as a consumer, or as you work in your day-to-day role, and as you go to different websites, you see things like this. Think about how that's being done, and how you can use the power of Dynamic Media in your own work and on your company's website. 

You just read about image sets and viewers. Let's look at a couple of other viewers and try them out on single assets. To reset the viewer, click the **[!UICONTROL Refresh]** button in the lower-left corner.

<!-- LEAVE THIS HIDDEN PATH IN THE DOCUMENTATION FOR DEMO PURPOSES [Flyout viewer with image set](http://www.partycity.com/girls-little-old-lady-costume-P750948.html) -->

* `ZoomVertical_dark` viewer applied to an image asset. [Try it](https://s7d1.scene7.com/s7viewers/html5/ZoomVerticalViewer.html?asset=jpearldemo/AdobeStock_96311480&config=jpearldemo/ZoomVertical_dark){target="_blank"}.
* `Zoom_light` viewer applied to an image. [Try it](https://s7d1.scene7.com/s7viewers/html5/BasicZoomViewer.html?asset=jpearldemo/AdobeStock_38827423&config=jpearldemo/Zoom_light){target="_blank"}.

## Optional - Learn more

If to learn more about what you just read, use the materials below to explore concepts in greater detail. Otherwise, your Dynamic Media Journey is complete!

<!--
_Dynamic Media Help topics_

* [How to create image presets](/help/assets/dynamic-media/image-presets.md)
* A list of [image processing parameters](https://experienceleague.adobe.com/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/c-command-reference.html) that you can use in the Image Modifier field when you create an image preset
* [How to preview assets](/help/assets/dynamic-media/previewing-assets.md)
* [How to preview 3D assets](/help/assets/dynamic-media/previewing-3d-assets.md)
* [How to create Image sets](/help/assets/dynamic-media/image-sets.md)
* [How to create Spin sets](/help/assets/dynamic-media/spin-sets.md)
* [How to create Mixed Media sets](/help/assets/dynamic-media/mixed-media-sets.md) -->

_Dynamic Media tutorials_

* [Use Dynamic Media with Experience Manager Assets](https://experienceleague.adobe.com/docs/experience-manager-learn/assets/dynamic-media/dynamic-media-overview-feature-video-use.html)
* [Adobe Experience Manager content library](https://experienceleague.adobe.com/?lang=en#recommended/solutions/experience-manager) (search on _Dynamic Media_)

_Dynamic Media viewers_

* [Live Demos](https://landing.adobe.com/en/na/dynamic-media/ctir-2755/live-demos.html) of each viewer

<!-- Live as of April 28 2022. LEAVE IN HERE https://landing.adobe.com/en/na/dynamic-media/ctir-2755/index.html -->