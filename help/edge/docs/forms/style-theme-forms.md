---
title: Customize theme and style for an AEM Forms Edge Delivery Service Form
description: Customize theme and style for an AEM Forms Edge Delivery Service Form
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Styling Form Fields 

Forms are crucial for user interaction on websites, allowing them to input data. This guide covers the fundamentals of styling various form fields within the [Form Block](/help/edge/docs/forms/create-forms.md), helping you create visually appealing and user-friendly forms.

## Understanding Form Field Types

Before diving into styling, let's review the common form field types supported by the Form Block:

* Input Fields: These include text inputs, email inputs, password inputs, and more.
* Checkbox Groups: Used for selecting multiple options.
* Radio Groups: Used for selecting only one option from a group.
* Dropdowns: Also known as select boxes, used for selecting one option from a list.
* Panels/Containers: Used to group related form elements together.

## Basic Styling Principles

Understanding fundamental CSS concepts is crucial before styling specific form fields:

* Selectors: CSS selectors allow you to target specific HTML elements for styling. You can use element selectors, class selectors, or ID selectors.
* Properties: CSS properties define the visual appearance of elements. Common properties for styling form fields include color, background-color, border, padding, margin, and more.
* Box Model: The CSS box model describes the structure of HTML elements as a content area surrounded by padding, borders, and margins.
* Flexbox/Grid: CSS Flexbox and Grid layouts are powerful tools for creating responsive and flexible designs.

## Styling a Form for Form Block

The Form Block offers a standardized HTML structure, simplifying the process of selecting and styling form components:

* **Update default styles**: You can modify the default styles of a form by editing the `/blocks/form/form.css file`. This file provides comprehensive styling for a form, supporting multi-step wizard forms. It emphasizes using custom CSS variables for easy customization, maintenance, and uniform styling across forms. For instructions on adding the Form Block to your project, refer to [create a form](/help/edge/docs/forms/create-forms.md).

* **Customization**: Use the default `forms.css` as a base and customize it to modify the look and feel of your form components, making it visually appealing and user-friendly. The file's structure encourages organization and maintains styles for forms, promoting consistent designs across your website.

## Breakdown of forms.css's structure

* **Global variables:** Defined at the `:root` level, these variables (`--variable-name`) store values used throughout the stylesheet for consistency and ease of updates. These variables define colors, font sizes, padding, and other properties. You can declare your own Global variables or modify existing ones to change the form's style.

* **Universal selector styles:** The `*` selector matches every element in the form, ensuring styles are applied to all components by default, including setting the `box-sizing` property to `border-box`.

* **Form styling:** This section focuses on styling form components using selectors to target specific HTML elements. It defines styles for input fields, text areas, checkboxes, radio buttons, file inputs, form labels, and descriptions.

* **Wizard styling (if applicable):** This section is dedicated to styling the wizard layout, a multi-step form where each step is displayed one at a time. It defines styles for the wizard container, fieldsets, legends, navigation buttons, and responsive layouts.

* **Media queries:** These provide styles for different screen sizes, adjusting layout and styling accordingly.

* **Miscellaneous styling:**: This section covers styles for success or error messages, file upload areas, and other elements you might encounter in a form.


## Components Structure

The Form Block offers a consistent HTML structure for various form elements, ensuring easier styling and management. You can manipulate the components using CSS for styling purposes.

### General Components (except dropdowns, radio groups, and checkbox groups):

All form fields, except for dropdowns, radio groups, and checkbox groups, has the following HTML structure:

#### HTML Stucture

```HTML

<div class="form-{Type}-wrapper form-{Name} field-wrapper" data-required={Required}>
  <label for="{FieldId}" class="field-label">Field Label</label>
  <input type="{Type}" placeholder="{Placeholder}" maxlength="{Max}" id="{FieldId}" name="{Name}" aria-describedby="{FieldId}-description">
  <div class="field-description" aria-live="polite" id="{FieldId}-description">
    Hint - Description of the field.
  </div>
</div>

```

* Classes: The div element has several classes for targeting specific elements and styling. You require the `form-{Type}-wrapper` or `form-{Name}` classes to develop a CSS selector to style a form field:
   * {Type}: Identifies the component by field type. For example, text (form-text-wrapper), number (form-number-wrapper), date (form-date-wrapper).
   * {Name}: Identifies the component by name. The name of the field can have only alphanumeric characters, the multiple consecutive dashes in the name are replaced with a single dash `(-)`, and starting and ending dashes in a field name are removed. For example, first-name (form-first-name field-wrapper).
   * {FieldId}: It is unique identifier for the field, automatically generated.
   * {Required}: It is a boolean indicating if the field is required.
* Label: The `label` element provides a descriptive text for the field and associates it with the input element using the `for` attribute.
* Input: The `input` element defines the type of data to be entered. For example, text, number, email.
* Description (Optional): The `div` with class `field-description` provides additional information or instructions for the user.

**Example**

