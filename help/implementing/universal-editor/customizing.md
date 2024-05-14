---
title: Customizing the Universal Editor Authoring Experience
description: Learn about the different extension points and other features that allow you to customize the UI of the Universal Editor to support the needs of your content authors.
exl-id: 8d6523c8-b266-4341-b301-316d5ec224d7
---

# Customizing the Universal Editor Authoring Experience {#customizing-ue}

Learn about the different extension points and other features that allow you to customize the authoring experience of the Universal Editor to support the needs of your content authors.

## Disabling Publishing {#disable-publish}

Certain authoring workflows require content to be reviewed before it is published. In such situations, the option to publish should not be available to any authors.

The **Publish** button can therefore be suppressed entirely in an app by adding the following metadata.

```html
<meta name="urn:adobe:aue:config:disable" content="publish"/>
```

## Filtering Components {#filtering-components}

When using the the Universal Editor, you can restrict the allowed components per container component. To do this, you must introduce an additional script tag, which points to the filter definition.

```html
<script type="application/vnd.adobe.aue.filter+json" src="/static/filter-definition.json"></script>
```

A filter definition might look like the following, which would restrict a container to only allow adding text and images.

```json
[
  {
    "id": "container-filter",
     "components": ["text", "image"]
   }
]
```

Then you can reference the filter definition from your container component by adding the property `data-aue-filter`, passing the ID of the filter you defined previously.

```html
data-aue-filter="container-filter"
```

Setting the `components` attribute in a filter definition to `null` allows all components, as if there were no filter.

```json
[
  {
    "id": "another-container-filter",
     "components": null
   }
]
```

## Conditionally Show and Hide Components in Properties Rail {#conditionally-hide}

Although a component or components may generally be available to your authors, there may be certain situations where it does not make sense. In such cases, you can hide components in the properties rail by adding a `condition` attribute to the [fields of the component model.](/help/implementing/universal-editor/field-types.md#fields)

Conditions can be defined using [JsonLogic schema.](https://jsonlogic.com/) If the condition is true, then the field will be displayed. If the condition is false, then the field will be hidden.

### Sample Model {#sample-model}

```json
 {
    "id": "conditionally-revealed-component",
    "fields": [
      {
        "component": "boolean",
        "label": "Shall the text field be revealed?",
        "name": "reveal",
        "valueType": "boolean"
      },
      {
        "component": "text-input",
        "label": "Hidden text field",
        "name": "hidden-text",
        "valueType": "string",
        "condition": { "===": [{"var" : "reveal"}, true] }
      }
    ]
 }
```

#### Condition False {#false}

![Hidden text field](assets/hidden.png)

#### Condition True {#true}

![Shown text field](assets/shown.png)

