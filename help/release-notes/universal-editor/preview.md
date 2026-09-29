---
title: Universal Editor Preview Release Notes
description: These are the release notes for the preview release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: e8d031aa-4676-4e45-977b-e5dffcc404c4
---

# Universal Editor Preview Release Notes {#preview}

These are the release notes for the **preview version** of the Universal Editor. These features are currently available in your Universal Editor's **preview environment**. These features are scheduled to be released to general availability on 1 October 2026.

These **preview** release notes are provided as a convenience so you know what changes to the Universal Editor are upcoming and you can test them by [switching to your preview version.](/help/sites-cloud/authoring/universal-editor/navigation.md#user-properties)

>[!TIP]
>
>For the **current release notes** for the Universal Editor, please see the document [Universal Editor Release Notes.](/help/release-notes/universal-editor/current.md)

>[!NOTE]
>
>The content of the actual release as well as the release date are subject to change.

## Upcoming Features {#upcoming-features}

* A `getPageDom` method was added to the extensibility remote app API, letting connected apps read the current page's rendered DOM.
* The custom class markers (dashed box and label chip) are now hidden from the in-context rich text editor so they no longer decorate the rendered page. The class picker remains available in both editors.
* Global ad item actions (add/delete) were added to the select renderer in the canvas.

## Upcoming Changes {#upcoming-improvements}

* The new general reference renderers now fall back to the legacy reference renderers on AEM 6.5, since the new renderers are not yet supported in 6.5.
* Single reference fields now render as a proper single field and are no longer forced into a multi-field shape when the general asset renderer feature is enabled.
* Invalid rich text fields in the property rail are now highlighted with a red border.
* The clear queue button in the debug events panel was repositioned so it aligns with the panel's top.
* The unpublish action now only reports the target resource itself and no longer includes pages that merely reference it.
