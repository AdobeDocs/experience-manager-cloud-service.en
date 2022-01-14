---
title: Persisted GraphQL queries
description: Learn how to to persist GraphQL queries in Adobe Experience Manager to optimize performance. Persisted queries can be requested by client applications using HTTP GET method and the response can be cached at the dispatcher and CDN layers, ultimately improving the performance of the client applications.
feature: Content Fragments,GraphQL API
---

# Persisted GraphQL queries {#persisted-queries-caching}

Persisted queries are GraphQL queries that are created and stored on the AEM server. Standard GraphQL queries are executed using POST requests and the response cannot easily be cached. Persisted queries can be requested with a GET request by client applications. The response of a GET request can be cached at the dispatcher and CDN layers, ultimately improving the performance of the requesting client application.

Persisted queries must always use the endpoint related to the [appropriate Sites configuration](graphql-endpoint.md); so they can use either, or both:

* The Global configuration and endpoint
  The query has access to all Content Fragment Models.
* Specific Sites configuration(s) and endpoint(s)
  Creating a persisted query for a specific Sites configuration requires a corresponding Sites-configuration-specific endpoint (to provide access to the related Content Fragment Models). 
  For example, to create a persisted query specifically for the WKND Sites configuration, a corresponding WKND-specific Sites configuration, and a WKND-specific endpoint must be created in advance.

