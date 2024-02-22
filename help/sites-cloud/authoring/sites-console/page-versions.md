---
title: Working with Page Versions
description: Learn how to create, compare, and restore versions of your pages in AEM.
exl-id: 33d8e43c-594d-4bba-9631-b2c42a1e910f
---
# Working with Page Versions {#working-with-page-versions}

Versioning creates a "snapshot" of a page at a specific point in time. With versioning, you can perform the following actions:

* Create a version of a page.
* Reinstate a previous version of one, or more, pages, to:
  * Undo changes made to the pages.
  * Restore pages that were deleted.
  * Restore a tree (as at a specified date and time).
* Preview a version.
* Compare the current version of a page with a previous version.
  * Differences in the text and images are highlighted.
* Timewarp uses the page versions to determine the state of the publish environment.

## Creating a New Version {#creating-a-new-version}

You can create a version of your resource from:

* The [Timeline rail](#creating-a-new-version-timeline)
* The [Create](#creating-a-new-version-create-with-a-selected-resource) option (when a resource is selected)

### Creating a New Version - Timeline {#creating-a-new-version-timeline}

1. Navigate to show the page for which you want to create a version.
1. Select the page in [selection mode](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources).
1. Open the **Timeline** rail.
1. Select the ellipsis by the comment field to reveal the options:

   ![Versions in the timeline rail](/help/sites-cloud/authoring/assets/versions-timeline-rail.png)

1. Select **Save as Version**.
1. Enter a **Label** and **Comment**, if necessary.

   ![Add label for a version](/help/sites-cloud/authoring/assets/versions-add-label.png)

1. Confirm the new version with **Create**.

   The information in the timeline is updated to indicate the new version.

### Creating a New Version - Create with a Selected Resource {#creating-a-new-version-create-with-a-selected-resource}

1. Navigate to show the page for which you want to create a version.
1. Select the page in [selection mode](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources).
1. Select the **Create** option from the toolbar.
1. The same dialog box opens. You can enter a **Label** and a **Comment**, if necessary.
1. Confirm the new version with **Create**.

The timeline is opened with the information updated to indicate the new version.

## Reinstating Versions {#reinstating-versions}

Once you have created a version of your page, there are various methods of reinstating a prior version:

* the **Revert to this Version** option from the [Timeline](/help/sites-cloud/authoring/basic-handling.md#timeline) rail

  Reinstate a prior version of a selected page.

* the **Restore** options from the top [actions toolbar](/help/sites-cloud/authoring/basic-handling.md#actions-toolbar)

  * **Restore Version**

    Reinstate versions of specified pages within the currently selected folder. It can also include restoring pages that have been previously deleted.

  * **Restore Tree**

    Reinstate a version of an entire tree as at a specified date and time. It can also include pages that have been previously deleted.

>[!NOTE]
>
>When reinstating a page, the version created is part of a new branch.
>
>To illustrate:  
>
>1. Create versions of any page.
>1. The initial labels and version node names are 1.0, 1.1, 1.2, and so forth.  
>1. Reinstate the first version; that is, 1.0.
>1. Create versions again.
>1. The generated labels and node names are now 1.0.0, 1.0.1, 1.0.2, and so on.

### Revert to a Version {#revert-to-a-version}

To **Revert** the selected page to a previous version:

1. Navigate to show the page that you want to revert to a previous version.
1. Select the page in [selection mode](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources).
1. Open the **Timeline** column and select either **Show All** or **Versions**. The page versions for the selected page are listed.
1. Select the version that you want to revert to. The possible options are shown:

   ![Revert to this Version](/help/sites-cloud/authoring/assets/versions-revert.png)

1. Select **Revert to this Version**. The selected version is restored and the information in timeline is updated.

### Restore Version {#restore-version}

This method can be used to restore versions of specified pages within the current folder. It can also include restoring pages that have been previously deleted:

1. Navigate to, and [select](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources), the required folder.

1. Select **Restore**, then **Restore Version** from the top [actions toolbar](/help/sites-cloud/authoring/basic-handling.md#actions-toolbar).

   >[!NOTE]
   >
   >If you either have:
   >
   >* selected a single page that has never had any child pages,
   >* or none of the pages in the folder have versions,
   >
   >The display becomes empty because there are no applicable versions.

1. The available versions are listed:

   ![Restore Version - List of all pages in folder](/help/sites-cloud/authoring/assets/versions-restore-version-01.png)

1. For a specific page, use the drop-down selector under **RESTORE TO VERSION** to select the required version for that page.

   ![Restore Version - Select Version](/help/sites-cloud/authoring/assets/versions-restore-version-02.png)

1. In the main display, select the required page to be restored:

   ![Restore Version - Select Page](/help/sites-cloud/authoring/assets/versions-restore-version-03.png)

1. Select **Restore** for the selected version, of the selected page, to be restored as the current version.

>[!NOTE]
>
>The order in which you select a required page and the related version is interchangeable.

### Restore Tree {#restore-tree}

This method can be used to restore a version of a tree as at a specified date and time. It can include pages that have been previously deleted:

1. Navigate to, and [select](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources), the required folder.

1. Select **Restore**, then **Restore Tree** from the top [actions toolbar](/help/sites-cloud/authoring/basic-handling.md#actions-toolbar). The latest version of the tree is shown:

   ![Restore Tree](/help/sites-cloud/authoring/assets/versions-restore-tree-01.png)

1. Use the date and time selector at **Latest Versions at Date** so you can select another version of the tree - the one to be restored.

1. Set the flag **Preserved Non Versioned Pages** as required:

   * If active (selected), any non-versioned pages are maintained and not impacted by the restore. 

   * If inactive (unselected), any non-versioned pages are removed as they did not exist in the versioned tree.

1. Select **Restore** for the selected version of the tree to be restored as the *current* version.

## Previewing a Version {#previewing-a-version}

You can preview a specific version:

1. Navigate to show the page that you want to compare.
1. Select the page in [selection mode](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources).
1. Open the **Timeline** column and select either **Show All** or **Versions**.
1. The page versions are listed. Select the version that you want to preview:

   ![Preview version](/help/sites-cloud/authoring/assets/versions-revert.png)

1. Select **Preview**. The page is shown in a new tab.

   >[!CAUTION]
   >
   >If a page has been moved, you can no longer perform a preview on any versions made before the move.
   >
   >If you experience problems with a preview, check the [Timeline](/help/sites-cloud/authoring/basic-handling.md#timeline) for the page to see whether the page has been moved.
  
## Comparing a Version with Current Page {#comparing-a-version-with-current-page}

To compare a previous version with the current page:

1. Navigate to show the page that you want to compare.
1. Select the page in [selection mode](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources).
1. Open the **Timeline** column and select either **Show All** or **Versions**.
1. The page versions are listed. Select the version that you want to compare:

   ![Compare versions](/help/sites-cloud/authoring/assets/versions-revert.png)

1. Select **Compare to Current**. The [page diff](/help/sites-cloud/authoring/sites-console/page-diff.md) opens and displays the differences.

## Timewarp {#timewarp}

Timewarp is a feature designed to simulate the *published* state of a page at specific times in the past.

>[!TIP]
>
>[Timewarp can also be used with Launches to preview the future](/help/sites-cloud/authoring/launches/preview.md).

Because content creation is an ongoing and collaborative process, the purpose of Timewarp is to allow authors to track the published website over time so they can understand how the content has changed. This feature uses the page versions to determine the state of the publish environment.

To use this feature:

* The system looks for the page version that was active at the selected time.
* It means the version shown was created/activated *before* the point in time selected in Timewarp.
* When navigating to a page that has been deleted, it also rendered - as long as the old versions of the page are still available in the repository.
* If no published version is found, Timewarp reverts to the current state of the page on the author environment (the reason is to prevent an error/404 page, which would prevent browsing).

### Using Timewarp {#using-timewarp}

Timewarp is a [mode](/help/sites-cloud/authoring/page-editor/introduction.md#page-modes) of the page editor. To start it, simply switch it as you would any other mode.

1. Start the editor for the page where you want to start Timewarp and then select **Timewarp** in the mode selection.

   ![Timewarp mode](/help/sites-cloud/authoring/assets/versions-timewarp-mode.png)

1. In the dialog box, set a target date and time and click **Set Date**. If you do not select a time, it defaults to use the current time.

   ![Timewarp target date](/help/sites-cloud/authoring/assets/versions-timewarp-target.png)

1. The page is displayed based on the date set. Timewarp mode is indicated by way of the blue status bar at the top of the window. Use the links in the status bar so you can select a new target date or exit Timewarp mode.

   ![In Timewarp mode](/help/sites-cloud/authoring/assets/versions-timewarp.png)

### Timewarp Limitations {#timewarp-limitations}

Timewarp makes a best effort to reproduce a page at a selected point in time. However, because of the complexities of the continuous authoring of content in AEM, this reproduction is not always possible. Keep these limitations in mind as you use Timewarp.

* **Timewarp works based on published pages** - Timewarp only works fully if you have previously published the page. If not, Timewarp shows the current page on the author environment.
* **Timewarp uses page versions** - If you navigate to a page that has been removed/deleted from the repository it is rendered properly if old versions of the page are still available in the repository.
* **Removed versions affect Timewarp** - If versions are removed from the repository then Timewarp cannot show the correct view.  
* **Timewarp is read-only** - You cannot edit the old version of the page. It is only available for viewing. If you want to restore the older version, you must do that manually using [restore](#revert-to-a-version).
* **Timewarp is based on page content** - If elements for rendering the website changed, such as code, css, and assets, the view differs from what it was originally. Those items are not versioned in the repository.

>[!CAUTION]
>
>Timewarp is designed as a tool to assist authors with understanding and creating their content. It is not intended as an audit log or for legal purposes.
