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

Users access forms on a wide range of devices, including desktops, tablets, and smartphones. Designing responsive forms ensures an optimal experience for all users, regardless of device. This guide explains how to design, test, and optimize forms for any screen size using the Universal Editor.


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

**Purpose:** Organizes related content into visually distinct sections that can be viewed simultaneously.

![Panel Layout Example](/help/edge/docs/forms/universal-editor/assets/panel-layout.png)

**Responsive Behavior:**

- **Desktop (1200px+):** Panels display side-by-side or in a grid
- **Tablet (768px–1199px):** Panels stack vertically with spacing
- **Mobile (320px–767px):** Single-column layout with clear section breaks

**Implementation Steps:**

1. Use the [Panel Component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel).
2. Group related fields within each panel.
3. Add clear headings for each section.
4. Ensure adequate spacing between panels.

**Best Practices:**

- Limit to 3–4 panels on desktop to avoid overwhelming users.
- Use descriptive titles for each panel.
- Group related fields logically to reduce cognitive load.
- Test panel navigation on touch devices.

**Example Use Cases:**

- **Job Application:** Personal Info, Education, Experience, References
- **Product Registration:** Basic Details, Technical Specs, Warranty Info
- **Survey Forms:** Demographics, Preferences, Feedback, Contact

### Wizard Layout

**Purpose:** Guides users through complex processes step-by-step, reducing cognitive load and improving completion rates.

![Wizard Layout Example](/help/edge/docs/forms/universal-editor/assets/wizard-layout.png)

**Responsive Behavior:**

- **All Devices:** Maintains single-step focus for optimal mobile experience.
- **Step Content:** Adapts within each step (stacking or side-by-side).
- **Navigation:** Touch-friendly buttons with sufficient spacing.
- **Progress Indicator:** Scales appropriately for screen size.

**Implementation Steps:**

1. Use the [Wizard Component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard).
2. Break complex forms into logical steps (3–7 steps is optimal).
3. Include progress indicators for user orientation.
4. Provide clear navigation controls (Next, Back, Save).

**Mobile Optimization:**

- Use large touch targets (minimum 44px) for navigation buttons.
- Ensure step indicators are clear and visible on small screens.
- Limit the number of fields per step to reduce scrolling.
- Enable auto-save to prevent data loss.

**Best Practices:**

- Ensure logical step progression—each step should build on the previous.
- Use clear step titles so users know what to expect.
- Validate input at each step to catch errors early.
- Allow users to navigate backward to review or edit information.

**Example Use Cases:**

- **Insurance Claims:** Incident → Evidence → Personal → Review
- **Account Setup:** Basic Info → Preferences → Security → Confirmation
- **Order Process:** Products → Shipping → Payment → Summary

### Accordion Layout

**Purpose:** Saves space by organizing content into collapsible sections, ideal for optional or secondary information.

![Accordion Layout Example](/help/edge/docs/forms/universal-editor/assets/accordion-layout.png)

**Responsive Behavior:**

- **Excellent mobile performance:** Only relevant content is shown.
- **Touch-optimized headers:** Easy to tap and expand sections.
- **Smooth animations:** Provide visual feedback for interactions.
- **Space efficient:** Minimizes scrolling on all devices.

**Implementation Steps:**

1. Use the [Accordion Component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion).
2. Group related optional content in each section.
3. Use descriptive section headers.
4. Set appropriate default open/closed states.

**Mobile Advantages:**

- Reduces scrolling by collapsing unused sections.
- Touch-friendly interaction with natural expand/collapse gestures.
- Faster loading—only active content is visible.
- Improved focus—users see only what they need.

**Best Practices:**

- Use clear section headers so users know what's inside before expanding.
- Group related content logically within each section.
- Set important sections to start expanded if needed.
- Provide brief section previews to help users decide what to expand.

**Example Use Cases:**

- **Product Configuration:** Basic → Advanced → Accessories → Support
- **FAQ Forms:** Account → Billing → Technical → General
- **Settings Forms:** Privacy → Notifications → Appearance → Advanced

