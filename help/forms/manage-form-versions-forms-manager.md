---
title: Manage form versions in Forms Manager
description: Learn to create and manage versions of Adaptive Forms, form fragments, themes, and other assets in the Forms Manager UI.
feature: Adaptive Forms, Core Components, Foundation Components
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: cd2c6e15-99a6-4b4e-bfd1-8291a2001ebe
---
# Manage Form Assets Versions in Forms Manager UI

**Forms Manager now supports versioning for form assets**, giving you full control over how your assets evolve over time. Directly from the **Forms Manager User Interface (UI)**, you can create versions, review a complete **version history**, and **restore** earlier versions whenever needed. Versioning brings the reliability of source-control-style workflows to form asset management, so changes are tracked, recoverable, and auditable.

## Key Capabilities

The versioning feature in the Forms Manager UI provides three core capabilities:

- **Create versions** — Capture a snapshot of a form asset at any point, preserving its exact state so that current work is never lost as edits continue.
- **View version history** — Browse a chronological record of all saved versions of a form asset, making it easy to see how the asset has changed across successive updates.
- **Restore earlier versions** — Roll a form asset back to a previously saved state with a single action, instantly recovering earlier content when a change needs to be undone.

## Why Version Form Assets

Versioning protects form assets against accidental changes, unwanted edits, and configuration errors. Because every saved version remains available in the version history, you can compare progress over time and confidently revert to a known-good state if a newer change introduces problems. This ensures that experimentation and iteration carry less risk, since an earlier working version can always be restored.

Common use cases include recovering a form asset after an unintended edit, returning to a stable configuration following a problematic update, and maintaining a traceable record of how a form asset was built and modified. By keeping version management inside the Forms Manager UI, these tasks are handled in one place without additional tooling.

## Supported asset types {#supported-asset-types}

Version management is supported for the following asset types in Adobe Experience Manager (AEM) Forms. You can create, track, and manage versions for each type listed below, ensuring that changes to forms and their components are captured and recoverable over time:

| Asset type | Description |
|---|---|
| Adaptive Forms (Core Components) | Adaptive Forms built using Core Components |
| Adaptive Forms (Foundation Components) | Adaptive Forms built using Foundation Components |
| Form Fragments | Reusable form sections shared across multiple forms |
| Themes | Visual style definitions applied to Adaptive Forms |
| XDP templates | XFA based form templates |
| Binary assets | Other files stored under the forms DAM repository |

These asset types cover the primary building blocks of Adaptive Forms. **Adaptive Forms** can be constructed using either **Core Components** or **Foundation Components**, both of which support versioning. **Form Fragments** are reusable form sections shared across multiple forms, so versioning them helps maintain consistency wherever the fragment is embedded. **Themes** define the visual style applied to Adaptive Forms. **XDP templates** are **XFA (XML Forms Architecture)** based form templates, while **Binary assets** are other files stored under the forms **DAM (Digital Asset Management)** repository. By supporting versioning across all of these types, teams can revert to earlier states, audit changes, and manage form development with greater reliability.

## Create a version {#create-version-forms-manager}

A version is a saved snapshot of a form asset at a specific point in time, capturing its current state so you can track changes and restore earlier iterations if needed. To create a version of a form asset:

1. Navigate to **[!UICONTROL Adobe Experience Manager]** > **[!UICONTROL Forms]** > **[!UICONTROL Forms & Documents]**.
1. Select the form or asset.
    ![Save as Version](/help/forms/assets/create-version.png)
1. In the left panel, select **[!UICONTROL Timeline]**.
1. Click **[!UICONTROL Save as Version]** in the timeline toolbar. This preserves the current state of the asset as a distinct, restorable snapshot.
    ![Save as Version2](/help/forms/assets/create-version1.png)
1. Enter a **[!UICONTROL Label]** and an optional **[!UICONTROL Comment]** to describe the changes. A clear label makes the version easy to identify later, and the comment documents what was modified for future reference.
1. Click **[!UICONTROL Create]**.

The version appears in the timeline panel with its label, comment, and timestamp. Because each version records this metadata, you can review the full revision history of the asset and revert to any earlier version directly from the timeline.

