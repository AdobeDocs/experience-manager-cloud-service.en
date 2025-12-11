---
title: Universal Editor 2025.12.11 Release Notes
description: These are the release notes for the 2025.12.11 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2025.12.11 Release Notes {#release-notes}

These are the release notes for the 11 December 2025 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page](/help/release-notes/release-notes-cloud/release-notes-current.md).

## What's New {#what-is-new}

* Support has been added to existing tables in the [rich text editor.](/help/sites-cloud/authoring/universal-editor/authoring.md#formatting-options)
* The tab key has been enabled for nesting lists in the [rich text editor.](/help/sites-cloud/authoring/universal-editor/authoring.md#formatting-options)
* The developer login feature can now be disabled via the [meta tag `dev-login`.](/help/implementing/universal-editor/customizing.md#meta-tags)
* A right-click in the overlay section now displays a [contextual options menu.](/help/sites-cloud/authoring/universal-editor/authoring.md#context-options)
* Scoped indentation is now supported in the [rich text editor.](/help/sites-cloud/authoring/universal-editor/authoring.md#formatting-options)
* Shallow copy has been implemented for Content Fragments.

## Other Improvements {#other-improvements}

* The properties rail is now synchronized when multi fields change in-context.
* The Content Fragment picker now opens as expected on AEM 6.5 instances.
* The escape key now closes dialogs in the rich text editor.
* The **Remove component** action is now only available when a component is selected.
* The correct (old or new) Content Fragment editor is now opened based on the used instance (if the hostname is the AEM as a Cloud Service pattern then use the new editor, else use the legacy editor).
* Filter validation is added to the duplicate action.
* Long titles are now truncated in the properties rail.
* Multi-site manager arrays with more than 10 values are now properly handled.
* Conflict errors when creating multiple components with same name are now properly handled.
* Multi-site manager array handling with values >10 was added.
