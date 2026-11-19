---
title: Universal Editor 2026.11.19 Release Notes
description: These are the release notes for the 2026.11.19 release of the Universal Editor.
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

# Universal Editor 2026.11.19 Release Notes {#release-notes}

These are the release notes for the 19 November 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What's New {#what-is-new}

* Native WebMCP support was added so the editor’s tools (including new undo and redo tools) are registered through `document.modelContext` when the browser provides it, alongside the existing integration.
* A variables dropdown is now available in the rich text editor for inserting variables into rich text fields for Content Fragments.

## Other Improvements {#other-improvements}

* The editor now clears a selection whose component no longer exists after navigating to a new page and keeps selections whose components appear in a later repaint.
* Native AEM header buttons now stay available on pages that contain nested Experience Fragments or Content Fragments.
