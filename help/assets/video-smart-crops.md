---
title: Apply Video Smart Crops to approved videos
description: Dynamic Media with OpenAPI capabilities enables you to generate Video Smart Cropped outputs for video assets in Adobe Experience Manager (AEM).
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets."
---

Apply Video Smart Crops to approved videos {#apply-video-smart-crops-dmwoapi}
================================================

[!DNL Dynamic Media with OpenAPI capabilities] enables you to generate Video Smart Cropped outputs for video assets in [!DNL Adobe Experience Manager (AEM)].

Video Smart Crops analyze video content and dynamically adjust framing to keep the key subject in focus across different aspect ratios and devices.

To use this feature, configure the metadata schema for video assets. Once enabled, users can apply Video Smart Crops by updating asset metadata and approving the asset.

Before you begin {#prerequisites-for-video-smart-crops}
--------------------------------------------------------

Ensure you have:

* Access to [!DNL AEM Assets as a Cloud Service].
* Permission to edit metadata schemas.
* Dynamic Media with OpenAPI capabilities enabled for your environment.
* Video assets available in AEM Assets.

Enable Video Smart Crops for videos (Admin) {#enable-video-smart-crops}
------------------------------------------------------------------------

To enable Video Smart Crops, configure the metadata schema used for video assets.

Execute the following steps:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.

2. Open the metadata schema applied to your video assets, and click **[!UICONTROL Edit]**.

3. In the Metadata Schema Editor, select the **[!UICONTROL Video]** tab.

4. From the **[!UICONTROL Build Form]** section, drag the **[!UICONTROL Dropdown]** component to the form.

   ![Create Video Smartcrops field added to metadata schema](/help/assets/assets/metadata-schema-form.png)

5. Select the newly added field and configure the following in the **[!UICONTROL Settings]** panel:

   * **Field Label**: Specify a field label of your choice.
   * **Map to property**: `./jcr:content/dam:applyVideoSmartCrop`

6. In the **[!UICONTROL Choices]** section, add the following values:

   * Yes → true  
   * No → false  

   ![Configure Create Video Smartcrops field](/help/assets/assets/edit-setting1.png)

7. Click **[!UICONTROL Save]**.

> **NOTE:** If the `dm_video` metadata schema is used in your environment, ensure that the same configuration is also applied to the `dm_video` schema. This ensures consistent behavior of Video Smart Crops across all video schema types.

Apply Video Smart Crops to approved videos {#apply-video-smart-crops}
----------------------------------------------------------------------

You can apply Video Smart Crops to video assets by enabling the metadata field and approving the asset.

Execute the following steps:

1. In [!DNL Assets View], select **[!UICONTROL Assets]** and navigate to your folder.

2. Select the video asset.

3. Click **[!UICONTROL Properties]**.

4. In the metadata panel, set **[!UICONTROL Create Video Smartcrops]** to **Yes**, update the asset status to **[!UICONTROL Approved]**, and click **[!UICONTROL Save]**.

   ![Approved video asset with Video Smartcrops enabled](/help/assets/assets/assets-create-video-smartcrops1.png)

A confirmation message displays after the properties are updated successfully.

View Video Smart Cropped outputs {#view-video-smart-crops}
----------------------------------------------------------

Once Video Smart Crops are generated, include the `mode=smartcrop` parameter in the `/play` endpoint video delivery request to render them.

* Video Smart Crops are applied dynamically during playback when the `mode=smartcrop` parameter is used.
* The Dynamic Media viewer automatically selects the most appropriate crop based on the device and aspect ratio.
* The video playback adjusts dynamically to keep the key subject in focus.