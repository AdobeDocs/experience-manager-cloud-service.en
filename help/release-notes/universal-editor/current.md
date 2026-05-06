---
title: Universal Editor 2026.05.07 Release Notes
description: These are the release notes for the 2026.05.07 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2026.05.07 Release Notes {#release-notes}

These are the release notes for the 7 May 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What's New {#what-is-new}

* You can now [drag-and-drop components in the editor to move them.](/help/sites-cloud/authoring/universal-editor/authoring.md#drag-and-drop-move)
* A service worker has been introduced to reduce latency between the Universal Editor UI and the backend systems.
* All adapters for Content Fragments (AEM 6.5, OpenAPI and GraphQL) now include the filters for the asset selector to ensure consistency and users being able to select allowed assets only.
* `content:patch` intent is now provided.
* To help with accessibility, author flow and landmarks have been defined.

## Other Upcoming Improvements {#other-improvements}

* Unnecessary type assertions in `assignImageDimensionFields` were removed.
* And issue was fixed where the server-side handling of the `add` operation iterated the string value, treating it as an object instead of a patch.
