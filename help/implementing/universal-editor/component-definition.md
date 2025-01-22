---
title: Component Definition
description: Understand the JSON contract between the component definition and the Universal Editor in detail.
feature: Developing
role: Admin, Architect, Developer
exl-id: e1bb1a54-50c0-412a-a8fd-8167c6f47d2b
---
# Component Definition {#component-definition}

Understand the JSON contract between the component definition and the Universal Editor in detail.

## Overview {#overview}

The `component-definition.json` file defines the components available to your content authors for the project. This document explains in detail the purpose of this file and how the Universal Editor uses it to present your authors with page authoring components.

>[!TIP]
>
>For an overview of the content modeling process, please see the document [Content Modeling for WYSIWYG Authoring with Edge Delivery Services Projects.](/help/edge/wysiwyg-authoring/content-modeling.md)

>[!TIP]
>
>You do not need to create your own `component-definition.json` file from scratch. The project boilerplate that you use to [bootstrap your project](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md) contains a [fully-functioning `component-definition.json` file](https://github.com/adobe-rnd/aem-boilerplate-xwalk/blob/main/component-definition.json) that you can adapt to your needs.

## Example Component Definition {#example}

The following is a complete, but simple `component-definition.json` as an example.

```json
{
  "groups": [
    {
      "title": "General Components",
      "id": "general",
      "components": [
        {
          "title": "Text",
          "id": "text",
          "plugins": {
            "aem": {
              "page": {
                "resourceType": "wknd/components/text",
                "template": {
                  "text": "Default Text"
                }
              }
            },
            "aem65": {
              "page": {
                "resourceType": "wknd/components/text",
                "template": {
                  "text": "Default Text"
                }
              }
            }
          }
        },
      }
   ]
}
```

## `groups` {#groups}

`groups` defines the groups of components that the author sees in the Universal Editor when clicking the **Add** icon in the properties panel of the editor to [add a new component to a page.](/help/sites-cloud/authoring/universal-editor/authoring.md#adding-components) Groups help organize the components. Common groups might be **General Components** and **Advanced Components**.

* `title` defines the textual description of the group shown in the editor UI.
* `id` uniquely identifies the group.

## `components` {#components}

`components` defines which components belong to a group.

* `title` defines the textual description of the component shown in the UI.
* `id` uniquely identifies the component.
  * The [component model](/help/implementing/universal-editor/field-types.md#model-structure) of the same `id` defines the fields of the component.
  * Because it is unique it can be used, for example, in a [filter definition](/help/implementing/universal-editor/filtering.md) to determine which components can be added to a container.

## `plugins` {#plugins}

`plugins` defines which plugin is responsible for persisting the component. Common plugins include:

* `aem` for AEM as a Cloud Service.
* `aem5` for AEM 6.5.
* `xwalk` for AEM as a Cloud Service WYSIWYG authoring.

## `page` or `cf` {#page-cf}

Once the `plugin` is defined, you need to indicate if it is page-related or fragment-related.

* `page` indicates that the component is content on the current page.
* `cf` indicates that the component is related to content within a [Content Fragment.](/help/assets/content-fragments/content-fragments.md)

### `page` {#page}

If the component is content on the page, you can provide the following information.

* `name` defines an optional name saved to the JCR for the newly-created component.
  * Informative only and not generally shown in the UI as the `title` is.
* `resourceType` defines the [Sling](/help/implementing/developing/introduction/sling-cheatsheet.md) `resourceType` used for rendering the component.
* `template` defines optional key/values to be automatically written to the newly-created component.
  * Useful for explanatory, sample, or placeholder text.

### `cf` {#cf}

If the component is related to content within a Content Fragment, you can provide the following information.

* `name` defines an optional name saved to the JCR for the newly-created component.
  * Informative only and not generally shown in the UI as the `title` is.
* `cfModel` defines the [Content Fragment](/help/assets/content-fragments/content-fragments-models.md) model for the newly-created component.
* `cfFolder` defines in which folder the Content Fragment shall be created.
* `title` defines the title of the new Content Fragment.
* `description` defines a description of the new Content Fragment.
* `template` defines optional key/values to be automatically written to the newly-created Content Fragment.
  * Useful for explanatory, sample, or placeholder text.

### `cf` Can be Implied {#cf-implied}

If the page is [instrumented](/help/implementing/universal-editor/getting-started.md#instrument-page) to point to a reference field, the `cf` will be assumed.

```html
<div data-aue-resource="urn:aem:/content" data-aue-type="container" data-aue-prop="field"></div>
```

In such a case, `cf` is assumed, because the `data-aue-prop` points to a reference field. Without the `data-aue-prop`, the Universal Editor will assume `page`, because in such case the components are not linked via a reference field.

```html
<div data-aue-resource="urn:aem:/content" data-aue-type="container"></div>
```

Components are simply subnodes below the resource.
