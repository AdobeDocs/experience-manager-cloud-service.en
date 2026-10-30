---
title: Reuse Content Fragments using MSM and Live Copies
description: Learn about using the Live Copy functionality of MSM to use the same, or similar, Content Fragment content in multiple locations, while synchronizing with the source content.
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
feature: Content Fragments
role: User
solution: Experience Manager Sites
exl-id: 5039cf92-21ff-4d6c-a684-72eab13b519d
product_v2:
  - id: c45915cf-e157-4af7-a80d-97b905bcb3a5
    internal-label: Experience Manager Sites
feature_v2:
  - id: a642c50e-80eb-4fc1-a5d2-f3762d1f841d
    internal-label: Administration
subfeature_v2:
  - id: e9db7c79-8f65-4281-a439-c9049296d903
    internal-label: Content Fragments
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
---
# Reuse Content Fragments using MSM {#reuse-content-fragments-using-msm}

Multi Site Manager (MSM), and the Live Copy functionality, enables you to use the same content in multiple locations, while synchronizing with the source content.

>[!NOTE]
>
>MSM for Content Fragments is also available when using Content Fragments via the [**Assets** console](/help/assets/content-fragments/content-fragments-msm.md).

* With MSM Live Copies you can:
  * Create content once 
  * Reuse this content in other areas of the same site, in other sites, or in applications.
* MSM then maintains the live relationships between your source content and its Live Copies so that:
  * When you change the source content, the source and Live Copies are synchronized.
  * You can make adjustments to only the content of the Live Copies by disconnecting the live relationship for individual sub fragments and/or components.

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

You can create a Live Copy for either a single Content Fragment or an entire folder of fragments.

>[!CAUTION]
>
>If you want to use MSM to create copies of Content Fragments), then any **Unique** constraints should be removed from any Data Types used in the respective [Content Fragment Models](/help/assets/content-fragments/content-fragments-models.md).

### Create a Live Copy - folder {#create-a-live-copy-folder}

To create a Live Copy of your Content Fragment folder:

1. In the Content Fragment console open the folders panel and navigate to show your folder.
1. Mouse over your folder entry to show the ellipses (three dots). Select to open the folder actions menu.
1. From **MSM Actions** select **Create live copy**.
1. In the dialog that opens specify the destination and continue with **Next**.
1. Specify the properties. You can specify the title, name and whether the Live Copy should exclude children (nested fragments).
1. Continue with **Next**.
1. Select whether you want the Live Copy created immediately (**Now**), or at a **Later** date and time.
1. Confirm with **Create Live Copy**.

### Create a Live Copy - single fragment {#create-a-live-copy-single-fragment}

To create a Live Copy of your Content Fragment:

1. In the Content Fragment console navigate to the location of your fragment.
1. Select your fragment.
1. Select **Create Live Copy** from the top toolbar.
1. In the dialog that opens specify the destination and continue with **Next**.
1. Specify the properties. You can specify the title, name and whether the Live Copy should exclude children (nested content).
1. Continue with **Next**.
1. Select whether you want the Live Copy created immediately (**Now**), or at a **Later** date and time.
1. Confirm with **Create Live Copy**.

## View properties and status {#view-properties-and-status}

In the main panel of the console:

* the **Live Copy** column indicates whether a fragment is a **Source** or a **Live Copy**; or not currently involved in MSM at all
* you can also select the Information (i) icon of your fragment to open the right information panel, from where you can select the **Live Copy Details** tab.

![Live Copy information from the Content Fragments console](/help/sites-cloud/administering/content-fragments/assets/cf-msm-information.png)

>[!NOTE]
>
>A **Live Copy** tab is also available in the right panel of the new Content Fragment editor.

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

## Take Action {#take-action}

There are multiple actions involved in using live copies for Content Fragments. The actions are context sensitive so you will only see the ones appropriate for your current scenario; exact details may vary dependent on the location within the console and whether the action is for a single fragment or an entire folder.

* **Create live copy**
* **Synchronize**
* **Roll out**
* **Suspend**
* **Suspend Live Copy**
* **Detach**
* **Detach from Source**
* **Reset**
* **Reset Live Copy**

>[!NOTE]
>
>Various actions can also be triggered from the new Content Fragment editor.

