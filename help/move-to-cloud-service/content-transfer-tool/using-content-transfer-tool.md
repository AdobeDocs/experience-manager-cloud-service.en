---
title: Using Content Transfer Tool
description: Using Content Transfer Tool
---

# Using Content Transfer Tool {#using-content-transfer-tool}

## Important Considerations for Using Content Transfer Tool {#pre-reqs}

Follow the section below to understand the important considerations while running the Content Transfer tool:

* The minimum system requirement for Content Transfer Tool is AEM 6.3 + and JAVA 8. If you are on a lower AEM version, you will need to upgrade your content repository to AEM 6.5 to use the Content Transfer Tool.

* The Content Transfer Tool can be used with the following types of Data Store: File Data Store, S3 Data Store, Shared S3 Data Store, and Azure Blob Store Data Store.

* If you are using a *Sandbox Environment*, ensure that your environment is current and upgraded to the latest release. If you are using a *Production Environment*, it is automatically updated.

* To use the Content Transfer Tool, you will need to be an admin user on your source instance and belong to the local AEM administrators group in the Cloud Service instance you are transferring content to. Unprivileged users will not be able to retrieve the access token to use the Content Transfer Tool.

* During the extraction phase, the Content Transfer Tool is executed on an active AEM source instance.

* The *Ingestion Phase* for the author will scale down the whole author deployment. This means that the author AEM will be unavailable during the whole ingestion process.

* Currently the default MongoDB size for a AEM as a Cloud Service Author instance is 32GB. It is recommended that for segment store size of greater than 20GB, you should submit a Support ticket to increase the MongoDB size.

## Availability {#availability}

The Content Transfer Tool can be downloaded as a zip file from the Software Distribution Portal. You can install the package via Package Manager on your source Adobe Experience Manager (AEM) instance. Make sure to download the latest version. For more details on the latest version, refer to [Release Notes](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html).

>[!NOTE]
>Download the Content Transfer Tool, from [Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html) portal.

## Running the Content Transfer Tool {#running-tool}

>[!VIDEO](https://video.tv.adobe.com/v/35460/?quality=12&learn=on)

Follow this section to learn how to use Content Transfer Tool to migrate the content to AEM as a Cloud Service (Author/Publish):

1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **Content Transfer**.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/content1.png)

1. The console below appears when you create the first migration set. Click on **Create Migration Set** to create a new migration set. 

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/01-migration-set-overview.png)
   
   >[!NOTE]
   >If you have existing migration sets, the console will display the list of existing migration sets with their current status.

1. Populate the fields in **Content Migrations Set details** screen, as described below.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/02-migration-set-creation.png)
   

   1. **Name**: Enter the name of the migration set.
      >[!NOTE]
      >No special characters are allowed for the migration set name.

   1. **Cloud Service Configuration**: Enter the destination AEM as a Cloud Service Author URL.

      >[!NOTE]
      >You can create and maintain a maximum of four migration sets at a time during the content transfer activity.
      >Additionally, you have to create a migration separately for each of the specific environments - *Stage*, *Development*, or *Production*.

   1. **Access Token**: Enter the access token.

      >[!NOTE]
      >You can retrieve the access token by using the **Open access token** button. You need to ensure that you belong to the AEM administrators group in the target Cloud Service instance.

   1. **Parameters**: Select the following parameters to create the migration set:

      1. **Include Version**: Select as required.

      1. **Paths to be included**: Use path browser to select paths which need to be migrated. Path picker accepts input by typing or by selection.

         >[!IMPORTANT]
         >Following paths are restricted while creating a migration set:
         >* `/apps`
         >* `/libs`
         >* `/home`
         >* `/etc`

1. Click **Save** after you populate all the fields in the **Content Migrations Set details** screen.

1. You will view your migration set in the *Overview* page.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/04-item-selection-and-quick-actions.png)

   All the the existing migration sets on this screen are displayed on the *Overview* page with their current status and status information. You may see some of these icons described below.

   * A *red cloud* indicates that you cannot complete the extraction process.
   * A *green cloud* indicates that you can complete the complete the extraction process.
   * A *yellow icon* indicates that you did not create the existing migration set and the specific one is created by some other user in the same instance.

1. Select a migration set from overview page and click **Properties** to view or edit the migration set properties. While editing properties, it is not possible to change the container name or the service URL. 

   

### Extraction Process in Content Transfer {#extraction-process}

Follow the steps below to extract your migration set from the Content Transfer Tool:

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

#### Top-Up Extraction {#top-up-extraction-process}

The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 

Once the extraction process is complete, you can transfer delta content, by using the top-up extraction method. Follow the steps below:

1. Navigate to the *Overview* page and select the migration set for which you want to perform the top-up extraction. Click **Extract** to start the top-up extraction. The **Migration Set extraction** dialog box displays.

   >[!IMPORTANT]
   >You should disable the **Overwrite staging container during extraction** option.
     ![image](/help/move-to-cloud-service/content-transfer-tool/assets/11-topup-extraction.png)
 
### Ingestion Process in Content Transfer {#ingestion-process}

Follow the steps below to ingest your migration set from the Content Transfer Tool:

1. Select a migration set from *Overview* page and click **Ingest** to start extraction. The **Migration Set ingestion** dialog box displays. Click on **Ingest** to start the ingestion phase. For demonstration purposes, the option **Ingest content to Author instance** is disabled. It is possible to ingest content to Author and Publish at the same time.  

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/12-content-ingestion.png)    
   

1. Once the ingestion is complete, the status in **PUBLISH INGESTION** field updates to **FINISHED**.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/15-ingestion-complete.png)

   
#### Top Up Ingestion {#top-up-ingestion-process}

The Content Transfer Tool has a feature that supports differential content *top-up* where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 

Once the ingestion process is complete, you can use delta content, by using the top-up ingestion method. Follow the steps below:

1. Navigate to the *Overview* page and select the migration set for which you want to perform the top-up ingestion. Click **Ingest** to start the top-up extraction. The **Migration Set Ingestion** dialog box displays. 

   >[!IMPORTANT]
   >You should disable the **Wipe existing content on Cloud instance before ingestion** option, to prevent deleting the existing content from the previous ingestion activity.
     ![image](/help/move-to-cloud-service/content-transfer-tool/assets/16-topup-ingestion.png)

### Viewing Logs for a Migration Set {#viewing-logs-migration-set}

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

* User creates a migration set for an author URL (Development/Stage/Production) and successfully performs extraction and ingestion.

* User then creates a new migration set for the same Author URL and performs extraction and ingestion on the new migration set. The UI shows that the ingestion status of the first migration set changes to **FAILED** and no logs are available.

* This does not mean that the ingestion for the first migration set failed. This behavior is seen because when a new ingestion job is started, it deletes the previous ingestion job. Hence, the changes status on the first migration set should be ignored.

* The icons in the Content Transfer Tool UI may appear to be different from the screenshots shown in this guide or may not show up at all depending on the version of the source AEM instance.


