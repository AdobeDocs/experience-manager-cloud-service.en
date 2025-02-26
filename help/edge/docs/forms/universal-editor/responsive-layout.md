---
title: Understanding Universal Editor - Responsive mode
description: This article explains how to preview forms using different emulators in the Universal Editor to visualize their look and feel during authoring.
feature: Edge Delivery Services
role: Admin, Architect, Developer
---
# Responsive Mode in WYSIWYG Authoring

<span class="preview"> This feature is available through the early access program. To request access, send an email from your official address to <a href="mailto:aem-forms-ea@adobe.com">aem-forms-ea@adobe.com</a> with your GitHub organization name and repository name. For example, if the repository URL is https://github.com/adobe/abc, the organization name is adobe and the repository name is abc.</span> 


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

## See also

{{universal-editor-see-also}}
