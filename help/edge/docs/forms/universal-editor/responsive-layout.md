---
title: Create Responsive Forms with Universal Editor
description: Learn how to design, test, and optimize responsive forms for all devices using Universal Editor. Master device testing, layout patterns, and mobile optimization techniques for AEM Forms with Edge Delivery Services.
keywords: responsive forms, mobile forms, device testing, universal editor, adaptive layout, form optimization, mobile design, responsive design, form layouts, device emulator
feature: Edge Delivery Services
role: User, Developer
level: Beginner
exl-id: 0c7fb491-4bad-4202-a472-87e6e6d9ab40
---

# Create Responsive Forms with Universal Editor

The modern web landscape demands forms that function seamlessly across an ever-expanding spectrum of devices and screen sizes. From large desktop monitors to compact smartphone screens, users expect consistent, intuitive experiences regardless of their chosen device. Creating responsive forms is no longer optional—it's a fundamental requirement for delivering professional, accessible, and conversion-optimized digital experiences.

Universal Editor provides comprehensive tools and methodologies for developing responsive forms that adapt intelligently to various screen dimensions, input methods, and user contexts. This guide explores the technical foundations, implementation strategies, and optimization techniques necessary to create forms that perform exceptionally across all devices while maintaining usability, accessibility, and visual appeal.

Responsive form creation involves two main activities:

- **Responsive Testing:** Preview and test your forms across various screen sizes using device emulators.
- **Responsive Design:** Select and implement layout patterns that adapt seamlessly to different devices.

**In this guide, you will learn how to:**

- Test forms on desktop, tablet, and mobile devices
- Select appropriate layout patterns for your content
- Apply responsive design best practices
- Troubleshoot common responsive form issues
- Optimize forms for mobile performance

## Why Responsive Forms Are Important

**User Experience Impact:**

- Over 60% of users access forms on mobile devices
- Poor mobile experiences result in a 67% higher abandonment rate
- Responsive forms can increase completion rates by up to 25%

**Business Benefits:**

- Higher form completion rates
- Improved user satisfaction
- Enhanced accessibility compliance
- Lower development and maintenance costs

>[!TIP]
>
> **Mobile-First Approach:** Begin designing for mobile devices, then enhance for larger screens. This ensures core functionality works in the most constrained environment.

## Part 1: Testing Forms Across Devices

Testing your forms on different devices helps you identify and resolve responsive issues before users encounter them. The Universal Editor provides an emulator mode to simulate various screen sizes and orientations.

### How to Test Your Forms

**Step 1: Open the Device Emulator**

1. Open your form in the Universal Editor.
2. Click the ![Emulator icon](/help/edge/docs/forms/universal-editor/assets/emulator.png){height=2%,width=2%} **Emulator** icon in the toolbar.
3. The device selector menu will appear.

![Universal Editor Responsive Testing Interface](/help/edge/docs/forms/universal-editor/assets/universal-editor-emulator.png)

**Step 2: Select a Device for Testing**

- **Desktop** (1200px+ width): Default editing view
- **Tablet** (768px–1199px width): Medium screen testing
- **Mobile** (320px–767px width): Small screen testing
- **Custom**: Specify exact dimensions for specific devices

**Step 3: Test Device Orientations**

Use the **Screen Rotator** icon to test both:

- **Portrait mode**: Standard mobile orientation
- **Landscape mode**: Rotated tablet or phone view

### Device Testing Results

Each device type reveals unique responsive behaviors:

| **Device Type** | **Screen Width** | **What to Check** | **Common Issues** |
|-----------------|------------------|-------------------|-------------------|
| **Desktop**     | 1200px+          | Full layout, all features visible | Excessive whitespace, overly wide layouts |
| **Tablet**      | 768px–1199px     | Component stacking, navigation usability | Awkward sizing, touch target issues |
| **Mobile**      | 320px–767px      | Single-column layout, thumb navigation | Small text, closely spaced buttons |
| **Custom**      | User-defined     | Device-specific requirements | Breakpoint edge cases |

### Visual Examples by Device

**Desktop View (1200px+):**
![Desktop form view](/help/edge/docs/forms/universal-editor/assets/universal-editor-desktop.png)
*Full-width layout with side-by-side form fields.*

