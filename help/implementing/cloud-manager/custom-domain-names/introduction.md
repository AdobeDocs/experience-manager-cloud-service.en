---
title: Introduction to Custom Domain Names
description: Cloud Manager's UI lets you add a custom domain to identify your site with a unique, branded name in a self-service manner.
exl-id: ed03bff9-dfcc-4dfe-a501-a7facd24aa7d
---

# Introduction to Custom Domain Names {#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_domains"
>title="Manage Custom Domain Names"
>abstract="Cloud Manager's UI lets you add a custom domain to identify your site with a unique, branded name in a self-service manner."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/custom-domain-names/add-custom-domain-name" text="Adding a Custom Domain Name"
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/custom-domain-names/managing-custom-domain-names" text="View & Update Custom Domain Name"

Cloud Manager's UI lets you add a custom domain to identify your site with a unique, branded name in a self-service manner. Adobe Experience Manager as a Cloud Service is provisioned with a default domain name, ending in `*.adobeaemcloud.com`. This default domain name remains, even after you associate custom domain names to your website.

## What are Custom Domain Names? {#what-are-custom-domain-names}

Each website has a unique, machine-readable, numerical address associated with it such as `184.33.123.64`. The Domain Name System (DNS) is what lets you have custom, branded domains attached to websites by translating numerical addresses into memorable addresses such as `wknd.com`.

It is good practices to have a domain name for your site that is memorable for your customers and reflects your brand.

You can buy a domain name from a domain name registrar, a company or organization managing and selling domain names. Domain name registrars manage domain names on DNS servers.

>[!IMPORTANT]
>
>Cloud Manager is not a domain name registrar and does not provide DNS services.

## Custom Domain Names and BYO CDNs {#byo-cdn}

AEM as a Cloud Service offers a built-in content delivery network (CDN) service, but also lets you bring-your-own (BYO) CDN to use with AEM. Custom domains can be installed either in the AEM-managed CDN or a CDN you manage.

* Custom domain names (and certificates) that are installed in the AEM-managed CDN are managed via Cloud Manager.
* Custom domain names (and certificates) that are installed in your own CDN are managed in that specific CDN. 

Domains managed in your own CDN do not need to be installed by way of Cloud Manager. They are made available to AEM by way of X-Forwarded-Host and match the vhosts defined in the Dispatcher. See the [CDN documentation](/help/implementing/dispatcher/cdn.md).

In one environment you can have both domains installed in the AEM-managed CDN and installed in your own CDN.

## Workflow {#workflow}

Adding a custom domain name requires interaction between the DNS service and Cloud Manager. Because of this there are several steps required to install, configure,and verify custom domain names. The following table gives an overview of the steps required, including what to do when common errors occur.

|Step|Description|Responsibility|Learn More|
|--- |--- |--- |---|
|1|Add SSL certificate to Cloud Manager|Customer|[Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md)|
|2|Add TXT record to verify domain|Customer|[Adding a TXT Record](/help/implementing/cloud-manager/custom-domain-names/add-text-record.md)|
|3|Review Domain Verification Status|Customer|[Checking Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md)|
|3a|If domain verification fails with the status `Domain Verification Failure`|Customer|[Checking Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md)|
|3b|If domain verification fails with the status `Verified, Deployment Failed`, contact Adobe|Adobe Customer Care|[Checking Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md)|
|4|Configure DNS settings by adding DNS CNAME or APEX records that point to AEM as a Cloud Service|Customer|[Configuring DNS Settings](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md)|
|5|Check DNS record status|Customer|[Checking DNS Record Status](/help/implementing/cloud-manager/custom-domain-names/check-dns-record-status.md)|
|5a|If DNS record status fails with `DNS status not detected`|Customer|[Checking DNS Record Status](/help/implementing/cloud-manager/custom-domain-names/check-dns-record-status.md)|
|5b|If DNS record status fails with `DNS resolves incorrectly`|Customer|[Checking DNS Record Status](/help/implementing/cloud-manager/custom-domain-names/check-dns-record-status.md)|

>[!TIP]
>
>Setting up custom domain names with AEM as a Cloud service is typically a simple process. However on occasion domain domain delegation issues can occur which can take 1-2 business days to resolve. For this reason, it is highly recommended to install the domains well before their go live date. See the document [Checking Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) for more information.

## Limitations {#limitations}

There are several limitations to using custom domain names with AEMaaCS.

* Custom domain names are supported in Cloud Manager for both publish and preview services for Sites programs. Custom domains for author services are not supported.
* Each Cloud Manager environment can host up to a maximum of 500 custom domains per environment.
* Domain namescannot be added to environments while there is a current running pipeline attached to those environments.
* The same domain namecannot be used on more than one environment.
* Only one domain name can be added at a time.
* AEM as a Cloud Service does not support wildcard domains such as `*.example.com`.
* Before adding a custom domain name, a valid SSL certificate that contains the custom domain name (wildcard certificates are valid) must be installed for your program. See [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) to learn more.
