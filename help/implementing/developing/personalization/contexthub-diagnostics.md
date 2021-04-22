---
title: ContextHub Diagnostics
description: ContextHub provides a diagnostics page where you can see an overview of the ContextHub framework
exl-id: c8d4e160-ea02-49f3-9e31-119445ef5a68
---
# ContextHub Diagnostics {#contexthub-diagnostics}

ContextHub provides a diagnostics page where you can see an overview of the ContextHub framework. To open the page, go to the `contexthub.diagnostics.html` page of your AEM author instance, for example:

`http://<host>:<port>/conf/<site>/settings/cloudsettings/default/contexthub.diagnostics.html`

The ContextHub Diagnostics page provides information about the stores and UI modules that have been created, the client library folders that are loaded, and links to useful pages.

>[!NOTE]
>
>In order for diagnostic information to be returned, debug mode must be enabled, otherwise the diagnostics page will be blank. Please see [this document](configuring-contexthub.md#debugging-contexthub) for details on how to enable debug mode.

## Stores {#stores}

The Stores section lists all the ContextHub stores that have been configured. Each item in the list consists of the following information:

* **Title:** The [store type](sample-stores.md) that the store is based on.
* **path:** The path to the repository node that holds the configuration.
* **resourceType:** The path of the repository node where the store type is defined.
* **clientlibs:** The categories of the client libraries that are loaded which implement the store type.

## Modules {#modules}

The Modules section lists all the ContextHub UI modules that have been configured. Each item in the list consists of the following information:

* **Title:** The [UI Module type](sample-modules.md) that the UI module is based on.
* **path:** The path to the repository node that holds the configuration.
* **resourceType:** The path of the repository node where the UI module type is defined.
* **clientlibs:** The categories of the client libraries that are loaded which implement the UI module type.

## Clientlibs {#clientlibs}

The Clientlibs section lists all of the [client library folders](/help/implementing/developing/introduction/clientlibs.md) that ContextHub has loaded. The client libraries are categorized as follows:

* **kernel.js:** Client libraries that implement the ContextHub framework, the segment engine, and store types.
* **ui.js:** Client libraries that implement the ContextHub UI and UI module types.
* **style.css:** CSS files that are loaded from client libraries.

## URLs {#urls}

The URLs section contains links to ContextHub features:

* **Configuration editor:** Opens the [ContextHub Configuration page](configuring-contexthub.md) where you can configure stores, UI modes, and UI modules.
* **Configuration of ContextHub modules:** Opens the `/etc/cloudsettings/default/contexthub.config.kernel.js` file, which contains the Javascript object representation of the ContextHub store configurations.
* **Configuration of ContextHub UI:** Opens the `/etc/cloudsettings/default/contexthub.config.ui.js` file, which contains the Javascript object representation of the ContextHub UI mode configurations.
* **kernel.js:** Opens the `/etc/cloudsettings/default/contexthub.kernel.js` file, which contains the source code of the client libraries that implement the ContextHub framework, the segment engine, and store types.
* **ui.js:** Opens the `/etc/cloudsettings/default/contexthub.ui.js` file, which contains the source code of the client libraries that implement the ContextHub UI and UI module types.
* **style.css:** Opens the `/etc/cloudsettings/default/contexthub.styles.css` file, which contains the CSS styles for the ContextHub UI and UI modules.
