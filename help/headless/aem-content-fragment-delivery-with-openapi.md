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

<!-- CQDOC-22720 -->

>[!IMPORTANT]
>
>To enable Content Fragment Delivery with OpenAPI on AEM as a Cloud Service you should ensure that it is not already enabled, then submit an Adobe Support ticket with the title **Enable Content Fragment Delivery with OpenAPI** and specifying:
>* the Cloud Service program and environment ID
>* details of the use-case you want to solve with the Content Fragment Delivery OpenAPI
>* the customer contacts who will be involved in the integration project
>* details of the [HTTP allowed origins](#cors) that will trigger requests to the Content Fragment Delivery API 

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

## Availability {#availability}

The Content Fragment Delivery with OpenAPI is available on Preview and Publish tiers. The OpenAPI delivers Content Fragments in JSON for delivery purposes, for both previewing and live delivery use-cases.

To simulate delivery of content from the AEM author directly, the Content Fragment Delivery with OpenAPI can be configured to enable auto-synchronizing of Content Fragments from the AEM author environment to the Preview tier. 

>[!NOTE]
>
>The auto-synchronizing from AEM Author to Preview is turned off by default. Contact your Support representative if you want it to be enabled.
>
>Whenever the auto-sync capability is enabled, we recommend making sure that [proper IP allowlisting rules are in place to protect content on the Preview tier](/help/sites-cloud/authoring/sites-console/previewing-content.md).

When auto-syncing is not enabled the Content Fragment authors:

* have control over how and when Content Fragments are available on the Preview service
* rely on the Publish to Preview operation to manually synchronize Content Fragments to be previewed.

## CORS {#cors}

<!-- CQDOC-22720 -->

<!--
[CORS allowed origins](/help/headless/deployment/cross-origin-resource-sharing.md) allow customers to define the origins that can call the API. The origins are defined in AEM as an OSGi configuration.
-->

[CORS allowed origins](/help/headless/deployment/cross-origin-resource-sharing.md) define the origins that can call the API. Allowed origins are managed manually by Adobe, but need information from the customer. For this, Adobe requires customers to share the allowed origins that must be configured. This information should be provided as part of the initial request (Adobe Support ticket) to enable the API.

The CORS allowed origins defined on the dispatcher configuration side, specifically for GraphQL, are not taken into consideration by this API.

<!-- 
## API Rate Limits {#api-rate-limits}
-->

<!-- 
## Limitations {#limitations}
-->
