---
title: Dispatcher endpoint configuration with AEM Headless
description: The Dispatcher is a caching and access-filtering layer in front of Adobe Experience Manager Publish environments. Several configurations are used to open GraphQL endpoints to headless applications.
feature: Headless, Dispatcher, GraphQL API
exl-id: 78a20021-910f-4cf0-87bf-6e2223994f76
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: bfd4bc52-c397-5127-8f86-8953ba9fc0a3
    internal-label: Headless
  - id: 2741637d-a621-529a-b21b-bfe9be07a9c8
    internal-label: Dispatcher
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Dispatcher - Endpoint configuration with AEM Headless

The [Dispatcher](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/dispatcher.html) is a caching and access-filtering layer in front of Adobe Experience Manager Publish environments. Several configurations are included by default to open GraphQL endpoints to headless applications.

>[!IMPORTANT]
>
>Dispatcher filter rules are access-filtering controls, not a substitute for JCR ACL-based access control on the publish instance. The publish instance must be secured independently of Dispatcher configuration. Ensure that sensitive resources are protected by denying `jcr:read` for the `everyone` and `anonymous` principals at the repository level, regardless of Dispatcher filter configuration.

>[!NOTE]
>
>For detailed documentation about the Dispatcher, see the [Dispatcher Guide](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/dispatcher.html).

As part of an AEM Project a Dispatcher module is included that contains configurations for the Dispatcher. Newly generated projects from the [AEM Project Archetype](https://github.com/adobe/aem-project-archetype) automatically include [filters](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/configuring/dispatcher-configuration.html?#defining-a-filter) that enable GraphQL endpoints.

## GraphQL Endpoints

As part of the default filters, [GraphQL endpoints](/help/headless/graphql-api/graphql-endpoint.md) are opened with the following rule:

```
/0060 { /type "allow" /method '(POST|OPTIONS)' /url "/content/_cq_graphql/*/endpoint.json" }
```

The `*` wildcard opens multiple endpoints on the AEM instance. Querying using a GraphQL endpoint is made using `POST` and the response is **not** cached.

## GraphQL Persisted Queries

The request for Persisted queries is made against a different endpoint. As part of the default filter configuration, the url for [Persisted queries](/help/headless/graphql-api/persisted-queries.md) is opened with the following rule:

```
/0061 { /type "allow" /method '(GET|POST|OPTIONS)' /url "/graphql/execute.json*" }
```

Persisted queries can be requested using `GET`, by caching the response at the Dispatcher and CDN level. More details about caching and cache invalidation can be found under [the Introduction to Caching in AEM as a Cloud Service](/help/implementing/dispatcher/caching.md).
