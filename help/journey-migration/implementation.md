---
title: Implementation Phase
description: Making sure your code and content are ready for the migration to the cloud
exl-id: d124f9a5-a754-4ed0-a839-f2968c7c8faa
feature: Migration
role: Admin
---
# Implementation Phase {#implementation-phase}

In the implementation phase of the journey, you will explore the tools through which you can make your code and content ready to be moved over to AEM as a Cloud Service.

## The Story So Far {#story-so-far}

In the previous parts of the journey, you have gone through [getting familiar with the changes in AEM as a Cloud Service](/help/journey-migration/getting-started.md), and determined if your deployment is ready to be moved to the cloud with the [readiness phase](/help/journey-migration/readiness.md).

This article continues on with advice on how to use Adobe provided tools to make sure that your code and content are ready to be moved to the cloud.

## Objective {#objective}

This document aims to:

* Introduce you to Cloud Manager, AEM's continuous integration and delivery framework used to deploy code to AEM as a Cloud Service
* Get you up to speed with the content transfer tool
* Describe the code refactoring tools you have to use so you can modernize your code for AEM as a Cloud Service

## Using Cloud Manager {#using-cloud-manager}

Before you start, you must familiarize yourself with Cloud Manager since it is the sole mechanism for deploying code to AEM as a Cloud Service.

Cloud Manager enables organizations to self-manage AEM in the Cloud. It includes a continuous integration and continuous delivery (CI/CD) framework that lets IT teams and implementation partners expedite the delivery of customizations or updates without compromising performance or security.

You can get familiar with using Cloud Manager by consulting the resources below:

* [Onboarding Journey](/help/journey-onboarding/overview.md) to understand self-help resources about onboarding for Experience Manager as a Cloud Service.

* [Integrating Git with Adobe Cloud Manager](/help/implementing/cloud-manager/managing-code/integrating-with-git.md) to learn about using a Single Git repository to deploy code.

