---
title: Introduction to Cloud Manager
description: Learn about Cloud Manager, Cloud Manager programs, and environments.
exl-id: b743f126-b34e-4f48-a3f0-5dbd4e1ac34e
---
# Introduction to Cloud Manager {#intro-cloud-manager}

Cloud Manager is an essential component of AEM as a Cloud Service and serves as the single entry point for your team.

To support customers with enterprise development setups, AEM as a Cloud Service fully integrates with Cloud Manager and its purpose-built CI/CD pipelines, which are equipped to ensure thorough testing and highest code quality to deliver exceptional experiences.

To ensure customers can start quickly with AEM as a Cloud Service, Cloud Manager provides everything required to get started in a self-service manner including the ability to create your cloud resources and environments. In this manner, your AEM developers can access the Git repository via Cloud Manager. Using Cloud Manager, development teams can work towards committing changes frequently in a self-service manner.

Your System Administrator will be responsible to setting up your Cloud Manager team which will include individuals that will create your cloud resources and developers. Refer to [Enterprise Team Development Setup for AEM as a Cloud Service](/help/implementing/cloud-manager/managing-code/enterprise-team-dev-setup.md) to learn how Cloud Manager supports in Enterprise Team Development Setup.

## Navigating to Cloud Manager's Overview Page {#navigate-cloud-manager}

Follow the steps below to navigate to Cloud Manager:

1. Navigate directly to Cloud Manager's login page from [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/). 

   >[!NOTE]
   >Please bookmark this page for future reference and to help you navigate directly to Cloud Manager's landing page.

1. Select the program from Cloud Manager’s **Programs and Products** page to launch the **Overview** page.

Additionally, you can also navigate to Cloud Manager’s Programs and Products page from Adobe Experience Cloud home page. Follow the steps below:

1. Navigate directly to [Adobe Experience Cloud](https://experience.adobe.com/#/@foundationinternal/home) and login using your Adobe ID.

1. Select **Experience Manager**.

1. Click on **Launch** from the Cloud Manager card. Once you have successfully logged in to Cloud Manager, you are ready to use the User Interface (UI).

   Upon successful login, you will be directed to the landing page of Cloud Manager.

## Role Based Permissions in Cloud Manager {#role-based-permissions}

|Permission|Description|Business Owner|Deployment Manager|Program Manager|Developer|
|--- |--- |--- |--- |--- |--- |
|Add Program<br>Edit Program|Add a New Program.<br>Edit a program - Add or remove solutions or add-on's|x||||
|Create Environment|Create Prod+Stage, Dev, Environments.|x|x|||
|Update Environment|Update Prod+Stage, Dev, Environments.|x|x|||
|Delete Dev Environment|Delete Dev Environments.|x|x|||
|Pipeline Setup|Setup or Edit Pipeline.||x|||
|Pipeline Execution|Start the Pipeline.|x|x|||
|Pipeline Execution|Reject/Approve Important 3-Tier Failures.|x|x|x||
|Pipeline Execution|Provide GoLive Approval.|x|x|x||
|Pipeline Execution|Schedule Production Deployment.|x|x|x||
|Pipeline Delete|Allows Deleting of a Pipeline.||x|||
|Execution Cancel|Cancel Current Execution.||x|||
|Generate Personal Access Token|Access Git.||x||x|

>[!NOTE]
>A user can be assigned to multiple roles. For example assigning both Business Owner and Deployment Manager roles to a user gives them the combination or sum of these permissions.

## Cloud Manager Programs {#cloud-manager-programs}

Cloud Manager Programs represent sets of Cloud Manager environments supporting logical sets of business initiatives, typically corresponding to a purchased Service Level Agreement (SLA). For example, one Program may represent the AEM resources to support the global public Web sites, while another Program represents an internal Central DAM. Watch this [video](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html?lang=en) to learn more on using Cloud Manager programs.

A user can create a **Sandbox** or a **Production** program. 

* A *Production Program* is created to enable live traffic at the appropriate time in the future.
   Refer to [Introduction to Production Programs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/production-programs/introduction-production-programs.html?lang=en) for more details.

* A *Sandbox Program* is typically created to serve the purposes of training, running demo’s, enablement, POC’s, or documentation. It is not meant to carry live traffic and will have restrictions that a Production program will not. It will include Sites and Assets and will be delivered auto-populated with a Git branch that includes sample code, a Dev environment, and a non-production pipeline.
   Refer to [Introduction to Sandbox Programs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/sandbox-programs/introduction-sandbox-programs.html?lang=en) for more details.

## Cloud Manager Environments {#cloud-manager-environments}

Your cloud environments will be created, accessed and viewed via Cloud Manager. These can be a Production environment, Stage environment, or Development environment. Different environments support different purposes and can be engaged using different CI/CD Pipelines. Environments are composed of services such as:

* [AEM Author Services](#author-services)
* [AEM Publish Services](#publish-services)
* [Dispatcher Services](#dispatcher-services)

   >[!NOTE]
   > Refer to the video [Using Adobe Cloud Manager Environments](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html?lang=en#cloud-manager) to learn more about the available environments. Additionally, see [Manage Environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html?lang=en) to learn more about types of environment a user can create and how the user can create an environment.

### AEM Author Service {#author-services}

AEM Author Service is included in an environment where site content and digital assets are created, managed and updated. Typically, only internal users have access to the Author Service and is behind a login screen. The Authoring Service is designed both as an authoring and preview environment.

### AEM Publish Service {#publish-services}

AEM Publish Service is included in an environment that hosts the end-user experience, like a web site. This is the service that site visitors will view and interact with. Typically, the Publish Service is publicly available.

### AEM Dispatcher Service {#dispatcher-services}

The Dispatcher is an `Apache HTTP Web server` module that provides a security and performance layer that sits in front of the AEM Publish Service.
