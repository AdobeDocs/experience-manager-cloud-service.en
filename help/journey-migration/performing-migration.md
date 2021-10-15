---
title: Performing the Migration
description: Learn how to perform the migration once the code and the content are cloud ready
---

# Performing the Migration {#performing-migration}

In this part of the journey, you will learn how to perform the migration once the code and the content are ready to be moved over to AEM as a Cloud Service.

## The Story So Far {#story-so-far}

In the previous steps of the journey, you learned how to [determine if your deployment is ready to be moved to the cloud](/help/journey-migration/readiness.md) as well as [the tools through which you can make your code and content cloud ready](/help/journey-migration/making-your-code-and-content-cloud-ready.md).

## Objective {#objective}

This document will help you understand how to complete the migration to AEM as a Cloud Service once you performed the previous steps of the journey.

## General guidelines {#completing-the-migration}

To ensure a smooth and successful migration to AEM as a Cloud Service, you should consider executing the following steps:

* Schedule code and content freeze period
* Perform final content top-up
* Complete testing iterations
* Run performance and security tests
* Cut-Over

## Content migration strategy and timeline {#stragtegy-timeline}

The following diagram shows the important steps and associated tasks that can be used to formulate a content migration strategy and timeline.

![image](/help/journey-migration/assets/content-migration.png)

## Gathering Data {#gathering-data}

The following datapoints can help you plan the migration activities/tasks:

* Total amount of time taken for extraction
* Total amount of time taken for ingestion
* Total amount of time taken for Top up extraction
* Total amount of time taken for Top up ingestion

As the set of (extraction, ingestion) times are associated with a specific size of migration set, these data points could be extrapolated to come up with a plan.

One more important data point to gather is:

The amount of time that it takes to complete the user mapping ( if this is coupled with content migration)(link tbd). It is worth taking it into consideration for more realistic estimates, since this time will be added to the overall extraction timeline and it may not be required to run it during top-ups.

## Migration plan {#migration-plan}

Based on the datapoints you gathered (see above) , you can create a migration plan that can be integrated into macro project plan. This step will enable all the key stakeholders to visualize and plan around the migration activities.

Some important details that will influence the migration plan:

**Total Number of Extractions required**

* Author and Publish extractions in specific environments are considered as two parallel extractions as they are independent of each other
* Number of Top Up extractions based on repository growth in specific time periods

**Total Number of Ingestions required**

* It is important to capture this item into plan, as an extracted set can be ingested into multiple Cloud Service environments.
* Number of Top up ingestions
* Migrating content from the Source Author to the Cloud service Author instance and from the Source Publish to Cloud Service Publish is the best practice to avoid ingesting all the Author content into the Cloud Service Publish

For example:

| Migration Iteration | Start Date | Estimated End Date | Dependencies | Estimated Duration (in days) | Additional Details / Action Items |
|---|---|---|---|---|---|
| PRDCLONE-AUTHOR-INITIAL-USRMAP-CSSTAGE-AUTHOR |   |   |   |   |   |
| PRDCLONE-PUBLISH-TOPUP-CSSTAGE-AUTHOR |   |   |   |   |   |

It would be helpful to follow a specific naming format to identify the migration iterations as shown above, including: Source AEM Environment, AEMaaCS Environment, AEMaaCS Instance.

## Migration Tracker {#migration-tracker}

You can use a migration tracker to note down the times taken for both the initial and top up runs. These data points will help formulate realistic content freeze requirements before the final top up.

The tracker will help to:

* Identify any deviations from the planner that requires adjustments in the plan or go-live timelines
* Provide a more realistic status that can be used in all necessary communications
* Plan for future top up or initial migrations

For example:

| Source (Env / Instance / URL) | Destination (Env / Instance / URL) | Migration Set Name, Type (Initial or Top up) | Migration Set Size (MB) | User Mapping (Yes / No) | Extraction Duration (Start, End, Time taken) | Ingestion Duration (Start, End, Time taken) | Issues / Resolutions / Details |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |

## Best Practices {#best-practices}

* Migrate from Author to Author and Publish to Publish
* Request a production clone that can be used to:
  * Capture repository statistics
  * Proof of migration activities
  * Prepare the migration plan
  * Identify content freeze requirements
  * Identify any upsizing needs on Production when doing the migration from production

Be careful when running the content transfer tool (CTT) from a production clone because:
* If a customer requires content versions to be migrated during top up migrations, then executing CTT from a clone does not work. Even if the clone is recreated from live author frequently, each time a clone is created the checkpoints that will be used by CTT to calculate the differential will be reset.
* Since a production clone can't be refreshed as a whole, ACL Query Package manager must be used to package & install the content being added / edited from Live to Clone. The problem with this approach is that any deletes that happen on the source instance will never get to the clone unless someone manually deletes them from both source and clone. So, there is a possibility that the deleted content on live production will not be deleted on the clone and AEMaaCS.

Running CTT from a live production will overcome the above limitations. A good approach is to use AZCopy for the initial migration and then run top up extractions frequently (even daily) to extract smaller chunks and to avoid any long-term load on the source AEM.

The load on the AEM source will be greater during the extraction phase:
* The content transfer tool is an external Java process that will use a JVM Heap of 4gb
* The non AzCopy version downloads binaries, stores them on temp space on the source AEM author (disk I/O) then uploads into the Azure container (network bandwidth).
* AzCopy transfers blobs directly from the blob store to the Azure container which saves disk I/O and network bandwidth. The AzCopy version still uses the disk and network bandwidth to extract and upload the data from segment store into the Azure container.
* During the ingestion phase the CTT process just streams ingestion logs and there is not much load on the source instance with respect to disk I/O or network bandwidth.

## Known Limitations {#known-limitations}

The entire ingestion fails if any one of these limitations are found as part of the extracted migration set:
* A JCR Node that has a name longer than 150 characters
* A JCR Node that is bigger than 16 MB
* Any User / Group with `rep:AuthorizableID` being ingested that is already present on AEMaaCS
* If any asset which is extracted and ingested moves into a different path either on source or destination before the next iteration of migration

## What's Next {#what-is-next}

Once you understand how to complete the migration to AEM as a Cloud Service, you can check the [Monitoring for issues and improving performance page](/help/journey-migration/monitor-and-improve.md) to keep your instance running smoothly.

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
