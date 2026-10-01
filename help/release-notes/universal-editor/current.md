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

* New reference renderers for the [AEM content,](/help/implementing/universal-editor/field-types.md#aem-content) [Content Fragment,](/help/implementing/universal-editor/field-types.md#content-fragment) [Experience Fragment,](/help/implementing/universal-editor/field-types.md#experience-fragment) and [generic reference types](/help/implementing/universal-editor/field-types.md#reference) were added.
  * Please contact Adobe if you would like to use these new renderers.
* Extensions can retrieve the page's HTML through the new `getPageDom` API. 
* Custom CSS class markers are hidden in the in-context rich text editor for a cleaner editing experience.
* Select fields now support field-level and per-item actions.

## Other Improvements {#other-improvements}

* Unpublishing a page no longer includes other pages that merely reference it.
* Enabling the new asset picker no longer incorrectly turns single-value reference fields into multifields.
* Invalid rich text fields now display a red border in the properties panel, with added coverage for required page fields.
* The clear-queue button is positioned correctly in the debug events panel.
* Content Fragment reference fields retain their icon, add/delete actions, and required-value checks after release branch reconciliation.
