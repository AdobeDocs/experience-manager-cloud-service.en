---
title: Content Inheritance in the Universal Editor
description: Learn how the Universal Editor supports content inheritance for Multi Site Management and Launches to support content reuse and localization.
solution: Experience Manager Sites
feature: Authoring
role: User
---

# Content Inheritance in the Universal Editor {#inheritance}

Learn how the Universal Editor supports content inheritance for Multi Site Management and Launches to support content reuse and localization.

## Use Case {#use-case}

For many users of AEM, creating a page is just the beginning. To scale content effectively, the following steps are typically involved after page creation:

1. **Translate the page** by using language copies and translation workflows.
1. **Localize the page** by using Multi Site Management to roll out the translated page to different markets.
1. **Create new versions** by using Launches to prepare future iterations of the page and taking those changes live.

These steps can accelerate content velocity and ensure content consistency. The Universal Editor supports content inheritance, which is the mechanism these steps rely on.

## Inheritance {#what-is-inheritance}

Inheritance is the mechanism where content can be linked such that changing one automatically changes the other. Inherited components can be the product of various scenarios, including:

* [Multi Site Management (MSM)](/help/sites-cloud/administering/msm/overview.md)
* [Launches](/help/sites-cloud/authoring/launches/overview.md) 

MSM and Launches are powerful tools to help you reuse your content. Pages can be copied from a central source (the blueprint) to enable authors to make changes specific to the context of those copies, while the rest of the content remains inherited from the blueprint. This is extremely useful when localizing sites.

To modify some content of the copies, authors break the inheritance on the affected components to ensure their local changes are not overwritten when the copies are synchronized from the blueprint.

## Content Inheritance and the Universal Editor {#universal-editor}

When a page is part of MSM or a Launch and content is edited with the Universal Editor, the editor automatically disables inheritance for all changes made by authors on that page, ensuring that modified content is retained when updates are synchronized from the blueprint.

The author does not need to click a button or otherwise take any other steps to disable inheritance before making local edits. As soon as a change is made, inheritance is implicitly canceled. This is in contrast to the [Page Editor.](/help/sites-cloud/authoring/page-editor/edit-content.md#inherited-components)

## Limitations {#limitations}

* Authors can not revert inheritance for single components.
  * Inheritance can only be reverted for the entire page via the [Live Copy Overview Console](/help/sites-cloud/administering/msm/live-copy-overview.md) or the [Launches Console.](/help/sites-cloud/authoring/launches/overview.md#the-launches-console)
* Authors do not have visual feedback to see which components have their inheritance disabled and which still have it preserved.
* These features are currently limited to components in pages and do not yet apply to [Content Fragments,](/help/sites-cloud/administering/content-fragments/overview.md) despite those also having MSM and Launch capabilities.
