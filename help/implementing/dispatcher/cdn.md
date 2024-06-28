---
title: CDN in AEM as a Cloud Service
description: Learn how to use the AEM-managed CDN and how to point your own CDN to the AEM-managed CDN.
feature: Dispatcher
exl-id: a3f66d99-1b9a-4f74-90e5-2cad50dc345a
---
# CDN in AEM as a Cloud Service {#cdn}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_cdn"
>title="CDN in AEM as a Cloud Service"
>abstract="AEM as Cloud Service is shipped with a built-in CDN. Its main purpose is to reduce latency by delivering cacheable content from the CDN nodes at the edge, near the browser. It is fully managed and configured for optimal performance of AEM applications."

AEM as Cloud Service is shipped with a built-in CDN. Its main purpose is to reduce latency by delivering cacheable content from the CDN nodes at the edge, near the browser. It is fully managed and configured for optimal performance of AEM applications.

The AEM-managed CDN satisfies most customer's performance and security requirements. For the publish tier, customers can optionally point to it from their own CDN, which they must manage. This scenario is allowed on a case-by-case basis, based on meeting certain pre-requisites including, but not limited to, the customer having a legacy integration with their CDN vendor that is difficult to abandon.

<!-- ERROR: NEITHER URL IS FOUND (HTTP ERROR 404) Also, see the following videos [Cloud 5 AEM CDN Part 1](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-5/cloud5-aem-cdn-part1.html) and [Cloud 5 AEM CDN Part 2](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-5/cloud5-aem-cdn-part2.html) for additional information about CDN in AEM as a Cloud Service. -->

## AEM-managed CDN  {#aem-managed-cdn}

Follow the sections below to use Cloud Manager self-service UI to prepare for content delivery by using AEM's out-of-the-box CDN:

1. [Managing SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md)
1. [Managing Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/introduction.md)

**Restricting traffic**

By default, for an AEM-managed CDN setup, all public traffic can make its way to the publish service, for both production and non-production (development and stage) environments. You can limit traffic to the publish service for a given environment (for example, limiting staging by a range of IP addresses) by way of the Cloud Manager user interface.

See [Managing IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/introduction.md) to learn more.

>[!CAUTION]
>
>Only requests from the allowed IPs are served by AEM's managed CDN. If you point your own CDN to the AEM-managed CDN, then make sure the IPs of your CDN are included in the allowlist.

### Configuring Traffic at the CDN {#cdn-configuring-cloud}

