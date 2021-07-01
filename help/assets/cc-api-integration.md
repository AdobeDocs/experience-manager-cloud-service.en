---
title: Content Automation for Creative Cloud integration
description: Generate variations of assets using Creative Cloud integration
contentOwner: AG
feature: Upload,Asset Processing,Publishing,Asset Compute Microservices,Workflow
role: Business Practitioner,Administrator
---

# Generate variations of assets using [!DNL Adobe Creative Cloud] integration {#content-automation}

Content automation add-on integrates Experience Manager Assets as a Cloud Service and Adobe Creative Cloud APIs to creatively process your assets at scale. Experience Manager uses cloud-based [asset microservices](/help/assets/asset-microservices-overview.md) to leverage the Adobe Creative Cloud features and automate the asset creation and media handling.

To edit assets in [!DNL Adobe Photoshop] and [!DNL Adobe Lightroom], you do not have to download from, edit, and upload to [!DNL Experience Manager Assets]. Just create and configure a processing profile, apply the profile to a folder, and upload the assets to the folder. The assets uploaded to the folder are processed to create different variations of that asset. The consistent and effortless bulk processing and editing of assets saved manual efforts and increases content velocity. Additionally, developers and partners can extend the asset microservices with direct access to these APIs and include custom logic. 

Users can create processing profiles to automate the following creative operations on their assets:  

* **Auto-tone**: Utilizes artificial intelligence to analyze the contents of the image and intelligently makes light and color corrections based on the unique attributes of the image.
* **Auto-upright**: Utilizes artificial intelligence to analyze the content of the image and correct skewed perspective in images. For example, to create level horizons.
* **Lightroom presets**: Applies a user-defined look to images to achieve a consistent appearance using custom-made presets.
* **Image Cutout**: Utilizes artificial intelligence to create selection around salient objects and remove background with a single command.
* **Image Mask**: Utilizes artificial intelligence to create mask around salient objects with a single command.
* **Photoshop Actions**: Applies a series of tasks (in Photoshop) to a file or a batch of files.
* **Smart Object Replacement**: Performs personalization at scale by allowing you to swap images while retaining all effects and adjustment applied within a PSD file.

## Use a processing profile to process assets {#process-assets}

To use processing profiles to automatically create variations, follow these steps:

1. Contact [Adobe Customer Care](https://experienceleague.adobe.com/#support) to receive the license.

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Processing Profiles]**.

1. Select **[!UICONTROL Create]**, and specify a **[!UICONTROL Name]**.

1. Select the **[!UICONTROL Creative]** tab, specify the output folder, select **[!UICONTROL Add New]** to add a creative configurations. 

1. Provide **[!UICONTROL Rendition Name]** (or output name), **[!UICONTROL Extension]** (or file type), select **[!UICONTROL Quality]** (or output parameters), select Includes and Excludes MIME type lists (or input asset filter), and select the required creative operation.

1. Some operations require an additional parameter (asset). Provide values for such additional parameters if required.

1. Add more creative operations as a part of the same processing profile or Save the profile.

1. Apply the processing profile to a folder. On a folder's **[!UICONTROL Properties]** page, select **[!UICONTROL Asset Processing]**, and select the processing profile to apply.

After the processing profile is applied to a DAM folder, all the assets uploaded or updated in this folder execute the defined operations in addition to the standard processing. The sub-folders inherit the same profiles as applied on the parent folders. Users can override this inheritance.

To process the existing assets, select the assets, select **[!UICONTROL Reprocess]** option, and then select the required processing profile.

## Tips and limitations {#limitations-best-practices}

* [!DNL Experience Manager] limits the asset processing to 300 requests per minute per environment and 700 requests per minute per organization.
* File size is limited to 4 GB for [!DNL Adobe Photoshop] API operations, and 1 GB for [!DNL Adobe Lightroom] operations.

>[!MORELIKETHIS]
>
>* [Configure and use asset microservices via processing profiles](/help/assets/asset-microservices-configure-and-use.md).
>* [Integrate [!DNL Experience Manager] with [!DNL Creative Cloud]](/help/assets/aem-cc-integration-best-practices.md).
