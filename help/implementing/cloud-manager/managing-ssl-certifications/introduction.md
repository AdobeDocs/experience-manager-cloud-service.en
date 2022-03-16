---
title: Introduction to Managing SSL Certificates
description: Learn how Cloud Manager provides you with self-service tools to install SSL certificates.
exl-id: 0d41723c-c096-4882-a3fd-050b7c9996d8
---

# Introduction {#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_sslcert"
>title="Manage SSL Certificates"
>abstract="Learn how Cloud Manager provides you with self-service tools to install SSL certificates. Cloud Manager uses a platform TLS service to manage SSL certificates and private keys owned by customers and typically obtained from third party certification authorities."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-ssl-certificates/view-update-replace-ssl-certificate.html" text="View, Updating & Replace an SSL Certificate"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-ssl-certificates/check-status-ssl-certificate.html" text="Check Status of an SSL Certificate"

Cloud Manager provides you with self-service tools to install SSL certificates. Cloud Manager uses a platform TLS service to manage SSL certificates and private keys owned by customers and typically obtained from third party certification authorities such as Let’s Encrypt.

>[!NOTE]
>
> Cloud Manager does not provide SSL certificates or private keys. These must be obtained from third party certification authorities.
>
>Please refer to the document [Getting an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/get-ssl-certificate.md) to learn more.

## Features {#features}

Cloud Manager supports the following customer SSL certificate usage options.

* An SSL certificate may be used by multiple environments. I.e. it can be added once and used multiple times.
* Each Cloud Manager environment can use multiple certificates.
* A private key may issue multiple SSL certificates.
* Each certificate will typically contain multiple domains.
* The platform TLS service routes requests to the customer's CDN service based on the SSL certificate used to terminate and the CDN service that hosts that domain.
* AEM as a Cloud Service will accept wildcard SSL certificates for a domain.

## Recommendations {#recommendations}

AEM as a Cloud Service only supports secure `https` sites.

* Customers with multiple custom domains will not want to upload a certificate every time they add a domain.
* Such customers will benefit by getting one certificate with multiple domains.

## Requirements {#requirements}

* AEM as a Cloud Service will only accept certificates that conform with OV (Organization Validation) or EV (Extended Validation) policy.
* Any certificate must be a X.509 TLS certificate from a trusted certification authority (CA) with a matching 2048-bit RSA private key.
* DV (Domain Validation) policy is not accepted.

## Limitations {#limitations}

At any given time, Cloud Manager will allow a maximum of 50 SSL certificates that can be associated with one or more environments across your program, even if a certificate is expired.

The Cloud Manager UI will, however, allow up 50 SSL certificates to be installed in the program with this constraint.

Typically a certificate can cover multiple domains (up to 100 SANs) so consider grouping multiple domains in the same certificate to stay under this limit.

## Learn More {#learn-more}

A user with the necessary permissions can use Cloud Manager to manage SSL certificates for a program. Please refer to the following documents for more details on using these features.

* [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md)
* [Viewing, Updating or Replacing an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/view-update-replace-ssl-certificate.md)
* [Deleting an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/delete-ssl-certificate.md)
