---
title: Filters
description: Learn how you can define filters to limit options available in the editor such as available components, RTE options, and asset selection.
feature: Developing
role: Admin, Developer
exl-id: eeae8d7c-c563-4d9b-8c54-1098a4e98c18
---

# Filters {#filters}

Learn how you can define filters to limit options available in the editor such as available components, RTE options, and asset selection.

## Configuring Filters {#configuring-filters}

When using the Universal Editor, you can restrict the options allowed for certain functionality by defining a filter. A filter is a list of items or actions available to the specific context. For example you can filter the components available to be inserted into a container, you can [filter the options available in the RTE,](/help/implementing/universal-editor/configure-rte.md) and you can [filter the assets available](/help/implementing/universal-editor/configure-assets-selector.md) in the assets selector.

The filters must all be defined similarly.

1. [Add script tag to point to filter definition](#add-tag)
1. [Define the filter](#define-filter)
1. [Reference the filter from the affected item](#reference-filter)

Let's take an example of filtering components per container component. 

## Reference Filter Definition {#add-tag}

First introduce an additional script tag, which points to the filter definition.

For our example to filter allowed components per container, the tag might look something like this.

```html
<script type="application/vnd.adobe.aue.filter+json" src="/static/filter-definition.json"></script>
```

## Define the Filter {#define-filter}

A filter definition contains JSON with an ID unique to the filter and the filter criteria.

For our example to filter allowed components per container, it might look like the following, which would restrict a container to only allow adding text and images.

```json
[
  {
    "id": "container-filter",
    "components": ["text", "image"]
   }
]
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

## Reference the Filter from the Item {#reference-filter}

To use the filter, you must reference the filter definition.

For our example to filter allowed components per container, you would reference the filter from your container component by adding the property `data-aue-filter`, passing the ID of the filter you defined previously.

```html
data-aue-filter="container-filter"
```

>[!TIP]
>
>Learn about other customization and extension options available to the Universal Editor in the documents:
>
>* [Configuring the RTE for the Universal Editor](/help/implementing/universal-editor/configure-rte.md)
>* [Configuring Filters for the Assets Selector](/help/implementing/universal-editor/configure-assets-selector.md)
>* [Customizing the Universal Editor](/help/implementing/universal-editor/customizing.md)
>* [Extending the Universal Editor](/help/implementing/universal-editor/extending.md)
