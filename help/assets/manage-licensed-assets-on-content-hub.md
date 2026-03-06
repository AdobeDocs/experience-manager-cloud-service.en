---
title: Manage Licensed Assets on Content Hub
description: Learn about adding a license field to the asset metadata form, applying the License metadata property to asset folders, and approving assets with licenses for use.
exl-id: ac3aad9f-c7b3-47a7-9314-a2f8277f0d3e
---
# Manage Licensed Assets on Content Hub {#manage-licensed-assets-on-content-hub}

As an administrator, edit the metadata form to include the asset license field so that it displays in Asset properties in the AEM author environment. You can then approve the asset as well as its license to make the asset licensed and available on Content Hub.

Execute the following steps:

1. Edit the metadata form to include a new text field to include the license details. Map the text field to `dc:license` property. For more information on how to add fields to a metadata form and define properties, see [Setup Metadata Forms](/help/assets/metadata-assets-view.md#metadata-forms).
![zip extraction](/help/assets/assets/metadata-form-edit.png)
1. Apply the metadata form to the asset folder to apply the settings incorporated in step 1. For information on how to assign a metadata form to the asset folder, see [Assign metadata form to a folder](/help/assets/metadata-assets-view.md#metadata-forms).
1. [Approve the licensed PDF](/help/assets/manage-organize-assets-view.md#set-asset-status)
1. Select the asset and click **Details** to view its properties. In the license field added in Step 1, define the absolute path for the asset license that has been approved in Step 3 or already approved earlier. The Content Hub absolute path follows this standard pattern: `/content/dam/(The asset's folder hierarchy within the DAM repository)/(asset_name).(file_extension)`. For example, /content/dam/teamA/projects/documents/file1.pdf
![absolute path](/help/assets/assets/absolute-path.png)
1. Approve the asset to make it available in Content Hub and click **Save**. For information on how to approve an asset, see [Set asset status](/help/assets/manage-organize-assets-view.md#set-asset-status).

## Frequently asked questions {#faqs-manage-licensed-assets-content-hub}

### What is the purpose of managing licensed assets on AEM Assets Content Hub?

Managing licensed assets on Content Hub allows administrators to ensure that only approved assets with valid licenses are available for use, maintaining compliance and proper metadata tracking within the AEM author environment.

### How can I add a license field to asset properties in Experience Manager as a Cloud Service?

You can add a license field to asset properties by editing the metadata form to include a new text field mapped to the `dc:license` property. This field then appears in the asset properties in the AEM Assets author environment.

### How to apply a metadata form to an asset folder to include the license field in asset properties?

Edit the metadata form to include the license field. Apply this metadata form to the desired asset folder to ensure the new settings are incorporated for all assets within that folder.

### How do I specify the license details for an asset?

To specify the license details, select the asset, click **Details** to view its properties, and enter the absolute path of the approved asset license in the license field added to the metadata form.

### What is the required format for the Content Hub absolute path for an asset license?

The Content Hub absolute path should follow the pattern: /content/dam/(The asset's folder hierarchy within the DAM repository)/(asset_name).(file_extension). For example, `/content/dam/teamA/projects/documents/file1.pdf`.

### Why is it important to approve both the asset and its license to make them available on AEM Assets Content Hub?

Approving both the asset and its license ensures that only properly licensed and authorized assets are made available on AEM Assets Content Hub, helping maintain compliance and proper usage rights.

### How do I make an asset available in AEM Assets Content Hub after approving its license?

After defining the license path in the asset's properties, approve the asset and click Save. This action makes the licensed asset available in AEM Assets Content Hub.

### Who is responsible for managing licensed assets in Content Hub?

Administrators are responsible for editing metadata forms, assigning them to asset folders, and approving both assets and their licenses in Content Hub.

### 
