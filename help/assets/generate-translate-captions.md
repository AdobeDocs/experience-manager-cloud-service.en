---
title: Generate and translate captions in Dynamic Media with OpenAPI capabilities
description: Learn how to generate captions from audio tracks and translate captions for video assets in Dynamic Media with OpenAPI capabilities within Adobe Experience Manager Assets.
role: User
badgeSaas: label="AEM Assets" type="Positive"
---

# Generate and translate captions in Dynamic Media with OpenAPI capabilities {#generate-translate-captions}

[!DNL Adobe Experience Manager Assets] Dynamic Media with OpenAPI capabilities enables you to generate captions from audio tracks and translate existing captions into multiple supported languages. These capabilities improve accessibility, simplify subtitle creation, and support localized video playback experiences.

>[!NOTE]
>
>Generate and translate captions is a Limited Availability feature. To enable this feature, create a [support ticket](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

You can manage captions directly from the **Captions & Audio tracks** tab on the video asset properties page.

>[!NOTE]
>
>Dynamic Media with OpenAPI capabilities does not require a video profile. The **Captions & Audio tracks** tab is available for video assets by default.

## Before you begin {#before-you-begin}

Ensure the following:

* The video asset is available in [!DNL AEM Assets].
* The video contains at least one audio track.

## Generate captions from audio tracks {#generate-captions}

To generate captions from an audio track:

1. Navigate to the uploaded video asset.
1. Select the asset and click **Properties**.
1. Open the **Captions & Audio tracks** tab.
1. Click **Create Caption** > **Convert audio tracks**.

   ![Convert Audio Tracks dialog](/help/assets/assets/convert-audio-tracks.png)

1. Select the audio track.
1. Select one or more output languages.
1. Click **Done**.

   Caption files are generated for the selected languages and are added to the **Captions** section.

   >[!NOTE]
   >
   >Only audio tracks that are in the **Processing**, **Processed**, or **Approved** state and are in a supported language can be selected for caption generation.

1. Click **Save** or **Save & Close**.

## Translate captions {#translate-captions}

To translate an existing caption:

1. Open the **Captions & Audio tracks** tab.
1. Click **Create Caption** > **Translate caption**.

   ![Translate Caption dialog](/help/assets/assets/translate-caption.png)

1. Select the source caption.
1. Select one or more output languages.
1. Click **Done**.

   Translated captions are added to the **Captions** section.

   >[!NOTE]
   >
   >Only caption files that are in the **Processing**, **Processed**, or **Approved** state and are in a supported language can be selected as source captions for translation.

1. Click **Save** or **Save & Close**.

## Edit captions {#edit-captions}

To edit a caption:

1. Open the **Captions & Audio tracks** tab.
1. Select the caption.
1. Click the **Edit** icon.
1. Modify the caption text.
1. Preview the updated caption.
1. Click **Save** or **Save & Close**.

The updated caption enters the **Processing** state before it becomes available.

## Approve captions {#approve-captions}

After caption processing is complete:

1. Open the **Captions & Audio tracks** tab.
1. Select one or more caption files.
1. Click **Approve**.

   ![Approve captions](/help/assets/assets/approval-status.png)

The selected caption files are approved and become available for delivery.

>[!NOTE]
>
>Dynamic Media with OpenAPI capabilities uses **Approve** instead of **Publish** for caption files.

## View caption lifecycle status {#status}

The **Status** column displays the current processing state of each caption.

* **Processing** – The caption is being generated or translated.
* **Processed** – The caption has been generated or translated and is ready for approval.
* **Approved** – The caption is approved and available for delivery.

## Deliver videos with captions {#deliver-videos-with-captions}

After the caption files are approved, you can deliver the video with captions using the Dynamic Media delivery URL.

To copy the delivery URL:

1. Open the video asset.
1. Open the **Dynamic Media** panel.
1. Click **Copy URL**.

The copied URL has the following format:

`https://delivery-p<programId>-e<environmentId>.adobeaemcloud.com/adobe/assets/urn:aaid:aem:<asset-uuid>/play`

When the video is played using the `/play` URL, approved captions are available from the **CC (Closed Captions)** button in the video player. If multiple approved caption languages are available, users can switch between them using the **CC** button.
