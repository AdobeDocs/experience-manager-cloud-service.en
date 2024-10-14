---
title: Connect AEM Assets to Creative Cloud
description: Learn how to configure and connect AEM Assets to Creative Cloud. Connect to a Creative Cloud entitlement that is provisioned to a different IMS organization to easily use the latest Creative Cloud integrations in AEM Assets, including Express and Creative Cloud Libraries.
exl-id: 880200fe-94b3-49de-802c-34283f7c71bc
feature: Collaboration
role: User
---
# Connect AEM Assets to Creative Cloud  {#cross-org-entitlements}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

Experience Manager Assets has the ability to connect to a Creative Cloud entitlement that is provisioned to a different IMS organization to easily use the latest Creative Cloud integrations in AEM Assets, including Express and Creative Cloud Libraries.

If your Creative Cloud products and AEM Assets are provisioned to separate IMS organizations, you can connect to a different Creative Cloud organization to be able to execute integrated workflows between the two solutions.

## Prerequisites {#prerequisites}

* Administrator rights to Experience Manager Assets

* Active entitlement to Creative Cloud for the same user ID used across Creative Cloud and Experience Manager. Entitlements to personal and federated IDs with the same email address are treated as different user IDs.

## Connect to a new Creative Cloud organization {#connect-to-creative-cloud-org}

To connect to a new Creative Cloud organization, execute the following steps:

1. Navigate to **[!UICONTROL Settings]** > **[!UICONTROL Creative Cloud]**.

1. Select the new Creative Cloud organization using the **[!UICONTROL Select new Creative Cloud org ID]** drop-down list. The list displays all organizations that you have access to. Select the organization with active Creative Cloud entitlements.

1. Click **[!UICONTROL Switch orgs]** to switch to the new organization.

   ![Cross Org Entitlements](assets/cross-org-entitlements.png)

## Limitations {#limitations}

* You can connect AEM Assets to one Creative Cloud organization at a time. Connection to multiple Creative Cloud organizations at a time is not supported.

* The Creative Cloud organization that you connect to within AEM Assets is applicable to all users within your organization.
