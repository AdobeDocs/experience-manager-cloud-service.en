---
title: Quick Start Guide to Authoring Pages
description: A quick, high-level guide to get you started authoring page content
exl-id: d37c9b61-7382-4bf6-8b90-59726b871264
---
# Quick Start Guide to Authoring Pages {#quick-guide-to-authoring-pages}

This document is intended as a high-level quick start guide for the key page authoring actions in AEM. This document:

* Is not intended as comprehensive coverage.
* Provides links to the detailed documentation.

For full details about authoring with AEM see:

* [Concepts of Authoring](/help/sites-cloud/authoring/getting-started/concepts.md)
* [Basic Handling](/help/sites-cloud/authoring/getting-started/basic-handling.md)

## A Few Quick Hints {#a-few-quick-hints}

Before beginning the quick start guide, here is a small collection of general tips and hints that you should bear in mind, divided between areas of the authoring system.

### In the Sites Console {#sites-console}

* Create Button

  * This button is available in many consoles - the options presented are context sensitive so can vary according to the scenario.

* Re-ordering Pages

  * This can be done in [List View](/help/sites-cloud/authoring/getting-started/basic-handling.md#list-view). The changes will be applied and be visible in other views.

### Page Authoring {#page-authoring}

* Navigating Links

  * **Links are not available for navigation** when you are in **Edit** mode. To navigate with links you need to [preview the page](/help/sites-cloud/authoring/fundamentals/editing-content.md#previewing-pages) using either:

    * [Preview Mode](/help/sites-cloud/authoring/fundamentals/editing-content.md#preview-mode)
    * [View as Published](/help/sites-cloud/authoring/fundamentals/editing-content.md#view-as-published)

* Versions are not started/created from the page editor. This is now done from the **Sites** console (via either **Create** or [Timeline](/help/sites-cloud/authoring/getting-started/basic-handling.md#timeline) for a selected resource).

>[!NOTE]
>
>There are a number of keyboard shortcuts that can make the authoring experience easier.
>
>* [Keyboard Shortcuts When Editing Pages](/help/sites-cloud/authoring/fundamentals/keyboard-shortcuts.md)
>* [Keyboard Shortcuts for Consoles](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md)  

### Finding Your Page {#finding-your-page}

There are various aspects to finding a page; you can navigate and/or search:

1. Open the **Sites** console (using the **Sites** option in the [Global Navigation](/help/sites-cloud/authoring/getting-started/basic-handling.md#global-navigation) - this is triggered (drop down) when you select the Adobe Experience Manager link (top left).  

1. Navigate down the tree by tapping/clicking on the appropriate page. How the page resources are represented depends on the view you are using - [Card, List, or Column](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources):

   ![View selection drop-down](/help/sites-cloud/authoring/assets/views.png)

1. Navigate up the tree using [the breadcrumb in the header](/help/sites-cloud/authoring/getting-started/basic-handling.md#the-header), which allows you to return to the selected location:

   ![Breadcrumb dropdown](/help/sites-cloud/authoring/assets/breadcrumb.png)

1. You can also [Search](/help/sites-cloud/authoring/getting-started/search.md) for a page. You can select your page from the results shown.

   ![Search field](/help/sites-cloud/authoring/assets/search.png)

### Creating a New Page {#creating-a-new-page}

To [create a new page](/help/sites-cloud/authoring/fundamentals/organizing-pages.md#creating-a-new-page):

1. [Navigate to the location](#finding-your-page) where you want to create the new page.
1. Use the **Create** icon and then select **Page** from the list:

   ![Create button](/help/sites-cloud/authoring/assets/create.png)

1. This opens the wizard that will guide you through collecting the information needed when [creating your new page](/help/sites-cloud/authoring/fundamentals/organizing-pages.md#creating-a-new-page). Follow the on screen instructions.

### Selecting Your Page for Further Action {#selecting-your-page-for-further-action}

You can select a page so that you can take action on it. Selecting a page will automatically update the toolbar so that the actions relevant to that resource are shown.

How to select a page depends on which view you are using in the console:

1. Column View:

    * Tap/click on the thumbnail for the required resource - the thumbnail will be overlaid with a tick to show that it has been selected.

1. List View:

    * Tap/click on the thumbnail for the required resource - the thumbnail will be overlaid with a tick to show that it has been selected.

1. Card View:

    * Enter selection mode by [selecting the required resource](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources). How you do this depends on your device:

        * On a mobile device: tap-and-hold the card
        * On a desktop device: use the [quick action](/help/sites-cloud/authoring/getting-started/basic-handling.md#quick-actions) represented by the tick icon:

    * The card will be overlaid with a tick to show that the page has been selected.

    ![Example card](/help/sites-cloud/authoring/assets/card.png)

### Quick Actions (Card View/Desktop Only) {#quick-actions-card-view-desktop-only}

[Quick actions](/help/sites-cloud/authoring/getting-started/basic-handling.md#quick-actions) are available:

1. [Navigate to the page](#finding-your-page) you want to take action on.
1. Hover your mouse pointer over the card that represents your required resource. The quick actions will be shown:

   ![Card actions](/help/sites-cloud/authoring/assets/card-actions.png)

### Editing Your Page Content {#editing-your-page-content}

To edit your page:

1. [Navigate to the page](#finding-your-page) you want to edit.
1. [Open your page for editing](/help/sites-cloud/authoring/fundamentals/organizing-pages.md#opening-a-page-for-editing) using the Edit (pencil) icon:

   ![Edit button](/help/sites-cloud/authoring/assets/edit.png)

   This can be accessed from either:

    * [Quick Actions (card view/desktop only)](#quick-actions-card-view-desktop-only) for the appropriate resource.
    * The toolbar when your [page has been selected](#selecting-your-page-for-further-action).

1. When the editor opens you can:

    * [Add a new component to your page](/help/sites-cloud/authoring/fundamentals/editing-content.md#inserting-a-component) by:

        * Opening the side panel
        * Selecting the components tab (the [components browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#components-browser))
        * Dragging the required component onto your page.

      The side panel can be opened (and closed) with:

        ![Side panel toggle button](/help/sites-cloud/authoring/assets/side-panel-toggle.png)

    * [Edit the content of an existing component](/help/sites-cloud/authoring/fundamentals/editing-content.md#component-toolbar) on the page:

        * Open the component toolbar with either tap or click. Use the **Edit** (pencil) icon to open the dialog.
        * Open the in place editor for the component with either tap-and-hold or a double-slow-click. The available actions will be shown (for some components, this will be a limited selection).
        * To see all actions available enter full-screen mode using:

          ![Full screen button](/help/sites-cloud/authoring/assets/full-screen.png)

    * [Configure the properties of an existing component](/help/sites-cloud/authoring/fundamentals/editing-content.md#component-edit-dialog)

        * Open the component toolbar with either tap or click. Use the **Configure** (wrench) icon to open the dialog.

    * [Move a component](/help/sites-cloud/authoring/fundamentals/editing-content.md#moving-a-component) either:

        * Drag the required component to its new location.
        * Open the component toolbar with either tap or click. Use the **Cut** then **Paste** icons where required.

    * [Copy (and Paste)](/help/sites-cloud/authoring/fundamentals/editing-content.md#component-toolbar) a component:

        * Open the component toolbar with either tap or click. Use the **Copy** then **Paste** icons as required.

   >[!NOTE]
   >
   >You can **Paste** components to either the same page, or a different page. If pasting to a different page that was already open before the cut/copy operation, then that page will need a page refresh.

    * [Delete](/help/sites-cloud/authoring/fundamentals/editing-content.md#component-toolbar) a component:

        * Open the component toolbar with either tap or click, then use the **Delete** icon.

    * [Add annotations](/help/sites-cloud/authoring/fundamentals/annotations.md#annotations) to the page:

        * Select the **Annotate** mode (speech bubble icon). Add annotations using the **Add annotation** (plus) icon. Exit annotation mode using the X at top right.

          ![Annotations button](/help/sites-cloud/authoring/assets/annotations.png)

    * [Preview a page](/help/sites-cloud/authoring/fundamentals/editing-content.md#preview-mode) (to see how it will appear in the publish environment)

        * Select **Preview** from the toolbar.

    * Return to edit mode (or select another mode) using the **Edit** drop down selector.

   >[!NOTE]
   >
   >To navigate using links in the content you must use [Preview mode](/help/sites-cloud/authoring/fundamentals/editing-content.md#preview-mode).

### Editing the Page Properties {#editing-the-page-properties}

There are two (main) methods of [editing page properties](/help/sites-cloud/authoring/fundamentals/page-properties.md):

* From the **Sites** console:

    1. [Navigate to the page](#finding-your-page) you want to publish.
    1. Select the **Properties** icon from either:

        * [Quick Actions (Card View/Desktop Only)](#quick-actions-card-view-desktop-only) for the appropriate resource.
        * The toolbar when your [page has been selected](#selecting-your-page-for-further-action).

        ![Properties button](/help/sites-cloud/authoring/assets/properties.png)

    1. The page properties will be shown. You can make updates as required, then use Save to persist these

* When [editing your page](#editing-your-page-content):

    1. Open the **Page Information** menu.
    1. Select **Open Properties** to open the dialog for editing the properties.

        ![Page Information button](/help/sites-cloud/authoring/assets/page-information.png)

### Publishing Your Page (or Unpublishing) {#publishing-your-page-or-unpublishing}

There are two main methods of [publishing your page](/help/sites-cloud/authoring/fundamentals/publishing-pages.md) (and also of unpublishing):

* From the **Sites** console:

    1. [Navigate to the page](#finding-your-page) you want to publish.
    1. Select the **Quick Publish** icon from either:

        * [Quick Actions (Card View/Desktop Only)](#quick-actions-card-view-desktop-only) for the appropriate resource.
        * The toolbar when your [page has been selected](#selecting-your-page-for-further-action) (also gives access to [Publish Later](/help/sites-cloud/authoring/fundamentals/publishing-pages.md)).

        ![Quick Publish button](/help/sites-cloud/authoring/assets/quick-publish.png)

* When [editing your page](#editing-your-page-content):

    1. Open the **Page Information** menu.
    1. Select **Publish Page**.

* Unpublishing a page from the console can only be done via the **Manage Publication** option, which is only available on the toolbar (not via the quick actions).

    ![Manage Publication button](/help/sites-cloud/authoring/assets/manage-publication.png)

  The **Unpublish Page** option is still available via the **Page Information** menu in the editor.

  See [Publishing Pages](/help/sites-cloud/authoring/fundamentals/publishing-pages.md#unpublishing-pages) for more information.

### Move, Copy and Paste, or Delete Your Page {#move-copy-and-paste-or-delete-your-page}

These actions can all be triggered by:

1. [Navigate to the page](#finding-your-page) you want to move, copy and paste, or delete.
1. Select the copy (and then paste), move or delete icon as required using either:

    * [Quick Actions (Card View/Desktop Only)](#quick-actions-card-view-desktop-only) for the required resource.
    * The toolbar when your [page has been selected](#selecting-your-page-for-further-action).

   Then, dependent on your action:

    * Copy:

        * You will then need to navigate to the new location and paste.

    * Move:

        * The wizard will open to collect the information needed to move the page. Follow the on-screen instructions.

    * Delete:

        * You will be asked to confirm the action.

   >[!NOTE]
   >
   >Delete is not available as a Quick Action.

### Locking Your Page (then Unlocking) {#locking-your-page-then-unlocking}

[Locking a page](/help/sites-cloud/authoring/fundamentals/editing-content.md#locking-a-page) prevents other authors from working on it while you are. The Lock (and Unlock) icon/button can be found:

* The toolbar when your [page has been selected](#selecting-your-page-for-further-action).
* The [Page Information drop down menu](#editing-the-page-properties) when editing a page.
* The page toolbar when editing a page (when the page is locked)

For example, the lock icon looks like this:

![Lock button](/help/sites-cloud/authoring/assets/lock.png)

### Accessing Page References {#accessing-page-references}

[Quick access to references](/help/sites-cloud/authoring/fundamentals/environment-tools.md#references) to/from a page are available in the References Rail.

1. Select **References** using the toolbar icon (either before or after [selecting your page](#selecting-your-page-for-further-action)):

   ![References view option](/help/sites-cloud/authoring/assets/references.png)

   A list of reference types is shown:

   ![References view](/help/sites-cloud/authoring/assets/references-list.png)

1. Tap/click on the required type of reference to show more details and (when appropriate) take further actions.

### Creating a Version of Your Page {#creating-a-version-of-your-page}

To create a [version](/help/sites-cloud/authoring/features/page-versions.md) of your page:

1. To open the Timeline rail, select **[Timeline](/help/sites-cloud/authoring/getting-started/basic-handling.md#timeline)** using the toolbar icon (either before or after [selecting your page](#selecting-your-page-for-further-action)):

   ![Timeline view option](/help/sites-cloud/authoring/assets/timeline.png)

1. Tap/click on the ellipsis at the bottom right of the Timeline column to reveal extra buttons, including **Save as Version**.

   ![Timeline view](/help/sites-cloud/authoring/assets/timeline-view.png)

1. Select **Save as Version**, then **Create**.

### Restoring/Comparing a Version of Your Page {#restoring-comparing-a-version-of-your-page}

The same basic mechanism is used when restoring and/or comparing versions of your page:

1. Select **[Timeline](/help/sites-cloud/authoring/getting-started/basic-handling.md#timeline)** using the toolbar icon (either before or after [selecting your page](#selecting-your-page-for-further-action)):

   ![Timeline view option](/help/sites-cloud/authoring/assets/timeline.png)

   If a version of your page has already been saved, this will be listed in the Timeline.

1. Tap/click on the version you want to restore - this will reveal additional action buttons:

    * **Revert to this Version**

        * The version will be restored.

    * **Show Differences**

        * The page will be opened with differences (between the two versions) highlighted.
