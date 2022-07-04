---
title: Assign Team Members to AEM as a Cloud Service Product Profiles
description: Follow this page to learn how to assign team members to AEM as a Cloud Service Product Profiles
feature: Onboarding
role: Admin, User, Developer
exl-id: c00f5d28-85af-4bd3-a50c-913d1342241c
---
# Assign Team Members to AEM as a Cloud Service Product Profiles {#assign-team-members-cloud-service}

## Objective {#objective}

This document helps you understand the steps that your System Administrator must take to assign your team members to AEM as a Cloud Service product profiles and why it is crucial to enable your AEM Authors to embark on their journey with AEM. 

After reading this section you should understand:

* Why and how your team members are assigned to AEM as a Cloud Service product profiles.
* How to add team members to AEM User product profile.
* How to add team members to AEM Administrators product profile.


## Introduction {#introduction}

To be granted access to AEM as a Cloud Service users must belong to one of two product profiles:  `AEM Users` or `AEM Administrators`. Your team members must be granted permissions to the AEM instance, since permissions to administer Cloud Manager will not suffice.

>[!NOTE]
>Every user assigned to AEM User product profile by the system administrator will have (read-only) access to Cloud Manager.

## Pre-requisites {#prerequisites}

Before you start reading this section, you should consider following these pre-requisites:

* Understand [AEM as a Cloud Service product profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#aem-product-profiles)
* Be familiar with [Admin Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/admin-console.html?lang=en)
* Cloud Manager product profiles have been assigned to your team members as appropriate, and cloud resources have been setup
* Details about your team member: System Administrator must have the names and email addresses and the roles and responsibilities for the team members who will need access to AEM as a Cloud Service. 

   >[!NOTE]
   >For the purpose of onboarding, we recommend that you initially add users who will participate in the immediate tasks, such as administrators, developers and content authors. You can continue the rest of the onboarding without adding all users. After you have finished onboarding, you can scale to a larger number of users later.


   >[!IMPORTANT]
   >Before you start reviewing the steps for assigning team members to AEM as a Cloud Service Product Profiles, please ensure that you follow these two steps:
   >
   >1. Log in to [Adobe Admin Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/admin-console.html?lang=en). Refer to Logging in to Admin Console for more details.
   >
   >1. Review [AEM as a Cloud Service Product Profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#aem-product-profiles). 

Follow the steps below to see the list of Cloud Manager Profiles from Adobe Admin Console:

1. Log in to [Adobe Admin Console](https://adminconsole.adobe.com/
). From the **Overview** page, select **Adobe Experience Manager as a Cloud Service** from the **Products and services** card.

   ![](/help/journey-onboarding/assets/assign-team1.png)   

1. Navigate and select the instance (Author instance of Development environment) as shown in the picture below.

   ![](/help/journey-onboarding/assets/cloud-profiles-1.png)


1. You will see the list of AEM as a Cloud Service product profiles that will be need to assigned to a user based on their role. 

    >[!NOTE]
    >To learn more about these, see [AEM as a Cloud Service Product Profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#aem-product-profiles).

   ![](/help/journey-onboarding/assets/cloud-profiles-2.png)


## Add Team Members to AEM User or AEM Administrator Product Profile {#add-team-members}

To be granted access to AEM as a Cloud Service instance users must belong to one of two product profiles `AEM Users` or `AEM Administrators`. 

>[!NOTE]
>You must be granted permissions to the instance, permissions to administer the Cloud Manager will not suffice. Learn more. 

The steps below must be followed by a System Administrator who is also in the Business Owner role.

1. Navigate to your program from Cloud Manager and select the **Manage Access** button from the context of the environment of interest as shown below.

   ![](/help/journey-onboarding/assets/add-team1.png)

1. A new tab navigates you to Adobe Admin Console from where you have access to the author instance of the environment. Select **AEM Administrators** or **AEM Users** based on the permissions this individual needs to be give. Learn more about [AEM as a Cloud Service product profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#aem-product-profiles). 

   ![](/help/journey-onboarding/assets/add-team2.png)

1. Select `AEM Administrator` or `AEM User` and click on **Add User** as shown below and submit the necessary details to complete adding the team member.

   ![](/help/journey-onboarding/assets/add-team3.png)

   The user you added will now have access to the AEM as a Cloud Service Author services!

   >[!NOTE]
   >You will want to repeat these steps for all environments including Development, Stage and Production, if you have the information of team members who need access available.


## What’s Next {#whats-next}

The users that you assigned to AEM as a Cloud Service product profiles are now ready to learn how to access Author and get familiar with authoring pages in AEM as a Cloud Service. You should follow the path, by next reviewing the document Learning Path for [AEM Users](/help/journey-onboarding/sysadmin/learning-path-aem-users.md) or for [Developers and Deployment Managers](/help/journey-onboarding/sysadmin/learning-path-developers-deploymentmanagers.md).

## Additional Resources {#additional-resources}

* [Managing Products and User Access in Admin Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/security/ims-support.html?lang=en#managing-products-and-user-access-in-admin-console)
* [Configuring access to AEM](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/walk-through.html?lang=en)
* [Quick Start Guide to Authoring Pages](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/sites/authoring/getting-started/quick-start.html?lang=en)
