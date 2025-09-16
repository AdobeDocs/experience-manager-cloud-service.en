---
title: Create Custom Components for an EDS Form
description: Create Custom Components for an EDS Form
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: 2bbe3f95-d5d0-4dc7-a983-7a20c93e2906
---

# Creating Custom Form Component in Adaptive Form Block

Edge Delivery Services Forms offer customization, allowing front-end developers to build tailored form components. These custom components integrate seamlessly into the WYSIWYG authoring experience, enabling form authors to easily add, configure, and manage them within the form editor. With custom components, authors can enhance functionality while ensuring a smooth and intuitive authoring process.

This document outlines the steps to create custom components by styling the native HTML form components to improve the user experience and increase the visual appeal of the form.

## Architecture Overview

Custom component for the Forms Block follows an **MVC (Model-View-Controller)** architecture pattern:

### Model

- Defined by the JSON schema for each `field/component`.

- Authorable properties are specified in the corresponding JSON file (see blocks/form/models/form- components).

- These properties are available to authors in  the form builder and passed to the component as part of the field definition (fd).

### View

- HTML structure for each field type is described in form-field-types.

- This is the base structure for your component which can be extended or modified.

- The base HTML structure for each OOTB component is documented in form-field-types.

### Controller/Component Logic

- Implemented in JavaScript, either as OOTB (out-of-the-box) or custom components.  - Located in `blocks/form/components` for custom components.

## OOTB Components

**OOTB (out-of-the-box)** components provide the foundation for custom development:  

- OOTB components are located in `blocks/form/models/form-components`.

- Each OOTB component has a JSON file defining its authorable properties (e.g.,` _text-input.json`,`_drop-down.json`).

- These properties are available to authors in the form builder and are passed to the component as part of the field definition (fd).

- The base HTML structure for each OOTB component is documented in form-field-types.

Extending an existing OOTB component allows you to reuse its base structure, behavior, and properties while customizing it to fit your needs.

- Custom components must extend from a predefined set of OOTB components.

- The system identifies which OOTB component to extend based on the `viewType` property in the field's JSON.

- The system maintains a registry of allowed custom component variants. Only variants listed in this registry can be used, for example, `customComponents[]` in `mappings.js`.

- When rendering a form, the system checks the variant property or `:type/fd:viewType`, and if it matches a registered custom component, loads the corresponding JS and CSS files from the `blocks/form/components` folder.

- The custom component is then applied to the base HTML structure of the OOTB component, allowing you to enhance or override its behavior and appearance.

## Structure of Custom Component

To create custom components, you can use the **Scaffolder CLI** to setup the files and folders required for your component and then add code for your custom component.

- Custom components reside in the `blocks/form/components` folder.

- Each custom component must be placed in its own folder, named after the component, for example cards. Inside the folder, the following files shold be:

  - **_cards.json** - JSON file that extends the component definition of an OOTB component, defines its authorable properties (models[]) and content structure on load (definitions[]).
  - **cards.js** - The JavaScript file that includes the main logic.
  - **cards.css** - optional, for styles.

- The name of the folder and the JS/CSS files must match.

### Reusing and Extending Fields in Custom Components

When defining fields in your custom component's JSON (for any field group, basic, validation, help, etc.), follow these best practices for maintainability and consistency:

- Reuse standard/shared fields by referencing existing shared containers or field definitions (e.g., `../form-common/_basic-input-placeholder-fields.json#/fields`, `../form-common/_basic- validation-fields.json#/fields`). This ensures you inherit all standard options without duplicating them.

- Add only new or custom fields explicitly in your container. This keeps your schema DRY and focused.

- Remove or avoid duplicating fields that are already included via references. Only define fields that are unique to your component's logic.

- Reference help containers and other shared content (e.g., `../form-common/_help-container.json`) as needed for consistency and maintainability.

>[!TIP]
>
> - This pattern makes it easy to update or extend logic in the future, and ensures your custom components remain consistent with the rest of the form system.
> - Always check for existing shared containers or field definitions before adding new ones.

### Defining New Properties for Custom Components

- If you need to capture new properties for your custom component from authors, it can be done so by defining a field in the `fields[]` array of the component in the JSON of the component.

- The custom component is identified using the :type property, which can be set as `fd:viewType` in the JSON file (e.g., `fd:viewType: cards`). This allows the system to recognize and load the correct custom component and therefore this is mandatory for custom components

- Any new properties added in the JSON definition are available in the field definition as properties. `<propertyName>` in your component's JS logic

## Custom Component JavaScript API

The Custom Component JavaScript API defines how to control the behavior, appearance, and reactivity of your custom form component.

### Decorate Function

