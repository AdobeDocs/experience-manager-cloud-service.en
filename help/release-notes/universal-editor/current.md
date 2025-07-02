---
title: Universal Editor 2025.06.19 Release Notes
description: These are the release notes for the 2025.06.19 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2025.06.19 Release Notes {#release-notes}

These are the release notes for the 19 June 2025 release of the Universal Editor.

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page](/help/release-notes/release-notes-cloud/release-notes-current.md).

## What's New {#what-is-new}

* **Support for multi-fields in the Properties Rail** - 
[The container component](/help/implementing/universal-editor/field-types.md#container) can now be used to create multi-field properties.
* **Support for nested properties** - The [`name` field](/help/implementing/universal-editor/field-types.md#nesting) now supports paths to enable property nesting.
* **Resizable right panel** - The side panel can now be resized to better account for longer content displayed in the side panel.

## Early Adoption Features {#early-adopter}

For a chance to test some upcoming features, be a part of Adobe's early adopter program.

### **Undo/Redo** {#undo-redo}

Undo and redo is now available to Universal Editor content authors.

* This includes edits done in context, edits done via the Properties panel, as well as adding (or duplicating), moving, and deleting blocks.
* Undo and redo is limited to the current browser session.

If you are interested in testing this new feature and sharing your feedback, please send an email to your Adobe Customer Success Manager from the email address associated with your Adobe ID. 

## Other Improvements {#other-improvements}

* Resource key collision errors when moving blocks between containers were fixed.
* An issue was fixed that made duplicating the last block of a container fail.
* The Add action drop-down now only lists components that have a suitable plugin defined in the `component-definition.json` file.
* The modification date used by the publish dialog was fixed where in some circumstances pages weren't recognized as modified and weren't republished.
* Fixed MSM inheritance behavior where editing a container cancelled inheritance for child nodes.
* `fetchUrl` was fixed, restoring moving blocks from one container to another.
