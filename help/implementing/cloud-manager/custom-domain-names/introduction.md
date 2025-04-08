---
title: Introduction to Custom Domain Names
description: Cloud Manager's UI lets you add a custom domain to identify your site with a unique, branded name in a self-service manner.
exl-id: ed03bff9-dfcc-4dfe-a501-a7facd24aa7d
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Introduction to custom domain names {#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_domains"
>title="Manage Custom Domain Names"
>abstract="Cloud Manager's UI lets you add a custom domain to identify your site with a unique, branded name in a self-service manner."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/custom-domain-names/add-custom-domain-name" text="Adding a Custom Domain Name"
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/custom-domain-names/managing-custom-domain-names" text="View & Update Custom Domain Name"

Adobe Experience Manager as a Cloud Service is provisioned with a default domain name, ending in `*.adobeaemcloud.com`. Using Cloud Manager's UI you can add a custom domain to identify your site with a unique, branded name in a self-service manner. The default `*.adobeaemcloud.com` domain name remains, even after you associate custom domain names to your website.

## What are custom domain names? {#what-are-custom-domain-names}

Each website has a unique, machine-readable, numerical address associated with it such as `184.33.123.64`. The Domain Name System (DNS) is what lets you have custom, branded domains attached to websites by translating numerical addresses into memorable addresses such as `wknd.com`.

It is good practice to have a domain name for your site that is memorable for your customers and reflects your brand.

You can buy a domain name from a domain name registrar, a company or organization managing and selling domain names. Domain name registrars manage domain names on DNS servers.

>[!IMPORTANT]
>
>Cloud Manager is not a domain name registrar and does not provide DNS services.

## Custom domain names and Bring Your Own CDNs {#byo-cdn}

AEM as a Cloud Service offers a built-in CDN (Content Delivery Network) service, but also lets you BYO (Bring Your Own) CDN to use with AEM. Custom domains can be installed either in the AEM-managed CDN or a CDN you manage.

* Cloud Manager manages custom domain names and certificates installed in the AEM-managed CDN.
* Custom domain names and certificates installed in a BYO CDN are managed directly within that CDN. 

**Domains managed in your own CDN do not require installation through Cloud Manager** - They are made available to AEM by way of X-Forwarded-Host and match the vhosts defined in the Dispatcher. See the [CDN documentation](/help/implementing/dispatcher/cdn.md).

In one environment, you can have both domains installed in the AEM-managed CDN and installed in a BYO CDN.

## Workflow {#workflow}

Adding a custom domain name requires interaction between the DNS service and Cloud Manager. Because of this workflow, there are several steps required to install, configure, and verify custom domain names. The following table gives an overview of the steps required, including links to documentation resources to complete those steps.

| Step | Description | Documentation |
| --- | --- | --- |
| 1 |Add SSL certificate to Cloud Manager | [Add an SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) |
| 2 | Add custom domain to Cloud Manager | [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) |
| 3 | Configure DNS settings by adding DNS CNAME or APEX records that point to AEM as a Cloud Service | [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) |
| 4 | Review domain verification status | [Check domain name status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) |
| 5 | Check DNS record status | [Check DNS record status](/help/implementing/cloud-manager/custom-domain-names/check-dns-record-status.md) |

>[!TIP]
>
>Setting up custom domain names with AEM as a Cloud service is typically a simple process. However, on occasion, domain delegation issues can occur which can take 1-2 business days to resolve. For this reason, it is recommended to install the domains well before their go live date. See the document [Check domain name status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) for more information.

## Limitations {#limitations}

There are several limitations to using custom domain names with AEMaaCS.

* Custom domain names are supported in Cloud Manager only for publish and preview services for Sites programs.
  * Custom domains for author services are not supported.
* Each Cloud Manager environment can host up to a maximum of 500 custom domains per environment.
* Domain names cannot be added to environments while there is a current running pipeline attached to those environments.
* The same domain name cannot be used in more than one environment.
* Only one domain name can be added at a time.
* AEM as a Cloud Service does not support wildcard domains such as `*.example.com`.
* Before adding a custom domain name, a valid SSL certificate that contains the custom domain name (wildcard certificates are valid) must be installed for your program.
* Additional configuration steps are required to use a custom domain name with [the Front-End Pipeline feature](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md#custom-domains).

## Get started {#get-started}

* Get started configuring a new custom domain name for your project by [adding an SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md).
* Manage your existing domain names by reviewing the document [Manage custom domain names](/help/implementing/cloud-manager/custom-domain-names/managing-custom-domain-names.md).
