---
title: Using the GraphiQL IDE in AEM
description: Learn how to use the GraphiQL IDE in Adobe Experience Manager.
feature: Content Fragments,GraphQL API
exl-id: be2ebd1b-e492-4d77-b6ef-ffdea9a9c775
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

You can access the query editor from either: 

* **Tools** -> **General** -> **GraphQL Query Editor**
* directly; for example, `http://localhost:4502/aem/graphiql.html`

![GraphiQL Interface](assets/cfm-graphiql-interface.png "GraphiQL Interface")

You can use GraphiQL on your development author system so that they can be requested by your client application using GET requests, and publishing queries. For production usage, you must then [move your queries to your production environment](/help/headless/graphql-api/persisted-queries.md#transfer-persisted-query-production). Initially to production author for validating newly authored content with the queries, and finally production publish for live consumption.

## Selecting your endpoint {#selecting-endpoint}

As a first step you need to select the **[Endpoint](/help/headless/graphql-api/graphql-endpoint.md)** that you want to use for the queries. The endpoint is appropriate to the Sites configuration that you want to use for your queries.

This is available from the drop-down list at the top-right.

## Creating, and persisting, a new query {#creating-new-query}

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

Use **Save As** to persist your new query.

## Updating your persisted query {#updating-persisted-query}

Select the query you want to update from the list in the **Persisted Queries** panel (far left).

The query will be shown in the editor panel. Make any changes you need, then use **Save** to commit your updates to the persisted query.

## Running queries {#running-queries}

You can run a new query immediately, or you can load and run a persisted query. To load a persisted query, select it from the list - the query will be shown in the editor panel.

In either case, the query showing in the editor panel is the query that will be executed when you either:

* click/tap on the **Execute Query** icon
* use the keyboard combination `Control-Enter`

## Query variables {#query-variables}

<!-- more details needed here? -->

The GraphiQL IDE also allows you to manage your [Query Variables](/help/headless/graphql-api/content-fragments.md#graphql-variables).

For example:

![GraphQL Variables](assets/cfm-graphqlapi-03.png "GraphQL Variables")

## Publishing persisted queries (dev-publish) {#publishing-persisted-queries}

Once you have selected your persisted query from the list (left panel) you can use the **Publish** and **Unpublish** actions. This will activate them to your development publish environment (`dev-publish`) environment for easy access by your applications when testing.

>[!NOTE]
>
>The definition of the persisted query's cache `Time To Live` {"cache-control":"parameter":value} has a default value of 2 hours (7200 seconds).

## Caching your persisted queries {#caching-persisted-queries}

AEM will invalidate the Content Delivery Network (CDN) cache based on a default Time To Live (TTL). 

This value is set to:

* 7200 seconds is the default TTL for the Dispatcher and CDN; also known as *shared caches*
  * default: s-maxage=7200
* 60 is the default TTL for the client (for example, a browser)
  * default: maxage=60

AEM GraphQL queries that were persisted with the GraphiQL UI will use the default TTL upon execution. If you want to change the TTL for your GraphLQ query, then the query must instead be persisted using the API method. This involves posting the query to AEM using CURL in your command line interface. 

For an example:

```xml
curl -X PUT \
    -H 'authorization: Basic YWRtaW46YWRtaW4=' \
    -H "Content-Type: application/json" \
    "http://localhost:4502/graphql/persist.json/wknd/plain-article-query-max-age" \
    -d \
'{ "query": "{articleList { items { _path author main { json } referencearticle { _path } } } }", "cache-control": { "max-age": 300 }}'
```

The `cache-control` can be set at the creation time (PUT) or later on (for example, via a POST request for instance). The cache-control is optional when creating the persisted query, as AEM can provide the default value. See [How to persist a GraphQL query](/help/headless/graphql-api/persisted-queries.md#how-to-persist-query), for an example of persisting a query using curl.

## Copy URL to directly access the query {#copy-url}

The **Copy URL** option allows you to simulate a query, by copying the URL used to directly access the persisted query and see the results. This can then be used for testing; for example, by accessing in a browser:

<!--
  >[!NOTE]
  >
  >The URL will need [encoding before using programmatically](/help/headless/graphql-api/persisted-queries.md#encoding-query-url).
  >
  >The target environment might need adjusting, depending on your requirements.
-->

For example:

`http://localhost:4502/graphql/execute.json/global/article-list-01`

By using this URL in a browser, you can confirm the results:

![GraphiQL - Copy URL](assets/cfm-graphiql-copy-url.png "GraphiQL - Copy URL")

The **Copy URL** option is accessible via the three vertical dots to the right of the persisted query name (far left panel):

![GraphiQL - Copy URL](assets/cfm-graphiql-persisted-query-options.png "GraphiQL - Copy URL")

## Deleting persisted queries {#deleting-persisted-queries}

The **Delete** option is also accessible via the three vertical dots to the right of the persisted query name (far left panel).

<!-- what happens if you try to delete something that is still published? -->


## Installing your Persisted Query on Production {#installing-persisted-query-production}

After developing and testing your persisted query with GraphiQL, the final goal is to [transfer it to your production environment](/help/headless/graphql-api/persisted-queries.md#transfer-persisted-query-production) for use by your applications.

## Keyboard shortcuts {#keyboard-shortcuts}

There are a selection of keyboard shortcuts that provide direct access to action icons in the IDE:

* Prettify Query:  `Shift-Control-P` 
* Merge Query:  `Shift-Control-M` 
* Execute Query:  `Control-Enter` 
* Auto Complete:  `Control-Space` 

>[!NOTE]
>
>On some keyboards the `Control` key is labelled as `Ctrl`.
