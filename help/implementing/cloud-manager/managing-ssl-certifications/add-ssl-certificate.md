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

>[!NOTE]
>
>If you use a customer managed (OV/EV) SSL certificate and a customer managed CDN provider, you can skip adding an SSL certificate and go directly to [Add a CDN configuration](/help/implementing/cloud-manager/cdn-configurations/add-cdn-config.md) when ready.

Provisioning a certificate can take several days. Therefore, Adobe advises provisioning your own certificate well in advance of any deadline or go-live date to avoid delays.

To learn about updating and managing your SSL certificates in Cloud Manager, see [Manage SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md).

If you are having issues adding or managing your certificates, see [Troubleshoot SSL certificate errors](/help/implementing/cloud-manager/managing-ssl-certifications/troubleshoot-ssl-cert.md).


## Prerequisites {#prerequisites}

* A user must be a member of the **Business Owner** or **Deployment Manager** role to add an SSL certificate.
* If you are installing your own certificate, see **Certificate requirements** in [Introduction to Managing SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md#requirements).

## Choosing which SSL certificate to add {#which-ssl-to-add} 

After [adding a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) in AEM Cloud Manager, the next step depends on whether you chose to use an Adobe managed (DV) SSL certificate (recommended) or a customer managed (OV/EV) SSL certificate.

* **For an Adobe managed (DV) SSL certificate:**
    * The domain validation process is done once the custom domain is added and verified in Cloud Manager.
    * Now, you must [add an Adobe managed (DV) SSL certificate](#add-adobe-managed-ssl-cert).
    Once added to Cloud Manager, wait for Adobe to issue and install the DV SSL certificate on your behalf.
    * When the certificate is active, your custom domain is ready to use.

* **For a customer managed (OV/EV) SSL certificate:**

    * Obtain your OV/EV SSL certificate from a Certificate Authority. For more details, review the [requirements for customer managed OV/EV SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md#requirements).
    * After acquiring the certificate, [add your customer managed (OV/EV) SSL certificate's](#add-customer-managed-ssl-cert) details in Cloud Manager.
    * Once added, the custom domain name is marked as verified, and the SSL certificate is applied.

In either case, after the certificate is verified and installed, the custom domain is available for secure use in your environment. Make sure to [check the domain's status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) in the Cloud Manager interface regularly to confirm everything is working as expected.

See also [Introduction to SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md).

## Add an Adobe managed (DV) SSL certificate {#add-adobe-managed-ssl-cert}

Need help with choosing whether to use an Adobe managed SSL certificate (recommended) or a customer managed SSL certificate with your domain? See [Choosing which SSL certificate to add](#which-ssl-to-add)

**To add an Adobe managed (DV) SSL certificate:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.
1. In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the side menu. 

1. Under the **Services** heading, click ![Lock closed icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_LockClosed_18_N.svg) **SSL Certificates**. 

   ![Adding an SSL certificate](/help/implementing/cloud-manager/assets/ssl/ssl-cert-add.png)

1. Near the upper-right corner of the SSL Certificates page, click **Add SSL Certificate**.

1. In the **Add SSL certificate** dialog box, based on [your particular use case](#which-ssl-to-add), select **Adobe Managed (DV)**.

    ![Add a DV certificate](/help/implementing/cloud-manager/assets/ssl/add-dv-certificate.png)

1. In the **Certificate name** field, enter a name you want associated with the DV SSL certificate.

1. In the **Select domains** drop-down list, select one or more verified domains that you want associated with the DV SSL certificate.
    * No domains to select? If so, you must first [add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) and ensure it is verified before you can add an Adobe managed SSL certificate.
    * When you are finished adding a custom domain name, return to this topic and begin at step 1 again.
    
1. In the lower-right corner of the dialog box, click **Save**.

    After the SSL certificate is successfully issued, it is displayed with a green Valid check mark in the **SSL Certificates** table. 

You now have added a working Adobe managed DV SSL certificate for your project. This step is often the first to set up a custom domain name.

You are now ready to add a [CDN configuration](/help/implementing/cloud-manager/cdn-configurations/add-cdn-config.md).

## Add a customer managed (OV/ED) SSL certificate {#add-customer-managed-ssl-cert}

<!-- IF THIS TOPIC GET UPDATED, REMEMBER TO UPDATE THE STEPS ALSO IN THE "MANAGE SSL CERTIFICATES TOPIC TOO -->

Need help with choosing whether to use an Adobe managed SSL certificate (recommended) or a customer managed SSL certificate with your domain? See [Choosing which SSL certificate to add](#which-ssl-to-add) 

**To add a customer managed (OV/EV) SSL certificate:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate program.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the side menu. 

1. Under the **Services** heading, click ![Lock closed icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_LockClosed_18_N.svg) **SSL Certificates**. 

   ![Adding an SSL certificate](/help/implementing/cloud-manager/assets/ssl/ssl-cert-add.png)

1. Near the upper-right corner of the SSL Certificates page, click **Add SSL Certificate**.

1. In the **Add SSL certificate** dialog box, based on [your particular use case](#which-ssl-to-add), select **Customer managed (OV/EV)**.

1. In the **Certificate name** field, enter a name for your certificate. 
    This field is for informational purposes only and can be any name that helps you reference your SSL certificate easily.

1. In the **Certificate**, **Private key**, and **Certificate chain** fields, copy the required values from your OV or EV SSL certificate, and paste them into their respective fields in the dialog box.

    Any detected errors in values are displayed. Before you can save your certificate, you must address all errors. See [Certificate Errors](#certificate-errors) to learn more about troubleshooting common errors.

    ![Add SSL certificate dialog box](/help/implementing/cloud-manager/assets/ssl/ssl-cert-02.png)| 

1. In the lower-right corner of the dialog box, click **Save**.

    >[!NOTE]
    >
    >* If you selected **Customer managed certificate** while [adding a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md), the domain is verified ***after*** the customer managed (OV/EV) SSL certificate is added and saved. See also [Check the status of a custom domain name](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md#how-to).

    After the SSL certificate is successfully issued, it is displayed with a green verified check mark in the **SSL Certificates** table. 

You now have added a working SSL certificate for your project. This step is often the first to set up a custom domain name.

You are now ready to add a [CDN configuration](/help/implementing/cloud-manager/cdn-configurations/add-cdn-config.md).
    






















<!--
## Add an SSL certificate {#add-ssl-cert}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.
1. In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the side menu. 
1. Under the **Services** heading, click ![Lock closed icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_LockClosed_18_N.svg) **SSL Certificates**. 

   ![Adding an SSL certificate](/help/implementing/cloud-manager/assets/ssl/ssl-cert-add.png)

1. Near the upper-right corner of the SSL Certificates page, click **Add SSL Certificate**.

1. In the **Add SSL certificate** dialog box, based on [your particular use case](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md), do one of the following:

    | | Use case | Steps |
    | --- | --- | --- |
    | 1 | **Add an Adobe managed (DV) certificate** | **To add an Adobe managed (DV) SSL certificate:**<br>a. In the **Add SSL Certificate** dialog box, select the certificate type **Adobe managed (DV)**.<br>![Add a DV certificate](/help/implementing/cloud-manager/assets/ssl/add-dv-certificate.png)<br>b. In the **Certificate name** field, enter a name you want associated with the certificate.<br>c. In the **Select domains** drop-down list, select one or more domains that you want associated with the DV SSL certificate.<br>No domains to select? If so, it means that you must first add a custom domain name and ensure it is verified before you can add an SSL certificate. See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). When you are finished adding a custom domain name, return to this topic and begin at step 1 again.<br>d. Continue to step 7. |
    | 2 | **Add a customer managed (OV/EV) certificate** | **To add a customer managed (OV/EV) SSL certificate:**<br>a. In the **Add SSL Certificate** dialog box, select the certificate type **Customer managed (OV/EV)**.<br>b. In the **Certificate name** field, enter a name for your certificate. This field is for informational purposes only and can be any name that helps you reference your SSL certificate easily.<br>c. In the **Certificate**, **Private key**, and **Certificate chain** fields, paste the required values into their respective fields.<br>![Add SSL certificate dialog box](/help/implementing/cloud-manager/assets/ssl/ssl-cert-02.png)<br>Any detected errors in values are displayed. Before you can save your certificate, you must address all errors. See [Certificate Errors](#certificate-errors) to learn more about troubleshooting common errors.<br>d. Continue to step 7. | 

1. In the lower-right corner of the dialog box, click **Save**.

    >[!NOTE]
    >
    >* If you selected **Adobe managed certificate** while [adding a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md), the domain is verified with the added certificate when the custom domain is added. 
    >
    >* If you selected **Customer managed certificate** while [adding a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md), the domain is verified ***after*** the customer managed (OV/EV) SSL certificate is added and saved. See also [Check the status of a custom domain name](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md#how-to).

    After the SSL certificate is successfully issued, it is displayed with a green verified check mark in the **SSL Certificates** table. 

    You now have added a working SSL certificate for your project. This step is often the first to set up a custom domain name. 
    

* To learn about updating and managing your SSL certificates in Cloud Manager, see [Manage SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md).

* If you are having issues adding or managing your certificates, see [Troubleshoot SSL certificate errors](/help/implementing/cloud-manager/managing-ssl-certifications/troubleshoot-ssl-cert.md). -->
