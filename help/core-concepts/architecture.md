---
title: Introduction to the Architecture of Adobe Experience Manager as a Cloud Service
description: Introduction to the Architecture of Adobe Experience Manager as a Cloud Service.
exl-id: fb169e85-ac19-4962-93d9-abaed812f948
---
# An Introduction to the Architecture of Adobe Experience Manager as a Cloud Service {#an-introduction-to-the-architecture-adobe-experience-manager-as-a-cloud-service}

>[!CONTEXTUALHELP]
>id="intro_aem_cloudservice_architecture"
>title="Introduction to AEM as a Cloud Service Architecture"
>abstract="In this tab, you can view the new architecture of AEM as a Cloud Service and understand the changes. AEM has resulted in a dynamic architecture with a variable number of images so it is important to take the time to understand.the cloud architecture"
>additional-url="https://video.tv.adobe.com/v/330542/" text="Architecture Overview"


Adobe Experience Manager (AEM) as a Cloud Service has resulted in changes to the architecture.

## Scaling {#scaling}

AEM as a Cloud Service now has:

* A dynamic architecture with a variable number of AEM images.

![Dynamic architecture](assets/concepts-01.png "Dynamic architecture")

This architecture:

* Is scaled based on the *actual* traffic and *actual* activity.

* Has individual instances that only run when needed.

* Uses modular applications.

* Has an author cluster as default; this avoids downtime for maintenance tasks.

This enables autoscaling for varying usage patterns:

![Autoscaling for varying usage patterns](assets/concepts-02.png "Autoscaling for varying usage patterns")

To achieve this, all instances of the AEM as a Cloud Service are created equal, each with the same default sizing characteristics in terms of the number of nodes, allocated memory and allocated computing capacity. 

AEM as a Cloud Service is based on the use of an orchestration engine that:

* Constantly monitors the state of the service.

* Dynamically scales each of the service instances as per the actual needs; both scaling up or down as appropriate. 

This:

* Is applicable to the number of nodes, the amount of memory and the allocated CPU capacity on each node.

* Allows AEM as a Cloud Service to accommodate your traffic patterns as they change.

The scaling of per-tenant instances of the service can be automatic or manual, on the two axes:

* Vertical: allocated memory and CPU capacity can be scaled up or down for a fixed number of nodes.

* Horizontal: the number of nodes for a given service can be increased or decreased.

## Environments {#environments}

