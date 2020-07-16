---
title: CDN in AEM as a Cloud Service
description: CDN in AEM as a Cloud Service
---

# CDN in AEM as a Cloud Service {#cdn}

AEM as Cloud Service is shipped with a built-in CDN. It’s main purpose is to reduce latency by delivering cacheable content from the CDN nodes at the edge, near the browser. It is fully managed and configured for optimal performance of AEM applications.

The AEM managed CDN will satisfy most customer's performance and security requirements. Customers can optionally point to it from their own CDN, which they will need to manage. This will be allowed on a case-by-case basis, based on meeting certain pre-requisites including, but not limited to, the customer having a legacy integration with their CDN vendor that is difficult to abandon.

## AEM Managed CDN  {#aem-managed-cdn}

Follow these to prepare for content delivery by using Adobe's out-of-the-box CDN:

1. Provide the signed SSL certificate and secret key to Adobe by sharing a link to a secure form containing this information. Please coordinate with customer support on this task.
**Note:** Aem as a Cloud Service does not support Domain Validated (DV) certificates.
1. Inform customer support:
   * which custom domain should be associated with a given environment, as defined by the program id and environment id. Note that custom domains on the author side are not supported.
   * if any IP allowlisting is needed to restrict traffic to a given environment.
1. Coordinate with customer support about timing of the necessary changes to the DNS records. The instructions are different based on whether an apex record is needed:
   * if an apex record is not needed, customers should set the CNAME DNS record to point their FQDN to `cdn.adobeaemcloud.com`.
   * if an apex record is needed, create an A record pointing to the following IPs: 151.101.3.10, 151.101.67.10, 151.101.131.10, 151.101.195.10. Customers need an apex record if the desired FQDN matches the DNS Zone. This can be tested by using the Unix dig command to see if the SOA value of the output matches the domain. For example, the command `dig anything.dev.adobeaemcloud.com` returns a SOA (Start of Authority, i.e., the zone) of `dev.adobeaemcloud.com` so its not an APEX record, while `dig dev.adobeaemcloud.com` returns a SOA of `dev.adobeaemcloud.com` so it is an apex record.
1. You will be notified when the SSL certificates are expiring so you can resubmit the new SSL certificates.

**Restricting traffic**

By default, for an Adobe Managed CDN setup, all public traffic can make its way to the publish service, for both production and non-production (development and stage) environments. If you wish to limit traffic to the publish service for a given environment (for example, limiting staging by a range of IP addresses) you should work with customer support to configure these restrictions. 

## Customer CDN points to AEM Managed CDN {#point-to-point-CDN}

If a customer must use its existing CDN, they may manage it and point it to Adobe's managed CDN, providing the following are satisfied:

* Customer must have an existing CDN that would be onerous to replace.
* Customer must manage it.
* Customer must be able to configure the CDN to work with AEM as a Cloud Service - see the configuration instructions below.
* Customer must have engineering CDN experts that are on call in case related issues arise.
* Customer must perform and successfully pass a load test before going to production.

Configuration instructions:

1. Set the `X-Forwarded-Host` header with the domain name.
1. Set Host header with the origin domain, which is Adobe's CDN's ingress. The value should come from Adobe.
1. Send the SNI header to the origin. Like the Host header, the sni header must be the origin domain.
1. Set the `X-Edge-Key`, which is needed to route traffic correctly to the AEM servers. The value should come from Adobe.

Prior to accepting live traffic, you should validate with Adobe customer support that the end-to-end traffic routing is functioning correctly.

Note that there is potentially a small performance hit due to the extra hop, although hops from the customer CDN to Adobe's managed CDN are likely to be efficient.
