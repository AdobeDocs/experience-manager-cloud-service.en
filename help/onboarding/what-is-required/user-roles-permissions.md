---
title: User Roles and Permissions
description: This page describes user roles and permissions. Follow this page to learn how to add users and assign them to Cloud Manager Roles.
---

# User Roles and Permissions {#user-roles-permissions}

Adobe will create an **Organization** identifier for your company in the Adobe Identity Management System (IMS), where all your users and their permissions can be managed. Each user, who needs to be a member of this organization, and will be granted access to any of the [!UICONTROL Experience Cloud] service, will need to have their own **Adobe ID**. 

## User Roles {#user-roles}

Many features in Cloud Manager require specific permissions to operate.

Many features in Cloud Manager require specific permissions to operate and limits the actions you take within the user interface based on the roles and permissions assigned. In some cases, if you do not have the permission to take an action, the interface control is present, but disabled.

If there is an action you want to take, but cannot, check [permissions associated with role definitions](#permissions). Depending on your goal, you can contact the System Administrator and request the role you need.

Cloud Manager currently defines four roles for users which govern the availability of specific features:

* Business Owner
* Deployment Manager
* Program Manager
* Developer

>[!NOTE]
>The Developer persona in Admin Console is unrelated to the Developer role in [!UICONTROL Cloud Manager].

## Role Definitions {#role-definitions}

The following table summarizes the roles:

|[!UICONTROL Cloud Manager] Roles|Description|
|--- |--- |
|Business Owner|Responsible for defining KPIs, approving production deployments and overriding important 3-tier failures.|
|Program Manager|Uses [!UICONTROL Cloud Manager] to perform team setup, review status and view KPIs. Can approve important 3-tier failures.|
|Deployment Manager|Manages deployment operations. Uses [!UICONTROL Cloud Manager] to execute stage/production deployments. Can edit CI/CD Pipelines. Can approve important 3-tier failures. Can get access to the Git repository.|
|Developer|Develops and tests custom application code. Primarily uses [!UICONTROL Cloud Manager] to view status. Can get access to the Git repository for code commit.|
|Content Author|Generally does not interact with [!UICONTROL Cloud Manager]. May use [!UICONTROL Cloud Manager] Program Switcher (having navigated from [!UICONTROL Experience Cloud]) to access AEM.|

### Viewing your Roles {#view-roles}

To view your role in Cloud Manager, sign in to Cloud Manager UI, select your profile icon at the top right corner and select **User Roles**, as shown in the figure below.

![](/help/onboarding/what-is-required/assets/admin-console-9.png)

### The Integration Product Profile {#integration-product-profile}

In addition to the above, Cloud Manager will automatically create a product profile named "Integrations - Cloud Service". This product profile is used for the integrations between Adobe Experience Manager and other Adobe products. This product profile **must** not be deleted. If you do accidentally delete this profile, it will need to be manually recreated. The Display Name for this profile **must** be `CM_CS_DEFAULT`.


## Permissions associated with Role Definitions {#permissions}

[!UICONTROL Cloud Manager] has pre-configured roles with appropriate permissions. For example, a developer develops code and has the permission to push the code to the **Git Repository**. Alternatively, a business owner has different permissions allowing them to define the Key Performance Indicators (KPIs) and approve deployments.


Each of the roles have specific permissions associated with each role. The following table summarizes the roles, lists the functions available, and the roles who can execute the function.

|Permission|Description|Business Owner|Deployment Manager|Program Manager|Developer|
|--- |--- |--- |--- |--- |--- |
|Add Program|Add a New Program.|x||||
|Create Environment|Create Prod+Stage, Dev, Environments.|x|x|||
|Update Environment|Update Prod+Stage, Dev, Environments.|x|x|||
|Delete Environment|Delete Non-prod, Dev, Environments.|x|x|||
|Pipeline Setup|Setup or Edit Pipeline.||x|||
|Pipeline Execution|Start the Pipeline.|x|x|||
|Pipeline Execution|Reject/Approve Important 3-Tier Failures.|x|x|x||
|Pipeline Execution|Provide GoLive Approval.|x|x|x||
|Pipeline Execution|Schedule Production Deployment.|x|x|x||
|Pipeline Delete|Allows Deleting of a Pipeline.||x|||
|Execution Cancel|Cancel Current Execution.||x|||
|Generate Personal Access Token|Access Git.||x||x|