---
title: Go-Live
description: Learn how to perform the migration once the code and the content are cloud ready
---

# Go-Live {#go-live}

In this part of the journey, you will learn how to plan and perform the migration once both the code and the content are ready to be moved over to AEM as a Cloud Service. Additionally, you will also learn what are the best practices and known limitations when performing the migration.

## The Story So Far {#story-so-far}

In the previous phases of the journey:

* You learned how to get started with the move to AEM as a Cloud Service in the [Getting Started](/help/journey-migration/getting-started.md) page.
* Determined if your deployment is ready to be moved to the cloud by reading the [Readiness phase](/help/journey-migration/readiness.md)
* As well as the tools through which you can make your code and content cloud ready with the [Implementation phase](/help/journey-migration/implementation.md).

## Objective {#objective}

This document will help you understand how to perform the migration to AEM as a Cloud Service once you are familiar with the previous steps of the journey. You will learn the content migration strategy and timeline, how to gather data, create a migration plan, as well as the best practices to follow when migrating to AEM as a Cloud Service.

## Preparing for Go-Live {#prepare-for-go-live}

Preparing the source system for migration involves system and AEM administrator level tasks. You can start by verifying that the content repository is in a well maintained state by checking the [revision cleanup](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/deploying/revision-cleanup.html) and the [data store garbage collection](https://experienceleague.adobe.com/docs/experience-manager-65/administering/operations/data-store-garbage-collection.html)task status. If you are running AEM version 6.3 (as the Content Transfer Tool is compatible from version 6.3 onwards), it is recommended to perform offline compaction, followed by Data Store Garbage collection.

[Data consistency check](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/configuring/consistency-check.html) is recommended across all AEM versions to ensure that the content repository in a good state to initiate migration activities.

System administrator level access is required to install and configure [AZCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md)

It is also recommended you review any unused Assets,Pages,AEM Projects, Users and Groups to save time on migration. See the [Content Repository Sanity](#repository-sanity) section.

### Content Repository Sanity {#repository-sanity}

Once access to a [production clone](#proof-migration) is established proceed to check the sanity of the repository. As mentioned in the previous section, the goal is to clean and compact the repository on the source before starting the migration. This step will potentially save a lot of time otherwise spend on troubleshooting issues once the migration starts.

| Action Item | Key Takeaways |
|---------|----------|
Users, Groups and Permissions | You need to understand the volume of users, groups, and complexity around memberships. Look for opportunities to clean up any unused users, groups in the source before migration.
Incomplete Asset processing | Try to complete the processing of assets in the source system before starting the migration to avoid potential concerns in AEM as a Cloud Service post migration. |
Content Sanity | It is recommended to query for bad content and purge it before you start the migration. For example, look for assets or pages that do not have original renditions or that are stuck in workflow processing. See also [Asset Sanity](#asset-sanity). |

## Gathering Data {#gathering-data}

>[!NOTE]
> The [Content migration strategy and timeline](#strategy-timeline) section further details how to extrapolate the gathered data and create a migration plan.

Gathering data can help you plan the migration activities and associated tasks. The extraction and ingestion times are particularly useful because the data points can be associated with a specific size of the migration set. As such, these data points can be extrapolated to come up with a plan:

* Total amount of time taken for [extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md)
* Total amount of time taken for [ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md)
* Total amount of time taken for top up [extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process)
* Total amount of time taken for top up [ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process)

One more important datapoint is the amount of time it takes to complete the [user mapping](/help/journey-migration/content-transfer-tool/user-mapping-tool/overview-user-mapping-tool.md) (if this is coupled with the content migration). You can take this data point into consideration for more realistic estimates, since it will be added to the overall extraction timeline and it may not be required to run it during top-ups.

These data points can also help you [Establish KPI's](/help/journey-migration/readiness.md#establish-kpis) and other migration related tasks.

### Migration plan {#migration-plan}

Based on the data points you gathered (see above), you can create a migration plan that can be integrated into a macro project plan. This step will enable all the key stakeholders to visualize and plan around the migration activities.

The following table illustrates a typical migration plan:

| Migration Iteration | Start Date | Estimated End Date | Dependencies | Estimated Duration (in days) | Additional Details / Action Items |
|---|---|---|---|---|---|
| PRDCLONE-AUTHOR-INITIAL-USRMAP-CSSTAGE-AUTHOR |   |   |   |   |   |
| PRDCLONE-PUBLISH-TOPUP-CSSTAGE-AUTHOR |   |   |   |   |   |

As you can see in the table above, it is helpful to follow a specific naming format to identify the migration iterations, for example: Source AEM Environment (PRDCLONE), AEMaaCS Environment (AUTHOR/PUBLISH), AEMaaCS Instance (CSSTAGE-AUTHOR) and so on.

Some important details that will influence your migration plan:

**The Total Number of Extractions required**

* Author and Publish extractions in specific environments are considered as two parallel extractions as they are independent of each other.
* Number of Top Up extractions based on repository growth in specific time periods.

**Total Number of Ingestions required**

* It is important to capture this item into the plan, as an extracted set can be ingested into multiple Cloud Service environments.
* Number of Top up ingestions.
* Migrating content from the Source Author to the Cloud service Author instance and from the Source Publish to Cloud Service Publish is the best practice to avoid ingesting all the Author content into the Cloud Service Publish.

### Migration Tracker {#migration-tracker}

You can use the migration tracker to note down the times for both the initial and top up runs. These data points will help you formulate realistic content freeze requirements before the final top up.

The tracker will also help you to:

* Identify any deviations from the planner that require adjustments in the plan or go-live timelines
* Provide a realistic status that can be used in all necessary communications
* Plan for initial or future top up migrations

The following table illustrates a functional migration tracker:

| Source (Env / Instance / URL) | Destination (Env / Instance / URL) | Migration Set Name, Type (Initial or Top up) | Migration Set Size (MB) | User Mapping (Yes / No) | Extraction Duration (Start, End, Time taken) | Ingestion Duration (Start, End, Time taken) | Issues / Resolutions / Details |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |

## Content migration strategy and timeline {#strategy-timeline}

The following section shows the important steps and associated tasks that can be used to formulate a content migration strategy and timeline.

![image](/help/journey-migration/assets/content-migration2.png)

### Fitment {#fitment-migration}

* Perform revision cleanup, data store garbage collection and data consistency checks. See also [Preparing for migration](#prepare-for-migration)
* [Gather statistics](#gathering-data) about the AEM source repository:
    * Segment store size
    * Index store size
    * Number of pages
    * Number of assets
    * Number of users and groups
* Know whether or not the following features are enabled on the AEM source (also required in AEM as a Cloud Service):
    * Smart tagging
    * Similarity search
    * Search for containing text in word and pdf documents
* Collect the Best Practice Analyzer [report](/help/journey-migration/best-practices-analyzer/overview-best-practices-analyzer.md)
* Import into the [Cloud Acceleration Manager](/help/journey-migration/cloud-acceleration-manager/introduction/overview-cam.md)
    * Review the self-analysis recommendation to make sure that AEM as a Cloud Service can handle the storage requirements.
* Create an Adobe Support ticket for any clarifications before continuing with the migration plan.

### Proof of migration {#proof-migration}

* Request a production clone that:
   * Is in the same network zone
   * Will provide production content like users, groups and so on
   * Clones author and publish - one node each in case of a cluster or publish farm
* Choose a subset of the content that will be migrated so that:
   * It is a mix of all the available content types
   * Contains all users and groups in case [user mapping](/help/journey-migration/content-transfer-tool/user-mapping-tool/overview-user-mapping-tool.md) is required
* Includes either 25% of the content or up to 1 TB of content, whichever is less.
* Execute at least one full and [top-up](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process) migration, from the production clone into the AEM as a Cloud Service non-production environment
* Resolve any potential issues like:
  * Disc space on the AEM source
  * Connectivity between the AEM source and AEM as a Cloud Service
  * Any [ingestion related limitations](#known-limitations)
Record the time taken for [extraction and ingestion](#gathering-data):
* Know how much content is added per week
* Extrapolate the times measured from the proof of migration to create a [migration plan](#migration-plan)

### Initial Migration {#initial-migration}

* Initiate the migration from production based on the experience you gained during the clone to AEM as a Cloud Service stage migration:
  * Author-Author
  * Publish-Publish
* Note: Aem as a Cloud Service author will be shown during ingestion but Aem as a Cloud Service publish will be up during ingestion
* Validate the content ingested into both the AEM as a Cloud Service author and publish tiers
* Instruct the content authoring team to avoid moving content on both source and destination until the ingestion is complete
* New content ca be added, edited or deleted but avoid moving it. This applies both to source of destination.
* Record the [time taken](#gathering-data) for full extraction and ingestion to have an estimate for future top up migration timelines
* Create a [migration planner](#migration-plan) for both author and publish

### Incremental Top Ups {#top-up}

* Gather data on the amount of content. For example: per one week, two weeks or a month.
* Make sure to plan top ups in such a way that you avoid more than 48 hours of content extraction and ingestion (so that it will fit into a weekend timeframe).
* Plan the number of top ups required and estimate/backtrack in relation to the go-live date.

## Identify Code and Content Freeze Timelines for the Migration {#code-content-freeze}

As mentioned previously you will eventually have to schedule a code and content freeze period. Consequently, the following questions may help you plan the freeze period better:

* How long do I have to freeze content authoring activities?
* For how long should I ask my delivery team to stop adding new features?

To answer the first question, you should take into consideration the time taken during trial runs in non-production environments. The second question is more complicated. To answer it you need close collaboration between the team who is adding new features and the team refactoring the code. The goal should be to make sure all the code that is added to the existing deployment is also added, tested, and deployed to the cloud services branch. Generally speaking, this means the amount of code freeze will be lower.

## Best Practices {#best-practices}

When planning or performing the migration you should consider the following guidelines:

* Migrate from Author to Author and Publish to Publish
* Request a production clone that can be used to:
  * Capture repository statistics
  * Proof of migration activities
  * Prepare the migration plan
  * Identify content freeze requirements
  * Identify any upsizing needs on Production when doing the migration from production

**Content Transfer Tool best practices**

You should run the Content Transfer Tool from a live production instead of a production clone. A good approach is to use [AZCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md) for the initial migration and then run top up extractions frequently (even daily) to extract smaller chunks and to avoid any long-term load on the source AEM.

You should avoid running the Content Transfer Tool from a production clone because:

* If a customer requires content versions to be migrated during top up migrations, then executing the Content Transfer Tool from a clone does not migrate the versions. Even if the clone is recreated from live author frequently, each time a clone is created the checkpoints that will be used by the Content Transfer Tool to calculate the differential will be reset.
* Since a production clone cannot be refreshed as a whole, ACL Query Package manager must be used to package and install the content being added or edited from live to clone. The problem with this approach is that any deleted content on the source instance will never get to the clone unless someone manually deletes the content from both source and clone. So, there is a possibility that the deleted content on live production will not be deleted on the clone and AEM as a Cloud Service.

**Optimizing the load on your AEM source while performing the content migration**

Remember, the load on the AEM source will be greater during the extraction phase. You should be aware that:

* The Content Transfer Tool is an external Java process that will use a JVM Heap of 4 GB.
* The non AzCopy version downloads binaries, stores them on a temporary space on the source AEM author (consuming disk I/O) then uploads into the Azure container which consumes network bandwidth.
* [AzCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md) transfers blobs directly from the blob store to the Azure container which saves disk I/O and network bandwidth. The AzCopy version still uses the disk and network bandwidth to extract and upload the data from the segment store into the Azure container.
* The Content Transfer Tool process is lighter on the system resources during the ingestion phase, since it only streams ingestion logs and there is not much load on the source instance with respect to disk I/O or network bandwidth.

## Known Limitations {#known-limitations}

You need to take into account that the entire ingestion fails if any of the following limitations are found as part of the extracted migration set:

* A JCR Node that has a name longer than 150 characters
* A JCR Node that is bigger than 16 MB
* Any User / Group with `rep:AuthorizableID` being ingested that is already present on AEM as a Cloud Service
* If any asset that is extracted and ingested moves into a different path either on source or destination before the next iteration of the migration.

## Asset Sanity {#asset-sanity}

Compared to the section above the ingestion **does not** fail due to the following asset concerns. However, it is highly recommended you take the appropriate steps in these scenarios:

* Any asset that has the original rendition missing
* Any folder that has a missing jcr:content node

Both of the above items will be identified and reported in [Best Practice Analyzer](/help/move-to-cloud-service/best-practices-analyzer/overview-best-practices-analyzer.md) report.

## Go-Live Checklist {#Go-Live-Checklist}

Please review the list of activities presented below to ensure that you can perform a smooth and successful migration:

* Schedule a code and content freeze period. See also [Code and Content Freeze Timelines for the Migration](#code-content-freeze).
* Perform the final content top-up
* Complete testing iterations
* Run performance and security tests
* Cut-Over and perform the migration on the production instance

You can always reference the list in case you need to re-calibrate your tasks while performing the migration.

## What's Next {#what-is-next}

Once you understand how to perform the migration to AEM as a Cloud Service, you can check the [Post-Go-Live](/help/journey-migration/post-go-live.md) page to keep your instance running smoothly.

<!--# Go Live {#golive-migration}
>exl-id: cf19d29f-3249-49d4-af02-bf68e247a8e9
>[!CONTEXTUALHELP]
>id="aemcloud_golive_prep"
>title="Go-Live Preparation"
>abstract="To ensure a smooth and successful go-live on AEM as a Cloud Service, you should plan for code and content freeze periods, testing iterations, content top-ups, performance tests, security tests and more."

To ensure a smooth and successful go-live on AEM as a Cloud Service, you should consider executing the following steps:

* Schedule code and content freeze period
* Perform final content top-up
* Complete testing iterations
* Run performance and security tests
* Cut-Over-->
