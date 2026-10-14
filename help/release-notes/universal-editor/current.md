---
title: Universal Editor 2026.10.15 Release Notes
description: These are the release notes for the 2026.10.15 release of the Universal Editor.
feature: Release Information
role: Admin
---

# Universal Editor 2026.10.08 Release Notes {#release-notes}

These are the release notes for the 15 October 2026 release of the Universal Editor.

>[!TIP]
>
>If you wish to test **upcoming** Universal Editor features before they are released, please see the [Universal Editor Preview Release Notes.](/help/release-notes/universal-editor/preview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## New Features {#what-is-new}

* AI agents can now see the editor's loaded content and update nested component properties more precisely.
* AI agents can undo and redo editor changes through the new WebMCP tools.
* Structured service log events now include a UTC datetime, and forwarded events keep their original datetime.

## Other Improvements {#other-improvements}

* URLs inside Unified Shell no longer pick up repeated shell or embedded-URL prefixes.
* The shell's force-reload flag is no longer passed through to the page's search parameters.
* Drag and drop no longer allows moving components onto targets that are not containers.
* AI agents can now set images that are not activated yet by using their author DAM path, and they also tell users the asset must be activated to appear on the published page.
* Updated the headless canvas components to fix remote URL construction for non-Sense-7 instances and bring in Dynamic Media for delivery instances.
* Icons in extension-provided renderers now receive their props correctly.
