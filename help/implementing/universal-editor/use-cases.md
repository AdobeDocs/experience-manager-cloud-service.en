---
title: Universal Editor Use Cases and Learning Paths
description: Learn about the main use cases of the Universal Editor and how best to learn about its use and how to implement it on your own projects.
exl-id: 398ad0e2-c299-4c49-9784-05c84c67bec2
feature: Developing
role: Admin, Architect, Developer
---
# Universal Editor Use Cases and Learning Paths {#use-cases-learning-paths}

Learn about the main use cases of the Universal Editor and how best to learn more about its use and how to implement it on your own projects.

## Overview {#overview}

The Universal Editor is a versatile visual editor that is part of Adobe Experience Manager Sites. It enables authors to perform what-you-see-is-what-you-get (WYSIWYG) editing of any headless or headful experience.

This document explains these two use cases in detail and shows you how you can learn more about them so you can implement the Universal Editor in your own project.

>[!TIP]
>
>If you have not already, please review the document [Universal Editor Introduction](/help/implementing/universal-editor/introduction.md) for a complete overview and value of the Universal Editor.

## Use Cases {#use-cases}

The Universal Editor presents a convenient, intuitive visual editor to your content authors no matter what kind of content they are creating. The two main use cases are:

* [WYSIWYG Authoring](#wysiwyg-authoring) - Use the AEM Sites console to manage your content and author pages within AEM using the Universal Editor
* [Headless Authoring](#headless-authoring) - Author content in your own custom headless application using the Universal Editor.

### WYSIWYG Authoring {#wysiwyg-authoring}

If you are already familiar with AEM, you can use the Sites console to create and manage your pages and then edit them with the Universal Editor.

In this way you can benefit from the tools available in the Sites console such as page management (copy, paste, move) and workflows, but also benefit from the modern Universal Editor.

If this is your use case, as an immediate next step, please see the following documents for a complete overview of how to get up-and-running with the Universal Editor in AEM.

1. [Developer Getting Started Guide for WYSIWYG authoring with Edge Delivery Services](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md) - Get started with your first Universal Editor project in AEM
1. [Creating Blocks Instrumented for use with the Universal Editor](/help/edge/wysiwyg-authoring/create-block.md) - Learn how to instrument blocks to make your content editable in the Universal Editor
1. [Content Modeling for WYSIWYG authoring with Edge Delivery Services Projects](/help/edge/wysiwyg-authoring/content-modeling.md) - Learn the details of how blocks are structured to effectively model your content for use with the Universal Editor.

Once you have read those documents, you can return to this page to learn about the headless authoring use case and how the Universal Editor works in general.

### Headless Authoring {#headless-authoring}

If you already have a headless app, you can use the Universal Editor to author content for the app and persist its content as Content Fragments in AEM. The only requirement is that the app is instrumented to allow the use of the Universal Editor.

If this is your use case, as an immediate next step, please see the following document for an example of a headless app instrumented to use the Universal Editor.

* [SecurBank Sample App for the Universal Editor](/help/implementing/universal-editor/securbank.md)

Once you have read that document, you can return to this page to learn about the WYSIWYG authoring use case and how the Universal Editor works in general.

## How the Universal Editor Works {#how-ue-works}

The power of the Universal Editor is its ability to author any content in-place, providing the content author an entirely intuitive and unified UI no matter what the content.

The Universal Editor works in the following way.

1. A developer instruments the app or page to use the Universal Editor. This instrumentation tells the editor what content is editable and how to persist it.
   * If you follow the [Developer Getting Started Guide for WYSIWYG Authoring with Edge Delivery Services](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md) documentation, your pages are automatically instrumented.
   * For headless authoring, your app can be easily instrumented.
1. The content author load the Universal Editor, which in turn loads your page for editing. Because it is instrumented, it knows which content is editable and how it is to be represented and persisted.
1. The content author edits the page content in an intuitive WYSIWYG interface, editing in-place.
1. The Universal Editor persists the changes automatically back to the data source.

If you would like to learn more about the architecture of the Universal Editor, please see the document [Universal Editor Architecture](/help/implementing/universal-editor/architecture.md).

## Universal Editor Concepts {#concepts}

For a page or app to be editable by the Universal Editor, it must be properly instrumented.

* [Attributes and Types](/help/implementing/universal-editor/attributes-types.md) - In order for an app or page to be editable by the Universal Editor, it must be properly instrumented. This includes including the proper metadata so the editor can edit the content of the app. 
* [Model Definitions, Fields, and Component Types](/help/implementing/universal-editor/field-types.md) - Once the metadata is present to enable editing of a component, you define what fields and component types they can manipulate in the properties panel of the editor.
* [Universal Editor Events](/help/implementing/universal-editor/events.md) - You can further customize your app by enhancing the editing experience in your app by consuming events the Universal Editor emits on content or UI interactions.

The Universal editor can also be adapted to your project needs.

* [Customizing the Universal Editor Authoring Experience](/help/implementing/universal-editor/customizing.md) - The Universal Editor experience can be adapted by filtering various aspects of the editor or by extending the functionality of the editor.
