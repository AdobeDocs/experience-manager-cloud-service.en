---
title: Universal Editor 2026.06.25 Release Notes
description: These are the release notes for the 2026.06.25 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2026.06.25 Release Notes {#release-notes}

These are the release notes for the 25 June 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What's New {#what-is-new}

* A new button has been added to the toolbar to access AEM Sites console.
  * This brings the functionality of the former **AEM Site Admin Extension** [extension](/help/implementing/universal-editor/extending.md) natively to the Universal Editor.
  * The button opens the current AEM page in the [Sites console,](/help/sites-cloud/authoring/universal-editor/authoring.md#sites-console) or the [Experience Fragments console](/help/sites-cloud/authoring/fragments/experience-fragments.md) for `/content/experience-fragments` paths.
  * The button is hidden for DAM paths (`/content/dam`) and when no unique AEM page can be determined from the current editables.
* Single-character shortcuts now work better with accessibility technologies.

## Other Improvements {#other-improvements}

* Numerous buttons now correctly have accessible names.
* A problem with persisting certain Content Fragments after selecting them with a picker has been fixed.
