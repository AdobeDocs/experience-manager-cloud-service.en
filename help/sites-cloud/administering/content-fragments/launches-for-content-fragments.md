---
title: Launches for Content Fragments
description: Learn how to use Launches for Content Fragments in Adobe Experience Manager as a Cloud Service. Launches enable you to efficiently develop content for a future release, while maintaining your current Content Fragments.
feature: Content Fragments
role: User, Developer
solution: Experience Manager Sites
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
exl-id: c0b9e571-3be5-42ab-8d56-d93e8ef4c2f7
---
# Launches for Content Fragments {#launches-for-content-fragments}

In Adobe Experience Manager (AEM) as a Cloud Service, Launches enable you to efficiently develop content for a future release.

A *Launch* is created to allow you to make changes in preparation for future publication, at the same time as maintaining your current content. For Content Fragments this means that you are effectively editing two versions at the same time: content that is currently published, and a version of that content, to be published at a time in the future. Once that time arrives you can replace the content of the original Content Fragments and publish the new versions. 

>[!NOTE]
>
>Launches are also available for Pages. The basic concepts are the same, but there are differences in how to manage them in AEM. 
>
>For full details see [Launches for Pages](/help/sites-cloud/authoring/launches/overview.md).

You create a *Launch*, then edit and update your Content Fragments in your *Launch*. If changes are made to the *Source* fragments during this phase, you can copy them to the *Launch* with the *Rebase* operation. When ready, *Promote* duplicates the launch content back to the source. You can then activate your source fragments, either manually or automatically (dependent on fields set when creating and editing the launch). You can also specify whether referenced fragments are to be included in this process.

For example, the seasonal product fragments of your online store are updated quarterly so that the featured products align with the current season. To prepare for the next quarterly update, you can create a launch of the appropriate fragments. Throughout the quarter, the following changes are accumulated in the launch copy:

* Edits that are performed directly on the launch fragments in preparation for the next quarter.
* Changes to the source Content Fragments that you transfer to the launch pages with *Rebase*.
* You can also navigate content in the launch branch; adding, or removing, fragments as necessary.

When the next quarter arrives, you promote the launch pages, so that you can publish the source pages (holding the updated content). You can promote either all fragments, or only those that you have modified.

![Launches overview - Rebase and Promote](/help/sites-cloud/administering/content-fragments/assets/cf-launches-overview.png)

This section describes how to create, edit, manage, rebase, promote, and if necessary delete, launches from within the [Content Fragments console](/help/sites-cloud/administering/content-fragments/managing.md):