>[!NOTE]
>
>Various actions can also be triggered from the new Content Fragment editor:
>
>* [Cancel, and revert to, inheritance](/help/sites-cloud/administering/content-fragments/authoring.md#cancel-and-revert-to-inheritance)
>* [Live Copy details and actions](/help/sites-cloud/administering/content-fragments/authoring.md#live-copy-details-and-actions)

There are multiple locations from where you can trigger actions related to your fragments and live copies: 

* the top toolbar for a single Content Fragment

  1. In the Content Fragment console navigate to the location of your fragment source.
  1. Select your fragment.
  1. Select the required action from the toolbar.

     ![Content Fragment Console - top toolbar actions MSM](/help/sites-cloud/administering/content-fragments/assets/cf-msm-top-toolbar.png)

  1. Continue with any further steps.

* the **Live Copy Details** tab for a single Content Fragment 

  1. In the Content Fragment console navigate to the location of your fragment source.
  1. Select your fragment.
  1. Use the Information icon (i) to open the information panel.
  1. Open the **Live Copy Details** tab.
  1. Select the ellipses for either:

     * a Source

       1. Select the ellipses next to the Source.
       1. Select the action from the drop down menu.

          ![Live Copy Details - source menu](/help/sites-cloud/administering/content-fragments/assets/cf-msm-live-copy-tab-source-menu.png)

     * a Live Copy

       1. Select the ellipses next to your Live Copy.
       1. Select the required action from the drop down menu.

          ![Live Copy Details - live copy menu](/help/sites-cloud/administering/content-fragments/assets/cf-msm-live-copy-tab-lc-menu.png)

     * Continue with any further steps.

* the folder actions menu for an entire folder

  1. In the Content Fragment console navigate to your folder.
  1. Use the ellipses to open the menu for folder actions.
  1. From **MSM Actions** select the required action.

     ![Content Fragment Console - folder actions MSM](/help/sites-cloud/administering/content-fragments/assets/cf-msm-folder-actions-msm.png)

  1. Continue with any further steps.

## Propagate your modifications {#propagate-your-modifications}

To propagate modifications between the source and your Live Copy you can:

* [Synchronize](#synchronize): to pull the content updates from your Live Copy to the source
* [Rollout](#rollout): to push the source updates to your Live Copy

### Synchronize {#synchronize}

There are [multiple locations](#how-to) from where you can trigger a Synchronization that pulls the content updates from your Live Copy to the source.

In all locations:

1. Select **Synchronize** from the toolbar or menu.
1. Confirm **Synchronize** in the dialog.

### Rollout {#rollout}

There are [multiple locations](#how-to) from where you can trigger a Rollout that pushes the source updates to your Live Copy.

In all locations:

1. Select **Rollout** from the toolbar or menu. The wizard will open to guide you through the process.
1. Select the Live Copies to include in the rollout and **Continue**.
1. Schedule the rollout for immediately (**Now**) or **Later**.
1. **Continue** as appropriate.

## Suspend, Resume, Detach, Reset {#suspend-resume-detach-reset}

You can manage your Live Copy with:

* Suspend the Live Copy

  Each fragment in a Live Copy is associated with its source via a live relationship. The live relationship configures the synchronization of Live Copy content from the source.

  You can Suspend the Live Copy inheritance for a Live Copy so that you can change page properties and components. When you suspend inheritance, the fragment properties and content are no longer synchronized with the source.

* Resume the Live Copy

  After a live copy has been suspended it can be resumed.

* Detach from Source

  The detach action permanently removes the live relationship between a Live Copy and its Source. All MSM-relevant properties are removed from the Live Copy and the Live Copy fragments become standalone.

* Reset Live Copy

  Reset a Live Copy to remove all inheritance cancellations and return the fragment to the same state as the source.

  Reset affects any changes that you have made to fragment properties and content.

Again there are [multiple locations](#how-to) from where you can trigger a Rollout that pushes the source updates to your Live Copy.

## Cancel, and revert to, inheritance in the editor {#cancel-and-revert-to-inheritance-in-the-editor}

Inheritance is the mechanism where content can be automatically pushed from one fragment to another. Inherited fields, and variations, can be the product of Multi-Site Management.

You can cancel (then revert to) the inheritance in the Content Fragment editor. Depending on the context, this can be available for a variation, or an individual field, if the fragment is part of a live copy.

For example:

* Cancel inheritance

  ![Cancel inheritance icon](/help/sites-cloud/administering/content-fragments/assets/cf-authoring-cancel-inheritance.png)

* Revert to inheritance (if inheritance is already canceled)

  ![Revert to inheritance icon](/help/sites-cloud/administering/content-fragments/assets/cf-authoring-revert-to-inheritance.png)

>[!CAUTION] 
>
> For Composite fields inheritance can only be broken for top-level fields. 
>
>* Inheritance for an entire composite field can be broken.
>* Breaking inheritance for individual fields within composite items is not supported.

>[!NOTE]
>
>For more details see [Cancel, and revert to, inheritance in the editor](/help/sites-cloud/administering/content-fragments/authoring.md#cancel-and-revert-to-inheritance).

## Compare MSM for Content Fragments and Sites Pages {#compare-msm-for-content-fragments-and-sites-pages}

In most scenarios, MSM for Content Fragments matches the behavior of MSM for Sites Pages functionality. Some key differences to note are:

* Blueprint in MSM for Sites Pages is called Live Copy source in MSM for Content Fragments.
* For Sites Pages, you can compare a blueprint and its live copy but it is not possible for Content Fragments to compare a source to its live copy.
* You cannot edit a live copy in the Content Fragments console.
* Sites Pages usually have children, but Content Fragment do not, though they may have referenced fragments. The option to include or exclude children refers to these referenced fragments.
* Removing the chapters step in the create site wizard is not supported in MSM for Content Fragments.
* Configuring MSM locks on page properties is not supported in MSM for Content Fragments.
* For MSM for Content Fragments, use only the **Standard rollout config**. Other rollout configurations are not available for MSM for Content Fragments.

>[!NOTE]
>
>It should be remembered that MSM for Content Fragments accessed through the Content Fragments console is based on the Assets functionality; this is because they are stored as Assets (though considered a Sites feature). 

## Limitations {#limitations}

* On-modify triggers, and the associated rollout configuration, do not exist for Content Fragments.
* Composite fields
  * Inheritance can only be broken for top-level fields. 
    * Inheritance for an entire composite field can be broken.
    * Breaking inheritance for individual fields within composite items is not supported.
