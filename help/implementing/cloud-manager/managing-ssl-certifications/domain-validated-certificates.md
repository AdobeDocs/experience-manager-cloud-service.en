---
title: Domain Validated (DV) Certificates
description: Learn how to manage domain validated (DV) certificates in Cloud Manager.
exl-id: 7f2c71b6-15c3-4919-9f51-a3e26d0d48d4
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Domain Validated (DV) Certificates {#domain-validated-certificates}

Learn how to manage domain validated (DV) certificates in Cloud Manager.

>[!NOTE]
>
>This feature is only available to [the early adopter program.](/help/implementing/cloud-manager/release-notes/current.md#early-adoption)


## Introduction {#introduction}

<!-- The content of this introduction was moved into introduction.md found under the managing-ssl-certifications folder

Cloud Manager allows you to self-service generate and manage a domain validated (DV) SSL certificate. This gives you the fastest, easiest, and most cost-effective solution to create a secure website for your online business.

Domain validated certificates are available to both [production and sandbox programs.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md) -->



## Add a custom domain name {#adding-domain}

<!-- The content of this step topic was incorporated into add-ssl-certificate.md.

Before you can add a Domain Validated (DV) certificate, you must first add your custom domain. The process is nearly the same as detailed in [Introduction to Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/introduction.md) and . However, that functionality is now slightly expanded, as described below.

1. When verifying the domain, you can choose to use Adobe-manged or self-managed certificates with the domain. Select **Adobe managed certificate** so you can add a DV certificate later.

   ![Choose Adobe-managed](assets/verify-domain-dialog.png)

1. To use an Adobe managed certificate, add a CNAME record to your DNS as described in the **Verify domain** dialog.

   ![Add CNAME entry](assets/verify-domain-dialog-adobe-managed.png)

1. Once the domain is created, tap or click the ellipsis button in the list of domains and select **Verify** to verify the domain.

   ![Verify domain](assets/verify-domain.png) -->

## Add a DV certificate {#adding}

<!-- The content of this step topic was incorporated into add-ssl-certificate.md.

Once you have your domain correctly configured, to add a DV certificate, tap or click the **Add SSL certificate** button in the SSL Certificates window.

![Adding a DC certificate](/help/implementing/cloud-manager/assets/ssl/add-dv-certificate.png)

1. Select **Adobe managed (DV)**.
1. Specify the domain name in the **Select domains** drop down.
1. Tap or click **Save**.

Once successfully added the certificate will have a pending status with a yellow warning sign to its name in the **SSL Certificates** window.

![Pending DV cert](assets/pending-dv-certificate.png)

Once successfully issued the certificate will have a green check mark to its name in the **SSL Certificates** window.

![Issued DV cert](assets/issued-dv-certificate.png)

For more information about adding SSL certificates and the SSL Certificates window, see [Add an SSL certificate](#add-ssl-certificate.md). -->

## Add CDN configuration {#add-cdn}

This step must be completed to configure a domain with a SSL using Fastly CDN.

Follow these steps to add a CDN configuration using Cloud Manager.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click **CDN Configurations**.

1. Near the upper-right corner of the CDN Configurations page, click **Add**. 

1. In the **Configure CDN** dialog box, provide the necessary information.

   * From the **Origin** drop-down list, do one of the following:
     * **Sites:** Select an Edge Delivery Services site.
     * **Environment:** Select a Cloud Service environment.
   * Select your CDN type: **Adobe managed CDN** or **Other CDN provider**.
   * Select the domain.
   * Select the SSL certificate. Only required if you selected **Adobe managed CDN** as your CDN type.

   ![Configure CDN dialog box](assets/configure-cdn-dialog.png)

>![NOTE]
>
>For Adobe-managed CDNs, when using DV certificates, only sites with ACME validation are permitted.
