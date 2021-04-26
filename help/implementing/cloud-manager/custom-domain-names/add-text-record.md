---
title: Adding a TXT Record
description: Adding a Custom Domain Name
exl-id: d441de29-af41-4d3e-9155-531af9702841
---
# Adding a TXT Record {#adding-txt}

A DNS TXT record authorizes a Domain to be hosted in a CDN service. The customer must create a DNS TXT record in the zone that authorizes Cloud Manager to deploy the CDN Service with the custom domain and associate it with the backend service. This association is entirely under the control of the customer and strongly authorizes Cloud Manager to serve content from the service to a domain. That authorization may be granted as well as withdrawn. 

You myst follow the steps below before you create a TXT record:

* Have the ability to modify the DNS records for your organization's domain, or contact the appropriate person who can.
* Identify your domain host or registrar if you do not know it already.

When you initiate domain verification, Cloud Manager gives you the name and TXT value to use for verification. Add a TXT record to your domain's DNS server using the specified Name and Value.

1. Login to your Domain Host and visit the DNS records section. 
1. Add `_aemverification.[yourdomainname]` as the Name, and add the TXT Value exactly as it appears. 
   Refer to the examples in the table below.

|Domain|Name|TXT Value|
|--- |--- |---|
|`example.com`|`_aemverification.example.com`|Displayed in Cloud Manager UI and is specific to the domain and the Cloud Manager environment|
|`test.example.com`|`_aemverification.test.example.com`|Displayed in Cloud Manager UI and is specific to the domain and the Cloud Manager environment|

When you are done you can verify the result by running: `dig _aemverification.[yourdomainname] -t txt`.
The expected result should display the TXT value provided in Cloud Manager UI.

For example, if your domain is `example.com`, then run: `dig TXT _aemverification.example.com -t txt`.

>[!NOTE]
>There are also various [DNS lookup tools](https://www.ultratools.com/tools/dnsLookup), Google DoH can be used to lookup TXT record entries and identify if the TXT record is missing or erroneous.
