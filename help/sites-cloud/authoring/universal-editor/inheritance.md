---
title: Content Inheritance for MSM and Launches
description: Learn how the Universal Editor supports content inheritance for Multi Site Management and Launches.
solution: Experience Manager Sites
feature: Authoring
role: User
---

# Content Inheritance for MSM and Launches {#inheritance}

Learn how the Universal Editor supports content inheritance for Multi Site Management and Launches.

## Introduction {#introduction}

[Multi Site Management (MSM)](/help/sites-cloud/administering/msm/overview.md) and [Launches](/help/sites-cloud/authoring/launches/overview.md) are powerful tools to help you reuse your content. Pages can be copied from a central source (the blueprint) to enable authors to make changes specific to the context of those copies, while the rest of the content remains inherited from the blueprint. This is extremely useful when localizing sites.

To modify some content of the copies, authors break the inheritance on the affected components to ensure their local changes are not overwritten when the copies are synchronized from the blueprint. The Universal Editor supports inheritance breaking such that when content is modified, those changes are retained when updates are synchronized from the blueprint.

## Content Inheritance and the Universal Editor {#inheritance}

When a page is part of MSM or a Launch and content is edited with the Universal Editor, the editor automatically disables inheritance for all changes made by authors on that page, ensuring that modified content is retained when updates are synchronized from the blueprint.

The author does not needs to click a button or otherwise take any other steps to disable inheritance before making local edits. As soon as a change is made, inheritance is implicitly canceled. This is in contrast to the [Page Editor.](/help/sites-cloud/authoring/page-editor/edit-content.md#inherited-components)

## Limitations {#limitations}

* Authors can not revert inheritance for single components.
  * Inheritance can only be reverted for the entire page via the MSM admin or the Launch admin UIs.
* Authors do not have visual feedback to see which components have their inheritance disabled and which still have it preserved.
These features are currently limited to components in pages and do not yet apply to Content Fragments, despite those also having MSM and Launch capabilities.