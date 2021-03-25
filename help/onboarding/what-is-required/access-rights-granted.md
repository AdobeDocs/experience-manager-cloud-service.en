---
title: Access Rights Granted - What Is Required
description: Access Rights Granted - What Is Required
---

# Access Rights Granted {#access-rights-granted} 

Adobe will create an **Organization** identifier for your company in the Adobe Identity Management System (IMS), where all your users and their permissions can be managed. Each user, who needs to be a member of this organization, and will be granted access to any of the [!UICONTROL Experience Cloud] service, will need to have their own **Adobe ID**. 

## User Identity Types {#user-identity-types}

To get started with an Adobe ID, please visit [Manage Adobe Identity Types](https://helpx.adobe.com/enterprise/using/identity.html) for detailed instructions on how to obtain an Adobe ID using one of the identity types available.

## Users and Roles {#users-and-roles}

Once Adobe has created an organization for your company, your designated administrator will be added as the first member to this organization. The administrator will be granted the administrator permissions by default, and assigned the [!UICONTROL AEM Managed Services] **Product**, and one or more [!UICONTROL Cloud Manager] **Product Profiles**. 

1. Once your System Administrator grants you access to Cloud Manager, you will receive an email that will take you to Cloud Manager login page which is also accessible through [Adobe Experience Cloud](https://my.cloudmanager.adobe.com/).

1. From the landing page of the Cloud Manager, click on **Manage Access**.

   ![](/help/onboarding/getting-access-to-aem-in-cloud/assets/sys-admin5.png)

1. Once you click on **Manage Access**, you are navigated to **Admin Console** from where you can manage the user roles or permissions to Cloud Manager.

   ![](/help/onboarding/getting-access-to-aem-in-cloud/assets/sys-admin1.png)

   From the Admin Console you can perform SysAdmin tasks such as:
   * [Managing Roles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/navigation.html?lang=en#manage-roles)
   * [Managing Access to Author Instance](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/navigation.html?lang=en#manage-access-aem)

      >[!NOTE]
      >Please visit the section [Users and Roles](#users-roles) to learn more about users and role definitions in Cloud Manager.

With these rights granted, your administrator is now set up with a single sign-on (using Adobe ID) to access the [!UICONTROL Experience Cloud] services, login to your AEM cloud environments, and use [!UICONTROL Cloud Manager].

Many features in [!UICONTROL Cloud Manager] require specific permissions to operate.

[!UICONTROL Cloud Manager] currently defines four roles for users which govern the availability of specific features:

* Business Owner
* Program Manager
* Deployment Manager
* Developer

>[!CAUTION]
>To use [!UICONTROL Cloud Manager], you must have an Adobe ID and the Adobe Experience Manager as a Cloud Service Product Context.

### Role Definitions {#role-definitions}

>[!NOTE]
>
>The Developer persona in Admin Console is unrelated to the Developer role in [!UICONTROL Cloud Manager].

The following table summarizes the roles:

|[!UICONTROL Cloud Manager] Roles|Description|
|--- |--- |
|Business Owner|Responsible for defining KPIs, approving production deployments and overriding important 3-tier failures.|
|Program Manager|Uses [!UICONTROL Cloud Manager] to perform team setup, review status and view KPIs. Can approve important 3-tier failures.|
|Deployment Manager|Manages deployment operations. Uses [!UICONTROL Cloud Manager] to execute stage/production deployments. Can edit CI/CD Pipelines. Can approve important 3-tier failures. Can get access to the Git repository.|
|Developer|Develops and tests custom application code. Primarily uses [!UICONTROL Cloud Manager] to view status. Can get access to the Git repository for code commit.|
|Content Author|Generally does not interact with [!UICONTROL Cloud Manager]. May use [!UICONTROL Cloud Manager] Program Switcher (having navigated from [!UICONTROL Experience Cloud]) to access AEM.|

### The Integration Product Profile {#integration-product-profile}

In addition to the above, Cloud Manager will automatically create a product profile named "Integrations - Cloud Service". This product profile is used for the integrations between Adobe Experience Manager and other Adobe products. This product profile **must** not be deleted. If you do accidentally delete this profile, it will need to be manually recreated. The Display Name for this profile **must** be `CM_CS_DEFAULT`.

