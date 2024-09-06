---
title: Adding a TXT Record
description: Learn how to add TXT record to verify your ownership of a custom domain for use with Cloud Manager.
exl-id: d441de29-af41-4d3e-9155-531af9702841
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Adding a TXT Record {#adding-txt}

Learn how to add TXT record to verify your ownership of a custom domain for use with Cloud Manager.

## What is a TXT record? {#what-is}

A text record (also known as a TXT record) is a type of resource record in the Domain Name System (DNS). It provides the ability to associate arbitrary text with a host name, such as human-readable information about a hostname such as server or network information.

Cloud Manager uses a specific TXT record to authorize a domain to be hosted in a CDN service. You must create a DNS TXT record in the zone that authorizes Cloud Manager to deploy the CDN service with the custom domain and associate it with the backend service. This association is entirely under your control and authorizes Cloud Manager to serve content from the service to a domain. This authorization may be granted and withdrawn. The TXT record is specific to the domain and the Cloud Manager environment.

## Requirements {#requirements}

You must fulfill these requirements before adding a TXT record.

* You must identify your domain host or registrar if you do not know it already.
* You must be able to edit the DNS records for your organization's domain, or contact the appropriate person who can.
* You must first add a custom domain name as described in the document [Adding a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).

## Adding a TXT Record for Verification {#verification}

A TXT record is added as part of the verification of a custom domain name to be used with Cloud Manager. 

1. You must first add a custom domain name as described in the document [Adding a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).

1. When on the **Verification** tab of the **Add Domain Name** dialog, Cloud Manager displays the name and TXT value to use for verification. Copy this value.

   ![Domain name verification](/help/implementing/cloud-manager/assets/cdn/cdn-create6.png)

1. Log in to your domain host and find the DNS records section. 

1. Add `_aemverification.[yourdomainname]` as the **Name** of the value and add the TXT value exactly as it appears in the **Add Domain Name** dialog.

   * See the [examples in the following section](#examples).

1. Save the TXT record to your domain host.

## TXT Record Examples {#examples}

|Domain|Name|TXT Value|
|--- |--- |---|
|`example.com`|`_aemverification.example.com` |Copy the entire value displayed in Cloud Manager UI. This is specific to the domain and the environment. For example:<br>`adobe-aem-verification=example.com/[program]/[env]/..*`|
|`www.example.com`|`_aemverification.www.example.com` |Copy the entire value displayed in Cloud Manager UI. This is specific to the domain and the environment. For example:<br>`adobe-aem-verification=www.example.com/[program]/[env]/..*`|

## Verify TXT Record {#verify}

When you are done you can verify the result by running the following command.

```shell
dig _aemverification.[yourdomainname] -t txt
```

The expected result should display the TXT value provided on the **Verification** tab of the **Add Domain Name** dialog of the Cloud Manager UI.

For example, if your domain is `example.com`, then run:

```shell
dig TXT _aemverification.example.com -t txt
```

>[!TIP]
>
>There are several [DNS lookup tools](https://www.ultratools.com/tools/dnsLookup) available. Google DoH can be used to lookup TXT record entries and identify if the TXT record is missing or erroneous.

>[!NOTE]
>
>DNS verification can take a few hours to process because of DNS propagation delays.
>
>Cloud Manager will verify ownership and update the status which can be seen in the Domain Settings Table. See [Checking Custom Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) for more details.

## Next Steps {#next-steps}

Now that you created your TXT entry, you can verify your domain name status. Proceed to the document [Checking Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) to continue setting up your custom domain name.

>[!TIP]
>
>The TXT entry and the CNAME or A Record can be set simultaneously on the governing DNS Server, thus saving time.
>
>If you wish to do this, first review the entire process of setting up a custom domain name as detailed in the document [Introduction to Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/introduction.md) taking special note of the document [help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md) and update your DNS settings appropriately.