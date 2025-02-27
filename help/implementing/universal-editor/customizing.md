---
title: Customizing the Universal Editor
description: Learn about the different options to customize the Universal Editor to support the needs of your content authors.
exl-id: 8d6523c8-b266-4341-b301-316d5ec224d7
feature: Developing
role: Admin, Architect, Developer
---

# Customizing the Universal Editor {#customizing}

Learn about the different options to customize the Universal Editor to support the needs of your content authors.

>[!TIP]
>
>The Universal Editor also offers many [extension points,](/help/implementing/universal-editor/extending.md) allowing you to expand its functionality to meet your project needs.

## Disabling Publishing {#disable-publish}

Certain authoring workflows require content to be reviewed before it is published. In such situations, the option to publish should not be available to any authors.

The **Publish** button can therefore be suppressed entirely in an app by adding the following metadata.

```html
<meta name="urn:adobe:aue:config:disable" content="publish"/>
```

## Disabling Publishing to Preview {#publish-preview}

Certain authoring workflows might preclude the publication to the [preview service](/help/sites-cloud/authoring/sites-console/previewing-content.md) (if available).

The **Preview** option in the publish window can therefore be suppressed entirely in an app by adding the following metadata.

```html
<meta name="urn:adobe:aue:config:disable" content="publish-preview"/>
```

## Filtering Components {#filtering-components}

You can restrict the allowed components per container in the Universal Editor using component filters. Please see the document [Filtering Components](/help/implementing/universal-editor/filtering.md) for more information.

## Conditionally Show and Hide Components in Properties Panel {#conditionally-hide}

Although a component or components may generally be available to your authors, there may be certain situations where it does not make sense. In such cases, you can hide components in the properties panel by adding a `condition` attribute to the [fields of the component model](/help/implementing/universal-editor/field-types.md#fields).

Conditions can be defined using [JsonLogic schema](https://jsonlogic.com/). If the condition is true, then the field will be displayed. If the condition is false, then the field will be hidden.

>[!BEGINTABS]

>[!TAB Sample Model]

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

>[!TAB Condition False]

![Hidden text field](assets/hidden.png)

>[!TAB Condition True]

![Shown text field](assets/shown.png)

>[!ENDTABS]

## Custom Preview URLs {#custom-preview-urls}

You can specify a custom preview URL via a `urn:adobe:aue:config:preview` meta configuration, which will open when clicking the **Open page** button in the [editor's top-right toolbar](/help/sites-cloud/authoring/universal-editor/navigation.md#universal-editor-toolbar).

This is particularly useful for applications with specific preview requirements, such as those [using Edge Delivery Services with WYSIWYG authoring](/help/edge/wysiwyg-authoring/authoring.md).

To do so, simply include the desired preview URL in a meta tag of the instrumented app like the following example.

```html
<meta name="urn:adobe:aue:config:preview" content="https://wknd.site"/>
```
