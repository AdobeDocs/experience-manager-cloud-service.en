---
title: Universal Editor 2026.10.29 Release Notes
description: These are the release notes for the 2026.10.29 release of the Universal Editor.
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

# Universal Editor 2026.10.29 Release Notes {#release-notes}

These are the release notes for the 29 October 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What's New {#what-is-new}

* Native multi-site management (MSM) support has been added to the editor, with a header menu icon showing inheritance status, link and unlink (shallow and deep) actions, and rollout. It also adds an MSM side panel, an updated icon for deeply broken inheritance, and localization updates.
* The AEM Workflow extension has been added natively to the editor.
* The rich text editor component now supports custom keyboard shortcuts.

## Other Improvements {#other-improvements}

* The properties rail now properly keeps focus on a newly selected component when a slow patch response arrives after the selection has changed and undo/redo now restores the component that was actually edited.
* The plain-text configuration of a field is now respected during inline editing, so the rich-text toolbar and actions stay disabled for plain-text fields even when filters are configured.
* The tab key is no longer trapped when no component is selected, and a sensible tab order is now used for overlays and the app iframe.
* Reference fields no longer fall back to older pickers on AEM Cloud Service pages with no containers or content from multiple pages.