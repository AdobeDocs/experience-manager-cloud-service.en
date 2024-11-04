---
title: Universal Editor 2024.09.3 Release Notes
description: These are the release notes for the 2024.09.3 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2024.09.3 Release Notes {#release-notes}

These are the release notes for the 3 September 2024 release of the Universal Editor.

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What’s New {#what-is-new}

* **`rootPath` now available for the content picker**: The content picker can now be provided with a `rootPath` to present the user with a targeted selection of content when using [AEM Content,](/help/implementing/universal-editor/field-types.md#aem-content) [Content Fragment,](/help/implementing/universal-editor/field-types.md#content-fragment) and [Experience Fragment](/help/implementing/universal-editor/field-types.md#experience-fragment) field types.
  * Content selection is thereby limited to content in the specified path and any subdirectories.

## Early Adoption Program for 6.5 Support {#early-adoption}

The Universal Editor is now available for headless use cases when using AEM 6.5 as part of an early adopter program.

If you are interested in testing this new feature and sharing your feedback, please send an email to your Adobe representative from the email address associated with your Adobe ID. 

## Bug Fixes {#bug-fixes}

* **Cross-Container Drag &amp; Drop**: [Moving components between different containers via drag-and-drop](/help/sites-cloud/authoring/universal-editor/authoring.md#reordering-components) now respects [component filters](/help/implementing/universal-editor/customizing.md#filtering-components) in both the source and target.
