---
title: Assigning AEM Product Profiles
description: Once you have your cloud resources configured, you will need to grant your team access to AEM itself using AEM product profiles.
feature: Onboarding
role: Admin, User, Developer
exl-id: c00f5d28-85af-4bd3-a50c-913d1342241c
---
# Assigning AEM Product Profiles {#assign-profiles-aem}

In this part of the [onboarding journey,](overview.md) you will learn how to grant you team access to AEM using AEM product profiles.

## Objective {#objective}

Once you have read the previous document in this onboarding journey, [Create Environments,](create-environments.md) and have your cloud resources configured, you will need to grant your team access to AEM itself using AEM product profiles. As the system administrator, you do this by assigning AEM product profiles.

After reading this document you should understand:

* What AEM product profiles are. 
* How to add team members to AEM User product profile.
* How to add team members to AEM Administrators product profile.

## AEM Product Profiles {#aem-product-profiles}

To use AEM, your team members must be assigned to at least one AEM product profile. Permissions to access Cloud Manager will not suffice. Users must belong to one of two product profiles:

* `AEM Users` - This group includes normal users who perform everyday content authoring tasks.
* `AEM Administrators` - This group includes users who are responsible for advanced features or AEM.

Every user assigned to an AEM product profile will also gain read-only access to Cloud Manager. Write access to Cloud Manager may be granted via other product profiles.

## Prerequisites {#prerequisites}

Before you start reading this section, you should have the following information available about your team who will use AEM.

* Names
* Email addresses
* Roles and responsibilities

>[!TIP]
>
>For the purpose of onboarding, we recommend that you initially add users who will participate in the immediate tasks, such as administrators, developers and content authors. You can continue the rest of the onboarding without adding all users. After you have finished onboarding, you can scale to a larger number of users later.

## View AEM Product Profiles {#view-profiles}

Follow these steps to see the AEM product profiles from the Admin Console.

1. Log in to Admin Console at [`https://adminconsole.adobe.com`.](https://adminconsole.adobe.com)

1. From the **Overview** page, select **Adobe Experience Manager as a Cloud Service** from the **Products and services** card.

   ![Products and services card](/help/journey-onboarding/assets/assign-team1.png)   

1. Navigate and select the instance.

   ![Select instance](/help/journey-onboarding/assets/cloud-profiles-1.png)

1. You will see the list of AEM as a Cloud Service product profiles that can be assigned to a user based on their roles.

   ![Product profiles](/help/journey-onboarding/assets/cloud-profiles-2.png)

## Add Team Members to Product Profiles {#add-team-members}

Now that you are familiar with the available profiles, you can assign them as necessary to your team members.

These tasks require you to be a system administrator with the **Business Owner** Cloud Manager product profile.

1. Navigate to your program from Cloud Manager and select the **Manage Access** button from the context of the environment of interest.

   ![Mange access](/help/journey-onboarding/assets/add-team1.png)

1. A new tab navigates you to the Admin Console from where you have access to the author instance of the environment. Select **AEM Administrators** or **AEM Users** based on the permissions this individual needs to be given.

   ![Assign access](/help/journey-onboarding/assets/add-team2.png)

1. Select `AEM Administrator` or `AEM User` and click on **Add User** as shown below and submit the necessary details to complete adding the team member.

   ![Add team member](/help/journey-onboarding/assets/add-team3.png)

1. Repeat these steps for all environments including development, staging and production, if you have the information of team members who need access available.

The user you added will now have access to the AEM as a Cloud Service Author services!

## End of the Journey? {#the-end}

Congratulations! The users that you assigned to AEM as a Cloud Service product profiles are now ready to access the AEM authoring environment and start creating content with AEM as a Cloud Service. Likewise, developers can now access Cloud Manager to use git to store custom application code and deploy it. In this sense, your onboarding journey is complete and your users can now use AEMaaCS.

However if you would like to better understand how authors and developers use the system, you can continue on with two optional parts of this onboarding journey:

* [Developer and Deployment Manager Tasks](developers.md) - Where you will learn how developers access git to store their custom code and deploy it using Cloud Manager pipelines.
* [AEM User Tasks](aem-users.md) - Where you will learn how to access the AEM environment where you can start creating content.

## Additional Resources {#additional-resources}

* [Managing Products and User Access in Admin Console](/help/security/ims-support.md#managing-products-and-user-access-in-admin-console) - Learn how to use the Admin Console to manage use access.
* [Configuring access to AEM walk-through](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/walk-through.html?lang=en) - Check out this abridged walk-though to learn about configuring Adobe IMS users, user groups, and product profiles in the Admin Console.

