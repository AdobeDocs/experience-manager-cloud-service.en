---
title: AEM Edge Delivery Services REST OpenAPI
description: Learn about the AEM Edge Delivery Services REST OpenAPI
feature: Headless, Content Fragments, Edge Delivery Services
role: Admin, Developer
---

# AEM Edge Delivery Services REST OpenAPI {#aem-edge-delivery-services-rest-openapi}

In Adobe Experience Manager (AEM) as a Cloud Service, the AEM Edge Delivery Services REST OpenAPI:

* is a HTTP REST API on [AEM Edge Delivery Services](/help/edge/overview.md), designed to deliver structured content in JSON format
* uses the infrastructure of Edge Delivery Services, including CDN integration that allows active invalidation 
* focuses on content delivery (performance, scalability, CDN integration, optimized JSON control and output) 
* includes the ability to hydrate JSON for referenced fragments and assets

This API:

* is the successor to [Content Fragments Support in the AEM Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md)
* is equivalent to the [Content Fragments and Content Fragment Models OpenAPIs](/help/headless/content-fragment-openapis.md)
* is a HTTP REST alternative to the [AEM GraphQL API for use with Content Fragments](/help/headless/graphql-api/content-fragments.md) 

## REST vs GraphQL {#rest-vs-graphql}

The API used is a decision for the developers - AEM supports both. Many comparisons are available online, but a few highlights and benefits are: 

* Simplicity

  * Developers are (often) familiar with HTTP and REST. According to the [Postman State of the APIs report](https://www.postman.com/state-of-api/), a high percentage of developers use REST. 

  * With simplicity comes familiarity. With REST there are no organizational questions of who owns the queries and who owns the app, whereas these questions can arise with GraphQL. 

  * With familiarity (typically) comes a broad community and tooling landscape. Not an inherent disadvantage of GraphQL, but likely to be broader and deeper for REST. 

  * The simpler approach can also make the security implementation easier. With REST, the filtering to determine the content to render all happens in the client app. With GraphQL this happens in a schema-based query between client and server. 

* Flexibility

  * With REST, the developer can `GET` any resource. With GraphQL they are limited to resources defined within a schema. 

* Caching

  * JSON responses to REST `GET` requests are inherently cacheable. GraphQL `POST` requests are not cacheable, unless they are made so; for example, by using AEM Persisted Queries that are stored on the server and requested with REST-like `GET`requests. 

* Efficiency of content delivery 

  * Focus
    
    * With GraphQL client applications can request the exact content that they need for rendering - and no more. This approach prevents content over-delivery, with excessive content payloads, and unnecessary bandwidth consumption.

  * Single endpoint
  
    * While in REST every API request is an endpoint, in GraphQL there is only one common endpoint, and different content requests are expressed as queries using that common endpoint. 

* Rapid Prototyping

  * REST is a 2-step process:

    1. Fetch content with API.
    2. In the JSON response, determine what to use for rendering in the client app. 

    With GraphQL this is a one-step process, brought together in the GraphQL query, and can make prototyping easier. 

