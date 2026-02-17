---
title: Universal Editor Preview Release Notes
description: These are the release notes for the preview release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: e8d031aa-4676-4e45-977b-e5dffcc404c4
---
# Universal Editor Preview Release Notes {#preview}

These are the release notes for the **preview version** of the Universal Editor. These features are currently available in your Universal Editor's **preview environment**. These features are scheduled to be released to general availability on 19 February 2026.

These **preview** release notes are provided as a convenience so you know what changes to the Universal Editor are upcoming and you can test them by [switching to your preview version.](/help/sites-cloud/authoring/universal-editor/navigation.md#user-properties)

>[!TIP]
>
>For the **current release notes** for the Universal Editor, please see the document [Universal Editor Release Notes.](/help/release-notes/universal-editor/current.md)

>[!NOTE]
>
>The content of the actual release as well as the release date are subject to change.

## Upcoming New Features {#what-is-new}

* Improvements have been made to the RTE.
  * Hiding toolbar items in the in context RTE is now supported.
  * Wrapping text inside tables with paragraphs is now supported.
  * Unsupported RTE tags are now preserved.
  * RTE logic is now served from a separate file.
  * Tables can now be created as well edited using the RTE.
* If no label is set, the component title from the component definition is now used.
* `setEditorMode` is now available via extensions.

## Upcoming Improvements {#other-improvements}

* Copy-and-paste functionality between pages has been fixed.
* `universal-editor-extensibility` has been shifted to `universal-editor`.
* The number of requests to the extensions endpoint has been reduced.
* RemoteApp unmounts has been reduced from three to one.
* RTE endpoints are now served for the in-place editor.
* Editing nested fields no longer results in overwriting peer entries from those structures.
* Mandatory RTE fields can no longer be saved as empty.
* In-place formatting is no longer improperly applied when adding links after formatting.
