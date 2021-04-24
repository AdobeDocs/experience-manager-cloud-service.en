---
title: Learn what is Cloud Manager
description: Follow this page to learn about Cloud Manager, Cloud Manager Programs, and Environments.
---

# Introduction to Cloud Manager {#intro-cloud-manager}

Cloud Manager is an essential component of AEM as a Cloud Service and serves as the single entry point for your team.

To support customers with enterprise development setups, AEM as a Cloud Service fully integrates with Cloud Manager and its purpose-built CI/CD pipelines, which are equipped to ensure thorough testing and highest code quality to deliver exceptional experiences.

To ensure customers can start quickly with AEM as a Cloud Service, Cloud Manager provides everything required to get started in a self-service manner including the ability to create your cloud resources and environments. In this manner, your AEM developers can access the Git repository via Cloud Manager. Using Cloud Manager, development teams can work towards committing changes frequently in a self-service manner.

Your System Administrator will be responsible to setting up your Cloud Manager team which will include individuals that will create your cloud resources and developers. Refer to [Enterprise Team Development Setup for AEM as a Cloud Service](/help/implementing/cloud-manager/enterprise-team-dev-setup.md) to learn how Cloud Manager supports in Enterprise Team Development Setup.

## Cloud Manager Programs {#cloud-manager-programs}

Cloud Manager Programs represent sets of Cloud Manager environments supporting logical sets of business initiatives, typically corresponding to a purchased Service Level Agreement (SLA). For example, one Program may represent the AEM resources to support the global public Web sites, while another Program represents an internal Central DAM. Watch this video to learn more.

A user can create a **Sandbox** or a **Production** program. 

* A *Production Program* is created to enable live traffic at the appropriate time in the future.
   Refer to [Introduction to Production Programs](/help/onboarding/getting-access-to-aem-in-cloud/introduction-production-programs.md) for more details.


* A *Sandbox Program* is typically created to serve the purposes of training, running demo’s, enablement, POC’s, or documentation. It is not meant to carry live traffic and will have restrictions that a Production program will not. It will include Sites and Assets and will be delivered auto-populated with a Git branch that includes sample code, a Dev environment, and a non-production pipeline.
   Refer to [Introduction to Sandbox Programs](/help/onboarding/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md) for more details.


## Cloud Manager Environments {#cloud-manager-environments}

Cloud Manager Environments typically have one Production environment, one Stage environment, and one Development environment. Different environments support roles and can be engaged using different CI/CD Pipelines. 

The CI/CD Pipelines in Cloud Manager are composed of services such as:

* [AEM Author](#aem-author-service)
* [AEM Publish](#aem-publish-service)
* [Dispatcher](#dispatcher-services)

   >[!NOTE]
   > Refer to the video [Using Adobe Cloud Manager Environments](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html?lang=en#cloud-manager) to learn more about the available environments.

### AEM Author Service {#aem-author-service}

Environment where site content and digital assets are created, managed and updated. Typically only internal users have access to the Author Service and is behind a login screen. The Authoring Service is designed both as an authoring and preview environment.

### AEM Publish Service {#aem-publish-service}

Environment that hosts the end-user experience, like a web site. This is the service that site visitors will view and interact with. Typically, the Publish Service is publicly available.

### AEM Dispatcher Service {#aem-publish-service}

The Dispatcher is an Apache HTTP Web server module that provides a security and performance layer that sits in front of the AEM Publish Service.