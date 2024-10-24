---
title: Assets as a Cloud Service Prime package
description: Assets as a Cloud Service Prime package
feature: Asset Management
role: User, Admin
---
# [!DNL Assets] as a Cloud Service Prime package  {#assets-upgrade-ultimate-package}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

![Upgrade to Asset Cloud Service Ultimate Package](/help/assets/assets/upgrade-assets-cs-ultimate-package-banner.png)

Assets as a Cloud Service Prime package includes a lightweight DAM that enables you to perform various key capabilities, such as:

* Asset management tasks, such as metadata management, permissions management, and asset governance.

* Trainable Smart Tags for better search.

* Automated content creation by creating asset variations using Adobe Express.

* Integrating Assets available in the Cloud Service repository with Adobe and non-Adobe applications using Asset Selector.

* Delivery of assets using Publish URL.

* Basic reporting operations, such as, asset usage and downloads.

* Content Hub for distributing assets for activation at scale.

However, as your DAM needs grow and you need more capabilities, such as, advanced asset management operations, including custom schema, metadata translations, custom processing profiles, and so on, Custom workflow management, API-driven UI extensibility, advanced reporting, such as, asset performance, and asset usage by user, and additional Stage and Development environments, you must consider upgrading to [Assets as a Cloud Service Ultimate package](/help/assets/user-types-privileges.md).

This article provides an end-to-end workflow to enable Assets as a Cloud Service Prime package.

## Enable Assets as a Cloud Service Prime package{#enable-assets-prime-package}

Enable the Assets Prime package while creating the new program using Cloud Manager. Execute the following steps:

1. As a system administrator, log on to Cloud Manager. Ensure that you select the right organization while logging in.

1. [Create a new program](/help/journey-onboarding/create-program.md).

   While creating the new program, in **[!UICONTROL Solutions & Add-ons]** tab, select **[!UICONTROL Assets Prime]**. You can also expand **[!UICONTROL Assets Prime]** and select **[!UICONTROL Content Hub]** to enable [Content Hub](/help/assets/product-overview.md) for asset distribution.

   ![AEM Assets Ultimate Package](assets/aem-assets-prime.png)

1. Click **[!UICONTROL Create]** to create the program. 

1. Click the program card and click **[!UICONTROL Add Environment]**.

1. Specify the environment name, define a region and click **[!UICONTROL Save]** to create the environment.

   ![Add environment to Assets Prime](assets/aem-assets-prime-add-environment.png)

>[!NOTE]
>
>Assets Prime only allows you to create a production environment. The option to Add environment is no longer available once the production environment is created successfully.

Assets Prime package is now enabled for Experience Manager Assets as a Cloud Service.

![AEM Assets Prime Package is avaiable](assets/aem-assets-prime-setup-complete.png)

System administrator is automatically entitled as AEM administrator and receives an email to navigate to Admin Console to manage product profiles.


Your AEM as a Cloud Service instance on Admin Console comprises the following product profiles:

* AEM Administrators

* AEM Users

* AEM Assets Collaborator Users

* AEM Assets Power Users

You can start adding users or user groups to AEM Assets Collaborator Users and AEM Assets Power Users product profiles. For more information, see [Onboard AEM Assets Collaborator users](#onboard-collaborator-users) and [Onboard AEM Assets Power users](#onboard-power-users).

![AEM Assets Product Profiles](assets/aem-assets-product-profiles.png)

If you have enabled Content Hub for Assets as a Cloud Service, there is a new instance created within AEM Assets as a Cloud Service on Admin Console with `delivery` as the suffix:

![New instance for Content Hub](assets/new-instance-content-hub.png)

>[!NOTE]
>
>If you have provisioned Content Hub before August 14, 2024, the new instance is created with `contenthub` as the suffix.

Note that there is no `author` or `publish` in the instance name for Content Hub.

Click the instance name to view the `AEM Assets Limited Users` Content Hub product profile.

![Content Hub product profile](assets/content-hub-product-profile.png)

>[!NOTE]
>
>If you have provisioned Content Hub before August 14, 2024, the Content Hub product profile has `contenthub` mentioned after `Limited Users` instead of `delivery`.

## Step 4: Onboard AEM Assets Collaborator users {#onboard-collaborator-users}

AEM Assets Collaborator users can work with assets from Experience manager via integrations of Assets available to your organization in other Adobe products and non-Adobe applications, create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on, and access and leverage approved assets from your organization using AEM Assets Content Hub portal.

To onboard Collaborator users:

1. Access Experience Manager Assets product profiles by clicking the AEM as a Cloud Service product name in the list of products on Admin Console.

1. Click the production author instance for AEM as a Cloud Service:
   ![Product profiles for AEM as a Cloud Service](assets/aem-cloud-service-instances.png)

1. Click the Collaborators users product profile and click **[!UICONTROL Add users]** to add the user to the product profile.
   ![User product profile](assets/aem-assets-collaborator-user-permissions.png)

1. Click **[!UICONTROL Save]** to save the changes.

You can also access and view the services assigned to Collaborator users, as depicted in the following image:

![Services for Collaborator users](assets/aem-assets-collaborator-users.png)

`Adobe Express` and `AEM Assets Collaborator Users` services are enabled by default. You can turn the toggle off and on, as per your requirements.

## Step 4: Onboard AEM Assets Power users {#onboard-power-users}

AEM Assets Power users can access all AEM Assets capabilities including managing assets, permissions, metadata and the overall governance and automation around digital assets, work with assets from Experience manager via integrations of Assets available to your organization in other Adobe and non-Adobe applications, create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on, and access and leverage approved assets from your organization using AEM Assets Content Hub portal.

To onboard Power users:

1. Access Experience Manager Assets product profiles by clicking the AEM as a Cloud Service product name in the list of products on Admin Console.

1. Click the production author instance for AEM as a Cloud Service:
   ![Product profiles for AEM as a Cloud Service](assets/aem-cloud-service-instances.png)

1. Click the Power users product profile and click **[!UICONTROL Add users]** to add the user to the product profile.
   ![User product profile](assets/aem-assets-power-user-permissions.png)

1. Click **[!UICONTROL Save]** to save the changes.

You can also access and view the services assigned to Power users, as depicted in the following image:

![Services for Power users](assets/aem-assets-power-users.png)

`Adobe Express` and `AEM Assets Power Users` services are enabled by default. You can turn the toggle off and on, as per your requirements.
