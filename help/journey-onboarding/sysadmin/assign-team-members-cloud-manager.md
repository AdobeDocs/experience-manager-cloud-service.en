---
title: Assigning Team Members to Cloud Manager Product Profiles
description: Follow this page to learn how to assign team members to Cloud Manager Product profiles
feature: Onboarding
role: Admin, User, Developer
exl-id: 555688e5-f937-462c-9fcc-b90685f1882b
---
# Assign Team Members to Cloud Manager Product Profiles {#assign-team-members}

Once you have learnt how to login to [Admin Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/admin-console.html?lang=en) and viewed your privileges as a [System Administrator](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/system-administrator.html?lang=en), you are now ready to assign team members to Cloud Manager Product profiles.

## Objective {#objective}

This document summarizes how to assign team members to Cloud Manager product profiles from the Adobe Admin Console. 

After reading this section you should be able to:

* Understand why and how you must add team members.
* Learn about three different Cloud Manager product profiles such as Business Owner, Deployment Manager, and Developer.
* Assign team members to Cloud Manager product profiles such as Business Owner, Deployment Manager, and Developer.

## Prerequisites {#prerequisites}

The following prerequisites should be considered before starting this section. You must:

* Be a System Administrator and understand [Cloud Manager Product Profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles).
* Understand [Adobe Admin Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/admin-console.html?lang=en) basics. 
* Have details about your team members. A System Administrator must have the names, email addresses, and the roles and responsibilities for the team members who will need access to AEM as a Cloud Service. 

   >[!NOTE]
   >For the purpose of onboarding, we recommend that you initially add users who will participate in the immediate tasks, such as administrators, developers and content authors. You can continue the rest of the onboarding without adding all users. After you have finished onboarding, you can scale to a larger number of users later.

## Review Cloud Manager Product Profiles {#review-product-profiles}

From the Adobe Admin Console you can see the list of Cloud Manager Profiles. 

>[!NOTE]
>Before you review the Cloud Manager product profiles from Admin Console, it is recommended to review the available [Cloud Manager Product Profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles).

Follow the steps below to view list of Cloud Manager Profiles:

1. Log in to [Adobe Admin Console](https://adminconsole.adobe.com/
). From the **Overview** page, select **Adobe Experience Manager as a Cloud Service** from the **Products and services** card.

   ![](/help/journey-onboarding/assets/assign-team1.png)

   >[!NOTE]
   >Refer to Logging in to Admin Console to learn how to use Admin Console.


1. Navigate to the **Cloud Manager** instance from the list of all instances. 

    ![](/help/journey-onboarding/assets/assign-team2.png)

1. You will see the list of pre-configured [Cloud Manager product profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles). 
   
   ![](/help/journey-onboarding/assets/assign-team3.png)


## Assign Users to Business Owner Product Profile {#assign-users-business-owner}

You are now ready to add users and assign them to Cloud Manager Business Owner product profile.

>[!NOTE]
>In order to successfully do this, from Adobe Admin console you must add a user to both the product (AEM as a Cloud Service in this case), and [Cloud Manager Business Owner product profile](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles).

The following steps will walk you through this:

1. Identify the user(s) who will manage Cloud Manager Programs and add them to the Business Owner product profile. The System Administrator must be the first person to access and log in to Cloud Manager. You must add yourself (System Administrator) to the Business Owner product profile first. 

