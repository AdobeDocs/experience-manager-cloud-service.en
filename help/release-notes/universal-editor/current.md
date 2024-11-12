---
title: Universal Editor 2024.11.12 Release Notes
description: These are the release notes for the 2024.11.12 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2024.11.12 Release Notes {#release-notes}

These are the release notes for the 12 November 2024 release of the Universal Editor.

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What’s New {#what-is-new}

* **Retry Option on CORS Timeout:** With [release 2024.09.26,](/help/release-notes/universal-editor/2024/2024-09-26.md) an error panel was introduced when the editor couldn’t establish a connection to the loaded page, preventing endless loading states. 
  * With this release, the editor automatically keeps retrying and once the connection is established, editing can be resumed.
  * This is especially useful for pages that may take longer than the one minute timeout to initialize.
* **Extensibility Enhancements for Developers:** The Universal Editor now supports  broadcasting events to extensions, allowing extension developers to subscribe to [events.](/help/implementing/universal-editor/events.md)
  * This enables developers to [react to editor events within their custom extensions.](/help/implementing/universal-editor/customizing.md#extending)
* **Persistent Component Selection:** Selected components in the editor will now persist even after refreshing the browser.
  * This ensures that users can continue working without losing their context when reloading the page.
* **Localized Quick Links:** The **Quick Links** section on the home screen now provides localized links to documentation, helping users easily access relevant guides based on their language preferences.
* **Request ID for Advanced Debugging:** Error notifications now include a **Request ID** in the details section, which correlates with the `x-request-id header`.
  * This makes it easier for Adobe engineering teams to trace and diagnose issues by matching those errors with internal logs.

## Other Improvements {#other-improvements}

* **Fixed Long Content Tree Labels:** Resolved an issue where long labels in the **Content Tree** panel were cut off
  * This ensures that drag-and-drop handles are always visible for content reordering.
* **Fixed Long Properties Labels:** Addressed a bug where long field labels in the **Properties** panel overlapped with field validation information
* **Horizontal Scrolling in Properties Panel:** Fixed an issue where wide elements in the **Properties** panel caused horizontal scrolling
* **Fixed Inactive Toolbar During Notifications:** The top **Adobe Experience Cloud** toolbar is now fully functional when [toast](https://spectrum.adobe.com/page/toast/) notifications are displayed.
* **Improved Stability:** Added error boundaries to handle unexpected values, preventing the entire UI from crashing when a single renderer or validator fails, improving robustness
