---
title: Customize theme and style for an Edge Delivery Services for AEM Forms
description: Effectively customize the theme and style for AEM Forms delivered via Edge Delivery Services, ensuring a cohesive and branded user experience.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: ac780399-34fe-457d-aaf4-b675656c024d
---
# Customize the look of your forms

Form styling in Edge Delivery Services for AEM Forms requires a sophisticated understanding of CSS custom properties, block-based architecture, and component-specific targeting strategies. Unlike traditional form styling approaches, the Adaptive Forms Block implements a systematic design token system that enables consistent theming while maintaining the performance and accessibility benefits of Edge Delivery Services.

The Adaptive Forms Block architecture generates standardized HTML structures across all form components, creating predictable patterns for CSS targeting and customization. This consistency enables developers to implement comprehensive styling systems that scale across complex form implementations while preserving the block-based performance optimizations that make Edge Delivery Services exceptionally fast.

This comprehensive guide covers the technical foundations of form styling within the Edge Delivery Services ecosystem, including CSS custom property systems, component HTML structure patterns, and advanced styling techniques. The documentation provides both theoretical understanding and practical implementation guidance for creating sophisticated, branded form experiences.

## What You'll Master

**CSS Custom Properties Mastery**: Understand the complete variable system that controls form appearance, including color schemes, typography scales, spacing systems, and layout parameters. Learn how to override and extend these properties to implement comprehensive brand themes.

**Component Architecture Understanding**: Gain deep knowledge of the HTML structure patterns used by each form component type, enabling precise CSS targeting and customization without breaking the underlying functionality or accessibility features.

**Advanced Styling Techniques**: Implement sophisticated styling patterns including state-based styling, responsive design integration, and performance-optimized customization strategies that maintain the fast-loading characteristics of Edge Delivery Services.

**Professional Implementation Strategies**: Learn industry-standard approaches to form styling including design system integration, maintainable CSS architecture, and troubleshooting techniques for complex styling scenarios.

## Understanding Form Field Types

Before diving into styling, let's review the common form [field types](/help/edge/docs/forms/universal-editor/create-custom-component.md#supported-fieldtypes) supported by the Adaptive Forms Block:

- Input Fields: These include text inputs, email inputs, password inputs, and more.
- Checkbox Groups: Used for selecting multiple options.
- Radio Groups: Used for selecting only one option from a group.
- Dropdowns: Also known as select boxes, used for selecting one option from a list.
- Panels/Containers: Used to group related form elements together.

## Basic Styling Principles

