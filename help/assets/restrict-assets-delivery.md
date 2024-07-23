---
title: Restrict delivery of assets in Experience Manager
description: Learn how to restrict the assets delivery in [!DNL Experience Manager].
role: User
---
# Restrict access to assets in [!DNL Experience Manager] {#restrict-access-to-assets}

Central asset governance in Experience Manager allows the DAM Admin or Brand Managers to manage access to assets. They can restrict the access by configuring roles for approved assets on the authoring side, specifically on the AEM as a Cloud Service author instance.

Users [searching](search-assets-api.md) or utilizing [delivery URLs](deliver-assets-apis.md) can gain access to restricted assets upon successfully passing the authorization process.

![Restricted access to assets](/help/assets/assets/restricted-access.png)

## Restricted delivery using an IMS token {#restrict-delivery-ims-token}

In Experience Manager Assets, restricted delivery via IMS involves two key stages: 

* Authoring 
* Delivery

### Authoring {#authoring}

You can restrict the delivery of assets within [!DNL Experience Manager] based on roles. To configure roles, execute the following steps:

1. Go to the [!DNL Experience Manager] as DAM Admin.
1. Select the asset for which you need to configure the role.
1. Navigate to **[!UICONTROL Properties]** > **[!UICONTROL Advanced]**, and ensure that the **[!UICONTROL Roles]** field exists in the [!UICONTROL Advanced Metadata] tab.

   ![Roles metadata](/help/assets/assets/roles_metadata.jpg)
If the field is not available, use the following steps to add the field:

   1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
   1. Select the metadata schema and click **[!UICONTROL Edit _(e)_]**.
   1. Add a **[!UICONTROL Multi Value Text]** field from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form. 
   1. Click the newly added field, and then do the following updates in the  **[!UICONTROL Settings]** panel:
      1. Change the **[!UICONTROL Field Label]** to _Roles_.
      1. Update the **[!UICONTROL Map to property]** to _./jcr:content/metadata/dam:roles_.

1. Obtain the IMS groups to be added in the Roles metadata of the asset. To fetch the IMS groups, follow these steps:
   1. Sign in at `https://adminconsole.adobe.com/.`
   1. Go to your respective organization and navigate to **[!UICONTROL User Groups]**.
   1. Select the **[!UICONTROL User Group]** you need to add, and extract the **[!UICONTROL orgID]** and **[!UICONTROL userGroupID]** from the URL or use your Org Id such as `{orgID}@AdobeOrg:{usergroupID}`.

1. Add the Group ID to the **[!UICONTROL Roles]** field of Asset properties. <br>
   The Group IDs defined in the **[!UICONTROL Roles]** field are the only users who can access the asset. You can also add IMS client ID and IMS profile id in the **[!UICONTROL Roles]** field. For example, `{orgId}@AdobeOrg:{profileId}`.

   >[!NOTE]
   >
   >For new Assets view, you can only give access up to the folder level, and exclusively to groups rather than individual users. Learn more about [managing permissions within Experience Manager Assets](https://experienceleague.adobe.com/en/docs/experience-manager-assets-essentials/help/get-started-admins/folder-access/manage-permissions).

   >[!VIDEO](https://video.tv.adobe.com/v/3427429)

#### Restrict delivery of assets using On and Off date and time {#restrict-delivery-assets-date-time}

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



### Delivery of restricted assets {#delivery-restricted-assets}

The delivery of restricted assets is based on successful authorization to access assets. The authorization is either based on an IMS token if the request is sent from an AEM author instance or Asset Selector or it is based on a special cookie if you have custom identity providers set up on your Publish or Preview instance.

#### Delivery for AEM author or Asset Selector requests {#delivery-aem-author-asset-selector}

To enable the delivery of restricted assets in case the request is sent from AEM author instance or Asset Selector, a valid IMS token is essential. Follow these steps:

1. [Generate an access token](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis.html?lang=en#generating-the-access-token).
   * Log in to your AEM as a Cloud Service environment's Dev Console.

   * Navigate to **[!UICONTROL Environment]** > **[!UICONTROL Integrations]** > **[!UICONTROL Local Token]** > **[!UICONTROL Get Local Development Token]** > **[!UICONTROL Copy accessToken value]**. Learn more about [how to access token and related aspects](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis.html?lang=en#generating-the-access-token)

1. Integrate the obtained access token to the **[!UICONTROL Authorization]** header, ensuring its value is prefixed with **[!UICONTROL Bearer]**.

1. Validate the access token's functionality by initiating a request. It should yield a 404 error in cases where there is no IMS access token, or the provided access token lacks the same principals or groups as those added in the asset's metadata.

#### Delivery for custom identity providers on Publish instance {#delivery-custom-identity-provider}

In case of a custom identity provider set up on your Publish or Preview instance, you can mention the group that must have access to secured assets within `groupMembership` attribute during the setup process. When you log on to custom identity provider via [SAML integration](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/authentication/saml-2-0), the `groupMembership` attribute is read and used to construct a cookie, which is sent in all requests for authentication, similar to an IMS token in case of a request from AEM author or Asset Selector.

When a secured asset is available on a page and a request is made to the delivery URL to render the asset, AEM checks the roles present in the cookie or the IMS token and matches it against the `dam:roles property` applied during the authoring of the asset. If there is a match, the asset gets displayed.

>[!NOTE]
>
> In the [support ticket to activate Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md#how-to-enable-the-dynamic-media-with-openapi-capabilities), mention restricted delivery in the use case. Adobe Engineering will help with necessary clarifications and/or set up process for restricted delivery.