## Part 3: Responsive Design Best Practices

### Best Practices by Device Type

+++Mobile Optimization (320px–767px)

**Essential Practices:**

- Use a single-column layout for all content.
- Provide large, touch-friendly buttons (minimum 44px height).
- Simplify navigation with clear back/next options.
- Minimize scrolling within each section.
- Auto-focus on the first field to display the keyboard.

**Field-Specific Guidelines:**

- **Text inputs:** Full width with ample padding.
- **Dropdowns:** Use native select elements for better touch experience.
- **Date pickers:** Use native date inputs for mobile compatibility.
- **File uploads:** Provide large, clear upload areas.

+++

+++Tablet Optimization (768px–1199px)

**Layout Strategies:**

- Use two-column layouts for related fields.
- Test both portrait and landscape orientations.
- Support both touch and mouse interactions.
- Provide larger content areas while maintaining readability.

+++

+++Desktop Optimization (1200px+)

**Advanced Features:**

- Use multi-column layouts for efficient space usage.
- Offer keyboard shortcuts for power users.
- Implement hover states for interactive feedback.
- Provide advanced validation with detailed error messages.

+++

## Comprehensive Troubleshooting

### Layout Issues

+++Form Layout Breaks on Mobile

**Common Causes:**

- Fixed-width elements that do not scale
- CSS designed for desktop-first layouts
- Images or content that overflow their containers

**Solutions:**

- Ensure images and containers scale to screen size.
- Use a mobile-first design with progressive enhancement.
- Test with both device emulators and real devices.
- Use flexible sizing instead of fixed dimensions.

+++

+++Touch Targets Too Small

**Common Causes:**

- Buttons smaller than 44px × 44px
- Interactive elements placed too close together
- Custom CSS overriding touch-friendly defaults

**Solutions:**

- Ensure all interactive elements are at least 44px × 44px.
- Add spacing between buttons and links.
- Test touch interaction with actual fingers, not just a mouse.
- Increase touch target areas for easier tapping.

+++

+++Content Overflow Issues

**Common Causes:**

- Long text or labels that do not wrap
- Fixed-width containers
- Images that do not scale properly

**Solutions:**

- Enable text wrapping for long content.
- Use responsive images that scale appropriately.
- Implement flexible layouts that adapt to content.
- Test with various content lengths.

+++

### Performance Issues

+++Slow Loading on Mobile

**Common Causes:**

- Large images not optimized for mobile
- Excessive JavaScript execution
- Too many form fields loading at once

**Solutions:**

- Optimize images for different screen sizes.
- Load non-critical content only when needed.
- Use techniques to speed up mobile loading.
- Minimize third-party scripts and widgets.

+++

### Testing and Validation Issues

+++Emulator vs. Real Device Differences

**Common Causes:**

- Browser-specific rendering differences
- Touch versus mouse interaction differences
- Network speed variations

**Solutions:**

- Test on actual devices whenever possible.
- Use multiple browsers for emulator testing.
- Simulate different network speeds during testing.
- Validate with real users in target environments.

+++

## Success Metrics for Responsive Forms

+++Key Performance Indicators

**User Experience Metrics:**

- **Form completion rate:** Target 85%+ on mobile
- **Time to complete:** Mobile completion time should be within 20% of desktop
- **Error rate:** Less than 5% validation errors
- **Abandonment points:** Identify where users drop off

**Technical Performance:**

- **Page load time:** Under 3 seconds on 3G networks
- **Core Web Vitals:** Pass all Google performance benchmarks
- **Accessibility score:** WCAG 2.1 AA compliance
- **Cross-browser compatibility:** 98%+ functionality across major browsers

+++

+++Testing Checklist

**Before Publishing:**

- Test the form on actual mobile devices.
- Ensure all touch targets are at least 44px × 44px.
- Verify text readability at all screen sizes.
- Confirm form validation works across all devices.
- Ensure loading time is under 3 seconds on mobile.
- Check that all interactive elements are accessible.
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


