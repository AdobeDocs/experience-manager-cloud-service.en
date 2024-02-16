---
title: Editing Page Content with the AEM Page Editor
description: The AEM Page Editor is a powerful tool for authoring your content.
---

# Editing Page Content with the AEM Page Editor {#edit-content}

The AEM Page Editor is a powerful tool for authoring the content of a page. Learn how to use it to drag-and-drop content and edit content in-place.

## Overview {#overview}

There are three basic actions you can take in the page editor to edit your content:

1. Adding new components by dragging and dropping them onto the page.
1. Adding new assets by dragging and dropping them onto the page.
1. Editing components in-place that already exist on the page.

The AEM page editor provides an intuitive UI for performing these tasks in addition to giving access to more advanced features.

In addition, the editor allows you to organize the existing content on you page by allowing you to 

* Move components
* Edit component layout
* Edit component inheritance


## Adding Components {#adding-components}

You can drag-and-drop new components onto your page by selecting them from the component browser in the side panel and dropping them in a component placeholder.

### Component Placeholder {#component-placeholder}

The component placeholder is an indicator to show where a component is positioned when you drop it - above the component you are currently hovering over.

* When adding a new component to the page (dragging from the component browser):

  ![Placeholder when adding a new component to a page](/help/sites-cloud/authoring/assets/editing-component-placeholder.png)

* When moving an existing component:

  ![Placeholder when moving an existing component on a page](/help/sites-cloud/authoring/assets/editing-component-placeholder-existing.png)

### Adding a Component from the Components Browser {#adding-a-component-from-the-components-browser}

