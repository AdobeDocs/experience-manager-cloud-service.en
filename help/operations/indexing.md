---
title: Content Search and Indexing
description: Content Search and Indexing
exl-id: 4fe5375c-1c84-44e7-9f78-1ac18fc6ea6b
---
# Content Search and Indexing {#indexing}

## Changes in AEM as a Cloud Service {#changes-in-aem-as-a-cloud-service}

With AEM as a Cloud Service, Adobe is moving away from an AEM instance-centric model to a service-based view with n-x AEM Containers, driven by CI/CD pipelines in the Cloud Manager. Instead of configuring and maintaining Indexes on single AEM instances, the Index configuration has to be specified before a deployment. Configuration changes in production are clearly breaking CI/CD policies. The same holds true for index changes since it can impact system stability and performance if not specified tested and reindexed before bringing them into production.

Below is a list of the main changes compared to AEM 6.5 and earlier versions:

1. Users will not have access to the Index Manager of a single AEM Instance to debug, configure or maintain indexing anymore. It is only used for local development and on-prem deployments.
1. Users will not change Indexes on a single AEM Instance nor will they have to worry about consistency checks or reindexing anymore.
1. In general, index changes are initiated before going to production in order to not circumvent quality gateways in the Cloud Manager CI/CD pipelines and not impact Business KPIs in production.
1. All related metrics including search performance in production will be available for customers at runtime in order to provide the holistic view on the topics of Search and Indexing.
1. Customers will be able to set up alerts according to their needs.
1. SREs are monitoring system health 24/7 and will take action as needed and as early as possible.
1. Index configuration is changed via deployments. Index definition changes are configured like other content changes.
1. At a high level on AEM as a Cloud Service, with the introduction of the [rolling deployment model](#index-management-using-rolling-deployments) two sets of indexes will exist: one set for the old version, and one set for the new version.
1. Customers can see whether the indexing job is complete on the Cloud Manager build page and will receive a notification when the new version is ready to take traffic.

Limitations:

* Currently, index management on AEM as a Cloud Service is only supported for indexes of type `lucene`.
* Only standard analyzers are supported (that is, those that are shipped with the product). Custom analyzers are not supported.
* Internally, other indexes might be configured and used for queries. For example, queries that are written against the `damAssetLucene` index might, on Skyline,  in fact be executed against an Elasticsearch version of this index. This difference is typically not visible to the application and user, however certain tools such as the `explain` feature will report a different index. For differences between Lucene indexes and Elastic indexes, see [the Elastic documentation in Apache Jackrabbit Oak](https://jackrabbit.apache.org/oak/docs/query/elastic.html). Customers do not need to, and can not, configure Elasticsearch indexes directly.

## How to Use {#how-to-use}

Defining indexes can comprise of these three use cases:

1. Adding a new customer index definition.
1. Updating an existing index definition. This effectively means adding a new version of an existing index definition.
1. Removing an existing index that is redundant or obsolete.

For both points 1 and 2 above, you need to create a new index definition as part of your custom code base in the respective Cloud Manager release schedule. For more information, see the [Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md) documentation.

## Index Names {#index-names}

An index definition can fall into one of the following three categories:

1. Out-of-the-box index: This refers to a predefined index option provided as-is. For instance: `/oak:index/cqPageLucene-2`.

2. Customization of an out-of-the-box index: customers can tailor existing indexes to meet their specific requirements. These customizations are indicated by appending `-custom-` followed by a numerical identifier to the original index name. For example: `/oak:index/cqPageLucene-2-custom-1`.

3. Fully custom index: It is possible to create an entirely new index from scratch. These custom indexes must have a prefix to avoid naming conflicts. For instance: `/oak:index/acme.product-1-custom-2`. In this case, the prefix is `acme.`

Please note that both customized out-of-the-box indexes and fully custom indexes must include the -custom- keyword. Further details and guidelines can be found in the [Preparing the New Index Definition](#preparing-the-new-index-definition-preparing-the-new-index-definition) section. 

## Preparing the New Index Definition {#preparing-the-new-index-definition}

>[!NOTE]
>
>If customizing an out-of-the-box index, for example `damAssetLucene-8`, please copy the latest out-of-the-box index definition from a *Cloud Service environment* using the CRX DE Package Manager (`/crx/packmgr/`) . Rename it to `damAssetLucene-8-custom-1` (or higher), and add your customizations inside the XML file. This ensures that required configurations are not being removed inadvertently. For example, the `tika` node under `/oak:index/damAssetLucene-8/tika` is required in the customized index of the cloud service. It doesn't exist on the Cloud SDK.

You need to prepare a new index definition package that contains the actual index definition, following this naming pattern:

`<indexName>[-<productVersion>]-custom-<customVersion>`

Only fully custom indexes must start with a prefix.

<!-- Alexandru: temporarily drafting this statement due to CQDOC-17701

The package from the above sample is built as `com.adobe.granite:new-index-content:zip:1.0.0-SNAPSHOT`. -->

>[!NOTE]
>
>Any content package containing index definitions should have the following properties set in in the properties file of the content package, located at `<package_name>/META-INF/vault/properties.xml`:
>
> * `noIntermediateSaves=true`
>
> * `allowIndexDefinitions=true`

## Deploying Custom Index Definitions {#deploying-custom-index-definitions}

To illustrate the deployment of a customized version of the out-of-the-box index `damAssetLucene-8`, we will provide a step-by-step guide. In this example, we will rename it to `damAssetLucene-8-custom-1`. The deployment process involves the following steps:

1. Create a new folder with the updated index name within the ui.apps directory: 
    * Example: `ui.apps/src/main/content/jcr_root/_oak_index/damAssetLucene-8-custom-1/`

2. Inside the newly created folder, add a configuration file named `.content.xml` that contains the custom configuration. Below is an example showcasing a customization where nodes from the original out-of-the-box index are removed:
    * Example: `ui.apps/src/main/content/jcr_root/_oak_index/damAssetLucene-8-custom-1/.content.xml`

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
        reindex="{Boolean}false"
        reindexCount="{Long}1"
        seed="{Long}-1290430931455096831"
        tags="[visualSimilaritySearch]"
        type="lucene">
        <aggregates jcr:primaryType="nt:unstructured">
            <dam:Asset jcr:primaryType="nt:unstructured">
                <include0
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content"/>
                <include1
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/metadata"/>
                <include2
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/metadata/*"/>
                <include3
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/renditions"/>
                <include4
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/renditions/original"/>
                <include5
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/renditions/original/jcr:content"/>
                <include6
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/comments"/>
                <include7
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/comments/*"/>
                <include8
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/data/master"/>
                <include9
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/usages"/>
                <include10
                    jcr:primaryType="nt:unstructured"
                    path="jcr:content/renditions/cqdam.text.txt/jcr:content"/>
            </dam:Asset>
        </aggregates>
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
                    <dcFormat
                        jcr:primaryType="nt:unstructured"
                        analyzed="{Boolean}true"
                        facets="{Boolean}true"
                        name="jcr:content/metadata/dc:format"
                        propertyIndex="{Boolean}true"/>
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

4. Add a tika configuration file under: `ui.apps/src/main/content/jcr_root/_oak_index/damAssetLucene-8-custom-1/tika/config.xml`:

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

The above example contains a configuration for Apache Tika. The Tika configuration file should be stored under `ui.apps/src/main/content/jcr_root/_oak_index/damAssetLucene-8-custom-1/tika/config.xml`.

## Project Configuration

It is advisable to use the most recent version of the Jackrabbit `filevault-package-maven-plugin`, which is currently at version 1.3.2. 
To use this, there are specific configurations that needs to be incorporated into the top-level `pom.xml` file if it does not already contains so: 

```xml
<validatorsSettings>
    <jackrabbit-packagetype>
        <options>   
            <immutableRootNodeNames>apps,libs,oak:index</immutableRootNodeNames>
        </options>
    </jackrabbit-packagetype>
</validatorsSettings>
```

Below is a sample of the top level `pom.xml` file of the project with the above configurations added: 

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
            </validatorsSettings>
            ...
        </configuration>
</plugin>
```

### ui.apps and ui.apps.structure

Inside `ui.apps.structure/pom.xml` and `ui.apps/pom.xml`, the configuration of the `filevault-package-maven-plugin` needs to have `allowIndexDefinitions` as well as `noIntermediateSaves` enabled. The option `allowIndexDefinitions` allows custom index definitions while `noIntermediateSaves` ensures that the index configurations are added atomically. 

Filenames: `ui.apps/pom.xml` and `ui.apps.structure/pom.xml`

```xml
<groupId>org.apache.jackrabbit</groupId>
    <artifactId>filevault-package-maven-plugin</artifactId>
    <configuration>
        <allowIndexDefinitions>true</allowIndexDefinitions>
        <properties>
            <cloudManagerTarget>none</cloudManagerTarget>
            <noIntermediateSaves>true</noIntermediateSaves>
        </properties>
    ...
```

In `ui.apps.structure/pom.xml` you also need to add a filter for `/oak:index`:

```xml
<filters>
    ...
    <filter><root>/oak:index</root></filter>
</filters>
```

Once the new index definition is added, the new application needs to be deployed via Cloud Manager. Upon deployment, two jobs are started that are responsible for adding (and merging if needed) the index definitions to MongoDB and Azure Segment Store for author and publish, respectively. The underlying repositories are reindexed with the new index definitions, before the switch takings place.

>[!TIP]
>
>For further details on the required package structure for AEM as a Cloud Service, see the document [AEM Project Structure.](/help/implementing/developing/introduction/aem-project-content-package-structure.md)

## Index Management using Rolling Deployments {#index-management-using-rolling-deployments}

### What is Index Management {#what-is-index-management}

Index management is about adding, removing, and changing indexes. Changing the *definition* of an index is fast, but applying the change (often called "building an index", or, for existing indexes, "reindexing") requires time. It is not instantaneous: the repository has to be scanned for data to be indexed.

### What are Rolling Deployments {#what-are-rolling-deployments}

A rolling deployment can reduce downtime. It also allows for zero downtime upgrades and provides fast rollbacks. The old version of the application runs at the same time as the new version of the application.

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

During development, or when using on premise installations, indexes can be added, removed, or changed at runtime. Indexes are used as soon as they are available. If an index is not supposed to be used in the old version of the application yet, then the index is typically built during a scheduled downtime. The same occurs when removing an index, or changing an existing index. When removing an index, it becomes unavailable as soon as it is removed.

### Index Management With Rolling Deployments {#index-management-with-rolling-deployments}

With rolling deployments, there is no downtime. For some time during an update, both the old version (for example, version 1) of the application, as well as the new version (version 2), run concurrently against the same repository. If version 1 requires a certain index to be available, then this index must not be removed in version 2. The index should be removed later, for example in version 3, at which point it is guaranteed that version 1 of the application is no longer running. Also, applications should be written such that version 1 works well, even if version 2 is running, and if indexes of version 2 are available.

After upgrading to the new version is complete, old indexes can be garbage collected by the system. The old indexes might still stay for some time, in order to speed up rollbacks (if a rollback should be needed).

The following table shows five index definitions: index `cqPageLucene` is used in both versions while index `damAssetLucene-custom-1` is used only in version 2.

>[!NOTE]
>
>`<indexName>-custom-<customerVersionNumber>` is needed for AEM as a Cloud Service to mark this as a replacement for an existing index.

| Index | Out-of-the-box Index  | Use in Version 1  | Use in Version 2  |
|---|---|---|---|
| /oak:index/damAssetLucene  | Yes  | Yes  | No  |
| /oak:index/damAssetLucene-custom-1  | Yes (customized)  | No  | Yes  |
| /oak:index/acme.product-custom-1  | No  | Yes  | No  |
| /oak:index/acme.product-custom-2  | No  | No  | Yes  |
| /oak:index/cqPageLucene  | Yes  | Yes  | Yes  |

The version number is incremented each time the index is changed. In order to avoid custom index names colliding with index names of the product itself, custom indexes, as well as changes to out of the box indexes must end with `-custom-<number>`.

### Changes to Out-of-the-Box Indexes {#changes-to-out-of-the-box-indexes}

Once Adobe changes an out-of-the-box index like "damAssetLucene" or "cqPageLucene", a new index named `damAssetLucene-2` or `cqPageLucene-2` is created, or, if the index was already customized, the customized index definition is merged with the changes in the out-of-the-box index, as shown below. Merging of changes happens automatically. That means that you do not need to do anything if an out-of-the-box index changes. However, it is possible to customize the index again later.

| Index  | Out-of-the-box Index  | Use in Version 2  | Use in Version 3  |
|---|---|---|---|
| /oak:index/damAssetLucene-custom-1  | Yes (customized)  | Yes  | No  |
| /oak:index/damAssetLucene-2-custom-1  | Yes (automatically merged from damAssetLucene-custom-1 and damAssetLucene-2)  | No  | Yes  |
| /oak:index/cqPageLucene  | Yes  | Yes  | No  |
| /oak:index/cqPageLucene-2  | Yes  | No  | Yes  |

### Current Limitations {#current-limitations}

Index management is currently only supported for indexes of type `lucene`, with `compatVersion` set to `2`. Internally, other indexes might be configured and used for queries, for example Elasticsearch indexes. Queries that are written against the `damAssetLucene` index might, on AEM as a Cloud Service, in fact be executed against an Elasticsearch version of this index. This difference is invisible to the application end user, however certain tools such as the `explain` feature will report a different index. For differences between Lucene and Elasticsearch indexes, see [the Elasticsearch documentation in Apache Jackrabbit Oak](https://jackrabbit.apache.org/oak/docs/query/elastic.html). Customers cannot and do not need to configure Elasticsearch indexes directly.

Only built-in analyzers are supported (that is, those that are shipped with the product). Custom analyzers are not supported.

For best operational performance, indexes should not be excessively large. The total size of all indexes can be used as a guide: If this increases by more than 100%  after custom indexes have been added and standard indices have been adjusted on a development environment, custom index definitions should be adjusted. AEM as a Cloud Service can prevent the deployment of indexes that would negatively impact system stability and performance. 

### Adding an Index {#adding-an-index}

To add a fully custom index named `/oak:index/acme.product-custom-1` to be used in a new version of the application and later, the index must be configured as follows:

`acme.product-1-custom-1`

This works by prepending a custom identifier to the index name, followed by a dot (**`.`**). The identifier should be between 2 and 5 characters in length.

As above, this ensures the index is only used by the new version of the application.

### Changing an Index {#changing-an-index}

When an existing index is changed, a new index needs to be added with the changed index definition. For example, consider the existing index `/oak:index/acme.product-custom-1` is changed. The old index is stored under `/oak:index/acme.product-custom-1`, and the new index is stored under `/oak:index/acme.product-custom-2`.

The old version of the application uses the following configuration:

`/oak:index/acme.product-custom-1`

The new version of the application uses the following (changed) configuration:

`/oak:index/acme.product-custom-2`

>[!NOTE]
>
>Index definitions on AEM as a Cloud Service may not fully match the index definitions on a local development instance. The development instance does not have a Tika configuration, while AEM as a Cloud Service instances do have one. If you customize an index with a Tika configuration, please retain the Tika configuration.

### Undoing a Change {#undoing-a-change}

Sometimes, a change in an index definition needs to be reverted. The reasons could be that a change was made by mistake, or a change is no longer needed. For example, the index definition `damAssetLucene-8-custom-3` was created by mistake and is already deployed. Because of that you may want to revert to the previous index definition `damAssetLucene-8-custom-2`. To do that, you need to add a new index called `damAssetLucene-8-custom-4` that contains the definition of the previous index, `damAssetLucene-8-custom-2`.

### Removing an Index {#removing-an-index}

The following only applies to custom indexes. Product indexes may not be removed as they are used by AEM.

If an index is to be removed in a later version of the application, you can define an empty index (an empty index that is never used, and does not contain any data), with a new name. For the purpose of this example, you can name it `/oak:index/acme.product-custom-3`. This replaces the index `/oak:index/acme.product-custom-2`. Once `/oak:index/acme.product-custom-2` is removed by the system, the empty index `/oak:index/acme.product-custom-3` can then also be removed. An example of such an empty index is:

```xml
<acme.product-custom-3
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
</acme.product-custom-3>
```

If it is no longer needed to have a customization of an out-of-the-box index, then you must copy the out-of-the-box index definition. For example, if you have already deployed `damAssetLucene-8-custom-3`, but no longer need the customizations and want to switch back to the default `damAssetLucene-8` index, then you must add an index `damAssetLucene-8-custom-4` that contains the index definition of `damAssetLucene-8`.

## Index and Query Optimizations {#index-query-optimizations}

Apache Jackrabbit Oak enables flexible index configurations to efficiently handle search queries. Indexes are especially important for larger repositories. Please ensure that all queries are backed by an appropriate index. Queries without a suitable index may read thousands of nodes, which is then logged as a warning.

Please see [this document](query-and-indexing-best-practices.md) for information on how queries and indexes can be optimized.
