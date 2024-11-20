---
title: Integrate remote AEM Assets with AEM Sites
description: Learn how to configure and connect AEM sites  with Approved AEM Assets.
exl-id: 382e6166-3ad9-4d8f-be5c-55a7694508fa
---
# Integrate remote AEM Assets with AEM Sites  {#integrate-approved-assets}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

>[!AVAILABILITY]
>
>Dynamic Media with OpenAPI capabilities guide is now available in PDF format. Download the entire guide and use Adobe Acrobat AI Assistant to answer your queries. 
>
>[!BADGE Dynamic Media with OpenAPI capabilities Guide PDF]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/dynamic-media-with-openapi-capabilities.pdf"}

Effectively managing digital assets is crucial for delivering engaging and consistent brand experiences across various online platforms. Dynamic Media with OpenAPI capabilities enhances digital asset management by enabling seamless integration between AEM Sites and AEM Assets as a Cloud Service. This innovative feature allows you to easily share and manage different types of approved digital assets across multiple AEM environments, streamlining workflows for sites authors and content editors.

Dynamic Media with OpenAPI capabilities allows sites authors to use assets from remote DAM directly within the AEM Page Editor and [Content Fragment](https://experienceleague.adobe.com/docs/experience-manager-65/content/assets/content-fragments/content-fragments.html), simplifying content creation and management processes.

Users can connect multiple AEM Sites instances, without any restrictions on the maximum number, to a remote DAM deployment, a notable advantage over the [Connected Assets](use-assets-across-connected-assets-instances.md) feature.

 ![image](/help/assets/assets/connected-assets-rdam.png)

After the initial setup, users can create pages on the AEM Sites instance and add assets as needed. When adding assets, they can either select assets stored in their local DAM or browse and use the assets available in the remote DAM.

Dynamic Media with OpenAPI capabilities offers several other benefits such as accessing and using remote assets in Content Fragment, fetching metadata of the remote assets and much more. Know more about the other [benefits of Dynamic Media with OpenAPI capabilities over Connected Assets](/help/assets/dynamic-media-open-apis-faqs.md). 

## Before you begin {#pre-requisites-sites-integration}

Support for remote assets using Dynamic Media with OpenAPI capabilities requires:

* AEM 6.5 SP 18+ or AEM as a Cloud Service

* Core Components release 2.23.2 or later

* Set up the following [environment variables](/help/implementing/cloud-manager/environment-variables.md#add-variables) for AEM as a Cloud Service:

    * ASSET_DELIVERY_REPOSITORY_ID= "delivery-pxxxxx-eyyyyyy.adobeaemcloud.com" <br>
    `pXXXX` refers to the program ID <br>
    `eYYYY` refers to the environment ID

    These variables are set using Cloud Manager user interface of the AEM as a Cloud Service environment acting as your local Sites instance. 

    * ASSET_DELIVERY_IMS_CLIENT= [IMSClientId]: You need to submit an Adobe support ticket to get the IMS Client ID.

      or configure the [OSGi settings](https://experienceleague.adobe.com/docs/experience-manager-65/content/implementing/deploying/configuring/configuring-osgi.html) for AEM 6.5 in the AEM Sites instance by following these steps:
    
    1. Sign in to the console and click **[!UICONTROL OSGi] >** or
    use the direct URL; for example: `https://localhost:4502/system/console/configMgr`

    1. Configure the **Next Generation Dynamic Media Config** (`NextGenDynamicMediaConfigImpl`) OSGi configuration as follows, replacing the values with those of your remote assets environment.

       ```text
         imsClient="<ims-client-ID>"
         enabled=B"true"
         imsOrg="<ims-org>@AdobeOrg"
         repositoryId="<repo-id>.adobeaemcloud.com"
       ```

       `imsOrg` is not a mandatory input.
       `repositoryId` = "delivery-pxxxxx-eyyyyyy.adobeaemcloud.com" 
        where `pXXXX` refers to the program ID 
        `eYYYY` refers to the environment ID

       ![The Next Generation Dynamic Media Config OSGi configuration window](/help/assets/assets/remote-assets-osgi.png)

    Learn more about [IMS authentication](https://experienceleague.adobe.com/docs/experience-manager-65/content/security/ims-config-and-admin-console.html).

    For details on how to configure OSGi, please see the following documents:

   * [Configuring OSGi for Adobe Experience Manager as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-osgi.html) for AEM as a Cloud Service
   * [Configuring OSGi](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/configuring/configuring-osgi.html) for AEM 6.5

* IMS access to sign into remote DAM AEM as a Cloud Service instance. It refers to the Sites author that has IMS access to the remote DAM environment.

* Configure the Image v3 component in the AEM Sites instance. If the component is not present, download and install the [content package](https://github.com/adobe/aem-core-wcm-components/releases/tag/core.wcm.components.reactor-2.23.0).

## Configure HTTPS {#https}

It is generally recommended to run all of your production AEM instances using HTTPs. However your local development environments may not be set up as such. However, remote assets using Dynamic Media with OpenAPI requires HTTPS in order to function.

[Use this guide](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/security/use-the-ssl-wizard.html) to configure HTTPS wherever you wish to use remote assets, including development environments.

## Access assets from Remote DAM {#fetch-assets}

Dynamic Media with OpenAPI capabilities allows you to access assets available in your Remote DAM instance on your local AEM Sites Page Editor and AEM Content Fragment.

![image](/help/assets/assets/open-APIs.png)

### Access remote assets in AEM Page Editor {#access-assets-page-editor}

Follow the below steps to use remote assets within AEM Page Editor on your AEM Sites instance. You can do this integration in AEM as a Cloud Service and AEM 6.5.

1. Go to **[!UICONTROL Sites]** > _your website_ where the AEM **[!UICONTROL Page]** is present within which you need to add the remote asset.
1. Select the page and click **[!UICONTROL Edit (_e_)]**. The AEM **[!UICONTROL Page Editor]** opens.
1. Click the Layout Container and add an **[!UICONTROL Image]** component.   
1. Click the **[!UICONTROL Image]** component and click ![settings icon](/help/assets/assets/do-not-localize/settings-icon.svg) icon.
1. Uncheck the **[!UICONTROL Inherit featured image from page]** option. 
1. Click **[!UICONTROL Pick]** and select **[!UICONTROL Remote]**.
    ![image](/help/assets/assets/uncheck-inherit-option.jpg)

    You are prompted to sign in.
1. Select the asset and click **[!UICONTROL Select]**.
1. Add an Alternative text and click **[!UICONTROL Done]**.
<br> The remote asset appears in the image component. You can also verify the delivery URL of the asset when it loads on the page or by using the 'Preview' tab. The delivery URL indicates that the asset is being accessed remotely.

You can access remote assets in AEM page editor out-of-the-box only for Image Core Component v3 and Teaser Core Component v2. For other components including custom components, customizations are required to integrate Asset Selector with those components.

#### Video: Access remote assets in AEM Page Editor

>[!VIDEO](https://video.tv.adobe.com/v/3427666)

### Access remote assets in AEM Content Fragment {#access-assets-content-fragment}

Follow the below steps to use Remote assets within AEM Content Fragment on your AEM Sites instance. You can do this integration in AEM 6.5 and not on AEM as a Cloud Service.

1. Go to **[!UICONTROL Assets]** > **[!UICONTROL Files]**.
1. Select asset folder where the Content Fragment is present.
1. Select the Content Fragment and click **[!UICONTROL Edit (_e_)]**. 

    >[!NOTE]
    >
    >If you don't have AEM Content Fragment model, you may need to [create one](https://experienceleague.adobe.com/docs/experience-manager-65/content/assets/content-fragments/content-fragments-models.html?lang=en).
    
1. Click the ![checkmark icon](/help/assets/assets/do-not-localize/checkmark-icon.svg) icon next to the text component.
1. Select **[!UICONTROL Remote]** to fetch the asset from the Remote DAM. <br>
You can either choose **[!UICONTROL Local]** or **[!UICONTROL Remote]** DAM repository based on your need. 
    
    ![image](/help/assets/assets/cf-pick.jpg)
    You are prompted to sign in.
1. Choose the asset and click **[!UICONTROL Select]**.
<br> The remote asset URL appears in the text component.

#### Video: Access remote assets in AEM Content Fragment

>[!VIDEO](https://video.tv.adobe.com/v/3427667)

### Access remote assets in Edge Delivery Services {#access-assets-eds}

You can also access remote assets in Edge Delivery Services. For more information, see [Utilizing assets from Assets as a Cloud Service delivered using Dynamic Media with OpenAPI capabilities](https://www.aem.live/docs/aem-assets-sidekick-plugin#utilizing-assets-from-assets-cloud-services-delivered-via-dynamic-media-with-openapi).
