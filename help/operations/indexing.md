---
title: Indexing
description: Indexing 
---

# Indexing {#indexing}

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

The version of the index that is used is configured using flags in the index definitions via the `useIfExist` flag. An index may be used in only one version of the application (for example only blue or only green), or in both versions. Detailed documentation is available at [Index Management using Blue-Green Deployments](#index-management-using-blue-green-deployments).

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

which then needs to go under `ui.content/src/main/content/jcr_root`. Sub root folders are not supported as of now.

<!-- need to review and link info on naming convention from https://wiki.corp.adobe.com/display/WEM/Merging+Customer+and+OOTB+Index+Changes?focusedCommentId=1784917629#comment-1784917629 -->

The package from the above sample is built as `com.adobe.granite:new-index-content:zip:1.0.0-SNAPSHOT`.

### Deploying Index Definitions {#deploying-index-definitions}

Index definitions are now marked as custom and versioned:

* The index definition itself (for example `/oak:index/ntBaseLucene-custom-1`)  which is MUTABLE content

Therefore, in order to deploy an index, the index definition (`/oak:index/definitionname`) should be delivered via the **mutable package**, typically `ui.content` via Git and the Cloud Manager deployment process.

Once the new index definition is added, the new application needs to be deployed via Cloud Manager. Upon deployment two jobs are started, responsible for adding (and merging if needed) the index definitions to MongoDB and Azure Segment Store for author and publish, respectively. The underlying repositories are being reindexed with the new index definitions, before the Blue-Green switch is taking place.

<!-- ## Index Management using Blue-Green Deployments {#index-management-using-blue-green-deployments}

### What is Index Management {#what-is-index-management}

Index management is about adding, removing, and changing indexes. Changing the *definition* of an index is fast, but applying the change (often called "building an index", or, for existing indexes, "reindexing") requires time. It is not instantaneous: the repository has to be scanned for data to be indexed. 

>[!NOTE]
> Query lookups and updating an indexes are not considered index management.

### What is Blue-Green Deployment {#what-is-blue-green-deployment}

Blue-Green deployment can reduce downtime (it allows for zero downtime upgrades) and provides fast rollbacks. The old version of the application (blue) runs at the same time as the new version of the application (green).

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

With blue-green deployments, there is no downtime. However, for index management, this requires that indexes are only used by certain versions of the application. For example, when adding an index in version 2 of the application, we don't want it to be used by version 1 of the application yet. The reverse is the case when an index is removed: an index removed in version 2 is still needed in version 1. When changing an index definition, we want the old version of the index only to be used for version 1, and the new version of the index only to be used for version 2.

The following table shows 5 index definitions: 

* index "a" is used in both versions; 
* index "b" only in version 2; 
* index "c" only in version 1; 
* index "d" was changed in version 2, so that we have a new index "d_v2".

>[!NOTE]
>Please note that "_v2" is a naming convention only.

| Index  | Use in Version 1  | Use in Version 2  |
|---|---|---|
| /oak:index/a  | Yes  | Yes  |
| /oak:index/b  | No  | Yes  |
| /oak:index/c  | Yes  | No  |
|  /oak:index/d | Yes  | No  |
|  /oak:index/d_v2 | No  | Yes  |

To mark which indexes to use in specific versions of the application, we use markers in the read-only area of the repository, as follows. Remember the read-only area of the repository can be different in each version:

| Node  | Version 1  | Version 2  |
|---|---|---|
| /libs/indexes/a  | v1 = true  | v1 = true  |
| /libs/indexes/b  | node missing  | v1 = true  |
| /libs/indexes/c  | v1 = true  | node missing  |
| /libs/indexes/d  | v1 = true  | v2 = true  |

The indexes themselves then contain pointers to the following flags:

| Index  | "useIfExists" property value  |
|---|---|
| /oak:index/a  | /libs/indexes/a/@v1  |
| /oak:index/b  | /libs/indexes/b/@v1  |
| /oak:index/c  | /libs/indexes/c/@v1  |
| /oak:index/d  | /libs/indexes/d/@v1  |
| /oak:index/d_v2 | /libs/indexes/d/@v2  |

Here again, the node names "/libs/indexes/a" and property names "v1" and "v2"  are naming conventions. Do ensure the conventions are followed, as in future versions the conventions might be enforced.

We recommend that the version number is incremented each time the index is changed. The very first version of an index does not need to include the version number in the index node name. It is possible to re-use index names if it is guaranteed that no version of AEM is running that points to the old index.

To avoid that customer index names collide with index names of the product itself, please use the prefix "custom_" for customer indexes, or another prefix as appropriate.

### Limitations {#limitations}

Index management is currently only supported for indexes of type `lucene`.

### Removing an Index {#removing-an-index}

To configure the index "acme" to be used in the application, the index needs to be configured as follows:

`/oak:index/acme/@useIfExists = "/libs/indexes/acme/@v1"`

This ensures the index is only used if the property `/libs/indexes/acme/v1` exists. Therefore, this property also needs to be created in the read-only area, as follows:

`/libs/indexes/acme/@v1`

If the index is to be removed in a later version of the application, the node `/libs/indexes/acme` can be removed from the read-only area of the repository.

Once this new version of the application is deployed, the index is still updated. However, it is not used for queries in the new version of the application. Once no instances of the old application are running, the index shown below can be safely removed:

`/oak:index/acme/`

### Adding an Index {#adding-an-index}

To add an index named "acmeNew" to be used in a new version of the application and later, the index needs to be configured as follows:

`/oak:index/acmeNew/@useIfExists = "/libs/indexes/acmeNew/@v1"`

As above, this ensures the index is only used if the property `/libs/indexes/acmeNew/v1` exists. We assume the old version of the application will not have that node `/` property.

However, a new version of the application needs to have the following node and property, in order for the index to be used:

`/libs/indexes/acmeNew/@v1`

### Changing an Index {#changing-an-index}

When an existing index is changed, a new index needs to be added with the changed index definition. For example, let's say the existing index "acme" is changed. The old index is stored under `/oak:index/acme`, and the new index is stored under `/oak:index/acme_v2`. The respective `useIfExists` flags are set as follows:

`/oak:index/acme/@useIfExists = "/libs/indexes/acme/@v1"`

`/oak:index/acme_v2/@useIfExists = "/libs/indexes/acme/@v2"`

The old version of the application uses the following configuration:

`/libs/indexes/acme/@v1`

The new version of the application uses the following (changed) configuration:

`/libs/indexes/acme/@v2`


ABOVE SHOULD BE REPLACED WITH INFO FROM https://wiki.corp.adobe.com/pages/viewpage.action?pageId=1638127306 -->