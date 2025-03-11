---
title: Validating Content Transfers
description: Use the Content Transfer Tool to validate content transfers
exl-id: a12059c3-c15a-4b6d-b2f4-df128ed0eea5
feature: Migration
role: Admin
---

# Validating Content Transfers {#validating-content-transfers}

## Getting Started {#getting-started}

Users can reliably determine if all the content that was extracted by the Content Transfer Tool was successfully ingested into the target instance. This validation feature works by comparing a digest of the paths of all nodes that were involved during extraction, with a digest of the paths of all nodes that were involved during ingestion. If there are any node paths included in the extraction digest that are missing from the ingestion digest, the validation is considered to have failed, and additional manual validation may be necessary.

>[!INFO]
>
>This feature will be available as of the Content Transfer Tool (CTT) version 1.8.x release. The AEM Cloud Service target environment must be running at least version 6158 or greater. It also requires the source environment to be setup to run [pre-copy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md#setting-up-pre-copy-step). The validation feature looks for the azcopy.config file on the source. If it fails to find this file, validation will not run. To learn more about how to configure an azcopy.config file, see [Handling Large Content Repositories - Configure an azcopy.config file](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md#configure-azcopy-config-file).

Validating a content transfer is an optional feature. Enabling this feature will increase both the time it takes to perform an extraction and an ingestion. To use the feature, enable it in the System Console of the source AEM environment by following these steps:

1. Navigate to the Adobe Experience Manager Web Console on your source instance, by going to **Tools - Operations - Web Console** or directly to the URL at *https://serveraddress:serverport/system/console/configMgr*
1. Search for **Content Transfer Tool Extraction Service Configuration**
1. Use the pencil icon button to edit its configuration values 
1. Enable the **Enable Migration Validation during extraction** setting, then press **Save**:

   ![image](/help/journey-migration/content-transfer-tool/assets/CTTvalidation1.png)

With this setting enabled, and the target AEM Cloud Service environment running a compatible release, migration validation will occur during all extraction and ingestions that follow.

For more information on how to install the Content Transfer Tool, see [Getting Started with Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/getting-started-content-transfer-tool.md).

## How to Validate a Content Transfer {#how-to-validate-a-content-transfer}

With migration validation enabled on the source AEM environment, begin an extraction.

If **Overwrite staging container during extraction** is enabled, all the nodes which are involved with the extraction are logged to the extraction path digest. When this setting is used, it is important to enable the **Wipe existing content on Cloud instance before ingestion** setting during ingestion, otherwise there may appear to be nodes missing from the ingestion digest. These are the nodes which are already present on the target from prior ingestions.

For a graphical illustration of this, see the following examples:

### Example 1 {#example-1}

* **Extraction (Overwrite)**

  ![image](/help/journey-migration/content-transfer-tool/assets-ctt/example1-extraction.png)

* **Ingestion (Wipe)**

  ![image](/help/journey-migration/content-transfer-tool/assets-ctt/validation-02.png)

* **Notes**

  This combination of "Overwrite" and "Wipe" will result in consistent validation results, even for repeated ingestions.

### Example 2 {#example-2}

* **Extraction**

  ![image](/help/journey-migration/content-transfer-tool/assets-ctt/example2-extraction.png)

* **Ingestion**

  ![image](/help/journey-migration/content-transfer-tool/assets-ctt/validation-04.png)

* **Notes**

  This combination of "Overwrite" and "Wipe" will result in consistent validation results for the initial ingestion.

  If ingestion is repeated, the ingestion digest is empty, and validation appears to have failed. The ingestion digest is empty because all the nodes from this extraction will already be present on the target.

Once extraction is complete, begin ingestion.

The top of the ingestion log will contain an entry, similar to `aem-ethos/tools:1.2.438`. Ensure this version number is **1.2.438** or greater, otherwise validation is not supported by the release of AEM as a Cloud Service that you are using.

After ingestion is complete and validation is beginning, the following log entry is noted in the ingestion log:

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

To compare, here is how a validation report would look if validation had failed (or if a top-up migration was performed):

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
See our Migration Validation FAQ (https://www.adobe.com/go/aem_cloud_ctt_validation_en) or open a ticket with Customer Care.
There are 4635 entries present in the extraction digest that are missing from the ingestion digest.
/content/dam/bruce
/content/dam/bruce-assets
... more paths listed (up to 10k) ...
----------------------------------------------------------
Comparing the path digests took 0 seconds
Migration validation took 0 minutes
```

The above failure example was achieved by running an ingestion, and then re-running the same ingestion again with Wipe disabled, such that no nodes were involved during ingestion — everything was already present on the target.

In addition to being included in the ingestion log, the validation report can also be accessed from the **Ingestion Jobs** user interface in Cloud Acceleration Manager. To do so, click the three dots (**...**)  then click **Validation report** in the drop-down to view the validation report. 


![image](/help/journey-migration/content-transfer-tool/assets-ctt/CTTvalidationreportnew.png)

## How to Validate the Principal Migration {#how-to-validate-group-migration}

See [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md) to read the principal migration details and why it is necessary.

After the extraction and ingestion are successfully completed, a summary and report of the principal migration is available. This information can be used to validate which groups were migrated successfully, and, perhaps, to determine why some were not.

To view this information, go to Cloud Acceleration Manager. Click your project card and click the Content Transfer card. Navigate to **Ingestion Jobs** and locate the ingestion that you want to verify. Click the three dots (**...**) for that ingestion, then click **View principal summary** in the drop-down.

![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-principal-action.png)

You see a dialog with the summary information. Use the help icons to read a more full description. To download the full comma-separated (CSV) Principal Migration Report select **Principal Migration Report** from the dropdown list under **Download a file...** and click the **Download** button. Also note that at the end of this report is the User Report, which can be used for post-migration user management.

![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-principal-dialog.png)

The Principal Migration report will report:

* Each group migrated and the first content path that triggered that group to be migrated; the group could also be on other paths, but only the first one found for a given group is reported. It also reports whether it was found in an ACL or a CUG policy.
* Each group migrated as a local group will have the word "local" indicated on the group's line.
* Each group not migrated, and the reason it was not migrated.  Typically it will be one of these reasons:
    * It is a built-in group
    * It is already on the target system
    * It is not in an ACL or CUG policy on the content being migrated
    * It has a duplicate unique field (one of rep:principalName, rep:authorizableId, jcr:uuid or rep:externalId is already on the destination, but these all must be unique)

## Troubleshooting {#troubleshooting}

### Validation failed. What now? {#validation-fail}

The first step is to determine if ingestion really did fail, or if the extracted content is already present on the target environment. This can occur if an ingestion is repeated with the **Wipe existing content on Cloud instance before ingestion** option disabled.

To verify, choose a path from the validation report and check if it is present on the target environment. If this is a publish environment, you may be limited to checking pages and assets directly. Open a ticket with Customer Care if you need assistance with this step.

### The node count is lower than I was expecting. Why is that? {#node-count-lower-than-expected}

Some paths from the extraction and ingestion digests are excluded purposefully to keep the size of these files manageable, with the goal of being able to calculate the migration validation result within two hours of the ingestion completing.

The paths we currently exclude from the digests include: `cqdam.text.txt` renditions, nodes within `/home`, and nodes within `/jcr:system`.

### Closed User Groups {#validating-cugs}

See [Migrating Closed User Groups](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/closed-user-groups-migration.md) for extra considerations when using a Closed User Group (CUG) policy.
