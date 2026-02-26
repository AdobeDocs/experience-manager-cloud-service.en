---
title: Universal Editor 2026.02.26 Release Notes
description: These are the release notes for the 2026.02.26 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2026.02.26 Release Notes {#release-notes}

These are the release notes for the 26 February 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page](/help/release-notes/release-notes-cloud/release-notes-current.md).

## What's New {#what-is-new}

* Descriptions were added to all schema fields to help the developers generate model/filter/component definition files.
* Multi-field updates to Content Fragments are now supported for in-context edits.


## Early Adoption Features {#early-adopter}

If you are interested in testing the upcoming features listed below and sharing your feedback, please send an email to your Adobe Customer Success Manager from the email address associated with your Adobe ID. 

* Shallow copy has been implemented for Content Fragments.

## Other Improvements {#other-improvements}

* Editor no longer defaults content to `{}` before content arrives, preventing data loss in certain situations.
* Persistence of data when field is in focus was made more robust.
* Changes are no longer lost in certain situations when editing in the left panel and then selecting another item in the editor window.
* Manual css import is no longer required when using `headless-canvas`.
* For CORS purposes the correct endpoints are used for stage, preview, and prod.
* Description was added to all schema fields.
* Fixed problem with Open API in the RTE.
