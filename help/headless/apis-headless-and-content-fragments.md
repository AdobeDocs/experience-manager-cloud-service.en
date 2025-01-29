---
title: AEM APIs for Structured Content Delivery and Content Fragment Management
description: Learn about the APIs available for Structured Content Delivery and Content Fragment Management
feature: Headless, Content Fragments, Edge Delivery Services
role: Admin, Developer
exl-id: 95aecd30-566a-42a9-b97a-7efe45fd389c
---
# AEM APIs for Structured Content Delivery and Management {#aem-apis-structured-content-delivery-and-management}

Adobe Experience Manager (AEM) as a Cloud Service offers multiple APIs for both structured content delivery from Content Fragments and Content Fragment management. See the individual pages for further details of the specific APIs.

* [AEM REST OpenAPI for Content Fragment Delivery](/help/headless/aem-rest-openapi-content-fragment-delivery.md )
  * This API creates JSON responses for delivering structured content from Content Fragments in AEM. 
  * It uses a path to a content fragment as endpoint. 
  * This API is REST based.
  * It is optimized for content delivery, including CDN integration. 
* [AEM GraphQL API for Content Fragment delivery](/help/headless/graphql-api/content-fragments.md)
  * This API is schema-based. API schemas are represented by Content Fragment Models, which define the content structure.
  * This API is GraphQL based.
* [Content Fragments and Content Fragment Models OpenAPIs](/help/headless/content-fragment-openapis.md)
  * These APIs are intended for structured content management. 
  * Respective GET operators are not optimized for content delivery.
  * This API is REST based. 
* [Content Fragments Support in the AEM Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md)
  * The original API for the JSON output for structured content delivery in AEM.  
    * While robust and proven, this API does not deliver *fully hydrated* JSON output. References are only output as paths, requiring secondary API requests for retrieving further content.
  * The Assets HTTP API can also be used for managing the Content Fragments and Content Fragment Models (CRUD).
  * This API is REST based.
  * Content Fragment Support in Assets HTTP API will be deprecated in the future as it is being succeeded by the Edge Delivery Services JSON REST API. The timescale has not been decided yet.

<!--
## JSON vs HTML {#json-vs-HTML}

The content delivery format used is driven by frontend implementation. Unstructured content/HTML for full-stack implementations, structured content/JSON for headless implementations, or a combination of both in hybrid implementations. 

Key considerations include:

* Definition
  * JSON (JavaScript Object Notation) - used to represent, access and process structured data. 
  * HTML (HyperText Markup Language) - a markup language of tags and elements in a hierarchical structure.
* Primary Purpose
  * JSON is often used for transferring structure content between the server and client app.
  * HTML is the standard markup language for creating and rendering web pages in a browser.
-->

## REST vs GraphQL {#rest-vs-graphql}

The API used is a decision for the developers - AEM supports both. 

Many comparisons are available online, but a few highlights and benefits of REST include: 

* Simplicity

  * Developers are (often) familiar with HTTP and REST. According to the [Postman State of the APIs report](https://www.postman.com/state-of-api/), a high percentage of developers use REST. 

  * With simplicity comes familiarity. With REST there are no organizational questions of who owns the queries and who owns the app, whereas these questions can arise with GraphQL. 

  * With familiarity (typically) comes a broad community and tooling landscape. Not an inherent disadvantage of GraphQL, but likely to be broader and deeper for REST. 

  * The simpler approach can also make the security implementation easier. With REST, the filtering to determine the content to render all happens in the client app. With GraphQL this happens in a schema-based query between client and server. 

* Flexibility

  * With REST, the developer can `GET` any resource. With GraphQL they are limited to resources defined within a schema. 

* Caching

  * JSON responses to REST `GET` requests are inherently cacheable. GraphQL `POST` requests are not cacheable, unless they are made so; for example, by using AEM Persisted Queries that are stored on the server and requested with REST-like `GET`requests. 

Benefits of GraphQL include:

* Efficiency of content delivery 

  * Focus

    * With GraphQL client applications can request the exact content that they need for rendering - and no more. This approach prevents content over-delivery, with excessive content payloads, and unnecessary bandwidth consumption.

  * Single endpoint
  
    * While in REST every API request is an endpoint, in GraphQL there is only one common endpoint, and different content requests are expressed as queries using that common endpoint. 

* Rapid Prototyping

  * With GraphQL this is a one-step process, brought together in the GraphQL query, and can make prototyping easier. REST on the other hand is a 2-step process:

    1. Fetch content with API.
    2. In the JSON response, determine what to use for rendering in the client app.
