---
title: Publishing Pages
description: Learn how to publish, and unpublish, your pages using various mechanisms in AEM.
exl-id: 89f2363c-7922-4ca5-92cb-cbee6a393ee3
solution: Experience Manager Sites
feature: Authoring
role: User
---
# Publishing Pages {#publishing-pages}

Once you have created and reviewed your content on the author environment, the goal is to [make it available on your public website](/help/sites-cloud/authoring/author-publish.md) (your publish environment).

This is referred to as publishing a page. When you want to remove a page from the publish environment is referred to as unpublishing. When publishing and unpublishing, the page remains available on the author environment for further changes until you delete it.

You can publish/unpublish a page immediately or at a predefined date/time in the future.

>[!NOTE]
>
>Publishing an [Experience Fragment](/help/sites-cloud/authoring/fragments/experience-fragments.md) basically follows the same procedure as for publishing a page, though from the Experience Fragments console or editor.

## Terminology {#terminology}

You may encounter different terms related to publishing as you work with Adobe Experience Manager (AEM) as a Cloud Service.

* **Publish / Unpublish**
  * These are the primary terms for the actions that make your content publicly available on your publish and/or preview environment(s) (or not).
  * These are the terms used in AEM documentation.
* **Activate / Deactivate**
  * These terms are synonymous with publish/unpublish.
  * These terms were used in previous versions of AEM.
* **Replicate / Replication**
  * These are the technical terms describing the movement of data (for example, page content, files, code, user comments) from one service to another when you publish a page (e.g. from author to preview).
  * These terms are primarily used by developers.

## Publishing Pages {#publishing-pages-1}

Depending on your location, you can publish:

