---
title: Universal Editor Preview Release Notes
description: These are the release notes for the preview release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: e8d031aa-4676-4e45-977b-e5dffcc404c4
---

# Universal Editor Preview Release Notes {#preview}

These are the release notes for the **preview version** of the Universal Editor. These features are currently available in your Universal Editor's **preview environment**. These features are scheduled to be released to general availability on 25 June 2026.

These **preview** release notes are provided as a convenience so you know what changes to the Universal Editor are upcoming and you can test them by [switching to your preview version.](/help/sites-cloud/authoring/universal-editor/navigation.md#user-properties)

>[!TIP]
>
>For the **current release notes** for the Universal Editor, please see the document [Universal Editor Release Notes.](/help/release-notes/universal-editor/current.md)

>[!NOTE]
>
>The content of the actual release as well as the release date are subject to change.

## Upcoming Features {#upcoming-features}

* A new button has been added to the toolbar to access AEM Sites console.
  * This brings the functionality of the former **AEM Site Admin Extension** [extension](/help/implementing/universal-editor/extending.md) natively to the Universal Editor.
  * The button opens the current AEM page in the [Sites console,](/help/sites-cloud/authoring/universal-editor/authoring.md#sites-console) or the [Experience Fragments console](/help/sites-cloud/authoring/fragments/experience-fragments.md) for `/content/experience-fragments` paths.
  * The button is hidden for DAM paths (`/content/dam`) and when no unique AEM page can be determined from the current editables.
* Single-character shortcuts now work better with accessibility technologies.

## Upcoming Changes {#upcoming-improvements}

* Numerous buttons now correctly have accessible names.
* A problem with persisting certain Content Fragments after selecting them with a picker has been fixed.
