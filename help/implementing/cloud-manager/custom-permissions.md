---
title: Custom Permissions
description: Learn how you can use custom permissions to create custom permission profiles with configurable permissions to restrict access to programs, pipelines, and environments for Cloud Managers users.
exl-id: 167da985-7f19-45b3-90a3-884817907da2
solution: Experience Manager
feature: Security, Developing
role: Admin, Architect, Developer
---

# Custom Permissions {#custom-permissions}

Learn how you can use custom permissions to create custom permission profiles with configurable permissions to restrict access to programs, pipelines, and environments for Cloud Managers users.

## Introduction {#introduction}

Cloud Manager has a set of pre-defined roles which govern access to various Cloud Manager features:

* Business Owner
* Program Manager
* Deployment Manager
* Developer

Custom permissions let users create custom permission profiles with configurable permissions to restrict access for Cloud Managers users to programs, pipelines, and environments.

>[!TIP]
>
>For details on pre-defined roles, see [AEM as a Cloud Service Team and Product Profiles](/help/onboarding/aem-cs-team-product-profiles.md).

## Using Custom Permissions {#using}

To create and use your own custom permissions, it requires three steps:

1. [Create a product profile](#create).
1. [Assign custom permissions to the product profile](#assign-permissions).
1. [Assign users to the product profile](#assign-users).

This section details these steps. You may find it useful to see the [Terms](#terms) and [Configurable Permissions](#configurable-permissions) sections as you create your own custom permissions.

>[!NOTE]
>
>You must have product administrator rights in the Admin Console for Adobe Experience Manager as a Cloud Service to create profiles and manage permissions for Cloud Manager.

### Create a New Product Profile {#create}

First create a product profile before to which you can assign custom permissions.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/).

1. On the Cloud Manager landing page, select the **Manage Access** button. 

  ![Manage Access button](assets/manage-access.png)

1. You are redirected to the **Products** tab of the Admin Console, where you can manage users and permissions for Cloud Manager. In the Admin Console, select the **New Profile** button.

  ![New Profile button](assets/admin-console-new-profile.png)

1. Provide the general details about the profile.

   * **Product profile name** - A descriptive name for the profile
   * **Display name** - An abbreviated name that is shown in the UI (options)
   * **Description** - An informative description of the profile explaining its purpose (optional)
   * **Notify users by email** - Users receive an email notification when they are added to or removed from this profile.

1. Select **Save** when complete.

The new product profile is saved and is visible in the list of product profiles in the Admin Console.

### Assign Custom Permissions to Profile {#assign-permissions}

Now that you have a new product profile, you can assign custom permissions to it.

1. In the Admin Console, select the name of the [new product profile you created](#create).

1. In the window that opens, select the **Permissions** tab to view a list of editable permissions.

   ![Editable permissions](assets/permissions-tab.png)

1. Select the **Edit** link of a permission so you can edit it.

1. The **Edit Permission** window opens.
   * The permission you selected in the previous step is selected in the left column.
   * The permission items available for assignment for the permission are in the middle column labeled **Available Permission** Items.
   * The assigned permission items are in the right column labeled **Included Permission Items**.

   ![Edit permission items](assets/edit-permission-items.png)

1. Select the plus (`+`) icon next to the permission item so you can add it to the column **Included Permission Items**.

   * Select the `i` icon next to a permission item if you want to learn more about it.

1. Select the **Add all** button at the top of the **Available Permissions** column so you can add all permissions.

1. Select **Save** when you are finished defining the permission items for your new product profile.

Your new product profile is now saved with its custom permissions.

### Assign Users to the Custom Permissions {#assign-users}

You can now assign users to the new product profile you created with custom permissions.

1. In the Admin Console, select the name of the [new product profile to which you assigned custom permissions](#assign-permissions).

1. In the window that opens, select the **Users** tab.

1. Select the **Add Users** button and assign users to your new product profile with custom permissions.

See the section **Add users and user groups to a product profile** of the document [Manage product profiles for enterprise users](https://helpx.adobe.com/enterprise/using/manage-product-profiles.html) for more details on how to use the Admin Console.

## Configurable Permissions {#configurable-permissions}

The following permissions are available for creating custom profiles.

| Permission | Description |
| --- | --- |
| Program Create | Let users create a program. |
| Program Access | Let users access programs. |
| Program Edit | Let users edit programs. |
| Environment Create | Let users create an environment. |
| Environment Edit | Let users update and edit environments. |
| Environment Logs Read | Let users read environment logs. |
| Environment Variables Manage | Let users create/edit/delete environment configurations. |
| Environment Restore Create | Let users create an environment restore. |
| Rapid Development Environment Reset | Let users reset the Rapid Development Environment (RDE). |
| Content Copy Manage | Let users manage content copy operations. |
| Pipeline Create | Let users create pipelines. |
| Pipeline Delete | Let users delete pipelines. |
| Pipeline Edit | Let users edit pipelines. |
| Production Deployments Approve/Reject | Let users approve or reject a production deployment step. |
| Pipeline Executions Cancel | Let users cancel pipeline executions. |
| Pipeline Executions Start | Let users start a new pipeline execution. |
| Override/Reject Important Metric Failures | Let users override/reject important metric failures. |
| Production Deployments Schedule | Let users schedule a production deployment step. |
| Repository Info Access | Let users access repository info and generate an access password. |
| Repository Create | Let users create Git repositories. |
| Repository Delete | Let users delete Git repositories. |
| Repository Edit | Let users edit Git repositories. |
| Repository Code Generate | Let users generate a project from archetype. |
| Domain Name Manage | Let users create/edit/delete domain names. |
| IP Allowlist Manage | Let users create/edit/delete IP allowlist and IP allowlist binding. |
| Network Infrastructure Manage | Let users create/edit/delete network infrastructure. |
| SSL Certificate Manage | Let users create/edit/delete SSL certificate. |
|New Relic Sub Account User Manage | Let users read/edit New Relic subaccount users. |

### Organization-Level Permissions {#organization-level}

Organization-level permissions refer to permissions which are always given across all programs in an organization.

The following permissions are organization-level permissions:

* **Program Create** - This permission lets users create a program in the organization.
* **Repository Info Access** This tenant/organization level permission allows users to generate a username, password, and repository URL for access and contributing to a customer project.
  * The username and password for repository access is common across all the repositories in the organization. However, the repository URL is unique to each program.
  * See [Accessing Repositories](/help/implementing/cloud-manager/managing-code/accessing-repos.md) for more information.

## Terms {#terms}

The following terms are used in creating and managing custom permissions and pre-defined roles.

| Term | Description |
| --- | --- |
| Predefined Permissions | Predefined roles like **Business Owner** and **Deployment Manager** to govern various features of Cloud Manager. For details on pre-defined roles, see [AEM as a Cloud Service Team and Product Profiles](/help/onboarding/aem-cs-team-product-profiles.md). |
| Custom Permissions | Cloud Manager features let users create permission profiles to define roles to govern the supported features of Cloud Manager. |
| Product Profile | Created in the Admin Console to manage configurable permissions that are applicable to users who are part of the permission profile. | 
| Configurable Permission | Cloud Manager permissions that you can configure in the permission profile. |
| Permission Item | A program, environment, or pipeline resource on which a permission can be applied. |

Permission items refer to the scope where permission is applied. Typically, it is one of the following.

| Permission Item Type | Example | Description |
| --- | --- | --- |
| Organization|organization:companyA | All applicable resources of an organization. A resource could be a program, environment, or pipeline. If the user adds an organization for any permission, then all new resources in that organization also have that permission. |
| Program | Program A | All applicable resources of a program. |
| Environment | Program A : environment | Applicable to a specific environment. |
| Pipeline | Program A : Pipeline | Applicable to a specific pipeline. |

## Usage notes {#usage-notes}

* A custom permissions profile also lists AMS programs, environments, and pipelines while configuring permissions.
* Resources like program, environment, and pipeline that were created in Cloud Manager may take up two minutes to display in Admin Console for permission configuration.
* In rare scenarios where a custom permissions service fails to respond, predefined profiles are still available and users in predefined profiles still have appropriate access.

## Frequently Asked Questions {#faq}

### Which permission profiles are predefined permission profiles?

* Business Owner
* Program Manager
* Deployment Manager
* Developer

For details on pre-defined roles, see [AEM as a Cloud Service Team and Product Profiles](/help/onboarding/aem-cs-team-product-profiles.md).

### What happens to predefined permission profiles with introduction to custom profiles?

Default product profiles and Cloud Manager roles continue to work the same as before.

### Can I edit predefined permission profiles?

No, default profiles are non-editable. You cannot add or remove permissions to the default permission profile. You can only add or remove users from predefined profiles.

### Should I delete predefined permission profiles since custom profiles are now available?

Do not delete predefined permission profiles from the Admin Console. 

### Can I add users to multiple permission profiles?

Yes, A user can be part of multiple profiles including predefined and custom permission profiles. When a user is assigned to multiple profiles, the combined permissions from all the assigned permission profiles are available to that user.

### What happens if a user has permission to edit an environment/pipeline but doesn't have access to a program which contains the environment/pipeline?

In this case, the user is unable to access the environment or pipeline if they do not have the **Program Access** permissions containing the environment or pipeline.