>[!NOTE]
>
>See [Enable Content Fragment Functionality in Configuration Browser](/help/assets/content-fragments/content-fragments-configuration-browser.md#enable-content-fragment-functionality-in-configuration-browser) for more details.
>
>The **GraphQL Persistence Queries** need to be enabled, for the appropriate Sites configuration. 

For example, if there is a particular query called `my-query`, which uses a model `my-model` from the Sites configuration `my-conf`:

* You can create a query using the `my-conf` specific endpoint, and then the query will be saved as following: 
`/conf/my-conf/settings/graphql/persistentQueries/my-query`
* You can create the same query using `global` endpoint, but then the query will be saved as following:
`/conf/global/settings/graphql/persistentQueries/my-query`

>[!NOTE]
>
>These are two different queries - saved under different paths. 
>
>They just happen to use the same model - but via different endpoints.

## How to persist a GraphQL query

It is recommended to persist queries on an AEM author environment initially and then [publish the query](#publish-persisted-query) to an AEM publish environment. Tools like [Postman](https://www.postman.com/) or command line tools like [curl](https://curl.se/) can be used.

Here are the steps to persist a given query using the **curl** command line tool:

1. Prepare the query by PUTing it to the new endpoint URL `/graphql/persist.json/<config>/<persisted-label>`.

   For example, create a persisted query:

   ```xml
   $ curl -X PUT \
       -H 'authorization: Basic YWRtaW46YWRtaW4=' \
       -H "Content-Type: application/json" \
       "http://localhost:4502/graphql/persist.json/wknd/plain-article-query" \
       -d \
   '{
     articleList {
       items{
           _path
           author
           main {
               json
           }
       }
     }
   }'
   ```

1. At this point, check the response.

   For example, check for success:

     ```xml
     {
       "action": "create",
       "configurationName": "wknd",
       "name": "plain-article-query",
       "shortPath": "/wknd/plain-article-query",
       "path": "/conf/wknd/settings/graphql/persistentQueries/plain-article-query"
     }
     ```

1. You can then request the persisted query by GETing the URL `/graphql/execute.json/<shortPath>`.

   For example, use the persisted query:

   ```xml
   $ curl -X GET \
       http://localhost:4502/graphql/execute.json/wknd/plain-article-query
   ```

1. Update a persisted query by POSTing to an already existing query path.

   For example, use the persisted query:

   ```xml
   $ curl -X POST \
       -H 'authorization: Basic YWRtaW46YWRtaW4=' \
       -H "Content-Type: application/json" \
       "http://localhost:4502/graphql/persist.json/wknd/plain-article-query" \
       -d \
   '{
     articleList {
       items{
           _path
           author
           main {
               json
           }
         referencearticle {
           _path
         }
       }
     }
   }'
   ```

1. Create a wrapped plain query.

   For example:

   ```xml
   $ curl -X PUT \
       -H 'authorization: Basic YWRtaW46YWRtaW4=' \
       -H "Content-Type: application/json" \
       "http://localhost:4502/graphql/persist.json/wknd/plain-article-query-wrapped" \
       -d \
   '{ "query": "{articleList { items { _path author main { json } referencearticle { _path } } } }"}'
   ```

1. Create a wrapped plain query with cache control.

   For example:

   ```xml
   $ curl -X PUT \
       -H 'authorization: Basic YWRtaW46YWRtaW4=' \
       -H "Content-Type: application/json" \
       "http://localhost:4502/graphql/persist.json/wknd/plain-article-query-max-age" \
       -d \
   '{ "query": "{articleList { items { _path author main { json } referencearticle { _path } } } }", "cache-control": { "max-age": 300 }}'
   ```

1. Create a persisted query with parameters:

   For example:

   ```xml
   $ curl -X PUT \
       -H 'authorization: Basic YWRtaW46YWRtaW4=' \
       -H "Content-Type: application/json" \
       "http://localhost:4502/graphql/persist.json/wknd/plain-article-query-parameters" \
       -d \
   'query GetAsGraphqlModelTestByPath($apath: String!, $withReference: Boolean = true) {
     articleByPath(_path: $apath) {
       item {
         _path
           author
           main {
           plaintext
           }
           referencearticle @include(if: $withReference) {
           _path
           }
         }
       }
     }'
   ```

1. Executing a query with parameters.

   For example:

   ```xml
   $ curl -X POST \
       -H 'authorization: Basic YWRtaW46YWRtaW4=' \
       -H "Content-Type: application/json" \
       "http://localhost:4502/graphql/execute.json/wknd/plain-article-query-parameters;apath=%2fcontent2fdam2fwknd2fen2fmagazine2falaska-adventure2falaskan-adventures;withReference=false"

   $ curl -X GET \
       "http://localhost:4502/graphql/execute.json/wknd/plain-article-query-parameters;apath=%2fcontent2fdam2fwknd2fen2fmagazine2falaska-adventure2falaskan-adventures;withReference=false"
   ```

## Publish a persisted query {#publish-persisted-query}

Persisted queries can be published to an AEM Publish environment where they can be requested by client applications. To use a persisted query on publish, the related persistent tree need to replicated.

There are several approaches for publishing a persisted query:

* **Using a POST for replication**:

    ```xml
    $ curl -X POST   http://localhost:4502/bin/replicate.json \
    -H 'authorization: Basic YWRtaW46YWRtaW4=' \
    -F path=/conf/wknd/settings/graphql/persistentQueries/plain-article-query \
    -F cmd=activate
    ```

* **Using a package**:
    1. Create a new package definition.
    1. Include the configuration (for example, `/conf/wknd/settings/graphql/persistentQueries`).
    1. Build the package.
    1. Replicate the package.

* **Using replication/distribution tool**:
    1. Go to the Distribution tool.
    1. Select tree activation for the configuration (for example, `/conf/wknd/settings/graphql/persistentQueries`).

* **Using a workflow (via workflow launcher configuration)**:
    1. Define a workflow launcher rule for executing a workflow model that would replicate the configuration on different events (for example, create, modify, amongst others).

Once the query configuration is on publish, the same authentication principles apply, just using the publish endpoint.

>[!NOTE]
>
>For anonymous access the system assumes that the ACL allows "everyone" to have access to the query configuration.
>
>If that is not the case it will not be able to execute.

>[!NOTE]
>
>Any semicolons (";") in the URLs need to be encoded.
>
>For example, as in the request to Execute a persisted query:
>
>```xml
>curl -X GET \ "http://localhost:4502/graphql/execute.json/wknd/plain-article-query-parameters%3bapath=%2fcontent2fdam2fwknd2fen2fmagazine2falaska-adventure2falaskan-adventures;withReference=false"
>```