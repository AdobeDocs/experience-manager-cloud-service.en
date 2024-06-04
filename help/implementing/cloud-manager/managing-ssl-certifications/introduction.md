---
title: Introduction to Managing SSL Certificates
description: Learn how Cloud Manager provides you with self-service tools to install SSL certificates.
exl-id: 0d41723c-c096-4882-a3fd-050b7c9996d8
solution: Experience Manager
feature: "Cloud Manager, Developing"
role: "Admin, Architect, Developer"
---

# Introduction to Managing SSL Certificates{#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_sslcert"
>title="Manage SSL Certificates"
>abstract="Learn how Cloud Manager provides you with self-service tools to install and manage SSL certificates to secure your site for your users. Cloud Manager uses a platform TLS service to manage SSL certificates and private keys owned by customers and obtained from third-party certification authorities."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/managing-certificates.html" text="View, Updating & Replace an SSL Certificate"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/managing-certificates.html" text="Check Status of an SSL Certificate"

Cloud Manager provides you with self-service tools to install and manage SSL certificates so you can secure your site for your users. Cloud Manager uses a platform TLS service to manage SSL certificates and private keys owned by customers and obtained from third-party certification authorities such as Let's Encrypt.

## Introduction to Certificates {#certificates}

Businesses use SSL certificates to secure their websites and allow their customers to place trust in them. To use the SSL protocol, a web server requires the use of an SSL certificate. 

When an entity requests a certificate from a Certificate Authority, the CA completes a verification process. This can range from verifying domain name control to collecting company registration documents and subscriber agreements. Once an entity's information has been verified, the CA will sign their public key using the CA's private key. Because all major certificate authorities have root certificates in web browsers, the entity's certificate is linked through a *chain of trust* and the web browser will recognize it as a trusted certificate.

>[!IMPORTANT]
>
>Cloud Manager does not provide SSL certificates or private keys. These must be obtained from Certification Authorities (CAs).

## Cloud Manager SSL Management Features {#features}

Cloud Manager supports the following customer SSL certificate usage options.

* An SSL certificate may be used by multiple environments. I.e. it can be added once and used multiple times.
* Each Cloud Manager environment can use multiple certificates.
* A private key may issue multiple SSL certificates.
* Each certificate typically contains multiple domains.
* The platform TLS service routes requests to the customer's CDN service based on the SSL certificate used to terminate and the CDN service that hosts that domain.
* AEM as a Cloud Service accepts wildcard SSL certificates for a domain.

## Recommendations {#recommendations}

AEM as a Cloud Service only supports secure `https` sites.

* Customers with multiple custom domains will not want to upload a certificate every time they add a domain.
* Such customers benefit by getting one certificate with multiple domains.

## Certificate Requirements {#requirements}

* AEM as a Cloud Service will only accept certificates that conform with OV (Organization Validation) or EV (Extended Validation) policy.
* Any certificate must be a X.509 TLS certificate from a trusted certification authority (CA) with a matching 2048-bit RSA private key.
* DV (Domain Validation) policy is not accepted.
* Self-signed certificates are not accepted.

OV and EV certificates provide users with extra, CA-validated information that can be used to decide if the owner of a website, sender of an email, or digital signatory of executable code or PDF documents is trustworthy. DV certificates do not allow such ownership verification.

### Certificate Format {#certificate-format}

SSL certificate files must be in PEM format to be installed with Cloud Manager. Common file extensions of the PEM format include `.pem,` .`crt`, `.cer`, and `.cert`. 

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

At any given time, Cloud Manager will allow a maximum of 50 SSL certificates to be installed. These can be associated with one or more environments across your program and also include any expired certificates.

If you have reached the limit, review your certificates and consider:

* Deleting any expired certificates.
* Grouping multiple domains in the same certificate since a certificate can cover multiple domains (up to 100 SANs).

## Learn More {#learn-more}

A user with the necessary permissions can use Cloud Manager to manage SSL certificates for a program. See the following documents for more details on using these features.

* [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md)
* [Viewing, Updating or Replacing an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md)
* [Deleting an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md)
