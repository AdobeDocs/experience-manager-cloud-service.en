---
title: Create Custom Components for an EDS Form
description: Create Custom Components for an EDS Form
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
role: Admin, Architect, Developer
exl-id: 2bbe3f95-d5d0-4dc7-a983-7a20c93e2906
---
# Create Custom Component in WYSIWYG Authoring

Edge Delivery Services Forms offer customization, allowing front-end developers to build tailored form components. These custom components integrate seamlessly into the WYSIWYG authoring experience, enabling form authors to easily add, configure, and manage them within the form editor. With custom components, authors can enhance functionality while ensuring a smooth and intuitive authoring process.

This document outlines the steps to create custom components by styling the native HTML form components to improve the user experience and increase the visual appeal of the form.

## Pre-requisites

Before you start creating your custom component, you should:

* Have a basic knowledge of [native HTML components](/help/edge/docs/forms/form-components.md).
* Know how to [style form fields based on field type using the CSS selectors](/help/edge/docs/forms/style-theme-forms.md)

## Create a custom component

Adding a custom component in the Universal Editor means making a new component available for form authors to use while designing forms. This involves registering the component, defining its properties, and configuring where it can be used. The steps to create custom components are:

[1. Adding structure for new custom component](#1-adding-structure-for-new-custom-component)
[2. Defining the properties of your custom component for authoring](#2-defining-the-properties-of-your-custom-component-for-authoring)
[3.  Making your custom component visible in the WYSIWYG component list](#3-making-your-custom-component-visible-in-the-wysiwyg-component-list)
[4. Registering your custom component](#4-registering-your-custom-component)
[5. Adding the runtime behaviour for your custom component](#5-adding-the-runtime-behaviour-for-your-custom-component)

Let's take an example of creating a new custom component called **range**. The range component appears as a straight line and displays values such as the minimum, maximum, or selected value.

![Range component style](/help/edge/docs/forms/universal-editor/assets/custom-component-range-style.png)

By the end of this article, you learn to create custom components from the scratch.

### 1. Adding structure for new custom component

Before a custom component can be used, it must be registered so that the Universal Editor recognizes it as an available option. This is achieved through a component definition, which includes a unique identifier, default properties, and the component's structure.Perform the following steps to make the custom component available for form authoring:

1. **Add new folder and files**
Add new folder and files for your new custom component in your AEM Project.
    1.  Open your AEM project and navigate to `../blocks/form/components/`.
    1.  Add a new folder for your custom component at `../blocks/form/components/<component_name>`. In this example, we create a folder named `range`.
    1.  Navigate to the newly created folder at `../blocks/form/components/<component_name>`. For example, navigate to `../blocks/form/components/range`, and add the following files:
        * `/blocks/form/components/range/_range.json`: Contains the definition of the custom component.
        * `../blocks/form/components/range/range.css`: Defines the styling for the custom component.
        * `../blocks/form/components/range/range.js`: Customizes the custom component at runtime.

            ![Adding the custom component for authoring](/help/edge/docs/forms/universal-editor/assets/adding-custom-component.png) 

            >[!NOTE]
            >
            > Ensure that the json file includes an underscore (_) as a prefix in its filename.

1. Navigate to the `/blocks/form/components/range/_range.json` file and add the component definition for the custom component.
   
1. **Add the component definition**
    
    To add the definition the fields need to be added in the `_range.json` file are:

      * **title**: The title of the component that is displayed in the Universal Editor.
      * **id**: A unique identifier of the component.
      * **fieldType**: Forms support various **fieldType** to capture specific types of user input. You can find the [supported fieldType in the Extra Byte section](#supported-fieldtypes).
      * **resourceType**: Each custom component has an associated resource type based on its fieldType. You can find the [supported resourceType in the Extra Byte section](#supported-resourcetype).
      * **jcr:title**: It is similar to a title, but it is stored within the component’s structure.
      * **fd:viewType**: It represents the name of the custom component. It is the unique identifier for the component. It is required to create a customized view for the component.

The `_range.json` file, after adding the component definition, is as follows:

```javascript
{
  "definitions": [
    {
      "title": "Range",
      "id": "range",
      "plugins": {
        "xwalk": {
          "page": {
            "resourceType": "core/fd/components/form/numberinput/v1/numberinput",
            "template": {
              "jcr:title": "Range",
              "fieldType": "number-input",
              "fd:viewType": "range",
              "enabled": true,
              "visible": true
            }
          }
        }
      }
    }
  ]
}
```

>[!NOTE]
>
> All form-related components follow the same approach as Sites when adding blocks to the Universal Editor. You can refer to the [Creating Blocks Instrumented for use with the Universal Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/wysiwyg-authoring/create-block) article for more information.

### 2. Defining the properties of your custom component for authoring

The custom component includes a component model that specifies which properties are configurable by the form author. These properties appear in the **Properties** dialog of the Universal Editor, allowing authors to adjust settings such as labels, validation rules, styles, and other attributes. To define properties:

1. Navigate to the `/blocks/form/components/range/_range.json` file and add the component model for the custom component. 

1. **Add the component model**

    To define the component model for your custom component, you need to add the relevant fields to the `_range.json` file.

      1. **Create new model**

          * In the models array, add a new object and set the `id` of the component model to match the `fd:viewType` property configured earlier in the component definition.
          * Include a fields array within this object.

      2. **Define Fields for the Property dialog**

          * Each object in the fields array should be a container-type component, allowing it to appear as a tab in the **Property** dialog.
          * Some fields can reference reusable properties available in `models/form-common`.

      3. **Use an Existing Component Model as a Reference**

           * You can copy the contents of an existing component model that corresponds to your chosen `fieldType` and modify it as needed. For example, the `number-input` component is extended to create a **range** component, so we can use the models array from `models/form-components/_number-input.json` as a reference.

    The `_range.json` file, after adding the component model, is as follows:

    ```javascript
    "models": [
    {
      "id": "range",
      "fields": [
        {
          "component": "container",
          "name": "basic",
          "label": "Basic",
          "collapsible": false,
          "...": "../../../../models/form-common/_basic-input-fields.json"
        },
        {
          "...": "../../../../models/form-common/_help-container.json"
        },
        {
          "component": "container",
          "name": "validation",
          "label": "Validation",
          "collapsible": true,
          "...": "../../../../models/form-common/_number-validation-fields.json"
        }
      ]
    }
    ]
    ```
    >[!NOTE]
    >
    > To add a new field to the **Property** dialog of a custom component, adhere to the [defined schema](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/field-types#loading-model).

    You can also [add custom properties](#adding-custom-properties-for-your-custom-component) to a custom component to extend its functionality.

#### Adding custom properties for your custom component

Custom properties enable you to define specific behaviors based on values set in the Property dialog of a component. This helps extend the component's functionality and customization options.

In this example, we add Step Value as a custom property to the Range component.

![Step value custom property](/help/edge/docs/forms/universal-editor/assets/customcomponent-stepvalue.png)

To add the Step Value custom property, append the component model with the following lines of code in the` _<component>.json` file:

    ```javascript
      {
      "component": "number",
      "name": "stepValue",
      "label": "Step Value",
      "valueType": "number"
      }
     ```

The JSON snippet defines a custom property called **Step Value** for a **Range** component. Below is a breakdown of each field:

* **component**: Specifies the type of input field used in the Property dialog. In this case, `number` indicates that the field accepts numeric values.
* **name**: The identifier for the property, used to reference it in the component’s logic. Here, the `stepValue` represents the step value setting for the range.
* **label**: The display name of the property as seen in the Property dialog. 
* **valueType**: Defines the data type expected for the property. The `number` ensures that only numeric inputs are allowed.

You can now use `stepValue` as a custom property in the JSON properties of `range.js` and implement dynamic behavior based on its value at runtime.

Hence, the final `_range.json` file, after adding the component definition, component model and custom properties, is as follows:

```javascript
 {
  "definitions": [
    {
      "title": "Range",
      "id": "range",
      "plugins": {
        "xwalk": {
          "page": {
            "resourceType": "core/fd/components/form/numberinput/v1/numberinput",
            "template": {
              "jcr:title": "Range",
              "fieldType": "number-input",
              "fd:viewType": "range",
              "enabled": true,
              "visible": true
            }
          }
        }
      }
    }
  ],
  "models": [
    {
      "id": "range",
      "fields": [
        {
          "component": "container",
          "name": "basic",
          "label": "Basic",
          "collapsible": false,
          "...": "../../../../models/form-common/_basic-input-fields.json"
         {
           "component": "number",
           "name": "stepValue",
            "label": "Step Value",
             "valueType": "number"
}
        },
        {
          "...": "../../../../models/form-common/_help-container.json"
        },
        {
          "component": "container",
          "name": "validation",
          "label": "Validation",
          "collapsible": true,
          "...": "../../../../models/form-common/_number-validation-fields.json"
        }
      ]
    }
  ]
}
```

![component definition and model](/help/edge/docs/forms/universal-editor/assets/custom-component-json-file.png)


### 3. Making your custom component visible in the WYSIWYG component list
    
A filter defines which section in which the custom component can be used in Universal Editor. This ensures that the component can only be used in appropriate sections, maintaining structure and usability.

To ensure the custom component appears in the list of available components during form authoring in WYSIWYG:

1. Navigate to the `/blocks/form/_form.json` file.
1. Locate the components array within the object that has `id="form"`.
1. Add the `fd:viewType` value from the `definitions[]` to the components array of the object with `id="form"`.

```javascript

 "filters": [
    {
      "id": "form",
      "components": [
        "captcha",
        "checkbox",
        "checkbox-group",
        "date-input",
        "drop-down",
        "email",
        "file-input",
        "form-accordion",
        "form-button",
        "form-fragment",
        "form-image",
        "form-modal",
        "form-reset-button",
        "form-submit-button",
        "number-input",
        "panel",
        "plain-text",
        "radio-group",
        "rating",
        "telephone-input",
        "text-input",
        "tnc",
        "wizard",
        "range"
      ]
    }
  ]
  ```

![component filter](/help/edge/docs/forms/universal-editor/assets/custom-component-form-file.png)

### 4. Registering your custom component

To enable the form block to recognize the custom component and load its properties defined in the component model during form authoring, add the `fd:viewType` value from the component definition to the `mappings.js` file.
To register a component:
1. Navigate to the `/blocks/form/mappings.js` file.
1. Locate the  `customComponents[]` array.
1. Add the `fd:viewType` value from the `definitions[]` array to the `customComponents[]` array.

```javascript
let customComponents = ["range"];
const OOTBComponentDecorators = ['file-input',
                                 'wizard', 
                                 'modal', 'tnc',
                                'toggleable-link',
                                'rating',
                                'datetime',
                                'list',
                                'location',
                                'accordion'];
```

![component mapping](/help/edge/docs/forms/universal-editor/assets/custom-component-mapping-file.png)

After completing the above steps, the custom component appears in the form's component list within the Universal Editor. You can then drag and drop it into your form section.

![range component](/help/edge/docs/forms/universal-editor/assets/custom-component-range.png)

You can now define the runtime behavior of your custom component by adding styling and functionality.

### 5. Adding the runtime behaviour for your custom component
 
You can modify custom components using predefined markup, as explained in the [Styling of form fields](/help/edge/docs/forms/style-theme-forms.md). This can be achieved with custom CSS (Cascading Style Sheets) and custom code to enhance the appearance of the component. To add the runtime behaviour for your component:

1. To add the styling, navigate to the `/blocks/form/components/range/range.css` file and add the following line of code:

    ```javascript
    /** Styling for range */
    main .form .range-widget-wrapper.decorated input[type="range"] {
    margin: unset;
    padding: unset;
    appearance: none;
    height: 5px;
    border-radius: 5px;
    border: none;
    background-image: linear-gradient(to right, #ADD8E6 calc(100% * var(--current-steps)/var(--total-steps)), #C5C5C5 calc(100% * var(--current-steps)/var(--total-steps)));
    }
 
    main .form .range-widget-wrapper.decorated input[type="range"]:focus {
    outline: none;
    }
 
    .range-widget-wrapper.decorated input[type="range"]::-webkit-slider-thumb {
    appearance: none;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: #00008B; /* Dark Blue */
    border: 3px solid #00008B; /* Dark Blue */
    cursor: pointer;
    outline: 3px solid #fff;
    }
 
    .range-widget-wrapper.decorated input[type="range"]:focus::-webkit-slider-thumb {
    border-color: #00008B; /* Dark Blue */
    }
 
    .range-widget-wrapper.decorated .range-bubble {
    color: #00008B; /* Dark Blue */
    font-size: 20px;
    line-height: 28px;
    position: relative;
    display: inline-block;
    padding-bottom: 12px;
    font-weight: bold;
    }
 
    .range-widget-wrapper.decorated .range-min,
    .range-widget-wrapper.decorated .range-max {
    font-size: 14px;
    line-height: 22px;
    color: #494f50;
    margin-top: 16px;
    display: inline-block;
    }
 
    .range-widget-wrapper.decorated .range-max {
    float: right;
    }
    ```
    The code helps you to define the styling and visual appearance of the custom component.

1. To add the functionality, navigate to the `/blocks/form/components/range/range.js` file and add the following line of code:

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
        '--total-steps': Math.ceil((max - min) / step),
        '--current-steps': Math.ceil((value - min) / step),
    };
    const style = Object.entries(steps).map(([varName, varValue]) => `${varName}:${varValue}`).join(';');
    bubble.style.left = `calc(${left})`;
    element.setAttribute('style', style);
    }
 
    export default async function decorate(fieldDiv, fieldJson) {
    console.log('RANGE DIV: ', fieldDiv);
    console.log('RANGE JSON: fieldJson', fieldJson);
     const input = fieldDiv.querySelector('input');
    // modify the type in case it is not range.
    input.type = 'range';
    input.min = input.min || 10;
    input.max = input.max || 1000;
    // create a wrapper div to provide the min/max and current value
    const div = document.createElement('div');
    div.className = 'range-widget-wrapper decorated';
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
    return fieldDiv;
    }
    ```

    It controls how the custom component interacts with user inputs, processes data, and integrates with the form block in the Universal Editor.

    After incorporating custom styling and functionality, the range component's appearance and behavior are enhanced. The updated design reflects the applied styles, while the added functionality ensures a more dynamic and interactive user experience. 
    The below screenshot illustrates the updated range component.

![Range component style](/help/edge/docs/forms/universal-editor/assets/custom-component-range-1.png)

## Frequently Asked Question

* **If I add styling in both component.css and forms.css, which one takes priority?**
When styles are defined in both `component.css` and **forms.css**, `component.css` takes priority. This is because component-level styles are more specific and override global styles from `forms.css`.

* **My custom component is not visible in the list of available components in Universal Editor. How can I fix this?**
If your custom component is not appearing, check the following files to ensure the component is correctly registered:
  * **component-definition.json**: Verify that the component is properly defined.
  * **component-filters.json**: Ensure the component is allowed in the appropriate sections.
  * **component-models.json**: Confirm that the component model is correctly configured.

## Best Practices

* It is recommended to [set up a local AEM development environment](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#set-up-local-aem-development-environment) for developing custom styles and components locally. 


## Extra Byte

### Supported resourceType

| Field Type    | Resource Type                                                   |
|--------------|------------------------------------------------------------------|
| text-input   | core/fd/components/form/textinput/v1/textinput                  |
| number-input | core/fd/components/form/numberinput/v1/numberinput              |
| date-input   | core/fd/components/form/datepicker/v1/datepicker                |
| panel        | core/fd/components/form/panelcontainer/v1/panelcontainer        |
| checkbox     | core/fd/components/form/checkbox/v1/checkbox                    |
| drop-down    | core/fd/components/form/dropdown/v1/dropdown                    |
| radio-group  | core/fd/components/form/radiobutton/v1/radiobutton              |
| plain-text   | core/fd/components/form/text/v1/text                            |
| file-input   | core/fd/components/form/fileinput/v2/fileinput                  |
| email        | core/fd/components/form/emailinput/v1/emailinput                |
| image        | core/fd/components/form/image/v1/image                          |
| button       | core/fd/components/form/button/v1/button                        |

### Supported fieldTypes

The supported fieldTypes for forms are:
* text-input
* number-input
* date-input
* panel
* checkbox
* drop-down
* radio-group
* plain-text
* file-input
* email
* image
* button

## See also

{{see-more-forms-eds}}
