---
title: Launches for Content Fragments
description: Learn how to use Launches for Content Fragments in Adobe Experience Manager as a Cloud Service. Launches enable you to efficiently develop content for a future release, while maintaining your current Content Fragments.
feature: Content Fragments
role: User, Developer, Architect
solution: Experience Manager Sites
---

# Launches for Content Fragments {#launches-for-content-fragments}

In Adobe Experience Manager (AEM) as a Cloud Service, Launches enable you to efficiently develop content for a future release.

A *Launch* is created to allow you to make changes in preparation for future publication, at the same time as maintaining your current content. For Content Fragments this means that you are effectively editing two versions at the same time: content that is currently published, and a version of that content, to be published at a time in the future. Once that time arrives you can replace the content of the original Content Fragments and publish the new versions. 

>[!NOTE]
>
>Launches are also available for Pages. The basic concepts are the same, but there are differences in how to manage them in AEM. 
>
>For full details see [Launches for Pages](/help/sites-cloud/authoring/launches/overview.md).

<!-- Confirm this content-->

You create a *Launch*, then after editing and updating Content Fragments in your *Launch* you *Promote* them back to the *Source*. If changes are made to the *Source* fragments during this phase, you can copy them to the *Launch* with the *Rebase* operation. When ready, *Promote* duplicates the launch content back to the source. You can then activate your source fragments, either manually or automatically (dependent on fields set when creating and editing the launch).

For example, the seasonal product fragments of your online store are updated quarterly so that the featured products align with the current season. To prepare for the next quarterly update, you can create a launch of the appropriate fragments. Throughout the quarter, the following changes are accumulated in the launch copy:

* Edits that are performed directly on the launch fragments in preparation for the next quarter.
* Changes to the source Content Fragments that you transfer to the launch pages with *Rebase*.

You can also:

* Navigate content in the launch branch; adding, or removing, fragments as necessary.
* Preview how published content will look at a specific date in the future.

When the next quarter arrives, you promote the launch pages, so that you can publish the source pages (holding the updated content). You can promote either all fragments, or only those that you have modified.

This section describes how to create, edit and promote (and if necessary [delete](/help/sites-cloud/authoring/launches/creating.md#deleting-a-launch)) launch fragments from within the [Content Fragments console](/help/sites-cloud/administering/content-fragments/managing.md):

* [Create a Launch](#create-a-launch)
* [Edit Launch content](#edit-launch-content)
* [Manage content within a Launch](#manage-content-within-a-launch)
* [Rebase a Launch](#rebase-a-launch)
* [Promote a Launch](#promote-a-launch)
* [Delete a Launch](#delete-a-launch)

## Create a Launch {#create-a-launch}

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select **Create Launch**.

1. Select the fragments to be included in the launch.

1. Specify details to configure the launch:

   * **Title**
   * **Description**
   * **Include References**: Create the Launch either with, or without, including any referenced Content Fragments. By default, referenced fragments are included.
   * **Publish Ready**: Enabling this toggle will automatically publish the fragments when the launch is promoted to the source.

1. **Save** the configuration.

1. You are returned to the **Launches** tab of the Content Fragments console, where:

   * your new launch is also listed.
   * a message is shown to confirm that the launch creation has started: 

     * **Job started to create new Launch, monitor the progress in AEM and reload page when done.** 

     Select **View** to see further details.

## Edit Launch content {#edit-launch-content}

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch.

1. Select **Open Launch**.

   Your launch will be shown, together with the fragments it holds.

1. Select **Edit** for the fragment you want to update. It will open in the [fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md) as usual.

## Manage content within a Launch {#manage-content-within-a-launch}

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch.

1. Select **Edit Sources**.

   The source fragments of your launch will be shown.

1. You can:

   1. **Add Sources** to add more fragments to your launch.

   1. Select **Edit** for the source fragment you want to update. It will open in the [fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md) as usual.

   1. Select a fragment, then the **Delete Sources** action from the toolbar to remove that fragment from the launch. 

## Compare Launch to Source {#compare-launch-to-source}

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch.

1. Select **Compare Launch to Source**.

   The source and launch fragments will be shown side-by-side to highlight the differences.

### Rebase a Launch {#rebase-a-launch}

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch.

1. Select **Rebase**.

>[!NOTE]
>
>You can also **Rebase** a launch from **Compare Launch to Source**.

### Promote a Launch {#promote-a-launch}

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch.

1. Select **Promote**.

>[!NOTE]
>
>You can also **Promote** a launch from **Compare Launch to Source**.

## Delete a Launch {#delete-a-launch}

1. Navigate to the Content Fragments console.

1. Open the **Launches** tab.

1. Select your launch.

1. Select **Delete Launch**.

   You are asked to confirm the action before the launch is deleted.
