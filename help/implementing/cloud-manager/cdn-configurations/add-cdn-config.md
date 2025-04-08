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

For Adobe managed CDNs, when using a DV SSL certificate, only sites with ACME validation are permitted. 

>[!IMPORTANT]
>
>Have you [added a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) and [added an SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md), respectively? If not, you must complete these two tasks before you can add a CDN configuration.

See also [Adobe Managed CDN](https://www.aem.live/docs/byo-cdn-adobe-managed).

**To add a CDN configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Depending on your use case, do one of the following:

   | Use case | Steps |
   | --- | --- |
   | I want to add a CDN configuration to an *existing* Edge Delivery site in Cloud Manager | a. In the left side menu, under **Services**, click ![Webpages icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_WebPages_18_N.svg) **Edge Delivery Sites**.<br>b. In the Edge Delivery table, at the end of a row that does not have a domain associated with it, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg).<br>c. Click **Configure CDN**. |
   | I want to add a CDN configuration in Cloud Manager | a. In the left side menu, under **Services**, click ![Social network icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_SocialNetwork_18_N.svg) **Domain Mappings**.<br>b. Near the upper-right corner of the Domain Mappings page, click **Add**.   |

1. In the **Configure CDN** dialog box, in the **Origin** drop-down list, select one of the following:

   ![Configure CDN dialog box](/help/implementing/cloud-manager/assets/configure-cdn-dialog.png)

   | Origin | Description |
   | --- | --- |
   | Sites | Select an Edge Delivery site. |
   | Environment | Select a specific Cloud Service environment that you want to target within your AEM setup.<br>In the **Tier** drop-down list, select one of the following:<br>&bull; Select **Publish** to target a live, production environment where content is delivered to end users.<br>&bull; Select **Preview** for staging or non-production environments where you test changes before they go live. |

1. Select your CDN type and associated configuration by selecting one of the following:

   | CDN type | Configuration details |
   | --- | --- |
   | Adobe managed CDN | Under **Configuration details**, do the following:<br>a. In the **Domain** drop-down list, select the domain name that you want to use.<br>No verified domains available in the drop-down list? See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).<br>b. In the **SSL certificate** drop-down list, select a certificate that you want to use.<br>No SSL certificates available in the drop-down list? See [Add an SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md). |
   | Other CDN provider | Select this option if you are using your own CDN provider and not the Adobe managed CDN that is available to you.<br>Under **Configuration details**, in the **Domain** drop-down list, select the domain name that you want to use.<br>No verified domains available in the drop-down list? See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). |

1. Click **Save**.
