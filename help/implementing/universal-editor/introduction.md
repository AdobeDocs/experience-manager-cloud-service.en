---
title: Universal Editor Introduction
description: Learn how the Universal Editor enables what-you-see-is-what-you-get (WYSIWYG) editing of any headless and headful experience. Understand how it can help content authors deliver exceptional experiences, increase their content velocity, and how provides a state-of-the-art developer experience.
exl-id: d4fc2384-a0f5-4a6f-9572-62749786be4c
---

# Universal Editor Introduction {#introduction}

Learn how the Universal Editor enables what-you-see-is-what-you-get (WYSIWYG) editing of any headless and headful experience. Understand how it can help content authors deliver exceptional experiences, increase their content velocity, and how provides a state-of-the-art developer experience.

## Background {#background}

The most powerful tool to the AEM content author has been the page editor. The page editor offers an intuitive, visual, in-context WYSIWYG authoring experience that requires minimal training and shows authors exactly how the content will appear.

However the page editor can only edit AEM page content, structure, and the components contained therein. Content today, however, is rarely sourced from one location. The Universal Editor offers the same in-place editing experience as the page editor but for any aspect of any content in any implementation.

## Truly Universal {#universal}

The Universal Editor can be instrumented for any implementation, for any content, and for any aspect of the content.

![What makes it universal](assets/universal.png)

### Any Implementation {#any-implementation}

Because experiences can be built in many different ways, any implementation can use the Universal Editor so authors can perform in-context editing.

Users often think that a headless implementation limits the authors to editing all content in a form-based UI, but this isn't the case with the Universal Editor

The requirements for an implementation to use the Universal Editor is straight-forward and supports the following:

* **Any Architecture** - Server-side rendering, edge-side rendering, client-side rendering, and so on.
* **Any Framework** - Vanilla AEM, or any third-party framework like React, Next.js, Angular, and so on.
* **Any Hosting** - Can be hosted locally to AEM, or on a remote domain

### Any Content {#any-content}

A content author should have the same powerful editing experience formerly offered by the AEM page editor. But the Universal Editor allows content authors to edit **any** content visually and in-context and supports:

* **AEM Page Structures** - Nested `cq:Components` of `cq:Pages`, including Experience Fragments
* **AEM Content Fragments** - Edit content from Content Fragments as they appear in-context of the experience.
* **Documents** - Proof of concepts have shown that also Word, Excel, Google Docs or Markdown documents can also be edited the same way (this is WIP).

### Any Aspect {#any-aspect}

For a content author, content is not just about the information contained, but how it is rendered and received. Content comes with additional meta-data and instrumentation rules, which the Universal Editor can understand and edit including:

* **Applying Layout &amp; Style** - By using a style system, the marketing practitioner and content author can apply different styles to their content and create different layouts for the content such as columns, carousels, tabs, accordions, and so on.

## Value {#value}

By decoupling the content editing experience from any particular content delivery system, the editor becomes truly universal and flexible allowing the content author to delivery exceptional experiences, increase content velocity, and provides a state-of-the-art developer experience.

![The value of the Universal Editor](assets/value.png)

* **Deliver Exceptional Experiences** - To enable practitioners to create a compelling experience for visitors, the Universal Editor allows practitioners to create and edit the content in the context of the preview. This allows them to create content that fits the design of the experience and that constitutes a meaningful journey for visitors.
* **Increase Content Velocity** - To streamline the management workflow of practitioners, the Universal Editor allows editing content within the preview to guide practitioners by showing only the options that are relevant to that context and makes the workflow independent from the content sources.
* **State-of-the-art Developer Experience** - To support real-world heterogeneous application landscape, the Universal Editor is completely fully decoupled and technology-agnostic, allowing developers to use their preferred technology stack to implement the experience.

## Universal Editor and the Content Fragment Editor {#universal-editor-content-fragment-editor}

At first glance, it might seem like the Universal Editor and the Content Fragment Editor provide similar editing capabilities. However, these editors offer very different capabilities and they accomplish different jobs of the marketing practitioner.

### Content Fragment Editor {#content-fragment-editor} 

A marketing practitioner wants to create content without having to care about its layout, so that it can be reused in numerous contexts of the experience.

* The underlying job to accomplish is to scale the content strategy.

### Universal Editor {#universal-editor}

A marketing practitioner wants to create content that is tailored to the layout of a given context to deliver an exceptional experience.

* The underlying job to accomplish is to convincingly connect with the readers.

## Road Map {#road-map}

It is important to note that the Universal Editor is a work in progress and some of the capabilities laid out in this document are a vision of the final editor and not necessarily representative of its current capabilities.

Speak with your Adobe contact for details on the upcoming features planned for the Universal Editor.

## Additional Resources {#additional-resources}

To learn more about the Universal Editor, see these documents.

* [Authoring Content with the Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md) - Learn how easy and intuitive it is for content authors to create content using the Universal Editor.
* [Publishing Content with the Universal Editor](/help/sites-cloud/authoring/universal-editor/publishing.md) - Learn how the Universal Editor publishes content and how your apps can handle the published content.
* [Getting Started with the Universal Editor in AEM](getting-started.md) - Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.
* [Universal Editor Architecture](architecture.md) - Learn about the architecture of the Universal Editor and how data flows between its services and layers.
* [Attributes and Types](attributes-types.md) - Learn about the data attributes and types that the Universal Editor requires.
* [Universal Editor Authentication](authentication.md) - Learn how the Universal Editor authenticates.
