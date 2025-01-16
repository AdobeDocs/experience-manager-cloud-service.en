---
title: Content Modeling for WYSIWYG Authoring with Edge Delivery Services Projects
description: Learn how content modeling works for WYSIWYG Authoring with Edge Delivery Services projects and how to model your own content.
exl-id: e68b09c5-4778-4932-8c40-84693db892fd
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Content Modeling for WYSIWYG Authoring with Edge Delivery Services Projects {#content-modeling}

Learn how content modeling works for WYSIWYG Authoring with Edge Delivery Services projects and how to model your own content.

## Prerequisites {#prerequisites}

Projects using WYSIWYG Authoring with Edge Delivery Services inherit the majority of the mechanics of any other Edge Delivery Services project, independent of the content source or [authoring method.](/help/edge/wysiwyg-authoring/authoring.md)

Before you begin modeling content for your project, make sure you first read the following documentation.

* [Getting Started - Developer Tutorial](/help/edge/developer/tutorial.md)
* [Markup, Sections, Blocks, and Auto Blocking](/help/edge/developer/markup-sections-blocks.md)
* [Block Collection](/help/edge/developer/block-collection.md)

It is essential to understand those concepts in order to come up with a compelling content model that works in a content source-agnostic way. This document provides details about the mechanics implemented specifically for WYSIWYG authoring.

## Default Content {#default-content}

**Default content** is content an author intuitively would put on a page without adding any additional semantics. This includes text, headings, links, and images. Such content is self-explanatory in its function and purpose.

In AEM, this content is implemented as components with very simple, pre-defined models, which include everything that can serialized in Markdown and HTML. 

* **Text**: Rich text (including list elements and strong or italic text)
* **Title**: Text, type (h1-h6)
* **Image**: Source, description
* **Button**: Text, title, url, type (default, primary, secondary)

The model of these components is part of the [Boilerplate for WYSIWYG authoring with Edge Delivery Services.](https://github.com/adobe-rnd/aem-boilerplate-xwalk/blob/main/component-models.json#L2-L112)

## Blocks {#blocks}

Blocks are used to create richer content with specific styles and functionality. In contrast to default content, blocks do require additional semantics. 

Blocks are essentially pieces of content decorated by JavaScript and styled with a stylesheet.

### Block Model Definition {#model-definition}

When using WYSIWYG authoring with Edge Delivery Services, the content of blocks must be modelled explicitly in order to provide the author the interface to create content. Essentially you need to create a model so the authoring UI knows what options to present to the author based on the block. 

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

Note that not every block must have a model. Some blocks are simply [containers](#container) for a list of children, where each child has its own model.

It is also necessary to define which blocks exist and can be added to a page using the Universal Editor. The [`component-definitions.json`](/help/implementing/universal-editor/component-definition.md) file lists the components as they are made available by the Universal Editor.

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

It is possible to use one model for many blocks. For example, some blocks may share a model that defines a text and image.

For each block, the developer:

* Must use the `core/franklin/components/block/v1/block` resource type, the generic implementation of the block logic in AEM.
* Must define the block name, which will be rendered in the block's table header.
  * The block name is used to fetch the right style and script to decorate the block.
* Can define a [model ID.](/help/implementing/universal-editor/field-types.md#model-structure)
  * The model ID is a reference to the component's model, which defines the fields available to the author in the properties panel.
* Can define a [filter ID.](/help/implementing/universal-editor/customizing.md#filtering-components)
  * The filter ID is a reference to the component's filter, which allows to change the authoring behavior, for example by limiting which children can be added to the block or section, or which RTE features are enabled.

All this information is stored in AEM when a block is added to a page. If either the resource type or block name are missing, the block will not render on the page.

>[!WARNING]
>
>While possible, it is not necessary or recommended to implement custom AEM components. The components for Edge Delivery Services provided by AEM are sufficient and offer certain guard rails to ease development.
>
>The components provided by AEM render a markup that can be consumed by [helix-html2md](https://github.com/adobe/helix-html2md) when publishing to Edge Delivery Services and by [aem.js](https://github.com/adobe/aem-boilerplate/blob/main/scripts/aem.js) when loading a page in the Universal Editor. The markup is the stable contract between AEM and the other parts of the system, and does not allow for customizations. For this reason, projects must not change the components and must not use custom components.

### Block Structure {#block-structure}

The properties of blocks are [defined in the component models](#model-definition) and persisted as such in AEM. Properties are rendered as cells in the block's table-like structure.

#### Simple Blocks {#simple}

In the simplest form, a block renders each property in a single row/column in the order the properties are defined in the model.

In the following example, the image is defined first in the model and the text second. They are thus rendered with the image first and text second.

>[!BEGINTABS]

>[!TAB Data]

```json
{
  "name": "Hero",
  "model": "hero",
  "image": "/content/dam/image.png",
  "imageAlt": "Helix - a shape like a corkscrew",
  "text": "<h1>Welcome to AEM</h1>"
}
```

>[!TAB Markup]

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

>[!TAB Table]

```text
+---------------------------------------------+
| Hero                                        |
+=============================================+
| ![Helix - a shape like a corkscrew][image0] |
+---------------------------------------------+
| # Welcome to AEM                            |
+---------------------------------------------+
```

>[!ENDTABS]

You may notice that some types of values allow inferring semantics in the markup, and properties are combined into in single cells. This behavior is described in the section [Type Inference.](#type-inference)

#### Key-Value Block {#key-value}

In many cases, it it recommended to decorate the rendered semantic markup, add CSS class names, add new nodes or move them around in the DOM, and apply styles.

In other cases however, the block is read as a key-value pair-like configuration.

An example of this is the [section metadata.](/help/edge/developer/markup-sections-blocks.md#sections) In this use case, the block can be configured to render as key-value pair table. Please see the section [Sections and Section Metadata](#sections-metadata) for more information.

>[!BEGINTABS]

>[!TAB Data]

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

>[!TAB Markup]

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

>[!TAB Table]

```text
+-----------------------------------------------------------------------+
| Featured Articles                                                     |
+=======================================================================+
| source   | [/content/site/articles.json](/content/site/articles.json) |
+-----------------------------------------------------------------------+
| keywords | Developer,Courses                                          |
+-----------------------------------------------------------------------+
| limit    | 4                                                          |
+-----------------------------------------------------------------------+
```

>[!ENDTABS]

#### Container Blocks {#container}

Both of the previous structures have a single dimension: the list of properties. Container blocks allow adding children (usually of the same type or model) and hence are two-dimensional. These blocks still support their own properties rendered as rows with a single column first. But they also allow adding children, for which each item is rendered as row and each property as column within that row.

In the following example, a block accepts a list of linked icons as children, where each linked icon has an image and a link. Notice the [filter ID](/help/implementing/universal-editor/customizing.md#filtering-components) set in the data of the block in order to reference the filter configuration.

>[!BEGINTABS]

>[!TAB Data]

```json
{
  "name": "Our Partners",
  "model": "text-only",
  "filter": "our-partners",
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

>[!TAB Markup]

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

>[!TAB Table]

```text
+------------------------------------------------------------ +
| Our Partners                                                |
+=============================================================+
| Our community of partners is ...                            |
+-------------------------------------------------------------+
| ![Icon of Foo][image0] | [https://foo.com](https://foo.com) |
+-------------------------------------------------------------+
| ![Icon of Bar][image1] | [https://bar.com](https://bar.com) |
+-------------------------------------------------------------+
```

>[!ENDTABS]

### Creating Semantic Content Models for Blocks {#creating-content-models}

With the [mechanics of block structure explained,](#block-structure) it is possible to create a content model that maps content persisted in AEM one-to-one to the delivery tier. 

Early in every project, a content model must be carefully considered for every block. It must be agnostic to the content source and authoring experience in order to allow authors to switch or combine them while reusing block implementations and styles. More details and general guidance can be found in [David's Model (take 2).](https://www.aem.live/docs/davidsmodel) More specifically, the [block collection](/help/edge/developer/block-collection.md) contains a extensive set of content models for specific use cases of common user interface patterns.

For WYSIWYG authoring with Edge Delivery Services, this raises the question how to serve a compelling semantic content model when the information is authored with forms composed of multiple fields instead of editing semantic markup in-context like rich text.

To solve this problem, there are three methods that facilitate creating a compelling content model:

* [Type Inference](#type-inference)
* [Field Collapse](#field-collapse)
* [Element Grouping](#element-grouping)

>[!NOTE]
>
>Block implementations can deconstruct the content and replace the block with a client-side-rendered DOM. While this is possible and intuitive for a developer, it is not the best practice for Edge Delivery Services.

#### Type Inference {#type-inference}

For some values we can infer the semantic meaning from the values itself. Such values include:

* **Images** - If a reference to a resource in AEM is an asset with a MIME type starting with `image/`,  the reference is rendered as `<picture><img src="${reference}"></picture>`.
* **Links** - If a reference exists in AEM and is not an image, or if the value starts with `https?://`  or `#`,  the reference is rendered as `<a href="${reference}">${reference}</a>` .
* **Rich Text** - If a trimmed value starts with a paragraph (`p`, `ul`, `ol`, `h1`-`h6`, etc.), the value is rendered as rich text.
* **Class Names** - The `classes` property is treated as [block options](/help/edge/developer/markup-sections-blocks.md#block-options) and rendered in the table header for [simple blocks,](#simple) or as value list for items in a [container block.](#container) It is useful if you wish to [style a block differently,](/help/edge/wysiwyg-authoring/create-block.md#block-options) but don't need to create an entirely new block.
* **Value Lists** - If a value is a multi-value property and the first value is none of the previous, all values are concatenated as comma-separated list.

Everything else will be rendered as plain text.

#### Field Collapse {#field-collapse}

Field collapse is the mechanism to combine multiple field values into a single semantic element based on a naming convention using the suffixes `Title`, `Type`, `MimeType`, `Alt`, and `Text` (all case sensitive). Any property ending with any of those suffixes will not be considered a value, but rather as an attribute of another property.

##### Images {#image-collapse}

>[!BEGINTABS]

>[!TAB Data]

```json
{
  "image": "/content/dam/red-car.png",
  "imageAlt: "A red card on a road"
}
```

>[!TAB Markup]

```html
<picture>
  <img src="/content/dam/red-car.png" alt="A red car on a road">
</picture>
```

>[!TAB Table]

```text
![A red car on a road][image0]
```

>[!ENDTABS]

##### Links &amp; Buttons {#links-buttons-collapse}

>[!BEGINTABS]

>[!TAB Data]

```json
{
  "link": "https://www.adobe.com",
  "linkTitle": "Navigate to adobe.com",
  "linkText": "adobe.com",
  "linkType": "primary"
}
```

>[!TAB Markup]

No `linkType`, or `linkType=default`

```html
<a href="https://www.adobe.com" title="Navigate to adobe.com">adobe.com</a>
```

`linkType=primary`

```html
<strong>
  <a href="https://www.adobe.com" title="Navigate to adobe.com">adobe.com</a>
</strong>
```

`linkType=secondary`

```html
<em>
  <a href="https://www.adobe.com" title="Navigate to adobe.com">adobe.com</a>
</em>
```

>[!TAB Table]

```text
[adobe.com](https://www.adobe.com "Navigate to adobe.com")
**[adobe.com](https://www.adobe.com "Navigate to adobe.com")**
_[adobe.com](https://www.adobe.com "Navigate to adobe.com")_
```

>[!ENDTABS]

##### Headings {#headings-collapse}

>[!BEGINTABS]

>[!TAB Data]

```json
{
  "heading": "Getting started",
  "headingType": "h2"
}
```

>[!TAB Markup]

```html
<h2>Getting started</h2>
```

>[!TAB Table]

```text
## Getting started
```

>[!ENDTABS]

#### Element Grouping {#element-grouping}

While [field collapse](#field-collapse) is about combining multiple properties into a single semantic element, element grouping is about concatenating multiple semantic elements into a single cell. This is particularly helpful for use cases where the author should be restricted in the type and number of elements that they can create.

For example, a teaser component may allow the author to only create a subtitle, title, and a single paragraph description combined with a maximum of two call-to-action buttons. Grouping these elements together yields a semantic markup that can be styled without further action.

Element grouping uses a naming convention, where the group name is separated from each property in the group by an underscore. Field collapse of the properties in a group works as previously described.

>[!BEGINTABS]

>[!TAB Data]

```json
{
  "name": "teaser",
  "model": "teaser",
  "image": "/content/dam/teaser-background.png",
  "imageAlt": "A group of people sitting on a stage",
  "teaserText_subtitle": "Adobe Experience Cloud"
  "teaserText_title": "Meet the Experts"
  "teaserText_titleType": "h2"
  "teaserText_description": "<p>Join us in this ask me everything session...</p>"
  "teaserText_cta1": "https://link.to/more-details",
  "teaserText_cta1Text": "More Details"
  "teaserText_cta2": "https://link.to/sign-up",
  "teaserText_cta2Text": "RSVP",
  "teaserText_cta2Type": "primary"
}
```

>[!TAB Markup]

```html
<div class="teaser">
  <div>
    <div>
      <picture>
        <img src="/content/dam/teaser-background.png" alt="A group of people sitting on a stage">
      </picture>
    </div>
  </div>
  <div>
    <div>
      <p>Adobe Experience Cloud</p>
      <h2>Meet the Experts</h2>
      <p>Join us in this ask me everything session ...</p>
      <p><a href="https://link.to/more-details">More Details</a></p>
      <p><strong><a href="https://link.to/sign-up">RSVP</a></strong></p>
    </div>
  </div>
</div>
```

>[!TAB Table]

```text
+-------------------------------------------------+
| Teaser                                          |
+=================================================+
| ![A group of people sitting on a stage][image0] |
+-------------------------------------------------+
| Adobe Experience Cloud                          |
| ## Meet the Experts                             |
| Join us in this ask me everything session ...   |
| [More Details](https://link.to/more-details)    |
| [RSVP](https://link.to/sign-up)                 |
+-------------------------------------------------+
```

>[!ENDTABS]

## Sections and Section Metadata {#sections-metadata}

The same way a developer can define and model multiple [blocks,](#blocks) they can define different sections.

The content model of Edge Delivery Services deliberately allows only a single level of nesting, which is any default content or block contained by a section. This means in order to have more complex visual components that can contain other components, they have to be modelled as sections and combined together using auto-blocking client side. Typical examples of this are tabs and collapsible sections like accordions.

A section can be defined in the same way as a block, but with the resource type of `core/franklin/components/section/v1/section`. Sections can have a name and a [filter ID,](/help/implementing/universal-editor/customizing.md#filtering-components) which are used by the [Universal Editor](/help/implementing/universal-editor/introduction.md) only, as well as a [model ID,](/help/implementing/universal-editor/field-types.md#model-structure) which is used to render the section metadata. The model is in this way the model of the section metadata block, which will automatically be appended to a section as key-value block if it is not empty.

The [model ID](/help/implementing/universal-editor/field-types.md#model-structure) and [filter ID](/help/implementing/universal-editor/customizing.md#filtering-components) of the default section is `section`. It can be used to alter the behavior of the default section. The following example adds some styles and and a background image to the section metadata model.

```json
{
  "id": "section",
  "fields": [
    {
      "component": "multiselect",
      "name": "style",
      "value": "",
      "label": "Style",
      "valueType": "string",
      "options": [
        {
          "name": "Fade in Background",
          "value": "fade-in"
        },
        {
          "name": "Highlight",
          "value": "highlight"
        }
      ]
    },
    {
      "component": "reference",
      "valueType": "string",
      "name": "background",
      "label": "Image",
      "multi": false
    }
  ]
}
```

The following example defines a tab section, which can be used to create a tabs block by combining consecutive sections with a tab title data attribute into a tabs block during auto-blocking.

```json
{
  "title": "Tab",
  "id": "tab",
  "plugins": {
    "xwalk": {
      "page": {
        "resourceType": "core/franklin/components/section/v1/section",
        "template": {
          "name": "Tab",
          "model": "tab",
          "filter": "section"
        }
      }
    }
  }
}
```

## Page Metadata {#page-metadata}

Documents can have a page [metadata block,](https://www.aem.live/developer/block-collection/metadata) which is used to define which `<meta>` elements are rendered in the `<head>` of a page. The page properties of pages in AEM as a Cloud Service map to those that are available out-of-the-box for Edge Delivery Services, like `title`, `description`, `keywords`, etc.

Before further exploring how to define your own metadata, please review the following documents to understand the concept of page metadata first.

* [Metadata](https://www.aem.live/developer/block-collection/metadata)
* [Bulk Metadata](/help/edge/docs/bulk-metadata.md)

It is also possible to define additional page metadata in two ways.

### Metadata Spreadsheets {#metadata-spreadsheets}

It is possible to define metadata on a per path or per path pattern basis in a table-like way in AEM as a Cloud Service. There is an authoring UI for table-like data available that is similar to Excel or Google Sheets.

For further details, please see the document [Using Spreadsheets to Manage Tabular Data](/help/edge/wysiwyg-authoring/tabular-data.md) for more information.

### Page Properties {#page-properties}

Many of the default page properties available in AEM are mapped to the respective page metadata in a document. That includes for example `title`, `description`, `robots`, `canonical url` or `keywords`. Some AEM-specific properties are available as well:

* `cq:lastModified` as `modified-time` in ISO8601 format
* The time the document was last published as `published-time` in ISO8601 format
* `cq:tags` as `cq-tags` as a comma-separated list of the tag IDs. 

It is also possible to define a component model for custom page metadata, which will be made available to the author in the Universal Editor.

To do so, create a component model with the ID `page-metadata`.

```json
{
  "id": "page-metadata",
  "fields": [
    {
      "component": "text",
      "name": "theme",
      "label": "Theme"
    }
  ]
}
```

## Next Steps {#next-steps}

Now that you know how to model content, you can create blocks for your own Edge Delivery Services with WYSIWYG authoring project.

See the document [Creating Blocks Instrumented for use with the Universal Editor](/help/edge/wysiwyg-authoring/create-block.md) to learn how to create blocks instrumented for use with the Universal Editor in WYSIWYG authoring with Edge Delivery Services projects.

If you are already familiar with creating blocks, please see the document [Developer Getting Started Guide for WYSIWYG authoring with Edge Delivery Services](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md) to get you up-and-running with a new Adobe Experience Manager site using Edge Delivery Services and the Universal Editor for content authoring.

>[!TIP]
>
>For an end-to-end walkthrough of creating a new Edge Delivery Services project that is enabled for WYSIWYG authoring with AEM as a Cloud Service as a content source, please view [this AEM GEMs webinar.](https://experienceleague.adobe.com/en/docs/events/experience-manager-gems-recordings/gems2024/wysiwyg-authoring-and-edge-delivery)

