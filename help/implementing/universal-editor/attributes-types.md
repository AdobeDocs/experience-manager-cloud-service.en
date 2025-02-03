---
title: Attributes and Item Types
description: Learn about the data attributes and item types that the Universal Editor requires.
exl-id: 02795a31-244a-42b4-8297-2649125d7777
---

# Attributes and Types {#attributes-types}

Learn about the data attributes and item types that the Universal Editor requires.

## Introduction {#introduction}

In order for an app to be editable by the Universal Editor, it must be properly instrumented. This includes including the proper metadata so the editor can edit the content of the app. This document details the attributes and item types of those metadata.

>[!NOTE]
>
>Content validation is performed on the server side. The Universal Editor simply works with the data attributes. Validation that they fit the model/structure must be addressed at the API level.

## Data Properties {#data-properties}

|Data Property|Description|
|---|---|
|`data-aue-resource`|URN to the resource, see the section [Instrument the Page of the document Getting Started with the Universal Editor in AEM](getting-started.md#instrument-thepage)|
|`data-aue-prop`|Attribute of the resource, see the section [Instrument the Page of the document Getting Started with the Universal Editor in AEM](getting-started.md#instrument-thepage)|
|`data-aue-type`|[Type of the editable item](#item-types) (for example, text, image, and reference)|
|`data-aue-filter`|Defines which references can be used|
|`data-aue-label`|Defines a custom label for a selectable item which is displayed in the editor <br>In case `data-aue-model` is set, the label is retrieved by way of the model|
|`data-aue-model`|Defines a model which is used for form-based editing in the properties rail|
|`data-aue-behavior`|Defines the [behavior of an instrumentation](#behaviors), for example, stand alone text or image can also mimic a component to make it moveable or deletable|

## Item Types {#item-types}

|`data-aue-type`|Description|`data-aue-resource`|`data-aue-prop`|`data-aue-filter`|`data-aue-label`|`data-aue-model`|`data-aue-behavior`|
|---|---|---|---|---|---|---|---|
|`text`|Text is editable within the HTML tags, but only in simple text format, no rich text formatting available, this is commonly used on title components, for example|Optional|Required|n/a|Optional|n/a|Optional|
|`richtext`|Text is editable with full rich text capabilities. RTE is shown in the right panel|Optional|Required|n/a|Optional|n/a|Optional|
|`media`|The editable is an asset, for example, image or video|Optional|Required|Optional<br>list of image or video filter criteria which is passed on to the asset selector|Optional|n/a|Optional|
|`container`|The editable behaves as container for components aka Paragraph System.|Depends <br>see below|Depends <br>see below|Optional<br>a list of allowed components|Optional|n/a|n/a|
|`component`|The editable is a component. It doesn't add additional functionality. It is required to indicate movable/deletable parts of the DOM and for opening the properties rail and its fields|Required|n/a|n/a|Optional|Optional|n/a|
|`reference`|The editable is a reference, for example, Content Fragment, Experience Fragment or Product|Depends <br>see below|Depends <br>see below|Optional<br>list of Content Fragment, Product, or Experience Fragment filter criteria which is passed on to the reference selector|Optional|Optional|n/a|

Depending on the use case `data-aue-prop` or `data-aue-resource` may or may not be required. For example:

* `data-aue-resource` is required if you query Content Fragments via GraphQL and you want to make the list editable in-context.
* `data-aue-prop` is required in case you have a component rendering the content of a referenced Content Fragment and you want to update the reference within the component.

## Behaviors {#behaviors}

|`data-aue-behavior`|Description|
|---|---|
|`component`|Used to allow standalone text, richtext, and media mimic components so they are also moveable and deletable on the page|
|`container`|Used to allow containers to be treated as their own components so they are movable and deletable on the page|

## Additional Resources {#additional-resources}

To learn more about the Universal Editor, see these documents.

* [Universal Editor Introduction](introduction.md) - Learn how the Universal Editor enables editing any aspect of any content in any implementation so you can deliver exceptional experiences, increase content velocity, and provide a state-of-the-art developer experience.
* [Authoring Content with the Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md) - Learn how easy and intuitive it is for content authors to create content using the Universal Editor.
* [Publishing Content with the Universal Editor](/help/sites-cloud/authoring/universal-editor/publishing.md) - Learn how the Universal Editor publishes content and how your apps can handle the published content.
* [Getting Started with the Universal Editor in AEM](getting-started.md) - Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.
* [Universal Editor Architecture](architecture.md) - Learn about the architecture of the Universal Editor and how data flows between its services and layers.
* [Universal Editor Authentication](authentication.md) - Learn how the Universal Editor authenticates.
