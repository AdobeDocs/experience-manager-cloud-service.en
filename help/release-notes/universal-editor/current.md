---
title: Universal Editor 2026.05.28 Release Notes
description: These are the release notes for the 2026.05.28 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2026.05.28 Release Notes {#release-notes}

These are the release notes for the 28 May 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What's New {#what-is-new}

* A new button has been added to the toolbar [to access AEM page properties.](/help/sites-cloud/authoring/universal-editor/authoring.md#page-properties)
  * This brings the functionality of the former `aem-page-properties` [extension](/help/implementing/universal-editor/extending.md) natively to the Universal Editor.
  * The button is shown only when the remote page has a [connection with protocol](/help/implementing/universal-editor/component-definition.md#plugins) `aem` or `xwalk` and a unique page path can be resolved from the current editable.

## Other Improvements {#other-improvements}

* The default background color of the edit canvas is now white (#FFFFFF) when the app sets no background color of its own.
* An issue was fixed where copy and pasting across pages was not working. 
