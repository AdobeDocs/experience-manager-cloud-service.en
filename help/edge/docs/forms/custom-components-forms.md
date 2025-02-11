---
title: Create Custom Components for an EDS Form
description: Create Custom Components for an EDS Form
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
exl-id: 77e90657-38db-4a49-9aac-3f3774b62624
role: Admin, Architect, Developer
---
# Create Custom Components

Edge Delivery Services for AEM Forms allows you to customize the [native HTML form components](/help/edge/docs/forms/form-components.md) and create user-friendly and interactive forms. It enables you to modify the form components with predefined markup, as explained in the [Styling of form fields](/help/edge/docs/forms/style-theme-forms.md) using custom CSS (Cascading Style Sheets) and custom code for decorating the component, thus enhancing the appearance of form fields within an Adaptive Forms Block.

![Custom component](/help/edge/assets/custom-component-image.png)

This document outlines the steps to create custom components by styling the native HTML form components to improve the user experience and increase the visual appeal of the form.

Let us take an example of a `range` component that displays the `Estimated trip cost` on a form. The `range` component appears as a straight line, without showing any values like the minimum, maximum, or selected value.

![Native Range component](/help/edge/assets/native-range-component.png)

Let's start customizing the `range` field to show the minimum, maximum, and selected values on the line by adding style using CSS and adding a custom function to decorate a component. 

![Custom Range component](/help/edge/assets/custom-range-component.png)

By the end of this article, you learn to create custom components by adding styles in the CSS file and custom function.

## Pre-requisites

Before you start creating your custom component, you should:

* Have a basic knowledge of [native HTML components](/help/edge/docs/forms/form-components.md).
* Know how to [style form fields based on field type using the CSS selectors](/help/edge/docs/forms/style-theme-forms.md)


## Create a custom component


![steps to create custom component](/help/edge/docs/forms/assets/steps-to-create-custom-component.png)

Let's now understand each step in detail.

<!--Refer to the [enquiry spreadsheet](/help/edge/docs/forms/assets/enquiry.xlsx) to customize the `range` component, by following the steps as explained below.-->

### Add a custom function to decorate the component 

The custom function added in `[../Form Block/components]` consists of:

* **Function declaration**: Define the function name and its parameters.
* **Logic implementation**: Write the logic to add the custom behavior for the component.
* **Function export**: Make the function accessible in `[Form Block]`.
  
Let us create a JavaScript file named `range.js` to style the range component. To add a custom function:

1. Go to your AEM Project folder on Google Drive or SharePoint. 
1. Navigate to  `[../Form Block/components]`.
1. Add a new file named `range.js`.
1. Add the following line of code:

    ```javascript
    function updateBubble(input, element) {
    const step = input.step || 1;
    const max = input.max || 0;
    const min = input.min || 1;
    const value = input.value || 1;
    const current = Math.ceil((value - min) / step);
    const total = Math.ceil((max - min) / step);
    const bubble = element.querySelector('.range-bubble');
    // during initial render the width is 0. Hence using a default here.
    const bubbleWidth = bubble.getBoundingClientRect().width || 31;
    const left = `${(current / total) * 100}% - ${(current / total) * bubbleWidth}px`;
    bubble.innerText = `${value}`;
    const steps = {
    '--total-steps': Math.ceil((max - min) /    step),
    '--current-steps': Math.ceil((value - min) / step),
    };
    const style = Object.entries(steps).map(([varName, varValue]) => `${varName}:${varValue}`).join(';');
    bubble.style.left = `calc(${left})`;
    element.setAttribute('style', style);
    }
    // eslint-disable-next-line no-unused-vars
    export default function decorateRange(fieldDiv, field) {
    loadCSS('/blocks/form/components/range/range.css');
    const input = fieldDiv.querySelector('input');
    // modify the type in case it is not range.
    input.type = 'range';
    input.min = input.min || 1;
    // create a wrapper div to provide the min/max and current value
    const div = document.createElement('div');
    div.className = 'range-widget-wrapper';
    input.after(div);
    const hover = document.createElement('span');
    hover.className = 'range-bubble';
    const rangeMinEl = document.createElement('span');
    rangeMinEl.className = 'range-min';
    const rangeMaxEl = document.createElement('span');
    rangeMaxEl.className = 'range-max';
    rangeMinEl.innerText = `${input.min || 1}`;
    rangeMaxEl.innerText = `${input.max}`;
    div.appendChild(hover);
    // move the input element within the wrapper div
    div.appendChild(input);
    div.appendChild(rangeMinEl);
    div.appendChild(rangeMaxEl);
    input.addEventListener('input', (e) => {
        updateBubble(e.target, div);
    });
    updateBubble(input, div);
    // as a best practice add a custom css class to apply custom styling
    fieldDiv.classList.add('decorated');
    return fieldDiv;    
    }
    ```

