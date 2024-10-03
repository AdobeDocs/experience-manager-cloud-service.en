---
title: Troubleshoot SSL Certificate Errors
description: Learn how to troubleshoot SSL certificate errors by identifying common causes so you can maintain secure connections.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Troubleshoot SSL certificate errors {#certificate-errors}

Learn how to troubleshoot SSL certificate errors by identifying common causes so you can maintain secure connections.

## Correct certificate order {#order}

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


## Remove client certificates {#client-certificates}

When adding a certificate, if you receive an error similar to the following:

```text
The Subject of an intermediate certificate must match the issuer in the previous certificate. The SKI of an intermediate certificate must match the AKI of the previous certificate.
```

You likely included the client certificate in the certificate chain. Make sure that the chain does not include the client certificate and try again.

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

## Certificate validity {#validity}

Cloud Manager expects the SSL certificate to be valid for at least 90 days from the current date. Check the validity of the certificate chain.
