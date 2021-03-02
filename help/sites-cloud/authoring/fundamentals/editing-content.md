---
title: Editing Page Content
description: Once your page is created you can edit the content to make the updates you require
---

# Editing Page Content{#editing-page-content}

Once your page is created (either new or as part of a launch or live copy) you can edit the content to make the updates you require.

Content is added using [components](/help/sites-cloud/authoring/features/components-console.md) (appropriate to the content type) that can be dragged onto the page. These can then be edited in place, moved, or deleted.

>[!NOTE]
>
>Your account needs the appropriate access rights and permissions to edit pages.
>
>If you encounter any problems we suggest you contact your system administrator.
<!--
>Your account needs the [appropriate access rights](/help/sites-administering/security.md) and [permissions](/help/sites-administering/security.md#permissions) to edit pages.
-->

>[!NOTE]
>
>If your page and/or template has been appropriately set up, then you can use [responsive layout](/help/sites-cloud/authoring/features/responsive-layout.md) when editing.

>[!TIP]
>
>When in **Edit** mode, links in your content are visible, but **not accessible**. Use [Preview mode](#previewing-pages) if you want to navigate using the links in your content.

## Page Toolbar {#page-toolbar}

The page toolbar offers access to the appropriate functionality, dependent on the page configuration.

![Page toolbar](/help/sites-cloud/authoring/assets/editing-page-toolbar.png)

The toolbar offers access to numerous options. Depending on your current context and configuration, some options may not be available.

* **Toggle Side Panel**

  This opens/closes the side panel, which holds the [Asset Browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#assets-browser), [Component Browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#components-browser), and [Content Tree](/help/sites-cloud/authoring/fundamentals/environment-tools.md#content-tree).

  ![Side Panel toggle](/help/sites-cloud/authoring/assets/side-panel-toggle.png)

* **Page Information**

  Provides access to the [Page Information](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-information) menu including page details and actions that can be taken on the page including viewing and editing page information, viewing page properties, and publishing/unpublishing the page.

  ![Page Information button](/help/sites-cloud/authoring/assets/page-information-icon.png)

* **Emulator**

  Toggles the [emulator toolbar](/help/sites-cloud/authoring/features/responsive-layout.md#selecting-a-device-to-emulate), which is used to emulate the look-and-feel of the page on another device. This is automatically toggled in layout mode.

  ![Emulator button](/help/sites-cloud/authoring/assets/emulator.png)

* **ContextHub**

  Opens the [ContextHub](/help/sites-cloud/authoring/personalization/contexthub.md). Only available in Preview mode.

  ![Context Hub button](/help/sites-cloud/authoring/assets/context-hub.png)

* **Page Title**

  This is purely informational.

  ![Page Title](/help/sites-cloud/authoring/assets/page-title.png)

* **Mode Selector**

  Displays the current [mode](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-modes) and allows you to select another mode such as edit, layout, timewarp, or targeting.

  ![Mode Selector button](/help/sites-cloud/authoring/assets/mode-selector.png)

* **Preview**

  Enables [preview mode](#preview-mode). This displays the page as it will appear when published.

  ![Preview button](/help/sites-cloud/authoring/assets/preview.png)

* **Annotate**

  Allows you to add [annotations](/help/sites-cloud/authoring/fundamentals/annotations.md) to the page when reviewing a page. After the first annotation, the icon will switch to a number indicating the number of annotations on the page.

  ![Annotation button](/help/sites-cloud/authoring/assets/annotations.png)

### Status Notification {#status-notification}

If a page is part of a [workflow](/help/sites-cloud/authoring/workflows/overview.md) or multiple workflows, this information is shown in a notification bar at the top of the screen when editing the page.

![Workflow notification](/help/sites-cloud/authoring/assets/editing-workflow-notification.png)

>[!NOTE]
>
>The status bar is only visible to user accounts with appropriate privileges.

The notification lists the workflow that is running against the page. If the user is involved in the current workflow step, options to [affect the workflow status](/help/sites-cloud/authoring/workflows/participating.md) and get more information about the workflow are also available such as:

* **Complete** - Opens the **Complete Work Item** dialog
* **Delegate** - Opens the **Complete Work Item** dialog
* **View details** - Opens the **Details** window of the workflow

Completing and delegating workflow steps via the notification bar works as it does when [participating in workflows](/help/sites-cloud/authoring/workflows/participating.md) from the Notification inbox.

If the page is subject to multiple workflows, the number of workflows is displayed at the right end of the notification along with arrow buttons to allow you to scroll through the workflows.

![Multiple workflow notifications](/help/sites-cloud/authoring/assets/editing-workflow-notification-multiple.png)

## Component Placeholder {#component-placeholder}

The component placeholder is an indicator to show where a component will be positioned when you drop it - above the component you are currently hovering over.

* When adding a new component to the page (dragging from the component browser):

  ![Placeholder when adding a new component to a page](/help/sites-cloud/authoring/assets/editing-component-placeholder.png)

* When moving an existing component:

  ![Placeholder when moving an existing component on a page](/help/sites-cloud/authoring/assets/editing-component-placeholder-existing.png)

## Inserting a Component {#inserting-a-component}

### Inserting a Component from the Components Browser {#inserting-a-component-from-the-components-browser}

You can add a new component by using the [component browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#components-browser). The [component placeholder](#component-placeholder) shows you where the component will be positioned:

1. Make sure that your page is in [**Edit** mode](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-modes).
1. Open the [component browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#components-browser).
1. Drag the required component to the [required position](#component-placeholder).
1. [Edit](#edit-content) the component.

>[!NOTE]
>
>On a mobile device, the component browser will fill the entire screen. Once you start dragging a component, the browser will close to show the page again so you can place the component.

### Inserting a Component from the Paragraph System {#inserting-a-component-from-the-paragraph-system}

You can add a new component by using the **Drag components here** box of the paragraph system:

1. Make sure that your page is in [**Edit** mode](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-modes).
1. There are two ways to select and add a new component from the paragraph system:

    * Select the **Insert Component** option (+) from either the toolbar of an existing component or the **Drag components here** box.

      ![Insert a component](/help/sites-cloud/authoring/assets/editing-insert-component.png)

    * If you are on a desktop device you can double-click on the **Drag components here** box.

    * The **Insert New Component** dialog will open to allow you to select your required component:

      ![Insert New Component dialog](/help/sites-cloud/authoring/assets/editing-insert-component-selection.png)

1. The selected component will be added to the bottom of the page. [Edit](#edit-content) the component as required.

### Inserting a Component using the Assets Browser {#inserting-a-component-using-the-assets-browser}

You can also add a new component to the page by dragging an asset from the [assets browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#assets-browser). This will automatically create a new component of the appropriate type (and containing the asset).

This behavior can be configured for your installation. See Configuring a Paragraph System so that Dragging an Asset Creates a Component Instance for further details. <!--This behavior can be configured for your installation. See [Configuring a Paragraph System so that Dragging an Asset Creates a Component Instance](/help/sites-developing/developing-components.md#configuring-a-paragraph-system-so-that-dragging-an-asset-creates-a-component-instance) for further details.-->

To create a component by dragging one of the above asset types:

1. Make sure that your page is in [**Edit** mode](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-modes).
1. Open the [asset browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#assets-browser).
1. Drag the required asset to the required position. The [component placeholder](#component-placeholder) shows you where the component will be positioned.

   A component, appropriate for the asset type, will be created at the required location - it will contain the selected asset.

1. [Edit](#edit-content) the component if required.

>[!NOTE]
>
>On a mobile device, the asset browser will fill the entire screen. Once you start dragging an asset, the browser will close to show the page again so you can place the asset.

If when browsing the assets you find that you need to make a quick change to an asset, you can start the [asset editor](/help/assets/manage-digital-assets.md) directly from the browser by clicking the edit icon next to the asset's name.

![Asset edit button](/help/sites-cloud/authoring/assets/asset-edit-button.png)

## Component Toolbar {#component-toolbar}

Selecting a component will open the toolbar. This provides access to various actions that can be performed on the component.

The actual actions available to the user will be shown as appropriate and not all actions may be described here.

![Component Toolbar](/help/sites-cloud/authoring/assets/editing-component-toolbar.png)

* **Edit**

  [Dependent on the component type](/help/sites-cloud/authoring/fundamentals/components.md) this will allow you to [edit the content of the component](#edit-content). Often a toolbar will be provided.

  ![Edit button](/help/sites-cloud/authoring/assets/editing-component-toolbar-edit.png)

* **Configure**

  [Dependent on the component type](/help/sites-cloud/authoring/fundamentals/components.md) this will allow you to edit and configure the properties of the component. Often a dialog will be opened.

  ![Configure button](/help/sites-cloud/authoring/assets/editing-component-toolbar-configure.png)

* **Copy**

  This will copy the component to the clipboard. After the paste action, the original component will remain.

  ![Copy button](/help/sites-cloud/authoring/assets/editing-component-toolbar-copy.png)

* **Cut**

  This will copy the component to the clipboard. After the paste action, the original component will be removed.

  ![Cut button](/help/sites-cloud/authoring/assets/editing-component-toolbar-cut.png)

* **Delete**

  This will delete the component from the page with your confirmation.

  ![Delete button](/help/sites-cloud/authoring/assets/editing-component-toolbar-delete.png)

* **Insert component**

  This opens the dialog to [add a new component](/help/sites-cloud/authoring/fundamentals/editing-content.md#inserting-a-component-from-the-paragraph-system).

  ![Insert button](/help/sites-cloud/authoring/assets/editing-component-toolbar-insert.png)

* **Paste**

  This will paste the component from the clipboard to the page. Whether the original remains, depends on whether you used copy or cut.

  * You can paste to the same page or to a different page.
  * The pasted item will be pasted above the item where you select the paste action.
  * The Pate action will only be shown if there is content on the clipboard.

  ![Paste button](/help/sites-cloud/authoring/assets/editing-component-toolbar-paste.png)

  >[!NOTE]
  >
  >If you paste to a different page that was already open before the cut/copy operation, you must refresh the page to see the pasted content.

* **Group**

  This allows you to select multiple components at once. The same can be achieved on a desktop device by a **Control+Click** or **Command+Click**.

  ![Group button](/help/sites-cloud/authoring/assets/editing-component-toolbar-group.png)

* **Parent**

  This allows you to select the parent component of the selected component.

  ![Parent button](/help/sites-cloud/authoring/assets/editing-component-toolbar-parent.png)

* **Layout**

  This allows you to modify the [layout](/help/sites-cloud/authoring/fundamentals/editing-content.md#edit-component-layout) of the selected component. This only applies to the selected component and does not activate the [Layout mode](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-modes) for the entire page.

  ![Layout button](/help/sites-cloud/authoring/assets/editing-component-toolbar-layout.png)

* **Convert to an experience fragment variation**

  This allows you to create a new [experience fragment](/help/sites-cloud/authoring/fundamentals/experience-fragments.md) from the selected component or add it to an existing experience fragment.

  ![Convert to Experience Fragment button](/help/sites-cloud/authoring/assets/editing-component-toolbar-xf.png)

## Edit Content {#edit-content}

There are two methods of adding and/or editing content in components:

* Open the [component dialog for editing](#component-edit-dialog).
* [Drag and drop an asset](#drag-and-drop-assets-into-component) from the assets browser to directly add content.

### Component Edit Dialog {#component-edit-dialog}

You can open a component to edit the content using the [Edit (pencil) icon of the component toolbar](#component-toolbar).

The exact edit options will depend on the component. For some components [all actions will only be available in full screen mode](#edit-content-full-screen-mode). For example:

* Text component

  ![Toolbar of the text component](/help/sites-cloud/authoring/assets/editing-text-component-toolbar.png)

* Image component

  ![Toolbar of the image component](/help/sites-cloud/authoring/assets/editing-image-component-toolbar.png)

  >[!NOTE]
  >
  >Editing does not work on an empty image component.
  >
  >You must drag or upload an image to the component before you can start to edit it.

* Image component - full screen

  [Entering full screen mode](#edit-content-full-screen-mode) for the image component allows for more space to edit the image as well as showing extra editing options such as **Launch Map** and **Reset Zoom**. In addition, full screen allows for crop presets to be selected.

  ![Image Component's full screen mode](/help/sites-cloud/authoring/assets/editing-image-component-full-screen.png)

* Components constructed from more than one basic component first ask you to confirm which set of edit options you want:

### Drag and Drop Assets into Component {#drag-and-drop-assets-into-component}

For specific component types (such as images) you can drag-and-drop assets from the asset browser directly into the component to update the content.

## Edit Content in Full Screen Mode {#edit-content-full-screen-mode}

For all components the full screen mode can be accessed with (and exited from):

![Full Screen button](/help/sites-cloud/authoring/assets/editing-full-screen.png)

For example, the **Text** component:

![Text component in full screen](/help/sites-cloud/authoring/assets/editing-text-full-screen.png)

>[!NOTE]
>
>For some components, the full screen mode will have more options available than the basic in-place editor.

## Moving a Component {#moving-a-component}

To move a paragraph component:

1. Select the paragraph to be moved with either tap-and-hold or click-and-hold.
1. Drag the paragraph to the new location. AEM indicates where the paragraph can be deposited. Drop it in your desired location.

   ![Moving a component](/help/sites-cloud/authoring/assets/editing-moving-component.png)

1. Your paragraph is moved.

>[!TIP]
>
>You can also use [Cut and Paste](#component-toolbar) to move a component.

## Edit Component Layout {#edit-component-layout}

Instead of repeatedly switching from edit to [layout mode](/help/sites-cloud/authoring/features/responsive-layout.md) to adjust a component, you can select the **Layout** action for a component to change that component's layout and save time by not having to leave the edit mode.

1. When in **Edit** mode of the sites console, selecting a component reveals the component's toolbar.

   ![The component toolbar of a page component](/help/sites-cloud/authoring/assets/editing-layout-toolbar.png)

   Click or tap the **Layout** action to adjust the layout of the component.

   ![The Layout button of the component toolbar](/help/sites-cloud/authoring/assets/editing-component-toolbar-layout.png)

1. Once the Layout action is selected:

    * The resizing handles for the component display.
    * The emulator toolbar is shown at the top of the screen.
    * Layout actions instead of the standard edit actions show on the component toolbar.

   ![A component in layout mode](/help/sites-cloud/authoring/assets/editing-layout-mode.png)

   You can now modify the layout of the component as you would in [layout mode](/help/sites-cloud/authoring/features/responsive-layout.md#defining-layouts-layout-mode).

1. After making the necessary layout changes, click the **Close** button in the component action menu to stop modifying the layout of the component. The component's toolbar returns to its normal edit state.

   ![The component toolbar of a page component](/help/sites-cloud/authoring/assets/editing-layout-exit.png)

>[!TIP]
>
>The Layout action is limited in scope to the selected component. For example, if you are editing the layout of one component and then click on another component, the standard edit toolbar (not the layout toolbar) displays for the newly selected component and the resizing handles as well as the emulator toolbar disappear.
>
>If you need to edit the overall layout of the page, affecting multiple components, switch to the [layout mode](/help/sites-cloud/authoring/features/responsive-layout.md).

## Inherited Components {#inherited-components}

Inheritance is the mechanism where content can be automatically pushed from one component to another. Inherited components can be the product of various scenarios, including:

* [Multi site management](/help/sites-cloud/administering/msm/overview.md)
* [Launches](/help/sites-cloud/authoring/launches/overview.md) (when based on live copy).

You can cancel (then re-enable) the inheritance. Depending on the component, this can be available from the component toolbar, if the component is on a page that is part of a live copy or launch (based on a live copy).

![A component toolbar showing inheritance relationship](/help/sites-cloud/authoring/assets/editing-component-toolbar-inheritance.png)

For example:

* Cancel Inheritance

  ![Cancel Inheritance button](/help/sites-cloud/authoring/assets/editing-cancel-inheritance.png)

* Re-enable Inheritance (if inheritance is already cancelled)

  ![Re-Enable Inheritance button](/help/sites-cloud/authoring/assets/editing-reenable-inheritance.png)

* Rollout action is also available in the blueprint or Live Copy source

  ![Rollout button](/help/sites-cloud/authoring/assets/editing-rollout.png)

## Editing the Page Template {#editing-the-page-template}

You can easily switch to the [template editor](/help/sites-cloud/authoring/features/templates.md#editing-templates-template-authors) by selecting **Edit Template** in the [Page Information menu](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-information).

You can easily see which template the page is based on when selecting the page in either [Column view](/help/sites-cloud/authoring/getting-started/basic-handling.md#column-view) or [List view](/help/sites-cloud/authoring/getting-started/basic-handling.md#list-view).

## Live Copy Status {#live-copy-status}

The [Live Copy Status page mode](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-modes) allows you a quick overview of the live copy status and which components are/are not inherited:

* Green border: Inherited
* Pink border: Inheritance has been cancelled

For example:

![Example of live copy status being displayed](/help/sites-cloud/authoring/assets/editing-live-copy-status.png)

## Adding Annotations {#adding-annotations}

[Annotations](/help/sites-cloud/authoring/fundamentals/annotations.md) allow reviewers and other authors to provide feedback on your content. They are often used for review and validation purposes.

## Previewing Pages {#previewing-pages}

There are two options for previewing a page:

* [Preview Mode](#preview-mode) - a quick, in-place preview
* [View as Published](#view-as-published) - a full preview that opens the page in a new tab

>[!TIP]
>
>* Links in the content are visible, but not accessible in Edit mode.
>* Use either of the preview options if you want to navigate using your links.
>* Use the [keyboard shortcut](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) `Ctrl-Shift-M` to switch between preview and the last selected mode.

>[!NOTE]
>
>The WCM Mode cookie is set for both preview options.

### Preview Mode {#preview-mode}

When editing content you can preview the page using the preview [mode](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-modes). This mode:

* Hides various edit mechanisms to give you a quick view of how the page will appear on publish.
* Allows you to use links to navigate.
* Does **not** refresh the page content.

When authoring, the preview mode is available using the icon at the top right of the page editor:

![Preview button](/help/sites-cloud/authoring/assets/preview.png)

### View as Published {#view-as-published}

The **View as Published** option is available from the [Page Information](/help/sites-cloud/authoring/fundamentals/environment-tools.md#page-information) menu. This opens the page in a new tab, refreshes the content and shows the page exactly as it will appear in the publish environment.

## Locking a Page {#locking-a-page}

AEM allows you to lock a page, so that no one else can modify the contents. This is useful when you are making a lot of edits to one specific page or when you need to freeze a page for a short while.

A page can be locked from either:

* **Sites** console

    1. Select the page with [selection mode](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources).
    1. Select the lock icon.

       ![Lock button](/help/sites-cloud/authoring/assets/lock.png)

* **Page Editor**

    1. Select the **Page Information** icon to open the menu.
    1. Select the **Lock Page** option.

Once locked the console view information is updated and when editing a lock symbol is shown in the toolbar.

![Example of a locked page](/help/sites-cloud/authoring/assets/editing-locked-page.png)

>[!CAUTION]
>
>Locking a page can be performed when impersonating a user. However a page locked in this way can only then be unlocked by the user who was impersonated or by the admin user.
>
>Pages can not be unlocked by impersonating the user who locked the page.
<!--
>Locking a page can be performed when [impersonating a user](/help/sites-administering/security.md#impersonating-another-user). However a page locked in this way can only then be unlocked by the user who was impersonated or by the admin user.
-->

## Unlocking a Page {#unlocking-a-page}

Unlocking a page is very similar to [locking the page](#locking-a-page). Once the page is locked the lock options are replaced by unlock actions.

The Page Information menu lists **Unlock** as an option and the Lock icon in the sites console is replaced by an **Unlock** icon.

![Unlock button](/help/sites-cloud/authoring/assets/unlock.png)

>[!CAUTION]
>
>Locking a page can be performed when impersonating a user. However a page locked in this way can only then be unlocked by the user who was impersonated or by the admin user.
>
>Pages can not be unlocked by impersonating the user who locked the page.
<!--
>Locking a page can be performed when [impersonating a user](/help/sites-administering/security.md#impersonating-another-user). However a page locked in this way can only then be unlocked by the user who was impersonated or by the admin user.
-->

## Undoing and Redoing Page Edits {#undoing-and-redoing-page-edits}

The following icons allow you to undo or redo an action. These are shown in the toolbar when appropriate:

![The Undo and Redo buttons](/help/sites-cloud/authoring/assets/redo.png)

>[!TIP]
>
>* The [keyboard shortcut](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) `Ctrl-Z` is also available to undo page edit actions.
>* The keyboard shortcut `Ctrl-Y` is also available to redo page edit actions.

>[!NOTE]
>
>See [Undoing and Redoing Page Edits - The Theory](#undoing-and-redoing-page-edits-the-theory) for the full details of what is possible when undoing and redoing page edits.

## Undoing and Redoing Page Edits - The Theory {#undoing-and-redoing-page-edits-the-theory}

AEM stores a history of actions that you perform and the sequence in which you performed them so that you can undo multiple actions in the order that you performed them as well as redo them to re-apply one or more of the actions if necessary.

If an element on the content page is selected (such as a text component), then the undo and redo command applies to the selected item.

The behavior of the undo and redo commands is similar to that in other software. Use the commands to restore the recent state of your web page as you make decisions about content. For example, if you move a text paragraph to a different location on the page, you can use the undo command to move the paragraph back. If you then decide that the previous position was better, use the redo command to "undo the undo".

For example, you can:

* Redo actions as long as you have not made a page edit since you used undo.
* Undo a maximum of 20 edit actions (default setting).
* Also use [Keyboard shortcuts](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) for undo and redo.

You can use undo and redo for the following types of page changes:

* Adding, editing, removing, and moving paragraphs
* In-place editing of paragraph content
* Copying, cutting, and pasting items within a page

>[!NOTE]
>
>* Special permissions are required to undo and redo changes to files and images.
>* The history of changes to files and images lasts for a minimum of ten hours. Beyond this time however, the undo of the changes is not guaranteed. Your administrator can change the default time of ten hours.
>* Your system administrator can configure various aspects of the Undo/Redo features according to the requirements for your instance.
<!--* Your system administrator can [configure various aspects of the Undo/Redo features](/help/sites-administering/config-undo.md) according to the requirements for your instance.-->
