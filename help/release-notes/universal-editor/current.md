---
title: Universal Editor 2025.07.09 Release Notes
description: These are the release notes for the 2025.07.09 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2025.07.09 Release Notes {#release-notes}

These are the release notes for the 9 July 2025 release of the Universal Editor.

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page](/help/release-notes/release-notes-cloud/release-notes-current.md).

## What's New {#what-is-new}

* [When clicking the **Add** toolbar button on containers,](/help/sites-cloud/authoring/universal-editor/authoring.md#adding-components) if only one component type is allowed, it is inserted immediately without requiring selection from the drop-down menu.
* [The authentication header toolbar option](/help/sites-cloud/authoring/universal-editor/navigation.md#autentication-settings) has been placed behind a feature toggle, as it is not useful in most cases.
* Since container nesting is not permitted for multi-fields in the properties panel, the rendering routine now filters out nested containers from the field list to prevent invalid nesting.

## Early Adoption Features {#early-adopter}

If you are interested in testing these upcoming features and sharing your feedback, please send an email to your Adobe Customer Success Manager from the email address associated with your Adobe ID. 

### New RTE {#new-rte}

The new ProseMirror RTE, featuring a page picker in the link dialog, is now available in the right panel.

### Undo/Redo {#undo-redo}

Undo and redo is now available to Universal Editor content authors.

* This includes edits done in context, edits done via the Properties panel, as well as adding (or duplicating), moving, and deleting blocks.
* Undo and redo is limited to the current browser session.

## Other Improvements {#other-improvements}

* An issue was fixed where single asset reference removal was not possible when editing via the property rail.
* An issue was fixed where the Properties panel would load indefinitely because asset references were automatically converted to arrays, causing an infinite loading state.
    * Asset reference values are now stored as-is, without automatic conversion to arrays.
* An issue was fixed where the Properties panel did not display fields when a model was defined but contained no content.
    * This caused an infinite loading state for the Properties panel for empty empty detail responses, like empty Content Fragments.
* The ESLint configuration has been refactored for compatibility with version 9, including updated rules and plugin support.

## Deprecations {#deprecations}

* The `text-input` component is now officially deprecated.
    * In `model-definition.json`, use the text component to create text inputs for the Properties panel.
