---
title: Verifying Domain
description: Verifying Domain
---

# Verifying Domain {#verify-domain-name}

A DNS TXT record authorizes a Domain to be hosted in a CDN service. The customer must create a DNS TXT record in the zone that authorizes Cloud Manager to deploy the CDN Service with the custom domain and associate it with the backend service. This association is entirely under the control of the customer and strongly authorizes Cloud Manager to serve content from the service to a domain. That authorization may be granted as well as withdrawn. The TXT record is specific to the Domain and the Cloud Manager environment.

1. Login to your Domain Host and visit the DNS records section. 
1. Copy and paste the TXT entry in your DNS zone where your custom domain is located, exactly as it appears. If you need a “name” for your entry, give it `@`.

>[!NOTE]
>Various DNS lookup tools such as [DNS Lookup Tool](https://www.ultratools.com/tools/dnsLookup), Google DoH can be used to lookup TXT record entries and identify if the TXT record is missing or erroneous.
