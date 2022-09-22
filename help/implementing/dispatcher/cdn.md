---
title: CDN in AEM as a Cloud Service
description: CDN in AEM as a Cloud Service
feature: Dispatcher
exl-id: a3f66d99-1b9a-4f74-90e5-2cad50dc345a
---
# CDN in AEM as a Cloud Service {#cdn}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_cdn"
>title="CDN in AEM as a Cloud Service"
>abstract="AEM as Cloud Service is shipped with a built-in CDN. It’s main purpose is to reduce latency by delivering cacheable content from the CDN nodes at the edge, near the browser. It is fully managed and configured for optimal performance of AEM applications."

AEM as Cloud Service is shipped with a built-in CDN. Its main purpose is to reduce latency by delivering cacheable content from the CDN nodes at the edge, near the browser. It is fully managed and configured for optimal performance of AEM applications.

The AEM managed CDN will satisfy most customer's performance and security requirements. For the publish tier, customers can optionally point to it from their own CDN, which they will need to manage. This will be allowed on a case-by-case basis, based on meeting certain pre-requisites including, but not limited to, the customer having a legacy integration with their CDN vendor that is difficult to abandon.

Also, see the following videos [Cloud 5 AEM CDN Part 1](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-5/cloud5-aem-cdn-part1.html) and [Cloud 5 AEM CDN Part 2](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-5/cloud5-aem-cdn-part2.html) for additional information about CDN in AEM as a Cloud Service.

## AEM Managed CDN  {#aem-managed-cdn}

Follow the sections below to use Cloud Manager self-service UI to prepare for content delivery by using AEM’s out-of-the-box CDN:

1. [Managing SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md)
1. [Managing Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/introduction.md)

**Restricting traffic**

By default, for an AEM managed CDN setup, all public traffic can make its way to the publish service, for both production and non-production (development and stage) environments. If you wish to limit traffic to the publish service for a given environment (for example, limiting staging by a range of IP addresses) you can do this in a self-service way via Cloud Manager UI.

Refer to [Managing IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/introduction.md) to learn more.

>[!CAUTION]
>
>Only requests from the allowed IPs will be served by AEM’s managed CDN. If you point your own CDN to the AEM managed CDN, then make sure the IPs of your CDN are included in the allowlist.

## Customer CDN points to AEM Managed CDN {#point-to-point-CDN}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_byocdn"
>title="Customer CDN points to AEM Managed CDN"
>abstract="AEM as Cloud Service offers an option for customers to use its existing CDN. For the publish tier, customers can optionally point to it from their own CDN, which they will need to manage. This will be allowed on a case-by-case basis, based on meeting certain pre-requisites including, but not limited to, the customer having a legacy integration with their CDN vendor that is difficult to abandon."

If a customer must use its existing CDN, they may manage it and point it to the AEM managed CDN, providing the following are satisfied:

* Customer must have an existing CDN that would be onerous to replace.
* Customer must manage it.
* Customer must be able to configure the CDN to work with AEM as a Cloud Service - see the configuration instructions presented below.
* Customer must have engineering CDN experts that are on call in case related issues arise.
* Customer must perform and successfully pass a load test before going to production.

>[!NOTE]
>
>The Adobe CDN is not optional. Customers bringing their own CDN must point it to the AEM Managed CDN.

Configuration instructions:

1. Point your CDN to the Adobe CDN’s ingress as its origin domain. For example, `publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com`.
1. SNI must also be set to the Adobe CDN's ingress.
1. Set the Host header to the origin domain. For example: `Host:publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com`.
1. Set the `X-Forwarded-Host` header with the domain name so AEM can determine the host header. For example: `X-Forwarded-Host:example.com`.
1. Set `X-AEM-Edge-Key`. The value should come from Adobe.

   * This is needed so that the Adobe CDN can validate the source of the requests and pass the `X-Forwarded-*` headers to the AEM application. For example,`X-Forwarded-For` is used to determine the client IP. So, it becomes the responsibility of the trusted caller (i.e. the customer-managed CDN) to ensure the correctness of the `X-Forwarded-*` headers (see the note below).
   * Optionally, access to Adobe CDN's ingress can be blocked when an `X-AEM-Edge-Key` is not present. Please inform Adobe if you need direct access to Adobe CDN's ingress (to be blocked).

See the [Sample CDN vendor configurations](#sample-configurations) section for configuration examples from leading CDN vendors.

Before accepting live traffic, you should validate with Adobe's customer support that the end-to-end traffic routing is functioning correctly.

After obtaining the `X-AEM-Edge-Key`, you can test that the request is routed correctly as follows.

In Linux:

```
curl https://publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com -H "X-Forwarded-Host: example.com" -H "X-AEM-Edge-Key: <PROVIDED_EDGE_KEY>"

```

In Windows:

```
curl https://publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com --header "X-Forwarded-Host: example.com" --header "X-AEM-Edge-Key: <PROVIDED_EDGE_KEY>"

```

Please note that when using your own CDN, there is no need to install the domains and certificates in Cloud Manager. The routing in Adobe CDN will be done using the default domain `publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com`.

>[!NOTE]
>
>Customers that manage their own CDN should ensure the integrity of the headers that are sent through to AEM's CDN. For instance, it is recommended that customers clear all `X-Forwarded-*` headers and set them to known and controlled values. For example, `X-Forwarded-For` should contain the client's IP address, while `X-Forwarded-Host` should contain the site's host.

>[!NOTE]
>
>Sandbox program environments do not support a customer-provided CDN.

The extra hop between the customer CDN and the AEM CDN is only needed in the event of a cache miss. By using the cache optimization strategies described in this article, the addition of a customer CDN should only introduce negligible latency.

Please note that this customer CDN configuration is supported for the publish tier, but not in front of the author tier.

### Sample CDN vendor configurations {#sample-configurations}

Presented below are several configuration examples from a number of leading CDN vendors.

**Akamai**

![Akamai1](assets/akamai1.png "Akamai")
![Akamai2](assets/akamai2.png "Akamai")

**Amazon CloudFront**

![CloudFront1](assets/cloudfront1.png "Amazon CloudFront")
![CloudFront2](assets/cloudfront2.png "Amazon CloudFront")

**Cloudflare**

![Cloudflare1](assets/cloudflare1.png "Cloudflare")
![Cloudflare2](assets/cloudflare2.png "Cloudflare")

## Geolocation Headers {#geo-headers}

The AEM managed CDN adds headers to each request with:

* country code: `x-aem-client-country`
* continent code: `x-aem-client-continent`

>[!NOTE]
>
>In case of customer managed CDN these headers will reflect the location of the customers CDN proxy server rather than the actual client.  Therefore, for customer managed CDN, geolocation headers should be managed by the customers CDN.  

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
