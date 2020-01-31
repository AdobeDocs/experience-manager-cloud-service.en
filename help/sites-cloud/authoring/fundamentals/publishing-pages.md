---
title: Publishing Pages
description: How to publish and unpublish pages using AEM
---

# Publishing Pages {#publishing-pages}

Once you have created and reviewed your content on the author environment, the goal is to [make it available on your public website](/help/sites-cloud/authoring/getting-started/concepts.md) (your publish environment).

This is referred to as publishing a page. When you want to remove a page from the publish environment is referred to as unpublishing. When publishing and unpublishing the page remains available on the author environment for further changes until you delete it.

You can publish/unpublish a page immediately or at a predefined date/time in the future.

## Terminology {#terminology}

You may encounter different terms related to publishing as you work with AEM.

* **Publish / Unpublish**
  * These are the primary terms for the actions that make your content publicly available on your publish environment (or not).
  * These are the terms used in AEM documentation.
* **Activate / Deactivate**
  * These terms are synonymous with publish/unpublish.
  * These terms were used in previous versions of AEM.
* **Replicate / Replication**
  * These are the technical terms describing the movement of data (e.g. page content, files, code, user comments) from one environment to another when you publish a page.
  * These terms are primarily used by developers.

## Publishing Pages {#publishing-pages-1}

Depending on your location, you can publish:

