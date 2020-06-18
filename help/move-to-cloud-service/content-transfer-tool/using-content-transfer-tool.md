---
title: Using Content Transfer Tool
description: Using Content Transfer Tool
---

# Using Content Transfer Tool {#using-content-transfer-tool}

## Important Considerations for Using Content Transfer Tool {#pre-reqs}

Follow the section below to understand the important considerations while running the Content Transfer tool:

* The minimum system requirement for Content Transfer Tool is AEM 6.3 + and JAVA 8. If you are on a lower AEM version, you will need to upgrade your content repository to AEM 6.5 to use the Content Transfer Tool.

* If you are using a *Sandbox Environment*, ensure that your environment is upgraded to June 10 2020 Release or later. If you are using a *Production Environment*, it is automatically updated.

* To use the Content Transfer Tool, you will need to be an admin user on your source instance and belong to the AEM administrators group in the Cloud Service instance you are transferring content to. Unprivileged users will not be able to retrieve the access token to use the Content Transfer Tool.

* During the extraction phase, the Content Transfer Tool is executed on an active AEM source instance.

* The *Ingestion Phase* for the author will scale down the whole author deployment. This means that the author AEM will be unavailable during the whole ingestion process.

* The recommended upper limit for the repository size that the Content Transfer Tool can support at a time is 20GB.

## Availability {#availability}

The Content Transfer Tool can be downloaded as a zip file (Content Transfer Tool v1.0.0) from the Software Distribution Portal. You can install the package via Package Manager on your source Adobe Experience Manager (AEM) instance.

>[!NOTE]
>Download the Content Transfer Tool, from [Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html) portal.

## Running the Content Transfer Tool {#running-tool}

Follow this section to learn how to use Content Transfer Tool to migrate the content to AEM as a Cloud Service (Author/Publish):

1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **Content Transfer**.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/content1.png)

1. Click on **Create Migration Set** to create a new migration set. The **Content Migrations Set details** displays.

   >[!NOTE]
   >You will view the existing migration sets on this screen with their current status.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ctt-img4.png)

1. Populate the fields in **Content Migrations Set details** screen, as described below.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/content-3.png)
   

   1. **Name**: Enter the name of the migration set.
      >[!NOTE]
      >No special characters are allowed for the migration set name.

   1. **Cloud Service Configuration**: Enter the destination AEM as a Cloud Service Author URL.

      >[!NOTE]
      >You can create and maintain a maximum of four migration sets at a time during the content transfer activity.
      >Additionally, you have to create a migration separately for each of the specific environments - *Stage*, *Development*, or *Production*.

   1. **Access Token**: Enter the access token.

      >[!NOTE]
      >You can retrieve the access token from the author instance by navigating to `/libs/granite/migration/token.json`. The access token is retrieved from the Cloud Service author instance.

   1. **Parameters**: Select the following parameters to create the migration set:

      1. **Include Version**: Select as required.

      1. **Paths to be included**: Use path browser to select paths which need to be migrated.

         >[!IMPORTANT]
         >Following paths are restricted while creating a migration set:
         >* `/apps`
         >* `/libs`
         >* `/home`
         >* `/etc`

1. Click **Save** after you populate all the fields in the **Content Migrations Set details** screen.

1. You will view your migration set in the *Overview* page.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ctt-img4.png)

   All the the existing migration sets on this screen are displayed on the *Overview* page with their current status and status information.

   * A *red cloud* indicates that you cannot complete the extraction process.
   * A *green cloud* indicates that you can complete the complete the extraction process.
   * A *yellow icon* indicates that you did not create the existing migration set and the specific one is created by some other user in the same instance.

1. Select a migration set from overview page and click **Properties** to view or edit the migration set properties.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ctt-img6.png)

### Extraction Process in Content Transfer {#extraction-process}

Follow the steps below to extract your migration set from the Content Transfer Tool:

1. Select a migration set from *Overview* page and click **Extract** to start extraction.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/extraction-img1.png)

1. The **Migration Set extraction** dialog box displays and click on **Extract** to complete the extraction phase.

   >[!NOTE]
   >You have the option to overwrite staging container during the extraction phase.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/extract-2.png)

1. The **EXTRACTION** field now displays the **RUNNING** status for the extraction process that is in-progress.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/extract-3.png)

   Once the extraction is complete, the status of the migration set updates to **FINISHED** and a *solid green* cloud icon displays under the **INFO** field.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/extract-4.png)

   >[!NOTE]
   >You will have to refresh the page to view the updated status.
   >When extraction phase is started, write lock is created and released after *60 seconds*. So, if an extraction is stopped, you need to wait for a minute for lock to be released before starting extraction again.

#### Top-Up Extraction {#top-up-extraction-process}

The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 

Once the extraction process is complete, you can transfer delta content, by using the top-up extraction method. Follow the steps below:

1. Navigate to the *Overview* page and select the migration set for which you want to perform the top-up extraction.

1. Click **Extract** to start the top-up extraction.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/extraction-img1.png)

1. The **Migration Set extraction** dialog box displays.

   >[!IMPORTANT]
   >You should disable the **Overwrite staging container during extraction** option.
     ![image](/help/move-to-cloud-service/content-transfer-tool/assets/extract-topup-1.png)
 
### Ingestion Process in Content Transfer {#ingestion-process}

Follow the steps below to ingest your migration set from the Content Transfer Tool:

1. Select a migration set from *Overview* page and click **Ingest** to start extraction.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ingest-1.png)

1. The **Migration Set ingestion** dialog box displays.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ingest-2.png)

    For demonstration purposes, the option **Ingest content to Author instance** is disabled. It is possible to ingest content to Author and Publish at the same time.

    ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ingest-3.png)

   Click on **Ingest** to complete the ingestion phase.

1. Once the ingestion is complete, the status in **AUTHOR INGESTION** field updates to **FINISHED** and a solid green cloud icon displays under the **INFO**.
   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ingest-4.png)

   >[!NOTE]
   > You will have to refresh the page to view the updated status.

#### Top Up Ingestion {#top-up-ingestion-process}

The Content Transfer Tool has a feature that supports differential content *top-up* where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 

Once the ingestion process is complete, you can use delta content, by using the top-up ingestion method. Follow the steps below:

1. Navigate to the *Overview* page and select the migration set for which you want to perform the top-up ingestion.

1. Click **Ingest** to start the top-up extraction.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ingest-1.png)

1. The **Migration Set Ingestion** dialog box displays.

   >[!NOTE]
   >You should disable the *Wipe* option, to prevent deleting the existing content from the previous ingestion activity.
     ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ingest-topup-1.png)

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
> `--verbose` flag is required to report the node paths from where the blobs are referenced.

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


