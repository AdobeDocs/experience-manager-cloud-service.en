---
title: Handling Large Content Repositories
description: This section describes handling of large content repositories
exl-id: 2eca7fa6-fb34-4b08-b3ec-4e9211e94275
---
# Handling Large Content Repositories {#handling-large-content-repositories}

## Overview {#overview}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_precopy"
>title="Handling Large Content Repositories"
>abstract="To significantly speed up the extraction and ingestion phases of the content transfer activity to move content to AEM as a Cloud Service, CTT can leverage AzCopy as an optional pre-copy step. Once this pre-step is configured, in the extraction phase, AzCopy copies blobs from Amazon S3 or Azure Blob Storage to the migration set blob store. In the ingestion phase, AzCopy copies blobs from the migration set blob store to the destination AEM as a Cloud Service blob store."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en#setting-up-pre-copy-step" text="Getting started with AzCopy as a Pre-Copy step"

Copying a large number of blobs with the Content Transfer Tool (CTT) may take multiple days. 
To significantly speed up the extraction and ingestion phases of the content transfer activity to move content to AEM as a Cloud Service, CTT can leverage [AzCopy](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) as an optional pre-copy step. This pre-copy step can be used when the source AEM instance is configured to use an Amazon S3 or Azure Blob Storage data store.  Once this pre-step is configured, in the extraction phase, AzCopy copies blobs from Amazon S3 or Azure Blob Storage to the migration set blob store. In the ingestion phase, AzCopy copies blobs from the migration set blob store to the destination AEM as a Cloud Service blob store. 

>[!NOTE]
> This functionality was introduced in the CTT 1.5.4 release.

## Important Considerations before you Start {#important-considerations}

Follow the section below to understand the important considerations before starting: 

