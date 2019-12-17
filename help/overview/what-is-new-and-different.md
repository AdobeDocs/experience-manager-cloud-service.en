---
title: What is Different and What is New - Adobe Experience Manager as a Cloud Service
seo-title: What is Different and What is New - Adobe Experience Manager (AEM) as a Cloud Service
description: What is Different and What is New - Adobe Experience Manager (AEM) as a Cloud Service. 
seo-description: What is Different and What is New - Adobe Experience Manager (AEM) as a Cloud Service. 
---

# What is Different and What is New {#what-is-different-and-what-is-new}

For many years AEM has been available both:

* On-Premise

* as a Managed Service

<!-- change link when 6.5 migrated -->

>[!NOTE]
>
>For further details on these versions see the documentation set for [AEM 6.5](https://helpx.adobe.com/support/experience-manager/6-5.html).

There are intrinsic differences between these previous approaches and AEM as a Cloud Service:

>[!NOTE]
>
>These overviews are not exhaustive, but are intended to provide an introduction.

* [Architecture](#architecture)
* [Upgrades](#upgrades)
* [Cloud Manager](#cloud-manager)
* [Onboarding](#onboarding)
* [Developing](#developing)
* [Operations and Performance](#operations-and-performance)
* [Identity Management](#identity-management)
* [Authoring](#authoring)
<!-- * [Miscellaneous](#miscellaneous) -->

* [AEM Sites](#aem-sites)

## Architecture {#architecture}

>[!NOTE]
>
>For further details see [Architecture](/help/core-concepts/architecture.md).

### Previous Versions {#previous-versions-architecture}

Both AEM on-premise, and AEM under Managed Services used a static architecture comprised of a fixed number of machines and instances. 

![Static architecture](assets/introduction-01.png "Static architecture")

These:

* Were sized for *peak* traffic (internet) and *peak* activity (marketing), which resulted in them being idle for significant periods of time:
![Static structure must cater for varying usage patterns](assets/introduction-02.png "Static structure must cater for varying usage patterns")

* Were monolithic applications (the quickstart).

* Had a single author instance; which was subject to downtime during maintenance windows.

### AEM as a Cloud Service {#aem-as-a-cloud-service-architecture}

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


## Upgrades {#upgrades}

<!--
>[!NOTE]
>
>For further details see the [Deploying Introduction](/help/sites/deploying/introduction.md).
-->

### Previous Versions {#previous-versions-upgrades}

Both AEM on-premise, and AEM under Managed Services were subject to a fixed pattern of a yearly major release augmented by service packs, feature packs and hot-fixes. Often instances would run a major version for two or more years. 

Depending on the upgrade type, the process could require significant preparation consisting of analysis, development and testing, followed with a window of downtime for the actual upgrade.

### AEM as a Cloud Service {#aem-as-a-cloud-service-upgrades}

AEM as a Cloud Service now uses Continuous Integration and Continuous Delivery (CI/CD) to ensure that your projects are fully up-to-date. These mean that all upgrade operations are fully automated, so do not require any interruption of service for users.

Adobe proactively takes care of updating all operational instances of the service to the latest version of the AEM code base:

* Bug-fixes:
 
  * Can be released on a daily basis.

  * Instances are frequently updated with the latest bug-fixes. As changes are applied regularly the impact is incremental, reducing the impact on your service.

  * Most updates are for maintenance and security reasons. 

* New Features:

  * Will be released via a predictable monthly schedule.

>[!NOTE]
>
>This is achieved using the [Cloud Manager](#cloud-manager).

## Cloud Manager {#cloud-manager}

>[!NOTE]
>
>For further details see [Deployment Architecture](/help/core-concepts/architecture.md#deployment-architecture).

### Previous Versions {#previous-versions-cloud-manager}

The Cloud Manager was used as a deployment tool for Managed Services instances of AEM.

The key differences between Cloud Manager for AMS and for Cloud Services, is when a tenant is created, it will be populated with credits based on the SKUs which have been purchased by the customer.

Creating a normal program does not consume any credits, but a core credit must exist in order to create one.
To learn in detail about creadits and how these are consumed, refer to [Create a Program](/help/onboarding/getting-access-to-aem-in-cloud/creating-a-program.md#program-types).

### AEM as a Cloud Service {#aem-as-a-cloud-service-cloud-manager}

Adobe Cloud Manager is integral to the continuous upgrade approach of AEM as a Cloud Service, as it controls all updates to your instances - this is mandatory. 

Updates can be triggered by Adobe when a new version of the cloud service is available. Alternatively you can trigger your application updates using the pipelines provided by Cloud Manager.

Cloud Manager is:

* used to manage AEM programs and environments,

* an essential component of AEM as a Cloud Service; each new tenant is first provisioned for Cloud Manager access,

* the single entry point for your operations and development staff. 

Specifically, the number of and the type of AEM programs that can be created from the Cloud Manager is derived either:

* from the customer licensing agreement, in the form of a pool of credits,

* from internal-driven actors when AEM as a Cloud Service is used for enablement, or training,

* from external-driven processes such as trials started from Adobe.com.  
  
Cloud Manager has evolved as a self-service portal where the main components of AEM as a Cloud Service can be created and configured:

* Creating and managing new programs.

* Creating and managing the AEM environments within these programs.

* Creating and managing the pipelines for deploying the customer code and the related configuration to a specific environment.

* Being notified of important lifecycle events for these components (for example, product updates).

Currently Cloud Manager is able to create environments in 3 geographical regions (with more regions following):

* US (East)

* EMEA (Netherlands)

* APAC (Australia)

## Onboarding {#onboarding}

<!--
>[!NOTE]
>
>For further details see [Onboarding - An Overview](/help/onboarding/overview.md).
-->

### Previous Versions {#previous-versions-onboarding}

Implementing an AEM project basically followed traditional project management methods.  

### AEM as a Cloud Service {#aem-as-a-cloud-service-onboarding}

Starting and managing an AEM project is significantly easier when using AEM as a Cloud service as Adobe is responsible for many aspects:

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
>For further details start with the [Development Guidelines](/help/implementing/developing/introduction/development-guidelines.md) documentation.

<!--
>[!NOTE]
>
>For further details start with [The Developing Experience](/help/sites/developing/introduction/developer-experience.md, [Developing - The Basics](/help/sites/developing/introduction/the-basics.md) and [Developing Best Practices](/help/sites/best-practices/developing.md).
--> 

### Previous Versions {#previous-versions-developing}

<!-- needs more detail -->
Development was an intensive task performed locally, followed by deployment to the production instance. 

### AEM as a Cloud Service {#aem-as-a-cloud-service-developing}

<!-- Will need information for new customers -->
The new architecture supporting AEM as a Cloud Service involves some key changes to the overall developer experience. One of the major goals for AEM as a Cloud Service is to allow experienced customers (having used AEM either on-premise or in the context of the Adobe Managed Services) to migrate to AEM as a Cloud Service as quickly as possible, without having to rewrite the bulk of their customized code. However, some adjustments might still be needed. 

#### Cloud Development {#aem-as-a-cloud-service-developing-cloud-development}

For existing AEM applications to run on AEM as a Cloud Service, the following steps are expected:

* The application code and configuration must be stored in the Git code repository of the associated Cloud Manager program.
* The application code and configuration must be compatible with the latest version of the baseline AEM image (which might be changing daily). 
  * The customer application must be built and deployed using the Cloud Manager pipeline associated to the Cloud Manager environment.
* The customer application must pass all the code quality, security and performance gates enforced in the pipeline.
* The images built for the customer application must be deployed by the Cloud Manager pipeline.

<!-- duration of what? -->
This process is commonly referred to as Cloud-first development. Since the end-to-end duration is expected to take minutes (from 20 to 50 depending on the complexity of the application), it is necessary to embrace rapid development methodologies before the pending code and configuration changes are attempted in the cloud.

<!-- is this really relevant at this point? -->
The Web Console, where OSGI bundles and their associated configuration are managed, and previously part of the AEM QuickStart, is no longer directly accessible to users of a AEM as a Cloud Service environment. This interface can still be accessed in read-only mode by using a new developer console. With this console, developers can select and login directly to any particular node of an author or publish service, then access the areas blocked by default.

Another common requirement for developers is quick access to the log files of the various environments. With AEM as a Cloud Service, the log files of the different nodes in the author and publish nodes are made available via the Cloud Manager, either in the form of files that can be downloaded, or via APIs.

Due to the clear separation of code and content, developers can use a particular process for updating content as part of a deployment. The typical use cases for mutable content are:

* Standard *default* content that is part of the customer project (for example, folders, templates, workflows, etc)

* Search index definitions

* ACLs and permissions

* Service users and user groups

#### Local Development {#aem-as-a-cloud-service-developing-local-development}

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

### Previous Versions {#previous-versions-operations-and-performance}

In the past, especially on the author side, there was a need to periodically stop an instance; for routine maintenance operations, as well as upgrades and updates. For some customers, this resulted in hours of scheduled downtime on a weekly basis. 

### AEM as a Cloud Service {#aem-as-a-cloud-service-operatioms-and-performance}

With AEM as a Cloud Service, such operations are automated so that any interruption of service is no longer necessary.

In these areas:

* Many tasks have been automated.

* Topologies are optimized for maximum resilience and efficiency; for example, binaryless replication is the default.

* Heavy-load tasks, such as queues, jobs and bulk-processing tasks have been moved out of the core AEM instance to be handled by shared and dedicated micro-services.

Operations for AEM as a Cloud Service are also supported by a new monitoring, reporting, and alerting infrastructure. This allows the Adobe SREs (Site Reliability Engineers) to proactively keep the service healthy. The various elements of the architecture are equipped with a variety of health checks. If, for some reason, a particular node of the architecture is deemed unhealthy, then it is removed from the service and silently replaced with a new, healthy one. 

## Identity Management {#identity-management}

<!--
>[!NOTE]
>
>For further details see [Security - Single Sign-On](/help/sites/security/single-sign-on.md).
-->

### Previous Versions {#previous-versions-identity-management}

By default, identity management was internal to AEM.

>[!NOTE]
>
>AEM 6.4.3.0 introduced:
>
>* Admin Console support for AEM instances. 
>* Adobe IMS (Identity Management System) based authentication for AEM Managed Services customers.

### AEM as a Cloud Service {#aem-as-a-cloud-service-identity-management}

A major change to AEM as a Cloud Service is the fully integrated use of Adobe IDs for accessing the author tier. 

This requires use of the [Adobe Admin console](https://helpx.adobe.com/enterprise/using/admin-console.html) for managing users and user groups. The user accounts enable your users to access Adobe products and services, as user-profile information is centralized in the Adobe Identity Management System (IMS) to be shared across all cloud services. Once assigned access to AEM, the user accounts can be referenced in AEM as a Cloud Service (as before); for example, for defining roles and permissions from the AEM Security user interfaces. 

This combines the benefits of:

* Using the Adobe Identity Management System (IMS) to provide single-sign-on across all Adobe cloud applications. 

* User preferences remaining local to each particular instance of AEM as a Cloud Service.

## Authoring {#authoring}

<!--
>[!NOTE]
>
>For further details, the [Basic Handling](/help/sites/authoring/getting-started/basic-handling.md) and [Best Practices](/help/sites/best-practices/authoring.md) are good starting points.
-->

### Previous Versions {#previous-versions-authoring}

Authoring was progressively developed and optimized to cater for all use-cases, using both the touch-enabled and classic UIs.

### AEM as a Cloud Service {#aem-as-a-cloud-service-authoring}

The basic principles of authoring (both Sites and Assets) will be very familiar to anyone who has used AEM in the past.

The main difference is that the UI is purely touch-enabled; the classic UI is no longer available. Otherwise the basics remain unchanged, with only small changes apparent. 

## AEM Sites {#aem-sites}

>[!NOTE]
>
>For further details see the Overview of [Changes to Sites](/help/sites-cloud/sites-cloud-changes.md).

## AEM Assets {#aem-assets}

Adobe Experience Manager Assets as a Cloud Service offers a cloud-native, SaaS solution for businesses to not only perform their Digital Asset Management and Dynamic Media operations with speed and impact, but also use next-generation smart capabilities, such as AI/ML, from within a system that is always current, always available, and always learning.

Assets offering includes next-generation asset processing in the cloud and high performance asset ingestion and search.

For details, see [overview and introduction to Assets as a Cloud Service](/help/assets/whats-new-assets.md).

<!--

#### Previous Versions {#previous-versions-aem-sites}

tbc

#### AEM as a Cloud Service {#aem-as-a-cloud-service-aem-sites}

tbc

-->

<!--

### AEM Assets {#aem-assets}

>[!NOTE]
>
>For further details see the [Introduction to AEM Assets as a Cloud Service](/help/assets/cloud/introduction-assets-cloud.md).

-->

<!--

#### Previous Versions* {#previous-versions-aem-assets}

tbc

#### AEM as a Cloud Service {#aem-as-a-cloud-service-aem-assets}

tbc 

-->

<!--

### Miscellaneous {#miscellaneous}

#### AEM as a Cloud Service {#aem-as-a-cloud-service-miscellaneous}

Additionally???

-->