---
title: Model Definitions and Field Types
description: Learn about fields and the component types that the Universal Editor can edit in the properties rail with examples. Understand how you can instrument your own app by creating a model definition and linking to the component.
exl-id: cb4567b8-ebec-477c-b7b9-53f25b533192
---

# Model Definitions and Field Types {#field-types}

Learn about fields and the component types that the Universal Editor can edit in the properties rail with examples. Understand how you can instrument your own app by creating a model definition and linking to the component.

{{universal-editor-status}}

## Overview {#overview}

When adapting your own apps for use with the Universal Editor, you must instrument the components and define what fields and component types they can manipulate in the properties rail of the editor. You do this by creating a model and linking to that from the component.

This document provides an overview of a model definition and of fields and the component types available to you along with example configurations.

>[!TIP]
>
>If you are not familiar with how to instrument your app for the Universal Editor, please see the document [Universal Editor Overview for AEM Developers.](/help/implementing/universal-editor/developer-overview.md)

## Model Definition Structure {#model-structure}

In order to configure a component via the properties rail in the Universal Editor, a model definition has to exist and be linked to the component.

The model definition is a JSON structure, starting with an array of models.

```json
[
  {
    "id": "model-id",        // must be unique
    "fields": []             // array of fields which shall be rendered in the properties rail
  }
]
```

