---
title: Introduction - Managing SSL Certificates
description: Introduction - Managing SSL Certificates
---

# Introduction {#introduction}

Cloud Manager provides customers the self-service capability to install SSL certificates via the Cloud Manager UI. Cloud Manager uses a Platform TLS service to manage SSL certificates and private keys owned by customers and typically obtained from third party certification authorities for example, Let’s Encrypt.

>[!IMPORTANT]
>Cloud Manager does not provide SSL certificates or private keys. These must be obtained from third party certification authorities. See How to Get an SSL Certificate to learn more. INSERT LINK

>[!NOTE] 
>AEM as a Cloud Service only supports secure https sites. Customers with multiple custom domains will not want to upload a certificate every time they add a domain. Hence such customers will benefit by getting one certificate with multiple domains.
  
Cloud Manager supports the following customer SSL certificate requirements: 

* An SSL certificate may be used by multiple Environments- Add once and use multiple times.
* Each Cloud Manager Environment can use multiple certificates.
* A Private Key may issue multiple SSL certificates.
* Each certificate will typically contain multiple Domains.
* The Platform TLS service routes requests to the customer's CDN Service based on the SSL certificate used to terminate and the CDN Service that hosts that domain.

Using the Cloud Manager UI SSL Certificates page, a user with permissions can perform several tasks to manage SSL certificates for a program:

* Adding an SSL certificate.
* Viewing, updating or replacing an SSL certificate. These actions allow you to view details or to replace a certificate that is about to expire.
* Deleting an SSL certificate.