1. In [Admin Console](https://adminconsole.adobe.com/enterprise/overview) **Overview** page, select **Adobe Experience Manager as a Cloud Service** product from **Products and services** card as shown below.

   ![](/help/journey-onboarding/assets/assign-team1.png)

1. Select the **Users** tab from the top navigation, then select **Add User**.

   ![](/help/journey-onboarding/assets/assign-team4.png)

1. In **Add users to your team** dialog box, type the email ID of the user you want to add. For the ID Type, select Adobe ID, if the Federated ID for your team members has not yet been set up.

   ![](/help/journey-onboarding/assets/assign-team5.png)

1. In the Product selection, select **Adobe Experience Manager as a Cloud Service** and assign **Business Owner** product profile to the user as shown below. 

   >[!NOTE]
   >Refer to [Cloud Manager product profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles) to ensure that the right users are assigned the right role(s) in Admin Console, as shown below.

   ![](/help/journey-onboarding/assets/assign-team6.png)

   >[!NOTE]
   >Assign the user to at least one product profile so that the user can access Cloud Manager. Remember to assign yourself (System Administrator) to Business Owner.

1. Click **Save**. A welcome email is sent to the user you added. The invited user can access Cloud Manager by clicking the link in the welcome email and signing in using their Adobe ID.

   Congratulations! Your newly formed Cloud Manager team (including yourself assigned to the ‘Business Owner’ role) has been setup. Members will receive a welcome email inviting them to login and access Cloud Manager. In the role of Business Owner, you are now just one step away from logging in to Cloud Manager and enabling the creation of your cloud resources.

## Assign Users to Deployment Manager Product Profile {#assign-users-deployment-manager}

1. Identify the user(s) who will manage Cloud Manager Programs and add them to the Deployment Manager product profile. The System Administrator must be the first person to access and log in to Cloud Manager. You must add yourself (System Administrator) to the Business Owner product profile first (as described in the previous section).

1. In [Admin Console](https://adminconsole.adobe.com/enterprise/overview) **Overview** page, select **Adobe Experience Manager as a Cloud Service** product from **Products and services** card as shown below.

   ![](/help/journey-onboarding/assets/assign-team1.png)

1. Select the **Users** tab from the top navigation, then select **Add User**.

   ![](/help/journey-onboarding/assets/assign-team4.png)

1. In **Add users to your team** dialog box, type the email ID of the user you want to add. For the ID Type, select Adobe ID, if the Federated ID for your team members has not yet been set up.

   ![](/help/journey-onboarding/assets/assign-team5.png)

1. In the Product selection, select **Adobe Experience Manager as a Cloud Service** and assign **Deployment  Manager** product profile to the user as shown below. 

   >[!NOTE]
   >Refer to [Cloud Manager product profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles) to ensure that the right users are assigned the right role(s) in Admin Console as seen below.

   ![](/help/journey-onboarding/assets/assign-team6.png).

   >[!IMPORTANT]
   >User can be added to the Deployment Manager product profile after Cloud Manager resources are created.

## Assign Users to Developer Product Profile {#assign-users-developer}

1. Identify the user(s) who will manage Cloud Manager Programs and add them to the Developer product profile. The System Administrator must be the first person to access and log in to Cloud Manager. You must add yourself (System Administrator) to the Business Owner product profile first. 

1. In [Admin Console](https://adminconsole.adobe.com/enterprise/overview) **Overview** page, select **Adobe Experience Manager as a Cloud Service** product from **Products and services** card as shown below.

   ![](/help/journey-onboarding/assets/assign-team1.png)

1. Select the **Users** tab from the top navigation, then select **Add User**.

   ![](/help/journey-onboarding/assets/assign-team4.png)

1. In **Add users to your team** dialog box, type the email ID of the user you want to add. For the ID Type, select Adobe ID, if the Federated ID for your team members has not yet been set up.

   >[!NOTE]
   >To learn more about identity types on Adobe Admin Console, refer to [Identity overview](https://helpx.adobe.com/enterprise/using/identity.html).

   ![](/help/journey-onboarding/assets/assign-team5.png)

1. In the Product selection, select **Adobe Experience Manager as a Cloud Service** and assign **Developer** product profile to the user as shown below. 

   >[!NOTE]
   >Refer to [Cloud Manager product profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles) to ensure that the right users are assigned the right role(s) in Admin Console as seen below.

   ![](/help/journey-onboarding/assets/assign-team6.png).


   >[!IMPORTANT]
   >User can be added to the Developer product profile after Cloud Manager resources are created.

## What’s Next {#whats-next}

You have learned about three different Cloud Manager product profiles such as Business Owner, Deployment Manager, and Developer. Next you assigned team members to Cloud Manager product profiles such as Business Owner, Deployment Manager, and Developer. You are now ready to continue your onboarding journey by next reviewing the document [Setup Cloud Resources via Cloud Manager](/help/journey-onboarding/sysadmin/setup-cloud-resources-via-cloud-manager.md), where you will learn:

1. As a System Administrator assigned to the *Business Owner* role, you must access and login to Cloud Manager. 

1. Next, a Cloud Manager user in the *Business Owner* role can login and setup your cloud resources including your cloud Program and Environments. This will ensure that your team of experts can begin accessing AEM as a Cloud Service as soon as possible.

1. After your *Business Owner* has setup your cloud resources, *Developers* and *Deployment Managers* who have been successfully added to the Cloud Manager product profiles can access Cloud Manager and familiarize themselves on how they can continue on their learning path.

## Additional Resources {#additional-resources}

Follow the additional resources to learn about:

* [Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/cloud-manager-introduction.html?lang=en)
* [Cloud Manager Product Profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles)
* [Admin Console Identity Overview](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/identity.ug.html)
