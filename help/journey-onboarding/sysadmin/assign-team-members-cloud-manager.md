---
title: Assigning Team Members to Cloud Manager Product Profiles
description: Follow this page to learn how to assign team members to Cloud Manager Product profiles
feature: Onboarding
role: Admin, User, Developer
exl-id: 555688e5-f937-462c-9fcc-b90685f1882b
---
# Assign Team Members to Cloud Manager Product Profiles {#assign-team-members}

In the previous step in this journey, [Get Started with Onboarding Process](/help/journey-onboarding/sysadmin/get-started-onboarding-journey.md), you learned now log in to the Admin Console and viewed your privileges as a System Administrator. You are now ready to assign team members to Cloud Manager Product profiles.

## Objective {#objective}

This document summarizes how to assign team members to Cloud Manager product profiles from the Adobe Admin Console. Once assigned, these members can then create an access cloud resources as described in the next step of this journey.

After reading this section you should be able to:

* Understand why and how you must add team members.
* Learn about three important Cloud Manager product profiles: **Business Owner**, **Deployment Manager**, and **Developer**.
* Assign team members to Cloud Manager product profiles.

>[!TIP]
>
>For the purpose of onboarding, Adobe recommend that you initially add users who will participate in the immediate tasks, such as administrators, developers, and content authors. You can continue the onboarding process without adding all users. After you have finished onboarding, you can add additional users.

## Prerequisites {#prerequisites}

The following prerequisites should be fulfilled before starting this section. You must:

* Be a System Administrator and understand Cloud Manager product profiles.
  * Return to the [Onboarding Journey overview](onboarding-journey-overview.md) if you are not familiar with these concepts.
* Understand Adobe Admin Console basics.
  * Return to the [Onboarding Journey overview](onboarding-journey-overview.md) if you are not familiar with these concepts.
* Have details about your team members, who will need to access AEM as a Cloud Service, including
  * Names
  * Email addresses
  * Roles and responsibilities 

## Review Cloud Manager Product Profiles {#review-product-profiles}

From the Adobe Admin Console you can see the list of Cloud Manager profiles. 

