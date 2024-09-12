---
title: Add a CDN Configuration
description: Learn about how to add a CDN configuration for an Edge Delivery site or a Cloud Manager environment.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
exl-id: 672513d7-ee0a-4f6e-9ef0-7a41fabbaf9a
---

# Add a CDN configuration {#add-cdn}

To link a domain with an SSL certificate on the Adobe-managed CDN within your program, you must add a CDN (Content Delivery Network) configuration.

For Adobe managed CDNs, when using DV certificates, only sites with ACME validation are permitted. 

>[!IMPORTANT]
>
>Have you [added a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) and [added an SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md), respectively? If not, you must complete these two tasks before you can add a CDN configuration.

**To add a CDN configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. In the left navigation panel, under **Services**, click **CDN Configurations**.

1. Near the upper-right corner of the CDN Configurations page, click **Add**. 

   ![Configure CDN dialog box](/help/implementing/cloud-manager/assets/configure-cdn-dialog.png)

1. In the **Configure CDN** dialog box, in the **Origin** drop-down list, select one of the following:

   | Origin | Description |
   | --- | --- |
   | Sites | Select an Edge Delivery site. |
   | Environment | Select a specific Cloud Service environment that you want to target within your AEM setup.<br>In the **Tier** drop-down list, select one of the following:<br>&bull; Select **Publish** to target a live, production environment where content is delivered to end users.<br>&bull; Select **Preview** for staging or non-production environments where you test changes before they go live. |

1. Select your CDN type by choosing one of the following:

   | CDN type | Description |
   | --- | --- |
   | Adobe managed CDN | a. In the **Domain** drop-down list, select the domain name that you want to use.<br>No verified domains available in the drop-down list? See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).<br>b. In the SSL Certificate drop-down list, select a certificate that you want to use.<br>No SSL certificates available in the drop-down list? See [Add an SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md). |
   | Other CDN provider. | Select this option if you are using your own CDN provider and not the Adobe managed CDN that is available to you.<br>In the **Domain** drop-down list, select the domain name that you want to use.<br>No available SSL certificates in the drop-down list? See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). |

1. Click **Save**.
