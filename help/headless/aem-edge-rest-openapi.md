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

<!-- Question -->
<!-- is it equivalent to the CF and CFM OpenAPI? -->
<!-- Thought that was for internal management of CFs/CFMs -->
<!-- now with focus on content delivery (performance, scalability, CDN integration, optimized JSON control and output)  -->

* is the successor to [Content Fragments Support in the AEM Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md)

<!--
* is equivalent to the [Content Fragments and Content Fragment Models OpenAPIs](/help/headless/content-fragment-openapis.md)
-->

* is a HTTP REST alternative to the [AEM GraphQL API for use with Content Fragments](/help/headless/graphql-api/content-fragments.md) 

## Authentication {#authentication}

<!-- Question -->
<!-- which API is meant by the CF Management API? 
<!-- The Content Fragments and Content Fragment Models OpenAPIs?-->
<!-- Though the existing documentation is for the GraphQL API; see: -->
<!-- https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/security/authentication -->

Requests made on the author tier must be authenticated, similar to any other request to the Content Fragment Management API. This means that an access token must be provided as part of the Authorization header of the HTTP request. 

The concept is the same as for [AEM GraphQL authenticated queries](/help/headless/security/authentication.md).

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