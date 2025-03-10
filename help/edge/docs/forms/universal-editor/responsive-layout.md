---
title: Understanding Universal Editor - Responsive mode
description: This article explains how to preview forms using different emulators in the Universal Editor to visualize their look and feel during authoring.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: 0c7fb491-4bad-4202-a472-87e6e6d9ab40
---

# Responsive Mode in WYSIWYG Authoring

<span class="preview"> This feature is available through the early access program. To request access, send an email with your GitHub organization name and repository name from your official address to <a href="mailto:aem-forms-ea@adobe.com">aem-forms-ea@adobe.com</a> . For example, if the repository URL is https://github.com/adobe/abc, the organization name is adobe and the repository name is abc.</span> 

## Introduction to Responsive Forms

In today's multi-device world, your forms need to look great and function well on screens of all sizes - from desktop monitors to smartphones. The responsive mode in Universal Editor helps you achieve this by letting you preview and test your forms across different device sizes during the authoring process.

The [Universal Editor](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) enables you to create forms that automatically adapt to different screen sizes, providing an optimal user experience regardless of the device being used.

## Preview Forms in Responsive Mode for Different Devices 

The Universal Editor provides an **Emulator** icon located at the top-right corner of the screen that allows you to preview pages across different device sizes and test the behavior of your responsive design for a better user experience.

To preview a form in responsive mode:

1. Open the form in Universal editor for editing.
2. Click the ![Emulator icon showing a device preview symbol](/help/edge/docs/forms/universal-editor/assets/emulator.png){height=2%,width=2%} icon in the toolbar.
3. Select a device format:
   - Desktop (default)
   - Tablet
   - Mobile 
   - Custom (specify width and height)

![Screenshot of Universal Editor showing responsive mode options for different devices](/help/edge/docs/forms/universal-editor/assets/universal-editor-emulator.png)

You can also use the **Screen Rotator** icon to toggle between portrait and landscape orientations when previewing on tablet or mobile devices.

The Universal Editor provides different emulators to preview forms on various devices. The table below lists the available emulator types along with their corresponding device representations:

<table border="1" style= text-align: left; border-collapse: collapse;">
    <tr>
        <th style="width: 20%">Type of Emulator</th>
        <th style="width: 80%">Device Image</th>
    </tr>
    <tr>
        <td style="width: 20%">Desktop</td>
        <td style="width: 80%"><img src="/help/edge/docs/forms/universal-editor/assets/universal-editor-desktop.png" alt="Desktop view of a form showing full-width layout" style="width: auto; height: auto"></td>
    </tr>
    <tr>
        <td style="width: 20%">Tablet</td>
        <td style="width: 80%"><img src="/help/edge/docs/forms/universal-editor/assets/universal-editor-tab.png" alt="Tablet view of a form showing medium-width layout with adjusted components" style="width: auto; height: auto"></td>
    </tr>
    <tr>
        <td style="width: 20%">Mobile</td>
        <td style="width: 80%"><img src="/help/edge/docs/forms/universal-editor/assets/universal-editor-mobile.png" alt="Mobile view of a form showing narrow layout with stacked components" style="width: auto; height: auto"></td>
    </tr>
    <tr>
        <td style="width: 20%">Custom Device</td>
        <td style="width: 80%"><img src="/help/edge/docs/forms/universal-editor/assets/universal-editor-custom.png" alt="Custom device view of a form with user-specified dimensions" style="width: auto; height: auto"></td>
    </tr>
</table>

## Layout Capabilities

Universal Editor allows you to create easy-to-use forms that offer dynamic experiences to end users. The form layout controls how items or components are displayed in a form.

Universal Editor supports the following types of layouts for forms:

