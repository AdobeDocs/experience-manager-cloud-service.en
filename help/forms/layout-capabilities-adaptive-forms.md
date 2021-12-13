---
title: Layout capabilities of Adaptive Forms
seo-title: Layout capabilities of Adaptive Forms
description: Layout and appearances of Adaptive Forms on various devices are governed by the layout settings. Understand the various layouts and how to apply them.
exl-id: e30c6ff9-692b-4415-8f14-b4ef616b2d12
---
# Layout capabilities of Adaptive Forms {#layout-capabilities-of-adaptive-forms}

[!DNL Adobe Experience Manager] lets you create easy-to-use Adaptive Forms that offer dynamic experiences to end users. The form layout controls how items or components are displayed in an Adaptive Form.

<!-- ## Prerequisite knowledge {#prerequisite-knowledge}

Before learning about the different layout capabilities of Adaptive Forms, read [Introduction to authoring forms](introduction-forms-authoring.md) to know more about Adaptive Forms. -->

## Types of layouts {#types-of-layouts}

An Adaptive Form provides you with the following types of layouts:

**[!UICONTROL Panel Layout]** Controls how items or components inside a panel are displayed on a device.

**[!UICONTROL Mobile Layout]** Controls the navigation of a form on a mobile device. If the device width is 768 pixels or more, the layout is considered a Mobile layout and optimized for a mobile device.

**[!UICONTROL Toolbar Layout]** Controls the placement of Action buttons in the toolbar or panel toolbar in a form.

All these panel layouts are defined at the `/libs/fd/af/layouts` location.

To change the layout of an Adaptive Form, use the Authoring Mode in [!DNL Experience Manager].

## [!UICONTROL Panel layout] {#panel-layout}

A form author can associate a layout with each panel of an Adaptive Form, including the root panel.

The Panel layouts are available at `/libs/fd/af/layouts/panel` location. Tap the panel and select ![cmppr1](assets/configure-icon.svg) to view the panel properties.

![List of panel layouts for root panel of an Adaptive Form](assets/layouts.png)

### [!UICONTROL Responsive - everything on one page without navigation] {#responsive-everything-on-one-page-without-navigation-br}

Use this panel layout to create a responsive layout that adjusts to the screen size of your device without any need for specialized navigation.

Using this layout, you can place multiple **[!UICONTROL Panel Adaptive Form]** components one after another inside the panel.

![A form using responsive layout as seen on a small screen](assets/responsive-layout.png)

### [!UICONTROL Wizard] {#wizard}

Use this panel layout to provide guided navigation inside a form. For example, use this layout when you want to capture mandatory information in a form while guiding users step by step.

Use the **[!UICONTROL Panel Adaptive Form]** component to provide step-by-step navigation inside a panel. When you use this layout, a user moves to the next step only after the current step is complete

```javascript
window.guideBridge.validate([], this.panel.navigationContext.currentItem.somExpression)
```

![A form using wizard layout](assets/wizard-layout2.png)

### [!UICONTROL Accordion] {#layout-for-accordion-design}

Using this layout, you can place the **[!UICONTROL Panel Adaptive Form]** component in a panel with accordion style navigation. Using this layout, you can also create repeatable panels. Repeatable panels enable you to dynamically add or remove panels as needed. You can define the minimum and the maximum number of times a panel repeats. Also, the title of the panel can be determined dynamically, based on the information provided in the panel items.

Summary expression can be used to show the values provided by the end user in the title of the minimized panel.

![Repeatable panels using Accordion layout in Adaptive Forms](assets/accordion-layout.png)

### [!UICONTROL Tabbed layout - tabs appear on the left ]{#tabbed-layout-tabs-appear-on-the-left}

Using this layout, you can place the **[!UICONTROL Panel Adaptive Form]** component in a panel with tab navigation. The tabs are placed on the left of the panel content.

![In the Tabbed layout, the tabs appear on the left](assets/tabs-on-left.png)

Tabs appearing on the left of a panel

### [!UICONTROL Tabbed layout - tabs appear on the top] {#tabbed-layout-tabs-appear-on-the-top}

Using this layout, you can place the **[!UICONTROL Panel Adaptive Form]** Component in a panel with tab navigation. The tabs are placed on top of the panel content.

![Tabbed layout in Adaptive Forms with tabs on the top](assets/tabs-on-top.png)

## Mobile layouts {#mobile-layouts}

Mobile layouts allow for user-friendly navigation on the mobile devices with relatively smaller screens. Mobile layouts use either tabbed or wizard styles for form navigation. Applying a Mobile Layout provides a single layout for the entire form.

This layout controls navigation using a navigation bar and a navigation menu. The navigation bar shows **&lt;** and **&gt;** icon to indicate **[!UICONTROL next]** and **[!UICONTROL previous]** navigation steps in the form.

The Mobile Layouts are available at `/libs/fd/af/layouts/mobile/` location. The following mobile layouts are available in Adaptive Forms, by default.

![List of Mobile Layouts in Adaptive Forms](assets/mobile-navigation.png)

Select the **[!UICONTROL Add navigable items of responsive layout to mobile menu]** option to view the navigable options available for a panel in Mobile layout. The navigable options are visible only if you select **[!UICONTROL Responsive]** layout for a panel.

When using a Mobile layout, the form menu, to access various form panels, is available by tapping ![aem6forms_form_menu](assets/rail-icon.svg) icon.

### [!UICONTROL Layout with panel titles in the form header] {#layout-with-panel-titles-in-the-form-header}

This layout, as the name suggests, shows panel titles along with the navigation menu and navigation bar. This layout also provides Next and Previous icons for navigation.

![Mobile layouts with panel titles in the form headers](assets/mobile-layout1.png)

### [!UICONTROL Layout without panel titles in the form header ]{#layout-without-panel-titles-in-the-form-header}

This layout, as the name suggests, shows only the navigation menu and navigation bar without panel titles. This layout also provides Next and Previous icons for navigation.

![Mobile layouts without panel titles in the form headers](assets/mobile-layout2.png)

<!-- ## Toolbar layouts {#toolbar-layouts}

A Toolbar Layout controls positioning and display of any action buttons that you add to your Adaptive Forms. The layout can be added at a form level or at a panel level.

![A list of Toolbar Layouts in Adaptive Forms to control layout of buttons](assets/toolbar-layouts.png)

A list of Toolbar Layouts in Adaptive Forms

Toolbar layouts are available at `/libs/fd/af/layouts/toolbar` location. Adaptive Forms provide the following Toolbar Layouts, by default.

### [!UICONTROL Default layout for toolbar] {#default-layout-for-toolbar}

This layout is selected as the default layout when you add any action buttons in an Adaptive Form. Selecting this layout displays the same layout for both, desktop and mobile devices.

Also, you can add multiple toolbars containing action buttons configured with this layout. An action button is associated with a form control. You can configure the toolbars to be before or after a panel.

![Default view for toolbar](assets/toolbar_layout_default.png)

Default view for toolbar

### [!UICONTROL Mobile fixed layout for toolbar] {#mobile-fixed-layout-for-toolbar}

Select this layout to provide alternate layouts for desktop and mobile devices.

For the desktop layout, you can add Action buttons using some specific labels. Only one toolbar can be configured with this layout. If more than one toolbar is configured with this layout, there is an overlap for mobile devices and only one toolbar is visible. For example, you can have a toolbar at the bottom or the top of the form, or, after or before panels in the form.

For the Mobile layout, you can add action buttons using icons.

![Mobile fixed layout for toolbar](assets/toolbar_layout_mobile_fixed.png)

Mobile fixed layout for toolbar-->
