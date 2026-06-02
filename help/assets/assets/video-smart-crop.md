---
title: Apply Video Smart Crops to video assets
description: Dynamic Media with OpenAPI capabilities enables you to generate Video Smart Crop outputs for video assets in Adobe Experience Manager (AEM).
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets."
---

# Apply Video Smart Crops to video assets {#apply-video-smart-crops-dmwoapi}

[!DNL Dynamic Media with OpenAPI capabilities] enables you to generate Video Smart Crops outputs for video assets in [!DNL Adobe Experience Manager (AEM)].

Video Smart Crops analyze video content and dynamically adjust framing to keep the key subject in focus across different aspect ratios and devices.

To use this feature, configure the metadata schema for video assets. Once enabled, users can apply Video Smart Crops by updating asset metadata. The asset must be in Approved state for processing.

## Before you begin {#prerequisites-for-video-smart-crops}

Ensure you have:

* Access to [!DNL AEM Assets as a Cloud Service].
* Permission to edit metadata schemas.
* Dynamic Media with OpenAPI capabilities enabled for your environment.
* Video assets available in AEM Assets.

## Enable Video Smart Crops for videos (Admin) {#enable-video-smart-crops}

To enable Video Smart Crops, configure the metadata schema used for video assets.

Execute the following steps:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.

1. Open the metadata schema applied to your video assets, and click **[!UICONTROL Edit]**.

1. In the Metadata Schema Editor, select the **[!UICONTROL Video]** tab.

1. From the **[!UICONTROL Build Form]** section, drag the **[!UICONTROL Dropdown]** component to the form.

   ![Create Video Smart Crop field added to metadata schema](/help/assets/assets/metadata-schema-form.png)

1. Select the newly added field and configure the following in the **[!UICONTROL Settings]** panel:

   * **Field Label**: Specify a label as per your metadata schema configuration.
   * **Map to property**: `./jcr:content/dam:applyVideoSmartCrop`

1. In the **[!UICONTROL Choices]** section, add the following values:

   * Yes → true
   * No → false

   ![Configure Video Smart Crop field](/help/assets/assets/edit-setting1.png)

1. Click **[!UICONTROL Save]**.

## Apply Video Smart Crops to video assets {#apply-video-smart-crops}

You can apply Video Smart Crops to video assets by enabling the metadata field and updating the asset status.

Execute the following steps:

1. In [!DNL Assets View], select **[!UICONTROL Assets]** and navigate to your folder.

1. Select the video asset.

1. Click **[!UICONTROL Properties]**.

1. In the metadata panel:

   * Set the Video Smart Crop field to **Yes**
   * Set the asset status to **Approved**
   * Click **[!UICONTROL Save & Close]**

   ![Approved video asset with Video Smart Crop enabled](/help/assets/assets/assets-create-video-smartcrops1.png)

A confirmation message is displayed after the properties are successfully updated.

## View Video Smart Crops outputs {#view-video-smart-crops}

Once Video Smart Crops outputs are generated, include the `mode=smartcrop` parameter in the `/play` endpoint request for video delivery to render them.

* Video Smart Crops are applied dynamically during playback when the `mode=smartcrop` parameter is used.
* The Dynamic Media viewer automatically selects the most appropriate crop based on the device and aspect ratio.
* The video playback adjusts dynamically to keep the key subject in focus.