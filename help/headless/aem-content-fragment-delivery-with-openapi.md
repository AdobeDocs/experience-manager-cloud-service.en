---
title: AEM Content Fragment Delivery with OpenAPI
description: Learn about tAEM Content Fragment Delivery with OpenAPI
feature: Headless, Content Fragments, Edge Delivery Services
role: Admin, Developer
exl-id: b298db37-1033-4849-bc12-7db29fb77777
---

# AEM Content Fragment Delivery with OpenAPI {#aem-content-fragment-delivery-with-openapi}

In Adobe Experience Manager (AEM) as a Cloud Service, the AEM OpenAPI for Content Fragment Delivery:

* is an OpenAPI that is optimized for live delivery of AEM Content Fragments in JSON format
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

>[!IMPORTANT]
>
>To enable Content Fragment Delivery with OpenAPI on AEM as a Cloud Service please ensure that it is not already enabled, then submit an Adobe Support ticket with the title **Enable Content Fragment Delivery with OpenAPI** and specifying:
>
>* the Cloud Service program and environment ID(s)
>* details of the use-case you want to solve with the Content Fragment Delivery OpenAPI
>* details of all your contacts that Adobe should respond to, and keep informed about the request, and project (if required)

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

Content Fragment Delivery with OpenAPI supports active CDN cache invalidation. This means that whenever content is updated, or published, the corresponding JSON OpenAPI responses are automatically invalidated, via a soft purge request to Fastly. This allows you to see changes reflected in the JSON output, before the actual CDN cache age (`s-maxage`) is reached.

## Availability {#availability}

The Content Fragment Delivery with OpenAPI is available on Preview and Publish tiers. The OpenAPI delivers Content Fragments in JSON format, for both preview and live delivery.

For preview the Content Fragment Delivery with OpenAPI can:

* publish to Preview
* enable access to preview with IP allow list
* get the preview URL

## CORS {#cors}

[CORS allowed origins](/help/headless/deployment/cross-origin-resource-sharing.md) define the origins that can call the API. 

The CORS allowed origins defined on the dispatcher configuration side, specifically for GraphQL, are not taken into consideration by this API.

## API Rate Limits {#api-rate-limits}

The API allows new requests at a rate of up to 200 requests per second, per environment. 

Once this limit is exceeded, the API starts sending [429 error](https://www.rfc-editor.org/rfc/rfc6585#section-4) responses. These errors must be handled by any client applications, and failed requests retried following an exponential backoff retry. The HTTP response comes with a specific header, `Retry-After`, that indicates to the client how long they need to wait before before sending the request again.

<!-- 
## Limitations {#limitations}
-->