* [Adobe Experience as a Cloud Service Configuration](/help/security/ims-support.md#aem-configuration) to learn about Managing Products and User Access in Admin Console.

## Use the Adobe Provided Tools to Make Your Content and Code Cloud Ready {#use-tools-to-make-code-and-content-cloud-ready}

The exact steps of your transition to Cloud Service depend on the systems you have purchased and the software development life-cycle practices you follow.

The following figure shows the main steps involved in the phase that involves converting your code and content for use with AEM as a Cloud Service:

![Conversion steps](/help/journey-migration/assets/exec-image1.png)

We will start detailing the tools you must use so you can achieve this in the chapters below.

## Content Migration {#content-migration}

To migrate content from your current AEM instance to your Cloud Service instance, you can use Adobe's Content Transfer Tool.

With this tool, you can specify the desired content subset that you want to transfer from your source AEM instance to your AEM Cloud Service instance.

Content Migration is a multi-step process that requires planning, tracking, and collaboration between different teams. 

For a complete detail on how the tool works and how Adobe recommends that you use it, see the [Content Transfer Tool documentation](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/overview-content-transfer-tool.md).

## Code Refactoring {#code-refactor}

### Set Up for Development {#set-up-for-development}

It is time to start refactoring the existing features to be compatible with Cloud Services.

First, look at the documentation detailing the basic tooling, and start refactoring your code:


* During planning, it is a good idea to have a list of areas that must be refactored to be compatible with AEM as a Cloud Service. You can review [Development Guidelines](/help/implementing/developing/introduction/development-guidelines.md) for more details on how to refactor and optimize code for Cloud Service.  
* Read up on how to [Manage Configurations](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/configurations.html#what-is-a-configuration) in AEM as a Cloud Service.
* Learn how to set up a Local Development Environment by downloading the [AEM as a Cloud Service SDK](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/aem-as-a-cloud-service-sdk.html)
* Finally, familiarize yourself with the [AEM as a Cloud Service Java API](https://www.adobe.io/experience-manager/reference-materials/cloud-service/javadoc/index.html).

Also, you can also:

* Watch this video to understand how to install the Dispatcher SDK locally:

  >[!VIDEO](https://video.tv.adobe.com/v/30601)

* Watch this video to understand how to configure Dispatcher SDK:

  >[!VIDEO](https://video.tv.adobe.com/v/30602)

### A Change in Mindset {#a-change-in-mindset}

Developing and running code in AEM as a Cloud Service requires a change in the mindset. It should be noted that code must be resilient, especially as an instance might be stopped at any time. Code running in Cloud Service must be aware of the fact that it is always running in a cluster. This means that there is always more than one instance running.

Certain changes are required for AEM Maven projects to be cloud compatible. AEM as a Cloud Service requires a separation of *content* and *code* into distinct packages for deployment into AEM:  

* `/apps` and `/libs` are considered immutable areas of AEM as they cannot be changed after AEM starts (that is to say at runtime). This includes create, update or delete operations. Any attempt to change an immutable area at runtime will fail.

* Everything else in the repository, (for example, `/content` , `/conf` , `/var` , `/home` , `/etc` , `/oak:index` , `/system` , `/tmp`) are all mutable areas, meaning they can be changed at runtime.

You can learn more by consulting the [Recommended Package Structure](/help/implementing/developing/introduction/aem-project-content-package-structure.md#recommended-package-structure) documentation. 


### Cloud Migration Tools {#cloud-migration-tools}

Adobe provides several tools to help accelerate some of your code refactoring tasks. Understanding these tools and the problems they solve will reduce migration complexity and time.

* [Asset Workflow Migration](/help/journey-migration/moving-to-aem-assets/asset-workflow-migration-tool.md), a tool that is used to automatically migrate asset processing workflows
* [Dispatcher Converter](/help/journey-migration/refactoring-tools/dispatcher-transformation-utility-tools.md), a tool that converts your existing Dispatcher configurations into a format that is ready for AEM as a Cloud Service.
* [Repository Modernizer](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/moving/refactoring-tools/repo-modernizer.html), a tool that takes an AEM Multimode project as input and converts it into an AEM as a Cloud Service one
* [Index Converter](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/moving/refactoring-tools/index-converter.html), a tool that converts indexes into a form compatible with AEM as a Cloud Service
* [Modernization Tools](/help/journey-migration/refactoring-tools/aem-modernization-tools.md), a suite of utilities which can be used to convert legacy AEM features to the modern and supported capabilities of AEM as a Cloud Service.

Once you have set up the local development environment, get familiar with the AEM as a Cloud Service SDK by consulting the [documentation](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md).

### Schedule a Code Freeze {#schedule-a-code-freeze}  

To manage your on-going code development on your active AEM along with the code refactoring tasks as part of your transition journey, Adobe recommends that you schedule a code freeze period until you have completed restructuring your Maven project to be compatible with AEM as a Cloud Service.

Once the project restructuring is done, you can resume new code development based on this new structure. This reduces Cloud Manager pipeline failures during code deployment and testing.

>[!NOTE]
>The Content Transfer and Code Refactor tasks do not have to be done sequentially. These tasks can be done independent of each other. However, the correct project structure is required to ensure that the content successfully renders in your Cloud Service environment.

## Best Practices for Code Deployment and Testing {#best-practices}

The Cloud Manager pipeline supports execution of tests that run against the stage environment.

Follow the best practices in the documents below regarding code quality testing:

* [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md), a document that describes the process of writing test scripts and explains the concept of recommended coverage of at least 50%.
* [Understanding Custom Code Quality Rules](/help/implementing/cloud-manager/custom-code-quality-rules.md) which aims to describe the custom code quality rules executed by Cloud Manager created based on best practices from AEM Engineering.

## Preparing for Go-Live {#preparing-for-go-live}

Preparing the source system for migration involves system and AEM administrator level tasks. You can start by verifying that the content repository is in a well maintained state by checking the [revision cleanup](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/deploying/revision-cleanup.html) and the [data store garbage collection](https://experienceleague.adobe.com/docs/experience-manager-65/administering/operations/data-store-garbage-collection.html) task status. If you are running AEM version 6.3 (as the Content Transfer Tool is compatible from version 6.3 onwards), it is recommended to perform offline compaction, followed by Data Store Garbage collection.

[Data consistency check](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/configuring/consistency-check.html) is recommended across all AEM versions to ensure that the content repository in a good state to initiate migration activities.

System administrator level access is required to install and configure [AZCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md)

It is also recommended you review any unused Assets, Pages, AEM Projects, Users and Groups to save time on migration. See the [Content Repository Health](#repository-health) section.

### Content Repository Health {#repository-health}

Once access to a [production clone](#proof-of-migration) is established proceed to check the health of the repository. As mentioned in the previous section, the goal is to clean and compact the repository on the source before starting the migration. This step will potentially save much time otherwise spend on troubleshooting issues once the migration starts.

| Action Item | Key Takeaways |
|---------|----------|
Users, Groups and Permissions | You need to understand the volume of users, groups, and complexity around memberships. Look for opportunities to clean up any unused users, groups in the source before migration.
Incomplete Asset processing | Try to complete the processing of assets in the source system before starting the migration to avoid potential concerns in AEM as a Cloud Service post migration. |
Content Health | It is recommended to query for bad content and purge it before you start the migration. For example, look for assets or pages that do not have original renditions or that are stuck in workflow processing. Also see [Asset Health](#asset-health). |

## Gathering Data {#gathering-data}

>[!NOTE]
> The [Content migration strategy and timeline](#content-strategy-and-timeline) section further details how to extrapolate the gathered data and create a migration plan.

Gathering data can help you plan the migration activities and associated tasks. The extraction and ingestion times are particularly useful because the data points can be associated with a specific size of the migration set. As such, these data points can be extrapolated to come up with a plan:

* Total amount of time taken for [extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md)
* Total amount of time taken for [ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md)
* Total amount of time taken for top-up [extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process)
* Total amount of time taken for top-up [ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process)


<!-- Alexandru: hiding this for now

One more important datapoint is the amount of time it takes to complete the [user mapping](/help/journey-migration/content-transfer-tool/user-mapping-tool/overview-user-mapping-tool.md), if this is coupled with the content migration. You can take this data point into consideration for more realistic estimates, because it is added to the overall extraction timeline and it may not be required to run it during top-ups.

-->

These data points can also help you [Establish KPI's](/help/journey-migration/readiness.md#establish-kpis) and other migration related tasks.

### Migration plan {#migration-plan}

Based on the data points you gathered (see above), you can create a migration plan that can be integrated into a macro project plan. This step will enable all the key stakeholders to visualize and plan around the migration activities.

The following table illustrates a typical migration plan:

| Migration Iteration | Start Date | Estimated End Date | Dependencies | Estimated Duration (in days) | Additional Details / Action Items |
|---|---|---|---|---|---|
| PRDCLONE-AUTHOR-INITIAL-USRMAP-CSSTAGE-AUTHOR |   |   |   |   |   |
| PRDCLONE-PUBLISH-TOPUP-CSSTAGE-AUTHOR |   |   |   |   |   |

As you can see in the table above, it is helpful to follow a specific naming format to identify the migration iterations, for example: **PRDCLONE** for the source AEM environment , **AUTHOR/PUBLISH** for the AEM as a Cloud Service environment, **CSSTAGE-AUTHOR** for the AEM as a Cloud Service instance, and so on.

Some important details that influence your migration plan:

**The Total Number of Extractions required**

* Author and Publish extractions in specific environments are considered as two parallel extractions as they are independent of each other.
* Number of Top Up extractions based on repository growth in specific time periods.

**Total Number of Ingestions required**

* It is important to capture this item into the plan, as an extracted set can be ingested into multiple Cloud Service environments.
* Number of Top-up ingestions.
* Migrating content from the Source Author to the Cloud service Author instance and from the Source Publish to Cloud Service Publish is the best practice to avoid ingesting all the Author content into the Cloud Service Publish.

### Migration Tracker {#migration-tracker}

You can use the migration tracker to note down the times for both the initial and top up runs. These data points will help you formulate realistic content freeze requirements before the final top-up.

The tracker will also help you to:

* Identify any deviations from the planner that require adjustments in the plan or go-live timelines
* Provide a realistic status that can be used in all necessary communications
* Plan for initial or future top-up migrations

The following table illustrates a functional migration tracker:

| Source (Environment / Instance / URL) | Destination (Environment / Instance / URL) | Migration Set Name, Type (Initial or Top up) | Migration Set Size (MB) | User Mapping (Yes / No) | Extraction Duration (Start, End, Time taken) | Ingestion Duration (Start, End, Time taken) | Issues / Resolutions / Details |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |

## Content migration strategy and timeline {#content-strategyand-timeline}

The following section shows the important steps and associated tasks that can be used to formulate a content migration strategy and timeline.

![Steps to formulate a migration strategy](/help/journey-migration/assets/content-migration2.png)

### Fitment {#fitment}

* Perform revision cleanup, data store garbage collection and data consistency checks. See also [Preparing for Go-Live](#preparing-for-go-live)
* [Gather statistics](#gathering-data) about the AEM source repository:
  * Segment store size
  * Index store size
  * Number of pages
  * Number of assets
  * Number of users and groups
* Know whether the following features are enabled on the AEM source (also required in AEM as a Cloud Service):
  * Smart tagging
  * Similarity search
  * Search for containing text in word and pdf documents
* Collect the Best Practice Analyzer [report](/help/journey-migration/best-practices-analyzer/overview-best-practices-analyzer.md)
* Import into the [Cloud Acceleration Manager](/help/journey-migration/cloud-acceleration-manager/introduction/overview-cam.md)
  * Review the self-analysis recommendation to make sure that AEM as a Cloud Service can handle the storage requirements.
* Create an Adobe Support ticket for any clarifications before continuing with the migration plan.

### Proof of migration {#proof-of-migration}

* Request a production clone that:
  * Is in the same network zone
  * Will provide production content like users and groups
  * Clones author and publish - one node each in case of a cluster or publish farm
* Choose a subset of the content that is migrated so that:
  * It is a mix of all the available content types
  * Contains all users and groups
* Includes either 25% of the content or up to 1 TB of content, whichever is less.
* Execute at least one full and [top-up](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process) migration, from the production clone into the AEM as a Cloud Service non-production environment
* Resolve any potential issues like:
  * Disk space on the AEM source
  * Connectivity between the AEM source and AEM as a Cloud Service
  * Any [ingestion related limitations](go-live.md#known-limitations).
* Record the time taken for [extraction and ingestion](#gathering-data):
  * Know how much content is added per week
  * Extrapolate the times measured from the proof of migration to create a [migration plan](#migration-plan).

## What's Next {#what-is-next}

After you have fully understood how to assess if your AEM installation is ready to be moved to the cloud, as we as learn how to use the tools needed to make it ready, it's time to move on to the [go-live phase](/help/journey-migration/go-live.md).
