---
title: Creating Video Renditions in Screens as a Cloud Service
description: This page describes how to create video renditions in Screens as a Cloud Service.
exl-id: a9c46036-cd29-47fa-81d9-c865cf22c98a
feature: Administering Screens
role: "Admin, Developer, User"
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
   >See [Using Screens Content Provider](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/screens-as-cloud-service/configure-screens-cloud/using-screens-content-provider.html#screens-content-provider) for  more details.

1. Click the Tools section from the left navigation bar and click **Assets** and then click **Processing Profiles**.

    ![Click Processing Profiles](/help/screens-cloud/assets/configure/screens-cp-3.png)

1. Click **Create** to create a processing profile.

   ![Click Create](/help/screens-cloud/assets/configure/screens-video-2.png)

1. Enter the **Name**, such as **ScreensProcessingProfile**.

   ![Processing Profile dialog box showing Name field highlighted.](/help/screens-cloud/assets/configure/screens-video-3.png)

1. Navigate to **Video** tab so you can add a video encoding,  and then click **Add New**.

   ![Processing Profile dialog box showing Add New button highlighted.](/help/screens-cloud/assets/configure/screens-video-4a.png)

1. Enter the **Encoding Name** such as , **screens-fullhd** and the **Bitrate** as **2500**.

   ![Processing Profile dialog box showing Save button highlighted.](/help/screens-cloud/assets/configure/screens-video-4.png)

   >[!IMPORTANT]
   >Use the Encoding name that starts with "screens-". Only these video renditions are considered to play the video experience in Screens as a Cloud Service. Enter the bitrate that works your videos (2500 kbps for 720-px video and 5000 kbps for 1080 px).

   >[!NOTE]
   >Multiple video renditions can be added with varying width/height/bitrate to work your videos. All the screens, renditions are downloaded by the Screens devices, even though the device plays only video rendition.

1. Click **Save**.

1. Select the Processing profile and click **Apply Profile to Folders**.

   ![Apply Profile to Folder](/help/screens-cloud/assets/configure/screens-video-5.png)

1. Select the folders where Screens videos are kept and click **Apply**.

   ![Click Apply](/help/screens-cloud/assets/configure/screens-video-6.png)

   >[!NOTE]
   >
   >* You can create multiple Processing profiles and apply them to the corresponding folders, so that the videos in those folders get the specific video renditions.
   >* When you upload any videos to the folder where a Processing profile is applied, videos are processed. Configured renditions are created, which are used by the Screens devices to play the videos.
