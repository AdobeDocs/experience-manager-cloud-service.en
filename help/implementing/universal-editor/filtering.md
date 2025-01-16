---
title: Filtering Components
description: Learn how you can restrict the allowed components per container in the Universal Editor using component filters.
feature: Developing
role: Admin, Architect, Developer
---

# Filtering Components {#filtering-components}

Learn how you can restrict the allowed components per container in the Universal Editor using component filters.

## Filters {#filters}

When using the Universal Editor, you can restrict the allowed components per container component. To do this, you must introduce an additional script tag, which points to the filter definition.

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

>[!TIP]
>
>Learn about other customization and extension options available to the Universal Editor in the document [Customizing and Extending the Universal Editor.](/help/implementing/universal-editor/customizing.md)
