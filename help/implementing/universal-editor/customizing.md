---
title: Customizing the UI
description: Learn about the different extension points that allow you to customize the UI of the Universal Editor to support the needs of your content authors.
exl-id: 8d6523c8-b266-4341-b301-316d5ec224d7
---

# Customizing the UI {#customizing-ui}

Learn about the different extension points that allow you to customize the UI of the Universal Editor to support the needs of your content authors.

## Disabling Publishing {#disable-publish}

Certain authoring workflows require content to be reviewed before it is published. In such situations, the option to publish should not be available to any authors.

The **Publish** button can therefore be suppressed enitrely in an app by adding the following metadata.

```html
<meta name="urn:adobe:aue:config:disable" content="publish"/>
```

## Filtering Components {#filtering-components}

When using the the Universal Editor, you can restrict the allowed components per container. To do this, you must introduce an additional script tag, which points to the filter definition.

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

Then you can reference the filter definition from your container.

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
