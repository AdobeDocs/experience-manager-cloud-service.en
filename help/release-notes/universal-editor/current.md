---
title: Universal Editor 2024.06.28 Release Notes
description: These are the release notes for the 2024.06.28 release of the Universal Editor.
feature: Release Information
role: Admin
---

# Universal Editor 2024.06.28 Release Notes {#release-notes}

These are the release notes for the 28 June 2024 release of the Universal Editor.

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What's New {#what-is-new}

* **Home**: The recent pages are displayed as a list, without preview images.
* **Location Bar**: Enhanced URL validation was added, enforcing HTTPS URLs and supporting hashes in URLs to account for hash-routed applications.
* **Keyboard Navigation**: The page overlay selection was decoupled from the properties rail focus to improve the keyboard navigation on the page without losing focus.
* **Item Labels**: The fallback value for labels now uses `data-aue-prop` instead of `data-aue-type` for clearer identification in overlays and the content tree.
* **RTE Modal**: A **Cancel** button was added to the rich text editor modal when opening it from the properties panel.
* **UE Service on Node**: HTTP support for the Universal Editor Service was reintroduced, as all HTTPS connections are terminated at the Dispatcher level.
* **Internal Copy API**: An API to the Universal Editor Service to copy components was added, allowing future introduction of toolbar options to copy and duplicate content.

## Bug Fixes {#bug-fixes}

* **Properties Panel Breadcrumb**: The breadcrumb menu in the properties panel for deeply nested items, which didn’t remain open, was fixed.
* **Content Fragment Selector**: The Content Fragment selector was improved to ensure that it respects the rules defined in the Content Fragment model or in the `data-aue-filter`.
* **Component Insertion**: The list to insert new components that didn’t update accurately after navigating to another page was corrected.
* **Publication Status**: The handling of publication statuses was improved to function more consistently.
* **Miscellaneous Fixes**: This release also contains various minor fixes, tech debt cleanup, security enhancements, and consolidated tests for overall stability and performance.