You can add a new component by using the [component browser](help/sites-cloud/authoring/getting-started/editor-side-panel.md#components-browser). The [component placeholder](#component-placeholder) shows you where the component is positioned:

1. Make sure that your page is in [**Edit** mode.](/help/sites-cloud/authoring/getting-started/page-editor.md#mode-selector)
1. Open the [component browser.](/help/sites-cloud/authoring/getting-started/editor-side-panel.md#components-browser)
1. Drag the required component to the [required position](#component-placeholder).
1. [Edit](#edit-content) the component.

>[!NOTE]
>
>On a mobile device, the component browser will fill the entire screen. Once you start dragging a component, the browser will close to show the page again so you can place the component.

### Adding a Component from the Paragraph System {#adding-a-component-from-the-paragraph-system}

You can add a new component by using the **Drag components here** placeholder of the paragraph system:

1. Make sure that your page is in [**Edit** mode.](/help/sites-cloud/authoring/getting-started/page-editor.md#mode-selector)
1. There are two ways to select and add a new component from the paragraph system:

    * Select the **Insert Component** option (+) from either the toolbar of an existing component or the **Drag components here** box.

      ![Insert a component](/help/sites-cloud/authoring/assets/editing-insert-component.png)

    * If you are on a desktop device you can double-click the **Drag components here** box.

    * The **Insert New Component** dialog open to let you select your required component:

      ![Insert New Component dialog](/help/sites-cloud/authoring/assets/editing-insert-component-selection.png)

1. The selected component is added to the bottom of the page. [Edit](#edit-content) the component as required.

## Adding an Asset {#adding-asset}

You can also add a new component to the page by dragging an asset from the [assets browser](/help/sites-cloud/authoring/getting-started/editor-side-panel.md#assets-browser). This automatically creates a component of the appropriate type (and containing the asset).

This behavior can be configured for your installation. Please see the document [Components Reference Guide](/help/implementing/developing/components/reference.md#component-placeholders) for further details.

To create a component by dragging one of the above asset types:

1. Make sure that your page is in [**Edit** mode.](/help/sites-cloud/authoring/getting-started/page-editor.md#mode-selector)
1. Open the [asset browser](/help/sites-cloud/authoring/getting-started/editor-side-panel.md#assets-browser).
1. Drag the required asset to the required position. The [component placeholder](#component-placeholder) shows you where the component is positioned.

   * A component, appropriate for the asset type, is created at the required location - it contains the selected asset.

1. [Edit](#edit-content) the component if necessary.

>[!NOTE]
>
>On a mobile device, the asset browser will fill the entire screen. Once you start dragging an asset, the browser will close to show the page again so you can place the asset.

If when browsing the assets you find that you need to make a quick change to an asset, you can start the [asset editor](/help/assets/manage-digital-assets.md) directly from the browser by clicking the edit icon next to the asset's name.

![Asset edit button](/help/sites-cloud/authoring/assets/asset-edit-button.png)

## Editing Components In-Place {#edit-in-place}

Selecting a component opens the component toolbar. This provides access to various actions that can be performed on the component.

The actual actions available to the user are shown as appropriate and not all actions may be described here.

![Component Toolbar](/help/sites-cloud/authoring/assets/editing-component-toolbar.png)

* **Edit**

  [Dependent on the component type](/help/sites-cloud/authoring/fundamentals/components.md), this lets you [edit the content of the component](#edit-content). Often a toolbar is provided.

  ![Edit button](/help/sites-cloud/authoring/assets/editing-component-toolbar-edit.png)

* **Configure**

  [Dependent on the component type](/help/sites-cloud/authoring/fundamentals/components.md), this lets you edit and configure the properties of the component. Often a dialog is opened.

  ![Configure button](/help/sites-cloud/authoring/assets/editing-component-toolbar-configure.png)

* **Copy**

  This will copy the component to the clipboard. After the paste action, the original component will remain.

  ![Copy button](/help/sites-cloud/authoring/assets/editing-component-toolbar-copy.png)

* **Cut**

  This will copy the component to the clipboard. After the paste action, the original component is removed.

  ![Cut button](/help/sites-cloud/authoring/assets/editing-component-toolbar-cut.png)

* **Delete**

  This will delete the component from the page with your confirmation.

  ![Delete button](/help/sites-cloud/authoring/assets/editing-component-toolbar-delete.png)

* **Insert component**

  This opens the dialog to [add a new component.](#adding-a-component-from-the-paragraph-system)

  ![Insert button](/help/sites-cloud/authoring/assets/editing-component-toolbar-insert.png)

* **Paste**

  This will paste the component from the clipboard to the page. Whether the original remains, depends on whether you used copy or cut.

  * You can paste to the same page or to a different page.
  * The pasted item is pasted above the item where you select the paste action.
  * The Pate action will only be shown if there is content on the clipboard.

  ![Paste button](/help/sites-cloud/authoring/assets/editing-component-toolbar-paste.png)

  >[!NOTE]
  >
  >If you paste to a different page that was already open before the cut/copy operation, you must refresh the page to see the pasted content.

* **Group**

  This lets you select multiple components at once. The same can be achieved on a desktop device by a **Control+Click** or **Command+Click**.

  ![Group button](/help/sites-cloud/authoring/assets/editing-component-toolbar-group.png)

* **Parent**

  This lets you select the parent component of the selected component.

  ![Parent button](/help/sites-cloud/authoring/assets/editing-component-toolbar-parent.png)

* **Layout**

  This lets you modify the [layout](#editing-component-layout) of the selected component. This only applies to the selected component and does not activate the [Layout mode](/help/sites-cloud/authoring/getting-started/page-editor.md#mode-selector) for the entire page.

  ![Layout button](/help/sites-cloud/authoring/assets/editing-component-toolbar-layout.png)

* **Convert to an experience fragment variation**

  This lets you create an [experience fragment](/help/sites-cloud/authoring/fundamentals/experience-fragments.md) from the selected component or add it to an existing experience fragment.

  ![Convert to Experience Fragment button](/help/sites-cloud/authoring/assets/editing-component-toolbar-xf.png)

### Component Edit Dialog {#component-edit-dialog}

Some components offer additional configuration options beyond what is available in-place. You can open a component's edit dialog the [Edit (pencil) icon of the component toolbar](#component-toolbar) to access additional configuration options.

The exact edit options will depend on the component. For some components [some actions will only be available in full screen mode](#edit-content-full-screen-mode). For example:

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

  [Entering full screen mode](#edit-content-full-screen-mode) for the image component allows for more space to edit the image and showing extra editing options such as **Launch Map** and **Reset Zoom**. In addition, full screen allows for crop presets to be selected.

  ![Image Component's full screen mode](/help/sites-cloud/authoring/assets/editing-image-component-full-screen.png)

* Components constructed from more than one basic component first ask you to confirm which set of edit options you want:

### Drag and Drop Assets into Component {#drag-and-drop-assets-into-component}

For specific component types (such as images) you can drag-and-drop assets from the asset browser directly into the component to update the content.

### Edit Components in Full-Screen Mode {#edit-content-full-screen-mode}

Many components offer a full-screen mode for editing that can be accessed with this button.

![Full Screen button](/help/sites-cloud/authoring/assets/editing-full-screen.png)

For example, the **Text** component:

![Text component in full screen](/help/sites-cloud/authoring/assets/editing-text-full-screen.png)

Use the **Minimize** button to exist full-screen mode.

![Minimize button](assets/edit-content-minimize.png)

>[!NOTE]
>
>For some components, the full screen mode will have more options available than the basic in-place editor.

## Moving Components {#moving-components}

To move a paragraph component:

1. Select the paragraph to be moved with either select-and-hold or click-and-hold.
1. Drag the paragraph to the new location. AEM indicates where the paragraph can be deposited. Drop it in your desired location.

   ![Moving a component](/help/sites-cloud/authoring/assets/editing-moving-component.png)

1. Your paragraph is moved.

>[!TIP]
>
>You can also use [Cut and Paste](#component-toolbar) to move a component.

## Editing Component Layout {#editing-component-layout}

Instead of repeatedly switching from edit to [layout mode](/help/sites-cloud/authoring/features/responsive-layout.md) to adjust a component, you can select the **Layout** action for a component to change that component's layout and save time by not having to leave the edit mode.

1. When in **Edit** mode of the sites console, selecting a component reveals the component's toolbar.

   ![The component toolbar of a page component](/help/sites-cloud/authoring/assets/editing-layout-toolbar.png)

   Select the **Layout** action to adjust the layout of the component.

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
>The Layout action is limited in scope to the selected component. For example, if you are editing the layout of one component and then click another component, the standard edit toolbar (not the layout toolbar) displays for the newly selected component and the resizing handles and the emulator toolbar disappear.
>
>If you need to edit the overall layout of the page, affecting multiple components, switch to the [layout mode](/help/sites-cloud/authoring/features/responsive-layout.md).

## Editing Component Inheritance {#inherited-components}

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
