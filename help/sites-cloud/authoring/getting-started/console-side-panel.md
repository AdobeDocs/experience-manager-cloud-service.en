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
* [Site](#site)
* [Filter](#filter)
* [Setup Analytics](#setup-analytics)

![Side panel views of the Sites console](assets/sites-console-side-panel-views.png)

The current view selected is indicated by a blue checkmark in the drop-down and the icon is updated with the name of the selected view.

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

The timeline can be used to view events that have affected the selected resource. You can also use it to start certain events such as workflows or versions.

![Timeline details](/help/sites-cloud/authoring/assets/timeline-detail.png)

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

In the Sites console you can also access additional features via the ellipsis button next to the **Comment** field.

* [Save a version](/help/sites-cloud/authoring/features/page-versions.md)
* [Start a workflow](/help/sites-cloud/authoring/workflows/applying.md)

![Sites console comment field](assets/sites-console-comment-ellipsis.png)

### Accessing Page References {#accessing-page-references}

[Quick access to references](/help/sites-cloud/authoring/getting-started/console-side-panel.md#references) to/from a page are available in the References Rail.

1. Select **References** using the toolbar icon (either before or after [selecting your page](#selecting-your-page-for-further-action)):

1. A list of reference types is shown:

   ![References view](/help/sites-cloud/authoring/assets/references-list.png)

1. Select the required type of reference to show more details and (when appropriate) take further actions.

## References {#references}

**References** shows connections to the selected page:

* Blueprints
* Launches
* Live copies
* Language copies
* Incoming Links
* Use of the reference component: borrowed and lent content

Open the Sites console, then navigate to the required resource and open **References** in the side panel.

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

## Site {#site}

**Site** shows details of sites [created using a site template](/help/sites-cloud/administering/site-creation/create-site.md).

![Site rail](../assets/site-rail.png)

See the document [Using the Site Rail to Manage Your Site Theme](/help/sites-cloud/administering/site-creation/site-rail.md) for more details on how you can use the rail to manage the [theme of your site](/help/sites-cloud/administering/site-creation/site-themes.md).

If you have not yet set up the front-end pipeline to enable theme-based site creation, the side panel will offer that option.

![Option to enable front-end pipeline in side panel](assets/sites-console-side-panel-site.png)

>[!TIP]
>
>An end-to-end description of the process of creating a site from a template and customizing its theme can be found in the [Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md).

## Filter {#filter}

This opens a panel similar to [search](/help/sites-cloud/authoring/getting-started/search.md) with the appropriate location filters already set, allowing you to further filter the content you want to view.

![Filter example](/help/sites-cloud/authoring/assets/filter.png)

Unlike other views of the side panel, to switch to another view either tap or click the `X` in the search field.

## Setup Analytics {#setup-analytics}

This view allows you to quickly set up Adobe Analytics for a selected site.

![Setup Analytics](assets/sites-console-side-panel-setup-analytics.png)
