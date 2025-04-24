---
title: AEM Content Fragment Delivery with OpenAPI
description: Learn about tAEM Content Fragment Delivery with OpenAPI
feature: Headless, Content Fragments, Edge Delivery Services
role: Admin, Developer
exl-id: b298db37-1033-4849-bc12-7db29fb77777
---
# AEM Content Fragment Delivery with OpenAPI {#aem-content-fragment-delivery-with-openapi}

In Adobe Experience Manager (AEM) as a Cloud Service, the AEM OpenAPI for Content Fragment Delivery:

* is a HTTP REST API on [AEM Edge Delivery Services](/help/edge/overview.md), designed to deliver structured content from Content Fragments in JSON format
* offers a modern CDN integration that allows active content invalidation 
* focuses on content delivery (performance, scalability, CDN integration, optimized JSON control and output) 
* includes the ability to hydrate JSON for referenced fragments and assets

This API:

* is the successor to [Content Fragments Support in the AEM Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md)

* supplements the [Content Fragments and Content Fragment Models OpenAPIs](/help/headless/content-fragment-openapis.md), that allow you to manage the Content Fragments and Content Fragment Models (CRUD)

* is a HTTP REST alternative to the [AEM GraphQL API for use with Content Fragments](/help/headless/graphql-api/content-fragments.md) 

For full documentation see [AEM Content Fragment Delivery with OpenAPI](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/contentfragments/delivery/). 

>[!NOTE]
>
>See [AEM APIs for Structured Content Delivery and Management](/help/headless/apis-headless-and-content-fragments.md) for an overview of the various APIs available and comparison of some of the concepts involved.

## Caching {#caching}

AEM integrates with the AEM CDN Fastly. This means that JSON responses served on the publish tier are cached at the Fastly level.

Responses are then cached, based on predefined caching headers (cannot be configured):

* Responses are cached for 5 minutes in the browser/client cache
  * `max-age`=`300`
* Responses are cached for 1 hour on the CDN cache
  * `s-maxage`=`3600`
* Stale content can be served while revalidating new requests for up to 1 hour 
  * `stale-while-revalidate`=`3600`
* Stale content can be served, by error, for up to 1 day 
  * `stale-on-error`=`86400`

AEM also comes with active CDN cache invalidation. This means that whenever content is updated, or published, the corresponding JSON OpenAPI responses are automatically invalidated, via a soft purge request to Fastly. This allows you to see changes reflected in the JSON output, before the actual CDN cache age (`s-maxage`) is reached.
