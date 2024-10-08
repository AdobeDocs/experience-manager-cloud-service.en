---
title: Add a Custom Domain Name
description: Learn how to add a custom domain name using Domain Settings in Cloud Manager.
exl-id: 0fc427b9-560f-4f6e-ac57-32cdf09ec623
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Add a custom domain name {#adding-cdn}

Learn how to add a custom domain name using **Domain Settings** in Cloud Manager.

## Requirements {#requirements}

Fulfill these requirements before adding a custom domain name in Cloud Manager.

* You must have added a domain SSL certificate for the domain you want to add before adding a custom domain name as described in the document [Add an SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md).
* You must have the **Business Owner** or **Deployment Manager** role to add a custom domain name in Cloud Manager.
* Use the Fastly or other CDN (Content Delivery Network).

>[!IMPORTANT]
>
>Even if you use a non-Adobe CDN, you still need to add your domain to Cloud Manager.

## Where to add custom domain names {#where-to-add-cdn}

You can add a custom domain name from the following two locations in Cloud Manager:

   * [Domain Settings page](#adding-cdn-settings)
   * [Environments page](#adding-cdn-environments)

When adding a custom domain name, the domain is served using the most specific, valid certificate. If multiple certificates have the same domain, then the most recently updated is chosen. Adobe recommends that you manage certificates such that there are no overlapping domains.

The steps for either method described in this document are based on Fastly. If you used a different CDN (Content Delivery Network), configure your domain with the CDN you have chosen to use.

## Add a custom domain name {#adding-cdn-settings}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. In the side menu, under **Services**, select ![Settings icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Settings_18_N.svg) **Domain Settings**.

   ![The Domain Settings window](/help/implementing/cloud-manager/assets/cdn/cdn-create.png)

1. Near the upper-right corner of the **Domain Settings** page, click **Add Domain**.

1. In the **Add domain** dialog box, in the **Domain Name** field, enter the custom domain name you are using. 
Do not include `http://`, `https://`, or spaces when entering in your domain.

1. Click **Create**.

1. In the **Verify domain** dialog box, in the **What certificate type do you plan on using with this domain?** drop-down list, select one of the following options:

   | Certificate type option | Description |
   | --- | --- |
   | Adobe managed certificate | Select this certificate type if you want to use a DV (Domain Validation) certificate. This option is ideal for most cases, providing basic domain validation. Adobe manages and renews the certificate automatically. |
   | Customer managed certificate | Select this certificate type if you want to use an EV/OV certificate. This option offers enhanced security with EV (Extended Validation) or OV (Organization Validation). Use if stricter verification, higher trust levels, or custom control over the certificates is required. |

1. In the **Verify domain** dialog box, based on the certificate type you selected, do one of the following:

   | If you selected the certificate type | Description |
   | --- | ---  |
   | Adobe managed certificate |  Complete the [Adobe managed certificate steps](#adobe-managed-cert-steps) before continuing to step 9. |
   | Customer managed certificate | Complete the [Customer managed certificate steps](#customer-managed-cert-steps) before continuing to step 9. |

1. Click **Verify**.

1. You are now ready to [add an SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md). 

   >[!NOTE]
   >
   >If you use a customer-managed SSL certificate and a customer-managed CDN provider, you can skip adding an SSL certificate and go directly to [Add a CDN configuration](/help/implementing/cloud-manager/cdn-configurations/add-cdn-config.md) when ready.


### Adobe managed certificate steps {#adobe-managed-cert-steps}

If you selected the certificate type *Adobe managed certificate*, complete the following steps in the **Verify domain** dialog box.

![Adobe managed certificate steps](/help/implementing/cloud-manager/assets/cdn/cdn-create-adobe-dv-cert.png)

To verify the domain in use, you are required to add and verify a CNAME. 

A `CNAME` or A record, once provisioned, routes all Internet traffic for the domain to wherever it is pointing. If that location is not provisioned to serve the traffic, there is an outage. If it has not been tested, there may be errors in the content. This reason is why this step is always done after testing is complete and you are ready to go live.

To configure these settings, determine if a `CNAME` or apex record must be configured to point your custom domain name to the Cloud Manager domain name. The following sections of this document can help you determine which type of record is appropriate for your DNS configuration.

>[!NOTE]
>
>For Adobe-managed CDNs, when using DV (Domain Validation) certificates, only sites with ACME validation are permitted.

#### Requirements {#adobe-managed-cert-dv-requirements}

Fulfill these requirements before configuring your DNS records.

* Identify your domain host or registrar if you do not know it already.
* Be able to edit the DNS records for your organization's domain, or contact the appropriate person who can.
* You must have already verified your configured custom domain name as described in the document [Checking Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md).

#### CNAME record {#adobe-managed-cert-cname-record}

A canonical name or CNAME record is a type of DNS record that maps an alias name to a true or canonical domain name. CNAME records are typically used to map a subdomain such as `www.example.com` to the domain hosting that subdomain's content. 

Log in to your DNS service provider and create a `CNAME` record to point your custom domain name to the target such as in the following table.

| CNAME | Custom domain dame point to target|
| --- | --- |
| `www.customdomain.com` | `cdn.adobeaemcloud.com` |

#### APEX record {#adobe-managed-cert-apex-record}

An apex domain is a custom domain that does not contain a subdomain, such as `example.com`. An apex domain is configured with an `A`, `ALIAS`, or `ANAME` record through your DNS provider. Apex domains must point to specific IP addresses.

Add the following `A` records to your domain's DNS settings by way of your domain provider.

* `A RECORD`

* `A record for domain @ pointing to IP 151.101.3.10`

* `A record for domain @ pointing to IP 151.101.67.10`

* `A record for domain @ pointing to IP 151.101.131.10`

* `A record for domain @ pointing to IP 151.101.195.10`

>[!TIP]
>
>The *CNAME* or *A Record* can be set on the governing DNS server to save you time.


### Customer managed certificate steps {#customer-managed-cert-steps}

If you selected the certificate type *Customer managed certificate*, complete the following steps.

1. In the **Verify domain** dialog box, upload a new EV/OV certificate that covers the selected domain. 

   ![Verify domain for a customer managed EV/OV certificate](/help/implementing/cloud-manager/assets/verify-domain-customer-managed-step.png)

1. Click **OK**.

   After uploading a valid EV/OV certificate, the domain's status is marked as **Verified** in the **Domain Settings** table. 

   ![Domain Setting table showing a Verified status.](/help/implementing/cloud-manager/assets/domain-settings-verified.png)

<!--
![Customer managed certificate steps](/help/implementing/cloud-manager/assets/cdn/cdn-create-customer-cert.png)

To verify the domain in use, you are required to add and verify a TXT record.

A text record (also known as a TXT record) is a type of resource record in the Domain Name System (DNS). It lets you associate arbitrary text with a hostname. This text could include human-readable details like server or network information.

Cloud Manager uses a specific TXT record to authorize a domain to be hosted in a CDN service. Create a DNS TXT record in the zone that authorizes Cloud Manager to deploy the CDN service with the custom domain and associate it with the backend service. This association is entirely under your control and authorizes Cloud Manager to serve content from the service to a domain. This authorization may be granted and withdrawn. The TXT record is specific to the domain and the Cloud Manager environment.

#### Requirements {#customer-managed-cert-requirements}

Fulfill these requirements before adding a TXT record.

* Identify your domain host or registrar if you do not know it already.
* Be able to edit the DNS records for your organization's domain, or contact the appropriate person who can.
* First, add a custom domain name as described earlier in this article.

#### Add a TXT record for verification {#customer-managed-cert-verification}

1. In the **Verify domain** dialog box, Cloud Manager displays the name and TXT value to use for verification. Copy this value.

1. Log in to your DNS service provider and find the DNS records section. 

1. Add `aemverification.[yourdomainname]` as the **Name** of the value and add the TXT value exactly as it appears in the **Domain Name** field.

   **TXT record examples**

   | Domain | Name | TXT Value |
   | --- | --- | --- |
   | `example.com` | `_aemverification.example.com` | Copy the entire value displayed in the Cloud Manager UI. This value is specific to the domain and the environment. For example:<br>`adobe-aem-verification=example.com/[program]/[env]/..*` |
   | `www.example.com` | `_aemverification.www.example.com` | Copy the entire value displayed in the Cloud Manager UI. This value is specific to the domain and the environment. For example:<br>`adobe-aem-verification=www.example.com/[program]/[env]/..*` |

1. Save the TXT record to your domain host.

#### Verify TXT record {#customer-managed-cert-verify}

When you are done, you can verify the result by running the following command.

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
>There are several [DNS lookup tools](https://www.ultratools.com/tools/dnsLookup) available. Google DoH can be used to look up TXT record entries and identify if the TXT record is missing or erroneous.

-->

>[!NOTE]
>
>DNS verification can take a few hours to process because of DNS propagation delays.
>
>Cloud Manager verifies ownership and updates the status, which can be seen in the **Domain Settings** table. See [Check custom domain name status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) for more details.

<!--
## Next Steps {#next-steps}

Now that you created your TXT entry, you can verify your domain name status. Proceed to the document [Checking Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) to continue setting up your custom domain name. -->


><!-- The TXT entry and the CNAME or A Record can be set simultaneously on the governing DNS server, thus saving time. -->
>
><!-- To do this, review the entire process of setting up a custom domain name as detailed in the document [Introduction to custom domain names](/help/implementing/cloud-manager/custom-domain-names/introduction.md) taking special note of the document [help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md) and update your DNS settings appropriately. -->

