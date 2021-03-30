---
title: Adding Users and Assigning Cloud Manager Roles 
description: Follow this page to learn how to add users and assign them to Cloud Manager roles
---

# Adding Users and Assigning Cloud Manager Roles {#add-users-assign}

Adobe will create an **Organization** identifier for your company in the Adobe Identity Management System (IMS), where all your users and their permissions can be managed. Each user, who needs to be a member of this organization, and will be granted access to any of the [!UICONTROL Experience Cloud] service, will need to have their own **Adobe ID**. 

## Understanding User Roles {#user-roles}

Many features in Cloud Manager require specific permissions to operate.

Cloud Manager currently defines four roles for users which govern the availability of specific features:

* Business Owner
* Deployment Manager
* Program Manager
* Developer

>[!NOTE]
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

## Adding Users {#add-users}

>[!NOTE]
>You must be a System Administrator to add a user. 

1. If you are a System Administrator, navigate to the [Admin Console](https://adminconsole.adobe.com). Alternatively, you can also  navigate to Cloud Manager where you will see the **Manage Access** button, as described below. 

1. Click on **Manage Access**  button, located on the top right of the Cloud Manager landing page, to open Admin Console in a new tab.

   ![](/help/onboarding/getting-access-to-aem-in-cloud/assets/sys-admin5.png)

   From the **Admin Console**, you can add users to Cloud Manager and assign them to Role(s), referred to as Product Profiles in Admin Console.  

1. Select **Adobe Experience Manager as a Cloud Service** from **Products and services** card as shown below.

   ![](/help/onboarding/what-is-required/assets/admin-console-1.png)

1. Select the **Users** tab from the action  bar and then select **Add User**.

   ![](/help/onboarding/what-is-required/assets/admin-console-2.png)

1.  Select the user and assign appropriate Cloud Manager Role(s) or Product Profile(s) to the user, as shown below.

    ![](/help/onboarding/what-is-required/assets/admin-console-3.png)

      >[!NOTE]
      >Refer to the preceding sections, [User Roles and Permissions](#user-roles) and [Permissions associated with Role Definitions](#permissions) to ensure that the right users are assigned the right Role(s) in the **Admin Console**.

      Now, you have added users to Adobe Experience Manager as a Cloud Service Product Context and are setup with the right Roles or Product Profiles.

      For example, if you are in the role of a:

      * ***Business Owner***, you have the permission to Add a new program or Edit a program, add or update an environment, add/edit/delete the pipeline and run any pipeline, and deploy code to AEM environment or code quality.

      * ***Deployment Manager***, you have the permission to add or update an environment, run any pipeline, and deploy code to AEM environment or code-quality. 

      * ***Developer***, you have the permission to generate Personal Access Token to access Git.

        >[!NOTE]
        > A user can be assigned to multiple roles. For example assigning both Business Owner and Deployment Manager roles to a user gives them the combination or sum of these permissions.
