---
title: Universal Editor Preview Release Notes
description: These are the release notes for the preview release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: e8d031aa-4676-4e45-977b-e5dffcc404c4
---

# Universal Editor Preview Release Notes {#preview}

These are the release notes for the **preview version** of the Universal Editor. These features are currently available in your Universal Editor's **preview environment**. These features are scheduled to be released to general availability on 8 October 2026.

These **preview** release notes are provided as a convenience so you know what changes to the Universal Editor are upcoming and you can test them by [switching to your preview version.](/help/sites-cloud/authoring/universal-editor/navigation.md#user-properties)

>[!TIP]
>
>For the **current release notes** for the Universal Editor, please see the document [Universal Editor Release Notes.](/help/release-notes/universal-editor/current.md)

>[!NOTE]
>
>The content of the actual release as well as the release date are subject to change.

## Upcoming Features {#upcoming-features}

* Authors can choose custom styles in the in-context rich text editor.
* Rich text asset selection now supports configured remote asset sources.
* Asset filters can be configured globally in `filter-definition.json`. 
* Extensions can customize the properties panel header through a new extension point.
* Number fields now support custom validation error messages.
* Text, combo box, and select fields now display configured placeholder text in their components.
* Select and multiselect menus share consistent sizing behavior that keeps their overlays within the editor area.

## Upcoming Changes {#upcoming-improvements}

* Copying content now targets the correct container when multiple containers share the same resource but use different properties.
* Rich text paragraphs no longer retain unwanted leading non-breaking spaces. 
* Rich text components were updated to include the paragraph-spacing correction and additional rich text fixes.
* The component picker sidebar and layout now fill the available height. 
* Overlay labels no longer wrap over small editable elements.
* Drag previews for multiple selections stay within the picker's bounds. 
* Asset reference validation now respects the field's configured filter.
* With  `FT_SITES-52747` enabled, page updates handle replacements between object and primitive values without the previous type-mismatch crash.
