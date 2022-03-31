---
title: Adding a TXT Record
description: Learn how to add TXT record to add a custom domain name in Cloud Manager.
exl-id: d441de29-af41-4d3e-9155-531af9702841
---
# Adding a TXT Record {#adding-txt}

A DNS TXT record authorizes a domain to be hosted in a CDN service. You must create a DNS TXT record in the zone that authorizes Cloud Manager to deploy the CDN Service with the custom domain and associate it with the backend service. This association is entirely under your control and authorizes Cloud Manager to serve content from the service to a domain. This authorization may be granted as well as withdrawn. The TXT record is specific to the Domain and the Cloud Manager environment.

You must fulfill these requirements before adding a TXT record.

* You must have the ability to modify the DNS records for your organization's domain, or contact the appropriate person who can.
* You must identify your domain host or registrar if you do not know it already.

When you initiate domain verification, Cloud Manager gives you the name and TXT value to use for verification. Add a TXT record to your domain's DNS server using the specified name and value.

1. Login to your domain host and find the DNS records section. 
1. Add `_aemverification.[yourdomainname]` as the **Name** value, and add the TXT value exactly as it appears.

Refer to the examples in this table.

|Domain|Name|TXT Value|
|--- |--- |---|
|`example.com`|`_aemverification.example.com` |Copy the entire value displayed in Cloud Manager UI. This is specific to the domain and the environment. For example:<br>`adobe-aem-verification=example.com/[program]/[env]/..*`|
|`www.example.com`|`_aemverification.www.example.com` |Copy the entire value displayed in Cloud Manager UI. This is specific to the domain and the environment. For example:<br>`adobe-aem-verification=www.example.com/[program]/[env]/..*`|

When you are done you can verify the result by running the following command

```shell
dig _aemverification.[yourdomainname] -t txt
```

The expected result should display the TXT value provided in Cloud Manager UI.

For example, if your domain is `example.com`, then run:

```shell
dig TXT _aemverification.example.com -t txt
```

>[!TIP]
>
>There are a number of [DNS lookup tools](https://www.ultratools.com/tools/dnsLookup) available. Google DoH can be used to lookup TXT record entries and identify if the TXT record is missing or erroneous.
