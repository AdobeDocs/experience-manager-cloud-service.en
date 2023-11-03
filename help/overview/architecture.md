---
title: Introduction to the Architecture of Adobe Experience Manager as a Cloud Service
description: Introduction to the Architecture of Adobe Experience Manager as a Cloud Service.
exl-id: 3fe856b7-a0fc-48fd-9c03-d64c31a51c5d
---
# An Introduction to the Architecture of Adobe Experience Manager as a Cloud Service {#an-introduction-to-the-architecture-adobe-experience-manager-as-a-cloud-service}

>[!CONTEXTUALHELP]
>id="intro_aem_cloudservice_architecture"
>title="Introduction to AEM as a Cloud Service Architecture"
>abstract="In this tab, you can view the new architecture of AEM as a Cloud Service and understand the changes. AEM has resulted in a dynamic architecture with a variable number of images so it is important to take the time to understand the cloud architecture."
>additional-url="https://video.tv.adobe.com/v/330542/" text="Architecture Overview"

Adobe Experience Manager (AEM) as a Cloud Service offers a set of composable services for the creation and management of high impact experiences. 

This page covers the logical architecture, the service architecture, the system architecture, and the development architecture for AEM as a Cloud Service.

## Logical architecture {#logical-architecture}

AEM as a Cloud Service is made up of high-level solutions such as AEM Sites, AEM Assets, and AEM Forms. These services are licensed individually, but can be used in collaboration. Each solution uses a combination of the composable services that AEM as a Cloud Service provides, dependent on their respective use cases.

### Programs {#programs}

AEM applications are materialized in the form of a Program that is created by the customers in the Cloud Manager application, in a self-service manner according to their licensing entitlements. The programs give full control and autonomy for the customers in the way the associated AEM application is named, configured and permissioned in the context of a particular project (link: cloud manager programs)

A customer is usually known to Adobe as a “tenant”, or sometimes also known as an “IMS” (Identity Management System) organization. A tenant can have as many programs as needed and licensed. For instance, it’s quite usual to see a central program for AEM Assets, while AEM Sites might be used in multiple programs corresponding to multiple online experiences. Note that the AEM Edge Delivery Services are exposed as a top-level solution in Cloud Manager while being part of the other main solutions from a licensing standpoint (e.g. AEM Sites with Edge Delivery Services).

A program can be configured to leverage from one to all these high-level solutions. Each can support from one-to-many add-ons itself (e.g., Commerce or Screens for AEM Sites, or Dynamic Media or Brand Portal for AEM Assets). 

![AEM as a Cloud Service - Programs](assets/architecture-aem-edge-programs.png "AEM as a Cloud Service - Deployment Architecture")

### Environments {#environments}

Once a program is created with the AEM Sites, AEM Assets or AEM Forms solutions, the associated AEM instances will be represented in the form of AEM environments in this program.

There are four types of environments available with AEM as a Cloud Service:

* Production environment:

  * A production environment hosts the applications for the business practitioners and runs the live experiences.

* Stage environment:

  * A stage environment is usually coupled to a production environment in a 1:1 relationship. The stage environment is primarily designed for automated testing before changes to the application are pushed to the production environment, independently from the changes being initiated by Adobe as part of a maintenance update or by customers as part of a code deployment. Manual testing can also be conducted by customer in case of a code deployment. The content of the stage environment is usually kept in sync with the production content using the self-service content copy feature.
* Development environment:
  * A development environment allows developers to implement and to test AEM applications under the same runtime conditions as the stage and production environments. The changes are going through a deployment pipeline allowing for the same code quality and security gates as in production deployment pipelines.
* Rapid development environment (RDE):
  * An RDE environment allows for rapid development iterations for deploying new or existing code into the RDE instances, without going through a formal deployment pipeline that is found on regular development environments.

(link: Cloud Manager, manage environments).

### Edge Delivery Services {#logical-architecture-edge-delivery-services}

An AEM program can be configured with the Edge Delivery Services as well. Once done, it allows to reference GitHub code repositories used for building the experiences with Edge Delivery Services. As a result, new configuration options such as setting up the Adobe-Managed CDN, accessing to licensing metrics or the SLA reports becomes available for the associated experiences.
 
## Service architecture {#service-architecture}

The list of high-level composable services in AEM as a Cloud Service can be represented like this:

![AEM as a Cloud Service Overview - with Edge Delivery Services](assets/architecture-aem-edge.png "AEM as a Cloud Service Overview - with Edge Delivery Services")

The lower part of is made of the services allowing for content management, while the upper part if made of services allowing for experience delivery.

For content management, there’s two main set of services allow for the authoring of content, both represented as “content sources”:

* The AEM Author tier, providing a web-based interface (with associated APIs) for the management of Web content both in headful (via the page editor or via the universal visual editor) and in headless (via the content fragment editor) ways.
* The Document-based authoring tier, allowing to leverage standard applications such as Microsoft Word and Excel (via SharePoint), or Google Docs or Sheets (via Google Drive), to author content from these well-known applications.

