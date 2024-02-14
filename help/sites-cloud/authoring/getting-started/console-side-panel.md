---
title: Sites Console Side Panel
description: Learn how to use the side panel in the AEM sites console to better understand and navigate your content.
---

# Sites Console Side Panel {#side-panel}

Learn how to use the side panel in the AEM sites console to better understand and navigate your content.

## Orientation {#orientation}

The side panel is by default closed when you enter the Sites console. In this way the screen is dedicated entirely to your content.

Tap or click the **Side Panel** icon in the sites console toolbar to activate the side panel and choose your view of the content.

* [Content Only](#content-only)
* [Content Tree](#content-tree)
* [Timeline](#timeline)
* [References](#references)
* [Filter](#filter)

## Content Only {#content-only}

This view of the side panel is effectively turning it off, i.e. to show only the content of your site.

Use the grave accent/backtick `´` keyboard shortcut to switch to the content only view of the side panel.

## Content Tree {#content-tree}

This view of the side panel displays your content in a tree hierarchy. The content tree can be used to quickly navigate the site hierarchy within the side panel and view much information about the pages in the current folder.

![The content tree view of the side panel](assets/console-side-panel-content-tree.png)

A right-pointing chevron next to an item in the tree indicates a node that can be expanded to reveal its children. Tap or click the chevron to reveal the children.

The console displays the content of the currently-select item in the content tree.

Using the content tree side panel in conjunction with a list view or cards view, users can easily see the hierarchical structure of the project and navigate easily across the content structure with the content tree side-panel, and view detailed page information in the list view.

Use the `Alt+1` keyboard shortcut to switch to the content tree view of the side panel.

>[!TIP]
>
>Once an entry in the hierarchy view is selected, arrow keys can be used to quickly navigate the hierarchy.
>
>See [keyboard shortcuts](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) for more information.

## Timeline {#timeline}

The timeline can be used to view and/or initiate events that have occurred on the selected resource.

![Comment field](/help/sites-cloud/authoring/assets/comments.png)

The timeline column lets you view various events related to a selected item selectable as types from a drop-down list:

* Comments
* [Annotations](/help/sites-cloud/authoring/fundamentals/annotations.md)
* [Activities](/help/sites-cloud/authoring/personalization/activities.md)
* [Launches](/help/sites-cloud/authoring/launches/overview.md)
* [Versions](/help/sites-cloud/authoring/features/page-versions.md)
* [Workflows](/help/sites-cloud/authoring/workflows/overview.md)
  * Note that no information will be shown for transient workflows as no history information is saved for these.<!--With the exception of [transient workflows](/help/sites-developing/workflows.md#transient-workflows) as no history information is saved for these-->
* Show All

In addition you can add/view comments about the selected item by using the **Comment** box shown at the bottom of the list of events. Typing a comment followed by `Return` will register the comment. It is shown when **Comments** or **Show All** is selected.

Tn the Sites console you can also access additional features via the elipsis button next to the **Comment** field.

* [Save a version](/help/sites-cloud/authoring/features/page-versions.md)
* [Start a workflow](/help/sites-cloud/authoring/workflows/applying.md)

### Accessing Page References {#accessing-page-references}

[Quick access to references](/help/sites-cloud/authoring/fundamentals/environment-tools.md#references) to/from a page are available in the References Rail.

1. Select **References** using the toolbar icon (either before or after [selecting your page](#selecting-your-page-for-further-action)):

   ![References view option](/help/sites-cloud/authoring/assets/references.png)

   A list of reference types is shown:

   ![References view](/help/sites-cloud/authoring/assets/references-list.png)

1. Select the required type of reference to show more details and (when appropriate) take further actions.

### Creating a Version of Your Page {#creating-a-version-of-your-page}

To create a [version](/help/sites-cloud/authoring/features/page-versions.md) of your page:

1. To open the Timeline rail, select **[Timeline](/help/sites-cloud/authoring/getting-started/basic-handling.md#timeline)** using the toolbar icon (either before or after [selecting your page](#selecting-your-page-for-further-action)):

   ![Timeline view option](/help/sites-cloud/authoring/assets/timeline.png)

1. Select the ellipsis at the bottom right of the Timeline column to reveal extra buttons, including **Save as Version**.

   ![Timeline view](/help/sites-cloud/authoring/assets/timeline-view.png)

1. Select **Save as Version**, then **Create**.

### Restoring/Comparing a Version of Your Page {#restoring-comparing-a-version-of-your-page}

The same basic mechanism is used when restoring and/or comparing versions of your page:

1. Select **[Timeline](/help/sites-cloud/authoring/getting-started/basic-handling.md#timeline)** using the toolbar icon (either before or after [selecting your page](#selecting-your-page-for-further-action)):

   ![Timeline view option](/help/sites-cloud/authoring/assets/timeline.png)

   If a version of your page has already been saved, it is listed in the Timeline.

1. Select the version you want to restore - this will reveal additional action buttons:

    * **Revert to this Version**

        * The version is restored.

    * **Show Differences**

        * The page is opened with differences (between the two versions) highlighted.

## References {#references}

**References** shows connections to the selected page:

* Blueprints
* Launches
* Live copies
* Language copies
* Incoming Links
* Use of the reference component: borrowed and lent content

Open the required console, then navigate to the required resource and open **References** using:

![References option](/help/sites-cloud/authoring/assets/references.png)

[Select your required resource](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources) to show a list of references types relevant to that resource:

![References details](/help/sites-cloud/authoring/assets/references-detail.png)

Select the appropriate reference type for more information. In certain situations further actions are available when you select a specific reference, including:

* **Incoming Links**, provides a list of pages that reference the page, together with direct access to **Edit** one of those pages when you select a specific link.

  * This can only show static links, not dynamically generated links; for example, from the List component.

* Instances of borrowed and lent content using the **Reference** component, from here you can navigate to the referencing/referenced page
* [Launches](/help/sites-cloud/authoring/launches/overview.md), provides access to related launches
* [Live Copies](/help/sites-cloud/administering/msm/overview.md) displays the paths of all live copies that are based on the selected resource.
* [Blueprint](/help/sites-cloud/administering/msm/best-practices.md), provides details and various actions
* [Languages Copies](/help/sites-cloud/administering/translation/managing-projects.md#creating-translation-projects-using-the-references-panel), provides details and various actions

## Events - Timeline {#events-timeline}

For appropriate resources (for example, pages from the **Sites** console, or assets from the **Assets** console) the [timeline can be used to show the recent activity on any selected items](/help/sites-cloud/authoring/getting-started/basic-handling.md#timeline).

Open the required console, then navigate to the required resource and open **Timeline**, using:

![Timeline option](/help/sites-cloud/authoring/assets/timeline.png)

[Select your required resource](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources), then either **Show All** or **Activities** to list any recent actions on the selected resources:

![Timeline details](/help/sites-cloud/authoring/assets/timeline-detail.png)