* Source AEM version needs to be 6.3 - 6.5
* Source AEM's data store is configured to use Amazon S3 or Azure Blob Storage. For more details, refer [Configuring node stores and data stores in AEM 6](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/deploying/data-store-config.html?lang=en).
* The entire data store will be copied during the extraction. Since there is a cost associated with transferring data out of both Amazon S3 and Azure Blob Storage, the transfer cost will be relative to the total amount of data in the storage container (whether referenced in AEM, or not). Refer to [Amazon S3](https://aws.amazon.com/s3/pricing/) and [Azure Blob Storage](https://azure.microsoft.com/en-us/pricing/details/bandwidth/) for more details. 
* Each migration set will copy the entire data store, so only a single migration set should be used.
* You will need access to install [AzCopy](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) on the instance (or VM) running the source AEM instance.
* You will need either an access key & secret key pair for the source Amazon S3 bucket, or a SAS URI for the source Azure Blob Storage container (read only access is fine).
* Data Store Garbage Collection has been run within the previous 7 days on the source. For more details, refer to [Data store garbage collection](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/deploying/data-store-config.html?lang=en#data-store-garbage-collection).
* The majority of the data on the source instance will be included in the migration.

## Setting up to Use AzCopy as a Pre-Copy Step {#setting-up-pre-copy-step}

Follow this section to learn how to set up to use AzCopy as a pre-copy step with Content Transfer Tool to migrate the content to AEM as a Cloud Service:

### 0. Determine total size of all content in the data store {#determine-total-size}

#### Azure Blob Storage Data Store {#azure-blob-storage}

From the container properties page in the Azure portal, use the **Calculate size** button to determine the size of all content in the container. For example:

![image](/help/move-to-cloud-service/content-transfer-tool/assets/Azure-blob-storage-data-store.png)

#### Amazon S3 Data Store {#amazon-data}

You can use the container's Metrics tab to determine the size of all content in the container. For example:


![image](/help/move-to-cloud-service/content-transfer-tool/assets/amazon-s3-data-store.png)

### 1. Install AzCopy {#install-azcopy}

[AzCopy](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) is a command-line tool provided by Microsoft that needs to be available on the source instance to enable this feature.

In short, you will most likely want to download the Linux x86-64 binary from the [AzCopy docs page](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) and un-tar it to a location such as /usr/bin. Make note of where you placed the binary, as you will need the full path to it in a later step.

### 2. Install a Content Transfer Tool (CTT) release with AzCopy support {#install-ctt-azcopy-support}

AzCopy support is included in the CTT 1.5.4 release. You can download the latest release of CTT from the [Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html) portal.

### 3. Configure an azcopy.config file {#configure-azcopy-config-file}

On the source AEM instance, in crx-quickstart/cloud-migration , create a new file called azcopy.config .

The contents of this config file will be different depending on whether your source AEM instance uses an Azure or Amazon S3 data store.

#### Azure Blob Storage Data Store {#azure-blob-storage-data}

Your azcopy.config file should include the following properties (make sure to use the correct azCopyPath and azureSas for your instance).

>[!NOTE]
>
> If you'd rather not grant write access to the blob storage container, you can generate a new SAS URI which only has Read  and List  permissions.

```
azCopyPath=/usr/bin/azcopy
azureSas=https://example-resource.blob.core.windows.net/example-container?sig=--REDACTED--
```

#### Amazon S3 Data Store {#amazon-sdata-store}

Your azcopy.config file should include the following properties (make sure to use the correct values for your instance).

>[!NOTE]
>
> If your instance uses IAM Roles to enable AEM to access S3, you will need to create a policy and user with the ListBucket and GetObject actions enabled for the S3 bucket. Once set up, use this user's access key and secret key.

```
azCopyPath=/usr/bin/azcopy
s3Bucket=aem-63
s3Region=us-west-2
s3AccessKey=--REDACTED--
s3SecretKey=--REDACTED--
```

### 4. Extracting with AzCopy {#extracting-azcopy}

With the above configuration file in place, the AzCopy pre-copy phase will run as part of every subsequent extraction. To prevent it from running, you can rename this file or remove it.

1. Begin an extraction from the CTT UI. Refer to [Running the Content Transfer Tool](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#running-tool) and the [Extraction Process](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#extraction-process) for more details.
1. Confirm the following line is printed in the extraction log:

```
c.a.g.s.m.commons.ContentExtractor - *************** Beginning AzCopy Pre-Copy phase ***************
```

Congratulations! This log entry means that your configuration was considered valid and that AzCopy is currently copying all blobs from the source container to the migration container.

The log entries from AzCopy will appear in the extraction log, and will be prefixed with c.a.g.s.m.c.azcopy.AzCopyBlobPreCopy - [AzCopy pre-copy] 

>[!CAUTION]
>
> For the first few minutes of an extraction, watch the extraction logs closely for any sign of an issue. As an example, here is what would be logged if the source Azure container could not be found:
>

```
[AzCopy pre-copy] failed to perform copy command due to error: cannot start job due to error: cannot list files due to reason -> github.com/Azure/azure-storage-blob-go/azblob.newStorageError, github.com/Azure/azure-storage-blob-go@v0.10.1-0.20210407023846-16cf969ec1c3/azblob/zc_storage_error.go:42
[AzCopy pre-copy] ===== RESPONSE ERROR (ServiceCode=ContainerNotFound) =====
[AzCopy pre-copy] Description=The specified container does not exist.
[AzCopy pre-copy] RequestId:5fb674b9-201e-001b-2a5b-527400000000
[AzCopy pre-copy] Time:2021-05-26T18:18:07.5931967Z, Details: 
[AzCopy pre-copy] Code: ContainerNotFound
```

In the event of an issue with AzCopy, the extraction will fail immediately, and the extraction logs will contain detail on the failure.

Any blobs which were copied prior to the error will be skipped automatically by AzCopy on subsequent runs, and will not need to be copied again.

### 5. Ingesting with AzCopy {#ingesting-azcopy}

With the release of Content Transfer Tool 1.5.4, we added AzCopy support to Author ingestion. 

>[!NOTE]
>The recommendation is to run Author ingestion first alone. This will speed up the Publish ingestion when it is run later.

To take advantage of AzCopy during ingestion, we require that you be on a AEM as a Cloud Service version that is at least version 2021.6.5561.

Begin the author ingestion from the CTT UI. Refer to the [Ingestion Process](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#ingestion-process) for more details.
The log entries from AzCopy will appear in the ingestion log. They will look like this:

```
*************** Beginning AzCopy pre-copy phase ***************
INFO: Scanning...
INFO: Failed to create one or more destination container(s). Your transfers may still succeed if the container already exists.
INFO: Any empty folders will not be processed, because source and/or destination doesn't have full folder support
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

Once you have learned Handling Large Content Repositories to significantly speed up the extraction and ingestion phases of the content transfer activity to move content to AEM as a Cloud Service, you are now ready to learn the Extraction Process in Content Transfer Tool. See [Extracting Content from Source in Content Transfer Tool](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool/extracting-content.md) to learn how to extract your migration set from the Content Transfer Tool.