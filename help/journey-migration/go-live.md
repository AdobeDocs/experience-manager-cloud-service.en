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
