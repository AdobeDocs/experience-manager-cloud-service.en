---
title: Introduction to Cloud Manager
description: Learn about how Cloud Manager supports your AEM project through its programs, environments, and pipelines.
exl-id: b743f126-b34e-4f48-a3f0-5dbd4e1ac34e
---
# Introduction to Cloud Manager {#intro-cloud-manager}

Cloud Manager is an essential component of AEM as a Cloud Service and serves as the single entry point for your team. Its purpose-built CI/CD pipelines are equipped to ensure thorough testing and highest code quality to deliver exceptional experiences. To ensure customers can quickly start their projects, Cloud Manager provides everything required in a self-service manner including the ability to create your cloud resources and environments and access your git repositories. These features support enterprise development setups so teams can work towards committing changes frequently, rapidly delivering exceptional digital experiences, and accelerating time-to-value.

Your system administrator is responsible for setting up your Cloud Manager team which will include individuals that will create your cloud resources and developers. For more information about how to set up and scale your enterprise development team and see how AEM as a Cloud Service can support your development process, please refer to the document [Enterprise Team Development Setup for AEM as a Cloud Service.](/help/implementing/cloud-manager/managing-code/enterprise-team-dev-setup.md)

## Navigating to Cloud Manager's Overview Page {#navigate-cloud-manager}

Follow these steps to navigate to Cloud Manager.

1. Navigate to Cloud Manager's login page at [`https://my.cloudmanager.adobe.com`.](https://my.cloudmanager.adobe.com/). 

1. Select the program from Cloud Manager's **Programs and Products** page to launch the **Overview** page.

You can also navigate to Cloud Manager’s Programs and Products page from Adobe Experience Cloud home page by following these steps.

1. Navigate to Adobe Experience Cloud at [`https://experience.adobe.com`](https://experience.adobe.com) and login using your Adobe ID.

1. Ensure that you are in the correct organization by referring to the organization name displayed at the top-right of the toolbar.

1. Select **Experience Manager**.

1. On the **Cloud Manager** card, click on **Launch**

## Role Based Permissions in Cloud Manager {#role-based-permissions}

|Permission|Description|Business Owner|Deployment Manager|Program Manager|Developer|
|--- |--- |--- |--- |--- |--- |
|Add Program<br>Edit Program|Add a New Program<br>Add or remove solutions or add-ons|x||||
|Create Environment|Create production+staging and development environments|x|x|||
|Update Environment|Update production+staging and development environments|x|x|||
|Delete Dev Environment|Delete development environments|x|x|||
|Pipeline Setup|Setup and edit pipelines||x|||
|Pipeline Execution|Start pipelines|x|x|||
|Pipeline Execution|Reject/approve important 3-tier quality gate failures|x|x|x||
|Pipeline Execution|Provide go live approval|x|x|x||
|Pipeline Execution|Schedule production deployments|x|x|x||
|Pipeline Delete|Allow pipeline deletion||x|||
|Execution Cancel|Cancel current execution||x|||
|Generate Personal Access Token|Access git||x||x|

>[!NOTE]
>
>A user can be assigned to multiple roles. For example assigning both **Business Owner** and **Deployment Manager** roles to a user gives the user the sum of these permissions.

## Cloud Manager Programs {#cloud-manager-programs}

Cloud Manager programs represent sets of Cloud Manager environments supporting logical groupings of business initiatives. These groupings typically correspond to a purchased Service Level Agreement (SLA). For example, one program may represent the AEM resources to support an organization's public Web site, while another program represents an internal DAM. 


Watch this [video](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html) to learn more on using Cloud Manager programs.

A user can create a **Sandbox** or a **Production** program. 

* A **production program** is created to enable live traffic at the appropriate time in the future.
  * Please refer to the document [Introduction to Production Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-production-programs.md) for more details.

* A **sandbox program** is typically created to serve the purposes of training, running demos, enablement, creating POCs, or for documentation.
  * It is not meant to carry live traffic and will have restrictions that a production program will not. 
  * It includes Sites and Assets and is delivered auto-populated with a git branch that includes sample code, a development environment, and a non-production pipeline.
  * Please refer to the document [Introduction to Sandbox Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md) for more details.

## Cloud Manager Environments {#cloud-manager-environments}

Your cloud environments will be created, accessed and viewed via Cloud Manager. These environments can be production, staging, or development environments. Different environments serve different purposes and can be used with different CI/CD pipelines. Environments are composed of services such as:

* [AEM Authoring Services](#author-services)
* [AEM Publishing Services](#publish-services)
* [Dispatcher Services](#dispatcher-services)

>[!TIP]
>
> Refer to the video [Using Adobe Cloud Manager Environments](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html) an overview of the available environments.
>
>Refer to the document [Manage Environments](/help/implementing/cloud-manager/manage-environments.md) to learn more about types of environment a user can create and how the user can create an environment.

### AEM Authoring Service {#author-services}

An AEM authoring service is included in environments where site content and digital assets are created, managed, and updated. Typically only internal users have access to the authoring service and it is maintained behind a login screen. The authoring service acts as both an authoring and preview environment.

### AEM Publishing Service {#publish-services}

An AEM publishing service is included in environments that host the end-user experience, like a web site. This is the service that site visitors will view and interact with. Typically, the publishing service is publicly available.

### AEM Dispatcher Service {#dispatcher-services}

The dispatcher is an `Apache HTTP Web server` module that provides a security and performance layer that sits in front of the AEM publishing service.
