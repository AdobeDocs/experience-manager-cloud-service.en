---
title: Configure a Custom Domain for the Publish Tier
description: Learn how to configure a custom domain for publish tier in Adobe Cloud Manager.
exl-id: cc71c8c5-cf42-4092-b0e0-646a2ed0ee54
---
# Configure a custom domain for the publish tier{#configure-custom-domain}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

>[!AVAILABILITY]
>
>Dynamic Media with OpenAPI capabilities guide is now available in PDF format. Download the entire guide and use Adobe Acrobat AI Assistant to answer your queries. 
>
>[!BADGE Dynamic Media with OpenAPI capabilities Guide PDF]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/dynamic-media-with-openapi-capabilities.pdf"}

In Adobe Cloud Manager, you can make your website stand out by adding a custom domain. While AEM as a Cloud Service comes with a default domain, you can customize it as per your needs.

## Before you begin

* You must have a multi-SAN (Subject Alternative Name) TLS or SSL certificate.
* The SSL certificate should have distinct SANs against the certificate mapped for the publish tier within the same domain.
* The certificate policy must adhere to either Extended Validation (EV) or Organization Validation (OV), and not Domain Validation (DV) policy.


## Configure a custom domain for the publish tier

1. Go to **[!UICONTROL Adobe Cloud Manager]** > **[!UICONTROL Program Overview]** > **[!UICONTROL SSL Certificates]**, and add your SSL certificate. 
 ![image](/help/assets/assets/ssl-certificate.png)
Learn how to add [SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) in Adobe Cloud Manager.

1. After adding the SSL certificate, add a custom domain. Click **[!UICONTROL Domain Settings]** and specify the custom domain against the **[!UICONTROL Publish service]** option.
Learn more about [custom domain](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).

1. Add two [CNAME records](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) in your DNS record corresponding to publish domains. 
DNS verification can take a few hours to process because of DNS propagation delays.

1. Log a support case to facilitate the configuration of the custom domain, ensuring it directs to the delivery tier.

>[!NOTE]
>
>Add the custom domain to the allowed redirect URLs list. The list is in the IMS client for the asset selector.<br>Coordinate with the respective Adobe team to execute this task by providing the custom domain string.
