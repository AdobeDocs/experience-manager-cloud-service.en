---
title: Content Search and Indexing
description: Content Search and Indexing
---

# Content Search and Indexing {#indexing}

## Changes in AEM as a Cloud Service {#changes-in-aem-as-a-cloud-service}

With AEM as a Cloud Service, Adobe is moving away from an AEM instance centric model to a service based view with n-x AEM Containers, driven by CI/CD pipelines in the Cloud Manager. Instead of configuring and maintaining Indexes on single AEM instances, the Index configuration has to be specified before a deployment. Configuration changes in production are clearly breaking CI/CD policies. The same holds true for index changes since it can impact system stability and performance if not specified tested and re-indexed before bringing them into production.

Below is a list of the main changes compared to AEM 6.5 and earlier versions:

1. Users will not have access to the Index Manager of a single AEM Instance to debug, configure or maintain indexing anymore. It is only used for local development and on-prem deployments.

1. Users will not change Indexes on a single AEM Instance nor will they have to worry about consistency checks or reindexing anymore.

1. In general, index changes are initiated before going to production in order to not circumvent quality gateways in the Cloud Manager CI/CD pipelines and not impact Business KPIs in production.

1. All related metrics including search performance in production will be available for customers at runtime in order to provide the holistic view on the topics of Search and Indexing.

1. Customers will be able to set up alerts according to their needs.

1. SREs are monitoring system health 24/7 and will take action as needed and as early as possible.

1. Index configuration is changed via deployments. Index definition changes are configured like other content changes.

