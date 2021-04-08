---
title: Getting an SSL Certificate - Managing SSL Certificates
description: Getting an SSL Certificate - Managing SSL Certificates
exl-id: a3a247e5-164a-4c9c-aeed-bde882635e6f
---
# Getting an SSL Certificate {#getting-an-ssl-certificate}

Businesses use SSL certificates to secure their websites and allow their customers to place trust in them. In order to use the SSL protocol, a web server requires the use of an SSL certificate. Cloud Manager does not provide SSL certificates or private keys. These must be obtained from Certification Authorities (CA’s).

When an entity requests a certificate from a Certificate Authority, the CA completes a verification process. This can range from verifying domain name control to collecting company registration documents and subscriber agreements. Once an entity's information has been verified, the CA will sign their public key using the CA's private key. Because all major certificate authorities have root certificates in web browsers, the entity's certificate will be linked through a *chain of trust* and the web browser will recognize it as a trusted certificate.

>[!NOTE]
>AEM as a Cloud Service will only accept OV(Organization Validation) or EV(Extended Validation) certificates. DV(Domain Validation) or self-signed certificates will not be accepted. OV and EV certificates provide users with extra, CA-validated information that they can use to decide if the owner of a website, sender of an email, or digital signatory of executable code or PDF documents is trustworthy. DV certificates are common and inexpensive. However, they do not allow ownership verification.
>In addition, any certificate must be a X.509 TLS certificate from a trusted certification authority (CA) with a matching 2048-bit RSA private key.
