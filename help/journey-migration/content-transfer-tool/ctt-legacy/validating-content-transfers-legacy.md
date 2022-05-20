---
title: Validating Content Transfers (Legacy)
description: Use the Content Transfer Tool to validate content transfers
hide: yes
hidefromtoc: yes
---
# Validating Content Transfers (Legacy) {#validating-content-transfers}

## Getting Started {#getting-started}

Users have the ability to reliably determine if all of the content that was extracted by the Content Transfer Tool was successfully ingested into the target instance. This validation feature works by comparing a digest of the nodes that were involved during extraction, with a digest of nodes that were involved during ingestion. If there are any node paths included in the extraction digest that are missing from the ingestion digest, the validation is considered to have failed, and additional manual validation may be necessary.

>[!INFO]
>
>This feature will be available as of the Content Transfer Tool (CTT) version 1.8.x release. The AEM Cloud Service target environment must be running at least version 6158 or greater. It also requires the source environment to be setup to run [pre-copy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md#setting-up-pre-copy-step). The validation feature looks for the azcopy.config file on the source. If it fails to find this file, validation will not run. To learn more about how to configure an azcopy.config file, see [this page](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md#configure-azcopy-config-file).

Validating a content transfer is an optional feature. Enabling this feature will increase both the time it takes to perform an extraction as well as an ingestion. In order to use the feature, enable it in the System Console of the source AEM environment by following these steps:

1. Navigate to the Adobe Experience Manager Web Console on your source instance, by going to **Tools - Operations - Web Console** or directly to the URL at *https://serveraddress:serverport/system/console/configMgr*
1. Search for **Content Transfer Tool Extraction Service Configuration**
1. Use the pencil icon button to edit its configuration values 
1. Enable the **Enable Migration Validation during extraction** setting, then press **Save**:

   ![image](/help/journey-migration/content-transfer-tool/assets/CTTvalidation1.png)

With this setting enabled, and the target AEM Cloud Service environment running a compatible release, migration validation will occur during all extraction and ingestions that follow.

For more information on how to install the Content Transfer Tool, see [Getting Started with Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/getting-started-content-transfer-tool.md).

## How to Validate a Content Transfer {#how-to-validate-a-content-transfer}

With migration validation enabled on the source AEM environment, begin an extraction.

If **Overwrite staging container during extraction** is enabled, all the nodes which are involved with the extraction will be logged to the extraction path digest. When this setting is used, it is important to enable the **Wipe existing content on Cloud instance before ingestion** setting during ingestion, otherwise there may appear to be nodes missing from the ingestion digest. These are the nodes which are already present on the target from prior ingestions.

For a graphical illustration of this, please refer to the examples below:

### Example 1 {#example-1}

* **Extraction (Overwrite)**

  ![image](/help/journey-migration/content-transfer-tool/assets/CTTextractionoverwrite.png)

* **Ingestion (Wipe)**

  ![image](/help/journey-migration/content-transfer-tool/assets/CTTingestionwipe.png)

* **Notes**

  This combination of "Overwrite" and "Wipe" will result in consistent validation results, even for repeated ingestions.

### Example 2 {#example-2}

* **Extraction**

  ![image](/help/journey-migration/content-transfer-tool/assets/CTTextraction.png)

* **Ingestion**

  ![image](/help/journey-migration/content-transfer-tool/assets/CTTingestion.png)

* **Notes**

  This combination of "Overwrite" and "Wipe" will result in consistent validation results for the initial ingestion.

  If ingestion is repeated, the ingestion digest will be empty, and validation will appear to have failed. The ingestion digest will be empty because all the nodes from this extraction will already be present on the target.

Once extraction is complete, begin ingestion.

The top of the ingestion log will contain an entry, similar to `aem-ethos/tools:1.2.438`. Ensure this version number is **1.2.438** or greater, otherwise validation is not supported by the release of AEM as a Cloud Service that you are using.

Once ingestion is complete and validation is beginning, the following log entry will be noted in the ingestion log:

```
Gathering artifacts for migration validation...  
```

The details of the validation will follow this entry. Find an example from a large migration below:

```
Beginning publish migration validation. Migration job id=[3aba1f96-84b6-4bd0-8642-c61c0d528387]
Extraction path digest is being processed...
Extraction path digest processing took 982 seconds
Ingestion path digest is being processed...
Ingestion path digest processing took 999 seconds
Comparing the Extraction and Ingestion path digests...
----------------------------------------------------------
EXTRACTION: Number of nodes extracted: 51674784
INGESTION: Number of nodes ingested: 51674784
----------------------------------------------------------
Validation succeeded! No entries were detected to be missing from the ingestion digest.
----------------------------------------------------------
Comparing the path digests took 29 seconds
Migration validation took 33 minutes
```

This is an example of a validation that has succeeded, since there were no entries missing from the ingestion digest that were present in the extraction digest.

To compare, here is how a validation report would look if validation had failed:

```
Beginning publish migration validation. Migration job id=[ac217e5a-a08d-4e81-cbd6-f39f88b174ce]
Extraction path digest is being processed...
Extraction path digest processing took 0 seconds
Ingestion path digest is being processed...
Ingestion path digest processing took 0 seconds
Comparing the Extraction and Ingestion path digests...
----------------------------------------------------------
EXTRACTION: Number of nodes extracted: 4635
INGESTION: Number of nodes ingested: 0
----------------------------------------------------------
Validation failed. However, the following nodes may already be present in the target environment.
Please refer to our Migration Validation FAQ (https://www.adobe.com/go/aem_cloud_ctt_validation_en) or open a ticket with Customer Care.
There are 4635 entries present in the extraction digest that are missing from the ingestion digest.
/content/dam/bruce
/content/dam/bruce-assets
... more paths listed (up to 10k) ...
----------------------------------------------------------
Comparing the path digests took 0 seconds
Migration validation took 0 minutes
```

The above failure example was achieved by running an ingestion, and then re-running the same ingestion again with Wipe disabled, such that no nodes were involved during ingestion — everything was already present on the target.

In addition to being included in the ingestion log, the validation report can also be accessed from the Content Transfer Tool user interface. To do so, select a migration set, and click the **Validate** button from the action bar:


![image](/help/journey-migration/content-transfer-tool/assets/CTTvalidatebutton.png)

The Validation Logs dialog will open:

![image](/help/journey-migration/content-transfer-tool/assets/CTTvalidationlogs.png)

Use the **Validation Publish/Author Report** button to view the validation report for the most recent ingestion to the given tier of your target environment. See below an example from a small publish ingestion:

![image](/help/journey-migration/content-transfer-tool/assets/CTTvalidationreport.png)

>[!NOTE]
>
>The **Validation Publish/Author Report** link will appear once the ingestion is complete. Additionally, the validation reports are persisted, so they do not expire after ingestion completes, like the ingestion logs do. 

## Troubleshooting {#troubleshooting}

### Validation failed. What now? {#validation-fail}

The first step is to determine if ingestion really did fail, or if the extracted content is already present on the target environment. This can occur if an ingestion is repeated with the **Wipe existing content on Cloud instance before ingestion** otpion disabled.

To verify, choose a path from the validation report and check if it is present on the target environment. If this is a publish environment, you may be limited to checking pages and assets directly. Please open a ticket with Customer Care if you need assistance with this step.

### The node count is lower than I was expecting. Why is that? {#node-count-lower-than-expected}

Some paths from the extraction and ingestion digests are excluded purposefully to keep the size of these files manageable, with the goal of being able to calculate the migration validation result within two hours of the ingestion completing.

The paths we currently exclude from the digests include: `cqdam.text.txt` renditions, nodes within `/home`, and nodes within `/jcr:system`.