1. At a high level on AEM as a Cloud Service, with the introduction of the [Blue-Green deployment model](#index-management-using-blue-green-deployments) two sets of indexes will exist: one set for the old version (blue), and one set for the new version (green).

<!-- The version of the index that is used is configured using flags in the index definitions via the `useIfExist` flag. An index may be used in only one version of the application (for example only blue or only green), or in both versions. Detailed documentation is available at [Index Management using Blue-Green Deployments](#index-management-using-blue-green-deployments). -->

1. Customers can see whether the indexing job is complete on the Cloud Manager build page and will receive a notification when the new version is ready to take traffic.

1. Limitations: currently, index management on AEM as a Cloud Service is only supported for indexes of type lucene.

<!-- ## Sizing Considerations {#sizing-considerations}

AEM as a Cloud Service comes with a default capacity model to provide sufficient performance for average web applications. This "average" measure relates to the repository size and even more relevant to the indexing size. If we have reasons to believe that we need extended capacity for a specific customer project, an evaluation with SREs and Engineering will take place to determine the required capacity settings.

AS NOTE: the above is internal for now.

-->

## How to Use {#how-to-use}

Defining indexes can comprise of the 3 use cases:

1. Adding a new customer index definition
1. Updating an existing index definition. This effectively means adding a new version of an existing index definition
1. Removing an existing index that is redundant or obsolete.

For both points 1 and 2 above, you need to create a new index definition as part of your custom code base in the respective Cloud Manager release schedule. For more information, see the [Deploying to AEM as a Cloud Service documentation](/help/implementing/deploying/overview.md).

### Preparing the New Index Defition {#preparing-the-new-index-definition}

You need to prepare a new index definition package that contains the actual index definition, following this naming pattern:

`<indexName>[-<productVersion>]-custom-<customVersion>`

which then needs to go under `ui.apps/src/main/content/jcr_root`. Sub root folders are not supported as of now.

<!-- need to review and link info on naming convention from https://wiki.corp.adobe.com/display/WEM/Merging+Customer+and+OOTB+Index+Changes?focusedCommentId=1784917629#comment-1784917629 -->

The package from the above sample is built as `com.adobe.granite:new-index-content:zip:1.0.0-SNAPSHOT`.

### Deploying Index Definitions {#deploying-index-definitions}

>[!NOTE]
>
> There is a known issue with Jackrabbit Filevault Maven Package Plugin version **1.1.0** which does not allow you to add `oak:index` to modules of `<packageType>application</packageType>`. To work around this, please use version **1.0.4**.

Index definitions are now marked as custom and versioned:

* The index definition itself (for example `/oak:index/ntBaseLucene-custom-1`)

Therefore, in order to deploy an index, the index definition (`/oak:index/definitionname`) needs to be delivered via `ui.apps` via Git and the Cloud Manager deployment process.

Once the new index definition is added, the new application needs to be deployed via Cloud Manager. Upon deployment two jobs are started, responsible for adding (and merging if needed) the index definitions to MongoDB and Azure Segment Store for author and publish, respectively. The underlying repositories are being reindexed with the new index definitions, before the Blue-Green switch is taking place.

## Index Management using Blue-Green Deployments {#index-management-using-blue-green-deployments}

### What is Index Management {#what-is-index-management}

Index management is about adding, removing, and changing indexes. Changing the *definition* of an index is fast, but applying the change (often called "building an index", or, for existing indexes, "reindexing") requires time. It is not instantaneous: the repository has to be scanned for data to be indexed.

### What is Blue-Green Deployment {#what-is-blue-green-deployment}

Blue-Green deployment can reduce downtime. It also allows for zero downtime upgrades and provides fast rollbacks. The old version of the application (blue) runs at the same time as the new version of the application (green).

### Read-Only and Read-Write Areas {#read-only-and-read-write-areas}

Certain areas of the repository (read-only parts of the repository) can be different in the old (blue) and in the new (green) version of the application. The read-only areas of the repository are typically "`/app`" and "`/libs`". In the following example, italic is used to mark read-only areas, while bold is used for read-write areas.

* **/**
* */apps (read-only)*
* **/content**
* */libs (read-only)*
* **/oak:index**
* **/oak:index/acme**
* **/jcr:system**
* **/system**
* **/var**

The read-write areas of the repository are shared between all versions of the application, while for each version of the application, there is a specific set of `/apps` and `/libs`.

### Index Management Without Blue-Green Deployment {#index-management-without-blue-green-deployment}

During development, or when using on premise installations, indexes can be added, removed, or changed at runtime. Indexes are used as soon as they are available. If an index is not supposed to be used in the old version of the application yet, then the index is typically built during a scheduled downtime. The same occurs when removing an index, or changing an existing index. When removing an index, it becomes unavailable as soon as it is removed.

### Index Management With Blue-Green Deployment {#index-management-with-blue-green-deployment}

With blue-green deployments, there is no downtime. However, for index management, this requires that indexes are only used by certain versions of the application. For example, when adding an index in version 2 of the application, you would not want it to be used by version 1 of the application yet. The reverse is the case when an index is removed: an index removed in version 2 is still needed in version 1. When changing an index definition, we want the old version of the index only to be used for version 1, and the new version of the index only to be used for version 2.

The following table shows 5 index definitions: index `cqPageLucene` is used in both versions while index `damAssetLucene-custom-1` is used only in version 2.

>[!NOTE]
>
> `<indexName>-custom-<customerVersionNumber>` is needed for AEM as a Cloud Service to mark this as a replacement for an existing index.

| Index | Out-of-the-box Index  | Use in Version 1  | Use in Version 2  |
|---|---|---|---|
| /oak:index/damAssetLucene  | Yes  | Yes  | No  |
| /oak:index/damAssetLucene-custom-1  | Yes (customized)  | No  | Yes  |
| /oak:index/acmeProduct-custom-1  | No  | Yes  | No  |
| /oak:index/acmeProduct-custom-2  | No  | No  | Yes  |
| /oak:index/cqPageLucene  | Yes  | Yes  | Yes  |

The version number is incremented each time the index is changed. In order to avoid custom index names colliding with index names of the product itself, custom indexes, as well as changes to out of the box indexes need to end with `-custom-<number>`.

### Changes to Out-of-the-Box Indexes {#changes-to-out-of-the-box-indexes}

Once Adobe changes an out-of-the-box index like "damAssetLucene" or "cqPageLucene", a new index named `damAssetLucene-2` or `cqPageLucene-2` is created, or, if the index was already customized, the customized index definition is merged with the changes in the out-of-the-box index, as shown below. Merging of changes happens automatically. That means that you do not need to do anything if an out-of-the-box index changes. However, it is possible to customize the index again later.

| Index  | Out-of-the-box Index  | Use in Version 2  | Use in Version 3  |
|---|---|---|---|
| /oak:index/damAssetLucene-custom-1  | Yes (customized)  | Yes  | No  |
| /oak:index/damAssetLucene-2-custom-1  | Yes (automatically merged from damAssetLucene-custom-1 and damAssetLucene-2)  | No  | Yes  |
| /oak:index/cqPageLucene  | Yes  | Yes  | No  |
| /oak:index/cqPageLucene-2  | Yes  | No  | Yes  |

### Limitations {#limitations}

Index management is currently only supported for indexes of type `lucene`.

### Removing an Index {#removing-an-index}

If an index is to be removed in a later version of the application, you can define an empty index (an index with no data to index), with a new name. For example purposes, you can name it `/oak:index/acmeProduct-custom-3`. This replaces the index `/oak:index/acmeProduct-custom-2`. Once `/oak:index/acmeProduct-custom-2` is removed by the system, the empty index `/oak:index/acmeProduct-custom-3` can then also be removed.

### Adding an Index {#adding-an-index}

To add an index named "/oak:index/acmeProduct-custom-1" to be used in a new version of the application and later, the index needs to be configured as follows:

`/oak:index/acmeProduct-custom-1`

As above, this ensures the index is only used by the new version of the application.

### Changing an Index {#changing-an-index}

When an existing index is changed, a new index needs to be added with the changed index definition. For example, consider the existing index "/oak:index/acmeProduct-custom-1" is changed. The old index is stored under `/oak:index/acmeProduct-custom-1`, and the new index is stored under `/oak:index/acmeProduct-custom-2`.

The old version of the application uses the following configuration:

`/oak:index/acmeProduct-custom-1`

The new version of the application uses the following (changed) configuration:

`/oak:index/acmeProduct-custom-2`