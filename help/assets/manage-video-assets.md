---
title: Manage video assets
description: Upload, preview, annotate, and publish video assets in [!DNL Adobe Experience Manager].
contentOwner: AG
feature: "Asset Management,Publishing,Collaboration,Video"
role: Business Practitioner
---

# Manage video assets {#manage-video-assets}

Video format is a critical part of digital assets of an organization. [!DNL Adobe Experience Manager] offers mature offerings and features to manage the entire lifecycle of your video assets after their creation.

Learn how to manage and edit the video assets in [!DNL Adobe Experience Manager Assets]. Video encoding and transcoding, for example, FFmpeg transcoding, is possible using Processing Profiles and using [!DNL Dynamic Media] integration. Without [!DNL Dynamic Media] license, [!DNL Experience Manager] provides basic support for videos, such as transcoding using FFmpeg, extraction of preview thumbnails for the supported file formats, and preview in the user interface for formats that are supported for playback in the browser directly.

## Upload and preview video assets {#upload-and-preview-video-assets}

[!DNL Adobe Experience Manager Assets] generates previews for video assets with the extension MP4. You can preview the renditions in the [!DNL Assets] user interface.

1. In the digital assets folder or subfolders, navigate to the location where you want to add digital assets.
1. To upload the asset, click **[!UICONTROL Create]** from the toolbar and choose **[!UICONTROL Files]**. Alternatively, drag a file on the user interface. See [upload assets](manage-digital-assets.md#uploading-assets) for details.
1. To preview a video in the card view, click the **[!UICONTROL Play]** ![play option](assets/do-not-localize/play.png) option on the video asset. You can pause or play video in the card view only. The [!UICONTROL Play] and [!UICONTROL Pause] options are not available in the list view.
1. To preview the video in the asset details page, select **[!UICONTROL Edit]** on the card. The video plays in the native video player of the browser. You can play, pause, control the volume, and zoom the video to full screen.

## Publish video assets {#publish-video-assets}

After publishing, you can include the video assets in a web page as a URL or directly embed the assets. For details, see [publish [!DNL Dynamic Media] assets](/help/assets/dynamic-media/publishing-dynamicmedia-assets.md).

## Transcode using Processing Profile {#transcode-video}

[!DNL Experience Manager] as a [!DNL Cloud Service] lets you do basic transcoding of MP4 video files using Processing Profiles. The functionality allows you to not just upload but also preview and scale a MP4 video file.

![Create Processing Profile for video transcoding in [!DNL Experience Manager]](assets/video-processing-profile-for-mp4.png)

*Figure: A Processing Profile for video transcoding in [!DNL Experience Manager].*

If you provide only width or only height and leave the other field blank, the renditions maintain the aspect ratio. H.264 video codec is available for transcoding.

To process assets using a processing profile, add a profile to a folder. See [use processing profiles to process assets](/help/assets/asset-microservices-configure-and-use.md#use-profiles).

## Annotate video assets {#annotate-video-assets}

1. From the [!DNL Assets] console, select **[!UICONTROL Edit]** on the asset card to display the asset details page.
1. To play the video, click **[!UICONTROL Preview]**.
1. To annotate the video, click **[!UICONTROL Annotate]**. An annotation is added at the particular time (frame) in the video. When annotating, you can draw on the canvas and include a comment with the drawing. Comments are auto-saved. To exit the annotation wizard, click **[!UICONTROL Close]**.
1. Seek to a specific point in the video, specify the time in seconds in the **text** field and click **Jump**. For example, to skip the first 20 seconds of video, enter 20 in the text field.
1. To view it in the timeline, click an annotation. To delete the annotation from the timeline, click **[!UICONTROL Delete]**.

## Best practices and limitations {#tips-limitations}

* Without [!DNL Dynamic Media] license, you can only process MP4 files using processing profiles.
* When transcoding MP4 files using Processing Profiles, the following guidelines and limitations apply:

  * Apple ProRes files can only transcode to a maximum resolution of 1080p.
  * If the source file has a bitrate >200 Mbps, you can only transcode to a maximum resolution of 1080p.
  * If the source framerate >=60 fps then, the maximum size of the source file that you can use is,

    * 400 MB for 4k transcoding.
    * 800 MB for 1080p transcoding.
    * 8 GB for 720p transcoding.

  * Maximum file size you can transcode to 4k resolution is 2.55 GB MP4 file of 4k resolution, 12 Mbps bitrate, and 23 fps.

>[!MORELIKETHIS]
>
>* [Dynamic Media video documentation](/help/assets/dynamic-media/video.md).
>* [Know more about use, types, and configuration of processing profiles](/help/assets/asset-microservices-configure-and-use.md).
