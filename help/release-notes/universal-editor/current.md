---
title: Universal Editor 2026.02.19 Release Notes
description: These are the release notes for the 2026.02.19 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2026.02.19 Release Notes {#release-notes}

These are the release notes for the 19 February 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page](/help/release-notes/release-notes-cloud/release-notes-current.md).

## What's New {#what-is-new}

* Improvements have been made to the RTE.
  * [Hiding toolbar items in the in context RTE](/help/implementing/universal-editor/configure-rte.md#common-action-options) is now supported.
  * [Wrapping text inside tables with paragraphs](/help/implementing/universal-editor/configure-rte.md#table-actions) is now supported.
  * Unsupported RTE tags are now preserved.
  * RTE logic is now served from a separate file.
  * [Tables can now be created](/help/sites-cloud/authoring/universal-editor/authoring.md#formatting-options) as well edited using the RTE.
* If no label is set, the component title from the component definition is now used.
* `setEditorMode` is now available via extensions.

## Early Adoption Features {#early-adopter}

If you are interested in testing the upcoming features listed below and sharing your feedback, please send an email to your Adobe Customer Success Manager from the email address associated with your Adobe ID. 

* Shallow copy has been implemented for Content Fragments.

## Other Improvements {#other-improvements}

* RTE endpoints are now served for the in-place editor.
* Editing nested fields no longer results in overwriting peer entries from those structures.
* Mandatory RTE fields can no longer be saved as empty.
* In-place formatting is no longer improperly applied when adding links after formatting.
