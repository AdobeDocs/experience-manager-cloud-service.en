---
title: Assigning Team Members to Cloud  Manager Product Profiles 
description: Follow this page to learn how to assign team members to Cloud  Manager Product profiles.
hide: yes
hidefromtoc: yes
index: no
---

# Assigning Team Members to Cloud  Manager Product Profiles {#assign-team-members}

Once you have learnt how to login to Admin Console and viewed your privileges as a System  Administrator, you are now ready to assign team members to Cloud Manager Product profiles.

## Objective {#objective}

This document summarizes how to assign team members to Cloud Manager product profiles from the Admin Console. 

After reading this section you should be able to:

* Understand why and how you must add team members.
* Learn about three different Cloud Manager product profiles such as Business Owner, Deployment Manager, and Developer.
* Assign team members to Cloud Manager product profiles (Business Owner, Deployment Manager, and Developer).


## Review Cloud Manager Product Profiles {review-product-profiles}

From Admin Console you can see the list of Cloud Manager Profiles. 

>[!NOTE]
>Before you review the Cloud Manager product profiles fromAdmin Console, it is recommended to review the available Cloud Manager Product Profiles.

Follow the steps below to view list of Cloud Manager Profiles:

1. Log in to Adobe Admin Console. From the **Overview** page, select Adobe Experience Manager as a Cloud service from the Products and Services card.

   >[!NOTE]
   >Refer to Logging in to Admin Console to learn how to use Admin Console.


1. Navigate to the cloud manager instance from the table with the list of all instances. You will see the list of pre-configured Cloud Manager product profiles.


## Assign Users to Business Owner Product Profile {#assign-users-business-owner}

You are now ready to add users and assign them to Cloud Manager Business Owner product profile.

In order to successfully do this, from Adobe Admin console you must add a user to both the product (AEM as a Cloud Service in this case), and Cloud Manager Business Owner product profile. 

The following steps will walk you through this:

1. Identify the user(s) who will manage Cloud Manager Programs and add them to the Business Owner product profile. The system administrator must be the first person to access and log in to Cloud Manager. You must add yourself (system administrator) to the Business Owner product profile first. 

1. In Admin Console Overview page, select Adobe Experience Manager as a Cloud Service product from products and services card as shown below:

1. Select the Users tab from the top navigation, then select Add User.

1. In the add user dialog box, type the email ID of the user you want to add. For the ID Type, select Adobe ID if the Federated ID for your team members has not yet been set up.

1. In the Product selection, select 'Adobe Experience Manager as a Cloud Service' and assign 'Business Owner' product profile to the user as shown below. Refer to Cloud Manager product profiles to ensure that the right users are assigned the right role(s) in Admin Console as seen below.

1. Assign the user to at least one product profile so that the user can access Cloud Manager. Remember to assign yourself (system administrator) to ‘Business Owner’.

1. Click Save. A welcome email is sent to the user you added. The invited user can access Cloud Manager by clicking the link in the welcome email and signing in using their Adobe ID.

Congratulations! Now, your newly formed Cloud Manager team including the yourself assigned to the ‘Business Owner’ role has been setup. Members will receive a welcome email inviting them to login and access Cloud Manager. In the role of Business Owner, you are now just one step away from logging in to Cloud Manager and enabling the creation of your cloud resources.

## Assign Users to Deployment Manager Product Profile {#assign-users-deployment-manager}

1. Identify the user(s) who will manage Cloud Manager Programs and add them to the Business Owner product profile. The system administrator must be the first person to access and log in to Cloud Manager. You must add yourself (system administrator) to the Business Owner product profile first. 

1. In Admin Console Overview page, select Adobe Experience Manager as a Cloud Service product from products and services card as shown below:

1. Select the Users tab from the top navigation, then select Add User.

1. In the add user dialog box, type the email ID of the user you want to add. For the ID Type, select Adobe ID if the Federated ID for your team members has not yet been set up.

1. In the Product selection, select 'Adobe Experience Manager as a Cloud Service' and assign 'Deployment Manager' product profile to the user as shown below. Refer to Cloud Manager product profiles to ensure that the right users are assigned the right role(s) in Admin Console as seen below.

   >[!NOTE]
   >User can be added to the Deployment Manager product profile after Cloud Manager resources are created.

## Assign Users to Developer Product Profile {#assign-users-developer}

1. Identify the user(s) who will manage Cloud Manager Programs and add them to the Business Owner product profile. The system administrator must be the first person to access and log in to Cloud Manager. You must add yourself (system administrator) to the Business Owner product profile first. 

1. In Admin Console Overview page, select Adobe Experience Manager as a Cloud Service product from products and services card as shown below:

1. Select the Users tab from the top navigation, then select Add User.

1. In the add user dialog box, type the email ID of the user you want to add. For the ID Type, select Adobe ID if the Federated ID for your team members has not yet been set up.

1. In the Product selection, select 'Adobe Experience Manager as a Cloud Service' and assign 'Developer' product profile to the user as shown below. Refer to Cloud Manager product profiles to ensure that the right users are assigned the right role(s) in Admin Console as seen below.

   >[!NOTE]
   >User can be added to the Developer product profile after Cloud Manager resources are created.

## What’s Next {#whats-next}

As a System Administrator assigned to the *Business Owner* role, you must access and login to Cloud Manager.
>[!NOTE]
>Refer to Navigating to Cloud Manager to learn how to login and access Cloud Manager.

A Cloud Manager user in the Business Owner role can login and setup your cloud resources including your Programs and Environments. This will ensure that your team of experts can begin accessing AEM as a Cloud Service as soon as possible.
After your Business Owner has setup your cloud resources, Developers and Deployment Managers who have been successfully added to the Cloud Manager product profiles can access Cloud Manager and familiarize themselves on how they can continue on their learning path.

## Additional Resources {#additional-resources}

Follow the additional resources to learn about:

* Cloud Manager
* Cloud Manager Product Profiles
* Admin Console Identity Overview 