* [Access and view Launches in the Content Fragment console](#launches-in-the-content-fragment-console)
* [Create a Launch](#create-a-launch)
* [Edit Launch content](#edit-launch-content)
* [Manage content within a Launch](#manage-content-within-a-launch)
* [Compare Launch to Source](#compare-launch-to-source)
* [Rebase a Launch from Source](#rebase-a-launch-from-source)
* [Promote a Launch to Source](#promote-a-launch-to-source)
* [Delete a Launch](#delete-a-launch)

## Launches in the Content Fragment Console {#launches-in-the-content-fragment-console}

The **Launches** tab of the Content Fragments console allows you to create launches, list all existing launches, see key properties, and take actions on them.

When no launch is selected you can [create a new launch](#create-a-launch).

![Launches tab in console](/help/sites-cloud/administering/content-fragments/assets/cf-launches-tab.png)

Select your launch to show:

* the toolbar, with the available actions
* the right panel, showing properties and further actions

![Launch actions toolbar in console](/help/sites-cloud/administering/content-fragments/assets/cf-launches-actions.png)

The toolbar allows you to:

* **[Open Launch](#edit-launch-content)**
* **[Edit Sources](#manage-content-within-a-launch)**
* **[Compare Launch to Source](#compare-launch-to-source)**
* **[Promote](#promote-a-launch-to-source)**
* **[Rebase](#promote-a-launch-to-source)**
* **[Delete Launch](#delete-a-launch)**

While the right panel enables you to:

* Edit the Launch **Title**
* Edit the Launch **Description**
* Update configuration details that were set when you [created the launch](#create-a-launch):

  * **Include references**: Create the Launch either with, or without, including any referenced Content Fragments. By default, referenced fragments are included.

    * Referenced fragments are also impacted when you [add, or remove fragments from the launch](#manage-content-within-a-launch) at a later stage.

    >[!NOTE]
    >
    >See [Details concerning Included References](#details-concerning-included-references)

  * **Publish Ready**; Enabling this toggle will automatically publish the fragments when the launch is promoted to the source.

* And also define:

  * A **Promote Date** and Time: if the [launch is to be automatically promoted](#promote-automatically)

## Create a Launch {#create-a-launch}

To create your launch:

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select **Create Launch**.

1. Navigate to the appropriate folder and select the fragments to be included in the launch:

   ![Select content fragments for new launch](/help/sites-cloud/administering/content-fragments/assets/cf-launches-create-select-cfs.png)

1. Select **Next**.

1. Specify details to configure the launch:

   * **Title**
   * **Description**
   * **Include References**: Create the Launch either with, or without, including any referenced Content Fragments. By default, referenced fragments are included.

     >[!NOTE]
     >
     >See [Details concerning Included References](#details-concerning-included-references)

   * **Publish Ready**: Enabling this toggle will automatically publish the fragments when the launch is promoted to the source.

   ![Details for new launch](/help/sites-cloud/administering/content-fragments/assets/cf-launches-create-launch-details.png)

1. **Save** the configuration.

1. You are returned to the **Launches** tab of the Content Fragments console, where:

   * your new launch is now listed
   * a message is shown to confirm that the launch creation has started: 

     * **Job started to create new Launch, monitor the progress in AEM and reload page when done.** 

1. Select **View**, from the message box, to see further details in the AEM console for [Background Operations](/help/operations/asynchronous-jobs.md).

   ![New launch in console](/help/sites-cloud/administering/content-fragments/assets/cf-launches-new-launch-in-console.png)

## Edit Launch content {#edit-launch-content}

To edit the Content Fragments in your launch:

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch to show the toolbar actions.

1. Select **Open Launch**.

   Your launch will be shown, together with the fragments it holds.

   ![Edit Launch content](/help/sites-cloud/administering/content-fragments/assets/cf-launches-edit-launch-content.png)

1. Select **Edit** for the fragment you want to update. It will open in the [fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md) as usual.

## Manage content within a Launch {#manage-content-within-a-launch}

To manage the Content Fragments in your launch, and also edit their content:

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch.

1. Select **Edit Sources**.

   The source fragments of your launch will be shown.

   ![Edit Source](/help/sites-cloud/administering/content-fragments/assets/cf-launches-edit-sources.png)

1. You can:

   1. **Add Sources** to add more fragments to your launch.

      * If **Include References** is true for the launch, all referenced Content Fragments will be brought into the launch as well (if not already present).

   1. Select **Edit** for the source fragment you want to update. It will open in the [fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md) as usual.

   1. Select a fragment, then the **Delete Sources** action from the toolbar to remove that fragment from the launch. 

      * If **Include References** is true for the launch, all referenced Content Fragments will be removed from the launch as well - unless they are also referenced by other Content Fragments still in the launch.

   >[!NOTE]
   >
   >See [Details concerning Included References](#details-concerning-included-references)

## Compare Launch to Source {#compare-launch-to-source}

It is recommended that before any Rebase or Promote action you always compare the source and launch to confirm the changes and their impact on your content (both actions overwrite the target content):

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch.

1. Select **Compare Launch to Source**.

   * The source and launch fragments are shown side-by-side to highlight the differences.
     * Source fragments are displayed on the left, Launch fragments are displayed on the right.
     * Updates are highlighted:
       * Source: blue
       * Launch: pink
       * Conflicts: yellow
   * The [Promote](#promote-a-launch-to-source) and [Rebase](#rebase-a-launch-from-source) actions are available from the top right.
   * **Updates found**: In the upper left, a summary of all updates is displayed. The number of source updates in blue, the number of launch updates in pink, and updates to both (conflicts) in yellow. 
     * The eye icons allow you to show, or hide, the actual content updates for a clearer overview.
   * **Include** sliders allow you to define the Content Fragments to be included in the subsequent Promote or Rebase operation:
     * **Include All** at the top right
     * **Include** above every fragment in the launch

     >[!NOTE]
     >
     >The sliders only apply to Promote and Rebase actions taken from the Compare screen.

   * Fragment content is displayed at field-level (Content Fragment element/datatype-level); with highlights indicating changes. 
   * Select **View** to recompute the differences.

   ![Compare Source and Launch](/help/sites-cloud/administering/content-fragments/assets/cf-launches-compare.png)

## Rebase a Launch (from Source) {#rebase-a-launch-from-source}

When updates have been made to the source fragments and you want to copy these changes to your launch:

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch and fragments.

1. Select **Rebase**.

>[!NOTE]
>
>You can also **Rebase** a launch from **[Compare Launch to Source](#compare-launch-to-source)**.

## Promote a Launch (to Source) {#promote-a-launch-to-source}

When your launch is ready to be published it should be copied to the source. You can either do this in the console, or configure the settings for it to happen automatically at a specific date and time.

### Promote Manually {#promote-manually}

When your launch is ready to be published it can be copied to the source with the explicit action:

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch and fragments.

1. Select **Promote**.

>[!NOTE]
>
>You can also **Promote** a launch from **Compare Launch to Source**.

### Promote Automatically {#promote-automatically}

For a launch to be automatically promoted at a specified date and time you need to:

1. Define the **Promote Date** and Time from the right panel of the  [Launches tab](#launches-in-the-content-fragment-console).

1. If the content can be published when it is promoted, set **Publish Ready** when [creating the launch](#create-a-launch), or from the right panel of the  [Launches tab](#launches-in-the-content-fragment-console).

## Delete a Launch {#delete-a-launch}

After you have promoted your launch, or decided that you do not need it anymore you can delete it:

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch.

1. Select **Delete Launch**.

   You are asked to confirm the action before the launch is deleted.

## Details concerning Included References {#details-concerning-included-references}

For Launches the following Content Fragment references are considered, dependent on [data type](/help/sites-cloud/administering/content-fragments/content-fragment-models.md#data-types):

* The **Fragment Reference** data type, applicable for both single fragment references, and multi-field fragment references.
* Fragments referenced inside the **Multi line text** data type when using **Rich Text**.

All points are also applicable for fragments referenced within variations

The following are not considered:

* Fragments referenced inside content reference data types, both **Content Reference** (path-based) and **Content Reference (UUID)**.
* Fragments referenced inside the **Fragment Reference (UUID)** data type.
