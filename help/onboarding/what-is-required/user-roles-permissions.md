---
title: Cloud Manager Roles
description: This page describes user roles and permissions. Follow this page to learn how to add users and assign them to Cloud Manager Roles.
---

# Cloud Manager Roles {#user-roles-permissions}
 
## User Roles {#user-roles}

Many features in Cloud Manager require specific permissions to operate and limits the actions you take within the user interface based on the roles and permissions assigned. In some cases, if you do not have the permission to take an action, the interface control is present, but disabled.

If there is an action you want to take, but cannot, check, the section below, [User Roles and Permissions](#permissions). Depending on your goal, you can contact the System Administrator and request the role you need.

Cloud Manager currently defines four roles for users which govern the availability of specific features:

* Business Owner
* Deployment Manager
* Program Manager
* Developer

>[!NOTE]
>The Developer persona in Admin Console is unrelated to the Developer role in [!UICONTROL Cloud Manager].

## Viewing your Roles {#view-roles}

To view your role in Cloud Manager, sign in to Cloud Manager UI, select your profile icon at the top right corner and select **User Roles**, as shown in the figure below.

>[!NOTE]
>See [Navigate to Cloud Manager](/help/onboarding/what-is-required/navigate-to-cloud-manager.md) to learn more about logging-in to Cloud Manager.

![](/help/onboarding/what-is-required/assets/admin-console-9.png)

### The Integration Product Profile {#integration-product-profile}

In addition to the above, Cloud Manager will automatically create a product profile named "Integrations - Cloud Service". This product profile is used for the integrations between Adobe Experience Manager and other Adobe products. This product profile **must** not be deleted. If you do accidentally delete this profile, it will need to be manually recreated. The Display Name for this profile **must** be `CM_CS_DEFAULT`.


## User Roles and Permissions {#permissions}

[!UICONTROL Cloud Manager] has pre-configured roles with appropriate permissions. For example, a developer develops code and has the permission to push the code to the Git repository. Alternatively, a business owner has different permissions allowing them to add and edit programs, add environments, and approve deployments.

Each of the roles have specific permissions associated with it. For example, if you are in the role of a:

* ***Business Owner***, you have the permission to Add a new program or Edit a program, add or update an environment, add/edit/delete the pipeline and run any pipeline, and deploy code to AEM environment or code quality.

* ***Deployment Manager***, you have the permission to add or update an environment, run any pipeline, and deploy code to AEM environment or code-quality. 

* ***Developer***, you have the permission to generate Personal Access Token to access Git.

    >[!NOTE]
    > A user can be assigned to multiple roles. For example assigning both Business Owner and Deployment Manager roles to a user gives them the combination or sum of these permissions.  


The following table summarizes the roles along with their associated permissions inside Cloud Manager.

|Permission|Description|Business Owner|Deployment Manager|Program Manager|Developer|
|--- |--- |--- |--- |--- |--- |
|Add Program<br>Edit Program|Add a New Program.<br>Edit a program - Add or remove solutions or add-on's|x||||
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

