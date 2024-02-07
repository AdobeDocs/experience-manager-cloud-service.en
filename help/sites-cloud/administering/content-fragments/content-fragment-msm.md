---
title: Reuse Content Fragments using MSM
description: MSM enables you to use the same, or similar, Content Fragment content in multiple locations, while synchronizing with the source content.
---
# Reuse Content Fragments using MSM {#reuse-content-fragments-using-msm}

The Multi Site Manager (MSM) enables you to use the same content in multiple locations. MSM uses its Live Copy functionality to achieve this.

* With MSM you can:
  * Create content once and then
  * Reuse this content in other areas (via Live Copies) of the same or other sites.
* MSM then maintains the live relationships between your source content and its Live Copies so that:
  * When you change the source content, the source and Live Copies are synchronized.
  * You can make adjustments only to the content of the Live Copies by disconnecting the live relationship for individual sub pages and/or components.

>[!NOTE]
>
>[Multi Site Manager (MSM)](/help/sites-cloud/administering/msm/overview.md) functionality in Adobe Experience Manager enables users to reuse content that is authored once and then reused across multiple web-locations. 
>
>[MSM for Assets](/help/assets/reuse-assets-using-msm.md) provides comparable functionality for Assets. 
>
>As Content Fragments are a Sites feature, stored as Assets the functionality is also available for Content Fragments.

Using MSM for Content Fragments you can:

* Create Content Fragments once and then make (linked) copies of these fragments to reuse in other areas.
* Keep multiple copies synchronized by updating the source copy once, then pushing the changes to the (live) copies.
* Make local changes by temporarily, or permanently, suspending the link between parent and child fragments.

MSM for Content Fragments is primarily based on MSM for Assets. combined with functionality within the Content Fragment Editor allowing you to break, and reinstate inheritance at the field level.

>[!CAUTION]
>
>MSM for Content Fragments is only available when using Content Fragments via the **Assets** console. 
>
>MSM functionality is *not* available when using the **Content Fragments** console.

<!--updated first 3 links for MSM/Assets 
The following details: 

* [Creating and Synchronizing Live Copies](/help/sites-cloud/administering/msm/overview.md#creating-live-copies.md)
* [Live Copy Overview Console](/help/sites-cloud/administering/msm/overview.md#live-copy-overview.md)
* [Configuring Live Copy Synchronization](/help/sites-cloud/administering/msm/overview.md#live-copy-sync-config.md)
* [MSM Rollout Conflicts](/help/sites-cloud/administering/msm/overview.md#rollout-conflicts.md)
* [MSM Best Practices](/help/sites-cloud/administering/msm/overview.md#best-practices.md)
-->

