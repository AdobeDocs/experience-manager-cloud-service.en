---
title: Handling Large Content Repositories
description: This section describes handling of large content repositories
exl-id: 21bada73-07f3-4743-aae6-2e37565ebe08
feature: Migration
role: Admin
---
# Handling Large Content Repositories {#handling-large-content-repositories}

## Overview {#overview}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_precopy"
>title="Handling Large Content Repositories"
>abstract="To significantly speed up the extraction and ingestion phases of the content transfer activity to move content to AEM as a Cloud Service, Content Transfer Tool (CTT) can use AzCopy as an optional pre-copy step. Once this pre-step is configured, in the extraction phase, AzCopy copies blobs from Amazon S3 or Azure Blob Storage to the migration set blob store. In the ingestion phase, AzCopy copies blobs from the migration set blob store to the destination AEM as a Cloud Service blob store."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/handling-large-content-repositories.html#setting-up-pre-copy-step" text="Getting started with AzCopy as a Pre-Copy step"

Copying many blobs with the Content Transfer Tool (CTT) may take multiple days. 
To speed up the extraction and ingestion phases of the content transfer activity to move content to AEM as a Cloud Service, CTT can use [AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) as an optional pre-copy step. This pre-copy step can be used when the source AEM instance is configured to use an Amazon S3, Azure Blob Storage data store, or File Data Store. The pre-copy step is most effective for the first full extraction and ingestion. However, using pre-copy for subsequent top-ups is not recommended (if the top-up size is less than 200 GB) because it may add time to the entire process. Once this pre-step is configured, in the extraction phase, AzCopy copies blobs from Amazon S3,  Azure Blob Storage, or File data store to the migration set blob store. In the ingestion phase, AzCopy copies blobs from the migration set blob store to the destination AEM as a Cloud Service blob store. 

## Important Considerations before you Start {#important-considerations}

Follow the section below to understand the important considerations before starting: 

* Starting from version 2.0.16 of CTT, the precopy setup is done automatically when the bundle is installed. Also, if the migration set size is greater than 200 GB, the extraction process automatically uses the precopy feature. The azcopy.config file is created in the crx-quickstart/cloud-migration/ directory. You do not need to manually do the precopy setup if you are using CTT version 2.0.16 or later.

* Source AEM version must be 6.3 - 6.5.

* Source AEM's data store is configured to use Amazon S3 or Azure Blob Storage. For more details, see [Configuring node stores and data stores in AEM 6](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/deploying/data-store-config.html).

* Each migration set copies the entire data store, so only a single migration set should be used.

* You need access to install [AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) on the instance (or VM) running the source AEM instance.

