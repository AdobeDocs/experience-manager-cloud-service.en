---
title: Adding an SSL Certificate - Managing SSL Certificates
description: Adding an SSL Certificate - Managing SSL Certificates
---

# Adding an SSL Certificate {#adding-an-ssl-certificate}

>[!NOTE]
>A Certificate takes a few days to provision and it is recommended that the certificate be provisioned even months in advance. Goto How to get an SSL certificate to learn more.INSERT LINK

## Certificate Format {#certificate-format}

SSL files must be in PEM format in order to be installed on Cloud Manager. Common file extensions that are within the PEM format include .pem, .crt, .cer, and .cert. 

Follow the steps below to convert the format of your SSL files to PEM:

1. Convert PFX to PEM

  `openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes`

1. Convert P7B to PEM

  `openssl pkcs7 -print_certs -in certificate.p7b -out certificate.cer`

1. Convert DER to PEM

  `openssl x509 -inform der -in certificate.cer -out certificate.pem`

## Adding your Certificate {#adding-certificate}

>[!NOTE]
>* A user must be in the Business Owner or Deployment Manager role in order to install an SSL certificate in Cloud Manager.
>* At any given time, Cloud Manager will allow a maximum of 5 SSL certificates that can be associated with one or more environments across your Program, even if a certificate is expired. Cloud Manager UI will, however, allow up 50 SSL certificates to be installed in the program with this constraint.

1. Login to Cloud Manager.
1. Navigate to Environments screen from Overview page.
1. Navigate to SSL Certificates screen from the left navigation menu. A table with details of any existing SSL certificates will be displayed on this screen.INSERT IMAGE
1. Select the **Add certificate** button to launch a wizard.
1. Enter a name for your certificate. This can be any name that helps you reference your certificate easily.
1. Paste the Certificate, Private Key and Chain contents into their respective fields. Use the paste icon to the right of the input box.
1. Select **Save**.

   >[!NOTE]
   >Any errors detected will be displayed. You must address all errors before your certificate can be saved. Refer to Certificate INSERT LINK Errors to learn more about addressing common errors.

   Once you submit your certificate, you will see it displayed as a new row in the table.

## Certificate Errors {#certificate-errors}

### Correct Certificate Order {#correct-certificate-order}

The most common reason for a certificate deployment to fail is that the intermediate or chain certificates are not in the correct order. Specifically, intermediate certificate files must end with the root certificate or certificate most proximate to the root and be in a descending order from the `main/server` certificate to the root. 

You can determine the order of your intermediate files using the following command:

`openssl crl2pkcs7 -nocrl -certfile $CERT_FILE | openssl pkcs7 -print_certs -noout`

You can verify that the private key and `main/server` certificate match using the following commands:

`openssl x509 -noout -modulus -in certificate.pem | openssl md5`

`openssl rsa -noout -modulus -in ssl.key | openssl md5`

>[!NOTE]
>The output of these two commands must be exactly the same. If you cannot locate a matching private key to your `main/server` certificate, you will be required to re-key the certificate by generating a new CSR and/or requesting an updated certificate from your SSL vendor.

### Certificate Validity Dates {certificate-validity-dates}

Cloud Manager expects the SSL certificate to be valid for at least 90 days into the future

Check the validity of the certificate chain.
