---
title: Universal Editor Preview Release Notes
description: These are the release notes for the preview release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: e8d031aa-4676-4e45-977b-e5dffcc404c4
---

# Universal Editor Preview Release Notes {#preview}

These are the release notes for the **preview version** of the Universal Editor. These features are currently available in your Universal Editor's **preview environment**. These features are scheduled to be released to general availability on 7 May 2026.

These **preview** release notes are provided as a convenience so you know what changes to the Universal Editor are upcoming and you can test them by [switching to your preview version.](/help/sites-cloud/authoring/universal-editor/navigation.md#user-properties)

>[!TIP]
>
>For the **current release notes** for the Universal Editor, please see the document [Universal Editor Release Notes.](/help/release-notes/universal-editor/current.md)

>[!NOTE]
>
>The content of the actual release as well as the release date are subject to change.

## Upcoming Features {#upcoming-features}

* A service worker has been introduced to reduce latency between the Universal Editor UI and the backend systems.
* All adapters for Content Fragments (AEM 6.5, OpenAPI and GraphQL) now include the filters for the asset selector to ensure consistency and users being able to select allowed assets only.
* `content:patch` intent is now provided.
* To help with accessibility, author flow and landmarks have been defined.

## Other Upcoming Improvements {#other-improvements}

* Unnecessary type assertions in `assignImageDimensionFields` were removed.
* And issue was fixed where the server-side handling of the `add` operation iterated the string value, treating it as an object instead of a patch.
