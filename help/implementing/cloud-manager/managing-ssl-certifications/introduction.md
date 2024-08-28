---
title: Introduction to Managing SSL Certificates
description: Learn how Cloud Manager provides you with self-service tools to install SSL certificates.
exl-id: 0d41723c-c096-4882-a3fd-050b7c9996d8
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Introduction to Managing SSL Certificates{#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_sslcert"
>title="Manage SSL certificates"
>abstract="Learn how Cloud Manager provides you with self-service tools to install and manage SSL certificates to secure your site for your users. Cloud Manager uses a platform TLS service to manage SSL certificates and private keys owned by customers and obtained from third-party certification authorities."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/managing-certificates" text="View, Updating & Replace an SSL Certificate"
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/managing-certificates" text="Check Status of an SSL Certificate"


Cloud Manager offers self-service tools to install and manage SSL certificates, ensuring site security for your users. The following two use cases are supported:

<!-- CQDOC-21758, #1 -->

* **Use case 1:** Cloud Manager uses a platform TLS service to manage customer-owned SSL certificates and private keys from third-party Certificate Authorities, such as *Let's Encrypt*.
* **Use case 2:** Cloud Manager lets users configure a DV (Domain Validation) certificate from Adobe for quick domain setup. DV certificates are the most basic level of SSL certification and are often used for testing purposes or for securing websites with basic encryption. DV certificates are available to both [production and sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md). 


## Introduction to certificates {#certificates}

Businesses and organizations use SSL certificates to secure their websites and allow their customers to place trust in them. To use the SSL protocol, a web server requires the use of an SSL certificate. 

When an entity, such as an organization or business, requests a certificate from a CA (Certificate Authority), the CA completes a verification process. This process can range from verifying domain name control to collecting company registration documents and subscriber agreements. After an entity's information is verified, the CA signs their public key using the CA's private key. Because all major Certificate Authorities have root certificates in web browsers, the entity's certificate is linked through a *chain of trust*, and the web browser recognizes it as a trusted certificate.

>[!IMPORTANT]
>
>Cloud Manager does not provide SSL certificates or private keys. These things must be obtained from a Certification Authority, a trusted third-party organization. Some well-known Certificate Authorities include *DigiCert*, *Let's Encrypt*, *GlobalSign*, *Entrust*, and *Verisign*.

## Cloud Manager SSL management features {#features}

Cloud Manager supports the following customer SSL certificate usage options.

* Multiple environments can use an SSL certificate. That is, it can be added once, but used multiple times.
* Each Cloud Manager environment can use multiple certificates.
* A private key may issue multiple SSL certificates.
* Each certificate typically contains multiple domains.
* The platform TLS service routes requests to the customer's CDN service based on the SSL certificate used to terminate and the CDN service that hosts that domain.
* AEM as a Cloud Service accepts wildcard SSL certificates for a domain.

## Recommendations {#recommendations}

AEM as a Cloud Service only supports secure `https` sites.

* Customers with multiple custom domains do not want to upload a certificate every time they add a domain.
* Such customers benefit by getting one certificate with multiple domains.

## Certificate requirements {#requirements}

* AEM as a Cloud Service accepts certificates that conform with OV (Organization Validation), or EV (Extended Validation), or DV (Domain Validation) policy. <!-- CQDOC-21758, #2 -->
* Any certificate must be an X.509 TLS certificate from a trusted Certificate Authority with a matching 2048-bit RSA private key.
* Self-signed certificates are not accepted.

OV and EV certificates offer CA-validated information. Such information helps users assess whether the website owner, email sender, or digital signatory of code or PDF documents can be trusted. DV certificates do not allow such ownership verification.

### Customer managed certificate format {#certificate-format} 
<!-- CQDOC-21758, #3 -->

SSL certificate files must be in PEM format to be installed with Cloud Manager. Common file extensions of the PEM format include `.pem,`. `crt`, `.cer`, and `.cert`. 

The following `openssl` commands can be used to convert non-PEM certificates.

* Convert PFX to PEM

  ```shell
  openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes
  ```

* Convert P7B to PEM

  ```shell
  openssl pkcs7 -print_certs -in certificate.p7b -out certificate.cer
  ```

* Convert DER to PEM

  ```shell
  openssl x509 -inform der -in certificate.cer -out certificate.pem
  ```

## Limitations {#limitations}

At any given time, Cloud Manager allows a maximum of 50 installed SSL certificates. These certificates can be associated with one or more environments across your program and also include any expired certificates.

If you have reached the limit, review your certificates and consider:

* Deleting any expired certificates.
* Grouping multiple domains in the same certificate since a certificate can cover multiple domains (up to 100 SANs).

## Learn more {#learn-more}

A user with the necessary permissions can use Cloud Manager to manage SSL certificates for a program. See the following documents for more details on using these features.

* [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md)
* [Viewing, Updating or Replacing an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md)
* [Deleting an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md)
