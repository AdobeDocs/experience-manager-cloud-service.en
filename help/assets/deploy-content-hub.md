---
title: Deploy [!DNL Content Hub]
description: Learn how to deploy and activate Content Hub and provide access to users with different types of privileges (upload assets, Adobe Express users) and how to provide administrator privileges to users.
role: Admin
---

# Deploy Content Hub {#deploy-content-hub}

![Deploy Content Hub](assets/deploy-content-hub.png)

Content Hub is available as part of Experience Manager Assets as a Cloud Service for democratizing access to on-brand content for organizations and their business partners.

The assets that are marked Approved on Experience Manager Assets as a Cloud Service are available for asset distribution on Content Hub.

This article provides an end-to-end workflow to provide Content Hub access to users including the variations of privileges based on their needs.

The variations of privileges on Content Hub include:

* [Asset consumers](#onboard-content-hub-consumer-users): Access brand approved assets on the Content Hub portal.

* [Administrators](#onboard-content-hub-administrator): Access to the [Configuration User Interface](/help/assets/configure-content-hub-ui-options.md) on Content Hub in addition to Asset consumer with submission rights.

* [Asset consumers with submission rights](#onboard-content-hub-consumer-users-submission-rights): Ability to [upload assets to Content Hub](/help/assets/upload-brand-approved-assets.md) and [Adobe Express Integration](/help/assets/edit-images-content-hub.md) in addition to accessing brand approved assets on the Content Hub portal.

* [Asset distributors](#content-hub-asset-distributors): Ability to approve assets on Experience Manager Assets as a Cloud Service to make those assets available on Content Hub.

## Step 1: Enable Content Hub for Experience Manager Assets using Cloud Manager {#enable-content-hub}

To access the Content Hub portal, administrators first need to enable Content Hub for Experience Manager Assets as a Cloud Service using Cloud Manager. Execute the following steps:

1. Log on to Cloud Manager. Ensure that you select the right organization while logging in. The Cloud Manager lists all your programs.

1. Navigate to Experience Manager Assets as a Cloud Service program, click the More options icon (...) and select **[!UICONTROL Edit Program]**.

   ![Edit program in Cloud Manager](assets/edit-program-cloud-manager.png)

1. On the [!UICONTROL Edit Program] dialog, select the **[!UICONTROL Solutions & Add-ons]** tab.

1. Expand **[!UICONTROL Assets]** and select **[!UICONTROL Content Hub]**.
   ![Select Content Hub in Cloud Manager](assets/edit-program-cloud-manager-content-hub.png)

1. Click **[!UICONTROL Update]**.

Content Hub is now enabled for Experience Manager Assets as a Cloud Service. 

>[!NOTE]
>
>You can access and use Content Hub with up to 250 Content Hub users. Please contact your Adobe representative if you have additional questions. 


If you are new to Experience Manager Assets, click **[!UICONTROL Add Program]** and then provide program details (Program Name, set up for Production) and click **[!UICONTROL Continue]**. You can then select **[!UICONTROL Assets]** and **[!UICONTROL Content Hub]** in the **[!UICONTROL Solutions & Add-ons]** tab.

### Content Hub instance and product profile on Admin Console{#content-hub-instance-product-profile}

After [enabling Content Hub for Assets as a Cloud Service using Cloud Manager](#enable-content-hub), there is a new instance created within AEM Assets as a Cloud Service on Admin Console with `contenthub` as the suffix:

![New instance for Content Hub](assets/new-instance-content-hub.png)

Note that there is no `author` or `publish` in the instance name for Content Hub.

Click the instance name to view the Content Hub product profile.

![Content Hub product profile](assets/content-hub-product-profile.png)

## Step 2: Onboard Content Hub administrator {#onboard-content-hub-administrator}

Content Hub administrators can add assets to Content Hub and can also set the [Configuration options](/help/assets/configure-content-hub-ui-options.md) for other users within your organization. 

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

## Step 3: Onboard Content Hub asset consumer users {#onboard-content-hub-consumer-users}

Content Hub consumer users can access assets available on the portal but cannot add any new assets or modify existing assets.

To onboard consumer users to Content Hub:

1. [Access and click the Content Hub user product profile](#content-hub-instance-product-profile).

1. Click **[!UICONTROL Add users]** to add users or user groups to the product profile.

1. Click **[!UICONTROL Save]** to save the changes.

These users can now access the assets available on the Content Hub portal.

>[!NOTE]
>
>You can use all the advanced enterprise features like synchronization with external Identity Providers.

After adding the appropriate users using Admin Console, the users can access Content Hub using the following link:

`https://experience.adobe.com/#/assets/contenthub`

### Disable email notifications to users {#disable-email-notifications}

If administrators need to disable email notifications sent to users when they are added to the Content Hub product profile:

Click the search icon adjacent to the product profile name and disable the **[!UICONTROL Notify users by email]** toggle.

![Disable email notifications](assets/disable-email-notifications.png)


## Step 4: Onboard Content Hub asset consumer users with submission permissions (Optional) {#onboard-content-hub-consumer-users-submission-rights}

Content Hub asset consumer users with submission permissions can:

* [Upload new brand-approved assets to Content Hub](/help/assets/upload-brand-approved-assets.md).

* [Modify existing assets using Adobe Express and save the asset to the repository](/help/assets/edit-images-content-hub.md). Editing assets using Adobe Express is only available if the user has Adobe Express entitlements.

To onboard Content Hub consumer user with submission rights:

1. [After adding the user to the Content Hub product profile](#onboard-content-hub-consumer-users), access Experience Manager Assets product profiles by clicking the AEM as a Cloud Service product name in the list of products on Admin Console.

1. Click the production author instance for AEM as a Cloud Service:
   ![Product profiles for AEM as a Cloud Service](assets/aem-cloud-service-instances.png)

   Admin Console displays two product profiles for AEM as a Cloud Service: Administrators and Users.
1. Click the Users product profile and click **[!UICONTROL Add users]** to add the user to the product profile.
   ![User product profile](assets/aem-cs-user-product-profile.png)

1. Click **[!UICONTROL Save]** to save the changes.

## Content Hub asset distributors {#content-hub-asset-distributors}

Asset distributors can approve assets on AEM as a Cloud Service so that they are available on Content Hub.

To configure the asset distributor role:

1. Access Experience Manager Assets product profiles by clicking the AEM as a Cloud Service product name in the list of products on Admin Console.

1. Click the production author instance for AEM as a Cloud Service:
   ![Product profiles for AEM as a Cloud Service](assets/aem-cloud-service-instances.png)

   Admin Console displays two product profiles for AEM as a Cloud Service: Administrators and Users.
1. Click the Users product profile and click **[!UICONTROL Add users]** to add the user to the product profile.
   ![User product profile](assets/aem-cs-user-product-profile.png)

1. Click **[!UICONTROL Save]** to save the changes.

   >[!NOTE]
   >
   > You do not need to be added to the [Content Hub product profile](#onboard-content-hub-consumer-users) for the asset distribution role.