**Tablet View (768px–1199px):**
![Tablet form view](/help/edge/docs/forms/universal-editor/assets/universal-editor-tab.png)
*Medium-width layout with adjusted component spacing.*

**Mobile View (320px–767px):**
![Mobile form view](/help/edge/docs/forms/universal-editor/assets/universal-editor-mobile.png)
*Single-column layout with stacked components.*

**Custom Device View:**
![Custom device view](/help/edge/docs/forms/universal-editor/assets/universal-editor-custom.png)
*User-specified dimensions for targeted testing.*

### Testing Workflow

**For New Forms:**

1. **Build in desktop view:** Start with full functionality.
2. **Test on tablet:** Check adaptations for medium screens.
3. **Validate on mobile:** Ensure usability on small screens.
4. **Fix responsive issues:** Adjust layouts as needed.
5. **Retest all devices:** Confirm fixes across all sizes.

**For Existing Forms:**

1. **Quick mobile check:** Does the form work on phones?
2. **Identify problem areas:** Note layout and usability issues.
3. **Systematic testing:** Test each device size thoroughly.
4. **Document issues:** Track what needs to be fixed.
5. **Implement fixes:** Address issues methodically.

## Part 2: Selecting Responsive Layout Patterns

Layout patterns determine how your form content adapts to different screen sizes. The right pattern improves both user experience and mobile performance.

### Layout Pattern Overview

| **Layout Type**     | **Best For**                              | **Mobile Performance** | **Complexity** |
|---------------------|-------------------------------------------|------------------------|----------------|
| **Panel Layout**    | Categorized content, dashboard-style forms| Good                   | Low            |
| **Wizard Layout**   | Multi-step processes, complex workflows   | Excellent              | Medium         |
| **Accordion Layout**| FAQ-style content, optional sections      | Excellent              | Low            |

### Quick Decision Guide

**Use Panel Layout when:**

- Your content is divided into distinct categories
- Users need to view multiple sections at once
- The content is relatively simple

**Use Wizard Layout when:**

- The form has multiple logical steps
- You want to reduce cognitive load
- Mobile users are a primary audience

**Use Accordion Layout when:**

- The form contains optional or secondary content
- Space conservation is important
- Content can be logically grouped

### Panel Layout

The Panel Layout organizes related content into visually distinct sections, allowing users to view multiple sections at once. This layout is ideal for forms with categorized information that benefits from a side-by-side presentation on larger screens.

![Panel Layout Example](/help/edge/docs/forms/universal-editor/assets/panel-layout.png)

**Responsive Behavior**

- **Desktop (1200px and above):** Panels are displayed side-by-side or in a grid for maximum visibility.
- **Tablet (768px–1199px):** Panels stack vertically with appropriate spacing to maintain clarity.
- **Mobile (320px–767px):** Panels are presented in a single-column layout, with clear separation between sections for easy navigation.

**How to Implement**

1. Add the [Panel Component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) to your form.
2. Group related fields within each panel to maintain logical organization.
3. Assign clear, descriptive headings to each panel section.
4. Ensure there is sufficient spacing between panels to prevent visual clutter.

**Best Practices**

- Limit the number of panels to 3 or 4 on desktop to avoid overwhelming users.
- Use concise, descriptive titles for each panel to aid user understanding.
- Organize fields within panels logically to minimize cognitive load.
- Test panel navigation on touch devices to ensure usability across all platforms.

**Common Use Cases**

- **Job Application:** Sections for Personal Information, Education, Experience, and References.
- **Product Registration:** Panels for Basic Details, Technical Specifications, and Warranty Information.
- **Survey Forms:** Groupings for Demographics, Preferences, Feedback, and Contact Information.

### Wizard Layout

The Wizard Layout guides users through a multi-step process, presenting one section at a time. This layout is especially effective for complex forms, as it reduces cognitive load and increases completion rates by breaking the process into manageable steps.

![Wizard Layout Example](/help/edge/docs/forms/universal-editor/assets/wizard-layout.png)

**Responsive Behavior**

- **All Devices:** Maintains a single-step focus, which is optimal for mobile users.
- **Step Content:** Each step adapts responsively, stacking fields or arranging them side-by-side as appropriate for the screen size.
- **Navigation:** Features touch-friendly buttons with adequate spacing for easy interaction.
- **Progress Indicator:** Progress bars or step indicators scale appropriately for different devices, providing clear feedback on completion status.

