---
title: Universal Editor 2026.10.08 Release Notes
description: These are the release notes for the 2026.10.08 release of the Universal Editor.
feature: Release Information
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: ed762d86-a04b-452b-a08f-86359bb8ff27
    internal-label: Configuration and operations
subfeature_v2:
  - id: c21ccc2b-e0c8-4853-bf41-f12259ed93f8
    internal-label: Release information
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---

# Universal Editor 2026.10.08 Release Notes {#release-notes}

These are the release notes for the 8 October 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## New Features {#what-is-new}

* Authors can choose custom styles in the in-context rich text editor.
* Rich text asset selection now supports configured remote asset sources.
* Asset filters can be configured globally in `filter-definition.json`. 
* Extensions can customize the properties panel header through a new extension point.
* Number fields now support custom validation error messages.
* Text, combo box, and select fields now display configured placeholder text in their components.
* Select and multiselect menus share consistent sizing behavior that keeps their overlays within the editor area.

## Other Improvements {#other-improvements}

* Copying content now targets the correct container when multiple containers share the same resource but use different properties.
* Rich text paragraphs no longer retain unwanted leading non-breaking spaces. 
* Rich text components were updated to include the paragraph-spacing correction and additional rich text fixes.
* The component picker sidebar and layout now fill the available height. 
* Overlay labels no longer wrap over small editable elements.
* Drag previews for multiple selections stay within the picker's bounds. 
* Asset reference validation now respects the field's configured filter.