For experience delivery, when using AEM Sites or AEM Forms, there’s also two main sets of services, non-mutually exclusive and operating under a shared Adobe-Managed CDN (content delivery network) as different origins:

* The AEM Publish tier, running a farm of standard AEM publishers and dispatchers, allowing for the dynamic rendering of web pages and API content (e.g., GraphQL) assembled with published content, based on server-side application logic primarily,
* The Edge Delivery Publish Tier, allowing for the dynamic rendering of web pages and API content from various content sources such as the AEM Author tier or the Document-based authoring tier, based on client-side application logic and designed for maximum performance.

It’s also worth noting the adjacent services:

* The Edge Delivery Assets Tier, allowing for the delivery of approved and published media items (e.g. images, videos) out of AEM Assets. The media items are usually referenced from experiences running on the AEM publish tier, or the Edge Delivery publish tier, or from any other Adobe Experience Cloud application integrated with AEM Assets
* The AEM Preview tier and the Edge Delivery Services Preview tier are also available for experiences built with the AEM Publish tier or the Edge Delivery publish tier respectively, allowing content authors to preview content in-context before publish operations. 

>[!NOTE]
>
>Assets-only programs do not have a publish tier nor a preview tier by default.

There are other “adjacent” services to highlight:

* The replication service, situated in between the content management tier and the experience delivery tier, is responsible for processing the “publish” operations issued by content authors and for providing the published content to the publish tiers (AEM or Edge Delivery). It is worth mentioning that the replication service went through a complete redesign compared to the 6.x versions of AEM, as the replication framework from previous versions of AEM is no longer used to publish content. The latest architecture is based on a “publish and subscribe” approach with cloud-based content queues. For the AEM publish tier, it allows a variable number of publishers to subscribe to the publish content and it was essential to achieve true and rapid autoscaling for AEM as a Cloud Service
* The content repository service, leveraged by the AEM author tier, is a cloud-based instance of a JCR-compliant content repository, implemented by the Apache Oak technology.  The persistence of content is primarily based on blob-based cloud storage.
* The CI/CD service represents the subset of Cloud Manager functionalities dedicated to managing deployment pipelines to the AEM environments.
* The testing service represents the underlying infrastructure used to execute functional tests, UI tests (e.g. based on Selenium or Cypress scripts), experience audit tests (e.g. Lighthouse scores), as part of a deployment pipeline to an AEM environment or as part of a GitHub pull request to an Edge Delivery code repository
* The data service is responsible for exposing customer data both via APIs and within product user interfaces (e.g., Cloud Manager), such as licensing metrics (e.g. Content Requests, Storage, Users) or usage reports (e.g. number of uploads, downloads)
* The real-user metric (RUM) service is responsible to both collect key metrics from a customer experience (e.g., page views, core web vitals, conversion events) and to respond to associated queries (e.g. top page views for a given domain in the last 7 days)
* The assets compute service is responsible for processing uploaded images, videos and documents (e.g. PDF or Photoshop files) in order to extract image and video metadata (via Adobe Sensei, e.g descriptive tags or primary color tones) and to generate renditions (e.g. in different sizes or formats), with access to the Adobe Photoshop and Lightroom APIs in this context
* The identity management service is the central place responsible for managing and authenticating users and user groups for a given Adobe Experience Cloud application (e.g. Cloud Manager or the AEM author tier), accessed via the Adobe Admin Console
 
## System architecture {#system-architecture}

### AEM Publish and Author Tiers {#aem-publish-author-tiers}

The AEM publish and author tiers are implemented as a set of Docker containers, operated by a standard Container Orchestration Service. The resulting containerized architecture means a fully dynamic system with a variable number of pods depending on actual activity (for content management) and actual traffic (for experience delivery): AEM as a Cloud Service accommodates your traffic patterns as they change.

The AEM author tier is operated as a cluster of AEM author pods sharing a single content repository. A minimum of two pods allows for business continuity while maintenance tasks are running or while a deployment process is happening. 

The AEM publish tier is operated as a farm of AEM publish instances each with their own content repository of published content. Each publisher is coupled to a single Apache instance equipped with the AEM dispatcher module for a materialized view of the content, serving as the origin for the Adobe-managed CDN. A minimum of two pods allows for business continuity as well, but it’s not unusual to see this number expanding in periods of high traffic.

The AEM preview tier is comprised of a single AEM node. This used for quality assurance of content before publishing to the publish tier. Occasional downtime, especially during deployments, can happen on the preview tier.

### Edge Delivery Services {#system-architecture-edge-delivery-services}

The Edge Delivery Services are operated on top of a CDN and serverless infrastructure for assembling the pages in the most performant way. When a resource is requested, the serverless infrastructure is responsible for converting the published content into semantic HTML and serves as the origin to the CDN.

The conversion to semantic HTML happens from the published content out of the AEM author tier or out of the document-based authoring environment.

The following diagram illustrates how you can edit Sites content in Microsoft Word (document-based authoring) and publish to Edge Delivery. It also shows the traditional AEM publishing method using the various editors.