**How to Implement**

1. Insert the [Wizard Component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) into your form.
2. Divide the form into logical steps, ideally between 3 and 7, to keep each step focused and manageable.
3. Add progress indicators to help users understand their position in the process.
4. Provide clear navigation controls, such as Next, Back, and Save buttons.

**Mobile Optimization Tips**

- Use large touch targets (at least 44px in height) for navigation controls to enhance accessibility.
- Ensure that step indicators are visible and legible on small screens.
- Limit the number of fields per step to minimize scrolling and improve focus.
- Enable auto-save functionality to prevent data loss if users leave the form.

**Best Practices**

- Design steps to follow a logical progression, with each step building on the previous one.
- Use clear, descriptive titles for each step to set user expectations.
- Validate user input at each step to catch errors early and reduce frustration.
- Allow users to navigate backward to review or edit previous information without losing data.

**Common Use Cases**

- **Insurance Claims:** Steps for Incident Details, Evidence Submission, Personal Information, and Review.
- **Account Setup:** Stages for Basic Information, Preferences, Security Settings, and Confirmation.
- **Order Process:** Steps for Product Selection, Shipping Information, Payment Details, and Order Summary.

### Accordion Layout

The Accordion Layout saves space by organizing content into collapsible sections, making it ideal for optional or secondary information. This layout is particularly effective for forms with content that can be logically grouped and does not need to be displayed all at once.

![Accordion Layout Example](/help/edge/docs/forms/universal-editor/assets/accordion-layout.png)

**Responsive Behavior**

- **Mobile Performance:** Only the relevant section is expanded, reducing the need for scrolling and improving load times.
- **Touch-Optimized Headers:** Section headers are easy to tap and expand, supporting natural gestures on mobile devices.
- **Smooth Animations:** Expanding and collapsing sections provide visual feedback for user interactions.
- **Space Efficiency:** Collapsed sections minimize vertical space, making the form easier to navigate on all devices.

**How to Implement**

1. Add the [Accordion Component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) to your form.
2. Group related optional or secondary content within each accordion section.
3. Use clear, descriptive headers for each section to help users understand what information is contained within.
4. Set appropriate default open or closed states for each section based on importance and user needs.

**Mobile Advantages**

- Reduces scrolling by collapsing unused sections, allowing users to focus on one section at a time.
- Touch-friendly interaction supports natural expand/collapse gestures.
- Faster loading, as only the active content is visible.
- Improved focus, since users see only the information they need at any given time.

**Best Practices**

- Use clear section headers so users know what to expect before expanding a section.
- Group related content logically within each section to aid comprehension.
- Set important sections to start expanded if immediate attention is required.
- Provide brief section previews or summaries to help users decide which sections to expand.

**Common Use Cases**

- **Product Configuration:** Sections for Basic Options, Advanced Settings, Accessories, and Support.
- **FAQ Forms:** Groupings for Account, Billing, Technical, and General questions.
- **Settings Forms:** Sections for Privacy, Notifications, Appearance, and Advanced options.


## Part 3: Responsive Design Best Practices

### Best Practices by Device Type

+++Mobile Optimization (320px–767px)

**Layout and Interaction:**

- Use a single-column layout for all form content to maximize readability and ease of use.
- Ensure all buttons and interactive elements are at least 44px in height for reliable touch interaction.
- Provide clear, simple navigation with visible back and next buttons.
- Minimize the need for scrolling within each section by breaking up long forms.
- Automatically focus on the first input field to prompt the mobile keyboard.

**Field Guidelines:**

- Text fields should span the full width of the screen with sufficient padding for touch input.
- Use native dropdown/select elements for optimal mobile usability.
- Implement native date pickers for consistent mobile experience.
- Make file upload areas large and clearly labeled for easy access.

+++

+++Tablet Optimization (768px–1199px)

**Layout and Usability:**

- Utilize two-column layouts for related fields to take advantage of increased screen space.
- Test form appearance and usability in both portrait and landscape orientations.
- Design for both touch and mouse input, ensuring all controls are easily accessible.
- Increase content area size while maintaining clear visual hierarchy and readability.

