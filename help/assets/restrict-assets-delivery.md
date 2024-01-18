---
title: Restrict delivery of assets in Experience Manager
description: Learn how to restrict the assets delivery in [!DNL Experience Manager].
role: User
---
# Restrict access to assets in [!DNL Experience Manager]

Central asset governance in Experience Manager allows the DAM Admin or Brand Manager to manage access to assets. They can restrict the access by configuring roles for approved assets on the authoring side, specifically on the AEMaaCS author instance.

End-users searching or utilizing delivered asset binaries can gain access to restricted assets upon successfully passing the authorization process.

## Restricted delivery via IMS

In Experience Manager, restricted delivery via IMS involves two key stages: 

* Authoring 
* Delivery

### Authoring

To restrict the delivery of assets, roles must be configured for the assets within the AEMaaCS instance. To configure roles, follow these steps:

1. Go to the [!DNL Experience Manager] as DAM Admin.
1. Select the asset for whoch you need to configure the role.
1. Navigate to **[!UICONTROL Properties]** > **[!UICONTROL Advanced]**, and Ensure that the **[!UICONTROL Roles]** field exists in the Advanced Metadata tab. 

<br>If the field is not available, use the following steps to add the field:

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
1. Select the metadata schema and click **[!UICONTROL Edit _(e)_]**.
1. Add a **[!UICONTROL Multi Value Text]** field from the **[!UICONTROL Build Form]** section in right side to Metadata section in the form. 
1. Click the newly added field, and then do the following updates in the  **[!UICONTROL Settings]** panel:
    1. Change the **[!UICONTROL Field Label]** to _Roles_.
    1. Update the **[!UICONTROL Map to property]** to _./jcr:content/metafdata/dam:roles_. 
1. Obtain the IMS groups to be added in the Roles metadata of the asset. To fetch the IMS groups, follow these steps:
   1. Sign in at https://adminconsole.adobe.com/.
   1. Go to your respective organization and navigate to **[!UICONTROL User Groups]**.
   1. Select the **[!UICONTROL User Group]** you need to add, and extract the **[!UICONTROL orgID]** and **[!UICONTROL userGroupID]** from the URL or use <Your Org Id>@AdobeOrg:<your user group ID> (i.e OrgID:userGroupID).

1. Add the Group ID to the Asset's Roles Metadata.


### Delivery

To enable the delivery of restricted assets, a valid IMS token is essential. Follow these steps:

1. [Generate an access token](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md).
   * Log in to your AEMaaCS environment's Dev Console, such as https://dev-console-ns-team-aem-cm-stg-n25271.ethos14-stage-va7.dev.adobeaemcloud.com/#release-cm-p47604-e144858.
   * Navigate to **[!UICONTROL Environment]** > **[!UICONTROL Integrations]** > **[!UICONTROL Local Token]** > **[!UICONTROL Get Local Development Token]** > **[!UICONTROL Copy accessToken value]**. Learn more about [how to access token and related aspects](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md)

1. Integrate the obtained access token to the **[!UICONTROL Authorization]** header, ensuring its value is prefixed with **[!UICONTROL Bearer]**.

1. Validate the access token's functionality by initiating a request. It should yield a 404 error in cases where there is no IMS access token or the provided access token lacks the same principals or groups as those added in the asset's metadata.
