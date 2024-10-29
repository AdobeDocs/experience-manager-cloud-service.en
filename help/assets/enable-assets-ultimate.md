---
title: Assets as a Cloud Service user types and privileges
description: 
feature: Asset Management
role: User, Admin
---
# Enable [!DNL Assets] as a Cloud Service Ultimate {#enable-assets-ultimate}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

![Upgrade to Asset Cloud Service Ultimate](/help/assets/assets/upgrade-assets-cs-ultimate-package-banner.png)

Assets as a Cloud Service Ultimate enables you to perform various key DAM capabilities, such as, advanced asset management operations, including, custom schema, metadata translations, custom processing profiles, custom workflow management, API-driven UI extensibility, advanced reporting, integrations with adobe and non-adobe applications, and many more. See [Assets as a Cloud Service Ultimate Overview](/help/assets/assets-ultimate-overview.md) for the complete list.


The new Assets as a Cloud Service users must first enable Assets Ultimate while creating the new program using Cloud Manager. Execute the following steps:

1. As a system administrator, log on to Cloud Manager. Ensure that you select the right organization while logging in.

1. [Create a new program](/help/journey-onboarding/create-program.md) and [add environments](/help/journey-onboarding//create-environments.md) to it.

   While creating the new program, in **[!UICONTROL Solutions & Add-ons]** tab, select **[!UICONTROL Assets Ultimate]**. You can also expand **[!UICONTROL Assets Ultimate]** and select **[!UICONTROL Content Hub]** to enable [Content Hub](/help/assets/product-overview.md) for asset distribution.

   ![AEM Assets Ultimate](assets/aem-assets-ultimate-solutions.png)

1. Click **[!UICONTROL Create]** to create the program. Assets Ultimate is now enabled for Experience Manager Assets as a Cloud Service.

The System Administrator is automatically entitled for the AEM Administrators role on Assets Ultimate and must have received an email to navigate to Admin Console to manage the updated product profiles.

Your AEM as a Cloud Service instance on Admin Console comprises the following product profiles:

* AEM Administrators

* AEM Users

* [AEM Assets Collaborator Users](#onboard-collaborator-users)

* [AEM Assets Power Users](#onboard-power-users)

   ![AEM Assets Product Profiles](assets/aem-assets-product-profiles.png)

If you have enabled Content Hub for Assets as a Cloud Service, there is a new instance created within AEM Assets as a Cloud Service on Admin Console with `delivery` as the suffix:

![New instance for Content Hub](assets/new-instance-content-hub.png)

>[!NOTE]
>
>If you have provisioned Content Hub before August 14, 2024, the new instance is created with `contenthub` as the suffix.

Note that there is no `author` or `publish` in the instance name for Content Hub.

Click the instance name to view the `AEM Assets Limited Users` Content Hub product profile.

![Content Hub product profile](assets/content-hub-product-profile.png)

You can start adding users or user groups to this product profile to provide them access to Content Hub.

>[!NOTE]
>
>If you have provisioned Content Hub before August 14, 2024, the Content Hub product profile has `contenthub` mentioned after `Limited Users` instead of `delivery`.

<!--

## Enable Assets as a Cloud Service Ultimate for existing users {#enable-assets-ultimate-existing-users}

Existing Assets as a Cloud Service users can upgrade to Assets ultimate by executing two simple steps. You can navigate to the Assets as a Cloud Service program in Cloud Manager and see upgrade status on the Program card based on the availability of credits. If there are enough credits available for upgrade to Assets Ultimate, you can see the status as `Assets license upgrade required`, as depicted in the following image:

![AEM Assets upgrade to Assets Ultimate](assets/aem-assets-upgrade-status-ultimate.png)

In case an existing user purchases a new license for Assets Ultimate, the upgrade status displays as `Assets license upgrade available`.

### Prerequisites for upgrade {#prerequisites-assets-upgrade}

All environments must be upgraded to latest AEM as a Cloud Service release version or a minimum of x release version. If you do not meet the minimum requirements, contact your Adobe representative to switch to the required AEM release version.

### Upgrade to Assets Ultimate {#upgrade-assets-ultimate}

Execute the following steps:

1. After switching to the minimum requirements for the AEM release version, click the program name. An Upgrade card displays just above **[!UICONTROL Environments]** section, as depicted in the following image:

   ![AEM Assets upgrade to Assets Ultimate](assets/aem-assets-upgrade-card.png)

1. Click **[!UICONTROL Add Product Profiles]**. Cloud Manager displays options to add new product profiles to all environments available in the program or individual environments.

   ![AEM Assets upgrade options](assets/aem-assets-upgrade-options.png)

1. Click **[!UICONTROL All Environments]** to add the new product profiles to all environments in the program or **[!UICONTROL Individual Environments]** to add the new product profiles to selected environments.

   Clicking **[!UICONTROL Individual Environments]** displays the list of all environments available in the program.

1. Click the More Options icon corresponding to an environment and select **[!UICONTROL Add Product Profiles]** to add the new product profiles to the selected environment.

   ![AEM Assets select individual environments](assets/aem-assets-individual-environments.png)

   You can also add product profiles to selected environments by navigating to the **[!UICONTROL Environments]** section, clicking the More Options icon corresponding to an environment, and selecting **[!UICONTROL Add Product Profiles]**.

   ![AEM Assets select individual environments in Environments section](assets/aem-assets-select-individual-environments.png)

   The status of the environment displays `Updating Product Profiles` while the new product profiles are being added and subsequently displays `Running` when the process is complete.

   You must add product profiles to all environments available in the program, individually or all environments together, before executing the next step.

1. Click **[!UICONTROL Upgrade]**. The **[!UICONTROL Upgrade]** option displays only when you add product profiles to all available environments. 

   ![Last step in the upgrade process](assets/aem-assets-upgrade-button.png)

   The upgrade process is complete and you have successfully upgraded your Assets as a Cloud Service to Assets Ultimate. The status of the program displays `Assets Ultimate`.

   ![Program status after upgrade](assets/program-status-post-upgrade.png)

Your AEM as a Cloud Service instance on Admin Console now comprises the following product profiles:

* AEM Administrators

* AEM Users

* [AEM Assets Collaborator Users](#onboard-collaborator-users)

* [AEM Assets Power Users](#onboard-power-users)

![AEM Assets Product Profiles](assets/aem-assets-product-profiles.png)

If you need Content Hub enabled, click More options (...) icon on the program name in Cloud Manager and select **[!UICONTROL Edit Program]**. Expand **[!UICONTROL Assets Ultimate]** and click **[!UICONTROL Content Hub]**. This step enables the Content Hub for Assets Ultimate. There is a new instance created within AEM Assets as a Cloud Service on Admin Console with `delivery` as the suffix:

![New instance for Content Hub](assets/new-instance-content-hub.png)

>[!NOTE]
>
>If you have provisioned Content Hub before August 14, 2024, the new instance is created with `contenthub` as the suffix.

Note that there is no `author` or `publish` in the instance name for Content Hub.

Click the instance name to view the `AEM Assets Limited Users` Content Hub product profile.

![Content Hub product profile](assets/content-hub-product-profile.png)

You can start adding users or user groups to this product profile to provide them access to Content Hub.

>[!NOTE]
>
>If you have provisioned Content Hub before August 14, 2024, the Content Hub product profile has `contenthub` mentioned after `Limited Users` instead of `delivery`.

-->

## Onboard AEM Assets Collaborator users {#onboard-collaborator-users}

AEM Assets Collaborator users can work with assets from Experience manager via integrations of Assets available to your organization in other Adobe products and non-Adobe applications, create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on, and access and leverage approved assets from your organization using AEM Assets Content Hub portal.

To onboard Collaborator users:

1. Access Experience Manager Assets product profiles by clicking the AEM as a Cloud Service product name in the list of products on Admin Console.

1. Click the production author instance for AEM as a Cloud Service:
   ![Product profiles for AEM as a Cloud Service](assets/aem-cloud-service-instances.png)

1. Click the Collaborators users product profile and click **[!UICONTROL Add users]** to add users or user groups to the product profile.
   ![User product profile](assets/aem-assets-collaborator-user-permissions.png)

1. Click **[!UICONTROL Save]** to save the changes.

You can also access and view the services assigned to Collaborator users, as depicted in the following image:

![Services for Collaborator users](assets/aem-assets-collaborator-users.png)

`Adobe Express` and `AEM Assets Collaborator Users` services are enabled by default.

>[!NOTE]
>
>You can turn the toggle off and on to enable or disable the available services, as per your requirements, however, Adobe recommends to use the default services enabled for the product profiles.


## Onboard AEM Assets Power users {#onboard-power-users}

AEM Assets Power users can access all AEM Assets capabilities including managing assets, permissions, metadata and the overall governance and automation around digital assets, work with assets from Experience manager via integrations of Assets available to your organization in other Adobe and non-Adobe applications, create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on, and access and leverage approved assets from your organization using AEM Assets Content Hub portal.

To onboard Power users:

1. Access Experience Manager Assets product profiles by clicking the AEM as a Cloud Service product name in the list of products on Admin Console.

1. Click the production author instance for AEM as a Cloud Service:
   ![Product profiles for AEM as a Cloud Service](assets/aem-cloud-service-instances.png)

1. Click the Power users product profile and click **[!UICONTROL Add users]** to add users or user groups to the product profile.
   ![User product profile](assets/aem-assets-power-user-permissions.png)

1. Click **[!UICONTROL Save]** to save the changes.

You can also access and view the services assigned to Power users, as depicted in the following image:

![Services for Power users](assets/aem-assets-power-users.png)

`Adobe Express` and `AEM Assets Power Users` services are enabled by default.

>[!NOTE]
>
>You can turn the toggle off and on to enable or disable the available services, as per your requirements, however, Adobe recommends to use the default services enabled for the product profiles.