1. Log in to Adobe Admin Console at [adminconsole.adobe.com](https://adminconsole.adobe.com/) and from the **Overview** page, select **Adobe Experience Manager as a Cloud Service** from the **Products and services** card.

   ![AEM as a product](/help/journey-onboarding/assets/assign-team1.png)

1. Navigate to the **Cloud Manager** instance from the list of all instances. 

    ![Cloud Manager](/help/journey-onboarding/assets/assign-team2.png)

1. You will see the list of pre-configured Cloud Manager product profiles. 
   
   ![Product profiles](/help/journey-onboarding/assets/assign-team3.png)

## Assign Users to Business Owner Product Profile {#assign-users-business-owner}

You are now ready to add users and assign them to the **Business Owner** product profile.

>[!NOTE]
>In order to successfully do this, from Adobe Admin console you must add a user to both the product (AEM as a Cloud Service in this case), and [Cloud Manager Business Owner product profile](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles).

1. Identify the user(s) who will manage Cloud Manager Programs and add them to the Business Owner product profile.

1. Log in to the Admin Console at [adminconsole.adobe.com](https://adminconsole.adobe.com/enterprise/overview) and on the **Overview** page, select **Adobe Experience Manager as a Cloud Service** product from **Products and services** card.

   ![Products and services](/help/journey-onboarding/assets/assign-team1.png)

1. Select the **Users** tab from the top navigation, then select **Add User**.

   ![Add user](/help/journey-onboarding/assets/assign-team4.png)

1. In the **Add users to your team** dialog, enter the email ID of the user you want to add.

   * If the federated ID for your team members has not yet been set up, select **Adobe ID** for the **ID Type**.

   ![Add user detail](/help/journey-onboarding/assets/assign-team5.png)

1. Click the plus button under the **Select products or user groups** heading to begin product selection and select **Adobe Experience Manager as a Cloud Service** and assign **Business Owner** product profile to the user.

   * Assign every user to at least one product profile so that the user can access Cloud Manager.
   * Remember to assign yourself as the System Administrator to the **Business Owner** role.

   ![Assigning users](/help/journey-onboarding/assets/assign-team6.png)

1. Click **Save** and a welcome email is sent to the user you added. The invited user can access Cloud Manager by clicking the link in the welcome email and signing in using their Adobe ID.

1. Repeat these steps for the users on your team.

Your newly formed Cloud Manager team (including yourself assigned to the **Business Owner** role) has been set up. In the role of **Business Owner**, you are now just one step away from logging in to Cloud Manager and enabling the creation of your cloud resources.

## Assign Users to Deployment Manager Product Profile {#assign-users-deployment-manager}

1. Identify the user(s) who will manage Cloud Manager Programs and add them to the Deployment Manager product profile.

1. Log in to the Admin Console at [adminconsole.adobe.com](https://adminconsole.adobe.com/enterprise/overview) and on the **Overview** page select **Adobe Experience Manager as a Cloud Service** product from the **Products and services** card.

   ![Products and services](/help/journey-onboarding/assets/assign-team1.png)

1. Select the **Users** tab from the top navigation and then select **Add User**.

   ![Add user](/help/journey-onboarding/assets/assign-team4.png)

1. In the **Add users to your team** dialog, enter the email ID of the user you want to add.

   * If the federated ID for your team members has not yet been set up, select **Adobe ID** for the **ID Type**.

   ![Enter ID](/help/journey-onboarding/assets/assign-team5.png)

1. Click the plus button under the **Select products or user groups** heading to begin product selection and select **Adobe Experience Manager as a Cloud Service** and assign **Deployment  Manager** product profile to the user. 

   ![Assign profile](/help/journey-onboarding/assets/assign-team6.png).

## Assign Users to Developer Product Profile {#assign-users-developer}

1. Identify the user(s) who will manage Cloud Manager Programs.

1. Log in to the Admin Console at [adminconsole.adobe.com](https://adminconsole.adobe.com/enterprise/overview) and on the **Overview** page select **Adobe Experience Manager as a Cloud Service** product from the **Products and services** card.

   ![Products and services](/help/journey-onboarding/assets/assign-team1.png)

1. Select the **Users** tab from the top navigation and then select **Add User**.

   ![Add user](/help/journey-onboarding/assets/assign-team4.png)

1. In **Add users to your team** dialog, enter the email ID of the user you want to add.

   * If the federated ID for your team members has not yet been set up, select **Adobe ID** for the **ID Type**.

   ![Add user ID](/help/journey-onboarding/assets/assign-team5.png)

1. Click the plus button under the **Select products or user groups** heading to begin product selection and select **Adobe Experience Manager as a Cloud Service** and assign **Developer** product profile to the user. 

   ![Assign profile](/help/journey-onboarding/assets/assign-team6.png).

## What’s Next {#whats-next}

In this part of the onboarding journey you learned all about assigning your team members to roles in the Admin Console. You should now:

* Understand why and how you must add team members.
* Understand three important Cloud Manager product profiles: **Business Owner**, **Deployment Manager**, and **Developer**.
* Be able to assign team members to Cloud Manager product profiles.

You are now ready to continue your onboarding journey by next reviewing the document [Setup Cloud Resources via Cloud Manager](/help/journey-onboarding/sysadmin/setup-cloud-resources-via-cloud-manager.md), where you will learn:

1. For your team to be able to access cloud resources, you as a System Administrator assigned to the **Business Owner** role, you must first access and login to Cloud Manager. 
1. How a user with the **Business Owner** role can login and setup your cloud resources including your cloud Program and Environments.
1. How users with the **Developer** and **Deployment Manager** roles can access Cloud Manager.

## Additional Resources {#additional-resources}

It is recommend to continue on the onboarding journey as described previously. These are some additional resources if you wish to do a deep dive on a particular topic from this journey.

* [Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/cloud-manager-introduction.html?lang=en)
* [Cloud Manager Product Profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles)
* [Admin Console Identity Overview](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/identity.ug.html)
