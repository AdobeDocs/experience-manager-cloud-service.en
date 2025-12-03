---
title: Universal Editor Preview Release Notes
description: These are the release notes for the preview release of the Universal Editor.
feature: Release Information
role: Admin
---

# Universal Editor Preview Release Notes {#preview}

These are the release notes for the **preview version** of the Universal Editor. These features are currently available in your Universal Editor's **preview environment**. These features are scheduled to be released to general availability on 11 December 2025.

These **preview** release notes are provided as a convenience so you know what changes to the Universal Editor are upcoming and you can test them by [switching to your preview environment.](/help/sites-cloud/authoring/universal-editor/navigation.md#user-properties)

>[!TIP]
>
>For the **current release notes** for the Universal Editor, please see the document [Universal Editor Release Notes.](/help/release-notes/universal-editor/current.md)

>[!NOTE]
>
>The content of the actual release as well as the release date are subject to change.

## Upcoming New Features {#what-is-new}

* Support is added to existing tables in the new rich text editor.
* Tab key is enabled for nesting lists in the new rich text editor.
* The developer login feature can be disabled via the meta tag `dev-login`.
* A right-click in the overlay section now displays a contextual menu.
* Scoped indentation is now supported in the new rich text editor
* Shallow copy has been implemented for Content Fragments.

## Upcoming Improvements {#other-improvements}

* The properties rail is now synchronized when multi fields change in-context.
* The content fragment picker now opens as expected on AEM 6.5 instances.
* The escape key now closes dialogs in the new rich text editor.
* The **Remove component** action is now only available when a component is selected.
* The correct (old or new) Content Fragment editor is now opened based on the used instance (if the hostname is the AEM as a Cloud Service pattern then use the new editor, else use the legacy editor).
* Filter validation is added to the duplicate action.
* Long titles are now truncated in the properties rail.
* Multi-site manager arrays with more than 10 values are now properly handled.
* Conflict errors when creating multiple components with same name are now properly handled.
* Multi-site manager array handling with values >10 was added.
