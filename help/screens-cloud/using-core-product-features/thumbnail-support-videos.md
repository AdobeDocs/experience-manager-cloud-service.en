---
title: Thumbnail Support for Videos in Screens as a Cloud Service
description: This page describes how to add Thumbnail Support for Videos in Screens as a Cloud Service.
index: yes
exl-id: 7b15d7cc-f089-4008-9039-5f48343a0f20
---
# Thumbnail Support for Videos {#thumbnail-support-videos}

## Introduction {#introduction}

A content author can define a thumbnail for videos so that the image can be used as a placeholder and properly test content playback and targeting, while the actual video is being finalized by the appropriate team. The image can also be used, in case the playback of the video fails.

Adding support for a thumbnail image on the video component lets the customer properly add a valid component in the channel, with actual content, and perform any targeting configurations before the video is actually delivered. 

>[!NOTE]
>The thumbnail image, if set on the video component, is played in case of video playback failure on the player. This allows you to deliver the desired message to the audience (by playing  content) instead of completely skipping it.

Thumbnail Support allows you to:

* Prepare a channel experience when the videos are not yet ready, or when you do not necessarily want to test a large asset download on the players

* Set a fallback mechanism, in case there are playback issues on the device.

## Using Thumbnails in Videos {#using-thumbnails}

>[!IMPORTANT]
>**Prerequisites**
>Before you learn how to use thumbnails for videos, please ensure to learn how to create video renditions for channels in Screens as a Cloud Service project. See [here](/help/screens-cloud/configuring/creating-screens-video-renditions-cloud-service.md) for more details.

Follow the steps below to use thumbnail in videos:

1. Navigate to an existing Screens channel or create a new channel.

   >[!NOTE]
   >To learn how to create a channel and add content to a channel, see [Creating and Managing a Channel in Screens as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/screens-as-cloud-service/create-content/creating-channels-screens-cloud.html?lang=en).

1. Select the channel and click on **Edit** from the action bar to open the editor.

   ![](/help/screens-cloud/using-core-product-features/assets/thumbnail-1.png)

1. Add or edit an existing video component, as shown in the figure below.

   ![](/help/screens-cloud/using-core-product-features/assets/thumbnail-2.png)

1. Select the video and click on the the *wrench* icon to open the video properties.

   ![](/help/screens-cloud/using-core-product-features/assets/thumbnail-3.png)

1. The **Video** dialog box opens where you will view the **Thumbnail** drop zone.

   ![](/help/screens-cloud/using-core-product-features/assets/thumbnail-4.png)

1. Drag and drop an image from the asset picker to the **Thumbnail** drop zone and click on **Done**.
   
   ![](/help/screens-cloud/using-core-product-features/assets/thumbnail-5.png)

1. Click on **Preview**.

1. If a video is set on the component, the video will play. If not, and the thumbnail is set, then the thumbnail will play. Otherwise the component is considered not configured and will be skipped.

## Supported Use Cases while using Thumbnail in Videos {#understand-use-case}

Thumbnail in videos supports the following use cases:

* A video component with nothing set up will be skipped.

* A video component with only the thumbnail set will play the thumbnail.

* A video component with both the video (if the video has correct rendition) and thumbnail set will play the video.

* A video component with the video set will play the thumbnail, in case of a playback error, or will just skip to the next item in case the thumbnail is not configured.
