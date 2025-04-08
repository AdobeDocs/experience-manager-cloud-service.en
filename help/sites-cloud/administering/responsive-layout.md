---
title: Configuring the Layout Container and Layout Mode
description: Learn how to configure layout container and layout mode to enable responsive layouts for your content authors.
exl-id: 469e8151-8231-4ccc-b7f6-855545f87440
solution: Experience Manager Sites
feature: Administering
role: Admin
---

# Configuring the Layout Container and Layout Mode {#configuring-layout-container-and-layout-mode}

Learn how to configure layout container and layout mode to enable responsive layouts for your content authors.

>[!TIP]
>
>This document describes how a site administrator can configure the layout container to support responsive web design. Additional resources are available:
>
>* For content authors, details of how to use responsive design features on a content page are available in the document [Responsive Layout.](/help/sites-cloud/authoring/page-editor/responsive-layout.md)
>* For developers, details of the Layout Container and the responsive grid are described in the [The Responsive Design document,](/help/implementing/developing/introduction/responsive-design.md) which provides and tips for using layout containers and responsive grid when designing your site.

## Overview {#overview}

Responsive Layout is a mechanism for realizing [responsive web design](https://en.wikipedia.org/wiki/Responsive_web_design). This allows the content author to create web pages that have a layout and dimensions dependent on the devices their users use.

AEM realizes responsive layout for your pages using a combination of mechanisms:

* **[Layout Container](/help/sites-cloud/authoring/page-editor/responsive-layout.md#adding-a-layout-container-and-its-content-edit-mode)** - This component provides a grid-paragraph system that allows you to add and position components within a responsive grid.
  * It can be used as the default parsys for your page and/or made available to authors in the component browser.
  * The default **Layout Container** component is defined under `/libs/wcm/foundation/components/responsivegrid`.
  * You can define layout containers:
    * As a component that the user can add to a page.
    * As the default parsys for the page.
    * As both a component and the default parsys.
      * You can have the layout container as standard for the page, while allowing the user to add further layout containers within this; for example, to achieve column control.
* **[Layout Mode](/help/sites-cloud/authoring/page-editor/introduction.md#mode-selector)** - Once the layout container is positioned on your page you can use the **Layout** mode to position content within the responsive grid.
* **[Emulator](/help/sites-cloud/authoring/page-editor/responsive-layout.md#selecting-a-device-to-emulate)** - This allows you to create and edit responsive websites that rearrange the layout according to device/window size by resizing components interactively. The user can then see how the content is rendered using the emulator.

With these responsive grid mechanisms you can:

* Use breakpoints (that indicate device grouping) to define differing content behavior based on device layout.
* Hide components based on device group (define on which breakpoint a component will be hidden).
* Use horizontal snap to grid (place components into the grid, resize as required, define when they should collapse/reflow to be side-by-side or above/below).
* Realize column control.

>[!NOTE]
>
>When creating a site from the [Project Archetype](#addlink) or from the [Standard Site Template](#addlink), the responsive layout is generally configured. Otherwise, you must [activate the Layout Container component](#enable-the-layout-container-component-for-page) for your pages.

## Enabling the Emulator {#enabling-emulator}

The [Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html) and the [Standard Site Template](/help/sites-cloud/administering/site-creation/site-templates.md#standard-site-template) are already enabled to use the emulator. If you have developed your own content not based on the Core Components or archetype, please see the document [Responsive Design](/help/implementing/developing/introduction/responsive-design.md) for details on how to develop your components while leveraging these features.

## Activate Layout Mode for your Site {#activate-layout-mode-for-your-site}

**Layout** mode allows you to use the emulator to adjust the layout of your content for different devices. The WKND sample site is already enabled for **Layout** mode. Follow these steps to enable your own site.

### Configure Breakpoints {#configure-breakpoints}

Breakpoints are vital to responsive design and define how and when content is adjusted to the target device. However, be cautious since each breakpoint you introduce will generate additional work for your authors to accommodate the content. Many times, two breakpoints can be sufficient, including the default breakpoint which is always there. Adobe recommends not to create more than three breakpoints including the default, i.e. not  more than two nodes below `cq:responsive/breakpoint`.

* Breakpoints have a title and a width:
  * The title describes the generic device grouping, with orientation if necessary.
    * For example, `phone`, `tablet`
  * The width defines the maximum width in pixels for that generic device grouping.
    * For example, if the breakpoint phone has a width of 768 then that it the maximum width of the layout used for a phone device.
* Breakpoints can be defined:
  * On the page template, from where the settings are copied to any pages created with that template.
  * On the page node, from where the settings are inherited by any child pages.
* Breakpoints are visible as markers at the top of the page editor when you are using the emulator.
* Breakpoints are inherited from the parent node hierarchy and can be overridden at will.
* There is a default (out-of-the-box) breakpoint which covers everything above the last configured breakpoint.
* Breakpoints can be defined using CRXDE Lite or XML.

Breakpoints should be considered for both new and existing projects.

* If you are setting up a new project, you should add breakpoints to the templates.
* If you are migrating an existing project (with existing content), you must:
  * Add breakpoints to the templates.
  * Add the same breakpoints to the existing pages.

Because of inheritance you only have to do this for the root page of your content.

#### Configuring Breakpoints using CRXDE Lite {#configuring-breakpoints-using-crxde-lite}

1. Using CRXDE Lite, navigate to either:

    * Your template definition.
    * The `jcr:content` node of your page.

1. Under `jcr:content` create the node:

    * Name: `cq:responsive`
    * Type: `nt:unstructured`

1. Under this create the node:

    * Name: `breakpoints`
    * Type: `nt:unstructured`

1. Under the breakpoints node you can create any number of breakpoints. Each definition is a single node with the following properties:

    * Name: `<descriptive name>`
    * Type: `nt:unstructured`
    * Title: `String <descriptive title seen in Emulator>`
    * Width: `Decimal <value of breakpoint>`

#### Configuring Breakpoints using XML {#configuring-breakpoints-using-xml}

Breakpoints are located inside the `<jcr:content>` section of the `.context.html` under the appropriate template (or content) folder.

An example definition:

```xml
<cq:responsive jcr:primaryType="nt:unstructured">
  <breakpoints jcr:primaryType="nt:unstructured">
    <phone jcr:primaryType="nt:unstructured" title="{String}Phone" width="{Decimal}768"/>
    <tablet jcr:primaryType="nt:unstructured" title="{String}Tablet" width="{Decimal}1200"/>
  </breakpoints>
</cq:responsive>
```

## Enable Component Resizing for the Page {#enable-component-resizing-for-the-page}

Resizing components in **Layout** mode is an important part of responsive design, which can be used in the WKND sample site. Follow these steps to enable your own site.

### Set Layout Container as Main Parsys {#set-layout-container-as-main-parsys}

To set the main parsys of your page to be a layout container, define the parsys as:

`wcm/foundation/components/responsivegrid`

In either the:

* Page component
* Page template (for future use)

The following two examples illustrate the definition:

* **HTL:**

  ```xml
  <sly data-sly-resource="${'par' @ resourceType='wcm/foundation/components/responsivegrid'}/>
  ```

* **JSP:**

  ```xml
  <cq:include path="par" resourceType="wcm/foundation/components/responsivegrid" />
  ```

### Include the Responsive CSS {#include-the-responsive-css}

#### CSS for Breakpoints using LESS {#css-for-breakpoints-using-less}

AEM uses LESS to generate parts of the necessary CSS, these need to be included for your projects.

You must create a [client library](/help/implementing/developing/introduction/clientlibs.md) to provide additional configuration and function calls. The following LESS extract is an example of the minimum that you must add to your project:

```java
@import (once) "/libs/wcm/foundation/clientlibs/grid/grid_base.less";

/* maximum amount of grid cells to be provided */
@max_col: 12;

/* default breakpoint */
.aem-Grid {
  .generate-grid(default, @max_col);
}

/* phone breakpoint */
@media (max-width: 768px) {
  .aem-Grid {
    .generate-grid(phone, @max_col);
  }
}

/* tablet breakpoint */
@media (min-width: 769px) and (max-width: 1200px) {
  .aem-Grid {
    .generate-grid(tablet, @max_col);
  }
}
```

The base grid definition can be found under:

`/libs/wcm/foundation/clientlibs/grid/grid_base.less`

#### Styling Considerations {#styling-considerations}

Components held within a responsive container are resized (together with their respective HTML DOM elements) according to the responsive grid size. Therefore, in these circumstances, it is recommended to avoid (or update) definitions of fixed width (contained) DOM elements.

For example:

* Before:

    * `width=100px`

* After:

    * `max-width=100px`

#### Resizing and Adaptive Image Compliance {#resizing-and-adaptive-image-compliance}

Any resizing of a component within the grid will trigger the following listeners as appropriate:

* `beforeedit`
* `beforechildedit`
* `afteredit`
* `afterchildedit`

To properly resize and update the content of an adaptive image included in a responsive grid, you need to add an `afterEdit` set to `REFRESH_PAGE` listener into the `EditConfig` file of every contained component.

For example:

`<cq:listeners jcr:primaryType="cq:EditListenersConfig" afteredit="REFRESH_PAGE" />`

The adaptive image mechanism is made available via a script that controls selection of the correct image for the current size of the window. It activates after the DOM is ready or when receiving a dedicated event. Currently the page must be refreshed to properly reflect the result of the user's action.

>[!CAUTION]
>
>Custom stylesheet clientlibs must be loaded as part of the header for them to work properly on author as well as publish.

## Enable the Layout Container Component for Page {#enable-the-layout-container-component-for-page}

For effective responsive layout, the content author must be able to drag instances of the Layout Container component onto the page. This is already enabled for the WKND sample site. Follow these steps to enable your own site.

### Enable the Layout Container Component for Page Editing {#enable-the-layout-container-component-for-page-editing}

To allow authors to add further responsive grids to the content pages you need to enable the Layout Container component for your page. You can do this using either:

* **Via the Author Environment** - [Edit your page templates](/help/sites-cloud/authoring/page-editor/templates.md) to enable the Layout Container for a page.
* **Component Definition** - Use `allowedComponent` or a static include when defining the component.

### Configure the Grid of the Layout Container {#configure-the-grid-of-the-layout-container}

You can configure the number of columns available for each specific instance of layout container [by editing your page templates](/help/sites-cloud/authoring/page-editor/templates.md).

### Nested Responsive Grids {#nested-responsive-grids}

Adobe's recommended best practice is to keep the structure as flat as possible.

When you can not avoid using nested responsive grids, please see the developer document [Responsive Design.](/help/implementing/developing/introduction/responsive-design.md#nested-responsive-grids)
