---
title: Configure a Custom Domain for the Delivery Tier
description: Learn how to configure a custom domain for Delivery tier in Adobe Cloud Manager.
exl-id: cc71c8c5-cf42-4092-b0e0-646a2ed0ee54
---

# Configure a custom domain for the Delivery tier{#configure-custom-domain}

In Adobe Cloud Manager, you can make your website stand out by adding a custom domain. While AEM as a Cloud Service comes with a default domain, you can customize it as per your needs.

>[!NOTE]
>
>Customers with Dynamic Media Prime or Dynamic Media Ultimate licenses must use the self-service custom domain configuration available in Cloud Manager.
>Refer to [Dynamic Media Prime and Ultimate documentation](/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md#configure-custom-domain-in-delivery-tier) for details.
>
>Customers using older Dynamic Media setups where Dynamic Media with OpenAPI is enabled manually should follow this documentation. For these setups, custom domain mapping is completed through an Adobe Support request.

## Prepare yourself to get started

Ensure that you fulfil the following requirements before starting the configuration process:

* Access to Cloud Manager
* Already enabled Dynamic Media with OpenAPI on your environment through a support ticket
* EV or OV type SSL certificate for the domain used in the delivery tier. See [Introduction to SSL certificates](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/introduction-to-ssl-certificates) for more details

## Configure custom domain in delivery tier using Cloud Manager

Execute the following steps in Cloud Manager:

1. [Add a customer managed SSL certificate](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-ssl-certificates/add-ssl-certificate#add-customer-managed-ssl-cert)

2. [Add a custom domain name](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/custom-domain-names/add-custom-domain-name#adding-cdn-settings)

After completing the above steps, raise an Adobe Support ticket for custom domain mapping. Adobe performs the domain mapping as part of the support process.

**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

