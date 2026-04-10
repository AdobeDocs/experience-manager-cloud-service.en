---
title: Content Search and Indexing
description: Learn about Content Search and Indexing in AEM as a Cloud Service.
exl-id: 4fe5375c-1c84-44e7-9f78-1ac18fc6ea6b
feature: Operations
role: Admin
---
# Content Search and Indexing {#indexing}

## Changes in AEM as a Cloud Service {#changes-in-aem-as-a-cloud-service}

With AEM as a Cloud Service, Adobe is moving away from an AEM instance-centric model to a service-based view with n-x AEM Containers, driven by CI/CD pipelines in the Cloud Manager. Instead of configuring and maintaining indexes on single AEM instances, the index configuration has to be specified before a deployment. Configuration changes in production are breaking CI/CD policies. The same holds true for index changes, since it can impact system stability and performance if not specified, tested, and reindexed before bringing them into production.

Below is a list of the main changes compared to AEM 6.5 and earlier versions:

1. Users do not have access to the Index Manager of a single AEM instance to debug, configure, or maintain indexing anymore. It is only used for local development and on-prem deployments.
1. Users do not change indexes on a single AEM instance nor do they have to worry about consistency checks or reindexing anymore.
1. In general, index changes are initiated before going to production to not circumvent quality gateways in the Cloud Manager CI/CD pipelines and not impact business KPIs in production.
1. All related metrics, including search performance in production, are available for customers at runtime to provide the holistic view on the topics of search and indexing.
1. Customers are able to set up alerts according to their needs.
1. SREs are monitoring system health 24/7 and action is taken as early as possible.
1. Index configuration is changed via deployments. Index definition changes are configured like other content changes.
1. At a high level on AEM as a Cloud Service, with the introduction of the [rolling deployment model](#index-management-using-rolling-deployments), two sets of indexes exist: one for the old version, and one for the new version.
1. Customers can see whether the indexing job is complete on the Cloud Manager build page and receive a notification when the new version is ready to take traffic.

Limitations:

* Currently, index management on AEM as a Cloud Service is only supported for indexes of type `lucene`. This means that all index customizations must be of type `lucene`. The `async` property can only be one of the following: `[async]`, `[async,nrt]` or `[fulltext-async]`.
* Internally, other indexes might be configured and used for queries. For example, queries that are written against the `damAssetLucene` index might, on AEM as a Cloud Service, in fact be executed against an Elasticsearch version of this index. This difference is  not visible to the user. However, certain tools such as the `explain` feature report a different index. For differences between Lucene indexes and Elastic indexes, see [the Elastic documentation in Apache Jackrabbit Oak](https://jackrabbit.apache.org/oak/docs/query/elastic.html). Customers do not need to, and cannot, configure Elasticsearch indexes directly.
* Only standard analyzers are supported (that is, those analyzers that are shipped with the product). Custom analyzers are not supported.
* Search by similar feature vectors (`useInSimilarity = true`) is not supported.  

>[!TIP]
>
>For more details on the Oak indexing and queries, including a detailed description of advanced search and indexing features, see the [Apache Oak documentation](https://jackrabbit.apache.org/oak/docs/query/query.html).

## How to Use {#how-to-use}

Index definitions can be categorized into three primary use cases, as follows:

1. **Add** a new custom index definition.
2. **Update** an existing index definition by adding a new version. 
3. **Remove** an index definition that is no longer necessary.

For both points 1 and 2 above, you need to create an index definition as part of your custom code base in the respective Cloud Manager release schedule. For more information, see the [Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md) documentation.

If a change in the index configuration is needed, ensure that your configuration conforms to the guidelines provided in the [Project Configuration](#project-configuration) section. Make any necessary adaptations accordingly.

## Project Configuration

We strongly recommend using version >= `1.3.2` of the Jackrabbit `filevault-package-maven-plugin`. The steps to incorporate it into your project are as follows: 

1. If needed, update the version in the top-level `pom.xml`:

    ```xml
    <plugin>
        <groupId>org.apache.jackrabbit</groupId>
            <artifactId>filevault-package-maven-plugin</artifactId>
            ...
            <version>1.3.2</version>
        ...
    </plugin>
    ```

2. Add the following to the top-level `pom.xml`:

    ```xml
    <jackrabbit-packagetype>
        <options>   
            <immutableRootNodeNames>apps,libs,oak:index</immutableRootNodeNames>
        </options>
    </jackrabbit-packagetype>
    ```

    Here is a sample of the project's top-level `pom.xml` file with the aforementioned configurations included:

    Filename: `pom.xml`

    ```xml
    <plugin>
        <groupId>org.apache.jackrabbit</groupId>
            <artifactId>filevault-package-maven-plugin</artifactId>
            ...
            <version>1.3.2</version>
            <configuration>
                ...
                <validatorsSettings>
                    <jackrabbit-packagetype>
                        <options>
                            <immutableRootNodeNames>apps,libs,oak:index</immutableRootNodeNames>
                        </options>
                    </jackrabbit-packagetype>
                    ...
                ...
    </plugin>
    ```

3. In `ui.apps/pom.xml` and `ui.apps.structure/pom.xml`, it is necessary to enable the `allowIndexDefinitions` and `noIntermediateSaves` options in the `filevault-package-maven-plugin`. Enabling `allowIndexDefinitions` allows for custom index definitions, while `noIntermediateSaves` ensures that the configurations are added atomically. 

    Filenames: `ui.apps/pom.xml` and `ui.apps.structure/pom.xml`

    ```xml
    <plugin>
        <groupId>org.apache.jackrabbit</groupId>
            <artifactId>filevault-package-maven-plugin</artifactId>
            <configuration>
                <allowIndexDefinitions>true</allowIndexDefinitions>
                <properties>
                    <cloudManagerTarget>none</cloudManagerTarget>
                    <noIntermediateSaves>true</noIntermediateSaves>
                </properties>
        ...
    </plugin>
    ```

4. Add a filter for `/oak:index` in `ui.apps.structure/pom.xml`:

    ```xml
    <filters>
        ...
        <filter><root>/oak:index</root></filter>
    </filters>
    ```

>[!TIP]
>
>For more details on the required package structure for AEM as a Cloud Service, see [AEM Project Structure](/help/implementing/developing/introduction/aem-project-content-package-structure.md).

## Simplified Index Management using the Diff Index

Most AEM indexes can be configured using Simplified Index Management.
This provides a simple way to customize out-of-the-box (OOTB) indexes and to define custom indexes using one JSON file.

>[!TIP]
>
>There is an online tool that helps configuring AEM indexes: [Oak Indexing Tools](https://oak-indexing.github.io/oakTools/index.html). It has [a section on Simplified Index Management](https://oak-indexing.github.io/oakTools/simplified.html) with a step-by-step guide and additional tools to help converting custom index to this new format.

Limitations: Simplified Index Management is not currently available for indexes that include `/apps`, `/libs`.
It can be used for all indexes that have an `includedPaths` property of e.g. `/content`.
For indexes without an `includedPaths` property, or where `includedPaths` contains `/apps` or `/libs`,
consider changing the query or using the Legacy Index Configurations mode below.

Simplified Index Management is able to customize existing out-of-the-box (OOTB) indexes and add fully custom indexes.
With Simplified Index Management, there is no need to copy definitions or define versions explicitly.
Index definition customizations are automatically merged with the latest out-of-the-box index,
and a new index version is created when needed.

For most indexes, custom indexes and customizations to existing indexes can be created using a `diff.index` package.
To configure such an index, use the following step-by-step guide.
The following example customizes the `damAssetLucene` index
and introduces a fully custom index at the same time.
The process is as follows:

1. Create a new folder in the `ui.apps` directory named `ui.apps/src/main/content/jcr_root/_oak_index/diff.index`.

2. Add a configuration file `.content.xml` (this is a required placeholder configuration, not a regular index definition) with the following content: `ui.apps/src/main/content/jcr_root/_oak_index/diff.index/.content.xml`

    ```xml
    <?xml version="1.0" encoding="UTF-8"?><jcr:root
        xmlns:jcr="http://www.jcp.org/jcr/1.0"
        xmlns:nt="http://www.jcp.org/jcr/nt/1.0"
        jcr:primaryType="nt:unstructured"
        type="lucene" includedPaths="/same" queryPaths="/same" async="async">
    <diff.json jcr:primaryType="nt:file"/></jcr:root>
    ```

3. Add a text file `diff.json` with the following content.
   In this example, we customize the out-of-the-box index `damAssetLucene`
   to additionally index the property named `test`, and in addition to that,
   a fully custom index named `acme.testIndex` that indexes the property `testing` in `nt:unstructured` nodes:

    `ui.apps/src/main/content/jcr_root/_oak_index/diff.index/diff.json`

    ```json
    {
        "damAssetLucene": {
            "indexRules": {
                "dam:Asset": {
                    "properties": {
                        "test": {
                            "name": "test",
                            "propertyIndex": true
                        }
                    }
                }
            }
        },
        "acme.testIndex": {
            "async": [ "async" ],
            "compatVersion": 2,
            "evaluatePathRestrictions": true,
            "includedPaths": [ "/content" ],
            "queryPaths": [ "/content" ],
            "selectionPolicy": "tag",
            "tags": [ "testing" ],
            "type": "lucene",
            "indexRules": {
                "nt:unstructured": {
                    "properties": {
                        "testing": {
                            "name": "testing",
                            "propertyIndex": true
                        }
                    }
                }
            }
        }
    }
    ```

4. Add an entry to the FileVault filter in `ui.apps/src/main/content/META-INF/vault/filter.xml`:

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <workspaceFilter version="1.0">
        ...
        <filter root="/oak:index/diff.index"/> 
    </workspaceFilter>
    ```

After applying the changes, deploy the new application using Cloud Manager.
This deployment initiates two jobs, responsible for adding (and merging if necessary)
the index definitions for author and publish, respectively.
Prior to the switch, the underlying repositories undergo reindexing with the updated index definitions.

## Legacy Index Configurations

Indexes that cannot be configured using Simplified Index Management
need to use the legacy configuration mode.

The Legacy Index Configuration only applies for indexes that can not have an `includedPaths` property,
or that have a property which needs to covers `/apps`, `/libs`, or `/`.
There are some out-of-the-box indexes that do cover these paths, namely:

* `cqPageLucene`: If you need to customize this index,
  consider migrating your queries to use `cqPageContent` instead,
  which has an `includedPaths` of `/content`, and a tag.
* `ntBaseLucene`: Best practice is to avoid changing this index,
  and instead using a fully custom index with a prefix such as `acme.`,
  which covers only the required paths. 
  See the section Simplified Index Management for details.

## Index Names {#index-names}

An index definition can fall into one of the following categories:

1. Out-of-the-box (OOTB) index. These are predefined indexes provided by AEM. For instance: `/oak:index/cqPageLucene-2` or `/oak:index/damAssetLucene-8`.

2. Customization of an OOTB index. To customize an OOTB index, append `-custom-` followed by a number. For example, `/oak:index/damAssetLucene-8-custom-1` is the customization of the OOTB index `/oak:index/damAssetLucene-8`. A customization is typically a copy of the OOTB index, plus additional properties that need to be indexed.

3. Fully custom index: you can create an entirely new index from scratch. These indexes also need to end with `-custom-` and a version number. In addition, to avoid naming conflicts, use a prefix in the index name. For instance: `/oak:index/acme.product-1-custom-2`, where `acme.` is the prefix.

>[!NOTE]
>
>Introducing new indexes on the `dam:Asset` nodetype (particularly fulltext indexes) is strongly discouraged as these can conflict with OOTB product features, leading to functional and performance issues. Instead, the most appropriate way to index queries on the `dam:Asset` nodetype is to customize the `damAssetLucene-*` index, by adding the additional properties. These changes will automatically be merged into a new product version in subsequent releases. If in doubt, contact Adobe Support for advice.

## Preparing the New Index Definition {#preparing-the-new-index-definition}

>[!NOTE]
>
>When customizing an out-of-the-box index, for example, `damAssetLucene-8`, copy the latest out-of-the-box index definition from a *Cloud Service environment* using the CRX DE Package Manager (`/crx/packmgr/`) . Rename it to `damAssetLucene-8-custom-1` (or higher), and add your customizations inside the XML file. If the index in the cloud environment is of type `elasticsearch`, then additional changes are needed: change the `type` property to `lucene`, change the `async` property to `[async,nrt]`, and change the property `similarityTags` to `true`. This ensures that the required configurations are not being removed inadvertently. For example, the `tika` node under `/oak:index/damAssetLucene-8/tika` is required in the customized index deployed to an AEM Cloud Service environment but doesn't exist on the local AEM SDK.

For customizations of an OOTB index, prepare a new package that contains the customized or custom index definition. The index name needs to follow the naming pattern:

`<indexName>-<productVersion>-custom-<customVersion>`

For a fully customized index, prepare a new index definition package that contains the index definition that follows this naming pattern:

`<prefix>.<indexName>-<productVersion>-custom-<customVersion>`

As mentioned in the limitations sections, the `type` of the customized index definition must always be set to `lucene` even if the extracted index definition using Package Manager is of a different type (e.g. `elasticsearch`).
The `async` property must also be changed in case the extracted index definition is set to `elastic-async`. The `async` property must be set to one of the following: `[async]`, `[async,nrt]` or `[fulltext-async]` for the customized index definition.

<!--
 Alexandru: temporarily drafting this statement due to CQDOC-17701

The package from the above sample is built as `com.adobe.granite:new-index-content:zip:1.0.0-SNAPSHOT`.
-->

>[!NOTE]
>
>Any content package containing index definitions should have the following properties set in the `properties.xml` file of the content package. `properties.xml` is created by default in a new package, and located at `<package_name>/META-INF/vault/properties.xml`:
>
> * `noIntermediateSaves=true`
>
> * `allowIndexDefinitions=true`

## Deploying Custom Index Definitions {#deploying-custom-index-definitions}

To illustrate the deployment of a customized version of the out-of-the-box index `damAssetLucene-8`, we will provide a step-by-step guide. In this example, we will rename it to `damAssetLucene-8-custom-1`. Then the process is as follows:

1. Create a new folder with the updated index name in the `ui.apps` directory: 
    * Example: `ui.apps/src/main/content/jcr_root/_oak_index/damAssetLucene-8-custom-1/`

2. Add a configuration file `.content.xml` with the custom configurations inside the created folder. Below is an example of a customization:
    Filename: `ui.apps/src/main/content/jcr_root/_oak_index/damAssetLucene-8-custom-1/.content.xml`

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <jcr:root xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:dam="http://www.day.com/dam/1.0" xmlns:nt="http://www.jcp.org/jcr/nt/1.0" xmlns:oak="http://jackrabbit.apache.org/oak/ns/1.0" xmlns:rep="internal"
        jcr:mixinTypes="[rep:AccessControllable]"
        jcr:primaryType="oak:QueryIndexDefinition"
        async="[async,nrt]"
        compatVersion="{Long}2"
        evaluatePathRestrictions="{Boolean}true"
        includedPaths="[/content/dam]"
        maxFieldLength="{Long}100000"
        type="lucene">
        <facets
            jcr:primaryType="nt:unstructured"
            secure="statistical"
            topChildren="100"/>
        <indexRules jcr:primaryType="nt:unstructured">
            <dam:Asset jcr:primaryType="nt:unstructured">
                <properties jcr:primaryType="nt:unstructured">
                    <cqTags
                        jcr:primaryType="nt:unstructured"
                        name="jcr:content/metadata/cq:tags"
                        nodeScopeIndex="{Boolean}true"
                        propertyIndex="{Boolean}true"
                        useInSpellcheck="{Boolean}true"
                        useInSuggest="{Boolean}true"/>
                </properties>
            </dam:Asset>
        </indexRules>
        <tika jcr:primaryType="nt:folder">
            <config.xml jcr:primaryType="nt:file"/>
        </tika>
    </jcr:root>
    ```

3. Add an entry to the FileVault filter in `ui.apps/src/main/content/META-INF/vault/filter.xml`:

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <workspaceFilter version="1.0">
        ...
        <filter root="/oak:index/damAssetLucene-8-custom-1"/> 
    </workspaceFilter>
    ```

4. Add a configuration file for Apache Tika in: `ui.apps/src/main/content/jcr_root/_oak_index/damAssetLucene-8-custom-1/tika/config.xml`:

    ```xml
    <properties>
        <detectors>
            <detector class="org.apache.tika.detect.TypeDetector"/>
        </detectors>
        <parsers>
            <parser class="org.apache.tika.parser.DefaultParser">
            <mime>text/plain</mime>
            </parser>
        </parsers>
        <service-loader initializableProblemHandler="ignore" dynamic="true"/>
    </properties>
    ```

5. Ensure that your configuration conforms to the guidelines provided in the [Project Configuration](#project-configuration) section. Make any necessary adaptations accordingly.

## Index Management using Rolling Deployments {#index-management-using-rolling-deployments}

### What is Index Management {#what-is-index-management}

Index management is about adding, removing, and changing indexes. Changing the *definition* of an index is fast, but applying the change (often called "building an index", or, for existing indexes, "reindexing") requires time. It is not instantaneous: the repository must be scanned for data to be indexed.

### What are Rolling Deployments {#what-are-rolling-deployments}

A rolling deployment allows for zero downtime upgrades, and provides fast rollbacks. The old version of the application runs at the same time as the new version of the application.

### Read-Only and Read-Write Areas {#read-only-and-read-write-areas}

Certain areas of the repository (read-only parts of the repository) can be different in the old and in the new version of the application. The read-only areas of the repository are typically `/app` and `/libs`. In the following example, italic is used to mark read-only areas, while bold is used for read-write areas.

* **/**
* */apps (read-only)*
* **/content**
* */libs (read-only)*
* **/oak:index**
* **/oak:index/acme.**
* **/jcr:system**
* **/system**
* **/var**

The read-write areas of the repository are shared between all versions of the application, while for each version of the application, there is a specific set of `/apps` and `/libs`.

### Index Management Without Rolling Deployments {#index-management-without-rolling-deployments}

During development, or when using on-premise installations, indexes can be added, removed, or changed at runtime. Indexes are used when they are available. If an index is not yet used in the old version of the application, then the index is typically built during a scheduled downtime. The same occurs when removing an index, or changing an existing index. When removing an index, it becomes unavailable when it is removed.

### Index Management With Rolling Deployments {#index-management-with-rolling-deployments}

With rolling deployments, there is no downtime. For some time during an update, both the old version (for example, version 1) of the application, and the new version (version 2), run concurrently against the same repository. If version 1 requires a certain index to be available, then this index must not be removed in version 2. The index should be removed later, for example, in version 3, at which point it is guaranteed that version 1 of the application is no longer running. Also, applications should be written such that version 1 works well, even if version 2 is running, and if indexes of version 2 are available.

After upgrading to the new version is complete, old indexes can be garbage collected by the system. The old indexes typically stay for one week, to speed up rollbacks (if a rollback should be needed).

The following table shows five index definitions: index `cqPageLucene` is used in both versions while index `damAssetLucene-custom-1` is used only in version 2.

>[!NOTE]
>
>The `<indexName>-custom-<customerVersionNumber>` is needed for AEM as a Cloud Service to mark it as a replacement for an existing index.

| Index | Out-of-the-box Index  | Use in Version 1  | Use in Version 2  |
|---|---|---|---|
| /oak:index/damAssetLucene-8  | Yes  | Yes  | No  |
| /oak:index/damAssetLucene-8-custom-1  | Yes (customized)  | No  | Yes  |
| /oak:index/acme.product-1-custom-1  | No  | Yes  | No  |
| /oak:index/acme.product-1-custom-2  | No  | No  | Yes  |
| /oak:index/cqPageLucene-2  | Yes  | Yes  | Yes  |

The version number is incremented each time the index is changed. To avoid custom index names colliding with index names of the product itself, custom indexes, and changes to out-of-the-box indexes must end with `-custom-<number>`.

### Changes to Out-of-the-Box Indexes {#changes-to-out-of-the-box-indexes}

After Adobe changes an out-of-the-box index like `damAssetLucene` or `cqPageLucene`, a new index named `damAssetLucene-2` or `cqPageLucene-2` is created. Or, if the index was already customized, the customized index definition is merged with the changes in the out-of-the-box index, as shown below. Merging of changes happens automatically. That means you do not need to do anything if an out-of-the-box index changes. However, it is possible to customize the index again later. In this case, it is important to use the latest (merged) version as the baseline.

| Index  | Out-of-the-box Index  | Use in Version 2  | Use in Version 3  |
|---|---|---|---|
| /oak:index/damAssetLucene-1-custom-1  | Yes (customized)  | Yes  | No  |
| /oak:index/damAssetLucene-2-custom-1  | Yes (automatically merged from damAssetLucene-1-custom-1 and damAssetLucene-2)  | No  | Yes  |
| /oak:index/cqPageLucene-1  | Yes  | Yes  | No  |
| /oak:index/cqPageLucene-2  | Yes  | No  | Yes  |

It is important to note that environments might be on different AEM versions. For example: `dev` environment is on release `X+1` while stage and prod are still on release `X` and are waiting to be upgraded to release `X+1` after required tests on `dev` have been performed. If release `X+1` comes with a newer version of a product index that has been customized and a new customization of that index is required, then the following table will explain what versions need to be set on environments based on the AEM release:

| Environment (AEM Release Version) | Product index version | Existing custom index version | New custom index version   |
|-----------------------------------|-----------------------|-------------------------------|----------------------------|
| Dev (X+1)                         | damAssetLucene-11     | damAssetLucene-11-custom-1    | damAssetLucene-11-custom-2 |
| Stage (X)                         | damAssetLucene-10     | damAssetLucene-10-custom-1    | damAssetLucene-10-custom-2 |
| Prod (X)                          | damAssetLucene-10     | damAssetLucene-10-custom-1    | damAssetLucene-10-custom-2 |


### Current Limitations {#current-limitations}

Index management is only supported for indexes of type `lucene`, with `compatVersion` set to `2`. Internally, other indexes might be configured and used for queries, for example, Elasticsearch indexes. Queries that are written against the `damAssetLucene` index might, on AEM as a Cloud Service, in fact be run against an Elasticsearch version of this index. This difference is invisible to the application user, however certain tools such as the `explain` feature reports a different index. For differences between Lucene and Elasticsearch indexes, see [the Elasticsearch documentation in Apache Jackrabbit Oak](https://jackrabbit.apache.org/oak/docs/query/elastic.html). Customers cannot and do not need to configure Elasticsearch indexes directly.

Only built-in analyzers are supported (that is, those analyzers that are shipped with the product). Custom analyzers are not supported.

Currently, indexing the contents of `/oak:index` is not supported. 

For best operational performance, indexes should not be excessively large. The total size of all indexes can be used as a guide. If this size increases by more than 100% after custom indexes have been added, and standard indexes have been adjusted on a development environment, custom index definitions should be adjusted. AEM as a Cloud Service can prevent the deployment of, or remove indexes that would negatively impact system stability and performance.

### Adding an Index {#adding-an-index}

To add a fully custom index named `/oak:index/acme.product-1-custom-1`, to be used in a new version of the application and later, the index must be configured as follows:

`acme.product-1-custom-1`

This configuration works by prepending a custom identifier to the index name, followed by a dot (**`.`**). The identifier should be from 2 through 5 characters in length.

As above, this configuration ensures that the index is only used by the new version of the application.

### Changing an Index {#changing-an-index}

When an existing index is changed, a new index must be added with the changed index definition. For example, consider the existing index `/oak:index/acme.product-1-custom-1` is changed. The old index is stored under `/oak:index/acme.product-1-custom-1`, and the new index is stored under `/oak:index/acme.product-1-custom-2`.

The old version of the application uses the following configuration:

`/oak:index/acme.product-1-custom-1`

The new version of the application uses the following (changed) configuration:

`/oak:index/acme.product-1-custom-2`

>[!NOTE]
>
>Index definitions on AEM as a Cloud Service may not fully match the index definitions on a local development instance. The development instance does not have a Tika configuration, while instances of AEM as a Cloud Service do have one. If you customize an index with a Tika configuration, retain the Tika configuration.

### Undoing a Change {#undoing-a-change}

Sometimes, it is necessary to undo a modification in an index definition, for example due to an error or because the modification is no longer needed. For instance, if the index definition `damAssetLucene-8-custom-3` contains a mistake, you may want to revert to the previous definition, `damAssetLucene-8-custom-2`. To accomplish this, create a new index named `damAssetLucene-8-custom-4` that is a copy of the prior index, `damAssetLucene-8-custom-2`.

### Removing an Index {#removing-an-index}

The following only applies to customizations of out-of-the-box (OOTB) indexes and to fully custom indexes. Note that the original OOTB indexes cannot be removed, as they are used by AEM.

To ensure system integrity and stability, index definitions should be treated as immutable once deployed. If you need to remove a custom index or customization, create a new version of that index with a definition that effectively simulates the removal
(see the examples below).

Once a new version of an index is deployed, the older version of the same index will no longer be used by queries. 
The older version will not be immediately deleted from the environment,
but will become eligible for garbage collection by a clean-up mechanism that runs periodically. 
After a grace period designed to allow recovery in case of mistakes 
(currently, 7 days counting from when the indexing was removed, but subject to change),
this clean-up mechanism will delete the unused index data,
and will either disable or remove the old version of the index from the environment.

Below we describe the two possible cases: removing customizations of an OOTB index, and removing a fully custom index.

#### Removing Customizations of an Out-Of-The-Box Index

Follow the steps described in [Undoing a Change](#undoing-a-change-undoing-a-change) using the definitions of the OOTB index as the new version. For example, if you have already deployed `damAssetLucene-8-custom-3`, but no longer need the customizations and want to switch back to the default `damAssetLucene-8` index, then you need to add an index `damAssetLucene-8-custom-4` that contains the index definition of `damAssetLucene-8`.

#### Removing a Fully Custom Index

Follow the steps described in [Undoing a Change](#undoing-a-change-undoing-a-change) using a dummy index as the new version. A dummy index is never used for queries and does not contain any data, so the effect is the same as if the index did not exist. For this example, you can name it `/oak:index/acme.product-1-custom-3`. This name replaces the index `/oak:index/acme.product-1-custom-2`. An example of such a dummy index is:

```xml
<acme.product-1-custom-3
        jcr:primaryType="oak:QueryIndexDefinition"
        async="async"
        compatVersion="2"
        includedPaths="/dummy"
        queryPaths="/dummy"
        type="lucene">
        <indexRules jcr:primaryType="nt:unstructured">
            <rep:root jcr:primaryType="nt:unstructured">
                <properties jcr:primaryType="nt:unstructured">
                    <dummy
                        jcr:primaryType="nt:unstructured"
                        name="dummy"
                        propertyIndex="{Boolean}true"/>
                </properties>
            </rep:root>
        </indexRules>
</acme.product-1-custom-3>
```

## Index and Query Optimizations {#index-query-optimizations}

Apache Jackrabbit Oak enables flexible index configurations to efficiently handle search queries. Indexes are especially important for larger repositories. Ensure that all queries are backed by an appropriate index. Queries without a suitable index may read thousands of nodes, which are then logged as a warning.

See [this document](query-and-indexing-best-practices.md) for information on how queries and indexes can be optimized.
