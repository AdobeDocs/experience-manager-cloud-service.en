---
title: Introduction - Managing SSL Certificates
description: Introduction - Managing SSL Certificates
exl-id: 0d41723c-c096-4882-a3fd-050b7c9996d8
---
# Introduction {#introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_sslcert"
>title="Manage SSL Certificates"
>abstract="Cloud Manager provides customers the self-service capability to install SSL certificates via the Cloud Manager UI. Cloud Manager uses a Platform TLS service to manage SSL certificates and private keys owned by customers and typically obtained from third party certification authorities."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-ssl-certificates/view-update-replace-ssl-certificate.html" text="View, Updating & Replace an SSL Certificate"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-ssl-certificates/check-status-ssl-certificate.html" text="Check Status of an SSL Certificate"


Cloud Manager provides customers the self-service capability to install SSL certificates via the Cloud Manager UI. Cloud Manager uses a Platform TLS service to manage SSL certificates and private keys owned by customers and typically obtained from third party certification authorities for example, *Let’s Encrypt*.

## Important Considerations {#important-considerations}

* Cloud Manager does not provide SSL certificates or private keys. These must be obtained from third party certification authorities. Refer to [Getting an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/get-ssl-certificate.md) to learn more.

* AEM as a Cloud Service only supports secure `https` sites. Customers with multiple custom domains will not want to upload a certificate every time they add a domain. Hence such customers will benefit by getting one certificate with multiple domains.

* AEM as a Cloud Service will only accept OV(Organization Validation) or EV(Extended Validation) certificates. DV(Domain Validation) certificates will not be accepted. In addition, any certificate must be a X.509 TLS certificate from a trusted certification authority (CA) with a matching 2048-bit RSA private key.

* AEM as a Cloud Service will accept wildcard SSL certificates for a domain.
  
Cloud Manager supports the following customer SSL certificate requirements: 

* An SSL certificate may be used by multiple Environments, that is, add once and use multiple times.
* Each Cloud Manager Environment can use multiple certificates.
* A Private Key may issue multiple SSL certificates.
* Each certificate will typically contain multiple Domains.
* The Platform TLS service routes requests to the customer's CDN Service based on the SSL certificate used to terminate and the CDN Service that hosts that domain.

Using the Cloud Manager UI SSL Certificates page, a user with permissions can perform several tasks to manage SSL certificates for a program:

* [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md)
* [Viewing, Updating or Replacing an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/view-update-replace-ssl-certificate.md)
   >[!NOTE]
   >These actions allow you to view details or to replace a certificate that is about to expire.
* [Deleting an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/delete-ssl-certificate.md)
