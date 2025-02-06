---
title: Notification Profiles
description: Learn how to create user profiles in the Admin Console to manage receipt of important email notifications.
feature: Onboarding
role: Admin, User, Developer
exl-id: 4edecfcd-6301-4a46-98c7-eb5665f48995
---

# Notification Profiles {#notification-profiles}

Learn how to create user profiles in the Admin Console to manage receipt of important email notifications.

## Overview {#overview}

From time-to-time, Adobe contacts users regarding their AEM as a Cloud Service environments. In addition to in-product notifications, Adobe also occasionally uses email for notifications. There are two types of such email notification:

* **Incident Notification** - These notifications are sent during an incident or when Adobe has identified a potential availability issue with your AEM as a Cloud Service environment.
* **Proactive Notification** - These notifications are sent when an Adobe support team member wants to provide guidance on a potential optimization or recommendation that can benefit your AEM as a Cloud Service environment.

Users can also receive these notifications for specific programs based on their [custom group permissions](/help/implementing/cloud-manager/custom-permissions.md).

Additionally, assigning groups to proactive notification is supported and users and groups can be assigned to the product profiles directly.

* Users in the incident and proactive notification groups will receive notifications for all programs by default.
* However, if users do not want to receive all notifications, they can use custom READ permissions to specify which program notifications they wish to receive.

For the correct users to receive these notifications, you need to configure and assign user profiles as described in this document.

## Prerequisites {#prerequisites}

Because user profiles are created and maintained in the Admin Console, before creating profiles for notifications, you must:

* Have permissions to add and profile memberships.
* Have a valid Adobe Admin Console profile.

## Create New Cloud Manager Product Profiles {#create-profiles}

To properly set up receipt of notifications, create two user profiles. These steps are only done one time.

1. Log in to Admin Console at [`https://adminconsole.adobe.com`](https://adminconsole.adobe.com).

1. Ensure that you are in the correct organization.

1. From the **Overview** page, select **Adobe Experience Manager as a Cloud Service** from the **Products and services** card.

   ![List of products and services in the Admin Console](assets/products_services.png)

1. Navigate to the **Cloud Manager** instance from the list of all instances.

     ![List of instances in the Admin Console](assets/cloud_manager_instance.png)

1. You can see the list of all configured Cloud Manager product profiles.

    ![Product profiles in the Admin Console](assets/cloud_manager_profiles.png)

1. Click **New Profile** and provide the following details:

   * **Product profile name**: `Incident Notification - Cloud Service`
   * **Display name**: `Incident Notification - Cloud Service`
   * **Description**: Cloud Manager profile for the users that will receive notifications during an incident or when Adobe has identified a potential availability problem with your AEM as a Cloud Service environment.
     * Users with custom READ permissions on specific programs will receive notifications only for those programs if they choose to use custom permissions.

1. Click **Save**.

1. Click **New Profile** once more and provide the following details:

   * **Product profile name**: `Proactive Notification - Cloud Service`
   * **Display name**: `Proactive Notification - Cloud Service`
   * **Description**: Cloud Manager profile for the users that will receive notifications when an Adobe support team member wants to provide guidance on a potential optimization or recommendation to do with your AEM as a Cloud Service environment configuration
     * Users with custom READ permissions on specific programs will receive notifications only for those programs if they choose to use custom permissions.

1. Click **Save**.

Your two new notification profiles are created.

>[!NOTE]
>
>It is important that the Cloud Manager **product profile name** is exactly the same as provided. Copy and paste the provided product profile name to avoid errors. Any deviations or typos will result in notifications not being sent as desired.
>
>In case of error or if the profiles have not been defined, Adobe will default to notifying existing users assigned to the **Cloud Manager Developer** or **Deployment Manager** profiles.

## Assign Users to the Notification Profiles {#add-users}

Now that the profiles have been created, you must assign the appropriate users. You can do this when creating new users or by updating existing users.

### Add New Users to Profiles {#new-user}

Follow these steps to add users for whom federated IDs have not yet been set up.

1. Identify the user(s) or group(s) who should receive either incident or proactive notifications.

1. Log in to Admin Console at [`https://adminconsole.adobe.com`](https://adminconsole.adobe.com) if you are not still logged in.

1. Ensure you have selected the appropriate organization.

1. From the **Overview** page, select **Adobe Experience Manager as a Cloud Service** from the **Products and services** card.

   ![Users](assets/product_services.png)

1. If the federated ID for your team members has not yet been set up, select the **Users** tab from the top navigation, then select **Add User**. Otherwise skip to the section [Add Existing Users to Profiles](#existing-users).

   ![Users](assets/cloud_manager_add_user.png)

1. In the **Add users to your team** dialog, enter the email ID of the user you want to add and select `Adobe ID` for the **ID Type**. 

1. Click the plus button under the **Select products** heading to begin product selection.

1. Select **Adobe Experience Manager as a Cloud Service** and assign one or both of the new profiles to the user.

   * **Incident Notification - Cloud Service**
   * **Proactive Notification - Cloud Service**

1. Click **Save** and a welcome email is sent to the user you added.

The invited user will now receive the notifications. Users with custom READ permissions on specific programs will receive notifications only for those programs if they choose to use custom permissions.

Repeat these steps for the users on your team that you would like to receive notifications.

### Add Existing Users to Profiles {#existing-user}

Follow these steps to add users for whom federated IDs already exist.

1. Identify the user(s) or group(s) who should receive either incident or proactive notifications.

1. Log in to Admin Console at [`https://adminconsole.adobe.com`](https://adminconsole.adobe.com) if you are not still logged in.

1. Ensure that you have selected the appropriate organization.

1. From the **Overview** page, select **Adobe Experience Manager as a Cloud Service** from the **Products and services** card.

1. Select the **Users** tab from the top navigation.

1. If the federated ID already exists for the team member whom you want to add to a notification profile, locate that user in the list and click it. Otherwise skip to the section [Add New Users to Profiles](#add-user).

1. In the **Products** section of the user details window, click the ellipsis button and then select **Edit**.

1. In the **Edit products** window, click the pencil button below the **Select products** heading to begin product selection.

1. Select **Adobe Experience Manager as a Cloud Service** and assign one or both of the new profiles to the user.

   * **Incident Notification - Cloud Service**
   * **Proactive Notification - Cloud Service**

1. Click **Save** and a welcome email is sent to the user you added.

The invited user will now receive the notifications. Users with custom READ permissions on specific programs will receive notifications only for those programs if they choose to use custom permissions.

Repeat these steps for the users on your team that you would like to receive notifications.

## Additional Resources {#additional-resources}

The following are additional, optional resources if you would like to go beyond the content of the onboarding journey.

* [Actions Center](/help/operations/actions-center.md) - Leverage the Actions Center to conveniently act on incidents and other important information.
