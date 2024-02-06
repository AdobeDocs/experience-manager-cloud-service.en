---
title: Content Modeling for AEM authoring with Edge Delivery Services Projects
description: Learn how content modeling works for AEM authoring with Edge Delivery Services projects and how to model your own content.
---

# Content Modeling for AEM authoring with Edge Delivery Services Projects {#content-modeling}

Learn how content modeling works for AEM authoring with Edge Delivery Services projects and how to model your own content.

{{aem-authoring-edge-early-access}}

## Prerequisites {#prerequisites}

Projects using AEM Authoring with Edge Delivery Services inherit the majority of mechanics of any other Edge Delivery Services project, independent of the content source or [authoring method.](/help/edge/authoring.md)

Before you begin modeling you content for your project, make sure you first read the following documentation.

* [Getting Started - Developer Tutorial](/help/edge/developer/tutorial.md)
* [Markup, Sections, Blocks, and Auto Blocking](/help/edge/developer/markup-sections-blocks.md)
* [Block Collection](/help/edge/developer/block-collection.md)

It is essential to understand those concepts in order to come up with a compelling content model that works in a content source-agnostic way. This document provides details about the mechanics implemented specifically for AEM authoring.

## Default Content {#default-content}

**Default content** is content an author intuitively would put on a page without adding any additional semantics. This includes text, headings, links, and images. Such content is self-explanatory in its function and purpose.

In AEM this content is implemented as components with very simple, pre-defined models, which include everything that can serialized in Markdown and HTML. 

* **Text**: Rich text (including list elements, strong, or italic text)
* **Title**: Text, type (h1-h6)
* **Image**: Source, description
* **Button**: Text, title, url, type (default, primary, secondary)

