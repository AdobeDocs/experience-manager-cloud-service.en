---
title: Multi Audio and Multi Captions in Dynamic Media with OpenAPI capabilities Videos
description: Learn how to add and manage multiple audio tracks and captions for video assets in Dynamic Media with OpenAPI capabilities within Adobe Experience Manager Assets.
role: User
badgeSaas: label="AEM Assets" type="Positive"
---

# Multi Audio and Multi Captions in Dynamic Media with OpenAPI capabilities Videos {#multi-audio-captions-dynamic-media-with-openapi-capabilities}

[!DNL Adobe Experience Manager Assets] Dynamic Media with OpenAPI capabilities enables you to add multiple audio tracks and caption files to video assets. This capability improves accessibility, supports localized playback experiences, and enhances video delivery for global audiences.

These features are managed directly from the **Captions & Audio tracks** tab on the video asset properties page.

>[!NOTE]
>
>Multi Audio and Multi Caption support in Dynamic Media with OpenAPI capabilities is a limited availability feature. You can enable it by creating a [support ticket](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

All supported Dynamic Media with OpenAPI capabilities video formats support multiple captions and audio tracks.

## Before you begin {#before-you-begin}

Ensure the following:

* The video asset is available in [!DNL AEM Assets]
* Supported audio format: `.mp3`
* Supported caption format: `.vtt`

>[!NOTE]
>
>Dynamic Media with OpenAPI capabilities does not require a video profile. The **Captions & Audio tracks** tab is available for all video assets by default.

## Add multiple audio tracks {#add-audio-tracks}

![Captions and Audio tracks tab](/help/assets/assets/caption-audio-tracks1.png)

To add audio tracks to a video:

1. Navigate to the uploaded video asset.
1. Select the asset and click **Properties**.
1. Open the **Captions & Audio tracks** tab.
1. Click **Upload Audio Tracks**.
1. Select one or more `.mp3` files.
1. Click **Draw** icon next to the audio track file name.

In the **Edit Audio Track** dialog box:

* **Filename** - Default filename derived from the uploaded file.
* **Language** - Select the audio language.
* **Type** - Original, Standard, or Audio Description.
* **Label** - Display name shown in the player audio selector.

![Audio Track dialog](/help/assets/assets/edit-audio1.png)

1. Click **Save**.
1. Repeat for additional audio tracks if required.
1. Click **Save & Close**.

>[!NOTE]
>
>Each audio track label must be unique.

## Add multiple captions {#add-captions}

![Captions and Audio tracks tab](/help/assets/assets/caption-audio-tracks1.png)

To add captions:

1. Open the video **Properties** page.
1. Open **Captions & Audio tracks** tab.
1. Click **Create Caption** > **Upload files**.
1. Select one or more `.vtt` files.
1. Click **Draw** icon next to caption file.

![Upload caption dialog](/help/assets/assets/upload-caption.png)

In the **Edit Caption** dialog box:

* **Filename** - Default uploaded filename.
* **Language** - Caption language.
* **Type** - Subtitle or Caption.
* **Label** - Display name shown in player caption selector.

![Edit Caption dialog](/help/assets/assets/edit-captions.png)

1. Click **Save**.
2. Click **Save & Close**.

>[!NOTE]
>
>Editing subtitle text is not supported. Update file externally and re-upload.

## Approval behavior {#approval-behavior}

Approval depends on parent video asset:

* If **Approved**, new files are auto-approved after processing.
* If not approved, they follow parent lifecycle.

## View file lifecycle status {#status}

* **Approved** - Ready for playback
* **Rejected** - File rejected

## Set default audio track {#set-default-audio}

By default, original audio is used.

1. Open **Captions & Audio tracks**.
1. Select audio track.
1. Click **Set as Default**.

   ![Set as Default action](/help/assets/assets/set-default.png)

1. Click **OK**.
1. Click **Save & Close**.

## Preview audio and captions {#preview-audio-captions}

After processing:

1. Open video preview.

   ![Video preview player](/help/assets/assets/preview-caption-audio.png)

1. Use player controls:

   * Switch audio tracks
   * Enable captions

## Download caption or audio files {#download-tracks}

1. Select caption or audio file.
1. Click **Download**.

   ![Download track action](/help/assets/assets/download-caption.png)

1. Click **Download**.

The selected file is downloaded to your local system.

## Delete caption or audio files {#delete-tracks}

1. Select caption or audio file.
1. Click **Delete**.

   ![Delete track action](/help/assets/assets/delete-caption.png)

1. Click **OK**.

Original audio extracted from video cannot be deleted.
