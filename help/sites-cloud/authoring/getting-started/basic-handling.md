---
title: Basic Handling
description: Get comfortable with navigating AEM and its basic usage
---

# Basic Handling {#basic-handling}

This document is designed to give an overview of basic handling when using the AEM author environment. It uses the **Sites** console as a basis.

>[!NOTE]
>
>* Some functionality is not available in all consoles and additional functionality may be available in some consoles. Specific information about the individual consoles and their related functionality will be covered in more detail on other pages.
>* Keyboard shortcuts are available throughout AEM. In particular when [using consoles](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) and [editing pages](/help/sites-cloud/authoring/fundamentals/keyboard-shortcuts.md).

## A Touch-Enabled UI {#a-touch-enabled-ui}

AEM's user interface is enabled for touch. A touch-enabled interface allows you to use touch to interact with the software through gestures such as tap, touch-and-hold, and swipe. Because the AEM UI is touch-enabled, you can use the touch gestures on your touch devices such as your mobile phone or tablet. However mouse actions on a traditional desktop device are also available, giving you flexibility in how you choose to author your content.

## First Steps {#first-steps}

Immediately after logging in you arrive on the [Navigation panel](#navigation-panel). Selecting one of the options opens the respective console.

![Navigation panel](/help/sites-cloud/authoring/assets/navigation.png)

To get a good understanding of the basic use of AEM, this document is based on the **Sites** console. Click or tap on **Sites** to get started.

## Product Navigation {#product-navigation}

Whenever a user first accesses a console, a product navigation tutorial is started. Take a minute to click or tap through to get a good overview of the basic handling of AEM.

![Navigation tutorial](/help/sites-cloud/authoring/assets/tutorial.png)

Click or tap **Next** to advance to the next page of the overview. Click or tap **Close** or click or tap outside of the overview dialog to close.

The overview will restart the next time you access a console unless you either view all slides or check the option **Don't show this again**.

## Global Navigation {#global-navigation}

You can navigate between the consoles using the global navigation panel. This is triggered as a full-screen drop down when you click or tap the Adobe Experience Manager link at the top-left of the screen.

You can close the global navigation panel by clicking or tapping **Close** to return to your previous location.

![Navigation panel top bar](/help/sites-cloud/authoring/assets/navigation-bar.png)

Global navigation has two panels, represented by icons at the left-margin of the screen:

* **[Navigation](#navigation-panel)** - Represented by a compass and the default panel when you log in to AEM
* **[Tools](#tools-panel)** - Represented by a hammer

The options available on these panels are described below.

### Navigation Panel {#navigation-panel}

The Navigation panel:

![Navigation panel](/help/sites-cloud/authoring/assets/navigation.png)

The title of the browser tab will update to reflect your location as you navigate through the consoles and content.

From Navigation the consoles available are:

|Console|Purpose|
|---|---|
|Projects|The Projects console gives you direct access to your projects. [Projects are virtual dashboards](/help/sites-cloud/authoring/projects/overview.md) that can be used to build a team. You can then give that team access to resources, workflows, and tasks, thus allowing people to work towards a common goal.|
|Sites|The Sites consoles let you [create, view, and manage sites](/help/sites-cloud/authoring/fundamentals/organizing-pages.md) running on your AEM instance. Through this console you can create, edit, copy, move, and delete pages, start workflows, and publish pages.|
|Experience Fragments|An [Experience Fragment](/help/sites-cloud/authoring/fundamentals/experience-fragments.md) is a stand-alone experience that can be re-used across channels and have variations, saving the trouble of repeatedly copying and pasting experiences or parts of experiences.|
|Assets|The Assets console lets you import and manage digital assets such as images, videos, documents, and audio files. These assets can then be used by any site running on the same AEM instance.<!--add some kind of assets link-->|
|Personalization|This console provides a framework of tools for [authoring targeted content and presenting personalized experiences.](/help/sites-cloud/authoring/personalization/overview.md)|

## Tools Panel {#tools-panel}

In the Tools panel has a side panel containing a range of categories, that group together similar Tools consoles. The Tools consoles provide access to a number of specialized tools and consoles that help you administer your websites, digital assets, and other aspects of your content repository. <!--The [Tools consoles](/help/sites-administering/tools-consoles.md) provide access to a number of specialized tools and consoles that help you administer your websites, digital assets, and other aspects of your content repository.-->

![Tools panel](/help/sites-cloud/authoring/assets/tools-panel.png)

## The Header {#the-header}

The header is always present at the top of the screen. While most options in the header remain the same no matter where you are in the system, some are context-specific.

![Navigation header](/help/sites-cloud/authoring/assets/navigation-bar.png)

* [Global Navigation](#global-navigation)

  Select the **Adobe Experience Manager** link to navigate between consoles.

  ![Global navigation](/help/sites-cloud/authoring/assets/global-navigation.png)

* [Search](/help/sites-cloud/authoring/getting-started/search.md)

  ![Search icon](/help/sites-cloud/authoring/assets/search-icon.png)

  You can also use the [shortcut key](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) `/` (forward slash) to invoke search from any console.

* [Solutions](https://www.adobe.com/experience-cloud.html)

  ![Solutions button](/help/sites-cloud/authoring/assets/solutions.png)

* [Help](#accessing-help)

  ![Help button](/help/sites-cloud/authoring/assets/help.png)

* [Notifications](/help/sites-cloud/authoring/getting-started/inbox.md)

  ![Notifications button](/help/sites-cloud/authoring/assets/notifications.png)

  This icon will be badged with the number of currently assigned incomplete notifications.
  
* [User Properties](/help/sites-cloud/authoring/getting-started/account-environment.md)

  ![User Properties button](/help/sites-cloud/authoring/assets/user-properties.png)

* [Rail selector](#rail-selector)

  ![Rail selector button](/help/sites-cloud/authoring/assets/rail-selector.png)

  The options presented depend on your current console. For example, in **Sites** you can select content only (the default), the timeline, references, or filter side panel.

  ![Example of rail selector](/help/sites-cloud/authoring/assets/rail-selector-example.png)

* Breadcrumbs

  ![Breadcrumbs in navigation bar](/help/sites-cloud/authoring/assets/breadcrumbs-navigation.png)

  Situated in the middle of the rail, and always showing the description of the currently selected item, the breadcrumbs allow you to navigate within a specific console. In the **Sites** console, you can navigate through the levels of your website.

  Simply click on the breadcrumb text to display a drop-down listing the levels of the hierarchy of the currently selected item. Click on an entry to jump to that location.

  ![Example of breadcrumbs expanded](/help/sites-cloud/authoring/assets/breadcrumbs-example.png)

* **Create** button

  ![Create button](/help/sites-cloud/authoring/assets/create.png)

  Once clicked, the options displayed are appropriate to the console/context.

* [Views](#viewing-and-selecting-resources)

  The view icon is at the far right of the AEM toolbar. As it also indicates the current view, it changes. For example, in the default view, **Column View** it shows:

  ![Views button](/help/sites-cloud/authoring/assets/views-button.png)

  You can switch between column view, card view, and list view. In the list view it also shows the view settings.

  ![Views](/help/sites-cloud/authoring/assets/view.png)

  >[!NOTE]
  >
  >The **View Settings** option is only available when in **List View** mode.

* Keyboard navigation 

  You can navigate a website using only the keyboard. This uses the standard browser functionality of the **TAB** key (or **OPT+TAB**) to move you between elements on the page that are focusable .

  In the **Sites** console there is the added option to **Skip to main content**. This becomes visible as you tab through the header options, and speeds your navigation by allowing you to skip the standard elements in the (product) toolbar and taking you directly to the main content.

  ![Skip to main content](/help/sites-cloud/authoring/assets/skip-to-main-content.png)

## Accessing Help {#accessing-help}

There are various help resources available:

* **Console Toolbar**

  Depending on your location the **Help** icon will open the appropriate resources:

  ![Help icon](/help/sites-cloud/authoring/assets/help-console.png)

* **Navigation**

  The first time you navigate the system, [a series of slides introduce AEM navigation](#product-navigation).

  ![Tutorial](/help/sites-cloud/authoring/assets/tutorial.png)

* **Page Editor**

  The first time you edit a page a series of slides introduce the page editor.

  ![Editor tutorial](/help/sites-cloud/authoring/assets/editor-tutorial.png)

  Navigate this overview as you would the [product navigation overview](#product-navigation) when first accessing any console.

  From the [**Page Information** menu you can select **Help**](/help/sites-cloud/authoring/fundamentals/environment-tools.md#accessing-help) to show this again at any time.

* **Tools Console**

  From the **Tools** console you can also access the external **Resources**:

  * **Documentation** - View the Web Experience Management documentation
  * **Developer Resources** - Developer resources and downloads

  >[!NOTE]
  >
  >You can access an overview of shortcut keys available at any time using the hotkey `?` (question mark) when in a console.
  >
  >For an overview of all keyboard shortcuts see the following documentation:
  >
  >* [Keyboard shortcuts for editing pages](/help/sites-cloud/authoring/fundamentals/keyboard-shortcuts.md)
  >* [Keyboard shortcuts for consoles](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md)

## Actions Toolbar {#actions-toolbar}

Whenever a resource is selected (e.g. a page or an asset), various actions are indicated by icons with explanatory text in the toolbar. These actions are dependent on:

* The current console
* The current context
* Whether you are in [selection mode](#viewing-and-selecting-resources)

The action available in the toolbar change to reflect the actions you can take on the specific items selected.

How you [select a resource](#viewing-and-selecting-resources) depends on the view.

Due to the space restrictions in some windows, the toolbar can quickly become longer than the space available. When this happens additional options appears. Clicking or tapping on the ellipsis (the three dots or **...**) opens a drop down selector holding all remaining actions. For example, after selecting a page in the **Sites** console:

![Additional options](/help/sites-cloud/authoring/assets/additional-options.png)

>[!NOTE]
>
>The individual icons available are documented in relation to the appropriate console/feature/scenario.

## Quick Actions {#quick-actions}

In [Card View](#card-view) certain actions are available as quick action icons as well as being on the toolbar. Quick action icons are available for a single item at a time and eliminate the need for you to preselect.

The quick actions are visible when you mouseover (desktop device) a resource card. The quick actions available can depend on the console and context. For example, here are the quick actions for a page in the **Sites** console:

![Additional options](/help/sites-cloud/authoring/assets/quick-actions.png)

## Viewing and Selecting Resources {#viewing-and-selecting-resources}

Viewing, navigating, and selecting are each conceptually the same across all views, but have small variations in handling, dependent on the view you are using.

You can view, navigate through, and select (for further action) your resources with any of the available views, each of which can be selected by the icon at the top right:

* [Column View](#column-view)
* [Card View](#card-view)
* [List View](#list-view)

>[!NOTE]
>
>By default, AEM Assets does not display the original renditions of assets in the UI as thumbnails in any of the views. If you are an administrator, you can use overlays to configure AEM Assets to display original renditions as thumbnails.

### Selecting Resources {#selecting-resources}

Selecting a specific resource is dependent on a combination of the view and the device:

|View|Select Touch|Select Desktop|Deselect Touch|Deselect Desktop|
|---|---|---|---|---|
|Column|Tap the thumbnail|Click the thumbnail|Tap the thumbnail|Click the thumbnail|
|Card|Tap and hold the card|Mouse over then use the check mark quick action|Tap the card|Click the card|
|List|Tap the thumbnail|Click the thumbnail|Tap the thumbnail|Click the thumbnail|

#### Select All {#select-all}

You can select all items in any view by clicking the **Select All** option at the top-right corner of the console.

* In **Card View** all cards are selected.
* In **List View** all items in the list are selected.
* In **Column View** all items in the leftmost column are selected.

![Select all](/help/sites-cloud/authoring/assets/select-all.png)

#### Deselecting All {#deselecting-all}

In all cases as you select items, the count of the items selected is displayed at the top-right of the toolbar.

You can deselect all items and exit selection mode by:

* Clicking or tapping the **X** next to the count
* Using the **escape** key

![Deselect all](/help/sites-cloud/authoring/assets/deselect-all.png)

In all views, all items can be deselected by tapping escape on the keyboard if you are using a desktop device.

#### Selecting Example {#selecting-example}

1. For example in card view:

   ![Card view select](/help/sites-cloud/authoring/assets/card-view-select.png)

1. Once you have selected a resource the top header is covered by the [actions toolbar](#actions-toolbar) that provides access to actions currently applicable to the selected resource.

   To exit selection mode select the **X** to the top-right, or use **escape**.

### Column View {#column-view}

![Column view](/help/sites-cloud/authoring/assets/column-view.png)

The column view allows for a visual navigation of a content tree through a series of cascading columns. This view allows you to visualize and traverse the tree structure of your website.

Selecting a resource in the leftmost column will display the child resources in a column to the right. Selecting a resource in the right column will then display the child resources in another column to the right and so on.

* You can navigate up and down in the tree by tapping or clicking on the resource name or the chevron to the right of the resource name.

  * The resource name and chevron will be highlighted when tapped or clicked.
  * The children of the clicked/tapped resource are displayed in the column to the right of the clicked/tapped resource.
  * If you tap or click on a resource name that has no children, its details will be displayed in the final column.

* Tapping or clicking on the thumbnail selects the resource.

  * When selected, a check mark will be overlaid on the thumbnail and the resource name will be highlighted as well.
  * The details of the selected resource will be shown in the final column.
  * The action toolbar will become available.

  When a page is selected in column view, the selected page is displayed in the final colum along with the following details:

  * Page title
  * Page name (part of the page's URL)
  * Template the page is based on
  * Modification details
  * Page language
  * Publication details

### Card View {#card-view}

![Card view](/help/sites-cloud/authoring/assets/card-view.png)

* Card view displays information cards for each item at the current level. These provide information such as:

  * A visual representation of the page content
  * The page title
  * Important dates (such as last edited, last published)
  * If the page is locked, hidden or part of a livecopy
  * If appropriate, when you are required to take action as part of a workflow
    * Markers that indicate required actions may be related to entries in your [Inbox](/help/sites-cloud/authoring/getting-started/inbox.md).

* [Quick actions](#quick-actions) are also available in this view such as selection and common actions such as edit.

  ![Quick actions](/help/sites-cloud/authoring/assets/quick-actions.png)

* You can navigate down the tree by tapping/clicking on cards (taking care to avoid the quick actions) or up again by using the [breadcrumbs in the header](#the-header).

### List View {#list-view}

![List view](/help/sites-cloud/authoring/assets/list-view.png)

* The list view lists information for each resource at the current level.
* You can navigate down through the tree by tapping/clicking on the resource name and back up by using the [breadcrumbs in the header](#the-header).
* To easily select all items in the list, use the checkbox at the top-left of the list.

  ![List view select all](/help/sites-cloud/authoring/assets/list-view-select-all.png)

  * When all items in the list are selected, this checkbox appears checked.

    * Click or tap the checkbox to deselect all.

  * When only some items are selected, it appears with a minus sign.

    * Click or tap the checkbox to select all.
    * Click or tap the checkbox again to deselect all.

* Select the columns to be shown using **View Settings** option located under the Views button. The following columns are available for display:

  * **Name** - Page name, which can be useful in a multilingual authoring environment since it is part of the page's URL and does not change regardless of language
  * **Modified** - Last modified date and last modified by user
  * **Published** - Publication status
  * **Template** - Template on which the page is based
  * **Workflow** - Workflow currently applied to the page. More information is available when you mouseover, or open Timeline.
  * **Page analytics**
  * **Unique visitors**
  * **Time on page**

    ![Select columns](/help/sites-cloud/authoring/assets/select-columns.png)

  By default the **Name** column is shown, which makes up part of the URL for the page. In some cases the author might need to access pages that are in a different language and seeing the name of the page (which is usually unchanging) can be of great help if the author does not know the language of the page.

* Change the order of items using the dotted vertical bar at the far right of each item in the list.

  >[!NOTE]
  >
  >Changing the order works only within an ordered folder that has `jcr:primaryType` value as `sling:OrderedFolder`.

  ![Column order](/help/sites-cloud/authoring/assets/column-order.png)

  Click or tap on the vertical selection bar and drag the item to a new position in the list.

  ![Order list](/help/sites-cloud/authoring/assets/order-list.png)

## Rail Selector {#rail-selector}

The **Rail Selector** is available at the top-left of the window and displays options depending on your current consoles.

![Rail selector expanded](/help/sites-cloud/authoring/assets/rail-selector-expanded.png)

For example, in **Sites** you can select content only (the default), content tree, the timeline, references, or filter side panel.

If content only is selected, then only the rail icon appears. When any other option is selected, the option name appears next to the rail icon.

>[!NOTE]
>
>[Keyboard shortcuts](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) are available to quickly switch between rail display options.

### Content tree {#content-tree}

The content tree can be used to quickly navigate the site hierarchy within the side panel and view much information about the pages in the current folder.

Using the content tree side panel in conjunction with a list view or cards view, users can easily see the hierarchical structure of the project and navigate easily across the content structure with the content tree side-panel, as well as view detailed page information in the list view.

![Content tree](/help/sites-cloud/authoring/assets/content-tree.png)

>[!NOTE]
>
>Once an entry in the hierarchy view is selected, arrow keys can be used to quickly navigate the hierarchy.
>
>Refer to the [keyboard shortcuts](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) for more information.

### Timeline {#timeline}

The timeline can be used to view and/or initiate events that have occurred on the selected resource. To open the timeline column use the rail selector:

![Timeline tree](/help/sites-cloud/authoring/assets/timeline.png)

The timeline column allows you to:

* View various events related to a selected item.

  * The event types can be selected from the drop-down list:

    * Comments
    * [Annotations](/help/sites-cloud/authoring/fundamentals/annotations.md)
    * [Activities](/help/sites-cloud/authoring/personalization/activities.md)
    * [Launches](/help/sites-cloud/authoring/launches/overview.md)
    * [Versions](/help/sites-cloud/authoring/features/page-versions.md)
    * [Workflows](/help/sites-cloud/authoring/workflows/overview.md)
      * With the exception of transient workflows as no history information is saved for these <!--With the exception of [transient workflows](/help/sites-developing/workflows.md#transient-workflows) as no history information is saved for these-->
    * Show All

* Add/view comments about the selected item. The **Comment** box is shown at the bottom of the list of events. Typing a comment followed by Return will register the comment. It is shown when **Comments** or **Show All** is selected.

* Specific consoles have additional functionality. For example, in the Sites console you can:

  * [Save a version](/help/sites-cloud/authoring/features/page-versions.md)
  * [Start a workflow](/help/sites-cloud/authoring/workflows/applying.md)

These options accessible via the chevron next to the **Comment** field.

![Comment field](/help/sites-cloud/authoring/assets/comments.png)

### References {#references}

**References** shows any connections to the selected resource. For example, in the **Sites** console [references](/help/sites-cloud/authoring/fundamentals/environment-tools.md#references) for pages shows:

* [Launches](/help/sites-cloud/authoring/launches/overview.md#launches-in-references-sites-console)
* [Live copies](/help/sites-cloud/administering/msm/overview.md#openingthelivecopyoverviewfromreferences)
* [Language copies](/help/sites-cloud/administering/translation/preparation.md#seeing-the-status-of-language-roots)
* Content references:

  * Links from other pages to the selected page
  * Content borrowed from and/or lent to the selected page by the Reference component

![References example](/help/sites-cloud/authoring/assets/references-example.png)

### Filter {#filter}

This will open a panel similar to [search](/help/sites-cloud/authoring/getting-started/search.md) with the appropriate location filters already set, allowing you to further filter the content you wish to view.

![Filter example](/help/sites-cloud/authoring/assets/filter.png)
