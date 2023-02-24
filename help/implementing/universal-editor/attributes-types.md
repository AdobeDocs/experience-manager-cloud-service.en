---
title: Attributes and Types
description: Learn about the data attributes and types that the Universal Editor requires.
feature: Universal Editor
---

# Attributes and Types {#attributes-types}

Learn about the data attributes and types that the Universal Editor requires.

## Introduction {#introduction}

In order for an app to be editable by the Universal Editor, it must be properly instrumented. This includes including the proper metadata so the editor can edit the content of the app. This document details the attributes and types of those metadata.

>[!NOTE]
>
>Content validation is performed on the server side. The Universal Editor simply works with the data attributes. Validation that they fit the model/structure needs to be addressed at the API level.

## Data Properties {#data-properties}

|Data Property|Description|
|---|---|
|`itemid`|URN to the resource, see the section [Instrument the Page of the document Getting Started with the Universal Editor in AEM](getting-started.md#instrument-thepage)|
|`itemprop`|Attribute of the resource, see the section [Instrument the Page of the document Getting Started with the Universal Editor in AEM](getting-started)|
|`itemtype`|Type of the editable item (e.g.text, image, reference, etc.)|
|`data-editor-itemfilter`|Defines which references can be used|
|`data-editor-itemlabel`|Defines a custom label for a selectable item which is displayed in the editor <br>In case `itemmodel` is set, the label will be retrieved via the model|
|`data-editor-itemmodel`|Defines a model which will be used for form-based editing in the properties rail|
|`data-editor-behavior`|Defines the behavior of an instrumentation, e.g.  stand alone text or image can also mimic a component to make it moveable or deletable|

## Item Types {#item-types}

|`itemtype`|Description|`itemid`|`itemprop`|`data-editor-itemfilter`|`data-editor-itemlabel`|`data-editor-itemmodel`|`data-editor-behvior`|
|---|---|---|---|---|---|---|---|
|`text`|Text is editable within the HTML tags, but only in simple text format, no rich text formatting available, this is commonly used on title components, for example|Optional|Required|n/a|Optional|n/a|Optional|
|`richtext`|Text is editable with full rich text capabilities. RTE will be shown in the right panel|Optional|Required|n/a|Optional|n/a|Optional|
|`media`|The editable is an asset, e.g. image or video|Optional|Required|Optional<br>list of image or video filter criteria which is passed on to the asset selector|Optional|n/a|Optional|
|`container`|The editable behaves as container for components aka Paragraph System.|Depends <br>see below|Depends <br>see below|Optional<br>a list of allowed components|Optional|n/a|n/a|
|`component`|The editable is a component. Doesn't add additional functionality, will be required to indicate movable/deletable parts of the DOM and for opening the properties rail and its fields|Required|n/a|n/a|Optional|Optional|n/a|
|`reference`|The editable is a reference, e.g. Content Fragment, Experience Fragment or Product|Depends <br>see below|Depends <br>see below|Optional<br>list of Content Fragment, Product, or Experience Fragment filter criteria which is passed on to the reference selector|Optional|Optional|n/a|

Depending on the use case `itemprop` or `itemid` may or may not be required. For example:

* `itemid` is required if you query Content Fragments via GraphQL and you want to make the list editable in-context.
* `itemprop` is required in case you have a component rendering the content of a referenced Content Fragment and you want to update the reference within the component.

## Behaviors {#behaviors}

|`data-editor-behavior`|Description|
|---|---|
|`component`|Can be used to let standalone text, richtext, and media mimic  components so they are also moveable and deletable on the page|

