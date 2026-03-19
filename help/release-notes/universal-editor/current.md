---
title: Universal Editor 2026.03.19 Release Notes
description: These are the release notes for the 2026.03.19 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2026.03.19 Release Notes {#release-notes}

These are the release notes for the 19 March 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page](/help/release-notes/release-notes-cloud/release-notes-current.md).

## What's New {#what-is-new}

* The items in the properties are now collapsed when navigating back to [the home screen.](/help/sites-cloud/authoring/universal-editor/navigation.md#home-button)
* [The assets selector](/help/implementing/universal-editor/configure-assets-selector.md) now supports [filter definitions.](/help/implementing/universal-editor/filtering.md)
* If there are no actions available for the selected item, [the context menu](/help/sites-cloud/authoring/universal-editor/authoring.md#context-menu) no longer shows a chevron to access actions.

## Early Adoption Features {#early-adopter}

If you are interested in testing the upcoming features listed below and sharing your feedback, please send an email to your Adobe Customer Success Manager from the email address associated with your Adobe ID. 

* Shallow copy has been implemented for Content Fragments.

## Other Improvements {#other-improvements}

* If there is a model/filter/component definition, it will get refetched when switching from one app to another in the editor.
* Removing an image no longer leaves empty image tags when using DA as a back end.
* Classes in blocks are now properly handled when using DA as a back end.
* Open API now saves remote assets properly as objects.

## Breaking Change {#breaking-change}

* All extensions should updated to `@adobe/uix-guest` >= `1.1.7` to improve stability.
