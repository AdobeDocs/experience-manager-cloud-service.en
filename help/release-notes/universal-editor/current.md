---
title: Universal Editor 2025.03.10 Release Notes
description: These are the release notes for the 2025.03.10 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2025.03.10 Release Notes {#release-notes}

These are the release notes for the 10 March 2025 release of the Universal Editor.

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page](/help/release-notes/release-notes-cloud/release-notes-current.md).

## What's New {#what-is-new}

* [Moving components between containers](/help/sites-cloud/authoring/universal-editor/authoring.md#reordering-components) now observes the component filter of the target container.
  * There is no longer a requirement to have the same [filter definition](/help/implementing/universal-editor/filtering.md) in place for both target and destination containers in order to move the component between the containers.
* Universal Editor Service observes the [lock status of a page](/help/sites-cloud/authoring/sites-console/managing-pages.md#locking-a-page) and only writes to pages which are not locked or are locked by the user.

## Other Improvements {#other-improvements}

* Fixes were made to correct validation for headless-canvas.

## Deprecation {#deprecation}

* The `universal-editor-cors` library provided via npm or `https://unviersal-editor-service.experiencecloud.live/corslib/*` should no longer be used.
  * A script tag pointing to `https://universal-editor-service.adobe.io/cors.js` should be used instead.
  * See the [Universal Editor Overview for AEM Developers](/help/implementing/universal-editor/developer-overview.md) for details on how to properly instrument your page for use with the Universal Editor.
  * Users will see a deprecation message once per day if the wrong method is used.
