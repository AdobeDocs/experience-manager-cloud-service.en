---
title: AEM as a Cloud Service Onboarding Journey Introduction
description: Start here for an overview of the guided journey through the onboarding process to AEM as a Cloud Service.
exl-id: 892577db-05dc-49ff-bb2c-203efdb89c8c
---

# Onboarding Journey {#onboarding-journey}

Congratulations on choosing AEM as a Cloud Service! This document is your starting point for a guided journey through the onboarding process. Whether you are deploying a new application or migrating an existing one, this onboarding journey ensures your teams are set up and have access to AEM as a Cloud Service.

## Introduction {#introduction}

Onboarding is the process during which a designated system administrator sets up AEM as a Cloud Service for your organization. This includes the initial provisioning of cloud resources and assigning users to roles based on their job responsibilities. As a result, each member is able to login and access their AEM as a Cloud Service resources.

![The onboarding journey](/help/journey-onboarding/assets/onboarding-journey.png)

This guide leads you through the most important onboarding topics so that on completion you will have:

* Full understanding of the different terms, services, and users involved in the onboarding process.
* Enabled your team to get up and running and take the first steps towards learning how to author and develop content for your AEM as a Cloud Service application.

As a result:

* Your team will be set up and has access to cloud resources.
* AEM authors will have access to AEM as a Cloud Service and can begin creating content.
* AEM developers and deployment managers will have access to AEM as a Cloud Service and can begin creating and deploying custom applications.

## Concepts and Goal {#concepts}

Although there may appear to be a lot to learn when getting started with AEM as a Cloud Service, conceptually there are only a few, logical pieces.

* **The Contract** - You need to be familiar with your Adobe contract since it defines aspects of the onboarding process.
* **Admin Console** - This is where users are managed and roles are assigned.
* **Cloud Manager** - This is the tool to set up resources such as programs and environments. It is also where you access git and create pipelines to manage and deploy your custom code.

These concepts will be laid out in detail in this onboarding journey. The goal is that at the end of the journey, you:

* Have granted the necessary users access to AEMaaCS
* Have set up the first cloud resources for your project
* Know how to deploy your first code and author your first content.

Basically you will hit the ground running with your new AEM as a Cloud Service project!

## Audience {#audience}

The onboarding journey is written specifically for the **system administrator** of customer's new to AEM as a Cloud Service and to AEM in general. The system administrator is the individual who is first contacted by Adobe after your AEM as a Cloud Service contract is signed, and is typically the first person to access and set up your AEM as a Cloud Service resources. If you are reading this, you are likely the system administrator.

The system administrator manages all aspects of their organization's AEMaaCS users, from access to permissions. However the system administrator must interact with other personas along the way.

|Persona|Description|Role in Journey|
|---|---|---|
|System administrator|Target of this journey, provides initial provisioning of cloud resources and assignment of users to appropriate roles based on their job responsibilities|Manages all aspects of users from access to permissions|
|Content author|Creates and reviews the content in AEM|Once granted permissions by the system administrator, authors can start their own journey creating content|
|Developer|Develops AEM applications which consume content from different sources|Once granted permissions by the system administrator, developers can start their own journey developing solutions|
|Deployment manager|Adds or updates an environment, runs pipelines, and deploys code to AEM environment or code-quality.|Once granted permissions by the system administrator, deployment managers can start their own journey managing deployments|

This onboarding guide illustrates the complete process of onboarding as a system administrator. The roles of AEM users, developers, and deployment managers are explored briefly as additional, optional parts of the journey.

>[!TIP]
>
>If you are new to AEM as a Cloud Service, but are already familiar with AEM and are migrating from on-premise or Adobe Managed Services, be sure to check out the [AEM as a Cloud Service Migration Journey.](/help/journey-migration/getting-started.md)

## Onboarding Journey Overview {#overview}

The following articles describe in details the core onboarding concepts and give you foundational knowledge of AEM as a Cloud Service. Although you can go directly to a particular part of the journey, many concepts build on ones in previous articles. Therefore if you are new to onboarding, we recommend that you start at the beginning and progress sequentially.

|#|Article|Description|Audience|
|---|---|---|---|
|0|Onboarding Journey|This document|System Administrator|
|1|[Onboarding Preparation](preparation.md)|Before the onboarding process begins, there are a number or preparatory steps that the system administrator must understand before logging into the system.|System Administrator|
|2|[AEM as a Cloud Service Terminology](terminology.md)|Before you sign into AEMaaCS for the first time, it is helpful to understand some of the terminology of the system and its basic structure.|System Administrator|
|3|[The Admin Console](admin-console.md)|Learn what the Admin Console is, how to log in, and how to verify your profile as a system administrator.|System Administrator|
|4|[Assigning Cloud Manager Product Profiles](assign-profiles-cloud-manager.md)|Review Cloud Manager Product Profiles and learn how to assign team members to Cloud Manager Product profiles.|System Administrator|
|5|[Access Cloud Manager](cloud-manager.md)|Lean how to access Cloud Manager so that you can set up your project resources.|System Administrator|
|6|[Create a Program](create-program.md)|Learn how to create a program using Cloud Manager.|System Administrator|
|7|[Create Environments](create-environments.md)|Learn how to create an environment using Cloud Manager.|System Administrator|
|8|[Assigning AEM Product Profiles](assign-profiles-aem.md)|Learn how System Administrator assign your team members to AEM as a Cloud Service product profiles.|System Administrator|
|9|[Developer and Deployment Manager Tasks](developers.md)|Optional - Learn how as a Developer you can access and manage Cloud Manager Git and how as a Deployment Manager you can setup pipelines and deploy code in Cloud Manager.|Developers and Deployment Managers|
|10|[AEM User Tasks](aem-users.md)|Optional - Learn how as an AEM author you can access AEM as a Cloud Service instance and get familiar with authoring content for AEM as a Cloud Service.|AEM Users|

## What's Next {#what-is-next}

You are now ready to start your AEM as a Cloud Service onboarding journey. We encourage you to continue to the next part of the journey and read the article [Onboarding Preparation](preparation.md)

## AEM Documentation Journeys {#documentation-journeys}

[A Documentation Journey](/help/journey-documentation/documentation-journeys.md) ties together many different and perhaps complicated topics and features by providing a narrative that helps the reader, who can be new to AEM, understand and solve a business problem from beginning to end, while assuming minimal prior topic or AEM knowledge.

Documentation Journeys are designed around best practices principles, informed by Adobe's latest research, proven implementation experience from Adobe consultants, and feedback from customer projects.

If you want to know how Adobe recommends how to get your team onboarded onto your new AEM as a Cloud Service application, this is where to start!