* [From the page editor](#publishing-from-the-page-editor)
* [From the **Sites** console](#publishing-from-the-sites-console)
* [From the Universal Editor](/help/sites-cloud/authoring/universal-editor/publishing.md)

>[!NOTE]
>
>If you do not have the required privileges for publishing a specific page:
>
>* A workflow is triggered to notify the appropriate person of your request to publish.
>* This workflow may have been customized by your development team.
>* A message is displayed briefly to notify you that the workflow was triggered.

>[!NOTE]
>
>If you want to preserve page order you have to use [Manage Publication](#manage-publication) to publish the parent page together with any child pages in a single action.
>
>Page order is not guaranteed:
>
>* if only child pages are selected for publication (as the order information is held on the parent page)
>* if the parent and child pages are published in separate actions 

### Publishing from the Page Editor {#publishing-from-the-page-editor}

If you are editing a page in the [page editor](/help/sites-cloud/authoring/page-editor/introduction.md), it can be published directly from the editor.

1. Select the **Page Information** icon to open the menu and then the **Publish Page** option.

   ![Publishing a page via page options](/help/sites-cloud/authoring/assets/publishing-page-options.png)

1. Depending on whether the page has references that need publishing:

   * The page is published directly if there are no references to be published.
   * If the page has references that need publishing, these are listed in the **Publish** wizard, where you can either:
     * Specify which of the assets, or tags, and so on, that you want to publish together with the page, then use **Publish** to complete the process.
     * Use **Cancel** to abort the action.

   ![Publishing references with the page](/help/sites-cloud/authoring/assets/publishing-references.png)

1. Selecting **Publish** will replicate the page to the publish environment. In the page editor, an information banner is shown confirming the publish action.

   ![Publish status info banner](/help/sites-cloud/authoring/assets/publishing-info.png)

   When viewing the same page in the console, the updated publication status is visible.

   ![Page publication status in column view in the sites console](/help/sites-cloud/authoring/assets/publishing-status-console-column.png)

>[!NOTE]
>
>Publishing from the page editor is a shallow publish, that is, only the selected page/pages is/are published and any child page(s) is/are not.

>[!NOTE]
>
>Pages accessed by [aliases](/help/sites-cloud/authoring/sites-console/page-properties.md#advanced) in the editor cannot be published. Publish options in the editor are only available for pages accessed via their actual paths.

### Publishing from the Site Console {#publishing-from-the-sites-console}

In the **Sites** console there are two options for publishing:

* [Quick Publish](#quick-publish)
* [Manage Publication](#manage-publication)

#### Quick Publish {#quick-publish}

**Quick Publish** is for simple cases and publishes the selected page(s) immediately without any further interaction. Because of this, any non-published references will also be published automatically.

To publish a page with Quick Publish:

1. Select the page or pages in the sites console and click the **Quick Publish** button.

   ![Selecting pages for publication](/help/sites-cloud/authoring/assets/publishing-select-pages.png)

1. In the Quick Publish dialog, confirm the publication by clicking on **Publish** or cancel by clicking on **Cancel**. Remember that any unpublished references will automatically be published as well.

   ![Quick publish confirmation](/help/sites-cloud/authoring/assets/publishing-quick-publish.png)

1. When the page is published an alert is shown confirming the publication.

>[!NOTE]
>
>Quick Publish is a shallow publish, that is, only the selected page/pages is/are published and any child pages are not.

#### Manage Publication {#manage-publication}

**Manage Publication** offers more options than **Quick Publish**, allowing for the inclusion of child pages, customization of the references, publishing to a preview service (if available,) and starting any applicable workflows and offering the option to publish at a later date.

To publish or unpublish a page using Manage Publication:

1. Select the page or pages in the sites console and click the **Manage Publication** button.

   ![Selecting pages for publication](/help/sites-cloud/authoring/assets/publishing-select-pages.png)

1. The **Manage Publication** wizard starts. The first step, **Options**, lets you:

   * **Action**

     Choose to publish or unpublish the selected pages.

   * **Destination** 

     Choose if you wish to publish to your publish service (default) or your preview service. Only available if you have a [preview service configured.](//help/sites-cloud/authoring/sites-console/previewing-content.md)

   * **Scheduling**

     Choose to take that action now or at a later date.

     Publishing later starts a workflow to publish the selected page or pages at the specified time. Conversely, unpublishing later starts a workflow to unpublish the selected page or pages at a specific time.

     >[!NOTE]
     >
     >If you want to cancel a publish/unpublish later, go to the [Workflow Console](/help/sites-cloud/administering/workflows-administering.md#suspending-resuming-and-terminating-a-workflow-instance) to terminate the corresponding workflow.

     >[!NOTE]
     >
     >Scheduling content for publishing is not the same as [**On Time** and **Off Time** available in the page properties,](/help/sites-cloud/authoring/sites-console/page-properties.md#basic) but can be used in similar circumstances.

   ![Manage Publication Options](/help/sites-cloud/authoring/assets/publishing-manage-publication-options.png)

1. Click **Next** to continue.

1. In the next step of the Manage Publication wizard, **Scope**, you can define the scope of the publication/un-publication such as including to include child pages and/or including references.

   ![Manage Publication Scope](/help/sites-cloud/authoring/assets/publishing-manage-publication-scope.png)

   **Add Content**

   You can use the **Add Content** button to add additional pages to the list of pages to be published in case you neglected to select one before starting the Manage Publication wizard.

   Selecting the **Add Content** button starts the [path browser](/help/sites-cloud/authoring/path-selection.md) to allow content selection.

   Select the required pages and then click **Select** to add the content to the wizard or **Cancel** to cancel the selection and return to the wizard.

   **Remove Selection**

   Back in the wizard, you can select an item in the list to remove it from the selection.

   ![Manage Publication selecting pages](/help/sites-cloud/authoring/assets/publishing-manage-publication-select.png)

   **Published References**

   You can view and modify the references to be published or unpublished for a page by selecting it and then clicking the **Published References** button.

   ![Manage Publication Options](/help/sites-cloud/authoring/assets/publishing-manage-publication-references.png)

   The **Published References** dialog displays the references for the selected content. By default, they are all selected and are published/unpublished, but you can un-check to deselect them so that they are not included in the action.

   Click **Done** to save your changes or **Cancel** to cancel the selection and return to the wizard.

   Back in the wizard, the **References** column is updated to reflect your selection of references to be published or unpublished.

   ![Manage Publication selecting pages](/help/sites-cloud/authoring/assets/publishing-manage-publication-select.png)

   **Include Children**
   
   >[!NOTE]
   >
   >See [Publishing and Unpublishing a Tree](#publishing-and-unpublishing-a-tree)
   
   Clicking **Include Children** opens a dialog box allowing you to:

   * **Include children**
   * **Include only immediate children**
   * **Include only modified pages**
   * **Include only already published pages**

   Activate the required options and confirm with **OK** to add the children pages to the list of pages to be published or unpublished based on the selection options. Click **Cancel** to cancel the selection and return to the wizard.

   ![Manage Publication including children](/help/sites-cloud/authoring/assets/publishing-include-children.png)

1. Click **Publish** to complete.

   Back in the sites console a notification message will confirm the publication.

1. If the published pages are associated with workflows, they may be shown in a final **Workflows** step of the publication wizard.

   ![Manage Publication selecting pages](/help/sites-cloud/authoring/assets/publishing-manage-publication-workflow.png)

   >[!NOTE]
   >
   >The **Workflows** step is shown based on what rights your user may or may not have. See the previous note on this page regarding publishing privileges and Managing Access to Workflows and [Applying Workflows to Pages](/help/sites-cloud/authoring/workflows/applying.md) for details.

   The resources are grouped by the workflows triggered and each given options to:

   * Define the title of the workflow.
   * Keep the workflow package, provided that the workflow has multi-resource support. 
   * Define a title of the workflow package if the option to keep the workflow package was chosen.

1. Click **Publish** or **Publish Later** to complete the publication.



## Unpublishing Pages {#unpublishing-pages}

Unpublishing a page will remove it from your publish, or [preview](/help/sites-cloud/authoring/sites-console/previewing-content.md), environment so that it is no longer available to your readers.

In a [manner similar to publishing](#publishing-pages), one or more pages can be unpublished from the desired destination:

* [From the page editor](#unpublishing-from-the-editor)
* [From the sites console](#unpublishing-from-the-console)

### Unpublishing from the Editor {#unpublishing-from-the-editor}

When editing a page, if you want to unpublish that page, select **Unpublish Page** in the **Page Information** menu, much as you would [publish the page](#publishing-from-the-editor).

>[!NOTE]
>
>Pages accessed by [aliases](/help/sites-cloud/authoring/sites-console/page-properties.md#advanced) in the editor cannot be unpublished. Publish options in the editor are only available for pages accessed via their actual paths.

### Unpublishing from the Console {#unpublishing-from-the-console}

Just as you [use the Manage Publication option to publish](#manage-publication), you can also use it to unpublish.

1. Select the page or pages in the sites console and click the **Manage Publication** button.
1. The **Manage Publication** wizard starts. In the first step, **Options**, select to **Unpublish** instead of the default option of **Publish**.

   ![Unpublishing - Options](/help/sites-cloud/authoring/assets/publishing-unpublish.png)

   Just as publishing later starts a workflow to publish this version of the page at the specified time, deactivating later starts a workflow to unpublish the selected page or pages at a specific time.

   >[!NOTE]
   >
   >If you want to cancel a publish/unpublish later, go to the [Workflow Console](/help/sites-cloud/administering/workflows-administering.md#suspending-resuming-and-terminating-a-workflow-instance) to terminate the corresponding workflow.

   >[!NOTE]
   >If you have a [Preview](/help/sites-cloud/authoring/sites-console/previewing-content.md) environment you can select the **Destination** during Manage Publication.

1. To complete the un-publication, continue through the wizard as you would to [publish the page](#manage-publication).

   ![Unpublishing - Scope](/help/sites-cloud/authoring/assets/publishing-unpublish-scope.png)

## Publishing and Unpublishing a Tree {#publishing-and-unpublishing-a-tree}

When you have entered or updated a considerable number of content pages - all of which are resident under the same root page - it can be easier to publish the entire tree in one action.

You can use the [Manage Publication](#manage-publication) option on the sites console to do this.

1. In the sites console, select the root page of the tree you want to publish or unpublish and select **Manage Publication**.
1. The **Manage Publication** wizard starts. Choose to publish or unpublish and when it should occur and select **Next** to continue.
1. In the **Scope** step, select the root page and select **Include Children**.

   ![Manage Publication selecting pages](/help/sites-cloud/authoring/assets/publishing-manage-publication-select.png)

1. In the **Include Children** dialog:

   * select **Include Children**
   * unselect **Include only immediate children**
   * unselect **Include only already published pages**
   * configure **Include only modified pages** as required

   These options are selected by default, so you must remember to configure them. Confirm the selection with **OK** to add the content to the publication/un-publication.

   ![Including children for tree publication](/help/sites-cloud/authoring/assets/publishing-include-children-tree.png)

1. In the **Manage Publication** wizard you can further customize the selection by adding additional pages or removing those selected.

   Remember that you can also review the references to be published via the **Published References** option.

1. [Continue the Manage Publication wizard as normal](#manage-publication) to complete the publication or un-publication of the tree.

## Determining Publication Status {#determining-publication-status}

You can determine the publication status of a page:

* In the [resource overview information on the sites console](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources)

  ![Publication status in card view](/help/sites-cloud/authoring/assets/publishing-status-console-card.png)

  The publication status is shown in [card](/help/sites-cloud/authoring/basic-handling.md#card-view), [column](/help/sites-cloud/authoring/basic-handling.md#column-view), and [list](/help/sites-cloud/authoring/basic-handling.md#list-view) views in the sites console.

* In the [timeline](/help/sites-cloud/authoring/basic-handling.md#timeline)

  ![Publication status in timeline view](/help/sites-cloud/authoring/assets/publishing-status-timeline.png)

* In the [Page Information menu](/help/sites-cloud/authoring/page-editor/introduction.md#page-information) when editing a page

  ![Publication status in Page Information menu](/help/sites-cloud/authoring/assets/publishing-status-page-information.png)