![AEM Sites as a Cloud Service - with Edge Delivery Services](assets/architecture-aem-edge-author-publish.png "AEM Sites as a Cloud Service - with Edge Delivery Services")

As Edge Delivery Services are part of Adobe Experience Manager and as such, Edge Delivery, AEM Sites and AEM Assets can co-exist on the same domain. This is a common use case for larger websites. For instance, a customer might want to migrate a particular page with high traffic to Edge Delivery Services, while all other pages might remain on the AEM Publish Tier.
 

## Development Architecture {#development-architecture}

### Code repositories {#code-repositories}

The code and configuration for AEM projects is necessarily stored in a code repository, from which deployment pipelines are issued when changes are made. There are code repositories of different type:

* AEM full stack:
  * allows for storing server-side Java code and OSGI configurations for the AEM author and publish tiers.
* AEM front end:
  * allows for storing client-side JS, CSS and HTML code for the AEM author and publish tiers (link to clientlibs)
* AEM web tier:
  * allows for storing the dispatcher configuration files for the AEM publish tier.
* AEM configuration:
  * allows for storing various configuration options (e.g. CDN settings, or maintenance tasks settings) for the AEM publish tier and the Edge Delivery Services publish tier.
* AEM edge delivery:
  * allows for storing the client-side JS, CSS and HTML code for the sites built with the Edge Delivery Services 

### Deployment pipelines {#deployment-pipelines}

Developers and administrators manage the AEM as a Cloud Service application by using a Continuous Integration/Continuous Delivery (CI/CD) service, made available via the Cloud Manager. Cloud Manager is also where anything related to monitoring, maintenance, troubleshooting (for example, access to log files) or licensing is exposed.

![AEM as a Cloud Service - Deployment Architecture](assets/architecture-aem-edge-deployment-pipelines.png "AEM as a Cloud Service - Deployment Architecture")

Cloud Manager manages all updates to the instances of the AEM as a Cloud Service. It is mandatory, being the only way to build, test, and deploy the customer application, to both the author, the preview, and the publish tiers. These updates can be triggered by Adobe, when a new version of the AEM Cloud Service is ready, or by the Customer, when a new version of their application is ready.

Technically, this is implemented via the concept of a deployment pipeline, coupled to each environment within a program. When a Cloud Manager pipeline is running, it creates a new version of the customer application, both for the author and the publish tiers. This is achieved by combining the latest customer packages with the latest baseline Adobe image.

The deployment pipeline is triggered either when customers are making code changes, or when Adobe is deploying a new maintenance release.

In both cases, the same set of automated tests is executed. It is made of tests contributed by Adobe to ensure the product integrity, and tests contributed by the customer: functional tests (http) or UI tests (based on Selenium or Cypress technology).

These automated tests are happening on the Stage environment – that’s why it’s important to keep the Stage environment content as close as possible to the content on the Production instance. When passing all tests, the new code is deployed to the Production environment.

### Rolling updates {#rolling-updates}

Cloud Manager fully automates the cutover to the latest version of the AEM application by updating all service nodes using a rolling update pattern. This results in no downtime for either the author or publish service.

## Major innovations since AEM 6.x {#major-innovations-since-aem-6x}

The latest architecture for AEM as a Cloud Service introduces some fundamental changes and innovations compared to the previous generations:

* All files are directly uploaded and served from a cloud data store. The associated stream of bits never goes through the JVM of the AEM Author and Publish services. As a result, the nodes of the AEM author and publish services can be smaller in size and more compatible with the expectation of fast autoscaling. For business practitioners, this results in a faster experience when uploading and downloading images, video, etc.

* All operations consisting of publishing content now involve a pipeline following a subscription pattern. Published content is pushed to various queues in the pipeline, to which all nodes of the publish service subscribe. As a result, the author tier does not need to be aware of the number of nodes in the publish service; this allows for fast autoscaling of the publish tier.

* The architecture completely separates the application content from the application code and configuration. All code and configuration is practically immutable and baked into the baseline image used to create the various nodes of the author and publish services. As a result, there is an absolute guarantee that each node is identical, and the changes to code and configuration can only be made globally by running a Cloud Manager pipeline.

* The architecture includes multiple micro-services built on serverless technology, especially with the Adobe I/O runtime

## Further Information {#further-information}

See also:

* Edge Delivery Services:

  * [AEM as a Cloud Service Overview - with Edge Delivery Services](/help/edge/overview.md)
  * [Using Edge Delivery Services](/help/edge/using.md)
  * [Explore the underlying architecture and important pieces of AEM as a Cloud Service with Edge Delivery Services](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/introduction/architecture.html)


![AEM as a Cloud Service - Deployment Model](assets/architecture-aem-edge-deployment-model.png "AEM as a Cloud Service - Deployment Model")


![AEM as a Cloud Service - Deployment Architecture](assets/architecture-aem-edge-deployment-pipelines.png "AEM as a Cloud Service - Deployment Architecture")
