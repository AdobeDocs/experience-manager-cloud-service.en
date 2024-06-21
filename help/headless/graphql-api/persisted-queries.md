---
title: Persisted GraphQL queries
description: Learn how to persist GraphQL queries in Adobe Experience Manager as a Cloud Service to optimize performance. Persisted queries can be requested by client applications using HTTP GET method and the response can be cached at the dispatcher and CDN layers, ultimately improving the performance of the client applications.
feature: Headless, Content Fragments,GraphQL API
exl-id: 080c0838-8504-47a9-a2a2-d12eadfea4c0
role: Admin, Developer
---
# Persisted GraphQL queries {#persisted-graphql-queries}

Persisted queries are GraphQL queries that are created and stored on the Adobe Experience Manager (AEM) as a Cloud Service server. They can be requested with a GET request by client applications. The response of a GET request can be cached at the dispatcher and CDN layers, ultimately improving the performance of the requesting client application. This differs from standard GraphQL queries, which are executed using POST requests where the response cannot easily be cached.

>[!NOTE]
>
>Persisted Queries are recommended. See [GraphQL Query Best Practices (Dispatcher)](/help/headless/graphql-api/content-fragments.md#graphql-query-best-practices) for details, and the related Dispatcher configuration.

The [GraphiQL IDE](/help/headless/graphql-api/graphiql-ide.md) is available in AEM for you to develop, test, and persist your GraphQL queries, before [transferring to your production environment](#transfer-persisted-query-production). For cases that need customization (for example, when [customizing the cache](/help/headless/graphql-api/graphiql-ide.md#caching-persisted-queries)) you can use the API; see the cURL example provided in [How to persist a GraphQL query](#how-to-persist-query).

## Persisted Queries and Endpoints {#persisted-queries-and-endpoints}

Persisted queries must always use the endpoint related to the [appropriate Sites configuration](graphql-endpoint.md); so they can use either, or both:

* The Global configuration and endpoint
  The query has access to all Content Fragment Models.
* Specific Sites configuration(s) and endpoint(s)
  Creating a persisted query for a specific Sites configuration requires a corresponding Sites-configuration-specific endpoint (to provide access to the related Content Fragment Models). 
  For example, to create a persisted query specifically for the WKND Sites configuration, a corresponding WKND-specific Sites configuration, and a WKND-specific endpoint must be created in advance.

>[!NOTE]
>
>See [Enable Content Fragment Functionality in Configuration Browser](/help/sites-cloud/administering/content-fragments/setup.md#enable-content-fragment-functionality-configuration-browser) for more details.
>
>The **GraphQL Persisted Queries** need to be enabled, for the appropriate Sites configuration. 

For example, if there is a particular query called `my-query`, which uses a model `my-model` from the Sites configuration `my-conf`:

* You can create a query using the `my-conf` specific endpoint, and then the query is saved as following: 
`/conf/my-conf/settings/graphql/persistentQueries/my-query`
* You can create the same query using `global` endpoint, but then the query is saved as following:
`/conf/global/settings/graphql/persistentQueries/my-query`

>[!NOTE]
>
>These are two different queries - saved under different paths. 
>
>They just happen to use the same model - but via different endpoints.

## How to persist a GraphQL query {#how-to-persist-query}

It is recommended to persist queries on an AEM author environment initially and then [transfer the query](#transfer-persisted-query-production) to your production AEM publish environment, for use by applications. 

There are various methods of persisting queries, including:

* GraphiQL IDE - see [Saving Persisted Queries](/help/headless/graphql-api/graphiql-ide.md#saving-persisted-queries) (preferred method)
* cURL - see the following example
* Other tools, including [Postman](https://www.postman.com/)

The GraphiQL IDE is the **preferred** method for persisting queries. To persist a given query using the **cURL** command line tool:

1. Prepare the query by PUTing it to the new endpoint URL `/graphql/persist.json/<config>/<persisted-label>`.

   For example, create a persisted query:

   ```shell
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

     ```json
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

   ```shell
   $ curl -X GET \
       http://localhost:4502/graphql/execute.json/wknd/plain-article-query
   ```

1. Update a persisted query by POSTing to an already existing query path.

   For example, use the persisted query:

   ```shell
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

   ```shell
   $ curl -X PUT \
       -H 'authorization: Basic YWRtaW46YWRtaW4=' \
       -H "Content-Type: application/json" \
       "http://localhost:4502/graphql/persist.json/wknd/plain-article-query-wrapped" \
       -d \
   '{ "query": "{articleList { items { _path author main { json } referencearticle { _path } } } }"}'
   ```

1. Create a wrapped plain query with cache control.

   For example:

   ```shell
   $ curl -X PUT \
       -H 'authorization: Basic YWRtaW46YWRtaW4=' \
       -H "Content-Type: application/json" \
       "http://localhost:4502/graphql/persist.json/wknd/plain-article-query-max-age" \
       -d \
   '{ "query": "{articleList { items { _path author main { json } referencearticle { _path } } } }", "cache-control": { "max-age": 300 }}'
   ```

1. Create a persisted query with parameters:

   For example:

   ```shell
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


## How to execute a Persisted query {#execute-persisted-query}

To execute a Persisted query, a client application makes a GET request using the following syntax:

```
GET <AEM_HOST>/graphql/execute.json/<PERSISTENT_PATH>
```

Where `PERSISTENT_PATH` is a shortened path to where the Persisted query is saved.

1. For example, `wknd` is the configuration name and `plain-article-query` is the name of the Persisted query. To execute the query:

   ```shell
   $ curl -X GET \
       https://publish-p123-e456.adobeaemcloud.com/graphql/execute.json/wknd/plain-article-query
   ```

1. Executing a query with parameters.

    >[!NOTE]
    >
    > Query variables and values must be properly [encoded](#encoding-query-url) when executing a Persisted query.

   For example:

   ```xml
   $ curl -X GET \
       "https://publish-p123-e456.adobeaemcloud.com/graphql/execute.json/wknd/plain-article-query-parameters%3Bapath%3D%2Fcontent%2Fdam%2Fwknd%2Fen%2Fmagazine%2Falaska-adventure%2Falaskan-adventures%3BwithReference%3Dfalse
   ```

   See using [query variables](#query-variables) for more details.

## Using query variables {#query-variables}

Query variables can be used with Persisted Queries. The query variables are appended to the request prefixed with a semicolon (`;`) using the variable name and value. Multiple variables are separated by semicolons. 

The pattern looks like the following:

```
<AEM_HOST>/graphql/execute.json/<PERSISTENT_QUERY_PATH>;variable1=value1;variable2=value2
```

For example, the following query contains a variable `activity` to filter a list based on an activity value:

```graphql
query getAdventuresByActivity($activity: String!) {
      adventureList (filter: {
        adventureActivity: {
          _expressions: [
            {
              value: $activity
            }
          ]
        }
      }){
        items {
          _path
        adventureTitle
        adventurePrice
        adventureTripLength
      }
    }
  }
```

This query can be persisted under a path `wknd/adventures-by-activity`. To call the Persisted query where `activity=Camping` the request would look like this:

```
<AEM_HOST>/graphql/execute.json/wknd/adventures-by-activity%3Bactivity%3DCamping
```

The UTF-8 encoding `%3B` is for `;` and `%3D` is the encoding for `=`. The query variables and any special characters must be [encoded properly](#encoding-query-url) for the Persisted query to execute.

### Using query variables - Best Practices {#query-variables-best-practices}

When using variables in your queries there are a few best practices that should be followed:

* Encoding
  As a general approach, it is always recommended to encode all special characters; for example, `;`, `=`, `?`, `&`, among others.

* Semicolon
  Persisted queries that use multiple variables (that are separated by semicolons) need to have either:
  * the semicolons encoded (`%3B`); encoding the URL will also achieve this
  * or a trailing semicolon added to the end of the query

* `CACHE_GRAPHQL_PERSISTED_QUERIES`
  When `CACHE_GRAPHQL_PERSISTED_QUERIES` is enabled for the Dispatcher, then parameters that contain the `/` or `\` characters in their value, are encoded twice at the Dispatcher level. 
  To avoid this situation:

  * Enable `DispatcherNoCanonURL` on the Dispatcher.
    This will instruct the Dispatcher to forward the original URL to AEM, so preventing duplicated encodings. 
    However this setting currently only works on the `vhost` level, so if you already have Dispatcher configurations to rewrite URLs (e.g. when using shortened URLs) you might need a separate `vhost` for persisted query URLs.

  * Send `/` or `\` characters unencoded.
    When calling the persisted query URL ensure that all `/` or `\` characters remain unencoded in the value of persisted query variables.
    >[!NOTE]
    >
    >This option is only recommended for when the `DispatcherNoCanonURL` solution cannot be implemented for any reason.

* `CACHE_GRAPHQL_PERSISTED_QUERIES`

   When `CACHE_GRAPHQL_PERSISTED_QUERIES` is enabled for the Dispatcher, then the `;` character cannot be used in the value of a variable.

## Caching your persisted queries {#caching-persisted-queries}

Persisted queries are recommended as they can be cached at the [Dispatcher](/help/headless/deployment/dispatcher.md) and Content Delivery Network (CDN) layers, ultimately improving the performance of the requesting client application.

By default AEM will invalidate cache based on a Time To Live (TTL) definition. These TTLs can be defined by the following parameters. These parameters can be accessed by various means, with variations in the names according to the mechanism used:

|Cache Type |[HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) |cURL |OSGi Configuration |Cloud Manager |
|--- |--- |--- |--- |--- |
|Browser |`max-age` |`cache-control : max-age` |`cacheControlMaxAge` |`graphqlCacheControl` |
|CDN |`s-maxage` |`surrogate-control : max-age` |`surrogateControlMaxAge` |`graphqlSurrogateControl` |60 |
|CDN |`stale-while-revalidate` |`surrogate-control : stale-while-revalidate `|`surrogateControlStaleWhileRevalidate` |`graphqlStaleWhileRevalidate` |
|CDN |`stale-if-error` |`surrogate-control : stale-if-error` |`surrogateControlStaleIfError` |`graphqlStaleIfError` |

{style="table-layout:auto"}

### Author instances {#author-instances}

For author instances the default values are:

* `max-age`  : 60
* `s-maxage` : 60
* `stale-while-revalidate` : 86400
* `stale-if-error` : 86400

These:

* cannot be overwritten:
  * with an OSGi configuration
* can be overwritten:
  * by a request that defines HTTP header settings using cURL; it should include suitable settings for `cache-control` and/or `surrogate-control`; for examples, see [Managing Cache at the Persisted Query Level](#cache-persisted-query-level)
  * if you specify values in the **Headers** dialog of the [GraphiQL IDE](#http-cache-headers-graphiql-ide)

### Publish instances {#publish-instances}

For publish instances the default values are:

* `max-age`  : 60
* `s-maxage` : 7200
* `stale-while-revalidate` : 86400
* `stale-if-error` : 86400

These can be overwritten:

* [from the GraphQL IDE](#http-cache-headers-graphiql-ide)

* [at the Persisted Query Level](#cache-persisted-query-level); this involves posting the query to AEM using cURL in your command line interface, and publishing the Persisted Query.

* [with Cloud Manager variables](#cache-cloud-manager-variables)

* [with an OSGi configuration](#cache-osgi-configration)

### Managing HTTP Cache Headers in the GraphiQL IDE {#http-cache-headers-graphiql-ide}

The GraphiQL IDE - see [Saving Persisted Queries](/help/headless/graphql-api/graphiql-ide.md#managing-cache)

### Managing Cache at the Persisted Query Level {#cache-persisted-query-level}

This involves posting the query to AEM using cURL in your command line interface. 

For an example of the PUT (create) method:

```bash
curl -u admin:admin -X PUT \
--url "http://localhost:4502/graphql/persist.json/wknd/plain-article-query-max-age" \
--header "Content-Type: application/json" \
--data '{ "query": "{articleList { items { _path author } } }", "cache-control": { "max-age": 300 }, "surrogate-control": {"max-age":600, "stale-while-revalidate":1000, "stale-if-error":1000} }'
```

For an example of the POST (update) method:

```bash
curl -u admin:admin -X POST \
--url "http://localhost:4502/graphql/persist.json/wknd/plain-article-query-max-age" \
--header "Content-Type: application/json" \
--data '{ "query": "{articleList { items { _path author } } }", "cache-control": { "max-age": 300 }, "surrogate-control": {"max-age":600, "stale-while-revalidate":1000, "stale-if-error":1000} }'
```

The `cache-control` can be set at the creation time (PUT) or later on (for example, via a POST request for instance). The cache-control is optional when creating the persisted query, as AEM can provide the default value. See [How to persist a GraphQL query](#how-to-persist-query), for an example of persisting a query using cURL.

### Managing Cache with Cloud Manager variables {#cache-cloud-manager-variables}

[Cloud Manager Environment Variables](/help/implementing/cloud-manager/environment-variables.md) can be defined with Cloud Manager to define the required values:

| Name | Value | Service Applied | Type | 
|--- |--- |--- |--- |
|`graphqlStaleIfError` |86400 | *as appropriate* | *as appropriate* |
|`graphqlSurrogateControl` |600 | *as appropriate* | *as appropriate* |

{style="table-layout:auto"}

### Managing Cache with an OSGi configuration {#cache-osgi-configration}

To manage the cache globally, you can [configure the OSGi settings](/help/implementing/deploying/configuring-osgi.md) for the **Persisted Query Service Configuration**.

>[!NOTE]
>
>For cache control, the OSGi configuration is only appropriate for publish instances. The configuration exists on author instances, but is ignored.

>[!NOTE]
>
>The **Persisted Query Service Configuration** is also used for [configuring the query response code](#configuring-query-response-code).

The default OSGi configuration for publish instances:

* reads the Cloud Manager variables if available: 

  | OSGi Configuration Property | reads this | Cloud Manager Variable |
  |--- |--- |--- |
  | `cacheControlMaxAge` | reads | `graphqlCacheControl`|
  | `surrogateControlMaxAge` | reads | `graphqlSurrogateControl` |
  | `surrogateControlStaleWhileRevalidate` | reads | `graphqlStaleWhileRevalidate` |
  | `surrogateControlStaleIfError` | reads | `graphqlStaleIfError` |

  {style="table-layout:auto"}

* and if not available, the OSGi configuration uses the [default values for publish instances](#publish-instances).

## Configuring the query response code {#configuring-query-response-code}

By default the `PersistedQueryServlet` sends a `200` response when it executes a query, regardless of the actual result.

You can [configure the OSGi settings](/help/implementing/deploying/configuring-osgi.md) for the **Persisted Query Service Configuration** to control whether more detailed status codes are returned by the `/execute.json/persisted-query` endpoint, when there is an error in the persisted query.

>[!NOTE]
>
>The **Persisted Query Service Configuration** is also used for [managing cache](#cache-osgi-configration).

The field `Respond with application/graphql-response+json` (`responseContentTypeGraphQLResponseJson`) can be defined as required:

* `false` (default value):
  It does not matter whether the persisted query is successful or not. The `Content-Type` header returned is `application/json`, and the `/execute.json/persisted-query` *always* returns the status code `200`.

* `true`:
  The returned `Content-Type` is `application/graphql-response+json`, and the endpoint will return the appropriate response code when there is any form of error upon running the persisted query: 

  | Code | Description |
  |--- |--- |
  | 200 | Successful response |
  | 400 | Indicates that there are missing headers, or an issue with the persisted query path. For example, configuration name not specified, suffix is not specified, and others.<br>See [Troubleshooting - GraphQL endpoint not configured](/help/headless/graphql-api/persisted-queries-troubleshoot.md#missing-path-query-url). |
  | 404 | The requested resource cannot be found. For example, the Graphql endpoint is not available on the server.<br>See [Troubleshooting - Missing path in the GraphQL persisted query URL](/help/headless/graphql-api/persisted-queries-troubleshoot.md#graphql-endpoint-not-configured). |
  | 500 | Internal server error. For example, validation errors, persistence error, and others. |

  >[!NOTE]
  >
  >See also https://graphql.github.io/graphql-over-http/draft/#sec-Status-Codes

## Encoding the query URL for use by an app {#encoding-query-url}

For use by an application, any special characters used when constructing query variables (that is, semicolons (`;`), equal sign (`=`), slashes `/`) must be converted to use the corresponding UTF-8 encoding.

For example:

```xml
curl -X GET \ "https://publish-p123-e456.adobeaemcloud.com/graphql/execute.json/wknd/adventure-by-path%3BadventurePath%3D%2Fcontent%2Fdam%2Fwknd%2Fen%2Fadventures%2Fbali-surf-camp%2Fbali-surf-camp"
```

The URL can be broken down into the following parts:

| URL Part | Description |
|----------| -------------|
| `/graphql/execute.json` | Persisted query endpoint |
| `/wknd/adventure-by-path` | Persisted query path |
| `%3B`                | Encoding of `;` |
| `adventurePath`      | Query variable |
| `%3D`                | Encoding of `=` |
| `%2F`                | Encoding of `/` |
| `%2Fcontent%2Fdam...` | Encoded path to the Content fragment |

In plain text the request URI looks like the following:

```plaintext
/graphql/execute.json/wknd/adventure-by-path;adventurePath=/content/dam/wknd/en/adventures/bali-surf-camp/bali-surf-camp
```

To use a persisted query in a client app, the AEM headless client SDK should be used for [JavaScript](https://github.com/adobe/aem-headless-client-js), [Java](https://github.com/adobe/aem-headless-client-java), or [NodeJS](https://github.com/adobe/aem-headless-client-nodejs). The Headless Client SDK will automatically encode any query variables appropriately in the request.

## Transferring a persisted query to your Production environment  {#transfer-persisted-query-production}

Persisted queries should always be created on an AEM Author service and then published (replicated) to an AEM Publish service. Often, Persisted queries are created and tested on lower environments like local or Development environments. It is then necessary to promote Persisted queries to higher level environments, ultimately making them available on a production AEM Publish environment for client applications to consume.

### Package Persisted queries

Persisted queries can be built into [AEM Packages](/help/implementing/developing/tools/package-manager.md). AEM Packages can then be downloaded and installed on different environments. AEM Packages can also be replicated from an AEM Author environment to AEM Publish environments.

To create a Package:

1. Navigate to **Tools** > **Deployment** > **Packages**.
1. Create a new package by tapping **Create Package**. This opens a dialog to define the Package.
1. In the Package Definition Dialog, under **General** enter a **Name** like "wknd-persistent-queries".
1. Enter a version number like "1.0".
1. Under **Filters** add a new **Filter**. Use the Path Finder to select the `persistentQueries` folder beneath the configuration. For example, for the `wknd` configuration, the full path is `/conf/wknd/settings/graphql/persistentQueries`.
1. Select **Save** to save the new Package definition and close the dialog.
1. Select the **Build** button in the created Package definition.

After the package has been built you can: 

* **Download** the package and re-upload on a different environment.
* **Replicate** the package by tapping **More** > **Replicate**. This will replicate the package to the connected AEM Publish environment.

<!--
1. Using replication/distribution tool:
   1. Go to the Distribution tool.
   1. Select tree activation for the configuration (for example, `/conf/wknd/settings/graphql/persistentQueries`).

* Using a workflow (via workflow launcher configuration):
  1. Define a workflow launcher rule for executing a workflow model that would replicate the configuration on different events (for example, create, modify, amongst others).
-->