1. Save the changes.

### Inject the decorator in the Form Block

The `[Form Block]` uses semantic HTML to render form fields, including input fields, labels, and help text, with standard attributes for accessibility. To have the `[Form Block]` use custom decorator for a specified component, define it in the `mappings.js` file. The `mappings.js` file imports a function that returns the module responsible for decorating a particular component. The function takes the field properties and returns a decorator function for the form field. 

In our case, the function checks the `fieldType` property of the field and return the custom range decorator from the `range.js` file present in `[../Form Block/components]`.

To inject the decorator in the Form Block:

1. Go to  `[../Form Block/]` and open `mapping.js`.
1. Add the following line of code:

    ```javascript
    export default async function componentDecorator(fd) {
    const { ':type': type = '', fieldType } = fd;
    .... existing code ....
    if (fieldType === 'range') {
    const module = await import('./components/range.js');
    return module.default(element,fd);;
    }
     return null; // null should be returned to use the original markup
    }
    ```

1. Save the changes.

### Add style for the component in the CSS file

You can change the appearance of form fields based on field type and field names using CSS selectors, allowing for consistent or unique styling based on requirements. To style the component, add code in the `form.css` file to modify the look and feel of the form's component. 

To customize the style for the `range` component, include a CSS code snippet that styles a `range` input element and its associated components within a form. This assumes a structured HTML layout with classes such as `.form` and `.range-wrapper`.

To add style for a component in the CSS file:
1. Go to  `[../Form Block/]` and open `form.css`.
1. Add the following line of code:

    ```javascript
        /** styling for range */
    main .form .range-wrapper.decorated input[type="range"] {
    margin: unset;
    padding: unset;
    appearance: none;
    height: 5px;
    border-radius: 5px;
    border: none;
    background-image: linear-gradient(to right, var(--button-primary-color) calc(100% * var(--current-steps)/var(--total-steps)), #C5C5C5 calc(100% * var(--current-steps)/var(--total-steps)));
    }

    main .form .range-wrapper.decorated input[type="range"]:focus {
    outline: none;
    }

    .range-wrapper.decorated input[type="range"]::-webkit-slider-thumb {
    appearance: none;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: #fff;
    border: 3px solid var(--button-primary-color);
    cursor: pointer;
    outline: 3px solid #fff;
    }

    .range-wrapper.decorated input[type="range"]:focus::-webkit-slider-thumb {
    border-color: var(--button-primary-color);
    }

    .range-wrapper.decorated .range-bubble {
    color: #17252e;
    font-size: 20px;
    line-height: 28px;
    position: relative;
    display: inline-block;
    padding-bottom: 12px;
    }

    .range-wrapper.decorated .range-min,
    .range-wrapper.decorated .range-max {
    font-size: 14px;
    line-height: 22px;
    color: #494f50;
    margin-top: 16px;
    display: inline-block;
    }

    .range-wrapper.decorated .range-max {
    float: right;
    }

    ```
1. Save the changes.

### Deploy the files and build the project

Deploy the updated `range.js`, `mapping.js` and `form.css` files to your GitHub project and verify a successful build.

### Preview the form using the AEM sidekick

Preview your form with the newly implemented function that styles the `range` component.

![Custom component form](/help/edge/assets/custom-componet-form.png)

The new styling for the `range` component shows the minimum, maximum, and selected values on the line by adding styles using CSS and a custom function that includes a decorator for the component.


## See also

{{see-more-forms-eds}}



