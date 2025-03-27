---
title: Restrict delivery of assets with Dynamic Media with OpenAPI capabilities
description: Learn how to restrict the assets delivery with OpenAPI capabilities.
role: User
exl-id: 3fa0b75d-c8f5-4913-8be3-816b7fb73353
---
# Restrict delivery of assets with Dynamic Media with OpenAPI capabilities {#restrict-access-to-assets}

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

Central asset governance in Experience Manager allows the DAM Admin or Brand Managers to manage access to assets available through Dynamic Media with OpenAPI capabilities. They can restrict delivery of approved assets (down to an individual asset) to selected [Adobe Identity Management System (IMS) User or Groups](https://helpx.adobe.com/in/enterprise/using/users.html#user-mgt-strategy) by configuring certain metadata on assets on their the AEM as a Cloud Service author service.

Once an asset is restricted through Dynamic Media with OpenAPIs, only the (Adobe IMS onboarded) users authorized to access the said asset are granted access. To access the asset, the user must leverage [Search](search-assets-api.md) and [Delivery](deliver-assets-apis.md) capabilities of Dynamic Media with OpenAPI.

![Restricted access to assets](/help/assets/assets/restricted-access.png)

In Experience Manager Assets, restricted delivery via IMS involves two key stages: 

* Authoring 
* Delivery

## Authoring {#authoring}

### Restricted delivery using an IMS Bearer token {#restrict-delivery-ims-token}

You can restrict the delivery of assets within [!DNL Experience Manager] based on IMS User and Group Identities .

>[!NOTE]
>
> This capability is currently not self-service. To restrict asset delivery for IMS [Users](https://helpx.adobe.com/in/enterprise/using/manage-directory-users.html) and [Groups](https://helpx.adobe.com/in/enterprise/using/user-groups.html), reach out to your Enterprise Support team for guidance on how to retrieve the information required for restricting access from [Adobe Admin Console](https://adminconsole.adobe.com/) portal and how to configure access in the AEM as a Cloud Service author service.

### Restrict delivery of assets using On and Off date and time {#restrict-delivery-assets-date-time}

DAM authors can also restrict the delivery of assets by defining an On or Off time for activation available in Asset properties.

If you define an On time for activation of an asset, a delivery URL gets generated for the asset at the defined time. The asset remains inactive before the defined time. Similarly, if you define an Off time for an asset, the asset is deactivated at the defined time and the delivery URL for the asset stops displaying the asset.

Execute the following steps to set the On and Off time for the asset:

1. Select the asset and click **[!UICONTROL Properties]**.

1. In the **[!UICONTROL Scheduled (de) activation]** section of the **[!UICONTROL Basic]** tab, define the On Time or the Off Time based on your requirements.

Similarly, in Assets view, you can select the asset and click **[!UICONTROL Details]** to view asset properties and define On time and Off time.

The field is available in the default metadata form. If your asset is not based on the default metadata schema and the On Time and Off Time fields are not available in the asset properties, execute the following steps in Admin view:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
1. Select the metadata schema and click **[!UICONTROL Edit]**.
1. Add a **[!UICONTROL Date]** field from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form. 
1. Click the newly added field, and then do the following updates in the  **[!UICONTROL Settings]** panel:
   1. Change the **[!UICONTROL Field Label]** to **On Time** or **Off Time**.
   1. Update the **[!UICONTROL Map to property]** to _./jcr:content/onTime_ for **On Time** field and _./jcr:content/offTime_ for **Off Time** field.
1. Click **[!UICONTROL Save]**.

Similarly, for Assets view, if your asset is not based on the default metadata schema and the On Time and Off Time fields are not available in the asset properties, execute the following steps:

1. Click **[!UICONTROL Metadata Forms]** in the **[!UICONTROL Settings]** section. 
1. Select the metadata form and click **[!UICONTROL Edit]**. 
1. Add a **[!UICONTROL Date]** field from the **[!UICONTROL Components]** section in left pane to the form. 
1. Click the newly added field and change the **[!UICONTROL Label]** to **On Time** or **Off Time**.
1. Update the **[!UICONTROL Metadata property]** to _./jcr:content/onTime_ for **On Time** field and _./jcr:content/offTime_ for **Off Time** field.
1. Click **[!UICONTROL Save]**. 



## Delivery of restricted assets {#delivery-restricted-assets}

The delivery of restricted assets is based on successful authorization to access assets. The authorization is either through [IMS Bearer Tokens](https://developer.adobe.com/developer-console/docs/guides/authentication/UserAuthentication/IMS/) (application for requests initiated from [AEM Asset Selector](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/asset-selector/overview-asset-selector)), or a secure-cookie (if you have custom identity providers set up on your AEM Publish/Preview services, and have set up the cookie creation and inclusion on the pages).

### Delivery for AEM author or Asset Selector requests {#delivery-aem-author-asset-selector}

To enable the delivery of restricted assets in case the request is sent from AEM author service or AEM Asset Selector, a valid IMS Bearer token is essential.  
On AEM Cloud Service author services as well as Asset Selector, the IMS Bearer Token is automatically generated and used for requests after a successful login.

>[!NOTE]
>
>To get more information on how to enable IMS authentication on AEM Asset Selector based integrations, reach out to Enterprise Support

1. For non-Asset Selector based experiences, AEM as a Cloud Service and Dynamic Media with OpenAPI capabilities currently support server-side-api integrations and can generate IMS Bearer tokens.
   * Follow the instructions [here](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis#the-server-to-server-flow) to perform service-to-server API integrations that can retrieve the IMS Bearer tokens through [AEM as a Cloud Service Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines#crxde-lite-and-developer-console)
   * For limited duration, local developer access (not meant for production use cases), short-lived IMS Bearer tokens for the user authenticated on [AEM as a Cloud Service Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines#crxde-lite-and-developer-console) can be generated by following the instructions [here](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis#developer-flow)

1. While making [Search](search-assets-api.md) and [Delivery](deliver-assets-apis.md) API requests, add the obtained IMS Bearer token to the **[!UICONTROL Authorization]** header of the HTTP request (ensure that its value is prefixed with **[!UICONTROL Bearer]**).

1. To validate the access restriction, initiate a Delivery API request with and without the **[!UICONTROL Authorization]** header.
   * The response will yield a `404` error status-code in cases where there is no IMS Bearer token, or the provided IMS Bearer token doesn't belong to the user that was granted access to the asset (either directly, or through group membership).
   * The response will yield a `200` success status-code with the binary content of the asset if the IMS Bearer token is one of the user or groups that were granted access to the asset.

### Delivery for custom identity providers on Publish service {#delivery-custom-identity-provider}

AEM Sites, AEM Assets and Dynamic Media with OpenAPI licenses can be used together, allowing for restricted delivery of assets to be configured on websites hosted on AEM Publish or Preview service. The secure delivery flow leverages browser cookies to establish user's access and having a custom domain for delivery tier that is subdomain of the publish domain is a pre-requisite for implementing this use case. In case AEM Sites' Publish and Preview services are configured to use a [custom identity provider (IdP)](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/authentication/saml-2-0), a new cookie called `delivery-token` encapsulating user's group membership must be set on publish domain post user's authentication. The delivery tier extracts the authorization material from the secure-cookie and validates the access. Please log an [enterprise support ticket](/help/assets/dynamic-media-open-apis-overview.md#how-to-enable-the-dynamic-media-with-openapi-capabilities) for more details.
