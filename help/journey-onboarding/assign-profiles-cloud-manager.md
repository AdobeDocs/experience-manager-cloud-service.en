---
title: Assigning Team Members to Cloud Manager Product Profiles
description: Follow this page to learn how to assign team members to Cloud Manager product profiles
feature: Onboarding
role: Admin, User, Developer
exl-id: 555688e5-f937-462c-9fcc-b90685f1882b
---

# Assign Team Members to Cloud Manager Product Profiles {#assign-team-members}

In this part of the [onboarding journey](overview.md), you learn how to assign team members to Cloud Manager product profiles.

## Objective {#objective}

In the previous step in this journey, [Accessing the Admin Console](admin-console.md), you learned now log in to the Admin Console and verify your privileges as a system administrator. You are now ready to allow your team members access to Cloud Manager. You do this by assigning product profiles.

When granting users access to an Adobe solution, you do not necessarily want to give them full access. Product profiles enable each solution to have its own set of user permissions. You use the Admin Console to assign product profiles.

Your first step is to grant users access to Cloud Manager. Cloud manager support you with enterprise development setups and its purpose-built CI/CD pipelines, which are equipped to ensure thorough testing and highest code quality to deliver exceptional experiences.

After reading this document, you should:

* Understand what product profiles are.
* Understand what Cloud Manager is.
* Know the three important Cloud Manager product profiles: **Business Owner**, **Deployment Manager**, and **Developer**.
* Be able to assign team members to Cloud Manager product profiles.

## Prerequisites {#prerequisites}

To assign team members to product profiles, you need to have details about your team members, who must access AEM as a Cloud Service, including:

* Names
* Email addresses
* Roles and responsibilities 

>[!TIP]
>
>For the purpose of onboarding, Adobe recommends that you initially add users who will participate in the immediate tasks, such as administrators, developers, and content authors.
>
>You can continue the onboarding process without adding all users. After you have finished onboarding, you can add additional users.

## Product Profiles {#product-profiles}

When granting users access to an Adobe solution, you do not necessarily want to give them full access. Product profiles enable each solution to have its own set of user permissions which are set using the Admin Console.

For example, later in this journey you will use the Admin Console to grant users access to the AEM solution by assigning product profiles for AEM administrators and AEM authors.

However the next step is to grant product profiles so your team members first have access to Cloud Manager.

## Cloud Manager {#cloud-manager}

As system administrator, you know that a successful AEM as a Cloud Service project depends not only on the creation of amazing content using AEM, but also the development and deployment of your own custom code and applications to deliver your AEM content.

Cloud Manager is an integral part of AEM as a Cloud Service and is used to manage your CI/CD pipelines for code deployment, manage your code repositories, and manage your environments.

Before your team can do anything else, they must be onboarded into Cloud Manager by granting them the necessary product profiles. The next steps show you where to find the Cloud Manager product profile using the Admin Console and how to assign them to your team members.

## Review Cloud Manager Product Profiles {#review-product-profiles}

Using the Admin Console you can see the list of Cloud Manager profiles. 

