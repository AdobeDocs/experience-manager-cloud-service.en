---
title: MSM FAQ
description: Find answers to the most frequently asked questions around MSM and Live Copy.
---

# MSM FAQ {#msm-faq}

## Why are some properties (e.g. title, annotations) are not updated during an MSM rollout? {#missing-properties}

MSM sync actions are highly configurable. Which properties or components are modified during rollouts directly depends on properties of those configurations.

Please see [this article](best-practices.md) for more information on this topic.

## How can I remove rollout permissions for a group of authors? {#remove-rollout-permissions}

There is no **rollout** privilege that can be set or removed for AEM principals (users or groups).

As an alternative you can either:

* Customization the product UI to hide the Rollout actions for a given principal.
* Remove write privileges from the Live Copy tree for authors who are not allowed to roll-out.

## Why do I see Live Copy pages with the suffix "_msm_moved"? {#moved-pages}

If a blueprint page is rolled out, it will either update its Live Copy page or create a new Live Copy page if it didn't exist yet (e.g. when it is rolled out for the first time or the Live Copy page was manually deleted).

In this latter case however, if a page without a `cq:LiveRelationship` property exists with the same name, this page will be renamed accordingly, before the Live Copy page is created.

By default, the rollout expects either a linked Live Copy page, to which the updates of the blueprints will be rolled out, or no page at, when a Live Copy page is created.

If a "standalone" page is found, MSM chooses to rename this page, and create a separate, linked Live Copy page.

Such a standalone page in a Live Copy sub-tree is typically the result of a **Detach** operation, or the former Live Copy page was manually deleted by an author and then re-created with the same name.

To avoid this use the Live Copy **Suspend** feature instead of **Detach**. More details on the **Detach** action in [this article.](creating-live-copies.md)
