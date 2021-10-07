---
title: Using Content Transfer Tool
description: Using Content Transfer Tool
exl-id: a19b8424-33ab-488a-91b3-47f0d3c8abf5
---
# Using Content Transfer Tool {#using-content-transfer-tool}

## Important Considerations for Using Content Transfer Tool {#pre-reqs}

Follow the section below to understand the important considerations while running the Content Transfer tool:

* The minimum system requirement for Content Transfer Tool is AEM 6.3 + and JAVA 8. If you are on a lower AEM version, you need to upgrade your content repository to AEM 6.5 to use the Content Transfer Tool.

* Java must be configured on the AEM environment, so that the `java` command can be executed by the user who starts AEM.

* It is recommended to uninstall older versions of the Content Transfer Tool when installing the version 1.3.0 because there was a major architectural change in the tool. With 1.3.0, you should also create new migration sets and re-run extraction and ingestion on the new migration sets.

* The Content Transfer Tool can be used with the following types of Data Store: File Data Store, S3 Data Store, Shared S3 Data Store, and Azure Blob Store Data Store.

* If you are using a *Sandbox Environment*, ensure that your environment is current and upgraded to the latest release. If you are using a *Production Environment*, it is automatically updated.

* To use the Content Transfer Tool, you need to be an admin user on your source instance and belong to the local AEM **administrators** group in the Cloud Service instance you are transferring content to. Unprivileged users will not be able to retrieve the access token to use the Content Transfer Tool. 

* If the setting **Wipe existing content on Cloud instance before ingestion** option is enabled, it deletes the entire existing repository and creates a new repository to ingest content into. This means that it resets all settings including permissions on the target Cloud Service instance. This is also true for an admin user added to the **administrators** group. User must need to be re-added to the **administrators** group to retrieve the access token for CTT.   

* The access token can expire periodically either after a specific time period or after the Cloud Service environment has been upgraded. If access token has expired, you will not be able to connect to the Cloud Service instance and you need to retrieve the new access token. The status icon associated with an existing migration set will change to a red cloud and will display a message when you hover over it.