Understanding [fundamental CSS concepts](https://www.w3schools.com/css/css_intro.asp) is crucial before styling specific form fields:

- [Selectors](https://www.w3schools.com/css/css_selectors.asp): CSS Selectors allow you to target specific HTML elements for styling. You can use element selectors, class selectors, or ID selectors.
- [Properties](https://www.w3schools.com/css/css_syntax.asp): CSS properties define the visual appearance of elements. Common properties for styling form fields include color, background-color, border, padding, margin, and more.
- [Box Model](https://www.w3schools.com/css/css_boxmodel.asp): The CSS box model describes the structure of HTML elements as a content area surrounded by padding, borders, and margins.
- Flexbox/Grid: CSS [Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) and [Grid layouts](https://www.w3schools.com/css/css_grid.asp) are powerful tools for creating responsive and flexible designs.




## Comprehensive Form Styling with CSS Custom Properties

The Adaptive Forms Block utilizes a sophisticated CSS architecture built on custom properties (CSS variables) that enables systematic theming and consistent styling across all form components. Understanding this structure is essential for effective form customization and branding.

### Understanding the forms.css Architecture

The default form styles are located in your project repository at `/blocks/form/form.css` and follow a structured approach that prioritizes maintainability, consistency, and customization flexibility. The architecture consists of several key components:

**CSS Custom Properties Foundation**: The styling system is built on CSS custom properties defined at the `:root` level, providing a centralized theming system that cascades throughout all form components. These variables establish design tokens for colors, typography, spacing, and layout properties.

**Block-Based CSS Structure**: Edge Delivery Services employs a block-based architecture where the `.form` class serves as the primary namespace for all form-related styles, ensuring proper scope isolation and preventing CSS conflicts with other page components.

**Component-Specific Styling**: Individual form components are styled using consistent wrapper patterns (`.{Type}-wrapper`) that provide predictable targeting for different field types while maintaining the overall design system integrity.

### CSS Custom Properties Reference and Customization

The form styling system includes over 50 CSS custom properties that control every aspect of form appearance and behavior. Understanding these properties enables comprehensive customization while maintaining design consistency.

+++ Color and Theming Variables

The color system establishes a complete visual foundation for forms through carefully organized custom properties:

```css
:root {
    /* Primary color system */
    --background-color-primary: #fff;
    --label-color: #666;
    --border-color: #818a91;
    --form-error-color: #ff5f3f;
    
    /* Button color system */
    --button-primary-color: #5F8DDA;
    --button-secondary-color: #666;
    --button-primary-hover-color: #035fe6;
    
    /* Form-specific color applications */
    --form-background-color: var(--background-color-primary);
    --form-input-border-color: var(--border-color);
    --form-invalid-border-color: #ff5f3f;
    --form-label-color: var(--label-color);
}
```

**Practical Customization Example**: To implement a dark theme for your forms, override the base color variables:

```css
:root {
    --background-color-primary: #1a1a1a;
    --label-color: #e0e0e0;
    --border-color: #404040;
    --form-error-color: #ff6b6b;
    --button-primary-color: #4a9eff;
}
```

This single change propagates through all form components because the system uses variable references rather than hardcoded values.

+++

+++ Typography and Spacing Variables

Typography and spacing variables provide comprehensive control over text presentation and layout spacing:

```css
:root {
    /* Font size system */
    --form-font-size-m: 22px;
    --form-font-size-s: 18px;
    --form-font-size-xs: 16px;
    
    /* Component-specific typography */
    --form-label-font-size: var(--form-font-size-s);
    --form-label-font-weight: 400;
    --form-title-font-weight: 600;
    --form-input-font-size: 1rem;
    
    /* Spacing system */
    --form-field-horz-gap: 40px;
    --form-field-vert-gap: 20px;
    --form-input-padding: 0.75rem 0.6rem;
    --form-padding: 0 10px;
}
```

**Practical Customization Example**: To create a more compact form layout with smaller typography:

```css
:root {
    --form-font-size-m: 18px;
    --form-font-size-s: 14px;
    --form-font-size-xs: 12px;
    --form-field-horz-gap: 20px;
    --form-field-vert-gap: 15px;
    --form-input-padding: 0.5rem 0.4rem;
}
```

+++

+++ Layout and Structure Variables

Layout variables control form dimensions, grid behavior, and component arrangement:

```css
:root {
    /* Form layout */
    --form-width: 100%;
    --form-columns: 12;
    --form-submit-width: 100%;
    
    /* Card-based components */
    --form-card-border-radius: 4px;
    --form-card-padding: 0.6rem 0.8rem;
    --form-card-shadow: 0 1px 2px rgb(0 0 0 / 3%);
    --form-card-hover-shadow: 0 2px 4px rgb(0 0 0 / 6%);
    
    /* Wizard-specific layout */
    --form-wizard-padding: 0px;
    --form-wizard-padding-bottom: 160px;
    --form-wizard-step-legend-padding: 10px;
}
```

**Practical Customization Example**: To create a card-style form with enhanced visual depth:

```css
:root {
    --form-card-border-radius: 12px;
    --form-card-padding: 1.5rem 2rem;
    --form-card-shadow: 0 4px 12px rgb(0 0 0 / 8%);
    --form-card-hover-shadow: 0 8px 24px rgb(0 0 0 / 12%);
    --form-background-color: #f8f9fa;
}

.form {
    background: var(--form-background-color);
    border-radius: var(--form-card-border-radius);
    box-shadow: var(--form-card-shadow);
    padding: var(--form-card-padding);
    max-width: 600px;
    margin: 2rem auto;
}
```

+++

### CSS Styling Patterns and Best Practices

The Adaptive Forms Block follows specific CSS patterns that ensure maintainable, performant, and consistent styling across all components.

+++ Primary Styling Patterns

**Block-Level Form Container**: Target the primary form container for overall layout and background styling:

```css
.form {
    /* Form-wide styles */
    max-width: 800px;
    margin: 0 auto;
    background-color: var(--form-background-color);
    padding: var(--form-padding);
    border-radius: var(--form-card-border-radius);
}
```

**Component Wrapper Patterns**: Target specific field types using consistent wrapper classes:

```css
/* Text input fields */
.form .text-wrapper input {
    padding: var(--form-input-padding);
    border: var(--form-input-border-size) solid var(--form-input-border-color);
    font-size: var(--form-input-font-size);
    border-radius: 4px;
    width: 100%;
}

/* Email input fields */
.form .email-wrapper input {
    padding: var(--form-input-padding);
    border: var(--form-input-border-size) solid var(--form-input-border-color);
    font-size: var(--form-input-font-size);
}

/* Button styling */
.form .button-wrapper button {
    background-color: var(--form-button-background-color);
    color: var(--form-button-color);
    padding: var(--form-button-padding);
    border: var(--form-button-border);
    font-size: var(--form-button-font-size);
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.form .button-wrapper button:hover {
    background-color: var(--form-button-background-hover-color);
}
```

+++ 

+++ Advanced Customization Patterns

**Field-Specific Targeting**: Target individual fields by name for unique styling requirements:

```css
/* Style specific fields */
.form .field-email input {
    background-image: url('data:image/svg+xml;...'); /* Email icon */
    background-repeat: no-repeat;
    background-position: right 12px center;
    padding-right: 40px;
}

.form .field-phone input {
    text-align: center;
    letter-spacing: 1px;
    font-family: monospace;
}
```

**State-Based Styling**: Implement validation and interaction states:

```css
/* Validation states */
.form .field-wrapper[data-valid="false"] input {
    border-color: var(--form-error-color);
    box-shadow: 0 0 0 2px rgba(255, 95, 63, 0.1);
}

.form .field-wrapper[data-valid="true"] input {
    border-color: #28a745;
    box-shadow: 0 0 0 2px rgba(40, 167, 69, 0.1);
}

/* Focus states */
.form .text-wrapper input:focus,
.form .email-wrapper input:focus {
    outline: none;
    border-color: var(--button-primary-color);
    box-shadow: 0 0 0 2px rgba(95, 141, 218, 0.2);
}
```

+++


## Components Structure 

The Adaptive Forms Block offers a consistent HTML structure for various form elements, ensuring easier styling and management. You can manipulate the components using CSS for styling purposes.

+++ General Components (except dropdowns, radio groups, and checkbox groups):

All form fields, except for dropdowns, radio groups, and checkbox groups, has the following HTML structure:

#### HTML Structure of General Components

```HTML

  <div class="{Type}-wrapper field-{Name}   field-wrapper" data-required={Required}>
     <label for="{FieldId}" class="field-label">First   Name</label>
     <input type="{Type}" placeholder="{Placeholder}"   maxlength="{Max}" id={FieldId}" name="{Name}"   aria-describedby="{FieldId}-description">
     <div class="field-description" aria-live="polite"  id="{FieldId}-description">
      Hint - First name should be minimum 3 characters  and a maximum of 10 characters.
     </div>
  </div>

```

  - Classes: The div element has several classes for targeting specific elements and styling. You require the `{Type}-wrapper` or `field-{Name}` classes to develop a CSS Selector to style a form field:
  - {Type}: Identifies the component by field type. For example, text (text-wrapper), number (number-wrapper), date (date-wrapper).
  - {Name}: Identifies the component by name. The name of the field can have only alphanumeric characters, the multiple consecutive dashes in the name are replaced with a single dash `(-)`, and starting and ending dashes in a field name are removed. For example, first-name (field-first-name field-wrapper).
  - {FieldId}: It is a unique identifier for the field, automatically generated.
  - {Required}: It is a boolean indicating if the field is required.
  - Label: The `label` element provides a descriptive text for the field and associates it with the input element using the `for` attribute.
  - Input: The `input` element defines the type of data to be entered. For example, text, number, email.
  - Description (Optional): The `div` with class `field-description` provides additional information or instructions for the user.

**Example of HTML Structure**

```HTML

<div class="text-wrapper field-first-name field-wrapper" data-required="true">
  <label for="firstName" class="field-label">First Name</label>
  <input type="text" placeholder="Enter your first name" maxlength="50" id="firstName" name="firstName" aria-describedby="firstName-description">
  <div class="field-description" aria-live="polite" id="firstName-description">
    Please enter your legal first name.
  </div>
</div>

```

#### CSS Selector for General Components

```css
/* Primary Pattern: Target field wrapper by type */
.form .{Type}-wrapper {
    /* Container styling for specific field types */
    margin-bottom: 1rem;
    border-radius: 4px;
}

/* Primary Pattern: Target input fields within wrapper */
.form .{Type}-wrapper input {
    /* Input field styling using CSS custom properties */
    border: var(--form-input-border-size) solid var(--form-input-border-color);
    padding: var(--form-input-padding);
    border-radius: 4px;
    width: 100%;
    font-size: var(--form-input-font-size);
}

/* Context-specific: Target element by field name when higher specificity needed */
.form .field-{Name} input {
    /* Field-specific customizations */
    /* Use this pattern for unique styling requirements */
}
```

  - `.form .{Type}-wrapper`: Targets the field wrapper element based on the field type. For example, `.form .text-wrapper` targets all text field containers.
  - `.form .{Type}-wrapper input`: Targets the actual input elements within the wrapper. This is the recommended pattern for styling form inputs.
  - `.form .field-{Name}`: Targets elements based on the specific field name. For example, `.form .field-first-name` targets the "First Name" field container. Use `.form .field-{Name} input` to target the input element specifically.
  - **Avoid**: `main .form form .{Type}-wrapper` - This creates unnecessary CSS specificity and is harder to maintain.

**Example CSS Selectors for General Components**

```css
/* Primary Pattern: Target all text input fields */
.form .text-wrapper input {
    border: var(--form-input-border-size) solid var(--form-input-border-color);
    padding: var(--form-input-padding);
    border-radius: 4px;
    width: 100%;
    font-size: var(--form-input-font-size);
    background-color: var(--form-input-background-color);
}

/* Context-specific: Target field by name when higher specificity needed */
.form .field-first-name input {
    text-transform: capitalize;
    border-color: var(--button-primary-color);
}

/* Alternative with main context if needed */
main .form .text-wrapper input {
    /* Use only when you need higher specificity */
    color: var(--form-label-color);
}
```

+++

+++ Dropdown Component

For dropdown menus, the `select` element is used instead of an `input` element:

#### HTML Structure of Dropdown Component

```HTML

<div class="{Type}-wrapper field-{Name} field-wrapper" data-required={Required}>
   <label for="{FieldId}" class="field-label">First Name</label>
   <input type="{Type}" placeholder="{Placeholder}" maxlength="{Max}" id={FieldId}" name="{Name}" aria-describedby="{FieldId}-description">
   <div class="field-description" aria-live="polite" id="{FieldId}-description">
    Hint - First name should be minimum 3 characters and a maximum of 10 characters.
   </div>
</div>

```

**Example HTML Structure**

```HTML

<div class="drop-down-wrapper field-country field-wrapper" data-required="true">
  <label for="country" class="field-label">Country</label>
  <select id="country" name="country">
    <option value="">Select Country</option>
    <option value="US">United States</option>
    <option value="CA">Canada</option>
  </select>
  <div class="field-description" aria-live="polite" id="country-description">
    Please select your country of residence.
  </div>
</div>

```

#### CSS Selectors for dropdown component

The following CSS lists some example CSS Selectors for dropdown components.

```css
/* Primary Pattern: Target the dropdown wrapper */
.form .drop-down-wrapper {
    /* Container layout using flexbox */
    display: flex;
    flex-direction: column;
    margin-bottom: var(--form-field-vert-gap);
}

/* Target the select element */
.form .drop-down-wrapper select {
    border: var(--form-input-border-size) solid var(--form-input-border-color);
    padding: var(--form-input-padding);
    border-radius: 4px;
    background-color: var(--form-input-background-color);
    font-size: var(--form-input-font-size);
    color: var(--form-label-color);
}

/* Style the label */
.form .drop-down-wrapper .field-label {
    margin-bottom: 5px;
    font-weight: var(--form-label-font-weight);
    color: var(--form-label-color);
    font-size: var(--form-label-font-size);
}
```

   - Target the Wrapper: The first selector (`.drop-down-wrapper`) targets the outer wrapper element, ensuring styles apply to the entire dropdown component.
   - Flexbox Layout: Flexbox arranges the label, dropdown, and description vertically for a clean layout.
   - Label Styling: The label stands out with bolder font weight and a slight margin.
   - Dropdown Styling: The `select` element receives a border, padding, and rounded corners for a polished look.
   - Background Color: A consistent background color is set for visual harmony.
   - Arrow Customization: Optional styles hide the default dropdown arrow and create a custom arrow using a Unicode character and positioning.

+++

+++ Radio Groups

Similar to dropdown components, radio groups have their own HTML structure and CSS structure:

#### HTML Structure of Radio Group 

```HTML

<fieldset class="radio-group-wrapper field-{Name} field-wrapper" id="{FieldId}" name="{Name}" data-required="{Required}">
   <legend for="{FieldId}" class="field-label">....</legend>
   <% for each radio in Group %>
   <div class="radio-wrapper field-{Name}">
      <input type="radio" value="" id="{UniqueId}" data-field-type="radio-group" name="{FieldId}">
      <label for="{UniqueId}" class="field-label">...</label>
   </div>
   <% end for %>
</fieldset>

```

**Example HTML Structure**

```HTML

<fieldset class="radio-group-wrapper field-color field-wrapper" id="color_preference" name="color_preference" data-required="true">
  <legend for="color_preference" class="field-label">Favorite Color:</legend>
  <% for each radio in Group %>
    <div class="radio-wrapper field-color">
      <input type="radio" value="red" id="color_red" data-field-type="radio-group" name="color_preference">
      <label for="color_red" class="field-label">Red</label>
    </div>
    <div class="radio-wrapper field-color">
      <input type="radio" value="green" id="color_green" data-field-type="radio-group" name="color_preference">
      <label for="color_green" class="field-label">Green</label>
    </div>
    <div class="radio-wrapper field-color">
      <input type="radio" value="blue" id="color_blue" data-field-type="radio-group" name="color_preference">
      <label for="color_blue" class="field-label">Blue</label>
    </div>
  <% end for %>
</fieldset>

```

#### CSS Selectors for Radio Groups

- Targeting the Fieldset

```css
/* Target radio group container */
.form .radio-group-wrapper {
    border: var(--form-input-border-size) solid var(--form-input-border-color);
    padding: var(--form-input-padding);
    border-radius: 4px;
    margin-bottom: var(--form-field-vert-gap);
}
```

This selector targets any fieldset with the class radio-group-wrapper. This would be useful for applying general styles to the entire radio group.

- Targeting Radio Button Labels

```css
/* Target radio button labels */
.form .radio-wrapper label {
    font-weight: var(--form-label-font-weight);
    margin-right: 10px;
    color: var(--form-label-color);
    font-size: var(--form-label-font-size);
    cursor: pointer;
}
```

- Target all radio button labels within a specific fieldset based on its name

```css
/* Target all radio button labels within a specific fieldset based on its name */
.form .field-color .radio-wrapper label {
    /* Field-specific radio label customizations */
    /* Add your custom styles here */
}
```

+++

+++ Checkbox Groups

#### HTML Structure of Checkbox Group 

```HTML

<fieldset class="checkbox-group-wrapper field-{Name} field-wrapper" id="{FieldId}" name="{Name}" data-required="{Required}">
   <legend for="{FieldId}" class="field-label">....</legend>
   <% for each radio in Group %>
   <div class="checkbox-wrapper field-{Name}">
      <input type="checkbox" value="" id="{UniqueId}" data-field-type="checkbox-group" name="{FieldId}">
      <label for="{UniqueId}" class="field-label">...</label>
   </div>
   <% end for %>
</fieldset>

```

**Example HTML Structure**

```HTML

<fieldset class="checkbox-group-wrapper field-topping field-wrapper" id="topping_preference" name="topping_preference" data-required="false">
  <legend for="topping_preference" class="field-label">Pizza Toppings:</legend>
  <div class="checkbox-wrapper field-topping">
    <input type="checkbox" value="pepperoni" id="topping_pepperoni" data-field-type="checkbox-group" name="topping_preference">
    <label for="topping_pepperoni" class="field-label">Pepperoni</label>
  </div>
  <div class="checkbox-wrapper field-topping">
    <input type="checkbox" value="mushrooms" id="topping_mushrooms" data-field-type="checkbox-group" name="topping_preference">
    <label for="topping_mushrooms" class="field-label">Mushrooms</label>
  </div>
  <div class="checkbox-wrapper field-topping">
    <input type="checkbox" value="onions" id="topping_onions" data-field-type="checkbox-group" name="topping_preference">
    <label for="topping_onions" class="field-label">Onions</label>
  </div>
</fieldset>

```

#### CSS Selectors for checkbox groups

- Targeting the outer wrapper: These selectors target the outermost containers of both radio and checkbox groups, allowing you to apply general styles to the entire group structure. This is useful for setting spacing, alignment, or other layout-related properties.

```css
/* Primary Pattern: Targets radio group wrappers */
.form .radio-group-wrapper {
    margin-bottom: var(--form-field-vert-gap); /* Adds space between radio groups */
    display: flex;
    flex-direction: column;
    border: var(--form-fieldset-border);
    padding: var(--form-input-padding);
}

/* Primary Pattern: Targets checkbox group wrappers */
.form .checkbox-group-wrapper {
    margin-bottom: var(--form-field-vert-gap); /* Adds space between checkbox groups */
    display: flex;
    flex-direction: column;
    border: var(--form-fieldset-border);
    padding: var(--form-input-padding);
}
```

- Targeting Group Labels: This selector targets the `.field-label` element within both radio and checkbox group wrappers. This allows you to style the labels specifically for these groups, potentially making them stand out more.

```css
/* Primary Pattern: Target group labels */
.form .radio-group-wrapper legend,
.form .checkbox-group-wrapper legend {
    font-weight: var(--form-title-font-weight); /* Makes the group label bold */
    margin-bottom: 0.5rem;
    font-size: var(--form-fieldset-legend-font-size);
    color: var(--form-fieldset-legend-color);
    padding: var(--form-fieldset-legend-padding);
    border: var(--form-fieldset-legend-border);
}
```

- Targeting Individual Inputs and Labels: These selectors provide more granular control over individual radio buttons, checkboxes, and their associated labels. You can use these to adjust sizing, spacing, or apply more distinct visual styles.

```css
/* Primary Pattern: Styling radio buttons */
.form .radio-group-wrapper input[type="radio"] {
    margin-right: 8px; /* Adds space between the input and its label */
    margin-bottom: 4px;
    cursor: pointer;
}

/* Primary Pattern: Styling radio button labels */
.form .radio-group-wrapper label {
    font-size: var(--form-label-font-size); /* Changes the label font size */
    color: var(--form-label-color);
    font-weight: var(--form-label-font-weight);
    display: flex;
    align-items: center;
    cursor: pointer;
}

/* Primary Pattern: Styling checkboxes */
.form .checkbox-group-wrapper input[type="checkbox"] {
    margin-right: 8px; /* Adds space between the input and its label */
    margin-bottom: 4px;
    cursor: pointer;
}

/* Primary Pattern: Styling checkbox labels */
.form .checkbox-group-wrapper label {
    font-size: var(--form-label-font-size); /* Changes the label font size */
    color: var(--form-label-color);
    font-weight: var(--form-label-font-weight);
    display: flex;
    align-items: center;
    cursor: pointer;
}
```

- Customizing the Appearance of Radio Buttons and Checkboxes: This technique hides the default input and uses `:before` and `:after` pseudo-elements to create custom visuals that change appearance based on the 'checked' state.

```css
/* Hide the default radio button or checkbox */
.form .radio-group-wrapper input[type="radio"],
.form .checkbox-group-wrapper input[type="checkbox"] {
    opacity: 0;
    position: absolute;
    width: 1px;
    height: 1px;
}

/* Create a custom radio button */
.form .radio-group-wrapper input[type="radio"] + label::before {
    content: '';
    display: inline-block;
    width: 16px;
    height: 16px;
    border: 2px solid var(--form-input-border-color);
    border-radius: 50%;
    margin-right: 8px;
    background-color: var(--form-input-background-color);
    transition: all 0.2s ease;
}

.form .radio-group-wrapper input[type="radio"]:checked + label::before {
    background-color: var(--button-primary-color);
    border-color: var(--button-primary-color);
    box-shadow: inset 0 0 0 3px var(--form-input-background-color);
}

/* Create a custom checkbox */
.form .checkbox-group-wrapper input[type="checkbox"] + label::before {
    content: '';
    display: inline-block;
    width: 16px;
    height: 16px;
    border: 2px solid var(--form-input-border-color);
    border-radius: 2px;
    margin-right: 8px;
    background-color: var(--form-input-background-color);
    transition: all 0.2s ease;
}

.form .checkbox-group-wrapper input[type="checkbox"]:checked + label::before {
    background-color: var(--button-primary-color);
    border-color: var(--button-primary-color);
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill="white" d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/></svg>');
    background-repeat: no-repeat;
    background-position: center;
}
```

+++

+++ Panel/Container components

#### HTML Structure of Panel/Container components

```HTML

<fieldset class="panel-wrapper field-{PanelName} field-wrapper">
  <legend for="{id}" class="field-label" data-visible="false">bannerComponent</legend>
  <div class="{Type}-wrapper field-{Name} field-wrapper">
    <label for="{FieldId}" class="field-label">First Name</label>
    <input type="{Type}" placeholder="{Placeholder}" maxlength="{Max}" id={FieldId}" name="{Name}">
    <div class="field-description" aria-live="polite" id="{FieldId}-description">
      Hint - First name should be minimum 3 characters and a maximum of 10 characters.
    </div>
  </div>
</fieldset>

```

**Example HTML Structure**

```HTML

<fieldset class="panel-wrapper field-login field-wrapper">
  <legend for="login" class="field-label" data-visible="false">Login Information</legend>
  <div class="text-wrapper field-username field-wrapper">
    <label for="username" class="field-label">Username</label>
    <input type="text" placeholder="Enter your username" maxlength="50" id="username" name="username">
    <div class="field-description" aria-live="polite" id="username-description">
      Please enter your username or email address.
    </div>
  </div>
  <div class="password-wrapper field-password field-wrapper">
    <label for="password" class="field-label">Password</label>
    <input type="password" placeholder="Enter your password" maxlength="20" id="password" name="password">
    <div class="field-description" aria-live="polite" id="password-description">
      Your password must be at least 8 characters long.
    </div>
  </div>
</fieldset>

```

- The fieldset element acts as the panel container with the class panel-wrapper and additional classes for styling based on the panel name (field-login).
- The legend element (`<legend>`) serves as the panel title with the text "Login Information" and the class field-label. The data-visible="false" attribute can be used with JavaScript to control the visibility of the title.
- Inside the fieldset, multiple.{Type}-wrapper elements (.text-wrapper and .password-wrapper in this case) represent individual form fields within the panel.
- Each wrapper contains a label, input field, and description, similar to the previous examples.


#### Example CSS Selectors for Panel/Container components

1. Targeting the Panel:

  ```CSS
    /- Target the entire panel container */
    main .form form .panel-wrapper {
      /- Add your styles here (e.g., border, padding, background color) */
      border: 1px solid #ccc;
      padding: 15px;
      border-radius: 4px;
      margin-bottom: 20px;
   }


  ```

  - The `.panel-wrapper` selector styles all elements with the class panel-wrapper, creating a consistent look for all panels.

1. Targeting the Panel Title:

  ```CSS
    /- Target the legend element (panel title) */
    .panel-wrapper legend {
      /- Add your styles here (e.g., font-weight, font-size) */
      font-weight: bold;
      font-size: 16px;
      padding-bottom: 5px;
      margin-bottom: 10px;
      border-bottom: 1px solid #ddd; /- Optional: create a separation line */
    }

  ```

  - The `.panel-wrapper legend` selector styles the legend element within the panel, making the title stand out visually.


1. Targeting Individual Fields within the Panel:  

  ```CSS

  /- Target all form field wrappers within a panel */
  main .form form .panel-wrapper .{Type}-wrapper {
    /- Add your styles here (e.g., margin) */
    margin-bottom: 10px;
  }


  ```

  - The `.panel-wrapper .{Type}-wrapper` selector targets all wrappers with the `.{Type}-wrapper` class within the panel, allowing you to style the spacing between form fields.

1. Targeting Specific Fields (Optional):

  ```CSS

    /- Target the username field wrapper */
    main .form form .panel-wrapper .text-wrapper.field-username {
      /- Add your styles here (specific to username field) */
    }

    /- Target the password field wrapper */
    main .form form .panel-wrapper .password-wrapper.field-password {
      /- Add your styles here (specific to password field) */
    }

  ```

  - These optional selectors allow you to target specific field wrappers within the panel for unique styling, such as highlighting the username field.


+++

+++ Repeatable Panel

#### HTML Structure of a Repeatable Panel

```HTML

<fieldset class="panel-wrapper field-{PanelName} field-wrapper">
  <legend for="{id}" class="field-label" data-visible="false">bannerComponent</legend>
  <div class="{Type}-wrapper field-{Name} field-wrapper">
    <label for="{FieldId}" class="field-label">First Name</label>
    <input type="{Type}" placeholder="{Placeholder}" maxlength="{Max}" id={FieldId}" name="{Name}">
    <div class="field-description" aria-live="polite" id="{FieldId}-description">
      Hint - First name should be minimum 3 characters and a maximum of 10 characters.
    </div>
</fieldset>



```

**Example HTML Structure**

```HTML
<fieldset class="panel-wrapper field-contact field-wrapper" data-repeatable="true">
  <legend for="contact-1" class="field-label" data-visible="false">Contact Information</legend>
  <div class="text-wrapper field-name field-wrapper">
    <label for="name-1" class="field-label">Name</label>
    <input type="text" placeholder="Enter your name" maxlength="50" id="name-1" name="contacts[0].name">
    <div class="field-description" aria-live="polite" id="name-1-description">
      Please enter your full name.
    </div>
  </div>
  <div class="email-wrapper field-email field-wrapper">
    <label for="email-1" class="field-label">Email</label>
    <input type="email" placeholder="Enter your email address" maxlength="100" id="email-1" name="contacts[0].email">
    <div class="field-description" aria-live="polite" id="email-1-description">
      Please enter a valid email address.
    </div>
  </div>
</fieldset>

<fieldset class="panel-wrapper field-contact field-wrapper" data-repeatable="true">
  <legend for="contact-2" class="field-label" data-visible="false">Contact Information</legend>
  <div class="text-wrapper field-name field-wrapper">
    <label for="name-2" class="field-label">Name</label>
    <input type="text" placeholder="Enter your name" maxlength="50" id="name-2" name="contacts[1].name">
    <div class="field-description" aria-live="polite" id="name-2-description">
      Please enter your full name.
    </div>
  </div>
  <div class="email-wrapper field-email field-wrapper">
    <label for="email-2" class="field-label">Email</label>
    <input type="email" placeholder="Enter your email address" maxlength="100" id="email-2" name="contacts[1].email">
    <div class="field-description" aria-live="polite" id="email-2-description">
      Please enter a valid email address.
    </div>
  </div>
</fieldset>
```

Each panel has the same structure as the single panel example, with additional attributes:

- data-repeatable="true": This attribute indicates that the panel can be repeated dynamically using JavaScript or a framework.

- Unique IDs and names: Each element within the panel has a unique ID (for example, name-1, email-1) and name attribute based on the index of the panel (for example, name="contacts[0].name"). This allows for proper data collection when multiple panels are submitted.


#### CSS Selectors for a Repeatable Panel

- Targeting All Repeatable Panels:

```CSS

  /- Target all panels with the repeatable attribute */
 main .form form .panel-wrapper[data-repeatable="true"] {
    /- Add your styles here (e.g., border, margin) */
    border: 1px solid #ccc;
    padding: 15px;
    border-radius: 4px;
    margin-bottom: 20px;
  }


```

The selector styles all panels that can be repeated, ensuring a consistent look and feel.


- Targeting Individual Fields within a Panel:

```CSS

/- Target all form field wrappers within a repeatable panel */
main .form form .panel-wrapper[data-repeatable="true"] .{Type}-wrapper {
  /- Add your styles here (e.g., margin) */
  margin-bottom: 10px;
}

```

This selector styles all field wrappers within a repeatable panel, maintaining consistent spacing between fields.

- Targeting Specific Fields (within a Panel):

```CSS
/- Target the name field wrapper within the first panel */
main .form form .panel-wrapper[data-repeatable="true"][data-index="0"] .text-wrapper.field-name {
  /- Add your styles here (specific to first name field) */
}

/- Target all



```


+++


+++ File attachment

#### HTML Structure for File Attachment

```HTML

<div class="file-wrapper field-{FileName} field-wrapper">
  <legend for="{id}" class="field-label" data-visible="false"> File Attachment </legend>
  <div class="file-drag-area">
    <div class="file-dragIcon"></div>
    <div class="file-dragText">Drag and Drop To Upload</div>
    <button class="file-attachButton" type="button">Attach</button>
    <input type="file" accept="audio/*, video/*, image/*, text/*, application/pdf" id="{id}" name="{FileName}" autocomplete="off" multiple="" required="required">
  </div>
  <div class="files-list">
    <div data-index="0" class="file-description">
      <span class="file-description-name">ClaimForm.pdf</span>
      <span class="file-description-size">26 kb</span>
      <button class="file-description-remove" type="button"></button>
    </div>
  </div>
</div>


```

**Example HTML Structure**


```HTML

<div class="file-wrapper field-claim_form field-wrapper">
  <legend for="claim_form" class="field-label" data-visible="false">File Attachment</legend>
  <div class="file-drag-area">
    <div class="file-dragIcon"></div>
    <div class="file-dragText">Drag and Drop To Upload</div>
    <button class="file-attachButton" type="button">Attach</button>
  </div>
  <input type="file" accept="audio/*, video/*, image/*, text/*, application/pdf" id="claim_form"
         name="claim_form" autocomplete="off" multiple="" required="required" data-max-file-size="2MB">
  <div class="files-list">
    </div>
</div>

```

- The class attribute uses the provided name for the file attachment (claim_form).
- The id and name attributes of the input element match the file attachment name (claim_form).
- The files-list section is initially empty. It is populated dynamically with JavaScript when files are uploaded.


#### CSS Selectors for the File Attachment component

- Targeting the Entire File Attachment Component:

```CSS

/- Target the entire file attachment component */
main .form form .file-wrapper {
  /- Add your styles here (e.g., border, padding) */
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 4px;
  margin-bottom: 20px;
}


```

This selector styles the entire file attachment component, including the legend, drag area, input field, and list.

- Targeting Specific Elements:

```CSS

/- Target the drag and drop area */
main .form form .file-wrapper .file-drag-area {
  /- Add your styles here (e.g., background color, border) */
  background-color: #f0f0f0;
  border: 1px dashed #ddd;
  padding: 10px;
  text-align: center;
}

/- Target the file input element */
main .form form .file-wrapper input[type="file"] {
  /- Add your styles here (e.g., hide the default input) */
  display: none;
}

/- Target individual file descriptions within the list (populated dynamically) */
main .form form .file-wrapper .files-list .file-description {
  /- Add your styles here (e.g., margin, display) */
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

/- Target the file name within the description */
main .form form .file-wrapper .files-list .file-description .file-description-name {
  /- Add your styles here (e.g., font-weight) */
  font-weight: bold;
}


```

These selectors allow you to style various parts of the file attachment component individually. You can adjust the styles to match your design preferences.

+++



## Styling components

You can style form fields based on their specific type (`{Type}-wrapper`) or individual names (`field-{Name}`). This allows for more granular control and customization of your form's appearance.

+++ Styling Based on Field Type

You can use CSS Selectors to target specific field types and apply styles consistently. 

#### HTML Structure

```HTML

<div class="{Type}-wrapper field-{Name} field-wrapper" data-required={Required}>
   <label for="{FieldId}" class="field-label">First Name</label>
   <input type="{Type}" placeholder="{Placeholder}" maxlength="{Max}" id={FieldId}" name="{Name}" aria-describedby="{FieldId}-description">
   <div class="field-description" aria-live="polite" id="{FieldId}-description">
    Hint - First name should be minimum 3 characters and a maximum of 10 characters.
   </div>
</div>

```

**Example HTML Structure**

```HTML

<div class="text-wrapper field-name field-wrapper" data-required="true">
  <label for="name" class="field-label">Name</label>
  <input type="text" placeholder="Enter your name" maxlength="50" id="name" name="name">
</div>

<div class="number-wrapper field-age field-wrapper" data-required="true">
  <label for="age" class="field-label">Age</label>
  <input type="number" placeholder="Enter your age" id="age" name="age">
</div>

<div class="email-wrapper field-email field-wrapper" data-required="true">
  <label for="email" class="field-label">Email Address</label>
  <input type="email" placeholder="Enter your email" id="email" name="email">
</div>


```

- Each field is wrapped in a `div` element with several classes:
   - `{Type}-wrapper`: Identifies the type of field. For example, `form-text-wrapper`, `form-number-wrapper`, `form-email-wrapper`.
   - `field-{Name}`: Identifies the field by its name. For example `form-name`, `form-age`, `form-email`.
   - `field-wrapper`: A generic class for all field wrappers.
- The `data-required` attribute indicates whether the field is required or optional.
- Each field has a corresponding label, input element, and potential additional elements like placeholders and descriptions.




#### Example CSS Selectors

```CSS

/- Primary Pattern: Target all text input fields */
.form .text-wrapper input {
  /- Add your styles here */
  width: 100%;
  padding: var(--form-input-padding);
}

/- Primary Pattern: Target all number input fields */
.form .number-wrapper input {
  /- Add your styles here */
  letter-spacing: 2px; /- Example for adding letter spacing to all number fields */
  text-align: center;
}


```
+++

+++ Styling Based on Field name

You can also target individual fields by name to apply unique styles. 

#### HTML Structure

```HTML

<div class="{Type}-wrapper field-{Name} field-wrapper" data-required={Required}>
   <label for="{FieldId}" class="field-label">First Name</label>
   <input type="{Type}" placeholder="{Placeholder}" maxlength="{Max}" id="{FieldId}" name="{Name}" aria-describedby="{FieldId}-description">
   <div class="field-description" aria-live="polite" id="{FieldId}-description">
    Hint - Enter the 6 digit number sent to your mobile number.
   </div>
</div>

```

**Example HTML Structure**

```HTML

<div class="number-wrapper field-otp field-wrapper" data-required="true">
  <label for="otp" class="field-label">OTP</label>
  <input type="number" placeholder="Enter your OTP" maxlength="6" id="otp" name="otp" aria-describedby="otp-description">
  <div class="field-description" aria-live="polite" id="otp-description">
    Hint - Enter the 6 digit number sent to your mobile number.
   </div>
</div>


```


#### Example CSS Selector

```CSS

/- Primary Pattern: Target specific field by name */
.form .field-otp input {
   letter-spacing: 2px;
   text-align: center;
   font-family: monospace;
}

/- Context-specific: Use higher specificity when needed */
main .form .field-otp input {
   /- Use only when you need to override other styles */
   font-weight: bold;
}

```

This CSS targets all input elements that are located within an element that has the class `field-otp`. The Edge Delivery Services form structure follows the Adaptive Forms Block conventions, where containers are marked with field-specific classes like "field-otp" for fields with the name "otp".


## CSS File Structure and Implementation

### **Reference Implementation**

The complete form styling reference is available in the AEM Forms Boilerplate repository:

```
https://github.com/adobe-rnd/aem-boilerplate-forms/blob/main/blocks/form/form.css
```

This file serves as the canonical implementation of the CSS custom properties system and provides the foundation for all form styling. It includes comprehensive definitions for all CSS variables, component styling patterns, and responsive design implementations.

+++

+++ Project Integration

In your Edge Delivery Services project, implement form styling through this structured approach:

```
/blocks/form/form.css          // Core form block styles (copied from boilerplate)
/styles/styles.css             // Global site styles and CSS variable overrides
/styles/lazy-styles.css        // Additional component enhancements
```

+++

+++ Implementation Strategy

**CSS Custom Property Overrides**: Override form variables in your global styles to implement brand-specific theming:

```css
/* In /styles/styles.css */
:root {
    /* Brand-specific overrides */
    --button-primary-color: #your-brand-color;
    --form-background-color: #your-background;
    --label-color: #your-text-color;
}
```

**Component-Specific Customizations**: 
Add component-specific styling while maintaining the CSS variable system:

```css
/* Enhanced component styling */
.form .text-wrapper input {
    border-radius: var(--form-card-border-radius);
    transition: all 0.2s ease;
}

.form .text-wrapper input:focus {
    transform: translateY(-1px);
    box-shadow: 0 0 0 3px rgba(var(--button-primary-color), 0.1);
}
```

**Responsive Design Integration**: Utilize CSS custom properties within media queries for consistent responsive behavior:

```css
@media (max-width: 768px) {
    :root {
        --form-input-padding: 0.875rem;
        --form-field-vert-gap: 1rem;
        --form-padding: 1rem;
    }
}
```

+++

### Complete Styling Implementation Example

This section demonstrates how to create a modern, branded form using CSS custom properties. The implementation is broken down into clear subsections for easier understanding and navigation.



+++ 1. Brand Theme Variables

Define your brand's color palette, spacing, and typography using CSS custom properties.

```css
/* Custom brand theme */
:root {
  /* Brand color system */
  --brand-primary: #2563eb;
  --brand-secondary: #64748b;
  --brand-success: #059669;
  --brand-error: #dc2626;
  --brand-background: #f8fafc;
  
  /* Override form variables */
  --background-color-primary: #ffffff;
  --button-primary-color: var(--brand-primary);
  --button-primary-hover-color: #1d4ed8;
  --form-error-color: var(--brand-error);
  --form-background-color: var(--brand-background);
  --label-color: var(--brand-secondary);
  --border-color: #d1d5db;
  
  /* Enhanced spacing */
  --form-input-padding: 1rem;
  --form-field-vert-gap: 1.5rem;
  --form-padding: 2rem;
  
  /* Modern typography */
  --form-font-size-s: 16px;
  --form-label-font-weight: 500;
}
```
  

+++

+++ 2. Form Container Styling

Apply a modern background, border radius, and shadow to the form container for a visually appealing layout.


```css
/* Enhanced form container */
.form {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    border-radius: 12px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
    max-width: 600px;
    margin: 2rem auto;
    overflow: hidden;
}
```
        

        

+++

+++ 3. Input Field Styling

Style text, email, and number input fields for a clean, modern look.


```css
/* Modern input styling */
.form .text-wrapper input,
.form .email-wrapper input,
.form .number-wrapper input {
    background: white;
    border: 2px solid var(--border-color);
    border-radius: 8px;
    padding: var(--form-input-padding);
    font-size: 16px;
    transition: all 0.2s ease;
    width: 100%;
}
```


+++

+++ 4. Additional Customization

You can further extend the form styling by targeting specific fields, states, or components as needed. Refer to earlier sections for advanced patterns.

```css
/* Custom brand theme */
:root {
    /* Brand color system */
    --brand-primary: #2563eb;
    --brand-secondary: #64748b;
    --brand-success: #059669;
    --brand-error: #dc2626;
    --brand-background: #f8fafc;
    
    /* Override form variables */
    --background-color-primary: #ffffff;
    --button-primary-color: var(--brand-primary);
    --button-primary-hover-color: #1d4ed8;
    --form-error-color: var(--brand-error);
    --form-background-color: var(--brand-background);
    --label-color: var(--brand-secondary);
    --border-color: #d1d5db;
    
    /* Enhanced spacing */
    --form-input-padding: 1rem;
    --form-field-vert-gap: 1.5rem;
    --form-padding: 2rem;
    
    /* Modern typography */
    --form-font-size-s: 16px;
    --form-label-font-weight: 500;
}

/* Enhanced form container */
.form {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    border-radius: 12px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
    max-width: 600px;
    margin: 2rem auto;
    overflow: hidden;
}

/* Modern input styling */
.form .text-wrapper input,
.form .email-wrapper input,
.form .number-wrapper input {
    background: white;
    border: 2px solid var(--border-color);
    border-radius: 8px;
    padding: var(--form-input-padding);
    font-size: 16px;
    transition: all 0.2s ease;
    width: 100%;
}

.form .text-wrapper input:focus,
.form .email-wrapper input:focus,
.form .number-wrapper input:focus {
    border-color: var(--brand-primary);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    transform: translateY(-1px);
}

/* Enhanced button styling */
.form .button-wrapper button[type="submit"] {
    background: linear-gradient(135deg, var(--brand-primary) 0%, #1d4ed8 100%);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 1rem 2rem;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    width: 100%;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.form .button-wrapper button[type="submit"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
}
```

This comprehensive approach demonstrates how CSS custom properties enable sophisticated theming while maintaining the structural integrity and accessibility features of the Adaptive Forms Block system.

+++

## Troubleshooting CSS Issues

+++ CSS Specificity Problems

```css
/- ❌ Problem: Styles not applying */
.text-wrapper input {
  color: red;
}

/- ✅ Solution: Match or exceed existing specificity */
.form .text-wrapper input {
  color: red;
}

/- ✅ Alternative: Use higher specificity when needed */
main .form .text-wrapper input {
  color: red;
}
```

+++

+++ CSS Variable Override Issues

```css
/- ❌ Problem: Variables not working */
.form {
  --form-border-color: blue; /- Local scope only */
}

/- ✅ Solution: Define in root scope */
:root {
  --form-border-color: blue; /- Global scope */
}
```

+++

+++ Form State Styling

```css
/- Validation states */
.form .field-wrapper.error input {
  border-color: var(--form-error-color);
}

.form .field-wrapper.success input {
  border-color: var(--form-success-color);
}

/- Loading state */
.form[data-submitting="true"] {
  opacity: 0.7;
  pointer-events: none;
}

/- Disabled state */
.form input:disabled {
  background-color: var(--form-input-disabled-background);
  cursor: not-allowed;
}
```

+++

+++ Common Selector Mistakes

```css
/- ❌ Incorrect: Assumes direct nesting */
.form form input {
  /- This might miss inputs in wrappers */
}

/- ✅ Correct: Target actual structure */
.form .text-wrapper input {
  /- Targets actual HTML structure */
}

/- ❌ Avoid: Unnecessary specificity */
main .form form .text-wrapper input {
  /- Too specific, harder to override */
}

/- ✅ Preferred: Balanced specificity */
.form .text-wrapper input {
  /- Easier to maintain and override */
}
```

+++



### **Component-Specific Best Practices**


+++ Button Styling

```css
/- Primary buttons */
.form .button-wrapper button[type="submit"] {
  background-color: var(--form-focus-color);
  color: white;
  border: none;
  padding: var(--form-input-padding);
  border-radius: var(--form-border-radius);
}

/- Secondary buttons */
.form .button-wrapper button[type="reset"] {
  background-color: transparent;
  color: var(--form-text-color);
  border: 1px solid var(--form-border-color);
}
```

+++

+++ Responsive Form Design

```css
/- Mobile-first approach */
.form {
  width: 100%;
  padding: 1rem;
}

/- Tablet and up */
@media (min-width: 768px) {
  .form {
    max-width: var(--form-max-width);
    padding: var(--form-padding);
  }
}
```

+++

## Best Practices Summary

1. **Use CSS Custom Properties**: Leverage variables for consistent theming
2. **Follow Block-Based Architecture**: Use `.form` as the primary block selector
3. **Avoid Over-Specificity**: Don't use `main .form form` unless necessary
4. **Target Wrappers**: Use `.{Type}-wrapper` patterns for component targeting
5. **Maintain Consistency**: Use the same selector patterns throughout your project
6. **Test Across Devices**: Ensure forms work well on mobile, tablet, and desktop
7. **Validate Accessibility**: Ensure styles don't interfere with screen readers or keyboard navigation


