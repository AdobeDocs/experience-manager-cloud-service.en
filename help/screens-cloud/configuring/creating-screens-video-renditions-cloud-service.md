---
title: Creating Screens Video Renditions in Screens as a Cloud Service
description: This page describes how to create Screens Video Renditions in Screens as a Cloud Service.
---

# Creating Screens Video Renditions in Screens as a Cloud Service {#creating-screens-video-renditions}

## Introduction {#introduction}

This will guide describes how to create video renditions used in Screens players. 

>[!IMPORTANT]
>The steps  highlighted in this section must be configured if you are planning to use videos in Screens channels.

## Steps to Create Screens Video Renditions in Screens as a Cloud Service {#steps-creating-screens-video-renditions}

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


   >[!IMPORTANT]
   >Please ensure to use the Encoding name that starts with "screens-", only these video renditions will be considered to play the video experience in Screens As a Cloud Service. Enter the bit rate that suits your videos (2500kbps for 720px video and 5000 kbps for 1080px)

   >[!NOTE]
   >Multiple video renditions can be added with varying width/height/bitrate to suit your needs, but please remember that all the screens- renditions will be downloaded by the Screens devices, even though the device play only video rendition.

1. Click on Save

1. Select the Processing profile and click on "Apply profile to Folder(s)"

1. Select the folder(s) where Screens videos are kept and click on Apply

1. You can create multiple Processing profiles and apply them to the corresponding folders, so that the videos in those folders gets the specific video renditions

1. When you upload any videos to the folder where Processing profile is applied, videos will be processed and configured renditions will be created, which will be used by the Screens devices to play the videos.

