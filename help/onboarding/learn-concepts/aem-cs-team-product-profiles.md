---
title: AEM as a Cloud Service Team and Product Profiles
description: Follow this page to learn about AEM as a Cloud Service Team and Product Profiles.
---

# AEM as a Cloud Service Team and Product Profiles {#product-profiles}

AEM as a Cloud Service is the fully cloud-native offering that delivers AEM as a service. It delivers AEM in a cloud native manner, with new attributes like always on, always current, always secure, and always at scale. At the same time, it retains the main value proposition that AEM provides as a customizable platform to customers and allows enterprise grade teams to integrate in their development and delivery procedure. To Refer to [Introduction to Adobe Experience Manager as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/overview/introduction.html?lang=en) to learn more about AEM as a Cloud Service.

Your AEM as a Cloud Service team members will be added and assigned to one or more of the following product profiles via Admin Console during onboarding.


## AEM as a Cloud Service Product Profiles {#aem-product-profiles}
 
The following Product profiles are available in AEM as a Cloud Service team:

* **AEM Administrator**: An AEM Administrator is typically assigned to developers, in particular developers who will need to have access to, for example, the development environments. The AEM Administrators product profile will be used to grant administrator privileges in the associated AEM instance.

* **AEM User**: AEM Users are the users in your organization who use AEM as a Cloud Service as part of the agreement with Adobe. These members will need to access AEM to do their tasks. The AEM Users product profile is typically assigned to an AEM content author who creates and reviews the content (this can be of several types; for example, pages, assets, publications, and so on) before it is published to your website. The AEM Users product profile shown below is assigned to these members.

   >[!NOTE]
   >Every user assigned to an AEM as a Cloud Service product profile has (read only) access to Cloud Manager.

## Cloud Manager Product Profiles {#cloud-manager-product-profiles}

Cloud Manager has pre-configured product profiles, or more simply, role based permissions. Your system administrator will be responsible for setting up your Cloud Manager team by assigning the to these product profiles, and must familiarize themselves with these product profiles, and which team member to assign them to.
>[!NOTE]
>Refer to [Role Based Permissions in Cloud Manager](/help/onboarding/what-is-required/user-roles-permissions.md) for more details.

Each of the product profiles have specific permissions associated with it. For example, if you are in the role of a:

* **Business Owner**, you have the permission to Add a new program or Edit a program, add or update an environment, add/edit/delete the pipeline and run any pipeline, and deploy code to AEM environment or code quality.

* **Deployment Manager**, you have the permission to add or update an environment, run any pipeline, and deploy code to AEM environment or code-quality.

* **Developer**, you have the permission to generate Personal Access Token to access Git.

* **Program Manager**, you have the permission to  access Git.

A user can be assigned to multiple product profiles. For example, assigning both Business Owner and Deployment Manager roles to a user gives them the combination or sum of these permissions. 

Your Cloud Manager team will include at least:

* One Business Owner,  who is typically also the System Administrator, and must be the first person to login and access Cloud Manager 
* One Deployment Manager
* One Developer

   >[!NOTE]
   >To be granted access to AEM as a Cloud Service, users must belong to one of two product profiles `AEM Users-xxx` or `AEM Administrators-xxx`. You must have permissions to the instance. Permissions to administer the associated Cloud Manager will not suffice.