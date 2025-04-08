---
title: AEM as a Cloud Service Onboarding Journey Introduction
description: Start here for an overview of the guided journey through the onboarding process to AEM as a Cloud Service.
exl-id: 892577db-05dc-49ff-bb2c-203efdb89c8c
recommendations: noDisplay
feature: Onboarding
role: Admin, User, Developer
---

# Onboarding Journey {#onboarding-journey}

Congratulations on choosing AEM as a Cloud Service! This document is your starting point for a guided journey through the onboarding process. Whether you are deploying a new application or migrating an existing one, this onboarding journey sets up your teams. It ensures they have access to AEM as a Cloud Service.

## Introduction {#introduction}

Adobe Experience Manager is a powerful suite of composable content services that rapidly deliver highly impactful, personalized experiences across any channel, unlocking content from all for all. **Edge Delivery Services** is the latest innovation in Adobe Experience Manager that enables extreme content velocity and delivers exceptional experiences. Learn how to get started with Edge Delivery Services, by consulting [Edge Delivery Services Overview](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/overview). To understand how to use Edge Delivery Services, see the [Developer Tutorial](https://www.aem.live/developer/tutorial) page.

Onboarding is the process during which a designated system administrator sets up AEM as a Cloud Service for your organization. This process includes the initial provisioning of cloud resources and assigning users to roles based on their job responsibilities. As a result, each member is able to log on and access their resource on AEM as a Cloud Service.

![The onboarding journey](/help/journey-onboarding/assets/onboarding-journey.png).

This guide leads you through the most important onboarding topics so that on completion you have the following:

* Full understanding of the different terms, services, and users involved in the onboarding process.
* Enabled your team to get up and running and take the first steps towards learning how to author and develop content for your AEM as a Cloud Service application.

As a result:

* Your team is set up and has access to cloud resources.
* AEM authors have access to AEM as a Cloud Service and can begin creating content.
* AEM developers and deployment managers have access to AEM as a Cloud Service and can begin creating and deploying custom applications.

## Concepts and Goal {#concepts}

Although there may appear to be a lot to learn when getting started with AEM as a Cloud Service, conceptually there are only a few, logical pieces.

* **The Contract** - You must be familiar with your Adobe contract since it defines aspects of the onboarding process.
* **Admin Console** - Where users are managed and roles are assigned.
* **Cloud Manager** - The tool to set up resources such as programs and environments. It is also where you access Git and create pipelines to manage and deploy your custom code.

These concepts are laid out in detail in this onboarding journey. The goal is that at the end of the journey, you can do the following:

* Grant the necessary user's access to AEM as a Cloud Service.
* Set up the first cloud resources for your project.
* Know how to deploy your first code and author your first content.

Basically, you hit the ground running with your new AEM as a Cloud Service project!

## Audience {#audience}

The onboarding journey is written specifically for the **system administrator** of customers that are new to AEM as a Cloud Service and to AEM in general. The system administrator is the individual who Adobe contacts first after your AEM as a Cloud Service contract is signed. They are typically the first person to access and set up your resources on AEM as a Cloud Service. If you are reading this topic, it is likely that you are the system administrator.

The system administrator manages all aspects of their organization's AEMaaCS users, from access to permissions. However, the system administrator must interact with other personas along the way.

|Persona|Description|Role in Journey|
|---|---|---|
|System administrator|The target of this journey provides initial provisioning of cloud resources and assignment of users to appropriate roles based on their job responsibilities|Manages all aspects of users from access to permissions|
|Content author|Creates and reviews the content in AEM|Once granted permissions by the system administrator, authors can start their own journey in creating content|
|Developer|Develops AEM applications that consume content from different sources|Once granted permissions by the system administrator, developers can start their own journey in developing solutions|
|Deployment manager|Adds or updates an environment, runs pipelines, and deploys code to AEM environment or code-quality.|Once granted permissions by the system administrator, deployment managers can start their own journey managing deployments|

This onboarding guide illustrates the complete process of onboarding as a system administrator. The roles of AEM users, developers, and deployment managers are explored briefly as additional, optional parts of the journey.

>[!TIP]
>
>If you are new to AEM as a Cloud Service and familiar with AEM and are migrating from on-premise or Adobe Managed Services, check out the [AEM as a Cloud Service Migration Journey](/help/journey-migration/getting-started.md).

## Onboarding Journey Overview {#overview}

The following articles describe in details the core onboarding concepts and give you foundational knowledge of AEM as a Cloud Service. Although you can go directly to a particular part of the journey, many concepts build on ones in previous articles. Therefore, if you are new to onboarding, Adobe recommends that you start at the beginning and progress sequentially.

| |Article|Description|Audience|
|---|---|---|---|
|0|Onboarding Journey|This document|System Administrator|
|1|[Onboarding Preparation](preparation.md)|Before the onboarding process begins, there are a number or preparatory steps that the system administrator must understand before logging into the system.|System Administrator|
|2|[AEM as a Cloud Service Terminology](terminology.md)|Before you sign into AEMaaCS for the first time, it is helpful to understand some of the terminology of the system and its basic structure.|System Administrator|
|3|[The Admin Console](admin-console.md)|Learn what the Admin Console is, how to log in, and how to verify your profile as a system administrator.|System Administrator|
|4|[Assigning Cloud Manager Product Profiles](assign-profiles-cloud-manager.md)|Review Cloud Manager Product Profiles and learn how to assign team members to Cloud Manager Product profiles.|System Administrator|
|5|[Access Cloud Manager](cloud-manager.md)|Lean how to access Cloud Manager so that you can set up your project resources.|System Administrator|
|6|[Create a Program](create-program.md)|Learn how to create a program using Cloud Manager.|System Administrator|
|7|[Create Environments](create-environments.md)|Learn how to create an environment using Cloud Manager.|System Administrator|
|8|[Assigning AEM Product Profiles](assign-profiles-aem.md)|Learn how System Administrator assigns your team members to product profiles in AEM as a Cloud Service.|System Administrator|
|9|[Developer and Deployment Manager Tasks](developers.md)|Optional - As a Developer, learn how you can access and manage Cloud Manager Git and how as a Deployment Manager you can set up pipelines and deploy code in Cloud Manager.|Developers and Deployment Managers|
|10|[AEM User Tasks](aem-users.md)|Optional - As an AEM author, learn how you can access AEM as a Cloud Service instance and get familiar with authoring content for AEM as a Cloud Service.|AEM Users|

## What's next {#what-is-next}

You are now ready to start your AEM as a Cloud Service onboarding journey. You are encouraged to continue to the next part of the journey and read the article [Onboarding Preparation](preparation.md)

## AEM documentation journeys {#documentation-journeys}

[A documentation journey](/help/journey-documentation/documentation-journeys.md) ties together many different, complicated topics and features. It provides a narrative that helps a reader new to AEM understand and solve a business problem from beginning to end, while assuming minimal prior topic or AEM knowledge.

Documentation Journeys are designed around best practices principles. They are informed using Adobe's latest research, proven implementation experience from Adobe consultants, and feedback from customer projects.

If you want to know what Adobe recommends on how to get your team onboarded onto your new AEM as a Cloud Service application, start here.

## Additional resources {#additional-resources}

The following are additional, optional resources if you would like to go beyond the content of the onboarding journey.

* [Onboarding to AEM as a Cloud Service](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/migration/moving-to-aem-as-a-cloud-service/onboarding) - This brief video gives an overview of the Cloud Service onboarding process for AEM.
