---
title: Introduction to SSL Certificates
description: Learn about the self-service tools Cloud Manager provides you to install and manage SSL certificates.
exl-id: 0d41723c-c096-4882-a3fd-050b7c9996d8
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Introduction to SSL certificates{#introduction}

Learn about the self-service tools Cloud Manager provides you to install and manage SSL certificates.

>[!CONTEXTUALHELP]
>id="aemcloud_golive_sslcert"
>title="Manage SSL certificates"
>abstract="Learn how Cloud Manager provides you with self-service tools to install and manage SSL certificates to secure your site for your users. Cloud Manager uses a platform TLS service to manage SSL certificates and private keys owned by customers and obtained from third-party certification authorities."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/managing-certificates" text="View, Updating & Replace an SSL Certificate"
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/managing-certificates" text="Check Status of an SSL Certificate"

## What are SSL certificates? {#overview}

Businesses and organizations use SSL (Secure Socket Layer) certificates to secure their websites and allow their customers to place trust in them. To use the SSL protocol, a web server requires an SSL certificate. 

When an entity, such as an organization or business, requests a certificate from a Certificate Authority (CA), the CA completes a verification process. This process can range from verifying domain name control to collecting company registration documents and subscriber agreements. After an entity's information is verified, the CA signs their public key using the CA's private key. Because all major Certificate Authorities have root certificates in web browsers, the entity's certificate is linked through a *chain of trust*, and the web browser recognizes it as a trusted certificate.

>[!IMPORTANT]
>
>Cloud Manager does not provide SSL certificates or private keys. These must be obtained from a Certification Authority, a trusted third-party organization. Some well-known Certificate Authorities include *DigiCert*, *Let's Encrypt*, *GlobalSign*, *Entrust*, and *Verisign*.

## Managing Certificates with Cloud Manager {#cloud-manager}

Cloud Manager offers self-service tools to install and manage SSL certificates, ensuring site security for your users. Cloud Manager supports two models for managing your certificates.

| | Model | Description |
| --- | --- | --- |
| 1 | **[Adobe managed certificate (DV)](#adobe-managed)** | Cloud Manager lets users configure DV (Domain Validation) certificates that that are provided by Adobe for quick domain setup.|
| 2 | **[Customer managed certificate (OV/EV)](#customer-managed)** | Cloud Manager offers a platform TLS (Transport Layer Security) service to allow you to manage OV and EV SSL certificates you own as well as private keys from third-party Certificate Authorities, such as *Let's Encrypt*. | 

Both models offer the following general features.

* Each Cloud Manager environment can use multiple certificates.
* A private key may issue multiple SSL certificates.
* The platform TLS service routes requests to the customer's CDN service based on the SSL certificate used to terminate and the CDN service that hosts that domain.

>[!IMPORTANT]
>
>[To add and and associate a custom domain to an environment,](/help/implementing/cloud-manager/custom-domain-names/introduction.md) you must have have a valid SSL certificate that covers the domain.

### Adobe Managed Certificates {#adobe-managed}

DV certificates are the most basic level of SSL certification and are often used for testing purposes or for securing websites with basic encryption. DV certificates are available in both [production programs and sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md).

After the DV certificate is created, Adobe renews it automatically every three months, unless it is deleted. 

### Customer Managed Certificates {#customer-managed}

OV and EV certificates offer CA-validated information. Such information helps users assess whether the website owner, email sender, or digital signatory of code or PDF documents can be trusted. DV certificates do not allow such ownership verification.

OV and EV additionally offer these features over DV certificates in Cloud Manager.

* Multiple environments can use an OV/EV certificate.
  * That is, it can be added once, but used multiple times.
* Each OV/EV certificate typically contains multiple domains.
* Cloud Manager accepts wildcard OV/EV certificates for a domain.

>[!TIP]
>
>If you you have multiple custom domains and do not want to upload a certificate every time you add a domain, you may benefit by getting one certificate with multiple domains.

>[!NOTE]
>
>If two certificates cover the same domain are installed, the one which is more exact is applied.
>
>For example, if your domain is `dev.adobe.com` and you have a certificate that covers `*.adobe.com` and a certificate that covers `dev.adobe.com`, the latter will be applied because it is more exact.

#### Requirements for Customer Managed Certificates {#requirements}

If you choose to upload your own EV/OV certificate, it must meet the following requirements.

* AEM as a Cloud Service accepts certificates that conform with OV (Organization Validation) or EV (Extended Validation) policy.
  * Cloud Manager does not support uploading your own DV (Domain Validation) certificates.
* Any certificate must be an X.509 TLS certificate from a trusted Certificate Authority with a matching 2048-bit RSA private key.
* Self-signed certificates are not accepted.

#### Format for Customer Managed Certificates {#certificate-format}

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

## Limitation on number of installed SSL certificates {#limitations}

At any given time, Cloud Manager allows a maximum of 50 installed SSL certificates. These certificates can be associated with one or more environments across your program and also include any expired certificates.

If you have reached the limit, review your certificates and consider deleting any expired certificates. Or, group multiple domains in the same certificate since a certificate can cover multiple domains (up to 100 SANs).

## Learn more {#learn-more}

A user with the necessary permissions can use Cloud Manager to manage SSL certificates for a program. See the following documents for more details on using these features.

* [Add an SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) <!--CQDOC-21758, #4 -->
* [Manage SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md) <!--CQDOC-21758, #4 -->

