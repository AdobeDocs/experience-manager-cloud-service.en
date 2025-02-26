---
title: Understanding Universal Editor - Responsive mode
description: This article explains how to preview forms using different emulators in the Universal Editor to visualize their look and feel during authoring.
feature: Edge Delivery Services
role: Admin, Architect, Developer
hide: Yes
hide from TOC: Yes
---

# Responsive Mode in WYSIWYG Authoring

The [Universal Editor](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) allows you to preview Edge Delivery Services Forms with different emulators to see the look and feel of the form during authoring.

The responsive mode enables developers to design layouts that automatically adapt to different screen sizes, including desktops, tablets, and mobile devices. The Universal Editor supports emulators for desktop, tablet, and mobile devices. You can set the height and width according to your screen size and perform the following actions:
   * Set the orientation
   * Specify the width and height
   * Change the orientation

## Preview Forms in Responsive Mode for Different Devices 

The Universal Editor provides an **Emulator** icon located at the top-right corner of the screen that allows you to preview pages across different device sizes and test the behavior of your responsive design for a better user experience.

To see how the Universal Editor renders forms on different screen sizes, perform the following steps:

1. Open the form in Universal editor for editing.
1. Select the ![Emulator icon](/help/edge/docs/forms/universal-editor/assets/emulator.png){height=2%,width=2%} available on the Universal Editor Toolbar and click the emulator icon to display the option.

    ![Responsive Mode](/help/edge/docs/forms/universal-editor/assets/universal-editor-emulator.png)

1. Select an option to emulate a form in the Universal Editor on a selected device: Desktop, Tablet, Mobile.

    ![Responsive mode](/help/edge/docs/forms/universal-editor/assets/ue-responsivemode.png){width=40%,height=40%}

   By default, the editor opens in a desktop layout, with the height and width automatically determined by the browser. Alternatively, you can emulate a form on a mobile or tablet device. You can also customize the screen width and height for custom devices.

The Universal Editor provides different emulators to preview forms on various devices. The table below lists the available emulator types along with their corresponding device representations:

<table border="1" style= text-align: left; border-collapse: collapse;">
    <tr>
        <th style="width: 20%">Type of Emulator</th>
        <th style="width: 80%">Device Image</th>
    </tr>
    <tr>
        <td style="width: 20%">Desktop</td>
        <td style="width: 80%"><img src="/help/edge/docs/forms/universal-editor/assets/universal-editor-desktop.png" alt="Desktop Emulator" style="width: auto; height: auto"></td>
    </tr>
    <tr>
        <td style="width: 20%">Tablet</td>
        <td style="width: 80%"><img src="/help/edge/docs/forms/universal-editor/assets/universal-editor-tab.png" alt="Tablet Emulator" style="width: auto; height: auto"></td>
    </tr>
    <tr>
        <td style="width: 20%">Mobile</td>
        <td style="width: 80%"><img src="/help/edge/docs/forms/universal-editor/assets/universal-editor-mobile.png" alt="Mobile Emulator" style="width: auto; height: auto"></td>
    </tr>
    <tr>
        <td style="width: 20%">Custom Device</td>
        <td style="width: 80%"><img src="/help/edge/docs/forms/universal-editor/assets/universal-editor-custom.png" alt="Custom Device Emulator" style="width: auto; height: auto"></td>
    </tr>
</table>

You can use the **Screen Rotator** icon to toggle between portrait and landscape orientations when previewing a form on different devices. It helps developers test how the responsive design adapts to screen rotations on various devices.

Universal Editor supports the various form layouts. To explore the different layout, refer to the [Layout Capabilities](#layout-capabilities) section.

## Layout Capabilities

Universal Editor allows you to create easy-to-use forms that offer dynamic experiences to end users. The form layout controls how items or components are displayed in an form.

Universal Editor supports the following types of layouts for forms:
* [Panel layout](#panel-layout)
* [Wizard layout](#wizard-layout)
* [Accordion layout](#accordion-layout)

### Panel Layout

Panel layout is useful for organizing related fields in a way that makes it easier to navigate and find corresponding content. The panel layout arranges form components within distinct, sections or panels in forms. 

![Panel Layout](/help/edge/docs/forms/universal-editor/assets/panel-layout.png)

You can use the [panel component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) to add the panel layout in a form. For detailed instructions on how to configure various properties of the panel component, refer to the [panel component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) article.

### Wizard Layout


The wizard layout helps simplifying a complex form by breaking it into distinct steps. Each step represents a different part of the process, and users navigate through the steps sequentially, often with **Next** and **Back** buttons. You can use the wizard layout to create a form that involves multiple sections or steps.

![Wizard Layout](/help/edge/docs/forms/universal-editor/assets/wizard-layout.png)

You can use the [wizard component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) to add the wizard layout in a form. For detailed instructions on how to configure the various properties of the wizard component, refer to the [wizard component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) article.

### Accordion Layout

The accordion layout displays content in collapsible sections or panels in an Adaptive Form. When a section is expanded, it displays the content within, while other sections remain collapsed. This layout is ideal for displaying large amounts of information in a compact form.

![Accordion Layout](/help/edge/docs/forms/universal-editor/assets/accordion-layout.png)

You can use the [accordion component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) to add the accordion layout in a form. For detailed instructions on how to configure the various properties of the accordion component, refer to the [accordion component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) article.

### How to choose the right layout?

It is important to select the right layout to optimize user experience and form functionality. The table helps you understand the different layout options available and guides you in selecting the most suitable layout based on your specific needs and use cases:

| Feature              | Panel Layout                                    | Wizard Layout                                   | Accordion Layout                                 |
|----------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| **Purpose**         | Groups related content into distinct sections  | Guides users through a multi-step process or form | Organizes content into collapsible sections  |
| **Structure**       | Distinct sections                              | Sequential steps/pages                         | Collapsible panels/sections                   |
| **Navigation**      | Click on the panel headers to navigate         | - Forward: “Next” button<br>- Backward: “Back” button<br>- Optional skipping steps | Click headers to expand/collapse sections  |
| **User Experience** | Organizes large amounts of content in a manageable way | Step-by-step guidance, reducing overwhelm | Compact view with expanded/collapsed sections |
| **Use Case**        | Complex forms with categorized sections        | Setup processes, complex forms                | FAQs, settings menus, detailed content sections |

## See also

{{universal-editor-see-also}}



