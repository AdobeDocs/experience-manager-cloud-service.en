---
title: Field Types for the Universal Editor
description: Learn about the different types of fields that the Universal Editor supports and what you can instrument for your own apps.
---

# Field Types for the Universal Editor {#field-types}

Learn about the different types of fields that the Universal Editor supports and what you can instrument for your own apps.

## Overview {#overview}

When adapting your own apps for use with the Universal Editor, you must instrument the components and define what data types they can manipulate in the editor. 

This document provides an overview of the field types available to you in the editor.

>[!TIP]
>
>If you are not familiar with how to instrument your app for the Universal Editor, please see the document [Universal Editor Overview for AEM Developers.](help/implementing/universal-editor/developer-overview.md)

## Boolean {#boolean}

A boolean field stores a simple true/false value rendered as a checkbox.

### Sample {#sample-boolean}

```json
{
  "fields": [   
   {
      "component": "boolean",
      "valueType": "boolean",
      "name": "field4",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "placeholder": null,
      "validation": {
        "customErrorMsg": "hehe"
      }
    }
  ]
}
```

## Checkbox Group {#checkbox-group}

Similar to a boolean, a checkbox group allows for the selection of multiple true/false items.

### Sample {#sample-checkbox-group}

```json
{
  "fields": [   
   {
      "component": "checkbox-group",
      "valueType": "string-array",
      "name": "field9",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "placeholder": null,
      "options": [
        { "name": "One", "value": "one" },
        { "name": "Two", "value": "two" },
        { "name": "Three", "value": "three" }
      ]
    }
  ]
}
```

## Date Time {#date-time}

A date time field allows the specification of a date or time or combination thereof.

### Sample {#sample-date-time}

```json
{
  "fields": [   
      {
      "component": "date-time",
      "valueType": "date-time",
      "name": "field5",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "placeholder": "YYYY-MM-DD HH:mm:ss",
      "displayFormat": null,
      "valueFormat": null,
      "validation": {
        "customErrorMsg": "hehe"
      }
    },
    {
      "component": "date-time",
      "valueType": "date",
      "name": "field6",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "placeholder": "YYYY-MM-DD",
      "displayFormat": null,
      "valueFormat": null,
      "validation": {
        "customErrorMsg": "hehe"
      }
    },
    {
      "component": "date-time",
      "valueType": "time",
      "name": "field7",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "placeholder": "HH:mm:ss",
      "displayFormat": null,
      "valueFormat": null,
      "validation": {
        "customErrorMsg": "hehe"
      }
    }
  ]
}
```

## Number {#number}

A number field allows for the input of a number.

### Sample {#sample-number}

```json
{
  "fields": [   
   {
      "component": "number",
      "valueType": "number",
      "name": "field8",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "placeholder": null,
      "validation": {
        "numberMin": null,
        "numberMax": null,
        "customErrorMsg": "hehe"
      }
    }
  ]
}
```

## Radio Group {#radio-group}

A radio group allows for a mutually-exclusive selection from multiple options rendered as a group similar to a checkbox group.

### Sample {#sample-radio-group}

```json
{
  "fields": [   
   {
      "component": "radio-group",
      "valueType": "string",
      "name": "field10",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "placeholder": null,
      "options": [
        { "name": "One", "value": "one" },
        { "name": "Two", "value": "two" },
        { "name": "Three", "value": "three" }
      ]
    }
  ]
}
```

## Reference {#reference}

A reference allows for the specification of another data object as a reference from the current object.

## Select {#select}

A select allows for selection of one or more predefined options in a drop-down menu.

### Sample {#sample-select}

```json
{
  "fields": [   
   {
      "component": "select",
      "valueType": "string",
      "name": "field9",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "placeholder": null,
      "options": [
        { "name": "One", "value": "one" },
        { "name": "Two", "value": "two" },
        { "name": "Three", "value": "three" }
      ],
      "emptyOption": true
    }
  ]
}
```

## Text Area {#text-area}

A text area allows for multi-line text input.

### Sample {#sample-text-area}

```json
{
  "fields": [   
   {
      "component": "text-area",
      "valueType": "string",
      "name": "field3",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "multi": true,
      "placeholder": null,
      "mimeType": "text/x-markdown"
    }
  ]
}
```

## Text Input {#text-input}

A text input allows for a single line of text input.

### Sample {#sample-text-input}

```json
{
  "fields": [   
   {
      "component": "text-input",
      "valueType": "string",
      "name": "field1",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "multi": true,
      "placeholder": null
    },
    {
      "component": "text-input",
      "valueType": "string",
      "name": "field2",
      "label": "xyz",
      "description": "xyz",
      "required": true,
      "multi": true,
      "placeholder": null,
      "validation": {
        "minLength": 5,
        "maxLength": 10,
        "regExp": "^foo:.*",
        "customErrorMsg": "hehe"
      }
    }
  ]
}
```