* [From the page editor](#publishing-from-the-editor)
* [From the sites console](#publishing-from-the-console)

>[!NOTE]
>
>If you do not have the required privileges for publishing a specific page:
>
>* A workflow will be triggered to notify the appropriate person of your request to publish.
>* This workflow may have been customized by your development team.
>* A message will be displayed briefly to notify you that the workflow was triggered.
<!--
>* This [workflow may have been customized](/help/sites-developing/workflows-models.md#main-pars-procedure-6fe6) by your development team.
>* A message will be displayed briefly to notify you that the workflow was triggered.
-->

### Publishing from the Editor {#publishing-from-the-editor}

If you are editing a page, it can be published directly from the editor.

1. Select the **Page Information** icon to open the menu and then the **Publish Page** option.

   ![Publishing a page via page options](/help/sites-cloud/authoring/assets/publishing-page-options.png)

1. Depending on whether the page has references that need publishing:

    * The page will be published directly if there are no references to be published.
    * If the page has references that need publishing, these will be listed in the **Publish** wizard, where you can either:
        * Specify which of the assets/tags/etc. you want to publish together with the page, then use **Publish** to complete the process.
        * Use **Cancel** to abort the action.

   ![Publishing references with the page](/help/sites-cloud/authoring/assets/publishing-references.png)

1. Selecting **Publish** will replicate the page to the publish environment. In the page editor an information banner will be shown confirming the publish action.

   ![Publish status info banner](/help/sites-cloud/authoring/assets/publishing-info.png)

   When viewing the same page in the console, the updated publication status is visible.

   ![Page publication status in column view in the sites console](/help/sites-cloud/authoring/assets/publishing-status-console-column.png)

>[!NOTE]
>
>Publishing from the editor is a shallow publish, i.e. only the selected page/pages is/are published and any child page(s) is/are not.

### Publishing from the Console {#publishing-from-the-console}

In the sites console there are two options for publishing:

* [Quick Publish](#quick-publish)
* [Manage Publication](#manage-publication)

#### Quick Publish {#quick-publish}

**Quick Publish** is for simple cases and publishes the selected page(s) immediately without any further interaction. Because of this, any non-published references will also be published automatically.

To publish a page with Quick Publish:

1. Select the page or pages in the sites console and click on the **Quick Publish** button.

   ![Selecting pages for publication](/help/sites-cloud/authoring/assets/publishing-select-pages.png)

1. In the Quick Publish dialog, confirm the publication by clicking on **Publish** or cancel by clicking on **Cancel**. Remember that any unpublished references will automatically be published as well.

   ![Quick publish confirmation](/help/sites-cloud/authoring/assets/publishing-quick-publish.png)

1. When the page is published an alert is shown confirming the publication.

>[!NOTE]
>
>Quick Publish is a shallow publish, i.e. only the selected page/pages is/are published and any child pages are not.

#### Manage Publication {#manage-publication}

**Manage Publication** offers more options than Quick Publish, allowing for the inclusion of child pages, customization of the references, and starting any applicable workflows as well as offering the option to publish at a later date.

To publish or unpublish a page using Manage Publication:

1. Select the page or pages in the sites console and click on the **Manage Publication** button.

   ![Selecting pages for publication](/help/sites-cloud/authoring/assets/publishing-select-pages.png)

1. The **Manage Publication** wizard starts. The first step, **Options**, allows you to:

    * Choose to publish or unpublish the selected pages.
    * Choose to take that action now or at a later date.

   Publishing later starts a workflow to publish the selected page or pages at the specified time. Conversely, unpublishing later starts a workflow to unpublish the selected page or pages at a specific time.

   If you want to cancel a publish/unpublish later, go to the Workflow Console to terminate the corresponding workflow. <!--If you want to cancel a publish/unpublish later, go to the [Workflow Console](/help/sites-administering/workflows.md) to terminate the corresponding workflow.-->

   ![Manage Publication Options](/help/sites-cloud/authoring/assets/publishing-manage-publication-options.png)

   Click **Next** to continue.

1. In the next step of the Manage Publication wizard, **Scope**, you can define the scope of the publication/un-publication such as including to include child pages and/or including references.

   ![Manage Publication Scope](/help/sites-cloud/authoring/assets/publishing-manage-publication-scope.png)

   You can use the **Add Content** button to add additional pages to the list of pages to be published in case you neglected to select one before starting the Manage Publication wizard.

   Clicking the Add Content button starts the [path browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#path-browser) to allow content selection.

   Select the required pages and then click **Select** to add the content to the wizard or **Cancel **to cancel the selection and return to the wizard.

   Back in the wizard, you can select an item in the list to configure its further options such as:

    * Include its children.
    * Remove it from the selection.
    * Manage its published references.

   ![Manage Publication selecting pages](/help/sites-cloud/authoring/assets/publishing-manage-publication-select.png)

   Clicking **Include Children** opens a dialogue allowing you to:

    * Include only immediate children.
    * Include only modified pages.
    * Include only already published pages.

   Click **Add** to add the children pages to the list of pages to be published or unpublished based on the selection options. Click **Cancel** to cancel the selection and return to the wizard.

   ![Manage Publication including children](/help/sites-cloud/authoring/assets/publishing-include-children.png)

   Returning to the wizard you see the pages added based on your choice of options in the Include Children dialogue.

   You can view and modify the references to be published or unpublished for a page by selecting it and then clicking the **Published References** button.

   ![Manage Publication Options](/help/sites-cloud/authoring/assets/publishing-manage-publication-references.png)

   The **Published References** dialog displays the references for the selected content. By default they are all selected and will be published/unpublished, but you can un-check to deselect them so that they are not included in the action.

   Click **Done** to save your changes or **Cancel** to cancel the selection and return to the wizard.

   Back in the wizard, the **References** column will be updated to reflect your selection of references to be published or unpublished.

   ![Manage Publication selecting pages](/help/sites-cloud/authoring/assets/publishing-manage-publication-select.png)

1. Click **Publish** to complete.

   Back in the sites console a notification message will confirm the publication.

1. If the published pages are associated with workflows, they may be shown in a final **Workflows** step of the publication wizard.

   >[!NOTE]
   >
   >The **Workflows** step will be shown based on what rights your user may or may not have. See the previous note on this page regarding publishing privileges as well as Managing Access to Workflows and [Applying Workflows to Pages](/help/sites-cloud/authoring/workflows/applying.md) for details.
   <!--
   >The **Workflows** step will be shown based on what rights your user may or may not have. See the previous note on this page regarding publishing privileges as well as [Managing Access to Workflows](/help/sites-administering/workflows-managing.md) and [Applying Workflows to Pages](/help/sites-cloud/authoring/workflows/applying.md) for details.
   -->

   The resources are grouped by the workflows triggered and each given options to:

    * Define the title of the workflow.
    * Keep the workflow package, provided that the workflow has multi-resource support. <!--Keep the workflow package, provided that the workflow has [multi-resource support](/help/sites-developing/workflows-models.md#configuring-a-workflow-for-multi-resource-support).-->
    * Define a title of the workflow package if the option to keep the workflow package was chosen.

   Click **Publish** or **Publish Later** to complete the publication.

## Unpublishing Pages {#unpublishing-pages}

Unpublishing a page will remove it from your publish environment so that it is no longer available to your readers.

In a [manner similar to publishing](#publishing-pages), one or more pages can be unpublished:

* [From the page editor](#unpublishing-from-the-editor)
* [From the sites console](#unpublishing-from-the-console)

### Unpublishing from the Editor {#unpublishing-from-the-editor}

When editing a page, if you wish to unpublish that page, select **Unpublish Page** in the **Page Information** menu, much as you would [publish the page](#publishing-from-the-editor).

### Unpublishing from the Console {#unpublishing-from-the-console}

Just as you [use the Manage Publication option to publish](#manage-publication), you can also use it to unpublish.

1. Select the page or pages in the sites console and click on the **Manage Publication** button.
1. The **Manage Publication** wizard starts. In the first step, **Options**, select to **Unpublish** instead of the default option of **Publish**.

   ![Unpublishing](/help/sites-cloud/authoring/assets/publishing-unpublish.png)

   Just as publishing later starts a workflow to publish this version of the page at the specified time, deactivating later starts a workflow to unpublish the selected page or pages at a specific time.

   If you want to cancel a publish/unpublish later, go to the Workflow Console to terminate the corresponding workflow. <!--If you want to cancel a publish/unpublish later, go to the [Workflow Console](/help/sites-administering/workflows.md) to terminate the corresponding workflow.-->

1. To complete the un-publication, continue through the wizard as you would to [publish the page](#manage-publication).

## Publishing and Unpublishing a Tree {#publishing-and-unpublishing-a-tree}

When you have entered or updated a considerable number of content pages - all of which are resident under the same root page - it can be easier to publish the entire tree in one action.

You can use the [Manage Publication](#manage-publication) option on the sites console to do this.

1. In the sites console, select the root page of the tree you wish to publish or unpublish and select **Manage Publication**.
1. The **Manage Publication** wizard starts. Choose to publish or unpublish and when it should occur and select **Next** to continue.
1. In the **Scope** step, select the root page and select **Include Children**.

   ![Manage Publication selecting pages](/help/sites-cloud/authoring/assets/publishing-manage-publication-select.png)

1. In the **Include Children** dialogue, un-check the options:

    * Include only immediate children
    * Include only already published pages

   These options are selected by default, so you must remember to unselect them. Click **Add** to confirm and add the content to the publication/un-publication.

   ![Including children when un-publishing](/help/sites-cloud/authoring/assets/publishing-tree-children.png)

1. The **Manage Publication** wizard lists the content of the tree for review. You can further customize the selection by adding additional pages or removing those selected.

   ![Manage Publication options](/help/sites-cloud/authoring/assets/publishing-tree-select.png)

   Remember that you can also review the references to be published via the **Published References** option.

1. [Continue the Manage Publication wizard as normal](#manage-publication) to complete the publication or un-publication of the tree.

## Determining Publication Status {#determining-publication-status}

You can determine the publication status of a page:

* In the [resource overview information on the sites console](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources)

  ![Publication status in card view](/help/sites-cloud/authoring/assets/publishing-status-console-card.png)

  The publication status is shown in [card](/help/sites-cloud/authoring/getting-started/basic-handling.md#card-view), [column](/help/sites-cloud/authoring/getting-started/basic-handling.md#column-view), and [list](/help/sites-cloud/authoring/getting-started/basic-handling.md#list-view) views in the sites console.

* In the [timeline](/help/sites-cloud/authoring/getting-started/basic-handling.md#timeline)

  ![Publication status in timeline view](/help/sites-cloud/authoring/assets/publishing-status-timeline.png)

* In the [Page Information menu](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-information) when editing a page

  ![Publication status in Page Information menu](/help/sites-cloud/authoring/assets/publishing-status-page-information.png)
