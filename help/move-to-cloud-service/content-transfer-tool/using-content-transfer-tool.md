---
title: Using Content Transfer Tool
description: Using Content Transfer Tool
exl-id: a19b8424-33ab-488a-91b3-47f0d3c8abf5
---
# Using Content Transfer Tool {#using-content-transfer-tool}

## Extraction Process in Content Transfer {#extraction-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_extraction"
>title="Content Extraction"
>abstract="Extraction refers to extracting content from the source AEM instance into a temporary area called migration set. A migration set is a cloud storage area provided by Adobe to temporarily store the transferred content between the source AEM instance and the Cloud Service AEM instance."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#top-up-extraction-process" text="Top Up Extraction"

Follow the steps below to extract your migration set from the Content Transfer Tool:
   >[!NOTE]
   >If Amazon S3 or Azure Data Store is used as the type of data store, you can run the optional pre-copy step to significantly speed up the extraction phase. To do so you will need to configure an `azcopy.config` file before running extraction. Refer to [Handling large content repositories](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en) for more details. 

1. Select a migration set from *Overview* page and click **Extract** to start extraction. The **Migration Set extraction** dialog box displays and click on **Extract** to start the extraction phase.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/06-content-extraction.png) 

   >[!NOTE]
   >You have the option to overwrite staging container during the extraction phase.

   
1. The **EXTRACTION** field now displays the **RUNNING** status to indicate that the extraction is in-progress.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/07-extraction-job-running.png)

   Once the extraction is complete, the status of the migration set updates to **FINISHED** and a *solid green* cloud icon displays under the **INFO** field.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/10-extraction-complete.png)

   >[!NOTE]
   >The UI has an auto-reload feature that reloads the overview page every 30 seconds.
   >When extraction phase is started, write lock is created and released after *60 seconds*. So, if an extraction is stopped, you need to wait for a minute for lock to be released before starting extraction again.

### Top-Up Extraction {#top-up-extraction-process}

The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 
>Additionally, it is essential that the content structure of existing content is not changed from the time the initial extraction is taken to when the top-up extraction is run. Top-ups cannot be run on content whose structure has been changed since the initial extraction. Please ensure you restrict this during the migration process.

Once the extraction process is complete, you can transfer delta content, by using the top-up extraction method. Follow the steps below:

1. Navigate to the *Overview* page and select the migration set for which you want to perform the top-up extraction. Click **Extract** to start the top-up extraction. The **Migration Set extraction** dialog box displays.

   >[!IMPORTANT]
   >
   >You should disable the **Overwrite staging container during extraction** option.
   >
   >![image](/help/move-to-cloud-service/content-transfer-tool/assets/11-topup-extraction.png)

## Ingestion Process in Content Transfer {#ingestion-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_ingestion"
>title="Content Ingestion"
>abstract="Ingestion refers to ingesting content from the migration set into the target Cloud Service instance. The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#top-up-ingestion-process" text="Top Up Ingestion"

Follow the steps below to ingest your migration set from the Content Transfer Tool:
   >[!NOTE]
   >If Amazon S3 or Azure Data Store is used as the type of data store, you can run the optional pre-copy step to significantly speed up the ingestion phase. Refer to [Ingesting with AzCopy](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en#ingesting-azcopy) for more details. 

1. Select a migration set from *Overview* page and click **Ingest** to start ingestion. The **Migration Set ingestion** dialog box displays. Content can be ingested to either Author instance or Publish instance at a time. Select the instance to ingest content to. Click on **Ingest** to start the ingestion phase. 

   >[!IMPORTANT]
   >If ingesting with pre-copy is used (for S3 or Azure Data Store), it is recommended to run Author ingestion first alone. This will speed up the Publish ingestion when it is run later. 

   >[!IMPORTANT]
   >When the **Wipe existing content on Cloud instance before ingestion** option is enabled, it deletes the entire existing repository and creates a new repository to ingest content into. This means that it resets all settings including permissions on the target Cloud Service instance. This is also true for an admin user added to the **administrators** group.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/content-ingestion-03.png)

   Additionally, click on **Customer Care** to log a ticket, as shown in the figure above. Also, refer to [Important Considerations for Using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#pre-reqs) to learn more.

1. Once the ingestion is complete, the status updates to **FINISHED**.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/15-ingestion-complete.png)

### Top Up Ingestion {#top-up-ingestion-process}

The Content Transfer Tool has a feature that supports differential content *top-up* where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service.

Once the ingestion process is complete, you can use delta content, by using the top-up ingestion method. Follow the steps below:

1. Navigate to the *Overview* page and select the migration set for which you want to perform the top-up ingestion. Click **Ingest** to start the top-up extraction. The **Migration Set ingestion** dialog box displays. 

    ![image](/help/move-to-cloud-service/content-transfer-tool/assets/content-ingestion-02.png)

   >[!IMPORTANT]
   >You should disable the **Wipe existing content on Cloud instance before ingestion** option, to prevent deleting the existing content from the previous ingestion activity. Additionally, click on **Customer Care** to log a ticket, as shown in the preceding figure.


### Viewing Logs for a Migration Set {#viewing-logs-migration-set}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_logs"
>title="Viewing Logs"
>abstract="Upon completion of Extraction of Ingestion, Check the logs for any error/warnings. Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe support."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#troubleshooting" text="Troubleshooting"
>additional-url="https://helpx.adobe.com/ca/enterprise/admin-guide.html/ca/enterprise/using/support-for-experience-cloud.ug.html" text="Contacting Adobe Support"

Upon completion of each step (extraction and ingestion) check the logs and look for errors.  Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe support.

You can view logs for an existing migration set from the *Overview* page.
Follow the steps below:

1. Navigate to the *Overview* page and select the migration set that you want to delete and click **View Log** from the action bar.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/view-log1.png)

1. The **Logs** dialog box displays. Click **Extraction Logs** to view the logs in a new tab.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/view-log2.png)
Or,

   You can also view logs for your migration set from the *Overview* screen. Select the migration set and click the status under **EXTRACTION** field. In this case, click  **FINISHED** to view logs in a new tab.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/view-log3.png)

1. To tail the logs without using the user interface, you can SSH into your source AEM environment and tail the `crx-quickstart/cloud-migration/extraction-XXXXX/output.log file`.

### Deleting a Migration Set {#deleting-migration-set}

You can delete the migration set from the *Overview* page.
Follow the steps below:

1. Navigate to the *Overview* page and select the migration set that you want to delete and click **Delete** from the action bar.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/delete-1.png)

1. Click **Delete** from **Delete Migration Set** dialog box to confirm the deletion.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/delete-3.png)


## Running the Content Transfer Tool on a Publish instance {#running-ctt-on-publish}

It is recommended that while moving content to a Publish instance, CTT be installed on the source Publish instance to move content to the target Publish instance. Follow the recommended approach as described below:

* Use the same version of the CTT which was used on the Author instance.

* Only a single publish node needs to be migrated. It should be removed from the load balancer prior to beginning the extraction.

* When creating the migration set, use the URL of the author AEMaaCS environment.

* During ingestion to publish, the publish tier will NOT be scaled down (unlike the author). As a precaution, please avoid any user initiated write operations such as:

  * Content distribution from AEMaaCS Author to Publish in that environment
  * User Sync between publish instances


## Troubleshooting {#troubleshooting}

### Missing Blob IDs {#missing-blobs}

If there are missing blob ids reported, as mentioned below, then there is a need to execute a consistency check in the existing repository and restore the missing blobs.
`ERROR o.a.j.o.p.b.AbstractSharedCachingDataStore - Error retrieving record [ba45c53f8b687e7056c85dceebf8156a0e6abc7e]`

The following command is executed 

>[!NOTE]
>
>`--verbose` flag is required to report the node paths from where the blobs are referenced.

**For repositories AEM 6.5 (Oak 1.8 and below)**

```shell
java -jar oak-run.jar datastorecheck --consistency --store [<SEGMENT_STORE_PATH>|<MONGO_URI>] --[s3ds|fds] <DATASTORE_CFG> --verbose <OUT_DIR> --dump
```

**For repositories having Oak > 1.10**

```shell
java -jar oak-run.jar datastore --check-consistency [<SEGMENT_STORE_PATH>|<MONGO_URI>] --[s3ds|fds|azureds] <DATASTORE_CFG> --out-dir <OUT_DIR> --work-dir <TEMP_DIR> --verbose

```

Refer to [Oak Runnable Jar](https://github.com/apache/jackrabbit-oak/tree/trunk/oak-run) for more details.

The files created in the *OUT_DIR* specified above for consistency can then be checked for paths missing binaries and appropriate action taken like restoring from a backup, deleting the paths, re-indexing, and so on.


### UI Behavior {#ui-behavior}

As a user, you might see the following behavioral changes in the User Interface (UI) for Content Transfer Tool:

* The icons in the Content Transfer Tool UI may appear to be different from the screenshots shown in this guide or may not show up at all depending on the version of the source AEM instance.
