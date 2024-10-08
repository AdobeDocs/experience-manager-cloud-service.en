---
title: Add an SSL Certificate
description: Learn how to add your own SSL certificate or and Adobe managed DV (Domain Validation) certificate using Cloud Manager's self-service tools.
exl-id: 104b5119-4a8b-4c13-99c6-f866b3c173b2
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Add an SSL certificate {#add-ssl-cert}

Learn how to add your own SSL certificate or and Adobe managed DV (Domain Validation) certificate using Cloud

>[!TIP]
>
>A certificate can take a few days to provision. As such, Adobe recommends that if you are providing your own certificate, that it be provisioned well in advance of any deadline or go-live date.

## Prerequisites {#prerequisites}

* A user must be a member of the **Business Owner** or **Deployment Manager** role to add a certificate.
* If you are installing your own certificate, be sure to review **Certificate requirements** in [Introduction to Managing SSL Certificates.](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md#requirements)

## Adding an SSL certificate {#add-certificate}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.
1. In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the side menu. 
1. Under the **Services** heading, click ![Lock closed icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_LockClosed_18_N.svg) **SSL Certificates**. 

   ![Adding an SSL certificate](/help/implementing/cloud-manager/assets/ssl/ssl-cert-add.png)

1. Near the upper-right corner of the SSL Certificates page, click **Add SSL Certificate**.

1. In the **Add SSL certificate** dialog box, based on [your particular use case](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md), do one of the following:

    | | Use case | Steps |
    | --- | --- | --- |
    | 1 | **Add an Adobe managed (DV) certificate** | **To add an Adobe managed (DV) certificate:**<br>a. In the **Add SSL Certificate** dialog box, select the certificate type **Adobe managed (DV)**.<br>![Add a DV certificate](/help/implementing/cloud-manager/assets/ssl/add-dv-certificate.png)<br>b. In the **Certificate name** field, enter a name you want associated with the certificate.<br>c. In the **Select domains** drop-down list, select one or more domains that you want associated with the DV certificate.<br>No domains to select? If so, it means that you must add a custom domain. See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). When you are finished adding a custom domain name, return to this topic and begin at step 1 again.<br>d. Continue to step 7. |
    | 2 | **Add a customer managed (OV/EV) certificate** | **To add a customer managed (OV/EV) certificate:**<br>a. In the **Add SSL Certificate** dialog box, select the certificate type **Customer managed (OV/EV)**.<br>b. In the **Certificate name** field, enter a name for your certificate. This field is for informational purposes only and can be any name that helps you reference your certificate easily.<br>c. In the **Certificate**, **Private key**, and **Certificate chain** fields, paste the required values into their respective fields.<br>![Add SSL certificate dialog box](/help/implementing/cloud-manager/assets/ssl/ssl-cert-02.png)<br>Any detected errors in values are displayed. Before you can save your certificate, you must address all errors. See [Certificate Errors](#certificate-errors) to learn more about troubleshooting common errors.<br>d. Continue to step 7. | 

1. In the lower-right corner of the dialog box, click **Save**.

After the certificate is successfully issued, it is displayed with a green check mark in the **SSL Certificates** table.

You now have added a working SSL certificate for your project. This step is often the first to set up a custom domain name.

* To set up a custom domain name, see [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).
* To learn about updating and managing your SSL certificates in Cloud Manager, see [Manage SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md).

>[!TIP]
>
>If you are having issues adding or managing your certificates, please see the document [Troubleshoot SSL certificate errors.](/help/implementing/cloud-manager/managing-ssl-certifications/troubleshoot-ssl-cert.md)
