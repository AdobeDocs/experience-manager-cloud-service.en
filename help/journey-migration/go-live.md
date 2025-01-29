---
title: Go-Live
description: Learn how to perform the migration once the code and the content are cloud ready
exl-id: 10ec0b04-6836-4e26-9d4c-306cf743224e
feature: Migration
role: Admin
---
# Go-Live {#go-live}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_prep"
>title="Go-Live Preparation"
>abstract="To ensure a smooth and successful go-live on AEM as a Cloud Service, you should plan for code and content freeze periods, testing iterations, content top-ups, performance tests, security tests and more."

In this part of the journey, you learn how to plan and perform the migration once both the code and the content are ready to be moved over to AEM as a Cloud Service. Also, you learn what are the best practices and known limitations when performing the migration.

## The Story So Far {#story-so-far}

In the previous phases of the journey:

* You learned how to get started with the move to AEM as a Cloud Service in the [Getting Started](/help/journey-migration/getting-started.md) page.
* Determined if your deployment is ready to be moved to the cloud by reading the [Readiness phase](/help/journey-migration/readiness.md)
* Familiarized yourself with the tools and process through which you can make your code and content cloud ready with the [Implementation phase](/help/journey-migration/implementation.md).

## Objective {#objective}

This document helps you understand how to perform the migration to AEM as a Cloud Service once you are familiar with the previous steps of the journey. You learn how to perform the initial production migration and the best practices to follow when migrating to AEM as a Cloud Service.

## Initial Production Migration {#initial-migration}

Before you can perform the production migration, follow the fitment and proof of migration steps outlined in the [Content migration strategy and timeline](/help/journey-migration/implementation.md##strategy-timeline) section of the [Implementation phase](/help/journey-migration/implementation.md).

* Initiate the migration from production based on the experience you gained during the AEM as a Cloud Service stage migration performed on clones:
  * Author-Author
  * Publish-Publish

* Validate the content ingested into both the AEM as a Cloud Service author and publish tiers.
* Instruct the content authoring team to avoid moving content on both source and destination until the ingestion is complete
* New content ca be added, edited, or deleted but avoid moving it. This applies both to source and destination.
* Record the [time taken](/help/journey-migration/implementation.md#gathering-data) for full extraction and ingestion to have an estimate for future top-up migration timelines.
* Create a [migration planner](/help/journey-migration/implementation.md#migration-plan) for both author and publish.

## Incremental Top-Ups {#top-up}

After the initial migration from production you must perform incremental top-ups to make sure your bring your content up to date on the cloud instance. Because of this, it is recommended you follow these best practices:

* Gather data on the amount of content. For example: per one week, two weeks or a month.
* Make sure to plan top-ups in such a way that you avoid more than 48 hours of content extraction and ingestion. This is recommended so that the content top-ups will fit into a weekend time frame.
* Plan the number of top ups required and use those estimates to plan around the Go-Live date.

## Identify Code and Content Freeze Timelines for the Migration {#code-content-freeze}

As mentioned previously, you will have to schedule a code and content freeze period. Use the following questions to help you plan the freeze period:

* How long do I have to freeze content authoring activities?
* For how long should I ask my delivery team to stop adding new features?

To answer the first question, you should consider the time it has taken to perform trial runs in non-production environments. To answer the second question, you need close collaboration between the team who is adding new features and the team refactoring the code. The goal is to make sure all the code that is added to the existing deployment is also added, tested, and deployed to the cloud services branch. Generally, it means that the amount of code freeze is lower. 

Also, you need to plan for a content freeze when the final content top-up is scheduled.

## Best Practices {#best-practices}

When planning or performing the migration, you should consider the following guidelines:

* Migrate from Author to Author and Publish to Publish
* Request a production clone that can be used to:
  * Capture repository statistics
  * Proof of migration activities
  * Prepare the migration plan
  * Identify content freeze requirements
  * Identify any upsizing needs on Production when doing the migration from production

**Content Transfer Tool best practices**

Make sure that when going live, you run the content migration on production instead of a clone. A good approach is to use [AZCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md) for the initial migration and then run top up extractions frequently (even daily) to extract smaller chunks and to avoid any long-term load on the source AEM.

When performing the production migration you should avoid running the Content Transfer Tool from a clone because:

* If a customer requires content versions to be migrated during top-up migrations, then executing the Content Transfer Tool from a clone does not migrate the versions. Even if the clone is recreated from live author frequently, each time a clone is created, the checkpoints that are used by the Content Transfer Tool to calculate the deltas are reset.
* Since a clone cannot be refreshed as a whole, the ACL Query package must be used to package and install the content being added or edited from production to clone. The problem with this approach is that any deleted content on the source instance will never get to the clone unless it is manually deleted from both source and clone. This introduces the possibility that the deleted content on production will not be deleted on the clone and AEM as a Cloud Service.

**Optimizing the load on your AEM source while performing the content migration**

Remember, the load on the AEM source is greater during the extraction phase. Be aware of the following:

* The Content Transfer Tool is an external Java process that uses a JVM Heap of 4 GB
* The non-AzCopy version downloads binaries, stores them on a temporary space on the source AEM author, consuming disk I/O, then uploads into the Azure container which consumes network bandwidth
* [AzCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md) transfers blobs directly from the blob store to the Azure container which saves disk I/O and network bandwidth. The AzCopy version still uses the disk and network bandwidth to extract and upload the data from the segment store into the Azure container
* The Content Transfer Tool process is lighter on the system resources during the ingestion phase, since it only streams ingestion logs and there is not much load on the source instance as far disk I/O or network bandwidth are concerned.

## Known Limitations {#known-limitations}

Take into account that the entire ingestion fails if any of the following limitations are found as part of the extracted migration set:

* A JCR Node that has a name longer than 150 characters
* A JCR Node that is larger than 16 MB
* If any asset that is extracted and ingested moves into a different path either on source or destination before the next iteration of the migration.

## Asset Health {#asset-health}

Compared to the section above the ingestion **does not** fail due to the following asset concerns. However, it is highly recommended you take the appropriate steps in these scenarios:

* Any asset that has the original rendition missing
* Any folder that has a missing `jcr:content` node.

Both of the above items are identified and reported in the [Best Practice Analyzer](/help/journey-migration/best-practices-analyzer/overview-best-practices-analyzer.md) report.

## Go-Live Checklist {#Go-Live-Checklist}

For more information, consult the [Go-Live Checklist](/help/journey-onboarding/go-live-checklist.md) documentation.

## What's Next {#what-is-next}

Once you understand how to perform the migration to AEM as a Cloud Service, you can check the [Post-Go-Live](/help/journey-migration/post-go-live.md) page to keep your instance running smoothly.
