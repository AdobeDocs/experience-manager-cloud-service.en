---
title: Configure asset upload restrictions
description: Configure Adobe Experience Manager Assets to restrict the type of assets that users can upload based on the MIME type. It helps prevent accidental uploads of undesired format and malicious files. 
---
# Configure asset upload restrictions {#configure-asset-upload-restrictions}

You can configure Adobe Experience Manager Assets to restrict the type of assets that users can upload based on the MIME type. 

>[!IMPORTANT]
>
>By default, Experience Manager Assets allows users to upload assets of all MIME types. However, you can configure the settings to restrict users to upload files of specific MIME types only.

## Prerequisites {#prerequisites-asset-upload-restrictions}

You must have administrator privileges to configure asset upload restrictions.

## Apply restrictions for asset uploads {#apply-restrictions-asset-uploadsssssss}

To configure [!DNL Experience Manager] to restrict users to upload files of specific MIME types:

1. Navigate to **[!UICONTROL Tools > Assets > Assets Configurations]**.

1. Click **[!UICONTROL Upload Restrictions]**.

1. Click **[!UICONTROL Add]** to define the allowed MIME types.

1. Specify the MIME type in the text box. You can click **[!UICONTROL Add]** again to specify more allowed MIME types. You can also click ![delete icon](assets/delete-icon.svg) to delete any MIME type from the list.

1. Click **[!UICONTROL Save]**.

**Example 1: Allow upload of all images and PDF files to Experience Manager Assets**

To allow the upload of images in all formats and PDF files to Experience Manager Assets, do the following settings:

   ![Asset upload restrictions](assets/asset-upload-restrictions.png)

`image/*` as the MIME type allows the upload of images in all formats. `application/pdf` as the MIME type allows the upload of PDF files to Experience Manager Assets.

**Example 2: Allow upload of specific image formats to Experience Manager Assets**

To add specific image formats to the allowed MIME types and to restrict uploading all other asset formats, do the following settings:

![Asset restrictions](assets/asset-restrictions.png)

Based on the settings depicted in the image, you can upload images in .JPG, .PNG, and .GIF formats to Experience Manager Assets.




