---
title: Universal Editor Preview Release Notes
description: These are the release notes for the preview release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: e8d031aa-4676-4e45-977b-e5dffcc404c4
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

# Universal Editor Preview Release Notes {#preview}

These are the release notes for the **preview version** of the Universal Editor. These features are currently available in your Universal Editor's **preview environment**. These features are scheduled to be released to general availability on 22 October 2026.

These **preview** release notes are provided as a convenience so you know what changes to the Universal Editor are upcoming and you can test them by [switching to your preview version.](/help/sites-cloud/authoring/universal-editor/navigation.md#user-properties)

>[!TIP]
>
>For the **current release notes** for the Universal Editor, please see the document [Universal Editor Release Notes.](/help/release-notes/universal-editor/current.md)

>[!NOTE]
>
>The content of the actual release as well as the release date are subject to change.

## Upcoming Features {#upcoming-features}

* Native multi-site management (MSM) support has been added to the editor, with a header menu icon showing inheritance status, link and unlink (shallow and deep) actions, and rollout. It also adds an MSM side panel, an updated icon for deeply broken inheritance, and localization updates.
* The AEM Workflow extension has been added natively to the editor.
* The rich text editor component now supports custom keyboard shortcuts.

## Upcoming Changes {#upcoming-improvements}

* The properties rail now properly keeps focus on a newly selected component when a slow patch response arrives after the selection has changed and undo/redo now restores the component that was actually edited.
* The plain-text configuration of a field is now respected during inline editing, so the rich-text toolbar and actions stay disabled for plain-text fields even when filters are configured.
* The tab key is no longer trapped when no component is selected, and a sensible tab order is now used for overlays and the app iframe.
