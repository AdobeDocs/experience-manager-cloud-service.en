---
title: Universal Editor 2026.10.01 Release Notes
description: These are the release notes for the 2026.10.01 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2026.10.01 Release Notes {#release-notes}

These are the release notes for the 1 October 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## New Features {#what-is-new}

* A `getPageDom` method was added to the extensibility remote app API, letting connected apps read the current page's rendered DOM.
* The custom class markers (dashed box and label chip) are now hidden from the in-context rich text editor so they no longer decorate the rendered page. The class picker remains available in both editors.
* Global ad item actions (add/delete) were added to the select renderer in the canvas.

## Other Improvements {#other-improvements}

* The new general reference renderers now fall back to the legacy reference renderers on AEM 6.5, since the new renderers are not yet supported in 6.5.
* Single reference fields now render as a proper single field and are no longer forced into a multi-field shape when the general asset renderer feature is enabled.
* Invalid rich text fields in the property rail are now highlighted with a red border.
* The clear queue button in the debug events panel was repositioned so it aligns with the panel's top.
* The unpublish action now only reports the target resource itself and no longer includes pages that merely reference it.