The **decorate** function is the entry point for your custom component. It initializes the component, links it with its JSON definition, and allows you to manipulate its HTML structure and behavior.

  >[!NOTE]
  >
  > The custom component's JavaScript file must export a default function as decorate:

#### Function Signature:

```javascript
export default function decorate(element, fieldJson, container, formId) 
{
  // element: The HTML structure of the OOTB component you are extending
  // fieldJson: The JSON field definition (all authorable properties)
  // container: The parent element (fieldset or form)
  // formId: The id of the form

  // ... your logic here ...
}
```

It can:

- **Modify the element**: Add event listeners, update attributes, or inject additional markup.

- **Access JSON properties**: Use `fd.properties.<propertyName>` to read values defined in the JSON schema and apply them within the component logic.

## Subscribe Function

The **subscribe** function enables your component to react to changes in field values or custom events. This ensures the component stays in sync with the form's data model and can dynamically update its UI.

### Function Signature:

```javascript
import { subscribe } from '../../rules/index.js';
export default function decorate(fieldDiv, fieldJson, container, formId) {
  // Access custom properties defined in the JSON
  const { initialText, finalText, time } = fieldJson?.properties;

  // ... setup logic ...

  subscribe(fieldDiv, formId, (_fieldDiv, fieldModel) => {
    fieldModel.subscribe(() => {
      // React to custom event (e.g., resetCardOption)
      // ... logic ...
    }, 'resetCardOption');
  });
}
```

It can:

- **Register a callback**: Calling **subscribe(element, formId, callback)** registers your callback to run whenever the field data changes.Use two callback parameters:
  - **element**: The HTML element representing the field.
  - **fieldModel**: The object representing the field's state and event APIs.

- **Listen for changes or events**: Use `fieldModel.subscribe((event) => { ... }, 'eventName')` to execute logic whenever a value changes or a custom event is triggered. The event object contains details about what changed.

## Creating a Custom Component

In this section, you'll learn the process of creating a **cards custom component** by extending OOTB radio button component.

![Card custom Component](/help/edge/docs/forms/universal-editor/assets/cc-ue-card-component.png)

### 1. Code Setup

#### 1.1 Files and Folders

The first step is to setup the necessary files of the custom component and wire it up to the code in the repository. This process is done automatically by the **AEM Forms Scaffolder CLI**, which makes it quicker to scaffold and wire the necessary files.

