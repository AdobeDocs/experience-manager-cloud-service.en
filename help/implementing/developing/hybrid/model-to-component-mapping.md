---
title: Dynamic Model to Component Mapping for SPAs
description: This article describes how the dynamic model to component mapping occurs in the JavaScript SPA SDK for AEM.
exl-id: 3a7b3f26-4a09-40c1-af03-bb8408a68e57
feature: Developing
role: Admin, Architect, Developer
---
# Dynamic Model to Component Mapping for SPAs {#dynamic-model-to-component-mapping-for-spas}

This document describes how the dynamic model to component mapping occurs in the JavaScript SPA SDK for AEM.

{{ue-over-spa}}

## ComponentMapping Module {#componentmapping-module}

The `ComponentMapping` module is provided as an NPM package to the front-end project. It stores front-end components and provides a way for the Single Page Application to map front-end components to AEM resource types. The module enables a dynamic resolution of components when parsing the JSON model of the application.

Each item present in the model contains a `:type` field that exposes an AEM resource type. When mounted, the front-end component can render itself using the fragment of model it has received from the underlying libraries.

See [SPA Blueprint](blueprint.md) document for more information about model parsing and the front-end component access to the model.

Also see the npm package: [@adobe/aem-spa-component-mapping](https://www.npmjs.com/package/@adobe/aem-spa-component-mapping)

## Model-Driven Single Page Application {#model-driven-single-page-application}

Single Page Applications using the JavaScript SPA SDK for AEM are model-driven:

1. Front-end components register themselves to the [Component Mapping Store](#componentmapping-module).
1. Then the [Container](blueprint.md#container), once provided with a model by the [Model Provider](blueprint.md#the-model-provider), iterates over its model content (`:items`).

1. If there is a page, its children (`:children`) first get a component class from the [Component Mapping](blueprint.md#componentmapping) and then instantiate it.

## App Initialization {#app-initialization}

Each component is extended with the capabilities of the [`ModelProvider`](blueprint.md#the-model-provider). Initialization therefore takes the following general form:

1. Each model provider initializes itself and listens for changes made to the piece of model that corresponds to its inner component.
1. The [`PageModelManager`](blueprint.md#pagemodelmanager) must be initialized as represented by the [initialization flow](blueprint.md).

1. Once stored, the page model manager returns the complete model of the app.
1. This model is then passed to the front-end root [Container](blueprint.md#container) component of the application.
1. Pieces of the model are finally propagated to each individual child component.

![App model initialization](assets/app-model-initialization.png)