## Version an asset during upload {#version-on-upload}

Uploading an asset with the same name as an existing asset **creates a new version automatically** in Forms Manager. This same-name upload behavior means you do not need to manually manage revisions—each replacement is captured as a distinct version, preserving the earlier state of the asset for future reference.

### How versioning works during upload

When you upload an asset that shares its name with an existing asset, Forms Manager displays a **File Upload** dialog that lists the assets to be updated. The dialog identifies each affected asset so you can confirm the update before it is applied. The dialog shows the following details for each asset:

- **Asset name** — the name of the asset being replaced.
- **Section** — the section in which the asset resides.
- **Path** — the full location of the asset within Forms Manager.

![File Upload dialog showing versioned upload](/help/forms/assets/version-upload.png)

When an asset with the same name already exists, the upload replaces the existing asset and **creates a new version automatically**. Because the prior state is retained as a version rather than discarded, the previous content remains recoverable, giving you a complete history of every change made to that asset.

### Viewing the new version

You can view each newly created version in the asset's timeline. The timeline records the sequence of versions for the asset, allowing you to track how the asset has changed over successive uploads. This provides a clear audit trail, making it straightforward to review earlier versions and confirm which upload produced the current state of the asset.

## View version history {#view-version-history}

The version history of an asset provides a complete, chronological record of every change made to that asset in Forms Manager. Reviewing this history allows you to track how an asset has evolved over time, identify who made specific modifications, and determine when changes occurred. This makes version history an essential tool for auditing edits, understanding revision context, and identifying earlier states of an asset.

To view the version history of an asset:

1. Select the asset in Forms Manager.
1. In the left panel, select **[!UICONTROL Timeline]**.

The **Timeline** panel displays all version entries alongside related activity events, giving you a unified view of both the saved versions and the actions performed on the asset. A version entry represents a specific saved state of the asset, while an activity event records an action or update associated with the asset over its lifecycle.

![Version History](/help/forms/assets/version-history.png)

Each version entry shows the following details:

- **Label** — the name or identifier assigned to the version, making it easy to distinguish one version from another.
- **Comment** — the note added when the version was created, providing context about what changed and why.
- **Author** — the user who created or modified the version, establishing accountability for each change.
- **Timestamp** — the date and time the version was recorded, allowing you to place each change accurately within the asset's revision history.

Because the Timeline presents this information in chronological order, you can quickly trace the full sequence of changes, review activity events in context, and pinpoint the exact version you need to reference or restore.

## Restore a previous version {#restore-version}

The **version restore** feature returns an asset to any previously saved state, allowing you to undo unwanted changes and recover earlier content. To restore an asset to an earlier version:

1. Select the asset in Forms Manager.
1. In the left panel, select **[!UICONTROL Timeline]**.
1. Select the version that you want to restore.
    ![Revert Version](/help/forms/assets/revert-version.png)
1. Click **[!UICONTROL Revert to this Version]**.

The **[!UICONTROL Timeline]** panel lists the saved versions of the asset in chronological order, so you can identify and select the exact version you want. Selecting **[!UICONTROL Revert to this Version]** restores the chosen version as the current active version of the asset.

>[!NOTE]
>
>Images cannot be reverted to a previous version. Because of this limitation, version restore applies to all other asset types, including Adaptive Forms, form fragments, themes, and XDP templates, which fully support restoring a previous version.

## See Also {#see-also}

Explore these related resources for managing Adaptive Forms across their full lifecycle in Adobe Experience Manager (AEM):

* [Versioning, reviewing, and commenting on an Adaptive Form](/help/forms/add-comments-annotations-versioning-adaptive-form-core-components.md) — track successive versions, review changes, and collaborate through inline comments and annotations before finalizing a form.
* [Import and export forms and related assets](/help/forms/import-export-forms-templates.md) — migrate forms, templates, and related assets between environments to reuse and share form content efficiently.
* [Publishing and unpublishing forms](/help/forms/publishing-unpublishing-forms.md) — control when a form becomes available to end users and remove it from the published environment when it is no longer needed.
