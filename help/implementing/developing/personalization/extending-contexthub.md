---
title: Extending ContextHub
description: Define new types of ContextHub stores and modules when the ones provided do not meet your solution requirements
exl-id: ba817c18-f8bd-485d-b043-87593a6a93b5
feature: Developing, Personalization
role: Admin, Architect, Developer
---
# Extending ContextHub {#extending-contexthub}

Define new types of ContextHub stores and modules when the ones provided do not meet your solution requirements.

## Creating Custom Store Candidates {#creating-custom-store-candidates}

ContextHub stores are created from registered store candidates. To create a custom store, you need to create and register a store candidate.

The javascript file that includes the code that creates and registers the store candidate must be included in a [client library folder](/help/implementing/developing/introduction/clientlibs.md). The category of the folder must match the following pattern:

```xml
contexthub.store.[storeType]
```

The `storeType` part of the category is the `storeType` with which the store candidate is registered. (See [Registering a ContextHub Store Candidate](#registering-a-contexthub-store-candidate)). For example, for the storeType of `contexthub.mystore`, the category of the client library folder must be `contexthub.store.contexthub.mystore`.

### Creating a ContextHub Store Candidate {#creating-a-contexthub-store-candidate}

To create a store candidate, you use the [`ContextHub.Utils.inheritance.inherit`](contexthub-api.md#inherit-child-parent) function to extend one of the base stores:

* [`ContextHub.Store.PersistedStore`](contexthub-api.md#contexthub-store-persistedstore)
* [`ContextHub.Store.SessionStore`](contexthub-api.md#contexthub-store-sessionstore)
* [`ContextHub.Store.JSONPStore`](contexthub-api.md#contexthub-store-jsonpstore)
* [`ContextHub.Store.PersistedJSONPStore`](contexthub-api.md#contexthub-store-persistedjsonpstore)

Each base store extends the [`ContextHub.Store.Core`](contexthub-api.md#contexthub-store-core) store.

The following example creates the simplest extension of the `ContextHub.Store.PersistedStore` store candidate:

```javascript
myStoreCandidate = function(){};
ContextHub.Utils.inheritance.inherit(myStoreCandidate,ContextHub.Store.PersistedStore);
```

Realistically, your custom store candidates will define additional functions or override the store's initial configuration. Several [sample store candidates](sample-stores.md) are installed in the repository below `/libs/granite/contexthub/components/stores`.

### Registering a ContextHub Store Candidate {#registering-a-contexthub-store-candidate}

Register a store candidate to integrate it with the ContextHub framework and enable stores to be created from it. To register a store candidate, use the [`registerStoreCandidate`](contexthub-api.md#registerstorecandidate-store-storetype-priority-applies) function of the `ContextHub.Utils.storeCandidates` class.

When you register a store candidate, you provide a name for the store type. When creating a store from the candidate, you use the store type to identify the candidate upon which it is based.

When you register a store candidate, you indicate its priority. When a store candidate is registered using the same store type as an already-registered store candidate, the candidate with the higher priority is used. Therefore, you can override existing store candidates with new implementations.

```javascript
ContextHub.Utils.storeCandidates.registerStoreCandidate(myStoreCandidate,
                                'contexthub.mystorecandidate', 0);
```

In most cases only one candidate is necessary and the priority can be set to `0`, but if you are interested you can learn about [more advanced registrations](contexthub-api.md#registerstorecandidate-store-storetype-priority-applies), which allows one of few store implementations to be chosen based on javascript condition (`applies`) and candidate priority.

## Creating ContextHub UI Module Types {#creating-contexthub-ui-module-types}

Create custom UI module types when the ones that are [installed with ContextHub](sample-modules.md) do not meet your requirements. To create a UI module type, create a UI module renderer by extending the `ContextHub.UI.BaseModuleRenderer` class and then registering it with `ContextHub.UI`.

To create a UI module renderer, create a `Class` object that contains the logic that renders the UI module. At a minimum, your class must perform the following actions:

* Extend the `ContextHub.UI.BaseModuleRenderer` class. This class is the base implementation for all UI module renderers. The `Class` object defines a property named `extend` that you use to name this class as that which is being extended.
* Provide a default configuration. Create a `defaultConfig` property. This property is an object that includes the properties that are defined for the [`contexthub.base`](sample-modules.md#contexthub-base-ui-module-type) UI module, and any other properties that you require.

The source for `ContextHub.UI.BaseModuleRenderer` is located at `/libs/granite/contexthub/code/ui/container/js/ContextHub.UI.BaseModuleRenderer.js`.  To register the renderer, use the [`registerRenderer`](contexthub-api.md#registerrenderer-moduletype-renderer-dontrender) method of the `ContextHub.UI` class. You need to provide a name for the module type. When administrators create a UI module based on this renderer, they specify this name.

Create and register the renderer class in a self-executing anonymous function. The following example is based on the source code for the `contexthub.browserinfo` UI module. This UI module is a simple extension of the `ContextHub.UI.BaseModuleRenderer` class.

```javascript
;(function() {

    var SurferinfoRenderer = new Class({
        extend: ContextHub.UI.BaseModuleRenderer,

        defaultConfig: {
            icon: 'coral-Icon--globe',
            title: 'Browser/OS Information',

            storeMapping: {
                surferinfo: 'surferinfo'
            },

            template:
                '<p>{{surferinfo.browser.family}} {{surferinfo.browser.version}}</p>' +
                '<p>{{surferinfo.os.name}} {{surferinfo.os.version}}</p>'
        }
    });

    ContextHub.UI.registerRenderer('contexthub.browserinfo', new SurferinfoRenderer());

}());
```

The javascript file that includes the code that creates and registers the renderer must be included in a [client library folder](/help/implementing/developing/introduction/clientlibs.md). The category of the folder must match the following pattern:

```javascript
contexthub.module.[moduleType]
```

The `[moduleType]` part of the category is the `moduleType` with which the module renderer is registered. For example, for the `moduleType` of `contexthub.browserinfo`, the category of the client library folder must be `contexthub.module.contexthub.browserinfo`.
