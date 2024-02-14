---
title: The Sites Console
description: Learn how to use the Sites console to manage and organize your AEM pages.
---

# The Sites Console {#sites-console}

Learn how to use the Sites console to manage and organize your AEM pages.

## Orientation {#sites-console}

The Sites console allows you to view your page hierarchy. 

![Column view of the Sites console with an item selected](assets/sites-console-column-view-selected.png)

It offers different views and toolbars to help you manage and organize your pages.

* [The console toolbar](#toolbar) is always present to help you navigate.
* [Three different views](#views) allow you to easily locate and select your page.
* [The action toolbar](#action-toolbar) appears when you have selected an item to take action on it.
* [The side panel](#side-panel) has multiple options to show detailed information on a selected page.

## Console Toolbar {#console-toolbar}

The console toolbar is always present on the console and helps you orient yourself in your content and to navigate the content.

![The toolbar of the Sites console](assets/sites-console-toolbar.png)

### Side Panel Selector {#side-panel-selector}

The side panel selector allow you to show additional information about the selected item in the console.

![Side panel selector button](/help/sites-cloud/authoring/assets/rail-selector.png)

The options presented depend on your current console. For example, in **Sites** you can select content only (the default), the timeline, references, or filter side panel.

![Example of side panel selector](/help/sites-cloud/authoring/assets/rail-selector-example.png)

### Breadcrumbs {#breadcrumbs}

Situated in the middle of the rail, and always showing the description of the currently selected item, the breadcrumbs allow you to navigate through the levels of your website.

![Breadcrumbs in navigation bar](/help/sites-cloud/authoring/assets/breadcrumbs-navigation.png)


Click the breadcrumb text to display a drop-down listing the levels of the hierarchy of the currently selected item. Click an entry to jump to that location.

![Example of breadcrumbs expanded](/help/sites-cloud/authoring/assets/breadcrumbs-example.png)

### Select All {#select-all}

Tapping or clicking the **Select All** button selects all of the items in your current view of the console.

![Select all button](assets/sites-console-select-all.png)

When you have selected all items, the count of the items selected is displayed at the top-right of the toolbar where the **Select All** button appeared.

You can deselect all items and exit selection mode by:

* Clicking or tapping the **X** next to the count.
* Using the **escape** key.

![Deselect all](/help/sites-cloud/authoring/assets/deselect-all.png)

### Create Button {#create-button}

The **Create** button allows you to add new pages to your site as well as create additional Sites objects such as Live Copies or Launches.

![Create button](/help/sites-cloud/authoring/assets/create.png)

Once clicked, the options displayed are appropriate to the console/context.

## Views and Selecting Pages {#views}

The Sites console offers three different views of your content hierarchy. You can view, navigate through, and select (for further action) your resources with any of the available views.

* [Column View](#column-view)
* [Card View](#card-view)
* [List View](#list-view)

The **View** icon at the far right of the AEM toolbar indicates the current view selected.

Tapping or clicking it allows you to select a different view.

![Views button](/help/sites-cloud/authoring/assets/views-button.png)

You can switch between column view, card view, and list view. In the list view it also shows the view settings.

![Views](/help/sites-cloud/authoring/assets/view.png)

>[!NOTE]
>
>The **View Settings** option is only available when in **List View** mode.

Viewing, navigating, and selecting are each conceptually the same across all views, but have small variations in handling, dependent on the view you are using.

>[!NOTE]
>
>By default, AEM Assets does not display the original renditions of assets in the UI as thumbnails in any of the views. If you are an administrator, you can use overlays to configure AEM Assets to display original renditions as thumbnails.

### Selecting Resources {#selecting-resources}

Selecting a specific resource is dependent on a combination of the view and the device:

|View|Select Touch|Select Desktop|Deselect Touch|Deselect Desktop|
|---|---|---|---|---|
|Column|Select the thumbnail|Click the thumbnail|Select the thumbnail|Click the thumbnail|
|Card|Select and hold the card|Mouse over then use the check mark quick action|Select the card|Click the card|
|List|Select the thumbnail|Click the thumbnail|Select the thumbnail|Click the thumbnail|

#### Selecting Example {#selecting-example}

1. For example, in card view:

   ![Card view select](/help/sites-cloud/authoring/assets/card-view-select.png)

1. Once you have selected a resource the top header is covered by the [actions toolbar](#actions-toolbar) that provides access to actions currently applicable to the selected resource.

1. To exit selection mode select the **X** to the top-right, or use **escape**.

### Column View {#column-view}

The column view allows for visual navigation of a content tree through a series of cascading columns. This view lets you visualize and traverse the tree structure of your website.

![Column view](/help/sites-cloud/authoring/assets/column-view.png)

Selecting a resource in the leftmost column will display the child resources in a column to the right. Selecting a resource in the right column will then display the child resources in another column to the right and so on.

* You can navigate up and down in the tree by tapping or clicking on the resource name or the chevron to the right of the resource name.

  * The resource name and chevron are highlighted when tapped or clicked.
  * The children of the clicked/tapped resource are displayed in the column to the right of the clicked/tapped resource.
  * If you select a resource name that has no children, its details are displayed in the final column.

* Tapping or clicking on the thumbnail selects the resource.

  * When selected, a check mark is overlaid on the thumbnail and the resource name is highlighted as well.
  * The details of the selected resource are shown in the final column.
  * The action toolbar becomes available.

* When a page is selected in column view, the selected page is displayed in the final colum along with the following details:

  * Page title
  * Page name (part of the page's URL)
  * Template the page is based on
  * Modification details
  * Page language
  * Publication, and Preview details

### Card View {#card-view}

In card view, each item at the current level in the hierarchy is displayed as a large card.

![Card view](/help/sites-cloud/authoring/assets/card-view.png)

* Cards provide information such as:

  * A visual representation of the page content.
  * The page title.
  * Important dates (such as last edited, last published).
  * If the page is locked, hidden, or part of a livecopy.
  * Indicators if you are required to act on the item as part of a workflow.

Card view also offers [quick actions](#quick-actions) for the items such as selection and common actions such as edit.

![Quick actions](/help/sites-cloud/authoring/assets/quick-actions.png)

You can navigate down the tree by tapping/clicking on cards (taking care to avoid tapping the quick actions) or up again by using the [breadcrumbs in the header](#the-header).

### List View {#list-view}

List view provides information for each resource at the current level in a list.

![List view](/help/sites-cloud/authoring/assets/list-view.png)

* You can navigate down through the tree by tapping/clicking on the resource name and back up by using the [breadcrumbs in the header](#the-header).
* To easily select all items in the list, use the [**Select All** checkbox in the toolbar.](#select-all)

* Select the columns to be shown using **View Settings** option located under the Views button. The following columns are available for display:

  * **Name** - Page name, which can be useful in a multilingual authoring environment since it is part of the page's URL and does not change regardless of language
  * **Modified** - Last modified date and last modified by user
  * **Published** - Publication status
  * **Preview** - Preview status
  * **Template** - Template on which the page is based
  * **Operation**
  * **Workflow** - Workflow currently applied to the page. More information is available when you mouse over, or open Timeline.
  * **Translated**
  * **Page Views**
  * **Unique Visitors**
  * **Time on Page**

![Select columns](/help/sites-cloud/authoring/assets/select-columns.png)

By default the **Name** column is shown, which makes up part of the URL for the page. In some cases the author might need to access pages that are in a different language and seeing the name of the page (which is usually unchanging) can be of great help if the author does not know the language of the page.

* Change the order of items using the dotted vertical bar at the far right of each item in the list.

![Column order](/help/sites-cloud/authoring/assets/column-order.png)

Select the vertical selection bar and drag the item to a new position in the list.

![Order list](/help/sites-cloud/authoring/assets/order-list.png)

>[!NOTE]
>
>Changing the order works only within an ordered folder that has `jcr:primaryType` value as `sling:OrderedFolder`.

## Actions Toolbar {#actions-toolbar}

Whenever a resource is selected, various actions are indicated by icons with explanatory text in the toolbar. These actions are dependent on:

* The current context
* Whether you are in [selection mode](#viewing-and-selecting-resources)

The action available in the toolbar change to reflect the actions you can take on the specific items selected and how you [select a resource](#viewing-and-selecting-resources) depends on the view.

Due to the space restrictions in some windows, the toolbar can quickly become longer than the space available. When this happens additional options appears. Clicking or tapping on the ellipsis (the three dots or **...**) opens a drop-down selector holding all remaining actions.

![Additional options](/help/sites-cloud/authoring/assets/additional-options.png)

>[!NOTE]
>
>The individual icons available are documented in relation to the appropriate console/feature/scenario.

* Keyboard navigation 

  You can navigate a website using only the keyboard. This uses the standard browser functionality of the **TAB** key (or **OPT+TAB**) to move you between elements on the page that are focusable .

  In the **Sites** console there is the added option to **Skip to main content**. This becomes visible as you tab through the header options, and speeds your navigation by allowing you to skip the standard elements in the (product) toolbar and taking you directly to the main content.

  ![Skip to main content](/help/sites-cloud/authoring/assets/skip-to-main-content.png)


## Locking and Unlocking a Page {#locking-unlocking}

AEM lets you lock a page so that no one else can edit the contents. Locking is useful when you are making numerous edits to one specific page or when you need to freeze a page for a short while.

1. Select the page with [selection mode](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources).
1. Select the lock icon.

   ![Lock button](/help/sites-cloud/authoring/assets/lock.png)

Once locked, the lock icon in the console toolbar is updated to an unlock icon.

Unlocking a page is very similar to locking the page. Once the page is locked, the lock options are replaced by unlock actions.

The Page Information menu lists **Unlock** as an option and the Lock icon in the sites console is replaced by an **Unlock** icon.

![Unlock button](/help/sites-cloud/authoring/assets/unlock.png)

>[!CAUTION]
>
>* Locking a page can be performed when impersonating a user. However a page locked in this way can only then be unlocked (by customers) using the user who was impersonated.
>* Pages cannot be unlocked by impersonating the user who locked the page.
>* If the user who locked the page is not available to unlock the page, contact Customer Support to evaluate options to remove the lock. 

## Templates

You can easily see which template the page is based on when selecting the page in either [Column view](/help/sites-cloud/authoring/getting-started/basic-handling.md#column-view) or [List view](/help/sites-cloud/authoring/getting-started/basic-handling.md#list-view).
