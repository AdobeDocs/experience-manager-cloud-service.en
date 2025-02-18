---
title: Universal Editor 2025.02.17 Release Notes
description: These are the release notes for the 2025.02.17 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2025.02.17 Release Notes {#release-notes}

These are the release notes for the 17 February 2025 release of the Universal Editor.

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page](/help/release-notes/release-notes-cloud/release-notes-current.md).

## What's New {#what-is-new}

* **Publish to preview** - When publishing (or unpublishing) your content using the Universal Editor, you can now choose if you wish to publish to your preview environment in addition to your publish environment
  * This allows review of your content before public publication.
* **Model and filter can be defined in the component definition** - You can now define what model and filter a component uses in the component definition.
  * This information can be maintained centrally in the definition and doesn't need to be specified the instrumentation.
  * This allows you to move components across containers.
* **Child elements of containers are implicitly considered components** - If an item with a `data-aue-resource` is placed as direct child into a container it is considered a component and can be moved without having to specify `data-aue-behavior="component"`.

## Other Improvements {#other-improvements}

* **AEM 6.5 Asset Selector** - The 6.5 asset selector now opens properly when running the Universal Editor with AEM 6.5.