```HTML

<div class="form-text-wrapper form-first-name field-wrapper" data-required="true">
  <label for="firstName" class="field-label">First Name</label>
  <input type="text" placeholder="Enter your first name" maxlength="50" id="firstName" name="firstName" aria-describedby="firstName-description">
  <div class="field-description" aria-live="polite" id="firstName-description">
    Please enter your legal first name.
  </div>
</div>


```

#### CSS Selector for General Components

```CSS

.form-{Type}-wrapper input {
  /* Add your styles here */
  border: 1px solid #ccc;
  padding: 8px;
  border-radius: 4px;
}


.form-{Name} input {
  /* Add your styles here */
  border: 1px solid #ccc;
  padding: 8px;
  border-radius: 4px;
}



```

* `.form-{Type}-wrapper`: Targets the outer `div` element based on the field type. For example, `.form-text-wrapper` targets all text input fields.
* `.form-{Name}`: Further selects the element based on the specific field name. For example, `.form-first-name` targets the "First Name" text field.

**Example:**

```CSS

/*Target all text input fields */

.form-text-wrapper input {
  border: 1px solid #ccc;
  padding: 8px;
  border-radius: 4px;
}

/*Target all fields with name first-name*/

.form-first-name input {
  border: 1px solid #ccc;
  padding: 8px;
  border-radius: 4px;
}


```


### Dropdown Component

For dropdown menus, the `select` element is used instead of an `input` element:


#### HTML Stucture

```HTML

<div class="form-drop-down-wrapper form-{Name} field-wrapper" data-required={required}>
  <label for="{FieldId}" class="field-label">First Name</label>
  <select id="{FieldId}" name="{Name}"><option></option><option></option></select>
  <div class="field-description" aria-live="polite" id="{FieldId}-description">
    Hint - First name should be minimum 3 characters and a maximum of 10 characters.
  </div>
</div>

```

**Example**

```HTML

    <div class="form-drop-down-wrapper form-country field-wrapper" data-required="true">
      <label for="country" class="field-label">Country</label>
      <select id="country" name="country">
         <option value="">Select Country</option>
         <option value="US">United States</option>
         <option value="CA">Canada</option>
    </select>
   <div class="field-description" aria-live="polite" id="country-description">Please select your country of residence.</div>
   </div>

```

#### CSS selectors for drop-down component

```CSS

/* Target the outer wrapper */
.form-drop-down-wrapper {
  /* Add your styles here */
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

/* Style the label */
.form-drop-down-wrapper .field-label {
  margin-bottom: 5px;
  font-weight: bold;
}

/* Style the dropdown itself */
.form-drop-down-wrapper select {
  border: 1px solid #ccc;
  padding: 8px;
  border-radius: 4px;
  background-color: white; /* Ensure a consistent background */
  /* Adjust arrow appearance as needed */
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}

/* Optional: Style the dropdown arrow */
.form-drop-down-wrapper select::-ms-expand {
  display: none; /* Hide the default arrow for IE11 */
}

.form-drop-down-wrapper select::after {
  content: "\25BC";
  font-size: 12px;
  color: #ccc;
  /* Adjust positioning as needed */
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
}

```

   * Target the Wrapper: The first selector (`.form-drop-down-wrapper`) targets the outer wrapper element, ensuring styles apply to the entire dropdown component.
   * Flexbox Layout: Flexbox arranges the label, dropdown, and description vertically for a clean layout.
   * Label Styling: The label stands out with bolder font weight and a slight margin.
   * Dropdown Styling: The select element receives a border, padding, and rounded corners for a polished look.
   * Background Color: A consistent background color is set for visual harmony.
   * Arrow Customization: Optional styles hide the default dropdown arrow and create a custom arrow using a Unicode character and positioning.

### Radio and Checkbox Groups

Similar to dropdown components, radio and checkbox groups have their own HTML structure and CSS considerations:

#### Radio Group HTML Structure 

```HTML

<div class="form-checkbox-group-wrapper form-{Name} field-wrapper" data-required={required}>
  <label class="field-label">{Label Text}</label>
  <div class="checkbox-group">
    <input type="checkbox" id="{FieldId}-1" name="{Name}" value="{Value1}">
    <label for="{FieldId}-1">{Option 1 Text}</label>
    <input type="checkbox" id="{FieldId}-2" name="{Name}" value="{Value2}">
    <label for="{FieldId}-2">{Option 2 Text}</label>
    </div>
  <div class="field-description" aria-live="polite" id="{FieldId}-description">
    Hint - Select multiple options (if applicable).
  </div>
</div>

```


#### Radio Group HTML Structure 

```HTML

<div class="form-checkbox-group-wrapper form-{Name} field-wrapper" data-required={required}>
  <label class="field-label">{Label Text}</label>
  <div class="checkbox-group">
    <input type="checkbox" id="{FieldId}-1" name="{Name}" value="{Value1}">
    <label for="{FieldId}-1">{Option 1 Text}</label>
    <input type="checkbox" id="{FieldId}-2" name="{Name}" value="{Value2}">
    <label for="{FieldId}-2">{Option 2 Text}</label>
    </div>
  <div class="field-description" aria-live="polite" id="{FieldId}-description">
    Hint - Select multiple options (if applicable).
  </div>
</div>


```

