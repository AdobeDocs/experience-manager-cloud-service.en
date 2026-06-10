---
title: Configure a Custom Domain for the Delivery Tier
description: Learn how to configure a custom domain for Delivery tier in Adobe Cloud Manager.
exl-id: cc71c8c5-cf42-4092-b0e0-646a2ed0ee54
---

# Configure a custom domain for the Delivery tier{#configure-custom-domain}

In Adobe Cloud Manager, you can make your website stand out by adding a custom domain. While AEM as a Cloud Service comes with a default domain, you can customize it as per your needs.

## Prepare yourself to get started

Ensure that you fulfil the following requirements before starting the configuration process:

* Access to Cloud Manager
* Already enabled Dynamic Media with OpenAPI on your environment through a support ticket
* EV or OV type certificate for the domain to be used for the delivery tier. See [Introduction to SSL certificates](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/introduction-to-ssl-certificates) for more details

## Configure custom domain in delivery tier using Cloud Manager

Execute the following steps in Cloud Manager to configure a custom domain in the delivery tier:

1. [Add a customer managed SSL certificate](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/add-ssl-certificate#add-customer-managed-ssl-cert).

2. [Add a custom domain name](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/custom-domain-names/add-custom-domain-name#adding-cdn-settings).

After completing the above steps, raise an Adobe Support ticket for custom domain mapping. Adobe performs the domain mapping for the custom domain as part of the support process.