See the **[Fields](#fields)** section of this document for more information about how to define your `fields` array.

To use the model definition with a component, the `data-aue-model` attribute can be used.

```html
<div data-aue-resource="urn:datasource:/content/path" data-aue-type="component"  data-aue-model="model-id">Click me</div>
```

## Loading a Model Definition {#loading-model}

Once a model is created, it can be referenced as an external file.

```html
    <script type="application/vnd.adobe.aue.model+json" src="<url-of-model-definition>"></script>
```

Alternatively you can also define the model inline.

```html
    <script type="application/vnd.adobe.aue.model+json">
      { ... model definition ... }
    </script>
```

## Fields {#fields}

The field object has the following type definition.

|Configuration|Value Type|Description|Required|
|---|---|---|---|
|`component`|`ComponentType`|Renderer of the component|Yes|
|`name`|`string`|Property where the data shall be persisted|Yes|
|`label`|`FieldLabel`|Label of the field|Yes|
|`description`|`FieldDescription`|Description of the field|No|
|`placeholder`|`string`|Placeholder for the field|No|
|`value`|`FieldValue`|Default value|No|
|`valueType`|`ValueType`|Standard validation, can be `string`, `string[]`, `number`, `date`, `boolean`|No|
|`required`|`boolean`|Is the field required|No|
|`readOnly`|`boolean`|Is the field read only|No|
|`hidden`|`boolean`|Is the field hidden by default|No|
|`condition`|`RulesLogic`|Rule to show or hide the field|No|
|`multi`|`boolean`|Is the field a multi field|No|
|`validation`|`ValidationType`|Validation rule or rules for the field|No|
|`raw`|`unknown`|Raw data which can be used by the component|No|

### Component Types {#component-types}

The following are the component types that are possible to use for rendering fields.

#### AEM Tag {#aem-tag}

An AEM tag component type enables an AEM tag picker, which can be used to attach tags to the component.

##### Sample {#sample-aem-tag}

```json
[
  {
    "id": "aem-tag-picker",
    "fields": [
      {
        "component": "aem-tag",
        "label": "AEM Tag Picker",
        "name": "cq:tags",
        "valueType": "string"
      }
    ]
  }
]
```

##### Screenshot {#screenshot-aem-tag}

![Screenshot of AEM tag component type](assets/component-types/aem-tag-picker.png)

#### AEM Content {#aem-content}

An AEM content component type type enables an AEM content picker, which can be used to set content references.

##### Sample {#sample-aem-content}

```json
[
  {
    "id": "aem-content-picker",
    "fields": [
      {
        "component": "aem-content",
        "name": "reference",
        "value": "",
        "label": "AEM Content Picker",
        "valueType": "string"
      }
    ]
  }
]
```

##### Screenshot {#screenshot-aem-content}

![Screenshot of AEM content component type](assets/component-types/aem-content-picker.png)

#### Boolean {#boolean}

A boolean component type stores a simple true/false value rendered as a toggle. It offers an additional validation type.

|Validation Type|Value Type|Description|Required|
|---|---|---|---|
|`customErrorMsg`|`string`|Message that will display if the value entered isn't a boolean value|No|

##### Sample {#sample-boolean}

```json
{
    "id": "boolean",
    "fields": [
      {
        "component": "boolean",
        "label": "Boolean",
        "name": "boolean",
        "valueType": "boolean"
      }
    ]
  }
```

##### Screenshot {#screenshot-boolean}

![Screenshot of boolean component type](assets/component-types/boolean.png)

#### Checkbox Group {#checkbox-group}

Similar to a boolean, a checkbox group component type allows for the selection of multiple true/false items, rendered as multiple checkboxes.

##### Sample {#sample-checkbox-group}

```json
{
    "id": "checkbox-group",
    "fields": [
      {
        "component": "checkbox-group",
        "label": "Checkbox Group",
        "name": "checkbox",
        "valueType": "string[]",
        "value": [],
        "options": [
          { "name": "Option 1", "value": "option1" },
          { "name": "Option 2", "value": "option2" }
        ]
      }
    ]
}
```

#### Screenshot {#screenshot-checkbox-group}

![Screenshot of checkbox group component type](assets/component-types/checkbox-group.png)

#### Container {#container}

A container component type allows the grouping of components. It offers an additional configuration.

|Configuration|Value Type|Description|Required|
|---|---|---|---|
|`collapsible`|`boolean`|Is the container collapsible|No|

##### Sample {#sample-container}

```json
 {
    "id": "container",
    "fields": [
      {
        "component": "container",
        "label": "Container",
        "name": "container",
        "valueType": "string",
        "collapsible": true,
        "fields": [
          {
            "component": "text-input",
            "label": "Simple Text 1",
            "name": "text",
            "valueType": "string"
          },
          {
            "component": "text-input",
            "label": "Simple Text 2",
            "name": "text2",
            "valueType": "string"
          }
        ]
      }
    ]
  }
```

##### Screenshot {#screenshot-container}

![Screenshot of container component type](assets/component-types/container.png)

#### Date Time {#date-time}

A date time component type allows the specification of a date, time, or combination thereof. It offers additional configurations.

|Configuration|Value Type|Description|Required|
|---|---|---|---|
|`displayFormat`|`string`|Format with which to display the date string|Yes|
|`valueFormat`|`string`|Format in which to store the date string|Yes|

It also offers an additional validation type.

|Validation Type|Value Type|Description|Required|
|---|---|---|---|
|`customErrorMsg`|`string`|Message that will display if `valueFormat` isn't met|No|

##### Sample {#sample-date-time}

```json
{
    "id": "date-time",
    "fields": [
      {
        "component": "date-time",
        "label": "Date & Time",
        "name": "date",
        "valueType": "date"
      }
    ]
  }
```

##### Screenshot {#screenshot-date-time}

![Screenshot of date time component type](assets/component-types/date-time.png)

#### Multiselect {#multiselect}

A multiselect component type presents multiple items for selection in a drop-down including the ability to group the selectable elements.

##### Samples {#sample-multiselect}

```json
{
    "id": "multiselect",
    "fields": [
      {
        "component": "multiselect",
        "name": "multiselect",
        "label": "Multi Select",
        "valueType": "string",
        "options": [
          { "name": "Option 1", "value": "option1" },
          { "name": "Option 2", "value": "option2" }
        ]
      }
    ]
}
```

```json
 {
    "id": "multiselect-group",
    "fields": [
      {
        "component": "multiselect",
        "name": "property",
        "label": "Multiselect field",
        "valueType": "string",
        "required": true,
        "maxSize": 2,
        "options": [
          {
            "name": "Theme",
            "children": [
              {
                "name": "Light",
                "value": "light"
              },
              {
                "name": "Dark",
                "value": "dark"
              }
            ]
          },
          {
            "name": "Type",
            "children": [
              {
                "name": "Alpha",
                "value": "alpha"
              },
              {
                "name": "Beta",
                "value": "beta"
              },

              {
                "name": "Gamma",
                "value": "gamma"
              }
            ]
          }
        ]
      }
    ]
  }
```

##### Screenshots {#screenshot-multiselect}

![Screenshot of multiselect component type](assets/component-types/multiselect.png)
![Screenshot of multiselect component type with grouping](assets/component-types/multiselect-group.png)

#### Number {#number}

A number component type allows for the input of a number. It offers additional validation types.

|Validation Type|Value Type|Description|Required|
|---|---|---|---|
|`numberMin`|`number`|Minimum number allowed|No|
|`numberMax`|`number`|Maximum number allowed|No|
|`customErrorMsg`|`string`|Message that will display if `numberMin` or `numberMax` isn't met|No|

##### Sample {#sample-number}

```json
{
    "id": "number",
    "fields": [
      {
        "component": "number",
        "name": "number",
        "label": "Number",
        "valueType": "number",
        "value": 0
      }
    ]
}
```

##### Screenshot {#screenshot-number}

![Screenshot of number component type](assets/component-types/number.png)

#### Radio Group {#radio-group}

A radio group component type allows for a mutually-exclusive selection from multiple options rendered as a group similar to a checkbox group.

##### Sample {#sample-radio-group}

```json
{
    "id": "radio-group",
    "fields": [
      {
        "component": "radio-group",
        "label": "Radio Group",
        "name": "radio",
        "valueType": "string",
        "options": [
          { "name": "Option 1", "value": "option1" },
          { "name": "Option 2", "value": "option2" }
        ]
      }
    ]
}
```

##### Screenshot {#screenshot-radio-group}

![Screenshot of radio group component type](assets/component-types/radio.png)

#### Reference {#reference}

A reference component type allows for a reference to another data object from the current object.

##### Sample {#sample-reference}

```json
{
    "id": "reference",
    "fields": [
      {
        "component": "reference",
        "label": "Reference",
        "name": "reference",
        "valueType": "string"
      }
    ]
}
```

##### Screenshot {#screenshot-reference}

![Screenshot of reference component type](assets/component-types/reference.png)

#### Select {#select}

A select component type allows for selection of a single option from a list of predefined options in a drop-down menu.

##### Sample {#sample-select}

```json
{
    "id": "select",
    "fields": [
      {
        "component": "select",
        "label": "Select",
        "name": "select",
        "valueType": "string",
        "options": [
          { "name": "Option 1", "value": "option1" },
          { "name": "Option 2", "value": "option2" }
        ]
      }
    ]
}
```

##### Screenshot {#screenshot-select}

![Screenshot of select component type](assets/component-types/select.png)

#### Tab {#tab}

A tab component type allows you to group other input fields together on multiple tabs to improve layout organization for the authors.

A `tab` definition can be thought of as a separator in the array of `fields`. Everything that comes after a `tab` will be placed on that tab until a new `tab` is encountered, whereafter the following items will be placed on the new tab.

If you wish to have items that appear above all tabs, they must be defined before any tabs.

##### Sample {#sample-tab}

```json
{
    "id": "tab",
    "fields": [
      {
        "component": "tab",
        "label": "Tab 1",
        "name": "tap1"
      },
      {
        "component": "text-input",
        "label": "Text 1",
        "name": "text1",
        "valueType": "string"
      },
      {
        "component": "tab",
        "label": "Tab 2",
        "name": "tap2"
      },
      {
        "component": "text-input",
        "label": "Text 2",
        "name": "text2",
        "valueType": "string"
      }
    ]
  }
```

##### Screenshot {#screenshot-tab}

![Screenshot of tab component type](assets/component-types/tab.png)

#### Text Area {#text-area}

A text area allows for multi-line, rich text input. It offers additional validation types.

|Validation Type|Value Type|Description|Required|
|---|---|---|---|
|`maxSize`|`number`|Maximum number characters allowed|No|
|`customErrorMsg`|`string`|Message that will display if `maxSize` is exceeded|No|

##### Sample {#sample-text-area}

```json
{
    "id": "richtext",
    "fields": [
      {
        "component": "text-area",
        "name": "rte",
        "label": "Rich Text",
        "valueType": "string"
      }
    ]
}
```

##### Screenshot {#screenshot-text-area}

![Screenshot of text area component type](assets/component-types/richtext.png)

#### Text Input {#text-input}

A text input allows for a single line of text input.  It includes additional validation types.

|Validation Type|Value Type|Description|Required|
|---|---|---|---|
|`minLength`|`number`|Minimum number of characters allowed|No|
|`maxLength`|`number`|Maximum number of characters allowed|No|
|`regExp`|`string`|Regular expression which the input text must match|No|
|`customErrorMsg`|`string`|Message that will display if `minLength`, `maxLength`, and/or `regExp` is/are violated|No|

##### Sample {#sample-text-input}

```json
{
    "id": "simpletext",
    "fields": [
      {
        "component": "text-input",
        "name": "text",
        "label": "Simple Text",
        "valueType": "string"
      }
    ]
 }
```

##### Screenshot {#screenshot-text-input}

![Screenshot of text input component type](assets/component-types/simpletext.png)
