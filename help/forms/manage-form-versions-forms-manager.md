---
title: Manage form versions in Forms Manager
description: Learn to create and manage versions of Adaptive Forms, form fragments, themes, and other assets in the Forms Manager UI.
feature: Adaptive Forms, Core Components, Foundation Components
role: User, Developer, Admin
exl-id: manage-form-versions-fm
---
# Manage form versions in Forms Manager

<span class="preview"> This feature is available through the Early Access program. To request access, send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com). </span>

Forms Manager now supports versioning for form assets. You can create versions, view version history, and restore earlier versions of your assets from the Forms & Documents console.

## Supported asset types {#supported-asset-types}

You can create and manage versions for the following asset types:

| Asset type | Description |
|---|---|
| Adaptive Forms (Core Components) | Adaptive Forms built using Core Components |
| Adaptive Forms (Foundation Components) | Adaptive Forms built using Foundation Components |
| Form Fragments | Reusable form sections shared across multiple forms |
| Themes | Visual style definitions applied to Adaptive Forms |
| XDP templates | XFA based form templates |
| Binary assets | Other files stored under the forms DAM repository |

## Create a version {#create-version-forms-manager}

To create a version of a form asset:

1. Navigate to **[!UICONTROL Adobe Experience Manager]** > **[!UICONTROL Forms]** > **[!UICONTROL Forms & Documents]**.
1. Select the form or asset.
1. In the left panel, select **[!UICONTROL Timeline]**.
1. Click **[!UICONTROL Save as Version]** in the timeline toolbar.
1. Enter a **[!UICONTROL Label]** and an optional **[!UICONTROL Comment]** to describe the changes.
1. Click **[!UICONTROL Create]**.

The version appears in the timeline panel with its label, comment, and timestamp.

## Version an asset during upload {#version-on-upload}

When you upload a file that already exists in Forms Manager, you are prompted to choose how to handle the duplicate:

* **Override**: Replaces the existing file with the uploaded content. The metadata is preserved.
* **Create Version**: Saves the existing asset as a version before replacing it with the uploaded content.

This applies to individual file uploads as well as folder or ZIP uploads. When a folder upload contains assets that match existing paths, you are prompted to choose whether to version all matching assets.

## View version history {#view-version-history}

To view the version history of an asset:

1. Select the asset in Forms Manager.
1. In the left panel, select **[!UICONTROL Timeline]**.

The timeline displays all version entries along with activity events. Each entry shows the label, comment, author, and timestamp.

## Restore a previous version {#restore-version}

To restore an asset to an earlier version:

1. Select the asset in Forms Manager.
1. In the left panel, select **[!UICONTROL Timeline]**.
1. Select the version that you want to restore.
1. Click **[!UICONTROL Revert to this Version]**.

>[!NOTE]
>
>For Adaptive Forms that have both a DAM node and a content page, reverting a version restores both components together to ensure consistency.

## See Also {#see-also}

* [Versioning, reviewing, and commenting on an Adaptive Form](/help/forms/add-comments-annotations-versioning-adaptive-form-core-components.md)
* [Import and export forms and related assets](/help/forms/import-export-forms-templates.md)
* [Publishing and unpublishing forms](/help/forms/publishing-unpublishing-forms.md)
