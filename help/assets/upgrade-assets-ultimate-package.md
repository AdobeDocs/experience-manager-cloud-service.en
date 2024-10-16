---
title: Assets as a Cloud Service user types and privileges
description: 
feature: Asset Management
role: User, Admin
---
# Upgrade to [!DNL Assets] as a Cloud Service Ultimate package  {#assets-upgrade-ultimate-package}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

![Upgrade to Asset Cloud Service Ultimate Package](/help/assets/assets/upgrade-assets-cs-ultimate-package-banner.png)

Assets as a Cloud Service Ultimate package enables you to perform various key DAM capabilities, such as, advanced asset management operations, including, custom schema, metadata translations, custom processing profiles, Custom workflow management, API-driven UI extensibility, advanced reporting, integrations with adobe and non-adobe applications, and many more. See [Assets as a Cloud Service Ultimate package](/help/assets/user-types-privileges.md) for the complete list.

This article provides an end-to-end workflow to upgrade your Assets as a Cloud Service environment to the Ultimate package, including the user assignments to the available product profiles.

## Step 1: Enable Assets as a Cloud Service Ultimate package using Cloud Manager {#enable-assets-ultimate-package}

Administrators first need to enable the Ultimate package for Assets as a Cloud Service using Cloud Manager. Execute the following steps:

1. Log on to Cloud Manager. Ensure that you select the right organization while logging in. The Cloud Manager lists all your programs.

1. Navigate to Experience Manager Assets as a Cloud Service program, click the More options icon (...) and select **[!UICONTROL Edit Program]**.

   ![Edit program in Cloud Manager](assets/edit-program-cloud-manager.png)

1. On the [!UICONTROL Edit Program] dialog, select the **[!UICONTROL Solutions & Add-ons]** tab.

1. Expand **[!UICONTROL Assets]** and select **[!UICONTROL Assets Ultimate]**.
   ![Select Content Hub in Cloud Manager](assets/edit-program-cloud-manager-content-hub.png)

   >[!NOTE]
   >
   >If **[!UICONTROL Update]** is not enabled for you after selecting Assets Ultimate, ensure that you have specified Go-Live settings for the program.

1. Click **[!UICONTROL Update]**.

Assets as a Cloud Service Ultimate package is now enabled for Experience Manager Assets as a Cloud Service. After enabling Content Hub on a Production environment, you cannot disable it in a self-service manner. 


If you are new to Experience Manager Assets, click **[!UICONTROL Add Program]** and then provide program details (Program Name, set up for Production) and click **[!UICONTROL Continue]**. You can then select **[!UICONTROL Assets]** and **[!UICONTROL Assets Ultimate]** in the **[!UICONTROL Solutions & Add-ons]** tab.

### Assets as a Cloud Service Ultimate package instance and product profiles on Admin Console{#assets-ultimate-instance-product-profile}

After [enabling Assets as a Cloud Service Ultimate package using Cloud Manager](#enable-assets-ultimate-package), there is a new instance created within AEM Assets as a Cloud Service on Admin Console (Instance name?):

![New instance for Content Hub](assets/new-instance-content-hub.png)

Click the instance name to view the Assets as a Cloud Service Ultimate package product profiles.

![Content Hub product profile](assets/content-hub-product-profile.png)


## Step 2: Onboard Assets as a Cloud Service administrator {#onboard-administrator}

Content Hub administrators can access the [Configuration User Interface](/help/assets/configure-content-hub-ui-options.md) on Content Hub in addition to accessing brand-approved assets, uploading assets to Content Hub, Adobe Express integration to edit images (if you have Adobe Express entitlements). 

To onboard the Content Hub administrator:

1. [Access and click the Content Hub user product profile](#content-hub-instance-product-profile).

1. Click **[!UICONTROL Add users]** to add users or user groups to the product profile.

1. Click **[!UICONTROL Save]** to save the changes.

1. After adding the user to the Content Hub product profile, access Experience Manager Assets product profiles by clicking the AEM as a Cloud Service product name in the list of products on Admin Console.

1. Click the production author instance for AEM as a Cloud Service:
   ![Product profiles for AEM as a Cloud Service](assets/aem-cloud-service-instances.png)

   Admin Console displays two product profiles for AEM as a Cloud Service: Administrators and Users.
1. Click the Administrators product profile and click **[!UICONTROL Add users]** to add the user to the product profile.
   ![Administrator product profile](assets/aem-cs-admin-product-profile.png)

1. Click **[!UICONTROL Save]** to save the changes.


## Step 4: Onboard AEM Assets Collaborator users {#onboard-collaborator-users}

AEM Assets Collaborator users can work with assets from Experience manager via integrations of Assets available to your organization in other Adobe products and non-Adobe applications, create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on, and access and leverage approved assets from your organization using AEM Assets Content Hub portal.

To onboard Collaborator users:

1. Access Experience Manager Assets product profiles by clicking the AEM as a Cloud Service product name in the list of products on Admin Console.

1. Click the production author instance for AEM as a Cloud Service:
   ![Product profiles for AEM as a Cloud Service](assets/aem-cloud-service-instances.png)

1. Click the Collaborators users product profile and click **[!UICONTROL Add users]** to add the user to the product profile.
   ![User product profile](assets/aem-cs-user-product-profile.png)

1. Click **[!UICONTROL Save]** to save the changes.

## Step 4: Onboard AEM Assets Power users {#onboard-power-users}

AEM Assets Power users can access all AEM Assets capabilities including managing assets, permissions, metadata and the overall governance and automation around digital assets, work with assets from Experience manager via integrations of Assets available to your organization in other Adobe and non-Adobe applications, create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on, and access and leverage approved assets from your organization using AEM Assets Content Hub portal.

To onboard Power users:

1. Access Experience Manager Assets product profiles by clicking the AEM as a Cloud Service product name in the list of products on Admin Console.

1. Click the production author instance for AEM as a Cloud Service:
   ![Product profiles for AEM as a Cloud Service](assets/aem-cloud-service-instances.png)

1. Click the Power users product profile and click **[!UICONTROL Add users]** to add the user to the product profile.
   ![User product profile](assets/aem-cs-user-product-profile.png)

1. Click **[!UICONTROL Save]** to save the changes.
