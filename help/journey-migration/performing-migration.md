---
title: Performing the Migration
description: Learn how to perform the migration once the code and the content are cloud ready
---

# Performing the Migration {#performing-migration}

In this part of the journey, you will learn how to plan and perform the migration once the code and the content are ready to be moved over to AEM as a Cloud Service. Additionally, you will also learn what are the best practices and known limitations when performing the migration.

## The Story So Far {#story-so-far}

In the previous steps of the journey:

* You learned how to get started with [the move to AEM as a Cloud Service](/help/journey-migration/getting-started.md)
* [Determined if your deployment is ready to be moved to the cloud](/help/journey-migration/readiness.md)
* As well as [the tools through which you can make your code and content cloud ready](/help/journey-migration/making-your-code-and-content-cloud-ready.md).

## Objective {#objective}

This document will help you understand how to perform the migration to AEM as a Cloud Service once you are familiar with the previous steps of the journey. You will learn how to gather data, create a migration plan, as well as the best practices to follow when migrating to AEM as a Cloud Service.

## Content migration strategy and timeline {#strategy-timeline}

The following diagram shows the important steps and associated tasks that can be used to formulate a content migration strategy and timeline.

![image](/help/journey-migration/assets/content-migration.png)

## Gathering Data {#gathering-data}

Gathering data can help you plan the migration activities and associated tasks. The extraction and ingestion times are particularly useful because the datapoints can be associated with a specific size of the migration set. As such, these datapoints can be extrapolated to come up with a plan:

* Total amount of time taken for [extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md)
* Total amount of time taken for [ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md)
* Total amount of time taken for top up [extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process)
* Total amount of time taken for top up [ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process)

One more important datapoint is the amount of time it takes to complete the [user mapping](/help/journey-migration/content-transfer-tool/user-mapping-tool/overview-user-mapping-tool.md) (if this is coupled with the content migration). You can take this data point into consideration for more realistic estimates, since it will be added to the overall extraction timeline and it may not be required to run it during top-ups.

These datapoints can also help you [Establish KPI's](/help/journey-migration/readiness.md#establish-kpis) and other migration related tasks.

## Migration plan {#migration-plan}

Based on the datapoints you gathered (see above), you can create a migration plan that can be integrated into a macro project plan. This step will enable all the key stakeholders to visualize and plan around the migration activities.

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

## Migration Tracker {#migration-tracker}

You can use the migration tracker to note down the times for both the initial and top up runs. These datapoints will help you formulate realistic content freeze requirements before the final top up.

The tracker will also help you to:

* Identify any deviations from the planner that require adjustments in the plan or go-live timelines
* Provide a realistic status that can be used in all necessary communications
* Plan for initial or future top up migrations

The following table illustrates a functional migration tracker:

| Source (Env / Instance / URL) | Destination (Env / Instance / URL) | Migration Set Name, Type (Initial or Top up) | Migration Set Size (MB) | User Mapping (Yes / No) | Extraction Duration (Start, End, Time taken) | Ingestion Duration (Start, End, Time taken) | Issues / Resolutions / Details |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |

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

## Go-Live plan {#completing-the-migration}

Following these steps can help you complete the migration process and ensure that you can perform a smooth and succesful migration:

* Schedule a code and content freeze period
* Perform the final content top-up
* Complete testing iterations
* Run performance and security tests
* Cut-Over and perform the migration on the production instance

You can always reference the list above in case you need to re-calibrate your tasks while completing the migration.

## What's Next {#what-is-next}

Once you understand how to perform the migration to AEM as a Cloud Service, you can check the [Monitoring for issues and improving performance page](/help/journey-migration/monitor-and-improve.md) to keep your instance running smoothly.

## Additional Resources {#additional-resources}

TBD

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
