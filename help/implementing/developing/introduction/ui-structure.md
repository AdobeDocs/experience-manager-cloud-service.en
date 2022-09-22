---
title: Structure of the AEM UI
description: The AEM UI has several underlying principles and is made up of several key elements
exl-id: ac211716-d699-4fdb-a286-a0a1122c86c5
---
# Structure of the AEM UI {#structure-of-the-aem-ui}

The AEM UI has several underlying principles and is made up of several key elements:

## Consoles {#consoles}

### Basic Layout and Resizing {#basic-layout-and-resizing}

The UI caters for both mobile and desktop devices, though rather than creating two styles, AEM uses one style that works for all screens and devices.

All modules use the same basic layout, in AEM this can be seen as:

![AEM Sites console](assets/ui-sites-console.png)

The layout adheres to a responsive design style and will accommodate itself to the size of the device/window you are using.

For example, when the resolution goes below 1024px (as on a mobile device) the display will be adjusted accordingly:

![Sites console mobile view](assets/ui-sites-mobile.png)

### Header Bar {#header-bar}

![AEM header bar](assets/ui-header-bar.png)

The header bar shows global elements including:

* The logo and the specific product/solution that you are currently using; for AEM this also forms a link to the Global Navigation
* Search
* Icon for accessing the help resources
* Icon for accessing other Solutions
* A indicator of (and access to) any alerts or Inbox items that are waiting for you
* The user icon, together with a link to your profile management

### Toolbar {#toolbar}

The toolbar is contextual to your location and surfaces tools relevant to controlling the view or assets in the page below. The toolbar is product specific, but there is some commonality to the elements.

In any location the toolbar shows the actions currently available:

![AEM Sites toolbar](assets/ui-sites-toolbar.png)

Also dependent on whether a resource is currently selected:

![AEM Sites toolbar selected](assets/ui-sites-toolbar-selected.png)

### Left Rail {#left-rail}

The left rail can be opened/hidden as required to show:

* **Content Only**
* **Content Tree**
* **Timeline**
* **References**
* **Filter**

The default is **Content Only** (rail hidden).

![Left Rail](assets/ui-left-rail.png)

## Page Authoring {#page-authoring}

When authoring pages the structural areas are as follows.

### Content Frame {#content-frame}

The page content is rendered in the content frame. The content frame is completely independent of the editor - to ensure that there are no conflicts due to CSS or javascript.

The content frame is on the right-hand section of the window, under the toolbar.

![Content frame](assets/ui-content-frame.png)

### Editor Frame {#editor-frame}

The editor frame enables the editing features.

The editor frame is a container (abstract) for all the page authoring elements. It lives on top of the content frame, and includes:

* The top toolbar
* The side panel
* All the overlays
* Any other page authoring element; for example, the component toolbar

![Editor frame](assets/ui-editor-frame.png)

### Side Panel {#side-panel}

This contains three default tabs. The **Assets** and **Components** tabs allow you to select such elements and drag them from the panel and drop them onto the page. The **Content Tree** tab allows you to inspect the hierarchy of content on the page.

The side panel is hidden by default. When selected it will either be shown at the left side, or will slide across to cover the entire window when the window size is below a width of 1024px; as, for example, on a mobile device.

![Side panel](assets/ui-side-panel.png)

### Side Panel - Assets {#side-panel-assets}

In the Assets tab you can select from the range of assets. You can also filter on a specific term, or select a group.

![Assets tab](assets/ui-side-panel-assets.png)

### Side Panel - Asset Groups {#side-panel-asset-groups}

In the Assets tab there is a drop down that you can use to select the specific asset groups.

![Asset groups](assets/ui-side-panel-asset-groups.png)

### Side Panel - Components {#side-panel-components}

In the Components tab you can select from the range of components. You can also filter on a specific term, or select a group.

![Components tab](assets/ui-side-panel-components.png)

### Side Panel - Content Tree {#side-panel-content-tree}

In the Content Tree tab you can view the hierarchy of content on the page. Clicking an entry in the tab jumps to and selects the item on the page within the editor.

![Content tree](assets/ui-side-panel-content-tree.png)

### Overlays {#overlays}

These overlay the content frame and are used by the [layers](#layer) to realize the mechanics of how you can interact (completely transparently) with the components and their content.

The overlays live in the editor frame (with all other page authoring elements), though they actually overlay the appropriate components in the content frame.

![Overlays](assets/ui-overlays.png)

### Layer {#layer}

A layer is an independent bundle of functionality that can be activated to:

* Provide a different view of the page
* Allow you to manipulate and/or interact with a page

The layers provide sophisticated functionality for the entire page, as opposed to specific actions on an individual component.

AEM comes with several layers already implemented for page authoring; including for example, edit, preview, and annotate layers.

>[!NOTE]
>
>Layers are a powerful concept that affect the user's view of and interaction with the page content. When developing your own layers you need to ensure that the layer cleans up when it is exited.

### Layer Switcher {#layer-switcher}

The layer switcher allows you to choose the layer you want to use. When closed, it indicates the layer currently in use.

The layer switcher is available as a drop down from the toolbar (at the top of the window, within the editor frame).

![Layer switcher](assets/ui-layer-switcher.png)

### Component Toolbar {#component-toolbar}

Each instance of a component will reveal its toolbar when clicked (either once or with a slow double-click). The toolbar contains the specific actions (e.g. copy, paste, open-editor) that are available for the component instance on the page.

Depending on the space available, the component toolbars are positioned at the top-, or bottom-, right corner of the appropriate component.

![Component toolbar](assets/ui-component-toolbar.png)

## Further Information {#further-information}

<!--For more details about the concepts around the touch-enabled UI, continue to the article [Concepts of the AEM Touch-Enabled UI](/help/sites-developing/touch-ui-concepts.md).-->

For further technical information see the [JS documentation set](https://helpx.adobe.com/experience-manager/6-5/sites/developing/using/reference-materials/jsdoc/ui-touch/editor-core/index.html) for the page editor.