#### CSS selectors for radio and checkbox groups

**Targeting the Outer Wrapper**


```CSS

   /* Targets all radio group wrappers */
.form-radio-group-wrapper {
  margin-bottom: 20px; /* Adds space between radio groups */
}

/* Targets all checkbox group wrappers */
.form-checkbox-group-wrapper {
  margin-bottom: 20px; /* Adds space between checkbox groups */
}


```

These selectors target the outermost containers of both radio and checkbox groups, allowing you to apply general styles to the entire group structure. This is useful for setting spacing, alignment, or other layout-related properties.

**Targeting Group Labels**

```CSS

.form-radio-group-wrapper .field-label,
.form-checkbox-group-wrapper .field-label {
 font-weight: bold; /* Makes the group label bold */
}


```

This selector targets the `.field-label` element within both radio and checkbox group wrappers. This allows you to style the labels specifically for these groups, potentially making them stand out more.

**Targeting Individual Inputs and Labels**

```CSS

/* Styling radio buttons */
.form-radio-group-wrapper input[type="radio"] {
  margin-right: 5px; /* Adds space between the input and its label */
} 

/* Styling radio button labels */
.form-radio-group-wrapper label {
  font-size: 15px; /* Changes the label font size */
}

/* Styling checkboxes */
.form-checkbox-group-wrapper input[type="checkbox"] {
  margin-right: 5px;  /* Adds space between the input and its label */ 
}

/* Styling checkbox labels */
.form-checkbox-group-wrapper label {
  font-size: 15px; /* Changes the label font size */
}


```

These selectors provide more granular control over individual radio buttons, checkboxes, and their associated labels. You can use these to adjust sizing, spacing, or apply more distinct visual styles.


**Customizing the Appearance of Radio Buttons and Checkboxes**

```CSS

/* Hide the default radio button or checkbox */
.form-radio-group-wrapper input[type="radio"],
.form-checkbox-group-wrapper input[type="checkbox"] {
  opacity: 0; 
  position: absolute; 
}

/* Create a custom radio button */
.form-radio-group-wrapper input[type="radio"] + label::before { 
  content: "";
  display: inline-block;
  width: 16px; 
  height: 16px; 
  border: 2px solid #ccc; 
  border-radius: 50%;
  margin-right: 5px;
}

.form-radio-group-wrapper input[type="radio"]:checked + label::before {
  background-color: #007bff; 
}

/* Create a custom checkbox */
/* Similar styling as above, with adjustments for a square shape */



```

This technique hides the default input and uses  :before and :after pseudo-elements to create custom visuals that change appearance based on the 'checked' state.


## Styling Fields

In addition to the general styling techniques covered earlier, you can also style form fields based on their specific type or individual names. This allows for more granular control and customization of your form's appearance.

### Styling Based on Field Type

You can use CSS selectors to target specific field types and apply styles consistently. 

**Example HTML Structure**

```HTML

<div class="form-text-wrapper form-name field-wrapper" data-required="true">
  <label for="name" class="field-label">Name</label>
  <input type="text" placeholder="Enter your name" maxlength="50" id="name" name="name">
</div>

<div class="form-number-wrapper form-age field-wrapper" data-required="true">
  <label for="age" class="field-label">Age</label>
  <input type="number" placeholder="Enter your age" id="age" name="age">
</div>

<div class="form-email-wrapper form-email field-wrapper" data-required="true">
  <label for="email" class="field-label">Email Address</label>
  <input type="email" placeholder="Enter your email" id="email" name="email">
</div>


```

* Each field is wrapped in a `div` element with several classes:
   * `form-{Type}-wrapper`: Identifies the type of field. For example, `form-text-wrapper`, `form-number-wrapper`, `form-email-wrapper`.
   * `form-{Name}`: Identifies the field by its name. For example `form-name`, `form-age`, `form-email`.
   * `field-wrapper`: A generic class for all field wrappers.
* The `data-required` attribute indicates whether the field is required or optional.
* Each field has a corresponding label, input element, and potential additional elements like placeholders and descriptions.

For example:

```CSS

/* Target all text input fields */
.form-text-wrapper input {
  /* Add your styles here */
}

/* Target all number input fields */
.form-number-wrapper input {
  /* Add your styles here */
  letter-spacing: 2px; /* Example for adding letter spacing to all number fields */
}


```

### Styling Specific Field Types

You can also target individual fields by name to apply unique styles. 

**Example HTML Structure**

```HTML

<div class="form-number-wrapper form-otp field-wrapper" data-required="true">
  <label for="otp" class="field-label">OTP</label>
  <input type="number" placeholder="Enter your OTP" maxlength="6" id="otp" name="otp">
</div>


```

**CSS Selector**

```CSS

.form-otp input {
   letter-spacing: 2px
}


```

* Selector: This CSS targets all input elements that are located within an element that has the class `form-otp`. Your HTML structure follows conventions of the Form Block, this implies there's a container marked with the class "form-otp" holds the field with the name "otp".

* Property and Value: The code applies `letter-spacing: 2px`. This CSS property controls the spacing between individual letters within the text content of the input field.