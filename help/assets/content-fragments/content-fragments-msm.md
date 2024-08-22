---
title: Reuse Content Fragments using MSM and Live Copies
description: Learn about using the Live Copy functionality of MSM to use the same, or similar, Content Fragment content in multiple locations, while synchronizing with the source content.
exl-id: f050b2d1-856c-4cdb-ac74-bc78016f144a
feature: Content Fragments
role: User
solution: Experience Manager Sites
---
# Reuse Content Fragments using MSM {#reuse-content-fragments-using-msm}

Multi Site Manager (MSM), and the Live Copy functionality, enables you to use the same content in multiple locations, while synchronizing with the source content.

* With MSM Live Copies you can:
  * Create content once and then
  * Reuse this content in other areas of the same or other sites, or applications.
* MSM then maintains the live relationships between your source content and its Live Copies so that:
  * When you change the source content, the source and Live Copies are synchronized.
  * You can make adjustments only to the content of the Live Copies by disconnecting the live relationship for individual sub pages and/or components.

For a detailed overview of MSM concepts see [Reusing Content: Multi Site Manager and Live Copy](/help/sites-cloud/administering/msm/overview.md).

>[!NOTE]
>
>[Multi Site Manager (MSM)](/help/sites-cloud/administering/msm/overview.md) functionality in Adobe Experience Manager enables users to reuse content that is authored once and then reused across multiple web-locations. 

Using MSM for Content Fragments you can:

* Create Content Fragments once and then make (linked) copies of these fragments to reuse in other areas of the site or application.
* Keep multiple copies synchronized by updating the source copy once, then pushing the changes to the (live) copies.
* Make local changes by temporarily, or permanently, suspending the link between parent and child fragments; either completely, or for their variations or fields.

MSM for Content Fragments, combined with functionality within the Content Fragment Editor, allows you to break, and reinstate inheritance at the field level.

>[!CAUTION]
>
>MSM for Content Fragments is only available when using Content Fragments via the **Assets** console. 
>
>MSM functionality is *not* available when using the **Content Fragments** console.

## How To {#how-to}

See the following documentation for details about the usage of MSM for Content Fragments (also applicable to Assets):

* How to use [MSM for Content Fragments (and Assets)](/help/assets/reuse-assets-using-msm.md) 

* [Create a Live Copy](/help/assets/reuse-assets-using-msm.md)

  >[!CAUTION]
  >
  >If you want to use MSM to create copies of Content Fragments), then any **Unique** constraints should be removed from any Data Types used in the respective [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md).

* [View properties and status of source and Live Copy](/help/assets/reuse-assets-using-msm.md#properties)
* [Propagate modifications from source to Live Copy](/help/assets/reuse-assets-using-msm.md#rollout-sync)
* Cancel, and reinstate, inheritance for:
  * fields and variations in the [Content Fragment editor](/help/assets/content-fragments/content-fragments-variations.md#inheritance)
  * [metadata of related assets](/help/assets/content-fragments/content-fragments-variations.md#canceling-reenabling-inheritance-individual-items)
* [Suspend and resume the relationship](/help/assets/reuse-assets-using-msm.md#suspend-resume)
* [Remove the live relationship](/help/assets/reuse-assets-using-msm.md#detach)
* [Compare MSM for Content Fragments (and Assets) with MSM for Sites](/help/assets/reuse-assets-using-msm.md#comparison)

## Limitations {#limitations}

* On-modify triggers, and the associated rollout configuration, do not exist for Content Fragments.
