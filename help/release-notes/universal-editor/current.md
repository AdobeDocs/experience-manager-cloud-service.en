---
title: Universal Editor 2026.11.26 Release Notes
description: These are the release notes for the 2026.11.26 release of the Universal Editor.
feature: Release Information
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: ed762d86-a04b-452b-a08f-86359bb8ff27
    internal-label: Configuration and operations
subfeature_v2:
  - id: c21ccc2b-e0c8-4853-bf41-f12259ed93f8
    internal-label: Release information
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---

# Universal Editor 2026.11.26 Release Notes {#release-notes}

These are the release notes for the 26 November 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What's New {#what-is-new}

* Authors can open a referenced page or Experience Fragment in its own editor using the reference field’s **Open** button.
  * Experience Fragments open the selected variation otherwise the main variation is opened if no variation is selected.
* Remote asset URLs with query parameters are now kept intact in AEM as a Cloud Service and AEM 6.5 output.
* Certain common service errors now report a clear cause instead of a 500.
  * Replacing an object field with a text value no longer fails.
  * Invalid connection URIs and URNs now return 400.
  * AEM login pages and unreachable backends give descriptive errors.

## Other Improvements {#other-improvements}