+++

+++Desktop Optimization (1200px+)

**Advanced Features and Layout:**

- Use multi-column layouts to efficiently use horizontal space and reduce vertical scrolling.
- Provide keyboard shortcuts for frequent actions to support power users.
- Implement hover states and visual feedback for interactive elements.
- Offer advanced validation with clear, detailed error messages for complex forms.

+++

## Comprehensive Troubleshooting

### Layout Issues

+++Form Layout Breaks on Mobile

**Possible Causes:**

- Fixed-width elements that do not adapt to smaller screens
- Desktop-first CSS that overrides mobile styles
- Images or content overflowing their containers

**How to Fix:**

- Make sure all images and containers use relative or percentage-based sizing.
- Start with a mobile-first CSS approach and layer on enhancements for larger screens.
- Test forms using both device emulators and real devices.
- Avoid fixed dimensions; use flexible layouts.

+++

+++Touch Targets Too Small

**Possible Causes:**

- Buttons or links smaller than 44px by 44px
- Interactive elements placed too close together
- Custom CSS reducing default touch target size

**How to Fix:**

- Ensure every interactive element is at least 44px by 44px.
- Add adequate spacing between buttons, links, and other controls.
- Test with real touch devices, not just a mouse.
- Expand touch target areas as needed for accessibility.

+++

+++Content Overflow Issues

**Possible Causes:**

- Long text or labels that do not wrap
- Containers with fixed widths
- Images that do not scale responsively

**How to Fix:**

- Enable text wrapping for all labels and content.
- Use responsive images that scale with the container.
- Design flexible layouts that adapt to varying content lengths.
- Test with both short and long content to ensure adaptability.

+++

### Performance Issues

+++Slow Loading on Mobile

**Possible Causes:**

- Large, unoptimized images
- Heavy or excessive JavaScript
- Too many form fields loading simultaneously

**How to Fix:**

- Optimize images for mobile and use appropriate file formats.
- Defer or lazy-load non-critical content.
- Minimize the use of third-party scripts and widgets.
- Streamline form fields to load only what is necessary.

+++

### Testing and Validation Issues

+++Emulator vs. Real Device Differences

**Possible Causes:**

- Differences in browser rendering engines
- Touch interaction not accurately simulated by mouse
- Network speed discrepancies

**How to Fix:**

- Always test on real devices in addition to emulators.
- Use multiple browsers and devices for comprehensive testing.
- Simulate various network speeds to identify performance bottlenecks.
- Gather feedback from real users in your target audience.

+++

## Success Metrics for Responsive Forms

+++Key Performance Indicators

**User Experience:**

- **Form completion rate:** Aim for 85% or higher on mobile devices.
- **Time to complete:** Mobile users should complete forms within 20% of desktop completion times.
- **Error rate:** Keep validation errors below 5%.
- **Abandonment points:** Identify and address steps where users drop off.

**Technical Performance:**

- **Page load time:** Less than 3 seconds on a 3G connection.
- **Core Web Vitals:** Meet or exceed Google's recommended thresholds.
- **Accessibility:** Achieve WCAG 2.1 AA compliance.
- **Browser compatibility:** Ensure 98%+ functionality across all major browsers.

+++

+++Testing Checklist

**Pre-Publication Checklist:**

- Test the form on actual mobile devices (not just emulators).
- Ensure all touch targets are at least 44px × 44px.
- Verify text readability at all supported screen sizes.
- Confirm form validation works consistently across devices and browsers.
- Ensure mobile loading time is under 3 seconds.
- Check that all interactive elements are accessible via keyboard and screen readers.
- Test form submission on all supported devices.


+++

## Next Steps

**Immediate Actions:**

1. **Audit your current forms:** Test existing forms using the device emulator.
2. **Identify quick wins:** Fix obvious mobile usability issues first.
3. **Prioritize high-traffic forms:** Focus on forms with the most user impact.
4. **Implement a mobile-first approach:** Start with the smallest screen design.

**Advanced Optimization:**

- **Performance monitoring:** Set up analytics to track form metrics.
- **A/B testing:** Experiment with different layouts and approaches.
- **User feedback collection:** Gather insights from real users.
- **Continuous improvement:** Regularly review and optimize forms.


