---
title: Reuse Content Fragments using MSM and Live Copies
description: Learn about using the Live Copy functionality of MSM to use the same, or similar, Content Fragment content in multiple locations, while synchronizing with the source content.
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
feature: Content Fragments
role: User
solution: Experience Manager Sites
hide: yes
hidefromtoc: yes
index: no
---
# Reuse Content Fragments using MSM {#reuse-content-fragments-using-msm}

Multi Site Manager (MSM), and the Live Copy functionality, enables you to use the same content in multiple locations, while synchronizing with the source content.

<!-- CQDOC-23473 - feature is currently beta so page is hidden, see metadata -->
<!-- CQDOC-23473 - screenshots -->
<!-- CQDOC-23473 - only mentioned once in ToC, add entries -->

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

>[!NOTE]
>
>This page covers MSM functionality when using the **Content Fragments** console.
>
>MSM for Content Fragments is also available when using [Content Fragments via the **Assets** console](/help/assets/content-fragments/content-fragments-msm.md). 

## Create a Live Copy {#create-a-live-copy}

To create a Live Copy of your Content Fragment:

1. In the Content Fragment console navigate to the location of your fragment.
1. Select your fragment.
1. Select **Create Live Copy** from the top toolbar.
1. In the dialog that opens specify the destination and continue with **Next**.
1. Specify the properties. You can specify the title, name and whether the Live Copy should exclude children (nested fragments).
1. Continue with **Next**.
1. Select whether you want the Live Copy created immediately (**Now**), or at a **Later** date and time.
1. Confirm with **Create Live Copy**.

  >[!CAUTION]
  >
  >If you want to use MSM to create copies of Content Fragments), then any **Unique** constraints should be removed from any Data Types used in the respective [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md).

## View properties and status {#view-properties-and-status}

To view properties and the status of the source and your Live Copy:

1. In the Content Fragment console navigate to the location of your fragment.
1. Select your fragment.
1. Select the Information (i) icon in the **Title** column of your fragment. 
   The right information panel will open. 
1. Select the tab for **Live Copy Details**.

## Propagate modifications {#propagate-modifications}

To propagate modifications from the source to your Live Copy.

### Synchronize {#synchronize}

To synchronize your content updates from the source to your Live Copy: 

1. In the Content Fragment console navigate to the location of your fragment source.
1. Select your fragment.
1. Select **Synchronize** from the toolbar.
1. Confirm **Synchronize** in the dialog.

### Rollout {#rollout}

To trigger a roll out, which synchronizes the source updates with your Live Copy:

1. In the Content Fragment console navigate to the location of your fragment Live Copy.
1. Select your fragment.
1. Select **Rollout** from the toolbar. The wizard will open to guide you through the process.
1. Select the Live Copies to include in the rollout and **Continue**.
1. Schedule the rollout for immediately (**Now**) or **Later**.
1. **Continue** as appropriate.

## Cancel, and reinstate, inheritance {#cancel-and-reinstate-inheritance}

Inheritance is the mechanism where content can be automatically pushed from one fragment to another. Inherited fields, and variations, can be the product of Multi-Site Management.

You can cancel (then re-enable) the inheritance. Depending on the context, this can be available for a variation, or an individual field, if the fragment is part of a live copy.

For example:

* Cancel Inheritance

  ![Cancel Inheritance button](/help/sites-cloud/administering/content-fragments/assets/cf-authoring-cancel-inheritance.png)

* Re-enable Inheritance (if inheritance is already canceled)

  ![Re-Enable Inheritance button](/help/sites-cloud/administering/content-fragments/assets/cf-authoring-reenable-inheritance.png)

## Compare MSM for Content Fragments and Sites Pages {#compare-msm-for-content-fragments-and-sites-pages}

<!-- CQDOC-23473 - needs a detailed review -->

In more scenarios, MSM for Content Fragments matches the behavior of MSM for Sites Pages functionality. Some key differences to note are:

* Blueprint in MSM for Sites Pages is called Live Copy source in MSM for Content Fragments.
* For Sites Pages, you can compare a blueprint and its live copy but it is not possible for Content Fragments to compare a source to its live copy.
* You cannot edit a live copy in the Content Fragments console.
* Sites pages usually have children, but Content Fragment do not, though they may have referenced fragments. The option to include or exclude children refers to these referenced fragments.
* Removing the chapters step in the create site wizard is not supported in MSM for Content Fragments.
* Configuring MSM locks on page properties is not supported in MSM for Content Fragments.
* For MSM for Content Fragments, use only the **Standard rollout config**. Other rollout configurations are not available for MSM for Content Fragments.

>[!NOTE]
>
>Remember that MSM for Content Fragments accessed through the Content Fragments console is based on the Assets functionality; this is because they are stored as Assets (though considered a Sites feature). 

## Limitations {#limitations}

* On-modify triggers, and the associated rollout configuration, do not exist for Content Fragments.