The model of these components is part of the [Boilerplate for AEM Authoring with Edge Delivery Services.](https://github.com/adobe-rnd/aem-boilerplate-xwalk/blob/main/component-models.json#L2-L112)

## Blocks {#blocks}

Blocks are used to create richer content with specific styles and functionality. In contrast to default content, blocks do require additional semantics. Blocks can be likened to [components in the AEM page editor.](/help/implementing/developing/components/overview.md)

Blocks are essentially pieces of content decorated by Javascript and styled with a stylesheet.

### Block Model Definition {#model-definition}

When using AEM Authoring with Edge Delivery Services, the content of blocks must be modelled explicitly in order to provide the author the interface to create content. Essentially you need to create a model so the authoring UI knows what options to present to the author based on the block. 

The [`component-models.json`](https://github.com/adobe-rnd/aem-boilerplate-xwalk/blob/main/component-models.json) file defines the model of blocks. The fields defined in the component model are persisted as properties in AEM and rendered as cells in the table that makes up a block.

```json
{
  "id": "hero",
  "fields": [
    {
      "component": "reference",
      "valueType": "string",
      "name": "image",
      "label": "Image",
      "multi": false
    },
    {
      "component": "text-input",
      "valueType": "string",
      "name": "imageAlt",
      "label": "Alt",
      "value": ""
    },
    {
      "component": "text-area",
      "name": "text",
      "value": "",
      "label": "Text",
      "valueType": "string"
    }
  ]
}
```

Note that not every block must have a model. Some blocks are simply containers for a list of children, where each child has its own model.

It is also necessary to define which blocks exist and can be added to a page using the Universal Editor. The [`component-definitions.json`](https://github.com/adobe-rnd/aem-boilerplate-xwalk/blob/main/component-definition.json) file lists the components as they are made available by the Universal Editor.

```json
{
  "title": "Hero",
  "id": "hero",
  "plugins": {
    "xwalk": {
      "page": {
        "resourceType": "core/franklin/components/block/v1/block",
        "template": {
          "name": "Hero",
          "model": "hero"
        }
      }
    }
  }
}
```

It is possible to use one model for many blocks. For example some blocks may share a model that defines a text and image.

For each block the developer:

* Must use the `core/franklin/components/block/v1/block` resource type, the generic implementation of the block logic in AEM.
* Must define the block name, which will be rendered in the block's table header.
* Can define a model ID. 
* Can define a filter ID.

All this information is stored in AEM when a block added to a page.

>[!WARNING]
>
>While possible, it is not necessary to implement custom AEM components. The components for Edge Delivery Services provided by AEM are sufficient and implement certain guard rails to ease development.
>
>For this reason, Adobe does not recommend using custom AEM resource types.

### Block Structure {#block-structure}

The properties of blocks are [defined in the component models](#model-definition) and persisted as such in AEM. Properties are rendered as cells in the block's table-like structure.

#### Simple Blocks {#simple}

In the simplest form, a block renders each property in a single row/column in the order the properties are defined in the model.

In the following example, the image is defined first in the model and the text second. They are thus rendered with the image first and text second.

##### Data {#data-simple}

```json
{
  "name": "Hero",
  "model": "hero",
  "image": "/content/dam/image.png",
  "imageAlt": "Helix - a shape like a corkscrew",
  "text": "<h1>Welcome to AEM</h1>"
}
```

##### Markup {#markup-simple}

```html
<div class="hero">
  <div>
    <div>
      <picture>
        <img src="/content/dam/image.png" alt="Helix - a shape like a corkscrew">
      </picture>
    </div>
  </div>
  <div>
    <div>
      <h1>Welcome to AEM</h1>
    </div>
  </div>
</div>
```

You may notice that some types of values allow inferring semantics in the markup, and properties are combined into in single cells. This will be explained in detail later.

#### Key-Value Block {#key-value}

In many cases, it it recommended to decorate the rendered semantic markup, add CSS class names, add new nodes or move them around in the DOM, and apply styles.

In other cases however, the block is read as a key-value pair-like configuration.

An example of this is the [section metadata.](/help/edge/developer/markup-sections-blocks.md#sections) In this use case, the block can be configured to render as key-value pair table instead. See more details about the sections and section metadata further in this document.

##### Data {#data-key-value}

```json
{
  "name": "Featured Articles",
  "model": "spreadsheet-input",
  "key-value": true,
  "source": "/content/site/articles.json",
  "keywords": ['Developer','Courses'],
  "limit": 4
}
```

##### Markup {#markup-key-value}

```html
<div class="featured-articles">
  <div>
    <div>source</div>
    <div><a href="/content/site/articles.json">/content/site/articles.json</a></div>
  </div>
  <div>
    <div>keywords</div>
    <div>Developer,Courses</div>
  <div>
  <div>
    <div>limit</div>
    <div>4</div>
  </div>
</div>
```

#### Container Blocks {#container}

Both of the previous structures have a single dimension: the list of properties. Container blocks allow adding children (usually of the same type or model) and hence are two-dimensional. These blocks still support their own properties rendered as rows with a single column first. But they also allow adding children, for which each item is rendered as row and each property as column within that row.

In the following example, a block accepts a list of linked icons as children, where each linked icon has an image and a link. Notice the filter ID set in the data of the block in order to reference the filter configuration.

##### Data {#data-container}

```json
{
  "name": "Our Partners",
  "model": "text-only",
  "filter:" "our-partners",
  "text": "<p>Our community of partners is ...</p>",
  "item_0": {
    "model": "linked-icon",
    "image": "/content/dam/partners/foo.png",
    "imageAlt": "Icon of Foo",
    "link": "https://foo.com/"
  },
  "item_1": {
    "model": "linked-icon"
    "image": "/content/dam/partners/bar.png",
    "imageAlt": "Icon of Bar",
    "link": "https://bar.com"
  }
}
```

##### Markup {#markup-container}

```html
<div class="our-partners">
  <div>
    <div>
        Our community of partners is ...
    </div>
  </div>
  <div>
    <div>
      <picture>
         <img src="/content/dam/partners/foo.png" alt="Icon of Foo">
      </picture>
    </div>
    <div>
      <a href="https://foo.com">https://foo.com</a>
    </div>
  </div>
  <div>
    <div>
      <picture>
         <img src="/content/dam/partners/bar.png" alt="Icon of Bar">
      </picture>
    </div>
    <div>
      <a href="https://bar.com">https://bar.com</a>
    </div>
  </div>
</div>
```