* Data Store Garbage Collection has been run within the previous seven days on the source. For more details, see [Data store garbage collection](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/deploying/data-store-config.html#data-store-garbage-collection).  

### Additional Considerations if source AEM instance is configured to use an Amazon S3 or Azure Blob Storage Data Store {#additional-considerations-amazons3-azure}

* There is a cost associated with transferring data out of Amazon S3 and Azure Blob Storage. The transfer cost is relative to the total amount of data in your existing storage container (whether referenced in AEM, or not). See [Amazon S3](https://aws.amazon.com/s3/pricing/) and [Azure Blob Storage](https://azure.microsoft.com/en-us/pricing/details/bandwidth/) for more details.

* You need either an access key and secret key pair for the existing source Amazon S3 bucket, or a SAS URI for the existing source Azure Blob Storage container (read-only access is fine).

### Additional considerations if source AEM instance is configured to use File Data Store {#additional-considerations-aem-instance-filedatastore}

* The local system must have free space strictly greater than 1/256 size of the source datastore. For example, if the size of the datastore is 3 terabytes, free space greater than 11.72 GB must exist in the `crx-quickstart/cloud-migration` folder on the source for AzCopy to work. At a minimum, the source system should have 1 GB of free space. Free space can be obtained by using `df -h` command on Linux&reg; instances, and dir command in the Windows instances.  

* Each time extraction is run with AzCopy enabled, the entire file datastore is flattened and copied to the cloud migration container. If your migration set is smaller than the size of your datastore, then AzCopy extraction is not the optimal approach.

* Once AzCopy has been used to copy over the existing datastore, disable it for delta or top-up extractions.

## Setting up to Use AzCopy as a Pre-Copy Step {#setting-up-pre-copy-step}

>[!NOTE]
>Starting from version 2.0.16 of CTT, the precopy setup is done automatically when the bundle is installed. Also, if the migration set size is greater than 200 GB, the extraction process automatically uses the precopy feature. The azcopy.config file is created in the crx-quickstart/cloud-migration/ directory. If you would like to update the configuration of the file manually, review the sections below.

Follow this section so you can learn how to set up to use AzCopy as a pre-copy step with Content Transfer Tool to migrate the content to AEM as a Cloud Service:

### 0. Determine total size of all content in the data store {#determine-total-size}

It is important to determine the total size of the data store for two reasons: 

* If the source AEM is configured to use File data store, the local system must have free space strictly greater than 1/256 size of the source data store.

#### Azure Blob Storage Data Store {#azure-blob-storage}

From the existing container properties page in the Azure portal, use the **Calculate size** button to determine the size of all content in the container. For example:

![image](/help/journey-migration/content-transfer-tool/assets/Azure-blob-storage-data-store.png)

#### Amazon S3 Data Store {#amazon-data}

You can use the container's Metrics tab to determine the size of all content in the container. For example:


![image](/help/journey-migration/content-transfer-tool/assets/amazon-s3-data-store.png)

#### File Data Store {#file-data-store-determine-size}
 
* For Mac, UNIX&reg; systems, run the du command on the datastore directory to get its size:
`du -sh [path to datastore on the instance]`. For example, if your datastore is at `/mnt/author/crx-quickstart/repository/datastore`, the following command gets you its size: `du -sh /mnt/author/crx-quickstart/repository/datastore`.

* For Windows, use the dir command on the datastore directory to get its size:
`dir /a/s [location of datastore]`.

### 1. Install AzCopy {#install-azcopy}

[AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) is a command-line tool provided by Microsoft&reg; that must be available on the source instance to enable this feature.

In short, you want to download the Linux&reg; x86-64 binary from the [AzCopy docs page](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) and untar it to a location such as /usr/bin. 

>[!IMPORTANT]
>Make note of where you placed the binary, because you need the full path to it in a later step.

### 2. Install Content Transfer Tool (CTT) release with AzCopy support {#install-ctt-azcopy-support}

>[!IMPORTANT]
>The most recently released version of CTT should be used.

AzCopy support for Amazon S3, Azure Blob Storage, and File Data Store is included in latest CTT release.
You can download the latest release of CTT from the [Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html) portal.
It should be noted that only versions 2.0.0 and higher are supported, and it is advisable to use the most recent version.

### 3. Configure an azcopy.config file {#configure-azcopy-config-file}

On the source AEM instance, in `crx-quickstart/cloud-migration`, create a file called `azcopy.config`.

>[!NOTE]
>The contents of this config file is different depending on whether your source AEM instance uses an Azure or Amazon S3 data store or File data store.

#### Azure Blob Storage Data Store {#azure-blob-storage-data}

Your azcopy.config file should include the following properties (make sure to use the correct azCopyPath and azureSas for your instance).

>[!NOTE]
>
> If you do not want grant write access to the existing blob storage container, you can generate a new SAS URI which only has Read and List permissions.

```
azCopyPath=/usr/bin/azcopy
azureSas=https://example-resource.blob.core.windows.net/example-container?sig=--REDACTED--
```

#### Amazon S3 Data Store {#amazon-sdata-store}

Your azcopy.config file should include the following properties (make sure to use the correct values for your instance).

>[!NOTE]
>
> If your instance uses IAM Roles to enable AEM to access S3, you must create a policy and user with the ListBucket and GetObject actions enabled for the S3 bucket. Once set up, use this user's access key and secret key.

```
azCopyPath=/usr/bin/azcopy
s3Bucket=aem-63
s3Region=us-west-2
s3AccessKey=--REDACTED--
s3SecretKey=--REDACTED--
```

#### File Data Store {#file-data-store-azcopy-config}

Your `azcopy.config` file must contain the azCopyPath property, and an optional repository.home property that points to the location of the file datastore. Use the correct values for your instance.
File Data Store

```
azCopyPath=/usr/bin/azcopy
repository.home=/mnt/crx/author/crx-quickstart/repository/datastore
```

The azCopyPath property must contain the full path of the location where the azCopy command-line tool is installed on the source AEM instance. If the azCopyPath property is missing, the blob precopy step is not performed. 

If `repository.home` property is missing from azcopy.config, then the default datastore location `/mnt/crx/author/crx-quickstart/repository/datastore` is used to perform precopy.

### 4. Extracting with AzCopy {#extracting-azcopy}

With the above configuration file in place, the AzCopy pre-copy phase runs as part of every subsequent extraction. To prevent it from running, you can rename this file or remove it.

>[!NOTE]
>If AzCopy is not configured correctly, you would see the following message in the logs:
>`INFO c.a.g.s.m.c.a.AzCopyCloudBlobPreCopy - Blob pre-copy is not supported`.

1. Begin an extraction from the CTT UI. See [Getting Started with Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/getting-started-content-transfer-tool.md) and the [Extraction Process](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md) for more details.

1. Confirm that the following line is printed in the extraction log:

```
c.a.g.s.m.commons.ContentExtractor - *************** Beginning AzCopy Pre-Copy phase ***************
```

Congratulations! This log entry means that your configuration was considered valid and that AzCopy is copying all blobs from the source container to the migration container.

The log entries from AzCopy appear in the extraction log, and are prefixed with c.a.g.s.m.c.azcopy.AzCopyBlobPreCopy - [AzCopy pre-copy] 

>[!CAUTION]
>
> For the first few minutes of an extraction, watch the extraction logs closely for any sign of an issue. As an example, here is what would be logged if the source Azure container could not be found:

```
[AzCopy pre-copy] failed to perform copy command due to error: cannot start job due to error: cannot list files due to reason > github.com/Azure/azure-storage-blob-go/azblob.newStorageError, github.com/Azure/azure-storage-blob-go@v0.10.1-0.20210407023846-16cf969ec1c3/azblob/zc_storage_error.go:42
[AzCopy pre-copy] ===== RESPONSE ERROR (ServiceCode=ContainerNotFound) =====
[AzCopy pre-copy] Description=The specified container does not exist.
[AzCopy pre-copy] RequestId:5fb674b9-201e-001b-2a5b-527400000000
[AzCopy pre-copy] Time:2021-05-26T18:18:07.5931967Z, Details: 
[AzCopy pre-copy] Code: ContainerNotFound
```

If there is an issue with AzCopy, the extraction fails immediately, and the extraction logs contain detail on the failure.

Any blobs that were copied before the error are skipped automatically by AzCopy on subsequent runs, and do not need to be copied again.

>[!TIP]
>An ingestion can now be scheduled to start automatically immediately after an extraction succeeds. See [Ingesting Content into Target](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md) for more information.

#### For File Data Store {#file-data-store-extract}

When AzCopy is running for source file dataStore, you should see messages like these in the logs indicating that folders are getting processed:
`c.a.g.s.m.c.a.AzCopyFileSourceBlobPreCopy - [AzCopy pre-copy] Processing folder (1/24) crx-quickstart/repository/datastore/5d` 

### 5. Ingesting with AzCopy {#ingesting-azcopy}

See [Ingesting Content into Target](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md) for general information about ingesting content into the target from the Cloud Acceleration Manager (CAM), including instruction on how to use AzCopy (pre-copy), or not, in the "New Ingestion" dialog.

To take advantage of AzCopy during ingestion, Adobe requires that you are on an AEM as a Cloud Service version that is at least version 2021.6.5561.

See the "Ingestion Jobs" list in the Cloud Acceleration Manager and the ingestion's logs so you can see the progress. The log entries related to the
successful AzCopy tasks appear as follows (allowing for some differences). Checking the logs occasionally could alert you to problems
early on, and help you find a quick solution to any problems.

```
*************** Beginning AzCopy pre-copy phase ***************
INFO: Scanning...
INFO: Failed to create one or more destination container(s). Your transfers may still succeed if the container already exists.
INFO: Any empty folders will not be processed, because source and/or destination does not have full folder support
INFO: azcopy: A newer version 10.11.0 is available to download
 
Job 419d98da-fc05-2a45-70cc-797fee632031 has started
Log file is located at: /root/.azcopy/419d98da-fc05-2a45-70cc-797fee632031.log
 
0.0 %, 0 Done, 0 Failed, 886 Pending, 0 Skipped, 886 Total,
 
Job 419d98da-fc05-2a45-70cc-797fee632031 summary
Elapsed Time (Minutes): 0.0334
Number of File Transfers: 886
Number of Folder Property Transfers: 0
Total Number of Transfers: 886
Number of Transfers Completed: 17
Number of Transfers Failed: 0
Number of Transfers Skipped: 869
TotalBytesTransferred: 248350
Final Job Status: CompletedWithSkipped
 
*************** Completed AzCopy pre-copy phase ***************
```

## What's Next {#whats-next}

You have now learned about Handling Large Content Repositories to speed up the extraction and ingestion phases of the content transfer activity to move content to AEM as a Cloud Service. You are now ready to learn the Extraction Process using the Content Transfer Tool. See [Extracting Content from Source in Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md) so you can learn how to extract your migration set from the Content Transfer Tool.
