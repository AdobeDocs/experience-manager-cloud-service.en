---
title: Using the GraphiQL IDE in AEM
description: Learn how to use the GraphiQL IDE in Adobe Experience Manager.
feature: Content Fragments,GraphQL API
---

# Using the GraphiQL IDE {#graphiql-ide}

An implementation of the standard [GraphiQL](https://graphql.org/learn/serving-over-http/#graphiql) IDE is available for use with the GraphQL API of Adobe Experience Manager (AEM) as a Cloud Service. 

>[!NOTE]
>
>GraphiQL is included in AEM, but by default it is only enabled on the `dev-authors` environments.

>[!NOTE]
>You must have [configured your endpoints](/help/headless/graphql-api/graphql-endpoint.md) in the [configuration browser](/help/assets/content-fragments/content-fragments-configuration-browser.md) before using the GraphiQL IDE.


The **GraphiQL** tool allows you to test and debug your GraphQL queries by enabling you to:
* select the **Endpoint** appropriate to the Sites configuration that you want to use for your queries
* directly input new queries 
* create, and access, **[Persisted Queries](/help/headless/graphql-api/persisted-queries.md)**
* run your queries to immediately see the the results
* manage **Query Variables** 
* save, and manage **Persisted Queries**
* publish, or unpublish, **Persisted Queries** (to/from `dev-publish`)
* see the **History** of your previous queries
* use the **Documentation Explorer** to access the documentation; helping you to learn and understand what methods are available.

<!-- what happened to request headers? -->

For example: 

* `http://localhost:4502/content/graphiql.html`

![GraphiQL Interface](assets/cfm-graphiql-interface.png "GraphiQL Interface")

## Selecting your endpoint {#selecting-endpoint}

As a first step you need to select the **[Endpoint](/help/headless/graphql-api/graphql-endpoint.md)** that you want to use for the queries. The endpoint is appropriate to the Sites configuration that you want to use for your queries.

This is available from the drop-down list at the top-right.

## Creating new queries {#creating-queries}

You can enter your new query in the editor - which is in the middle-left panel, directly under the GraphiQL logo.

>[!NOTE]
>
>If you have a persisted query already selected, and showing in the editor panel, then select `+` (next to **Persisted Queries**) to empty the editor ready for your new query.

Just start typing, the editor also:

* uses mouse-over to show you additional information about elements
* provides features such as syntax-highlighting, auto-complete, auto-suggest

>[!NOTE]
>
>GraphQL queries typically start with a `{` character. 
>
>Lines that start with a `#` are ignored.

## Running queries {#running-queries}

You can run your new query immediately, or you can load and run a persisted query. To load a persisted query, select it from the list - the query will be shown in the editor panel.

In either case, the query showing in the editor panel is the query that will be executed when you either:

* click/tap on the **Execute Query** icon
* use the keyboard combination `Control-Enter`

## Query variables {#query-variables}

<!-- more details needed here? -->

The GraphiQL IDE also allows you to manage your [Query Variables](/help/headless/graphql-api/content-fragments.md#graphql-variables)

## Saving persisted queries {#saving-persisted-queries}

You can either use:

* **Save As** to persist a new query
* **Save** to save updates changes to the persisted query that is currently loaded in the editor

## Publishing persisted queries {#publishing-persisted-queries}

Once you have selected your persisted query from the list (left panel) you can use the **Publish** and **Unpublish** actions. This will activate them to your publish (`dev-publish`) environment for easy access by your applications when testing.

<!-- mention caching here? need more details -->

>[!NOTE]
>
>The definition of the persisted query's cache `Time To Live` {"cache-control":"parameter":value} has a default value of 600ms.

## Copy URL to access the query from your app {#copy-url}

The **Copy URL** option allows you to copy the URL used to directly access the persisted query and see the results. This can then be used for:

* testing
* embedding in your application, for use with your production environment

For example:

`http://localhost:4502/graphql/execute.json/global/article-list-01`

By using this URL in a browser, you can confirm the results:

![GraphiQL - Copy URL](assets/cfm-graphiql-copy-url.png "GraphiQL - COpy URL")

The **Copy URL** option is accessible via the three vertical dots to the right of the persisted query name (far left panel):

![GraphiQL - Copy URL](assets/cfm-graphiql-persisted-query-options.png "GraphiQL - COpy URL")

## Deleting persisted queries {#deleting-persisted-queries}

The **Delete** option is also accessible via the three vertical dots to the right of the persisted query name (far left panel).

<!-- what happens if you try to delete something that is still published? -->

## Keyboard shortcuts {#keyboard-shortcuts}

There are a selection of keyboard shortcuts that provide direct access to action icons in the IDE:

* Prettify Query:  `Shift-Control-P` 
* Merge Query:  `Shift-Control-M` 
* Execute Query:  `Control-Enter` 
* Auto Complete:  `Control-Space` 

>[!NOTE]
>
>On some keyboards the `Control` key is labelled as `Ctrl`.