>[!VIDEO](https://video.tv.adobe.com/v/3474752)

1. Open the terminal and navigate to the root of your form project.
2. Run the following commands:

```bash
npm install
npm run create:custom-component
```

![Scaffolder CLI](/help/edge/docs/forms/universal-editor/assets/scaffolder-cli.png)

It will:

- **Prompt you to name** your new component. For example, in this case use cards.
- **Ask you to choose** a base component (select radio group)

This creates all necessary folders and files, including:

```
blocks/form/
└── components/
  └── cards/
    ├── cards.js
    └── cards.css
    └── _cards.json
```

And wires it up with the rest of the code in the repository as shown in the output of the CLI. 
It performs the below functionalities automatically:

- Adds cards to the filters to allow for addition inside Adaptive Form Block.  
- Updates allowlist of `mappings.js` to include the new cards component.
- Registers the definition of the cards component under the **Custom components** listing in Universal Editor.

>[!NOTE]
>
> You can also create a custom component using the manual (legacy) method. See the [Manual or Legacy Method](#manual-or-legacy-method-to-create-custom-component) to create custom component section for details.

#### 1.2 Using Component in Universal Editor

1. **Refresh the Universal Editor**: Open your form in the Universal Editor and refresh the page to ensure it loads the latest code from the repository.

2. **Add the Custom Component**

   1. Click the **Add (+)** button on the form canvas.
   2. Scroll to the Custom Components section.
   3. Select the newly created **Cards component** to insert it into your form.

        ![Select Custom Component](/help/edge/docs/forms/universal-editor/assets/select-custom-component.png)

As no code is present inside `cards.js` the custom component is rendered as a radio group.

#### 1.3 Preview and Test Locally

Now that the form contains the custom component, you can proxy the form and make changes to it locally and see the changes:

1. Go to your terminal and run `aem up`.

2. Open the proxy server started at `http://localhost:3000/{path-to-your-form}` (path example: `/content/forms/af/custom-component-form`)


### 2. Implementing Custom Behaviour for your Custom Component

#### 2.1 Styling the Custom Component

Let's add a class **card** to the component for styling and add an image for each radio, use the below code for this.

**Style the Custom Component using decorate function in cards.js**

```javascript
import { createOptimizedPicture } from '../../../../scripts/aem.js';

export default function decorate(element, fieldJson, container, formId) {
  element.classList.add('card');

  element.querySelectorAll('.radio-wrapper').forEach((radioWrapper) => {
    const image = createOptimizedPicture(
      'https://main--afb--jalagari.hlx.live/lab/images/card.png',
      'card-image'
    );
    radioWrapper.appendChild(image);
  });

  return element;
}
```

**Add Runtime Behaviour for the Custom Component in cards.css**

```javascript
.card .radio-wrapper {
  min-width: 320px; /* or whatever width fits your design */
  max-width: 340px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  flex: 0 0 auto;
  scroll-snap-align: start;
  padding: 24px 16px;
  margin-bottom: 0;
  position: relative;
  transition: box-shadow 0.2s;
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
```

Now, the cards component appears like this:

![add card css and js](/help/edge/docs/forms/universal-editor/assets/add-card-css.png)

#### 2.2 Adding Dynamic Behavior using Subscribe Function

When the dropdown is changed the cards are fetched and set in the enum of the radio group. But currently the view doesn't handle this. So it renders as shown below:

![subscribe function](/help/edge/docs/forms/universal-editor/assets/card-subscribe.png)

When API is called it sets the field Model and must listen to the changes and accordingly render the view. This is achieved using the **subscribe function**.

Let's convert the view code in previous step to a function and call this inside the subscribe function in `cards.js` as shown below:

```javascript
import { createOptimizedPicture } from '../../../../scripts/aem.js';
import { subscribe } from '../../rules/index.js';

function createCard(element, enums) {
  element.querySelectorAll('.radio-wrapper').forEach((radioWrapper, index) => {
    if (enums[index]?.name) {
      let label = radioWrapper.querySelector('label');

      if (!label) {
        label = document.createElement('label');
        radioWrapper.appendChild(label);
      }

      label.textContent = enums[index]?.name;
    }

    const image = createOptimizedPicture(
      enums[index]?.image || 'https://main--afb--jalagari.hlx.page/lab/images/card.png',
      'card-image'
    );

    radioWrapper.appendChild(image);
  });
}

export default function decorate(element, fieldJson, container, formId) {
  element.classList.add('card');
  createCard(element, fieldJson.enum);

  subscribe(element, formId, (fieldDiv, fieldModel) => {
    fieldModel.subscribe((e) => {
      const { payload } = e;

      payload?.changes?.forEach((change) => {
        if (change?.propertyName === 'enum') {
          createCard(element, change.currentValue);
        }
      });
    });
  });

  return element;
}
```

**Use Subscribe Function to Listen the Event Changes in cards.js**

Now when you change the dropdown the cards get populated as shown below:

![subscribe function](/help/edge/docs/forms/universal-editor/assets/card-subscribe-final.png)

#### 2.3 Syncing View Updates with Field Model

To sync the view changes to field Model, you must set the value of selected card. So, add the following change event listener in cards.js as shown below:

**Using Field Model API in cards.js**

```javascript
import { createOptimizedPicture } from '../../../../scripts/aem.js';
import { subscribe } from '../../rules/index.js';

function createCard(element, enums) {
  element.querySelectorAll('.radio-wrapper').forEach((radioWrapper, index) => {
    if (enums[index]?.name) {
      let label = radioWrapper.querySelector('label');

      if (!label) {
        label = document.createElement('label');
        radioWrapper.appendChild(label);
      }

      label.textContent = enums[index]?.name;
    }

    // Attach index to input element for later reference
    radioWrapper.querySelector('input').dataset.index = index;

    const image = createOptimizedPicture(
      enums[index]?.image || 'https://main--afb--jalagari.hlx.page/lab/images/card.png',
      'card-image'
    );

    radioWrapper.appendChild(image);
  });
}

export default function decorate(element, fieldJson, container, formId) {
  element.classList.add('card');
  createCard(element, fieldJson.enum);

  subscribe(element, formId, (fieldDiv, fieldModel) => {
    fieldModel.subscribe((e) => {
      const { payload } = e;

      payload?.changes?.forEach((change) => {
        if (change?.propertyName === 'enum') {
          createCard(element, change.currentValue);
        }
      });
    });

    element.addEventListener('change', (e) => {
      e.stopPropagation();
      const value = fieldModel.enum?.[parseInt(e.target.dataset.index, 10)];
      fieldModel.value = value.name;
    });
  });

  return element;
}
```

Now the custom card component appears, as shown below:

![Card custom Component](/help/edge/docs/forms/universal-editor/assets/cc-ue-card-component.png)

### 3. Commit and Push Changes

Once you've implemented the JavaScript and CSS for your custom component and verified it locally, commit and push the changes to your Git repository.

```bash
git add . && git commit -m "Add card custom component" && git push
```

You have successfully created a complex custom card selection component in a few simple steps.

+++ **Manual or Legacy Method to Create Custom Component**

The legacy way to do this is to manually follow the steps described below:

1. **Choose an OOTB component** to extend (e.g., button, drop-down, text-input, etc.). In this case, extend the radio component.

2. **Create a folder** in `blocks/form/components` with your component's name (cards in this case).

3. **Add a JS file** with the same name: 
     - `blocks/form/components/cards/cards.js`.

4. (Optional) **Add a CSS file** for custom styles:  
     - `blocks/form/components/cards/cards.css.`

5. **Define a new JSON file** (e.g.,` _cards.json`) in the same folder as your **component JS file** (`blocks/form/components/cards/_cards.json`). This JSON should extend an existing component and in its definitions, set `fd:viewType` to your component's name (cards in this case):

     - For all field groups (basic, validation, help, etc.) add your custom fields explicitly.

6. **Implement the JS and CSS logic:**
      - Export a default function as described above.
      - Use the **element** parameter to modify the base HTML structure.
      - Use the **fieldJson** parameter if needed for standard field data.
      - Use **subscribe** function to listen to field changes or custom events if needed.

        >[!NOTE]
        >
        >Implement the JS and CSS logic for your custom component as explained above.

7. Register your component as a variant in the form builder and set the variant property or
`fd:viewType/:type` in the JSON to your component's name, for example, add the `fd:viewType` value from the `definitions[]` as cards to the components array of the object with `id="form`.

    ```
        {
      "definitions": [
        {
          "title": "Cards",
          "id": "cards",
          "plugins": {
            "xwalk": {
              "page": {
                "resourceType": "core/fd/components/form/radiobutton/v1/radiobutton",
                "template": {
                  "jcr:title": "Cards",
                  "fieldType": "radio-button",
                  "fd:viewType": "cards",
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

8. **Update mappings.js**: Add your component's name to the **OOTBComponentDecorators** (for OOTB- style components) or **customComponents** list so it is recognized and loaded by the system.

    ```javascript
    let customComponents = ["cards"];
    const OOTBComponentDecorators = [];
    ```

9. **Update _form.json**: Add your component's name to the `filters.components` array so it can be dropped in the authoring UI.

    ```javascript
    "filters": [
    {
        "id": "form",
        "components": [ "cards"]}
        ]
    ```

10. **Update _component-definition.json**: In `models/_component-definition.json` update the array within the group with `id custom-components` with an object in the following manner:

    ```javascript
    {
    "...":"../blocks/form/components/cards/_cards.json#/definitions"
    }

    ```

    This is to provide the reference to the new cards component to be built with the rest of the components

11. **Run the build:json script**: Execute `npm run build:json` to compile and merge all component JSON definitions into a single file to be served from the server. This ensures your new component's schema is included in the merged output.

12. Commit and push your changes to your Git repository.

Now, you can add the custom component to your form.

+++

## Create a Composite Component

A composite component is created by combining multiple components.
For example, a Terms and Conditions composite component consists of a parent panel that contains:

- A plain-text field for displaying the terms

- A checkbox for capturing the user's agreement

This composition structure is defined as a template inside the respective component's JSON file. The following example shows how to define a template for a Terms and Conditions component:

```javascript
{
  "definitions": [
    {
      "title": "Terms and conditions",
      "id": "tnc",
      "plugins": {
        "xwalk": {
          "page": {
            "resourceType": "core/fd/components/form/termsandconditions/v1/termsandconditions",
            "template": {
              "jcr:title": "Terms and conditions",
              "fieldType": "panel",
              "fd:viewType": "tnc",
              "text": {
                "value": "Text related to the terms and conditions come here.",
                "sling:resourceType": "core/fd/components/form/text/v1/text",
                "fieldType": "plain-text",
                "textIsRich": true
              },
              "approvalcheckbox": {
                "name": "approvalcheckbox",
                "jcr:title": "I agree to the terms & conditions.",
                "sling:resourceType": "core/fd/components/form/checkbox/v1/checkbox",
                "fieldType": "checkbox",
                "required": true,
                "type": "string",
                "enum": [
                  "true"
                ]
              }
            }
          }
        }
      }
    }
  ],
  ...
}
```
 
## Best Practices

Keep the below points in mind before creating your own custom component:

- **Keep your component logic focused**: Only add/override what is necessary for your custom behavior

- **Leverage the base structure**: Use the OOTB HTML as your starting point

- **Use authorable properties:** Expose configurable options via the JSON schema

- **Namespace your CSS**: Avoid style collisions by using unique class names

## References

- form-field-types: Base HTML structures and properties for all field types. [Click here](/help/edge/docs/forms/eds-form-field-properties) to view detailed form field structures and properties.

- **blocks/form/models/form-components**: OOTB and custom component property definitions.

- **blocks/form/components**: Place for your custom components. For example: `blocks/form/components/countdown-timer/_countdown-timer.json` shows how to extend a base component and add new properties.
