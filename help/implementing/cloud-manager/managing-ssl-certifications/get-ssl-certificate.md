---
title: Getting an SSL Certificate - Managing SSL Certificates
description: Getting an SSL Certificate - Managing SSL Certificates
---

# Getting an SSL Certificate {#getting-an-ssl-certificate}

Businesses use SSL certificates to secure their websites and allow their customers to place trust in them. In order to use the SSL protocol, a web server requires the use of an SSL certificate. Cloud Manager does not provide SSL certificates or private keys. These must be obtained from Certification Authorities (CA’s).

When an entity requests a certificate from a Certificate Authority (CA), the CA completes a verification process. This can range from verifying domain name control to collecting company registration documents and subscriber agreements. 

Once an entity's information has been verified, the CA will sign their public key using the CA's private key. Because all major certificate authorities have root certificates in web browsers, the entity's certificate will be linked through a *chain of trust* and the web browser will recognize it as a trusted certificate.

