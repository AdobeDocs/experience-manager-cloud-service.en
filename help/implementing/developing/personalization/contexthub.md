---
title: ContextHub
description: ContextHub is a framework for storing, manipulating, and presenting context data
exl-id: 604477c6-d96a-441f-b5fc-5def93832478
feature: Developing, Personalization
role: Admin, Architect, Developer
---
# ContextHub {#contexthub}

ContextHub is a framework for storing, manipulating, and presenting context data. Its primary feature is offering the ability to [view context data while simulating and switching between various personas](/help/sites-cloud/authoring/personalization/contexthub.md).

The ContextHub allowing you to:

* [Present, view, switch personas, and simulate user experience](#presentation) while authoring pages using context data.
* [Persist context data](#persistence) on your website as a data layer representation.
* [Manage segments](#segmentation) for the selected context.

The client-side JavaScript API enables you to access the data for personalizing content.

## Presentation {#presentation}

The [ContextHub toolbar](/help/sites-cloud/authoring/personalization/contexthub.md) enables marketers and authors to see and manipulate store data for simulating the user experience when authoring pages. The toolbar consists of groups of UI modules that provide access to [ContextHub stores](#persistence), which persist ContextHub data on the client.

Each ContextHub UI module is an instance of a predefined module type:

* ContextHub provides several [sample module types](sample-modules.md).
* Use AEM consoles to [add UI modules](configuring-contexthub.md#adding-a-ui-module), and to [group them in UI modes](configuring-contexthub.md#adding-a-ui-mode).
* Developers can [create custom module types](extending-contexthub.md#creating-contexthub-ui-module-types).

Developers need to [add the ContextHub component to the page](configuring-contexthub.md).

## Persistence {#persistence}

ContextHub stores persist context data on the client. The ContextHub JavaScript API enables you to access stores to create, update, and delete data as necessary. As such, ContextHub represents a data layer on your pages.

Each ContextHub store is an instance of a predefined store type:

* ContextHub provides several [sample store types](sample-stores.md).
* Use AEM consoles to [create stores](configuring-contexthub.md#creating-a-contexthub-store).
* Developers can [create custom store types](extending-contexthub.md#creating-custom-store-candidates).
* Developers can [access store data](adding-contexthub.md#interacting-with-contexthub-stores) by way of JavaScript.

## Segmentation {#segmentation}

ContextHub includes a segmentation engine that manages segments and determines which segments are resolved for the current context. Several segments are defined. You can use the JavaScript API to [determine resolved segments](adding-contexthub.md#determining-resolved-contexthub-segments).
