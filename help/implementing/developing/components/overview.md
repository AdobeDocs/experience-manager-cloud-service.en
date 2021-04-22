---
title: Components Overview
description: Components are modular units which realize specific functionality to present your content on your website
exl-id: 0fdc99e7-2103-448d-8217-d5d52c94acea
---
# Components Overview {#components-overview}

This page provides an overview of Adobe Experience Manager (AEM) components such as those [used for page authoring](/help/sites-cloud/authoring/fundamentals/components.md).

## What are Components? {#what-are-components}

Components in AEM are:

* Modular units which realize specific functionality to present your content on your website.
* Re-usable.
* Developed as self-contained units within one folder of the repository.
* Have no hidden configuration files.
* Can contain other components.
* Can run anywhere within any AEM system and can also be limited to run under specific components.
* Have a standardized user interface.
* Have edit behavior that can be configured.
* Use dialog boxes that are built using sub-elements based on Granite UI components.
* Are developed using [HTL](https://docs.adobe.com/content/help/en/experience-manager-htl/using/overview.html).
* Can be developed to create customized components that extend the default functionality.

Because components are modular, you can:

* Develop a new component on your local instance.
* Deploy it to your test environment.
* Deploy it to your live authoring environment, where they allow authors and/or administrators to add and configure content.
* Deploy it to your live publish environment(s), where they are used to render content for visitors to your website.

Each AEM component:

* Is a resource type.
* Is a collection of scripts that completely realize a specific function.
* Can function in isolation, meaning either within AEM or a portal.

## AEM Core Components {#aem-core-components}

[The AEM Core Components](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/introduction.html) are a set of standardized Web Content Management (WCM) components for AEM to speed up development time and reduce maintenance cost of your websites.

The Core Components are provided with AEM as a Cloud Service and the [WKND Tutorial](/help/implementing/developing/introduction/develop-wknd-tutorial.md) illustrates how to implement and use components. The components are provided with all source code and can be used as is or as starting points for modified or extended components.

### Viewing Available Components {#viewing-available-components}

For an overview of all of the available components in your AEM instance, use the [Components Console](/help/sites-cloud/authoring/features/components-console.md).

Alternatively, you can also use CRXDE Lite to get a list of all the components available in the repository.

1. In **[!UICONTROL CRXDE Lite]**, select **[!UICONTROL Tools]** from the toolbar, then **[!UICONTROL Query]**, which opens the **[!UICONTROL Query]** tab.

1. In the **[!UICONTROL Query]** tab, select `XPath` as **[!UICONTROL Type]**.

1. In the **[!UICONTROL Query]** input field, enter following string:

   `//element(*, cq:Component)`

1. Click **[!UICONTROL Execute]** and the components are listed.
