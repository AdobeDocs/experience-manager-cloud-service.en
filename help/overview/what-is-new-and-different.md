---
title: What is Different and What is New - Adobe Experience Manager as a Cloud Service
description: What is Different and What is New - Adobe Experience Manager (AEM) as a Cloud Service. 
---

# What is New and What is Different {#what-is-new-and-what-is-different}

For many years AEM has been available both:

* On-Premise

* as a Managed Service

There are intrinsic differences between these previous approaches and AEM as a Cloud Service:

* [Architecture](#architecture)
* [Upgrades](#upgrades)
* [Cloud Manager](#cloud-manager)
* [Onboarding](#onboarding)
* [Developing](#developing)
* [Operations and Performance](#operations-and-performance)
* [Identity Management](#identity-management)
* [Authoring User Interface](#authoring-user-interface)
* [AEM Sites](#aem-sites)
* [AEM Assets](#aem-assets)

>[!NOTE]
>
>These overviews are not exhaustive, but are intended to provide an introduction.

>[!NOTE]
>
>For further details on the On-Premise and Managed Service versions, see the documentation set for [AEM 6.5](https://helpx.adobe.com/support/experience-manager/6-5.html).

## Architecture {#architecture}

>[!NOTE]
>
>For further details see [Architecture](/help/core-concepts/architecture.md).

AEM as a Cloud Service now has:

* A dynamic architecture with a variable number of AEM images.

![Dynamic architecture](assets/introduction-03.png "Dynamic architecture")

This architecture:

* Is scaled based on the *actual* traffic and *actual* activity.

* Has individual instances that only run when needed.

* Uses modular applications.

* Has an author cluster as default; this avoids downtime for maintenance tasks.

This enables autoscaling for varying usage patterns:

![Autoscaling for varying usage patterns](assets/introduction-04.png "Autoscaling for varying usage patterns")


## AEM Updates {#aem-updates}

>[!NOTE]
>For further details see the [AEM Version Updates](/help/implementing/deploying/aem-version-updates.md).

AEM as a Cloud Service now uses Continuous Integration and Continuous Delivery (CI/CD) to ensure that your projects are on the most current AEM version. This means that Production and Stage instances are updated to the latest AEM version without any interruption of service for users.

>[!NOTE]
> If the update to production environment fails, Cloud Manager will automatically rollback the stage environment. This is done automatically to make sure that after an update completes, both stage and production environments are at on same AEM version.

AEM version updates are of two types:

* **AEM Push updates**

   * Can be released on a daily basis.
   * Mostly maintenance, including the latest bug-fixes and security updates.

     As changes are applied regularly the impact is incremental, reducing the impact on your service.

* **New Feature updates**

   * Released via a predictable monthly schedule.

## Cloud Manager {#cloud-manager}

Adobe Cloud Manager is integral to the continuous upgrade approach of AEM as a Cloud Service, as it controls all updates to your instances - this is mandatory. 

Updates can be triggered by Adobe when a new version of the cloud service is available. Alternatively you can trigger your application updates using the pipelines provided by Cloud Manager.

Cloud Manager is:

* used to manage AEM programs and environments,

* an essential component of AEM as a Cloud Service; each new tenant is first provisioned for Cloud Manager access,

* the single entry point for your operations and development staff. 

Specifically, the number of and the type of AEM programs that can be created from the Cloud Manager is derived either:

* from the customer licensing agreement,

* from internal-driven actors when AEM as a Cloud Service is used for enablement, or training,

* from external-driven processes such as trials started from Adobe.com.  
  
Cloud Manager has evolved as a self-service portal where the main components of AEM as a Cloud Service can be created and configured:

* Creating and managing new programs. Refer to [Understanding Programs and Program Types](/help/onboarding/getting-access-to-aem-in-cloud/understand-program-types.md) for more details.

* Creating and managing the AEM environments within these programs. Refer to [Managing Environments](/help/implementing/cloud-manager/manage-environments.md) for more details.

* Creating and managing the pipelines for deploying the customer code and the related configuration to a specific environment. Refer to [Configuring your CI-CD Pipeline](/help/implementing/cloud-manager/configure-pipeline.md) for more details.

* Being notified of important lifecycle events for these components (for example, product updates).

Cloud Manager creates environments in datacenters across many geographic regions, providing for global coverage. CDN Points of Presence (PoPs) ensure low-latency content delivery for customers located all over the world.

>[!NOTE]
>Refer to [Accessing Experience Manager as a Cloud Service](/help/onboarding/getting-access-to-aem-in-cloud/navigation.md) to get started with Cloud Manager in AEM as a Cloud Service.

## Onboarding {#onboarding}

>[!NOTE]
>
>For further details see [Onboarding](/help/onboarding/home.md).

Starting and managing an AEM project is straightforward when using AEM as a Cloud service as Adobe is responsible for many aspects:

* Baseline AEM images are optimized for specific use-cases.

* Many of the manual configuration tasks have been made redundant.

It is also significantly different as there is now:

* An assessment phase to ensure that all pre-requisites have been met; including, for example:

  * Legal requirements
  
  * Contractual agreements

  * Technical requirements for any existing content and/or code customized by the customer

* Deployment requirements:

  * Code updates; any customer applications developed for a previous version of AEM will need to be reviewed and possibly updated.

  * Content migration

## Developing {#developing}

>[!NOTE]
>
>For further details you can start with [Development Guidelines](/help/implementing/developing/introduction/development-guidelines.md) and [Developing - The WKND Tutorial](/help/implementing/developing/introduction/develop-wknd-tutorial.md).

The new architecture supporting AEM as a Cloud Service involves some key changes to the overall developer experience. One of the major goals for AEM as a Cloud Service is to allow experienced customers (having used AEM either on-premise or in the context of the Adobe Managed Services) to migrate to AEM as a Cloud Service as quickly as possible, without having to rewrite the bulk of their customized code. However, some adjustments might still be needed. 

### Cloud Development {#aem-as-a-cloud-service-developing-cloud-development}

For existing AEM applications to run on AEM as a Cloud Service, the following steps are expected:

* The application code and configuration must be stored in the Git code repository of the associated Cloud Manager program.
* The application code and configuration must be compatible with the latest version of the baseline AEM image (which might be changing daily). 
  * The customer application must be built and deployed using the Cloud Manager pipeline associated to the Cloud Manager environment.
* The customer application must pass all the code quality, security and performance gates enforced in the pipeline.
* The images built for the customer application must be deployed by the Cloud Manager pipeline.

This process is commonly referred to as Cloud-first development. Since the end-to-end duration is expected to take minutes (from 20 to 50 depending on the complexity of the application), it is necessary to embrace rapid development methodologies before the pending code and configuration changes are attempted in the cloud.

The Web Console, where OSGI bundles and their associated configuration are managed, and previously part of the AEM QuickStart, is no longer directly accessible to users of a AEM as a Cloud Service environment. This interface can still be accessed in read-only mode by using a new developer console. With this console, developers can select and login directly to any particular node of an author or publish service, then access the areas blocked by default.

>[!NOTE]
>
>See also [OSGi Configuration](/help/implementing/deploying/overview.md#osgi-configuration)

Another common requirement for developers is quick access to the log files of the various environments. With AEM as a Cloud Service, the log files of the different nodes in the author and publish nodes are made available via the Cloud Manager, either in the form of files that can be downloaded, or via APIs.

Due to the clear separation of code and content, developers can use a particular process for updating content as part of a deployment. The typical use cases for mutable content are:

* Standard *default* content that is part of the customer project (for example, folders, templates, workflows, etc)

* Search index definitions

* ACLs and permissions

* Service users and user groups

### Local Development {#aem-as-a-cloud-service-developing-local-development}

In order to support rapid iterations and development, it is also possible to develop AEM applications outside the AEM as a Cloud Service context. For this purpose, the following artifacts are made available to the developers:

* The AEM as a Cloud Service QuickStart: a `.jar` based, standalone installer of the latest AEM code base, with the same functional and API surface.

* The AEM as a Cloud Service Dispatcher SDK: an image-based process for testing and validating Dispatcher configurations locally

>[!NOTE]
>
>It should be noted that the Cloud QuickStart does not allow for all AEM Sites and AEM Assets functionalities. It consists of a simple author environment where the majority of the extensions can be developed and tested.

## Operations and Performance {#operations-and-performance}

>[!NOTE]
>
>For further details start with [Backup](/help/operations/backup.md), [Indexing](/help/operations/indexing.md), and [other Maintenance Tasks](/help/operations/maintenance.md).

With AEM as a Cloud Service, such operations are automated so that any interruption of service is no longer necessary.

In these areas:

* Many tasks have been automated.

* Topologies are optimized for maximum resilience and efficiency; for example, binaryless replication is the default.

* Heavy-load tasks, such as queues, jobs and bulk-processing tasks have been moved out of the core AEM instance to be handled by shared and dedicated micro-services.

Operations for AEM as a Cloud Service are also supported by a new monitoring, reporting, and alerting infrastructure. This allows the Adobe SREs (Site Reliability Engineers) to proactively keep the service healthy. The various elements of the architecture are equipped with a variety of health checks. If, for some reason, a particular node of the architecture is deemed unhealthy, then it is removed from the service and silently replaced with a new, healthy one. 

## Identity Management {#identity-management}

>[!NOTE]
>
>For further details see [Security - IMS Support](/help/security/ims-support.md).

A major change to AEM as a Cloud Service is the fully integrated use of Adobe IDs for accessing the author tier. 

This requires use of the [Adobe Admin console](https://helpx.adobe.com/enterprise/using/admin-console.html) for managing users and user groups. The user accounts enable your users to access Adobe products and services, as user-profile information is centralized in the Adobe Identity Management System (IMS) to be shared across all cloud services. Once assigned access to AEM, the user accounts can be referenced in AEM as a Cloud Service (as before); for example, for defining roles and permissions from the AEM Security user interfaces. 

This combines the benefits of:

* Using the Adobe Identity Management System (IMS) to provide single-sign-on across all Adobe cloud applications. 

* User preferences remaining local to each particular instance of AEM as a Cloud Service.

## Authoring User Interface {#authoring-user-interface}

>[!NOTE]
>
>For further details, the [Basic Handling](/help/sites-cloud/authoring/getting-started/basic-handling.md) is a good starting point.

The basic principles of the authoring user interface (UI), for both Sites and Assets, will be very familiar to anyone who has used AEM in the past.

The main difference is that the UI is purely touch-enabled; the classic UI is no longer available. Otherwise the basics remain unchanged, with only small changes apparent. 

## AEM Sites {#aem-sites}

Adobe Experience Manager Sites as a Cloud Service enables you to provide your customers with personalized, content-led experiences, by combining the power of the AEM Content Management System with AEM Digital Asset Management.

For details see the overview of [Changes to Sites](/help/sites-cloud/sites-cloud-changes.md).

## AEM Assets {#aem-assets}

Adobe Experience Manager Assets as a Cloud Service offers a cloud-native, PaaS solution for businesses to not only perform their Digital Asset Management and Dynamic Media operations with speed and impact, but also use next-generation smart capabilities, such as AI/ML, from within a system that is always current, always available, and always learning.

Assets offering includes next-generation asset processing in the cloud and high performance asset ingestion and search.

For details, see [overview and introduction to Assets as a Cloud Service](/help/assets/overview.md).

## Getting to Know Adobe Experience Manager as a Cloud Service {#getting-to-know-aem-as-cloud-service}

For further information see:

* [An Introduction to Adobe Experience Manager as a Cloud Service](/help/overview/introduction.md)
* The [Architecture](/help/core-concepts/architecture.md) of Adobe Experience Manager as a Cloud Service
* [Notable changes to AEM as a Cloud Service (Release Notes)](/help/release-notes/aem-cloud-changes.md)
* [Notable changes to AEM Sites as a Cloud Service](/help/sites-cloud/sites-cloud-changes.md)
* [Notable changes to AEM Assets as a Cloud Service](/help/assets/assets-cloud-changes.md)
* [Introducing AEM Assets as a Cloud Service](/help/assets/overview.md)
* [Adobe Experience Manager as a Cloud Service Tutorials](https://docs.adobe.com/content/help/en/experience-manager-learn/cloud-service/overview.html)
