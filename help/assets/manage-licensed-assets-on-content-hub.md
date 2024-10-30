---
title: Manage Licensed Assets on Content Hub
description: Learn about various metadata management and editing methods
---

# Manage Licensed Assets on Content Hub {#manage-licensed-assets-on-content-hub}

As an administrator, edit the metadata form to include the asset license field so that it displays in Asset properties in AEM author environment. You can then approve the asset as well as its license to make the asset licensed and available on Content Hub.

Execute the following steps:

1. Edit the metadata form to include a new Text field to include the license details. Map the text field to `./jcr:content/metadata/dc:license` property. For more information on how to add fields to a metadata form and define properties, see [Setup Metadata Forms](/help/assets/metadata-assets-view.md#metadata-forms).
![zip extraction](/help/assets/assets/metadata-form-edit.png)
1. Apply the metadata form to the asset folder to apply the settings incorporated in step 1. For information on how to assign metadata form to the asset folder, see [Assign metadata form to a folder](/help/assets/metadata-assets-view.md#metadata-forms).
1. Select the asset and click **Details** to view its properties. In the license field added in Step 1, define the absolute path for the asset license. The Content Hub absolute path follows this standard pattern: `/content/dam/(The asset's folder hierarchy within the DAM repository)/(asset_name).(file_extension)`. For example, /content/dam/teamA/projects/documents/file1.pdf
![absolute path](/help/assets/assets/absolute-path.png)
1. Approve the asset to make it available in Content Hub and click **Save**. For information on how to approve an asset, see [Set asset status](/help/assets/manage-organize-assets-view.md#set-asset-status).
1. Similar to step 4, [approve the licensed asset](/help/assets/manage-organize-assets-view.md#set-asset-status) defined in Step 3.

