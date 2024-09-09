---
title: Add an SSL Certificate
description: Learn how to add your own SSL certificate or DV (Domain Validation) certificate using Cloud Manager's self-service tools.
exl-id: 104b5119-4a8b-4c13-99c6-f866b3c173b2
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Add an SSL certificate

Learn how to add a customer managed SSL certificate or an Adobe generated and managed DV (Domain Validation) certificate using Cloud Manager's self-service tools.


## Add an SSL or DV certificate {#adding-an-ssl-certificate}

A certificate can take a few days to provision. As such, Adobe recommends that the certificate be provisioned well in advance of any deadline or go-live date.

Be sure you review **Certificate requirements** in [Introduction to Managing SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md#requirements) to make sure AEM as a Cloud Service supports the certificate that you want to add.

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

>[!NOTE]
>
>Customers are not permitted to upload DV (Domain Validation) certificates.

**To add an SSL or DV certificate:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization. 

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. From the **Overview** page, navigate to the **Environments** screen.

1. From the left navigation panel, under **Services**, click **SSL Certificates**. If you do not see the left navigation panel as seen in the following image, you may need to click the hamburger icon in the upper-left corner.

   ![Adding an SSL certificate](/help/implementing/cloud-manager/assets/ssl/ssl-cert-add.png)

1. Near the upper-right corner of the page, click **Add SSL Certificate**.

1. In the **Add SSL certificate** dialog box, based on [your particular use case](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md), do one of the following:

    | | Use case | Steps |
    | --- | --- | --- |
    | 1 | **Add an Adobe managed certificate (DV)** | **To add an Adobe managed certificate (DV):**<br>a. Select the certificate type **Adobe managed (DV)**.<br>![Add a DV certificate](/help/implementing/cloud-manager/assets/ssl/add-dv-certificate.png)<br>b. In the **Select domains** drop-down list, select one or more domains that you want associated with the DV certificate.<br>No domains to select? If so, it means that you must add a custom domain. See [Add a custom domain](#add-custom-domain). When you are finished adding a custom domain name, return to this topic and begin at step 1 again.<br>d. Continue to step 7. |
    | 2 | **Add a customer managed certificate (OV/EV)** | **To add a customer managed certificate (OV/EV):**<br>a. Select the certificate type **Customer managed (OV/EV)**.<br>b. In the **Certificate name** field, enter a name for your certificate. This field is for informational purposes only and can be any name that helps you reference your certificate easily.<br>c. In the **Certificate**, **Private key**, and **Certificate chain** fields, paste the required values into their respective fields.<br>![Add SSL certificate dialog box](/help/implementing/cloud-manager/assets/ssl/ssl-cert-02.png)<br>Any detected errors in values are displayed. Before you can save your certificate, you must address all errors. See [Certificate Errors](#certificate-errors) to learn more about troubleshooting common errors.<br>d. Continue to step 7. | 

<!--
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

        No domains to select? If so, it means that you must add a custom domain. See [Add a custom domain](#add-custom-domain). When you are finished, resume the steps from the beginning again. -->

1. In the lower-right corner of the dialog box, click **Save**.

    After the certificate is successfully issued, it shows a green check mark, as seen in the image above

    ![Issued DV cert](assets/issued-dv-certificate.png)

### Add a custom domain {#add-custom-domain}

Before you can add an Adobe generated and managed Domain Validated (DV) certificate, you must first add a custom domain. The process for doing so is nearly the same as detailed in [Introduction to custom domain names](/help/implementing/cloud-manager/custom-domain-names/introduction.md) and [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). However, that functionality is now slightly expanded, as described below.

1. When adding a custom domain name, in the **Verify domain** dialog box, select an **Adobe managed certificate**.

    ![Choose Adobe-managed](assets/verify-domain-dialog.png)

1. In the **Verify domain** dialog box, add a CNAME verification record to your DNS.

    ![Add CNAME entry](assets/verify-domain-dialog-adobe-managed.png)

1. After the domain is created, click the ellipsis button in the list of domains and select **Verify** to verify the domain.

    ![Verify domain](assets/verify-domain.png) 

1. Resume the task [Add a DV certificate](#adding-an-ssl-certificate).

### Troubleshooting certificate errors {#certificate-errors}

Certain errors may arise if a certificate is not installed properly or does not meet the requirements of Cloud Manager.

+++**Correct certificate order**

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

    When adding a certificate, if you receive an error similar to the following:

    ```text
    The Subject of an intermediate certificate must match the issuer in the previous certificate. The SKI of an intermediate certificate must match the AKI of the previous certificate.
    ```

    You likely included the client certificate in the certificate chain. Make sure that the chain does not include the client certificate and try again.

+++

+++**Certificate policy**

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

+++**Certificate validity dates**

    Cloud Manager expects the SSL certificate to be valid for at least 90 days from the current date. Check the validity of the certificate chain.

+++

## Next steps {#next-steps}

You now have added a working SSL certificate for your project. This step is often the first to set up a custom domain name.

* To set up a custom domain name, see [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).
* To learn about updating and managing your SSL certificates in Cloud Manager, see [Manage SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md).
