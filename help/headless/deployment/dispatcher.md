---
title: Dispatcher configuration with AEM Headless
description: The Dispatcher is a caching and security layer in front of Adobe Experience Manager Publish environments. Several configurations are used to open GraphQL endpoints to headless applications.
feature: Dispatcher, GraphQL API
exl-id: 78a20021-910f-4cf0-87bf-6e2223994f76
---
# Dispatcher configuration with AEM Headless

The [Dispatcher](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/dispatcher.html) is a caching and security layer in front of Adobe Experience Manager Publish environments. Several configurations are included by default to open GraphQL endpoints to headless applications.

>[!NOTE]
>
>For detailed documentation about the Dispatcher see the [Dispatcher Guide](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/dispatcher.html)

As part of an AEM Project a dispatcher module is included that contains configurations for the dispatcher. Newly generated projects from the [AEM Project Archetype](https://github.com/adobe/aem-project-archetype) automatically includes [filters](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/configuring/dispatcher-configuration.html?#defining-a-filter) that enables GraphQL endpoints.

## GraphQL Endpoint(s)

As part of the default filters, [GraphQL endpoints](/help/headless/graphql-api/graphql-endpoint.md) are opened with the following rule:

```
/0060 { /type "allow" /method '(POST|OPTIONS)' /url "/content/_cq_graphql/*/endpoint.json" }
```

The `*` wildcard opens multiple endpoints on the AEM instance. Querying using a GraphQL endpoint will be made using `POST` and the response will **not** be cached.

## GraphQL Persisted Queries

The request for Persisted queries are made against a different endpoint. As part of the default filter configuration, the url for [Persisted queries](/help/headless/graphql-api/persisted-queries.md) are opened with the following rule:

```
/0061 { /type "allow" /method '(GET|POST|OPTIONS)' /url "/graphql/execute.json*" }
```

Persisted queries can be requested using `GET`, thereby caching the response at the Dispatcher and CDN level. More details about caching and cache invalidation can be found [here](/help/implementing/dispatcher/caching.md).
