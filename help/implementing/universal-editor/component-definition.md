---
title: Component Definition
description: Understand the JSON contract between the component definition and the Universal Editor in detail.
feature: Developing
role: Admin, Architect, Developer
---

# Component Definition {#component-definition}

Understand the JSON contract between the component definition and the Universal Editor in detail.

## Overview {#overview}

The `component-definition.json` file defines the components available to your content authors for the project. This document explains in detail the purpose of this file and how the Universal Editor uses it to present your authors with page authoring components.

>[!TIP]
>
>You do not need to create your own `component-definition.json` file from scratch. The project boilerplate that you use to [bootstrap your project](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md) contains a fully-functioning `component-definition.json` file that you can adapt to your needs.

## Example Component Definition {#example}

The following is a complete, but simplified `component-definition.json` file for reference.

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

* `title` defines the textual description of the group shown in the UI.
* `id` uniquely identifies the group.

## `components` {#components}

`components` defines which components belong to a group.

* `title` defines the textual description of the component shown in the UI.
* `id` uniquely identifies the component.

## `plugins` {#plugins}

`plugins` defines which plugin is responsible for creating/editing the component. Common plugins include:

* `aem` for AEM as a Cloud Service
* `aem5` for AEM 6.5
* `xwalk` for AEM as a Cloud Service WYSIWYG authoring

## `page` or `cf` {#page-cf}

Once the `plugin` is defined, you need to indicate if it is page or fragment-related.

* `page` indicates that the component is content on the current page.
* `cf` indicates that the component is related to content within a [Content Fragment.](/help/assets/content-fragments/content-fragments.md)

### `page` {#page}

If the component is content on the page, you can provide the following information.

* `name` defines an optional name saved to the JCR for the newly-created component.
* `resourceType` defines the [Sling](/help/implementing/developing/introduction/sling-cheatsheet.md) `resourceType` used for rendering the component.
* `template` defines optional key/values to be automatically written to the newly-created component.
  * Useful for explanatory, sample, or placeholder text.

### `cf` {#cf}

If the component is related to content within a Content Fragment, you can provide the following information.

* `name` defines an optional name saved to the JCR for the newly-created component.
* `cfModel` defines the Content Fragment model for the newly-created component.
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
