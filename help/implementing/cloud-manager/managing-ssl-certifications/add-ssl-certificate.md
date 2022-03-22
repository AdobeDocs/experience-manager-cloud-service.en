---
title: Adding an SSL Certificate
description: Learn how to add your own SSL certificate using Cloud Manager's self-service tools.
exl-id: 104b5119-4a8b-4c13-99c6-f866b3c173b2
---
# Adding an SSL Certificate {#adding-an-ssl-certificate}

Learn how to add your own SSL certificate using Cloud Manager's self-service tools.

>[!TIP]
>
>A certificate can take a few days to provision. Adobe therefore recommends that the certificate is provisioned well in advance.

## Certificate Format {#certificate-format}

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

## Adding a Certificate {#adding-a-cert}

Follow these steps to add a certificate using Cloud Manager.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to **Environments** screen from the **Overview** page.

1. Click on **SSL Certificates** from the left navigation panel. A table with details of any existing SSL certificates will be displayed on the main screen.

   ![Adding an SSL cert](/help/implementing/cloud-manager/assets/ssl/ssl-cert-1.png)

1. Click on **Add SSL Certificate** to open **Add SSL Certificate** dialog box.

   * Enter a name for your certificate in **Certificate Name**.
     * This is for informational purposes only and can be any name that helps you reference your certificate easily.
   * Paste the **Certificate**, **Private key**, and **Certificate chain** values into their respective fields.
     * You can use the paste icon to the right of the input box. 
     * All three fields are mandatory.

   ![Add SSL Certificate dialog](/help/implementing/cloud-manager/assets/ssl/ssl-cert-02.png)
  
   * Any errors detected will be displayed.
     * You must address all errors before your certificate can be saved.
     * Refer to the [Certificate Errors](#certificate-errors) section to learn more about addressing common errors.

1. Click **Save** to save your certificate.

Once saved, you will see your certificate displayed as a new row in the table.

![Saved SSL certificate](/help/implementing/cloud-manager/assets/ssl/ssl-cert-3.png)

>[!NOTE]
>
>A user must be a member of the **Business Owner** or **Deployment Manager** role in order to install an SSL certificate in Cloud Manager.

## Certificate Errors {#certificate-errors}

Certain errors may arise if a certificate is not installed properly or meet the requirements of Cloud Manager.

### Certificate Policy {#certificate-policy}

If you see the following error, please check the policy of your certificate.

```text
Certificate policy must conform with EV or OV, and not DV policy.
```

Normally certificate policies are identified by embedded OID values. Outputting a certificate to text and searching for the OID will reveal the certificate's policy.

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

### Correct Certificate Order {#correct-certificate-order}

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
>The output of these two commands must be exactly the same. If you can not locate a matching private key for your `main/server` certificate, you will be required to re-key the certificate by generating a new CSR and/or requesting an updated certificate from your SSL vendor.

### Certificate Validity Dates {#certificate-validity-dates}

Cloud Manager expects the SSL certificate to be valid for at least 90 days from the current date. You should check the validity of the certificate chain.