Rules to configure CDN traffic and filters can be declared in a configuration file and deployed to the CDN, by using the [Cloud Manager's Configuration Pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#config-deployment-pipeline). For more details, see [Configuring Traffic at the CDN](/help/implementing/dispatcher/cdn-configuring-traffic.md) and [Traffic Filter rules including WAF rules](/help/security/traffic-filter-rules-including-waf.md).

### Configuring CDN Error Pages {#cdn-error-pages}

A CDN error page can be configured to override the default, unbranded page that is served to the browser in the rare event that AEM cannot be reached. For more details, see [Configuring CDN error pages](/help/implementing/dispatcher/cdn-error-pages.md).

## Customer CDN points to AEM-managed CDN {#point-to-point-CDN}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_byocdn"
>title="Customer CDN points to AEM Managed CDN"
>abstract="AEM as Cloud Service offers an option for customers to use its existing CDN. For the publish tier, customers can optionally point to it from their own CDN, which they must manage. This scenario is allowed on a case-by-case basis, based on meeting certain pre-requisites including, but not limited to, the customer having a legacy integration with their CDN vendor that is difficult to abandon."

If a customer must use its existing CDN, they may manage it and point it to the AEM-managed CDN, providing the following are satisfied:

* Customer must have an existing CDN that would be onerous to replace.
* Customer must manage it.
* Customer must be able to configure the CDN to work with AEM as a Cloud Service - see the configuration instructions presented below.
* Customer must have engineering CDN experts that are on call in case-related issues arise.
* Customer must perform and successfully pass a load test before going to production.

Configuration instructions:

1. Point your CDN to the Adobe CDN's ingress as its origin domain. For example, `publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com`.
1. Set SNI to the Adobe CDN's ingress.
1. Set the Host header to the origin domain. For example: `Host:publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com`.
1. Set the `X-Forwarded-Host` header with the domain name so AEM can determine the host header. For example: `X-Forwarded-Host:example.com`.
1. Set `X-AEM-Edge-Key`. The value should come from Adobe.

   * Needed so that the Adobe CDN can validate the source of the requests and pass the `X-Forwarded-*` headers to the AEM application. For example,`X-Forwarded-For` is used to determine the client IP. So, it becomes the responsibility of the trusted caller (that is, the customer-managed CDN) to ensure the correctness of the `X-Forwarded-*` headers (see the note below).
   * Optionally, access to Adobe CDN's ingress can be blocked when an `X-AEM-Edge-Key` is not present. Inform Adobe if you need direct access to Adobe CDN's ingress (to be blocked).

See the [Sample CDN vendor configurations](#sample-configurations) section for configuration examples from leading CDN vendors.

Before accepting live traffic, you should validate with Adobe's customer support that the end-to-end traffic routing is functioning correctly.

After obtaining the `X-AEM-Edge-Key`, you can test that the request is routed correctly as follows.

In Linux&reg;:

```
curl https://publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com -H "X-Forwarded-Host: example.com" -H "X-AEM-Edge-Key: <PROVIDED_EDGE_KEY>"

```

In Windows:

```
curl https://publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com --header "X-Forwarded-Host: example.com" --header "X-AEM-Edge-Key: <PROVIDED_EDGE_KEY>"

```

>[!NOTE]
>
>When using your own CDN, you do not need to install domains and certificates in Cloud Manager. The routing in the Adobe CDN is done by using the default domain `publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com` which should be sent in the request `Host` header. Overwriting the request `Host` header with a custom domain name can cause the request to be incorrectly routed by the Adobe CDN.


>[!NOTE]
>
>Customers that manage their own CDN should ensure the integrity of the headers that are sent through to AEM's CDN. For instance, it is recommended that customers clear all `X-Forwarded-*` headers and set them to known and controlled values. For example, `X-Forwarded-For` should contain the client's IP address, while `X-Forwarded-Host` should contain the site's host.

>[!NOTE]
>
>Sandbox program environments do not support a customer-provided CDN.

The extra hop between the customer CDN and the AEM CDN is only needed if there is a cache miss. By using the cache optimization strategies described in this article, the addition of a customer CDN should only introduce negligible latency.

This customer CDN configuration is supported for the publish tier, but not in front of the author tier.

### Sample CDN vendor configurations {#sample-configurations}

Presented below are several configuration examples from several leading CDN vendors.

**Akamai**

![Akamai1](assets/akamai1.png "Akamai")
![Akamai2](assets/akamai2.png "Akamai")

**Amazon CloudFront**

![CloudFront1](assets/cloudfront1.png "Amazon CloudFront")
![CloudFront2](assets/cloudfront2.png "Amazon CloudFront")

**Cloudflare**

![Cloudflare1](assets/cloudflare1.png "Cloudflare")
![Cloudflare2](assets/cloudflare2.png "Cloudflare")

### Common Errors
The sample configurations provided show the base settings needed, but a customer configuration may have other impacting rules that remove, modify, or re-arrange the headers needed for AEM as a Cloud Service to serve the traffic. Below are common errors that occur when configuring a customer managed CDN to point to AEM as a Cloud Service.

**Redirection to the Publish Service Endpoint**

When a request receives a 403 forbidden response the cause is that the request is missing some required headers. A common cause for this is when a CDN is managing both apex and www domain traffic, but is not adding the correct header for the www domain. This problem can be triaged by checking your AEM as a Cloud Service CDN logs and verifying the needed request headers. 

**Too Many Redirects Loop**

When a page gets a "Too Many Redirect" loop, some request header is being added at the CDN that matches a redirect that forces it back to itself. As an example:

1. A CDN rule is created to match either the apex domain or the www domain, and add the X-Forwarded-Host header of the apex domain only.
2. A request for an apex domain matches this CDN rule, which adds the apex domain as the X-Forwarded-Host header.
2. A request is sent to the origin where a redirect matches the host header explicitly for the apex domain (e.g, ^example.com).
3. A rewrite rule is triggered, which rewrites the request for the apex domain to https with the www subdomain.
4. That redirect is then sent to the customer's edge, where the CDN rule is re-triggered, and the process starts over until the request is blocked.

To resolve this problem, assess your SSL redirect strategy, CDN rules, and redirect and rewrite rule combinations.

## Geolocation Headers {#geo-headers}

The AEM-managed CDN adds headers to each request with:

* country code: `x-aem-client-country`
* continent code: `x-aem-client-continent`

>[!NOTE]
>
>If there is a customer-managed CDN, these headers reflect the location of the customers CDN proxy server rather than the actual client. Therefore, for customer-managed CDN, geolocation headers should be managed by the customers CDN.  

The values for the country codes are the Alpha-2 codes described [here](https://en.wikipedia.org/wiki/ISO_3166-1).

The values for the continent codes are:

* AF Africa
* AN Antarctica
* AS Asia
* EU Europe
* NA North America
* OC Oceania
* SA South America

This information may be useful for use cases such as redirecting to a different url based on the origin (country) of the request. Use the Vary header for caching responses that depend on geo information. For example, redirects to a specific country landing page should always contain `Vary: x-aem-client-country`. If needed, you can use `Cache-Control: private` to prevent caching. See also [Caching](/help/implementing/dispatcher/caching.md#html-text).
