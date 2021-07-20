---
title: Assigning Team Members to AEM as a Cloud Service Product Profiles 
description: Follow this page to learn how to assign team members to AEM as a Cloud Service Product Profiles
hide: yes
hidefromtoc: yes
index: no
---

# Assigning to AEM as a Cloud Service Product Profiles {#assign-team-members-cloud-service}

## Objective {#objective}

This document helps you understand the steps that your System Administrator must take to assign your team members to AEM as a Cloud Service product profiles and why it is crucial to enable your AEM Authors to embark on their journey with AEM. 

After reading this section you should:

* Understand why and how your team members are assigned to AEM as a Cloud Service product profiles 
* Understand how to add team members to AEM User product profile
* Understand how to add team members to AEM Administrators product profile


## Introduction {#introduction}

To be granted access to AEM as a Cloud Service users must belong to one of two product profiles, 'AEM Users' or 'AEM Administrators'. Your team members must be granted permissions to the AEM instance, since permissions to administer Cloud Manager will not suffice. Learn more.

>[!NOTE]
>Every user assigned to AEM User product profile by the system administrator will have (readonly) access to Cloud Manager.

## Pre-requisites {#prerequisites}

* Understand AEM as a Cloud Service product profiles
* Be familiar with Admin Console
* Cloud Manager product profiles have been assigned to your team members as appropriate, and cloud resources have been setup
* Details about your team member: System administrator must have the names and email addresses and the roles and responsibilities for the team members who will need access to AEM as a Cloud Service. For the purpose of onboarding, we recommend that you initially add users who will participate in the immediate tasks, such as administrators, developers and content authors. You can continue the rest of the onboarding without adding all users. After you've finished onboarding, you can scale to a larger number of users later.


1. Log in to Admin Console
(Same as before)

1. Review AEM as a Cloud Service Product Profiles
From Admin Console you can see the list of Cloud Manager Profiles. To do this:

1. Once you're logged in to Adobe Admin Console, select Adobe Experience Manager as a Cloud service from the Products and Services card:

1. Navigate and select the instance (Author instance of Development environment) as shown in the picture below.



   Now you will be able to see the list of AEM as a Cloud Service product profiles that will be need to assigned to a user based on their role. To learn more about these go to AEM as a Cloud Service Product Profiles.




## Add team members to AEM User or AEM Administrator Product Profile {#add-team-members}

To be granted access to AEMaaCS instance users must belong to one of two product profiles 'AEM Users' or 'AEM Administrators'. 

>[!NOTE]
>You must be granted permissions to the instance, permissions to administer the Cloud Manager will not suffice. Learn more. 

The steps below must be followed by system administrator who is also in the Business Owner role.

1. From Cloud Manager, navigate to Cloud Manager and select the Manage Access button from the context of the environment of interest as shown below:

1. Once you click on Manage Access, a new TAB navigates you to Admin Console from where you have access to the author instance of the environment. Select "AEM Administrators" or "AEM Users" based on the permissions this individual needs to be give. Learn more about AEM as a Cloud Service product profiles. 

1. Select Add user as shown below and submit the necessary details to complete adding the team member:


1. You will want to repeat these steps for all environments including Development, Stage and Production, if you have the information of team members who need access available.

   The user you added will now have access to the AEM as a Cloud Service Author services!


## What’s Next {#whats-next}

The users that you assigned to AEMaaCS product profiles are now ready to learn how to access Author and get familiar with authoring pages in AEM as a Cloud Service. Learn more.

## Additional Resources {#additional-resources}

Configuring access to AEM (Video walk through)
Quick Start Guide to Authoring Pages
