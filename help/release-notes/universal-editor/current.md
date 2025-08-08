---
title: Universal Editor 2025.07.31 Release Notes
description: These are the release notes for the 2025.07.31 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2025.07.31 Release Notes {#release-notes}

These are the release notes for the 31 July 2025 release of the Universal Editor.

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page](/help/release-notes/release-notes-cloud/release-notes-current.md).

## What's New {#what-is-new}

* New features for [RTE early adopters](#new-rte)
  * Dark mode support was added.
  * Text alignment support was added.
    * Disabled by default and only available for headless projects
  * Indentation support was added.
    * Disabled by default and only available for headless projects
  * Breaks (`<br>`) are now inserted on shift+enter.

## Early Adoption Features {#early-adopter}

If you are interested in testing these upcoming features and sharing your feedback, please send an email to your Adobe Customer Success Manager from the email address associated with your Adobe ID. 

### New RTE {#new-rte}

The new ProseMirror RTE, featuring a page picker in the link dialog, is now available in the right panel.

### Undo/Redo {#undo-redo}

Undo and redo is now available to Universal Editor content authors.

* This includes edits done in context, edits done via the Properties panel, as well as adding (or duplicating), moving, and deleting blocks.
* Undo and redo is limited to the current browser session.

## Other Improvements {#other-improvements}

* Fixes for the early adopter RTE
  * Pressing enter now creates a new list item (`<li>`) when within a list.
* Videos now properly update when using remote DAM.
* Service support added for 6.5 LTS.

## Deprecations {#deprecations}

* The `text-input` component was officially deprecated with [release 2025.07.09.](/help/release-notes/universal-editor/2025/2025-07-09.md)
  * In `model-definition.json`, use the text component to create text inputs for the Properties panel.
