---
title: Responsive Layout
description: AEM lets you realize a responsive layout for your pages
exl-id: 87202742-5bed-4e87-a427-456a1a0e72cc
solution: Experience Manager Sites
feature: Authoring
role: User
---
# Responsive Layout {#responsive-layout}

AEM lets you have a responsive layout for your pages by using the **Layout Container** component.

This provides a paragraph system that lets you position components within a responsive grid. This grid can rearrange the layout according to the device/window size and format. The component is used in conjunction with the [**Layout** mode](/help/sites-cloud/authoring/page-editor/introduction.md#mode-selector), which lets you create and edit your responsive layout dependent on device.

The layout container:

* Provides horizontal snap to grid, together with the ability to place components into the grid side-by-side and define when they should collapse/reflow.
* Uses pre-defined breakpoints (for example, for phone, tablet, and so on) to allow you to define the required behavior of content for related devices/orientation.
  * For example, you can customize the component size or whether the component can be seen on specific devices.
* Can be nested to allow column control.

The user can then see how the content is rendered for specific devices using the emulator.

AEM realizes responsive layout for your pages using a combination of mechanisms:

* [**Layout Container**](#adding-a-layout-container-and-its-content-edit-mode) component

  This component is available in the [component browser](/help/sites-cloud/authoring/page-editor/editor-side-panel.md#components-browser) and provides a grid-paragraph system to allow you to add and position components within a responsive grid. It can also be set as the default paragraph system on your page.

* [**Layout Mode**](/help/sites-cloud/authoring/page-editor/introduction.md#mode-selector)

  Once the layout container is positioned on your page you can use the **Layout** mode to position content within the responsive grid.

* [**Emulator**](#selecting-a-device-to-emulate)
  This lets you create and edit responsive websites that rearrange the layout according to device/window size by resizing components interactively. The user can then see how the content is rendered using the emulator.

With these responsive grid mechanisms you can:

* Use breakpoints to define differing content layouts based on device width (related to device type and orientation).
* Use these same breakpoints and content layouts to ensure that your content is responsive to the size of the browser window on the desktop.
* Use horizontal snap to grid allowing you to place components in the grid, resize as required, and define when they should collapse/reflow to be side-by-side or above/below.
* Hide components for specific device layouts.
* Realize column control.

Depending on your project, the Layout Container might be used as the default paragraph system for your pages or as a component available to be added to your page by way of the component browser (or both).

>[!TIP]
>
>Adobe provides [GitHub documentation](https://adobe-marketing-cloud.github.io/aem-responsivegrid/) of the responsive layout as a reference that can be given to front-end developers allowing them to use the AEM grid outside of AEM, for example, when creating static HTML mock-ups for a future AEM site.

>[!NOTE]
>
>Use of the above mechanisms is enabled by configuration on the template. Please see the document [Configuring Responsive Layout](/help/sites-cloud/administering/responsive-layout.md) for further information.

## Layout Definitions, Device Emulation, and Breakpoints {#layout-definitions-device-emulation-and-breakpoints}

When you are creating your website content you want to ensure that your content is displayed appropriate to the device being used to view it.

AEM lets you define layouts dependent on the width of the device:

* The emulator enables you to emulate these layouts on a range of devices. In addition to the device type, the orientation, selected by the **Rotate device** option, can impact the breakpoint selected as the width changes.
* Breakpoints are the points which separate the layout definitions.
  * They effectively define the maximum width (in pixels) of any device using a specific layout.
  * The breakpoints are usually valid for a selection of devices, dependent on the width of their displays.
  * The range of a breakpoint extends left until the next breakpoint.
  * You cannot select the breakpoint specifically, selecting a device and orientation will automatically select the appropriate breakpoint.

The device **Desktop**, which does not have a specific width, relates to the default breakpoint (that is, everything above the last configured breakpoint).

>[!NOTE]
>
>It would be possible to define breakpoints for every individual device, but this would drastically increase the effort required for layout definition and maintenance.

When using the emulator, you select a specific device for emulation and layout definition and the related breakpoint is highlighted too. Any layout changes that you make are applicable for other devices to which the breakpoint applies. That is, any devices positioned to the left of the active breakpoint marker, but before the next breakpoint marker.

For example, when you select the device **iPhone 6 Plus** (defined with a width of 540 pixels) for emulation and layout, the breakpoint **Phone** (defined as 768 pixels) is activated too. Any layout changes you make for the **iPhone 6** are applicable to other devices under the **Phones** breakpoint, such as **iPhone 5** (defined as 320 pixels).

![Emulators](/help/sites-cloud/authoring/assets/responsive-layout-emulators.png)

## Selecting a Device to Emulate {#selecting-a-device-to-emulate}

1. Open the required page for editing. For example:

   `http://<host>:<port>/editor.html/content/wknd/en/sports/la-skateparks.html`

1. Select the **Emulator** icon from the top toolbar:

   ![Emulator button](/help/sites-cloud/authoring/assets/emulator.png)

1. The emulator toolbar opens.

   ![Emulator toolbar](/help/sites-cloud/authoring/assets/responsive-layout-emulator-toolbar.png)

   The emulator toolbar displays additional layout options:

    * **Rotate device** - Lets you rotate a device from vertical (portrait) orientation to horizontal (landscape) orientation and conversely.

   ![Rotate device landscape button](/help/sites-cloud/authoring/assets/responsive-layout-rotate-device-landscape-button.png)
   ![Rotate device portrait button](/help/sites-cloud/authoring/assets/responsive-layout-rotate-device-portrait-button.png)

    * **Select Device** - Define a specific device to emulate from a list (see next step for details)

   ![Select Device button](/help/sites-cloud/authoring/assets/responsive-layout-select-device-button.png)

1. To select a specific device to emulate you can either:

    * Use the Select Device icon and select from a drop-down selector.
    * Select the device indicator in the emulator toolbar.

   ![Select device dropdown](/help/sites-cloud/authoring/assets/responsive-layout-select-device-dropdown.png)

1. Once a specific device has been selected you can:

    * See the active marker for the selected device, such as **iPad.**
    * See the active marker for the appropriate [breakpoint](#layout-definitions-device-emulation-and-breakpoints) such as **Tablet.**
    * The blue dotted line represents the *fold* for the selected device (here an **iPhone 6 Plus** in landscape).

   ![The fold](/help/sites-cloud/authoring/assets/responsive-layout-fold.png)

    * The fold can also be considered the page line break (not to be confused with the [breakpoints](#layout-definitions-device-emulation-and-breakpoints)) for the content. This is displayed for convenience to show what part of the content the user sees on the device before scrolling.
    * The line for the fold is not shown if the height of the device being emulated is higher than the screen size.
    * The fold is shown for the author's convenience and is not shown on the published page.

## Adding a Layout Container and its Content (Edit mode) {#adding-a-layout-container-and-its-content-edit-mode}

A **Layout Container** is a paragraph system that:

* Contains other components.
* Defines the layout.
* Responds to changes.

>[!NOTE]
>
>If not already available, the **Layout Container** must be explicitly [activated for a paragraph system/page](/help/sites-cloud/administering/responsive-layout.md).

1. The **Layout Container** is available as a standard component in the [Components Browser](/help/sites-cloud/authoring/page-editor/editor-side-panel.md#components-browser). From here you can drag it to the required location on the page after which you can see the **Drag Components here** placeholder.
1. You can then add components to the layout container. These components will hold the actual content:

   ![Layout container](/help/sites-cloud/authoring/assets/responsive-layout-add-to-layout-container.png)

## Selecting and Taking Action on a Layout Container (Edit mode) {#selecting-and-taking-action-on-a-layout-container-edit-mode}

As with other components, you can select and then act on (cut, copy, delete) a Layout Container (when in **Edit** mode):

>[!CAUTION]
>
>As a layout container is a paragraph system, deleting the component will delete both the layout grid and all the components (and their content) held within the container.

1. If you mouse over or select the grid placeholder, the action menu is displayed.

   ![Add to the layout container](/help/sites-cloud/authoring/assets/responsive-layout-container.png)

   You need to select the **Parent** option.

   ![Parent button](/help/sites-cloud/authoring/assets/responsive-layout-parent-button.png)

1. If the layout component is nested, selecting the **Parent** option presents a drop-down selection, letting you to select the nested layout container or its parents.

   When you mouse over the container names in the drop-down, their outlines are displayed on the page.

    * The lowest nested layout container is outlined in blue.
    * Every successive container is outlined a lighter shade of blue.

   ![Nested containers](/help/sites-cloud/authoring/assets/responsive-layout-nested.png)

1. The entire grid is highlighted with its content. The action toolbar is shown, from where you can select an action such as **Delete.**

## Defining Layouts (Layout mode) {#defining-layouts-layout-mode}

>[!NOTE]
>
>You can define a separate layout for each [breakpoint](#layout-definitions-device-emulation-and-breakpoints) (as determined by emulated device type and orientation).

To configure the layout of a responsive grid implemented with the Layout Container you need to use the **Layout** mode.

**Layout** mode can be started in two ways.

* By using the [mode menu in the toolbar](/help/sites-cloud/authoring/page-editor/introduction.md#mode-selector) and choosing **Layout** mode
  * Select the **Layout** mode just as you would switch to **Edit** mode or **Targeting** mode.
  * **Layout** mode remains persistent and you do not leave **Layout** mode until you select another mode via the mode selector.
* When [editing an individual component](/help/sites-cloud/authoring/page-editor/edit-content.md#editing-component-layout).
  * By using the **Layout** option in the component's quick action menu, you can switch to **Layout** mode.
  * **Layout** mode persists while editing the component and reverts to **Edit** mode once focus changes to another component.

When in layout mode you can perform various actions on a grid:

* Resize the content components using the blue dots. Resizing will always snap-to-grid. When resizing, the background grid is shown to aid alignment:

  ![Resize components](/help/sites-cloud/authoring/assets/responsive-layout-resizing.png)

  >[!NOTE]
  >
  >Proportions and ratios are maintained when components such as **Images** are resized.

* Select a content component, the toolbar lets you:
  * **Parent** - Lets you select the entire layout container component for taking action on the whole.
  * **Float to new line** - The component is moved to a new line, dependent on the space available within the grid.
  * **Hide component** - The component is made invisible (it can be restored from the toolbar of the layout container).

  ![Hide component](/help/sites-cloud/authoring/assets/responsive-layout-hide.png)

* In **Layout** mode you can select the **Drag components here** to select the entire component. The toolbar is shown for this mode.

  The toolbar has different options depending on the state of the layout component and the components belonging to it. For example:

  * **Parent** - Select the parent component.

    ![Parent button](/help/sites-cloud/authoring/assets/responsive-layout-parent-button.png)

  * **Show hidden components** - Reveal all or individual components. The number indicates how many hidden components there currently are. The counter shows how many components are hidden.

    ![Show hidden components button](/help/sites-cloud/authoring/assets/responsive-layout-show-button.png)

  * **Revert breakpoint layout** - Revert to the default layout. No customized layout is imposed.

    ![Revert breakpoint layout button](/help/sites-cloud/authoring/assets/responsive-layout-revert-button.png)

  * **Float to new line** - Move the component up a position if spacing allows.

    ![Float to a new line button](/help/sites-cloud/authoring/assets/responsive-layout-float-button.png)

  * **Hide component** - Hide the current component.

    ![Hide component button](/help/sites-cloud/authoring/assets/responsive-layout-hide-button.png)

  >[!NOTE]
  >
  >In the above example the float and hide actions are available because this Layout Container is nested within a parent Layout Container.

  * **Unhide components**
      Select the parent components to show the action toolbar with the **Show hidden components** option. In this example, two components are hidden.

    ![Unhide components](/help/sites-cloud/authoring/assets/responsive-layout-unhide.png)

  Selecting the **Show hidden components** option will display in blue the components that are currently hidden in their original positions.

  ![Restore all button](/help/sites-cloud/authoring/assets/responsive-layout-restore-all.png)

  Selecting **Restore all** will unhide all hidden components.
