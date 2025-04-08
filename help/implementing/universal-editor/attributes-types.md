---
title: Attributes and Item Types
description: Learn about the data attributes and item types that the Universal Editor requires.
exl-id: 02795a31-244a-42b4-8297-2649125d7777
feature: Developing
role: Admin, Architect, Developer
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
|`data-aue-filter`|Defines:<br>- Which RTE functionalities are enabled<br>- Which components can be added to a container<br>- Which assets can be added to a media type|
|`data-aue-label`|Defines a custom label for a selectable item which is displayed in the editor|
|`data-aue-model`|Defines a model which is used for form-based editing in the properties panel|
|`data-aue-behavior`|Obsolete. It once defined the behavior of an instrumentation to allow standalone text, richtext, and media to mimic components so they were also moveable and deletable on the page, offering a single potential value of `component`. This property is now ignored and when an item with `data-aue-resource` is a direct child of a container it is automatically considered a component.|

## Item Types {#item-types}

|`data-aue-type`|Description|`data-aue-resource`|`data-aue-prop`|`data-aue-filter`|`data-aue-label`|`data-aue-model`|
|---|---|---|---|---|---|---|
|`text`|Text is editable within the HTML tags, but only in simple text format, no rich text formatting available, this is commonly used on title components, for example|Optional|Required|n/a|Optional|n/a|
|`richtext`|Text is editable with full rich text capabilities. RTE is shown in the right panel|Optional|Required|n/a|Optional|n/a|
|`media`|The editable is an asset, for example, image or video|Optional|Required|Optional<br>list of image or video filter criteria which is passed on to the asset selector|Optional|n/a|
|`container`|The editable behaves as container for components aka Paragraph System.|Depends <br>see below|Depends <br>see below|Optional<br>a list of allowed components|Optional|n/a|
|`component`|The editable is a component. It doesn't add additional functionality. It is required to indicate movable/deletable parts of the DOM and for opening the properties panel and its fields|Required|n/a|n/a|Optional|Optional|
|`reference`|The editable is a reference, for example, Content Fragment, Experience Fragment or Product|Depends <br>see below|Depends <br>see below|Optional<br>list of Content Fragment, Product, or Experience Fragment filter criteria which is passed on to the reference selector|Optional|Optional|

`data-aue-resource` is always required since it is the primary key indicating where content changes are written.

* It is not required directly on the tag where the `data-aue-type` is set.
* In case it is not set, the `data-aue-resource` attribute of a the nearest parent will be used.

`data-aue-prop` is required whenever you want to do an edit in context the except for a container where it is optional (if set the container is a content fragment and the prop points to a multi-reference field).

* The `data-aue-prop` is the attribute to update for the primary key of `data-aue-resource`.
