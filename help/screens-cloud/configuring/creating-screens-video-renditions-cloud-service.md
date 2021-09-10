---
title: Creating Video Renditions in Screens as a Cloud Service
description: This page describes how to create video renditions in Screens as a Cloud Service.
exl-id: a9c46036-cd29-47fa-81d9-c865cf22c98a
---
# Creating Video Renditions in Screens as a Cloud Service {#creating-screens-video-renditions}

## Introduction {#introduction}

This section describes how to create video renditions used in Screens players. 

>[!IMPORTANT]
>The steps  highlighted in this section must be configured, if you are planning to use videos in Screens channels.

## Steps to Create Video Renditions in Screens as a Cloud Service {#steps-creating-screens-video-renditions}

Follow the steps below to create video renditions in Screens as a Cloud Service from Screens Content Provider:

1. Navigate to your channel in Screens Content Provider.

   >[!NOTE]
   >Refer to [Using Screens Content Provider](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/screens-as-cloud-service/configure-screens-cloud/using-screens-content-provider.html?lang=en#screens-content-provider) for  more details.

1. Click on the Tools section from the left navigation bar and click on **Assets** and then click on **Processing Profiles**.

    ![](/help/screens-cloud/assets/configure/screens-cp-3.png)

1. Click on **Create** to create new processing profile.

   ![](/help/screens-cloud/assets/configure/screens-video-2.png)

1. Enter the **Name**, such as **ScreensProcessingProfile**.

   ![](/help/screens-cloud/assets/configure/screens-video-3.png)

1. Navigate to **Video** tab to add a video encoding and click on **Add New**.

   ![](/help/screens-cloud/assets/configure/screens-video-4a.png)

1. Enter the **Encoding Name** such as , **screens-fullhd** and the **Bitrate** as **2500**.

   ![](/help/screens-cloud/assets/configure/screens-video-4.png)

   >[!IMPORTANT]
   >Please ensure to use the Encoding name that starts with "screens-", only these video renditions will be considered to play the video experience in Screens as a Cloud Service. Enter the bitrate that works your videos (2500kbps for 720px video and 5000 kbps for 1080px).

   >[!NOTE]
   >Multiple video renditions can be added with varying width/height/bitrate to work your videos. Please remember that all the screens- renditions will be downloaded by the Screens devices, even though the device plays only video rendition.

1. Click on **Save**.

1. Select the Processing profile and click on **Apply Profile to Folder(s)**.

   ![](/help/screens-cloud/assets/configure/screens-video-5.png)

1. Select the folder(s) where Screens videos are kept and click on **Apply**.

   ![](/help/screens-cloud/assets/configure/screens-video-6.png)

   >[!NOTE]
   >* You can create multiple Processing profiles and apply them to the corresponding folders, so that the videos in those folders get the specific video renditions.
   >* When you upload any videos to the folder where Processing profile is applied, videos are processed and configured renditions are created, which are further used by the Screens devices to play the videos.
