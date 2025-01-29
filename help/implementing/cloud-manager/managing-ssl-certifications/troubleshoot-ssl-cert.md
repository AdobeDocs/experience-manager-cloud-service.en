---
title: Troubleshoot SSL Certificate Problems
description: Learn how to troubleshoot SSL certificate problems by identifying common causes so you can maintain secure connections.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
exl-id: 8fb8f708-51a5-46d0-8317-6ce118a70fab
---
# Troubleshoot SSL certificate problems {#certificate-problems}

Learn how to troubleshoot SSL certificate problems by identifying common causes so you can maintain secure connections.

+++**Invalid certificate**

## Invalid certificate {#invalid-certificate}

This error occurs because the customer used an encrypted private key and provided the key in DER format.

+++

+++**Private key needs to be PKCS 8 format**

## Private key needs to be PKCS 8 format {#pkcs-8}

This error occurs because the customer used an encrypted private key and provided the key in DER format.

+++

+++**Correct certificate order**

## Correct certificate order {#certificate-order}

The most common reason for a certificate deployment to fail is that the intermediate or chain certificates are not in the correct order.

Intermediate certificate files must end with the root certificate or the certificate most proximate to the root. They must be in descending order from the `main/server` certificate to the root. 

You can determine the order of your intermediate files using the following command.

```shell
openssl crl2pkcs7 -nocrl -certfile $CERT_FILE | openssl pkcs7 -print_certs -noout
```

You can verify that the private key and `main/server` certificate match using the following commands.

```shell
openssl x509 -noout -modulus -in certificate.pem | openssl md5
```

```shell
openssl rsa -noout -modulus -in ssl.key | openssl md5
```

>[!NOTE]
>
>The output of these two commands must be exactly the same. If you cannot locate a matching private key for your `main/server` certificate, you are required to re-key the certificate by generating a new CSR and/or requesting an updated certificate from your SSL vendor.

+++ 

+++**Remove client certificates**

## Remove client certificates {#client-certificates}

When adding a certificate, if you receive an error similar to the following:

```text
The Subject of an intermediate certificate must match the issuer in the previous certificate. The SKI of an intermediate certificate must match the AKI of the previous certificate.
```

You likely included the client certificate in the certificate chain. Make sure that the chain does not include the client certificate and try again.

+++

+++**Certificate policy**

## Certificate policy {#policy}

If you see the following error, check the policy of your certificate.

```text
Certificate policy must conform with EV or OV, and not DV policy.
```

Embedded OID values normally identify certificate policies. Outputting a certificate to text and searching for the OID reveals the certificate's policy.

You can output your certificate detail as text using the following example as a guide.

```text
openssl x509 -in 9178c0f58cb8fccc.pem -text
certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            91:78:c0:f5:8c:b8:fc:cc
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = US, ST = Arizona, L = Scottsdale, O = "GoDaddy.com, Inc.", OU = http://certs.godaddy.com/repository/, CN = Go Daddy Secure Certificate Authority - G2
        Validity
            Not Before: Nov 10 22:55:36 2021 GMT
            Not After : Dec  6 15:35:06 2022 GMT
        Subject: C = US, ST = Colorado, L = Denver, O = Alexandra Alwin, CN = adobedigitalimpact.com
        Subject Public Key Info:
...
```

The OID pattern in the text defines the policy type of the certificate.

|Pattern|Policy|Acceptable in Cloud Manager|
|---|---|---|
|`2.23.140.1.1`|EV|Yes|
|`2.23.140.1.2.2`|OV|Yes|
|`2.23.140.1.2.1`|DV|No|

By `grep`ping for the OID patterns in the output certificate text, you can confirm your certificate policy.

```shell
# "EV Policy"
openssl x509 -in certificate.pem -text grep "Policy: 2.23.140.1.1" -B5

# "OV Policy"
openssl x509 -in certificate.pem -text grep "Policy: 2.23.140.1.2.2" -B5

# "DV Policy - Not Accepted"
openssl x509 -in certificate.pem -text grep "Policy: 2.23.140.1.2.1" -B5
```
+++

+++**Certificate validity

## Certificate validity {#validity}

Cloud Manager expects the SSL certificate to be valid for at least 90 days from the current date. Check the validity of the certificate chain.

+++

+++**Wrong SAN certificate is applied to my domain

## Wrong SAN certificate is applied to my domain {#wrong-san-cert}

Let's say that you want to link `dev.yoursite.com` and `stage.yoursite.com` to your non-production environment and `prod.yoursite.com` to your production environment.

In order to configure the CDN for these domains, you need a certificate installed for each, so you install one certificate that covers `*.yoursite.com` for your non-production domains and another that also covers `*.yoursite.com` for your production domains.

This configuration is valid. However, when you update one of the certificates, because both certificates cover the same SAN entry, the CDN will install the most recent certificate upon all the applicable domains, which could appear unexpected.

Although this may be unexpected this is not an error and is the standard behavior of the underlying CDN. If you have two or more SAN certificates that cover the same SAN domain entry, if that domain is covered by one certificate and the other one is updated, the latter will now be installed for the domain.

+++