>[!NOTE]
>For further information see [Deploying - Runmodes](/help/implementing/deploying/overview.md#runmodes)

AEM as a Cloud Service is made available as individual instances  with each instance representing a complete AEM environment. 

There are three types of environments available with AEM as a Cloud Service:

* **Production environment**: hosts the applications for the business practitioners.

* **Stage environment**: is always coupled to a single production environment in a 1:1 relationship. The stage environment is used for various performance and quality tests before changes to the application are pushed to the production environment.

* **Development environment**: allows developers to implement AEM applications under the same runtime conditions as the stage and production environments.

   Refer to [Managing Environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html?lang=en#using-cloud-manager) for more details.

## Programs {#programs}

Any new AEM project is always bound to exactly one specific codebase, where you can store both configuration and custom code for your project. This information is stored in a code repository, accessible via the usual Git clients, made available to you at the time new programs are created. 

An AEM program is the container that includes:

| Program Element | Number |
|--- |--- |
| Code repository (Git) | 1 |
| Baseline image (Sites or Assets) | 1 |
| Stage and production environment set (1:1) | 0 or 1 |
| Non-production environments (development or demonstration) | 0 to N |
| Pipeline for each environment | 0 or 1 |

Two types of programs are initially available for AEM as a Cloud Service:

* AEM Cloud Sites Service

* AEM Cloud Assets Service

Both of these allow access to a number of features and functionalities. The author tier will contain all Sites and Assets functionality for all programs, but the Assets programs will not have a publish tier by default.

## Runtime Architecture {#runtime-architecture}

There are various main components of this new architecture:

<!--- needs reworking -->

![AEM as a Cloud Service - Runtime Architecture](assets/concepts-03.png "AEM as a Cloud Service - Runtime Architecture")

* For AEM Sites as a Cloud Service:

  * There continues to be the concept of an authoring tier and a publish tier for each environment (at a high level).

  * The author tier is made of two or more nodes within a single author cluster. It scales automatically, dependent on the authoring activity.

    * Content authors/creators login to the AEM author tier to create, edit, and manage content.

    * Logging into the author tier is managed by the Adobe Identity Management Services (IMS).

    * Assets integration and processing use a dedicated Assets Compute Service.

  * The publish tier is comprised of two or more nodes within a single publish farm: they can operate independently from each other. Each node consists of an AEM publisher and a web server equipped with the AEM Dispatcher module. It scales automatically with site traffic needs.
  
    * End users, or site visitors, visit the website via the AEM Publish Service.

* For AEM Assets as a Cloud Service:
  
  * The architecture only includes an authoring environment.

* Both the author tier and publish tier read and persist content from/to a Content Repository Service.

  * The publish tier only reads content from the persistence layer.

  * The author tier reads and writes content from and to the persistence layer.

  * The blobs storage is shared across the publish and the author tier; files are not *moved*.

  * When content is approved from the author tier, this is an indication that it can be activated, therefore pushed to the publish tier persistence layer. This happens via the Replication Service, a middleware pipeline. This pipeline receives the new content, with the individual publish service nodes subscribing to the content pushed to the pipeline.

    >[!NOTE]
    >
    >For more details see [Replication](/help/operations/replication.md).

  * Developers and administrators manage the AEM as a Cloud Service application by using a Continuous Integration/Continuous Delivery (CI/CD) service, made available via the [Cloud Manager](/help/overview/what-is-new-and-different.md#cloud-manager)). This includes code and configuration deployments using the Cloud Manager's CI/CD pipeline. Anything related to monitoring, maintenance and troubleshooting (for example, log files) is exposed to customers within Cloud Manager.
  
  * Accessing the author and publish tiers always happens via a load balancer. This is always up-to-date with the active nodes in each of the tiers.

  * For the publish tier, a Continuous Delivery Network (CDN) Service is also available as the first entry point.

* For demonstration instances of AEM as a Cloud Service the architecture is simplified to a single author node. Therefore it does not present all the characteristics of standard development, stage or production environment. This also means that there can be some downtime and there is not support for backup/restore operations.

## Deployment Architecture {#deployment-architecture}

Cloud Manager manages all updates to the instances of the AEM as a Cloud Service. It is mandatory, being the only way to build, test, and deploy the customer application, to both the author and the publish tiers. These updates can be triggered by Adobe, when a new version of the AEM Cloud Service is ready, or by the Customer, when a new version of their application is ready.

Technically, this is implemented due to the concept of a deployment pipeline, coupled to each environment within a program. When a Cloud Manager pipeline is running, it creates a new version of the customer application, both for the author and the publish tiers. This is achieved by combining the latest customer packages with the latest baseline Adobe image. When the new images are built and tested successfully, Cloud Manager fully automates the cutover to the latest version of the image by updating all service nodes using a rolling update pattern. This results in no downtime for either the author or publish service.

<!--- needs reworking -->

![AEM as a Cloud Service - Deployment Architecture](assets/concepts-04.png "AEM as a Cloud Service - Deployment Architecture")

## Content Distribution {#content-distribution}

Adobe Experience Manager as a Cloud Service has modified the way publishing content works. With AEM as a Cloud Service, the replication framework from previous versions of AEM is no longer used to publish pages (move changes from author instance to publish instances).

AEM as a Cloud Service now uses the [Sling Content Distribution](https://sling.apache.org/documentation/bundles/content-distribution.html) capability to move the appropriate content. This uses a pipeline service run on Adobe I/O, which is outside the AEM runtime. 

The setup is automated, including automatic self-configuration when publish nodes are added, removed or recycled during runtime.

A single publish or unpublish request can include multiple resources, but will return a single status applied to all; it will succeed for all resources in the AEM Publish Service, or fail for all. This ensures that the resources within the AEM Publish Service will never be in a inconsistent state.

**High-level Content Distribution Architecture Diagram**

![High-level Content Distribution Architecture Diagram](assets/architecture-diagram.png "High-level Content Distribution Architecture Diagram")

## Key Evolutions {#key-evolutions}

The new architecture for AEM as a Cloud Service introduces some fundamental changes and innovations compared to the previous generations:

* All files (blobs) are directly uploaded and served from a cloud data store. The associated stream of bits never goes through the JVM of the AEM Author and Publish services. As a result, the nodes of the AEM author and publish services can be smaller in size and more compatible with the expectation of fast autoscaling. For business practitioners, this results in a faster experience when uploading and downloading images, video, etc.

* All operations consisting of publishing content now involve a pipeline following a subscription pattern. Published content is pushed to various queues in the pipeline, to which all nodes of the publish service subscribe. As a result, the author tier does not need to be aware of the number of nodes in the publish service; this allows for fast autoscaling of the publish tier.

* The concept of a golden master was introduced for automating the lifecycle of the publish nodes. The golden master is a specialized publish node, never accessed by any end user, and from which all the nodes of the publish service are created. Maintenance operations such as compaction are performed on the content repository attached to the golden master. The publish nodes are recycled daily and do not require any sort of routine maintenance; in the past such maintenance required some downtime, especially for the author instance.

* The architecture completely separates the application content from the application code and configuration. All code and configuration is practically immutable and baked into the baseline image used to create the various nodes of the author and publish services. As a result, there is an absolute guarantee that each node is identical, and the changes to code and configuration can only be made globally by running a Cloud Manager pipeline.
