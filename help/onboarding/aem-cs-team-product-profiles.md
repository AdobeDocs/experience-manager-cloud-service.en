---
title: AEM as a Cloud Service Team and Product Profiles
description: Learn how AEM as a Cloud Service team and product profiles can grant and limit access to your licensed Adobe solutions.
exl-id: 7b1474c9-aca0-4354-8798-1abdcda2f6dd
feature: Onboarding
role: "Admin, User, Developer"
---

# AEM as a Cloud Service Team and Product Profiles {#product-profiles}

Learn how AEM as a Cloud Service team and product profiles can grant and limit access to your licensed Adobe solutions.

## Product Profiles {#profiles}

When granting a user access to a specific Adobe solution, you do not necessarily want to give them full access. Product profiles enable each solution to have its own set of user permissions. These are available and accessible via the [Admin Console](/help/journey-onboarding/admin-console.md).

## AEM as a Cloud Service Product Profiles {#aem-product-profiles}

AEM as a Cloud Service is a fully cloud-native offering that delivers AEM as a service. It delivers AEM in a cloud native manner, with new attributes like always on, always current, always secure, and always at scale. At the same time, it retains the main value proposition that AEM provides as a customizable platform to customers and allows enterprise grade teams to integrate in their development and delivery procedure. See [Introduction to Adobe Experience Manager as a Cloud Service](/help/overview/introduction.md) to learn more about AEM as a Cloud Service.

Your AEM as a Cloud Service team members are added and assigned to one or more of the following product profiles via the Admin Console during onboarding.

* **AEM Administrators**: An AEM administrator is typically assigned to developers, in particular developers who need access to, for example, the development environments. The AEM administrator's product profile is used to grant administrator privileges in the associated AEM instance.

* **AEM Users**: AEM users are the users in your organization who use AEM as a Cloud Service generally to create content. These users need to access AEM to do their tasks. The AEM users product profile is typically assigned to an AEM content author who creates and reviews the content. This content can be of many types such as pages, assets, publications, and so on. The AEM users product profile shown below is assigned to these members.

![Product profiles](/help/onboarding/assets/admin-console-profiles.png)

>[!NOTE]
>
>Every user assigned to an AEM as a Cloud Service product profile has read-only access to Cloud Manager via the **Cloud Manager User** role.
>
>Users with only the **Cloud Manager User** role can log into Cloud Manager and navigate to the AEM author environments (if they exist) by using the **Programs** menu options. The **Cloud Manager User** role is not sufficient to access program details. If such access is needed, users must be granted additional roles by their system administrator.

>[!WARNING]
>
>The **AEM Administrators** product profile name must not be changed. Changing the name of the **AEM Administrators** product profile will remove administrator rights from all users assigned to that profile.

>[!TIP]
>
>* To learn more about AEM product profiles, see [Assigning AEM Product Profiles](/help/journey-onboarding/assign-profiles-aem.md).
>* For more information on the onboarding process, see [onboarding journey](/help/journey-onboarding/overview.md).

## Cloud Manager Product Profiles {#cloud-manager-product-profiles}

Cloud Manager has pre-configured product profiles which can be thought of as role-based permissions. Your system administrator is responsible for setting up your Cloud Manager team by assigning them to these product profiles.

>[!TIP]
>
>See [Role Based Permissions in Cloud Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions) for more details.

Each of the product profiles have specific permissions associated with them.

* **Business Owner**
  * In this role you have the permission to add a new program or edit a program, add or update an environment, deploy code to AEM environment, or execute code quality checks.
  * This user is responsible for defining KPIs, approving production deployments, and overriding important 3-tier failures when necessary.
* **Deployment Manager**
  * In this role, you have the permission to add or update an environment, run any pipeline, and deploy code to AEM environment, or execute code quality checks.
  * This user manages deployment operations and uses Cloud Manager to execute staging/production deployments, edit CI/CD pipelines, approve important 3-tier failures when necessary, and can access the git repository.
* **Developer**
  * In this role, you have the permission to generate personal access tokens to access git.
  * This user develops and tests custom application code and primarily uses Cloud Manager to view deployment status and can access the git repository for code commits.
* **Program Manager**
  * In this role, you have the permission to schedule pipelines, override the 3-tier quality gates, and provide production approval.
  * This user uses Cloud Manager to perform team setup, review status, view KPIs, and can approve important 3-tier failures when necessary.

A user can be assigned to multiple product profiles. For example, assigning both **Business Owner** and **Deployment Manage**r roles to a user gives them the sum of these permissions. 

Your Cloud Manager team will include at least:

* One **Business Owner**,  who is typically also the system administrator, and must be the first person to login and access Cloud Manager 
* One **Deployment Manager**
* One **Developer**

>[!NOTE]
>
>To be granted access to AEM as a Cloud Service, users must belong to one of two product profiles: `AEM Users` or `AEM Administrators`. Permissions to administer Cloud Manager will not suffice.

>[!TIP]
>
>* To learn more about Cloud Manager product profiles, see [Assigning Team Members to Cloud Manager Product Profiles](/help/journey-onboarding/assign-profiles-cloud-manager.md).
>* For more information on the onboarding process, see [onboarding journey](/help/journey-onboarding/overview.md).
