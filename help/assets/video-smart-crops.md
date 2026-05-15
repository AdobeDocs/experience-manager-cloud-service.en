---
title: Apply Video Smart Crops to approved videos
description: Dynamic Media with OpenAPI capabilities enable you to automatically generate Video Smart Cropped outputs for approved video assets in Adobe Experience Manager (AEM).
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: video-smartcrop-dmwoapi
---

# Apply Video Smart Crops to approved videos {#apply-video-smart-crops-dmwoapi}

[!DNL Dynamic Media with OpenAPI capabilities] enable you to automatically generate Video Smart Cropped outputs for video assets in [!DNL Adobe Experience Manager (AEM)]. Video Smart Crops analyze video content and dynamically adjust framing to keep the key subject in focus across different aspect ratios and devices.

Video Smart Crops are generated automatically when the feature is enabled and the video asset is approved

## Before you begin {#prerequisites-for-video-smart-crops}

Ensure you have:

* Access to [!DNL AEM Assets as a Cloud Service].
* Permission to edit metadata schemas.
* Dynamic Media with OpenAPI capabilities enabled for your environment.
* Video assets that can be marked as **[!UICONTROL Approved]**.

## Enable Video Smart Crops for videos {#enable-video-smart-crops}

To enable Video Smart Crops, configure the metadata schema used for video assets:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
2. Open the applicable metadata schema (for example, **default**).
3. Select the **Video** form and click **[!UICONTROL Edit]**.
4. Add a new **[!UICONTROL Dropdown field]** and configure the following:

   * **Field Label**: Create Video Smartcrops  
   * **Map to property**: `./jcr:content/dam:applyVideoSmartCrop`

5. Add the following values manually:

   * Yes → true  
   * No → false  

6. Save the schema.

The **Create Video Smartcrops** option is now available in the video asset metadata form.

<!--
broken link
![Create Video Smartcrops field](/help/assets/assets/video-smartcrop-metadata-field.png)
-->

## Apply Video Smart Crops to approved videos {#apply-video-smart-crops}

You can apply Video Smart Crops to video assets by enabling the metadata field and approving the asset.

Execute the following steps:

1. In [!DNL Assets View], select **[!UICONTROL Assets]** and navigate to your folder.
2. Select the video asset.
3. Click **[!UICONTROL Details]**.
4. In the metadata panel, locate **[!UICONTROL Create Video Smartcrops]**.
5. Set the value to **Yes**, then click **[!UICONTROL Save]**.
6. Set the asset status to **[!UICONTROL Approved]**.

After the asset is approved, Video Smart Cropped outputs are generated automatically.

## View Video Smart Cropped outputs {#view-video-smart-crops}

Once Video Smart Crops are generated:

* The outputs are available during video playback.
* The Dynamic Media viewer automatically selects the most appropriate crop based on the device and aspect ratio.
* The video playback dynamically adjusts to keep the key subject in focus.

## Use Video Smart Cropped videos {#use-video-smart-crops}

You can use Video Smart Cropped outputs wherever the video asset is delivered, such as:

* Web pages
* Applications
* Embedded video players

The viewer automatically applies the appropriate smart crop during playback.

>[!NOTE]
>
>* Video Smart Crops are generated only for **Approved** video assets.
>* Ensure that the **Create Video Smartcrops** field is set to **Yes** before approving the asset.
>* Video Smart Crops do not modify the original asset. Cropping is applied dynamically during playback.