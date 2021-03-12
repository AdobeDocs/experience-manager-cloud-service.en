---
title: CDN in AEM as a Cloud Service
description: CDN in AEM as a Cloud Service
---

# CDN in AEM as a Cloud Service {#cdn}

AEM as Cloud Service is shipped with a built-in CDN. It’s main purpose is to reduce latency by delivering cacheable content from the CDN nodes at the edge, near the browser. It is fully managed and configured for optimal performance of AEM applications.

The AEM managed CDN will satisfy most customer's performance and security requirements. For the publish tier, customers can optionally point to it from their own CDN, which they will need to manage. This will be allowed on a case-by-case basis, based on meeting certain pre-requisites including, but not limited to, the customer having a legacy integration with their CDN vendor that is difficult to abandon.

## AEM Managed CDN  {#aem-managed-cdn}

Follow the sections below to use Cloud Manager self-service UI to prepare for content delivery by using AEM’s out-of-the-box CDN:

1. [Managing SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md)
1. [Managing Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/introduction.md)

**Restricting traffic**

By default, for an AEM managed CDN setup, all public traffic can make its way to the publish service, for both production and non-production (development and stage) environments. If you wish to limit traffic to the publish service for a given environment (for example, limiting staging by a range of IP addresses) you can do this in a self-service way via Cloud Manager UI.

Refer to [Managing IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/introduction.md) to learn more.

>[!CAUTION]
>
>Only requests from the allowed IPs will be served by AEM’s managed CDN. If you point your own CDN to the AEM managed CDN then make sure the IPs of your CDN are included in the allowlist.

## Customer CDN points to AEM Managed CDN {#point-to-point-CDN}

If a customer must use its existing CDN, they may manage it and point it to the AEM managed CDN, providing the following are satisfied:

* Customer must have an existing CDN that would be onerous to replace.
* Customer must manage it.
* Customer must be able to configure the CDN to work with AEM as a Cloud Service - see the configuration instructions below.
* Customer must have engineering CDN experts that are on call in case related issues arise.
* Customer must perform and successfully pass a load test before going to production.

Configuration instructions:

1. Set the `X-Forwarded-Host` header with the domain name.
1. Set Host header with the origin domain, which is the AEM CDN's ingress. The value should come from Adobe.
1. Send the SNI header to the origin. Like the Host header, the sni header must be the origin domain.
1. Set either the `X-Edge-Key` or the `X-AEM-Edge-Key` (if your CDN strips X-Edge-*), which is needed to route traffic correctly to the AEM servers. The value should come from Adobe. Please inform Adobe if you want direct access to Adobe CDN's ingress (to be blocked when `X-Edge-Key` is not present).

Prior to accepting live traffic, you should validate with Adobe customer support that the end-to-end traffic routing is functioning correctly.

>[!NOTE]
>
>Customers that manage their own CDN should ensure the integrity of the headers that are sent through to AEM's CDN. For instance, it is recommended that customers clear all `X-Forwarded-*` headers and set them to known and controlled values. For example, `X-Forwarded-For` should contain the client's IP address, while `X-Forwarded-Host` should contain the site's host.

There is potentially a small performance hit due to the extra hop, although hops from the customer CDN to the AEM managed CDN are likely to be efficient.

Note that this customer CDN configuration is supported for the publish tier, but not in front of the author tier.

## Geolocation Headers {#geo-headers}

The AEM managed CDN will add headers to each request with:

* country code: `x-aem-client-country`
* continent code: `x-aem-client-continent`

The values for the country codes are the Alpha-2 codes described [here](https://en.wikipedia.org/wiki/ISO_3166-1).

The values for the continent codes are:

* AF Africa
* AN Antarctica
* AS Asia
* EU Europe
* NA North America
* OC Oceania
* SA South America

This information may be useful for use cases such as redirecting to a different url based on the origin (country) of the request. Use the Vary header for caching responses that are dependent on geo information. For example, redirects to a specific country landing page should always contain `Vary: x-aem-client-country`. If needed, you can use `Cache-Control: private` to prevent caching. See also [Caching](/help/implementing/dispatcher/caching.md#html-text).
