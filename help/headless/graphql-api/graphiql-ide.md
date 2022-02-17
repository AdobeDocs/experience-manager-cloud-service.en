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


The **GraphiQL** tool allows you to test and debug your GraphQL queries by enabling you to:
* select the **Endpoint** that you want to use for your queries
* directly input queries, or access **[Persisted Queries](/help/headless/graphql-api/persisted-queries.md)**
* run your queries to immediately see the the results
* manage **Query Variables** and **Request Headers**
* select the **Endpoint** appropriate to your Sites configuration.
* save, and manage **Persisted Queries**
* publish, or unpublish, **Persisted Queries**
* see the **History** of your previous queries
* use the **Documentation Explorer** to access the documentation; helping you to learn and understand what methods are available.

For example: 

* `http://localhost:4502/content/graphiql.html`

![GraphiQL Interface](assets/cfm-graphiql-interface.png "GraphiQL Interface")

## Selecting your endpoint {#selecting-endpoint}

As a first step you need to select the **[Endpoint](/help/headless/graphql-api/graphql-endpoint.md)** that you want to use for the queries. 

This is available from the drop-down list at the top-right.

## Creating Queries {#creating-queries}

You can enter your new query in the editor - which is in the middle-left panel, directly under the GraphiQL logo.

>[!NOTE]
>
>GraphQL queries typically start with a `{` character. 
>
>Lines that start with a `#` are ignored.

Just start typing, the editor also:

* uses mouse-over to show you additional information about elements
* provides features such as syntax-highlighting, auto-complete, auto-suggest

## Running Queries {#running-queries}

You can run your new query immediately, or you can load and run a persisted query. In either case, the query showing in the editor panel is the query that will be executed when you either:

* click/tap on the **Execute Query** icon
* use the keyboard combination `Control-Enter`

## Saving Persisted Queries {#saving-persisted-queries}

<!-- 
is it possible to save a new query here?
having issues either:
deselecting a persisted query to allow me to save a new one 
or updating the currently selected persisted query
ie got message "Persisted Query: article-by-author was not found for an Update"
and at the moment persisted queries and the Save button aren't visible on the test instance anyway
-->

## Publishing Persisted Queries {#publishing-persisted-queries}

Once you have selected your persisted query from the list (left panel) you can use the **Publish** and **Unpublish** actions.

<!--
at the moment they're not visible on the test instance
 -->

## Keyboard shortcuts {#keyboard-shortcuts}

There are a selection of keyboard shortcuts that provide direct access to action icons in the IDE:

* Prettify Query:  `Shift-Control-P` 
* Merge Query:  `Shift-Control-M` 
* Execute Query:  `Control-Enter` 
* Auto Complete:  `Control-Space` 

>[!NOTE]
>
>On some keyboards the `Control` key is labelled as `Ctrl`.