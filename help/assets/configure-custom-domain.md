---
title: Configure custom domain for publish tier
description: Learn how to configure custom domain for publish tier in Adobe Cloud Manager. 
role:
---

# Configure custom domain for publish tier{#configure-custom-domain}

In Adobe Cloud Manager, you can make your website stand out by adding a custom domain. While AEM as a Cloud Service comes with a default domain, you can customize it as per your needs.

## Before you begin

* You must have a multi-SAN (Subject Alternative Name) TLS or SSL certificate.
* The SSL certificate should have distinct SANs against the certificate mapped for the publish tier within the same domain.
* The certificate policy must adhere to either Extended Validation (EV) or Organization Validation (OV), and not Domain Validation (DV) policy.


## Add custom domain

To configure a custom domain for the publish tier, follow these steps:

1. Go to **[!UICONTROL Adobe Cloud Manager]** > **[!UICONTROL Program Overview]** > **[!UICONTROL SSL Certificates]**, and add your SSL certificate. 
 ![image](/help/assets/assets/ssl-certificate.png)
Learn how to add [SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) in Adobe Cloud Manager.

1. After adding the SSL certificate, add a custom domain. Click **[!UICONTROL Domain Settings]** and specify the custom domain against the **[!UICONTROL Publish service]** option.
Learn more about [custom domain](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).

1. Add 2 [CNAME records](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md) in your DNS record corresponding to publish domains. 
DNS verification can take a few hours to process because of DNS propagation delays.

1. Log a support case to facilitate the configuration of the custom domain, ensuring it directs to the delivery tier.

>[!NOTE]
>
> Make sure to add the custom domain to the list of allowed redirect URLs in the IMS client for the asset selector.<br>Coordinate with the respective Adobe team to execute this task by providing the custom domain string.