* The Content Transfer Tool (CTT) does not perform any kind of content analysis before transferring content from the source instance to the target instance. For example, CTT does not differentiate between published and unpublished content while ingesting content into a Publish environment. Whatever content is specified in the migration set will be ingested into the chosen target instance. User has the ability to ingest a migration set into an Author instance or Publish instance or both. It is recommended that while moving content to a Production instance, CTT be installed on the source Author instance to move content to the target Author instance and similarly, install CTT on the source Publish instance to move content to the target Publish instance. Refer to [Running the Content Transfer Tool on a Publish instance](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#running-ctt-on-publish) for more details.

* The Users and Groups transferred by the Content Transfer Tool are only those that are required by the content to satisfy permissions. The *Extraction* process copies the entire `/home` into the migration set and the *Ingestion* process copies all users and groups referenced in the migrated content ACLs. To automatically map the existing users and groups to their IMS IDs, please refer to [Using User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#cloud-migration).

* During the extraction phase, the Content Transfer Tool is executed on an active AEM source instance.

* After completing the *Extraction* phase of the content transfer process and before starting the *Ingestion Phase* to ingest content into your AEM as a Cloud Service *Stage* or *Production* instances, you will need to log a support ticket to notify Adobe of your intention to run *Ingestion* so that Adobe can ensure that no interruptions occur during the *Ingestion* process. You will need to log the support ticket 1 week prior to your planned *Ingestion* date. Once, you've submitted the support ticket, the support team will provide guidance on next steps. You can log a support ticket with the following details:

   * Exact date and estimated time (with your time-zone) when you plan to start the *Ingestion* phase. 
   * Environment type (Stage or Production) that you plan to ingest data into.
   * Program ID.

* The *Ingestion Phase* for the author scales down the whole author deployment. This means that the author AEM will be unavailable during the whole ingestion process. Please also ensure that no Cloud Manager pipelines are executed while you are running the *Ingestion* phase. 

* When using `Amazon S3` or `Azure` as the data store on the source AEM system, the data store should be configured so that the blobs stored cannot be deleted (garbage collected). This ensures integrity of index data and failure to configure this way may result in failed extractions due to lack of integrity of this index data.

* If you are using custom indexes, you must ensure to configure  the custom indexes with `tika` node before running Content Transfer Tool. Refer to [Preparing the New Index Definition](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/indexing.html?lang=en#preparing-the-new-index-definition) for more details.

* If you intend to do top ups, it is essential that the content structure of existing content is not changed from the time the initial extraction is taken to when the top-up extraction is run. Top-ups cannot be run on content whose structure has been changed since the initial extraction. Please ensure you restrict this during the migration process.

* If you intend to include versions as part of a migration set, and are performing top-ups with `wipe=false`, then you must disable version purging due to a current limitation in the Content Transfer Tool. If you prefer to keep version purge enabled and are performing top-ups into a migration set, then you must perform the ingestion as `wipe=true`.

## Availability {#availability}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_download"
>title="Download"
>abstract="The Content Transfer Tool can be downloaded as a zip file from the Software Distribution Portal. You can install the package via Package Manager on your source Adobe Experience Manager (AEM) instance. Make sure to download the latest version."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html" text="Release Notes"
>additional-url="https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html" text="Software Distribution Portal"

The Content Transfer Tool can be downloaded as a zip file from the Software Distribution Portal. You can install the package via Package Manager on your source Adobe Experience Manager (AEM) instance. Make sure to download the latest version. For more details on the latest version, refer to [Release Notes](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html).

>[!NOTE]
>Download the Content Transfer Tool, from [Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html) portal.

## Running the Content Transfer Tool {#running-tool}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_demo"
>title="Running Content Transfer Tool"
>abstract="Learn how to use Content Transfer Tool to migrate the content to AEM as a Cloud Service (Author/Publish)."
>additional-url="https://video.tv.adobe.com/v/35460/?quality=12&learn=on" text=" See Demo"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/migration/content-transfer-tool.html?lang=en#migration" text="Tutorial - using Content Transfer Tool"

>[!VIDEO](https://video.tv.adobe.com/v/35460/?quality=12&learn=on)


Follow this section to learn how to use Content Transfer Tool to migrate the content to AEM as a Cloud Service (Author/Publish):

1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **Content Migration**.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ctt-entry-card01.png)

1. Select the **Content Transfer** option from **Content Migration** wizard.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/ctt-entry-card02.png)


1. The console below appears when you create the first migration set. Click on **Create Migration Set** to create a new migration set. 

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/01-create-migrationset.png)
   
   
   >[!NOTE]
   >If you have existing migration sets, the console will display the list of existing migration sets with their current status.

   Additionally, click on **Create User Mapping Config** to access the [User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#using-user-mapping-tool).

1. Populate the fields in **Create Migration Set** screen, as described below.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/migration-set-creation-04.png)
   
   1. **Name**: Enter the name of the migration set.
      >[!NOTE]
      >No special characters are allowed for the migration set name.

   1. **Cloud Service Configuration**: Enter the destination AEM as a Cloud Service Author URL.

      >[!NOTE]
      >You can create and maintain a maximum of ten migration sets at a time during the content transfer activity.
      >Additionally, you have to create a migration separately for each of the specific environments - *Stage*, *Development*, or *Production*.

   1. **Access Token**: Enter the access token.

      >[!NOTE]
      >You can retrieve the access token by using the **Open access token** button. You need to ensure that you belong to the AEM administrators' group in the target Cloud Service instance.

   1. **Parameters**: Select the following parameters to create the migration set:

      1. **Include Version**: Select as required. When versions are included, the path `/var/audit` is automatically included to migrate audit events.

      >[!NOTE]
      >If you intend to include versions as part of a migration set, and are performing top-ups with `wipe=false`, then you must disable version purging due to a current limitation in the Content Transfer Tool. If you prefer to keep version purge enabled and are performing top-ups into a migration set, then you must perform the ingestion as `wipe=true`.

      1. **Include Mapping from IMS Users and Groups**: Select the option to include mapping from IMS Users and Groups. 
      Refer to [User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html) for more details.

      1. **Paths to be included**: Use path browser to select paths which need to be migrated. Path picker accepts input by typing or by selection.

         >[!IMPORTANT]
         >Following paths are restricted while creating a migration set:
         >* `/apps`
         >* `/libs`
         >* `/home`
         >* `/etc` (some `/etc` paths are allowed to be selected in CTT)

1. Click **Save** after you populate all the fields in the **Create Migration Set** details screen.

1. You will view your migration set in the *Overview* page.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/04-item-selection-and-quick-actions.png)

   All the existing migration sets on this screen are displayed on the *Overview* page with their current status and status information. You may see some of these icons described below.

   * A *red cloud* indicates that you cannot complete the extraction process.
   * A *green cloud* indicates that you can complete the extraction process.
   * A *yellow icon* indicates that you did not create the existing migration set and the specific one is created by some other user in the same instance.

1. Select a migration set from overview page and click **Properties** to view or edit the migration set properties. While editing properties, it is not possible to change the container name or the service URL. 


### Extraction Process in Content Transfer {#extraction-process}

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

#### Top-Up Extraction {#top-up-extraction-process}

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

### Ingestion Process in Content Transfer {#ingestion-process}

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

#### Top Up Ingestion {#top-up-ingestion-process}

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
