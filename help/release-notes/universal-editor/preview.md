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

These are the release notes for the **preview version** of the Universal Editor. These features are currently available in your Universal Editor's **preview environment**. These features are scheduled to be released to general availability on 15 October 2026.

These **preview** release notes are provided as a convenience so you know what changes to the Universal Editor are upcoming and you can test them by [switching to your preview version.](/help/sites-cloud/authoring/universal-editor/navigation.md#user-properties)

>[!TIP]
>
>For the **current release notes** for the Universal Editor, please see the document [Universal Editor Release Notes.](/help/release-notes/universal-editor/current.md)

>[!NOTE]
>
>The content of the actual release as well as the release date are subject to change.

## Upcoming Features {#upcoming-features}

* The AI agent can now preview content and makes more precise updates, keeping nested content intact when it updates components.

## Upcoming Changes {#upcoming-improvements}

* URLs inside Unified Shell no longer pick up repeated shell or embedded-URL prefixes.
* The shell's force-reload flag is no longer passed through to the page's search parameters.
* Drag and drop no longer allows moving components onto targets that are not containers.
* Content updates made through WebMCP now fall back to the author DAM path for assets that haven't been activated.
* Icons in extension-provided renderers now receive their props correctly.
* Structured log events from Universal Editor Service now include a UTC timestamp.