- [Panel layout](#panel-layout)
- [Wizard layout](#wizard-layout)
- [Accordion layout](#accordion-layout)

### Panel Layout

Panel layout is useful for organizing related fields in a way that makes it easier to navigate and find corresponding content. The panel layout arranges form components within distinct sections or panels in forms. 

![Panel layout showing multiple distinct sections within a form](/help/edge/docs/forms/universal-editor/assets/panel-layout.png)

**Example:** A job application form might use panels to separate "Personal Information," "Education," "Work Experience," and "References" into distinct sections.

**Responsive behavior:** On smaller screens, panels typically stack vertically, maintaining their distinct groupings while adjusting to the narrower width.

You can use the [panel component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) to add the panel layout in a form. For detailed instructions on how to configure various properties of the panel component, refer to the [panel component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) article.

### Wizard Layout

The wizard layout helps simplify a complex form by breaking it into distinct steps. Each step represents a different part of the process, and users navigate through the steps sequentially, often with **Next** and **Back** buttons. You can use the wizard layout to create a form that involves multiple sections or steps.

![Wizard layout showing a multi-step form with navigation controls](/help/edge/docs/forms/universal-editor/assets/wizard-layout.png)

**Example:** An insurance claim form might use a wizard to guide users through providing incident details, uploading evidence, entering personal information, and reviewing the submission.

**Responsive behavior:** On mobile devices, the wizard maintains its step-by-step approach but adjusts the content within each step to fit the narrower screen, often stacking elements that would appear side-by-side on larger screens.

You can use the [wizard component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) to add the wizard layout in a form. For detailed instructions on how to configure the various properties of the wizard component, refer to the [wizard component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) article.

### Accordion Layout

The accordion layout displays content in collapsible sections or panels in an Adaptive Form. When a section is expanded, it displays the content within, while other sections remain collapsed. This layout is ideal for displaying large amounts of information in a compact form.

![Accordion layout showing expandable sections in a form](/help/edge/docs/forms/universal-editor/assets/accordion-layout.png)

**Example:** A product configuration form might use accordion sections for "Basic Options," "Advanced Features," "Accessories," and "Payment Plans," allowing users to focus on one aspect at a time.

**Responsive behavior:** Accordions work particularly well on mobile devices as they naturally conserve vertical space by showing only the expanded content section, making them ideal for smaller screens.

You can use the [accordion component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) to add the accordion layout in a form. For detailed instructions on how to configure the various properties of the accordion component, refer to the [accordion component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) article.

### How to choose the right layout?

It is important to select the right layout to optimize user experience and form functionality. The table helps you understand the different layout options available and guides you in selecting the most suitable layout based on your specific needs and use cases:

| Feature              | Panel Layout                                    | Wizard Layout                                   | Accordion Layout                                 |
|----------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| **Purpose**         | Groups related content into distinct sections  | Guides users through a multi-step process or form | Organizes content into collapsible sections  |
| **Structure**       | Distinct sections                              | Sequential steps/pages                         | Collapsible panels/sections                   |
| **Navigation**      | Click on the panel headers to navigate         | - Forward: "Next" button<br>- Backward: "Back" button<br>- Optional skipping steps | Click headers to expand/collapse sections  |
| **User Experience** | Organizes large amounts of content in a manageable way | Step-by-step guidance, reducing overwhelm | Compact view with expanded/collapsed sections |
| **Use Case**        | Complex forms with categorized sections        | Setup processes, complex forms                | FAQs, settings menus, detailed content sections |
| **Best for mobile** | Moderate - panels stack vertically             | Good - keeps focus on current step only        | Excellent - conserves space with collapsible sections |

## Best Practices for Responsive Forms

To ensure your forms provide the best experience across all devices, follow these best practices:

1. **Design for mobile first:** Start by designing your form for mobile devices, then enhance for larger screens. This approach ensures the core functionality works on the smallest screens.

2. **Use appropriate field types:** Choose field types that work well on touch devices:
   - Use dropdowns instead of radio buttons when there are many options
   - Use date pickers designed for touch input
   - Ensure buttons and touch targets are at least 44px x 44px

3. **Simplify for smaller screens:**
   - Display fewer fields per row on mobile devices
   - Consider hiding optional fields behind a "Show more" option
   - Break complex forms into more steps on mobile

4. **Test thoroughly:** Always test your forms on actual devices or using the emulator mode in Universal Editor to ensure they function properly across screen sizes.

5. **Consider loading times:** Optimize image sizes and minimize required resources, especially for mobile users who may have slower connections.

## Troubleshooting Responsive Forms

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Form appears cut off on mobile devices | Fixed width settings or overflow issues | Use relative units (%, rem) instead of pixels, and check for overflow:hidden properties |
| Touch elements difficult to interact with | Touch targets too small or too close together | Increase button/input size to at least 44px x 44px and add more space between interactive elements |
| Content overflows on small screens | No responsive rules for smaller viewports | Add media queries or responsive classes to adjust layout for different screen sizes |
| Form too slow on mobile devices | Large images or excessive scripts | Optimize images, minimize JavaScript, and consider lazy loading for non-critical elements |
| Different appearance between emulator and real devices | Browser-specific rendering or device variations | Test on actual devices when possible, not just emulators |

## See also

{#see-more-eds-forms}
