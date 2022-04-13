---
title: Create an API Request - Headless Setup
description: Learn how to use the GraphQL API for headless delivery of Content Fragment content and AEM's Assets REST API to manage Content Fragments.
exl-id: 2b72f222-2ba5-4a21-86e4-40c763679c32
---
# Create an API Request - Headless Setup {#accessing-delivering-content-fragments}

Learn how to use the GraphQL API for headless delivery of Content Fragment content and AEM's Assets REST API to manage Content Fragments.

## What are GraphQL and Assets REST APIs? {#what-are-the-apis}

[Now that you have created some content fragments,](create-content-fragment.md) you can use AEM's APIs to deliver them headlessly.

* [The GraphQL API](/help/headless/graphql-api/content-fragments.md) allows you to create requests to access and deliver Content Fragments. This API offers the most robust set of capabilities for querying and consuming Content Fragment content.
   * To use this, [endpoints need to be defined and enabled in AEM](/help/headless/graphql-api/graphql-endpoint.md), and if required, the [GraphiQL interface installed](/help/headless/graphql-api/graphiql-ide.md).
* [The Assets REST API](/help/assets/content-fragments/assets-api-content-fragments.md) allows you to create and modify Content Fragments (and other assets).

The remainder of this guide will focus on GraphQL access and Content Fragment delivery.

## Enable GraphQL Endpoint

Before the GraphQL APIs can be used, a GraphQL endpoint must be created.

1. Navigate to **Tools**, **General**, then select **GraphQL**.
1. Select **Create**.
1. The **Create new GraphQL Endpoint** dialog will open. Here you can specify:
   * **Name**: name of the endpoint; you can enter any text.
   * **Use GraphQL schema provided by**: use the dropdown to select the required configuration.
1. Confirm with **Create**.
1. In the console a **Path** will now be displayed based on the configuration created earlier. This is the path used to execute GraphQL queries.

    ```
    /content/cq:graphql/<configuration-name>/endpoint
    ```

More details about enabling [GraphQL endpoints can be found here](/help/headless/graphql-api/graphql-endpoint.md).

## Query content using GraphQL with GraphiQL

Information architects will need to design queries for their channel endpoints in order to deliver content. These queries will generally only need to be considered once per endpoint per model. For the purposes of this getting started guide we will only need to create one.

GraphiQL is an IDE that can be installed on an AEM environment. Follow the steps on [Using the GraphiQL IDE](/help/headless/graphql-api/graphiql-ide.md) to install on your AEM environment. 

1. Log into AEM as a Cloud Service and access the GraphiQL interface:

   You can access the query editor from either: 

   * **Tools** -> **General** -> **GraphQL Query Editor**
   * directly; for example, `http://localhost:4502/aem/graphiql.html`

1. The GraphiQL IDE is an in-browser query editor for GraphQL. You can use it to build queries to retrieve Content Fragments to deliver them headlessly as JSON.
   * The drop-down top-right allows you to select the endpoint.
   * A far-left panel lists the persisted queries (when available)
   * The middle-left panel allows you to build your query.
   * The middle-right panel displays the results.
   * The query editor features code completion and hotkeys to easily execute the query.

   ![GraphiQL editor](../assets/graphiql.png)

1. Assuming that the model we created was called `person` with fields `firstName`, `lastName`, and `position`, we can build a simple query to retrieve the content of our Content Fragment.

   ```text
   query 
   {
     personList {
       items {
         _path
         firstName
         lastName
         position
       }
     }
   }
   ```

1. Enter the query into the left panel.
   ![GraphiQL query](../assets/graphiql-query.png)

1. Click the **Execute Query** button or use the `Ctrl-Enter` hotkey and the results are displayed as JSON in the right panel.
   ![GraphiQL results](../assets/graphiql-results.png)

1. Click the **Docs** link at the top-right of the page to show in-context documentation to help you build your queries which adapts to your own models.
   ![GraphiQL documentation](../assets/graphiql-documentation.png)

GraphQL enables structured queries that can target not only specific data sets or individual data objects, but also can deliver specific elements of the objects, nested results, offers support for query variables, and much more.

GraphQL can avoid iterative API requests as well as over-delivery, and instead allows for bulk delivery of exactly what is needed for rendering as a response to a single API query. The resulting JSON can be used to deliver data to other sites or apps.

## Next Steps {#next-steps}

That's it! You now have a basic understanding of headless content management in AEM. Of course there are many more resources where you can dive deeper for a comprehensive understanding of the features available.

* **[Content Fragments](/help/assets/content-fragments/content-fragments.md)** - For details about creating and managing Content Fragments
* **[Content Fragments Support in AEM Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md)** - For details on accessing AEM content directly over the HTTP API, via CRUD operations (Create, Read, Update, Delete)
* **[GraphQL API](/help/headless/graphql-api/content-fragments.md)** - For details on how to deliver Content Fragments headlessly