1. Log in to Adobe Admin Console at [adminconsole.adobe.com](https://adminconsole.adobe.com/) and from the **Overview** page, select **Adobe Experience Manager as a Cloud Service** from the **Products and services** card.

   ![AEM as a product](/help/journey-onboarding/assets/assign-team1.png)

1. Navigate to the **Cloud Manager** instance from the list of all instances. 

    ![Cloud Manager](/help/journey-onboarding/assets/assign-team2.png)

1. You can see the list of pre-configured Cloud Manager product profiles. 
   
   ![Product profiles](/help/journey-onboarding/assets/assign-team3.png)

The most important profiles to assign as part of the initial onboarding process are:

* **Business Owner** - These users manage different programs.
* **Deployment Manager** - These users deploy code from your repositories to running AEM environments.
* **Developer** - These users develop your custom AEM applications and commit code to your repositories.

Knowing what these roles are and what they do, review your list of team members to determine who needs which profile. Keep in mind that users can have and often do have multiple roles in your team and therefore also need multiple profiles.

## Assign the Business Owner Product Profile {#assign-business-owner}

You are now ready to add users and assign them to the **Business Owner** product profile.

1. Identify the users who need to manage Cloud Manager programs. These are your **Business Owners**.

1. Log on to the Admin Console at `[adminconsole.adobe.com](https://adminconsole.adobe.com/enterprise/overview)` and on the **Overview** page, select **Adobe Experience Manager as a Cloud Service** product from **Products and services** card.

   ![Products and services](/help/journey-onboarding/assets/assign-team1.png)

1. Select the **Users** tab from the top navigation, then select **Add User**.

   ![Add user](/help/journey-onboarding/assets/assign-team4.png)

1. In the **Add users to your team** dialog, enter the email ID of the user you want to add.

   * If the federated ID for your team members has not yet been set up, select **Adobe ID** for the **ID Type**.

   ![Add user detail](/help/journey-onboarding/assets/assign-team5.png)

1. Click the plus button under the **Select products or user groups** heading to begin product selection and select **Adobe Experience Manager as a Cloud Service** and assign **Business Owner** product profile to the user.

   * Assign every user to at least one product profile so that the user can access Cloud Manager.
   * Remember to assign yourself as the system administrator to the **Business Owner** role.

   ![Assigning users](/help/journey-onboarding/assets/assign-team6.png)

1. Click **Save** and a welcome email is sent to the user you added. The invited user can access Cloud Manager by clicking the link in the welcome email and signing in using their Adobe ID.

1. Repeat these steps for the users on your team.

Your **Business Owner**s have been assigned and can now access Cloud Manager. Don't forget to also assign yourself as system administrator to the **Business Owner** profile.

## Assign the Deployment Manager Product Profile {#assign-deployment-manager}

1. Identify the user(s) who need to deploy code.

1. Log in to the Admin Console at `[adminconsole.adobe.com](https://adminconsole.adobe.com/enterprise/overview)` and on the **Overview** page select **Adobe Experience Manager as a Cloud Service** product from the **Products and services** card.

   ![Products and services](/help/journey-onboarding/assets/assign-team1.png)

1. Select the **Users** tab from the top navigation and then select **Add User**.

   ![Add user](/help/journey-onboarding/assets/assign-team4.png)

1. In the **Add users to your team** dialog, enter the email ID of the user you want to add.

   * If the federated ID for your team members has not yet been set up, select **Adobe ID** for the **ID Type**.

   ![Enter ID](/help/journey-onboarding/assets/assign-team5.png)

1. Click the plus button under the **Select products or user groups** heading to begin product selection and select **Adobe Experience Manager as a Cloud Service** and assign **Deployment  Manager** product profile to the user. 

   ![Assign profile](/help/journey-onboarding/assets/assign-team6.png)

Your **Deployment Manager**s have been assigned and can now access Cloud Manager. Depending on your future responsibilities, you may or may not need to also assign yourself as the system administrator to the **Deployment Manager** profile.

## Assign the Developer Product Profile {#assign-developer}

1. Identify the user(s) who need to develop AEM applications and manage code.

1. Log in to the Admin Console at `[adminconsole.adobe.com](https://adminconsole.adobe.com/enterprise/overview)` and on the **Overview** page select **Adobe Experience Manager as a Cloud Service** product from the **Products and services** card.

   ![Products and services](/help/journey-onboarding/assets/assign-team1.png)

1. Select the **Users** tab from the top navigation and then select **Add User**.

   ![Add user](/help/journey-onboarding/assets/assign-team4.png)

1. In **Add users to your team** dialog, enter the email ID of the user you want to add.

   * If the federated ID for your team members has not yet been set up, select **Adobe ID** for the **ID Type**.

   ![Add user ID](/help/journey-onboarding/assets/assign-team5.png)

1. Click the plus button under the **Select products or user groups** heading to begin product selection and select **Adobe Experience Manager as a Cloud Service** and assign **Developer** product profile to the user. 

   ![Assign profile](/help/journey-onboarding/assets/assign-team6.png).

Your **Developer**s have been assigned and can now access Cloud Manager. Depending on your future responsibilities, you may or may not need to also assign yourself as the system administrator to the **Developer** profile.

## What's Next {#whats-next}

Congratulations! Your newly formed Cloud Manager team (including yourself assigned to the **Business Owner** profile) has been set up. In the role of **Business Owner**, you are now just one step away from logging in to Cloud Manager and enabling the creation of your cloud resources.

In this part of the onboarding journey you learned about assigning your team members to profiles in the Admin Console. You should now:

* Understand what product profiles are.
* Understand what Cloud Manager is.
* Know the three important Cloud Manager product profiles: **Business Owner**, **Deployment Manager**, and **Developer**.
* Be able to assign team members to Cloud Manager product profiles.

You are now ready to continue your onboarding journey by next reviewing the document [Access Cloud Manager](cloud-manager.md), where you learn how to access Cloud Manager and create your project resources.

## Additional Resources {#additional-resources}

It is recommended that you continue the onboarding journey as described previously. These are some additional resources if you want to do a deep dive on a particular topic from this journey.

* [Cloud Manager Introduction](/help/onboarding/cloud-manager-introduction.md) - Learn about Cloud Manager, Cloud Manager programs, and environments.
* [Cloud Manager Product Profiles](/help/onboarding/aem-cs-team-product-profiles.md) - Learn about AEM as a Cloud Service team and product profiles.
* [Identity types on Adobe Admin Console](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/identity.ug.html) - Adobe's identity management system helps admins create and manage user's access to applications and services. Adobe offers these identities types or accounts to authenticate and authorize users.

