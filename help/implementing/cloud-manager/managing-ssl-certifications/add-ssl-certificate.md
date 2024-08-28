---
title: Add an SSL Certificate or DV Certificate
description: Learn how to add your own SSL certificate or Domain Validation certificate using Cloud Manager's self-service tools.
exl-id: 104b5119-4a8b-4c13-99c6-f866b3c173b2
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Add an SSL certificate or a DV certificate

Learn how to add your own SSL certificate or DV (Domain Validation) certificate using Cloud Manager's self-service tools.

See [Add an SSL certificate](#adding-an-ssl-certificate)
See [Add a DV certificate]()


## Add an SSL certificate {#adding-an-ssl-certificate}

Learn how to add your own SSL certificate using Cloud Manager's self-service tools.

>[!TIP]
>
>A certificate can take a few days to provision. As such, Adobe recommends that the certificate be provisioned well in advance of any deadline or go-live date.

Be sure you review **Certificate requirements** in [Introduction to Managing SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md#requirements) to make sure AEM as a Cloud Service supports the certificate that you want to add.



**To add an SSL or DV certificate:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization. 

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. From the **Overview** page, navigate to the **Environments** screen.

1. From the left navigation panel, under **Services**, click **SSL Certificates**. If necessary, you may need to click the hamburger icon in the upper-left corner to reveal the navigation panel. A table with details of any existing SSL certificates is displayed.

   ![Adding a SSL cert](/help/implementing/cloud-manager/assets/ssl/ssl-cert-1.png)

1. Near the upper-right corner of the page, click **Add SSL Certificate**.

1. In the **Add SSL certificate** dialog box, do one of the following based on your particular use case:

    **Add an SSL certificate:**
    1. Select the certificate type **Customer managed (OV/EV)**.
    1. In **Certificate name** field, enter a name for your certificate. This field is for informational purposes only and can be any name that helps you reference your certificate easily.
    1. In the **Certificate**, **Private key**, and **Certificate chain** fields, paste the required values into their respective fields.

        ![Add SSL certificate dialog box](/help/implementing/cloud-manager/assets/ssl/ssl-cert-02.png)
  
    Any detected errors in values are displayed. Before you can save your certificate, you must address all errors. See [Certificate errors](#certificate-errors) to learn more about troubleshooting common errors.

    **Add a DV certificate:**
    1. Select the certificate type **Adobe managed (DV)**.

        ![Adding a DC certificate](/help/implementing/cloud-manager/assets/ssl/add-dv-certificate.png)

    1. In the **Select domains** drop-down list, select one or more domains that you want associated with the DV certificate.

        No domains to select? If so, it means that you must add a custom domain. See [Add a custom domain](#add-custom-domain). When you are finished, resume the steps from the beginning again.

1. Click **Save**.

    ![Pending DV cert](assets/pending-dv-certificate.png)After successfully adding the SSL or DV certificate, it shows a pending status with a yellow warning sign next to its name in the **SSL Certificates** window.

    ![Issued DV cert](assets/issued-dv-certificate.png)After the SSL or DV certificate is successfully issued, it shows a green check mark to its name in the **SSL Certificates** window.

>[!NOTE]
>
>A user must be a member of the **Business Owner** or **Deployment Manager** role to install an SSL certificate in Cloud Manager.

### Add a custom domain {#add-custom-domain}

Before you can add a Domain Validated (DV) certificate, you must first add a custom domain. The process for doing so is nearly the same as detailed in [Introduction to Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/introduction.md) and [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). However, that functionality is now slightly expanded, as described below.

1. When adding a custom domain name, in the **Verify domain** dialog box, select **Adobe managed certificate**.

    ![Choose Adobe-managed](assets/verify-domain-dialog.png)

1. In the **Verify domain** dialog box, add a CNAME verification record to your DNS.

    ![Add CNAME entry](assets/verify-domain-dialog-adobe-managed.png)

1. After the domain is created, click the ellipsis button in the list of domains and select **Verify** to verify the domain.

    ![Verify domain](assets/verify-domain.png) 

1. You can now resume [adding a DV certificate]() by starting at the beginning of these steps again.



### Troubleshooting certificate errors {#certificate-errors}

Certain errors may arise if a certificate is not installed properly or does not meet the requirements of Cloud Manager.

* **Correct certificate order**

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

* **Remove client certificates**

    When adding a certificate, if you receive an error similar to the following:

    ```text
    The Subject of an intermediate certificate must match the issuer in the previous certificate. The SKI of an intermediate certificate must match the AKI of the previous certificate.
    ```

    You likely included the client certificate in the certificate chain. Make sure that the chain does not include the client certificate and try again.

* **Certificate policy**

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

* **Certificate validity dates**

    Cloud Manager expects the SSL certificate to be valid for at least 90 days from the current date. Check the validity of the certificate chain.

### Next steps {#next-steps}

You now have added a working SSL certificate for your project. This step is often the first to set up a custom domain name.

* To set up a custom domain name, see [Add a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).
* To learn about updating and managing your SSL certificates in Cloud Manager, see [Manage SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md).

## Add a DV certificate {#add-dv-cert}

Before you can add a Domain Validated (DV) certificate, you must first add your custom domain name. The process is nearly the same as detailed in [Introduction to custom domain names](/help/implementing/cloud-manager/custom-domain-names/introduction.md) and . However, that functionality is now slightly expanded, as described below.

Add your custom domain name

1. When verifying the domain, you can choose to use Adobe-manged or self-managed certificates with the domain. Select **Adobe managed certificate** so you can add a DV certificate later.

   ![Choose Adobe-managed](assets/verify-domain-dialog.png)

1. To use an Adobe managed certificate, add a CNAME record to your DNS as described in the **Verify domain** dialog.

   ![Add CNAME entry](assets/verify-domain-dialog-adobe-managed.png)

1. Once the domain is created, tap or click the ellipsis button in the list of domains and select **Verify** to verify the domain.

   ![Verify domain](assets/verify-domain.png)

## Add a DV certificate {#adding}

Once you have your domain correctly configured, to add a DV certificate, tap or click the **Add SSL certificate** button in the SSL Certificates window.

![Adding a DC certificate](/help/implementing/cloud-manager/assets/ssl/add-dv-certificate.png)

1. Select **Adobe managed (DV)**.
1. Specify the domain name in the **Select domains** drop down.
1. Tap or click **Save**.

Once successfully added the certificate will have a pending status with a yellow warning sign to its name in the **SSL Certificates** window.

![Pending DV cert](assets/pending-dv-certificate.png)

Once successfully issued the certificate will have a green check mark to its name in the **SSL Certificates** window.

![Issued DV cert](assets/issued-dv-certificate.png)

For more information about adding SSL certificates and the SSL Certificates window, see [Add an SSL certificate](#add-ssl-certificate.md).
