---
title: Guidelines and  Best Practices for using Content Transfer Tool
description: Guidelines and  Best Practices for using Content Transfer Tool
exl-id: d1975c34-85d4-42e0-bb1a-968bdb3bf85d
---
# Guidelines and  Best Practices for using Content Transfer Tool {#guidelines}

## Guidelines and Best Practices {#best-practices}

<!-- Alexandru: hiding for now

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_guidelines"
>title="Guidelines and Best Practices"
>abstract="Review guidelines and best practices to use the Content Transfer tool including revision cleanup tasks, Disk space considerations and more."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html" text="Important Considerations for using Content Transfer Tool"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/user-mapping-and-migration.md#important-considerations" text="Important Considerations when Mapping and Migrating Users" 

-->

A new version of the Content Transfer Tool is available which integrates the content transfer process with Cloud Acceleration Manager. It is highly recommended to switch over to this new version to use all the benefits it provides:

* Self-service way to extract a migration set once and ingest it into multiple environments in parallel
* Improved user experience via better loading states, guardrails, and error handling 
* Ingestion logs are persisted and are always available for troubleshooting

To start using the new version you will need to uninstall older versions of the Content Transfer Tool. This is needed because the new version comes with a major architectural change. With version 2.x, you will need to create new migration sets and re-run extraction and ingestion on the new migration sets.
Versions earlier than 2.0.0 will no longer be supported, and it is advisable to use the most recent version.

The following Guidelines and Best Practices apply to the new version of the Content Transfer Tool:

* It is advisable to run [Revision Cleanup](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/deploying/revision-cleanup.html) and [data store consistency checks](https://helpx.adobe.com/experience-manager/kb/How-to-run-a-datastore-consistency-check-via-oak-run-AEM.html) on the **source** repository to identify potential problems and reduce the size of the repository.

* In the ingestion phase, it is recommended to run the ingestion using the *wipe* mode enabled where the existing repository (author or publish) in the target AEM Cloud Service environment is completely deleted and then updated with the migration set data. This mode is much faster than the non-wipe mode,  where the migration set is applied on top of the current content.

* After the content transfer activity is completed, the correct project structure is required in the Cloud Service environment to ensure that the content renders successfully in the Cloud Service environment.

* Before running the Content Transfer Tool, you must ensure that there is enough disk space in the `crx-quickstart` subdirectory of the source AEM instance. This is because the Content Transfer Tool creates a local copy of the repository that is later uploaded to the migration set. 
   The general formula to calculate the required free disk space is as follows:
   `data store size + node store size * 1.5`

     * *data store size*: the Content Transfer Tool uses 64 GB, even if the actual data store is larger.
     * *node store size*: segment store directory size or the MongoDB database size.
  Hence, for a segment store size of 20GB, the required free disk space would be 94GB.
  
* A migration set needs to be maintained throughout the content transfer activity to support content top-ups. A maximum of twenty migration sets per project in Cloud Acceleration Manager can be created and maintained at a time during the content transfer activity. If more than twenty migration sets are needed, you will need to create a second project in Cloud Acceleration Manager. However, this will require additional project management and out-of-product governance to avoid overwriting content on the target by multiple users.

* Avoid altering the installation directory of the CTT tool. By default, the installation takes place in the crx-quickstart/cloud-migration path. This specific location is internally utilized by other libraries. Modifying this path can result in extraction issues.

## Important Considerations Before Using Content Transfer Tool {#important-considerations}

Follow the section below to understand the important considerations while running the Content Transfer tool:

* The minimum system requirement for Content Transfer Tool is AEM 6.3 + and JAVA 8. If you are on a lower AEM version, you need to upgrade your content repository to AEM 6.5 to use the Content Transfer Tool.

* Java must be configured on the AEM environment, so that the `java` command can be executed by the user who starts AEM.

* The Content Transfer Tool can be used with the following types of Data Store: File Data Store, S3 Data Store, Shared S3 Data Store, and Azure Blob Store Data Store.

* If you are using a *Sandbox Environment*, ensure that your environment is current and upgraded to the latest release. If you are using a *Production Environment*, it is automatically updated.

* To start an ingestion, you need to belong to the local AEM **administrators** group in the Cloud Service instance you are transferring content to. Unprivileged users will not be able to start ingestions without manually providing the migration token.

* If the setting **Wipe existing content on Cloud instance before ingestion** option is enabled, it deletes the entire existing repository and creates a new repository to ingest content into. This means that it resets all settings including permissions on the target Cloud Service instance. This is also true for an admin user added to the **administrators** group. The user must be re-added to the **administrators** group to retrieve the access token for the Content Transfer Tool.

* Ingestions do not support merging content from multiple sources into the target Cloud Service instance if the content from the two sources is moved to the same paths on the target. To move content from multiple sources into a single target Cloud Service instance, you need to ensure that there is no overlap of the content paths from the sources.

* The extraction key is valid for 14 days from the time it was created/renewed. It can be renewed at any time. If the extraction key has expired, you will not be able to perform an extraction.

* The Content Transfer Tool (CTT) does not perform any kind of content analysis before transferring content from the source instance to the target instance. For example, CTT does not differentiate between published and unpublished content while ingesting content into a Publish environment. Whatever content is specified in the migration set is ingested into the chosen target instance. User has the ability to ingest a migration set into an Author instance or Publish instance or both. It is recommended that while moving content to a Production instance, CTT be installed on the source Author instance to move content to the target Author instance and similarly, install CTT on the source Publish instance to move content to the target Publish instance. See [Running the Content Transfer Tool on a Publish instance](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html#running-tool) for more details.

* The Users and Groups transferred by the Content Transfer Tool are only those that are required by the content to satisfy permissions. The _Extraction_ process copies the entire `/home` into the migration set, and it does User Mapping by adding a field made from each user's email address. For more information, see [User Mapping and Principal Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/user-mapping-and-migration.md). The _Ingestion_ process copies all users and groups referenced in the migrated content ACLs. See [Migrating Closed User Groups](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/closed-user-groups-migration.md) for extra considerations for groups used in a Closed User Group (CUG) policy.

* During the extraction phase, the Content Transfer Tool is executed on an active AEM source instance.

* After completing the *Extraction* phase of the content transfer process and before starting the *Ingestion Phase* to ingest content into your AEM as a Cloud Service *Stage* or *Production* instances, you will need to log a support ticket to notify Adobe of your intention to run *Ingestion* so that Adobe can ensure that no interruptions occur during the *Ingestion* process. You will need to log the support ticket 1 week prior to your planned *Ingestion* date. After you have submitted the support ticket, the support team provides guidance on next steps. You can log a support ticket with the following details:

   * Exact date and estimated time (with your time-zone) when you plan to start the *Ingestion* phase. 
   * Environment type (Stage or Production) that you plan to ingest data into.
   * Program ID.

* The *Ingestion Phase* for the author scales down the whole author deployment. It means that the author AEM is unavailable during the whole ingestion process. Also ensure that no Cloud Manager pipelines are executed while you are running the *Ingestion* phase. 

* When using `Amazon S3` or `Azure` as the data store on the source AEM system, the data store should be configured so that the blobs stored cannot be deleted (garbage collected). This ensures integrity of index data and failure to configure this way may result in failed extractions due to lack of integrity of this index data.

* If you are using custom indexes, you must ensure to configure  the custom indexes with `tika` node before running Content Transfer Tool. See [Preparing the New Index Definition](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/indexing.html#preparing-the-new-index-definition) for more details.

* If you intend to do top ups, it is essential that the content structure of existing content is not changed from the time the initial extraction is taken to when the top-up extraction is run. Top-ups cannot be run on content whose structure has been changed since the initial extraction. Ensure that you restrict this during the migration process.

* If you intend to include versions as part of a migration set, and are performing top-ups with `wipe=false`, then you must disable version purging due to a current limitation in the Content Transfer Tool. If you prefer to keep version purge enabled and are performing top-ups into a migration set, then you must perform the ingestion as `wipe=true`.

* A migration set will expire after a prolonged period of inactivity, after which its data will no longer be available. Review [Migration Set Expiry](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html#migration-set-expiry) for more details.

## What's Next {#whats-next}

Once you have learned the guidelines, best practices, and the important considerations for using Content Transfer Tool, you are now ready to install and use the tool, starting with creation of a migration set. See [Getting Started with Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/getting-started-content-transfer-tool.md) to learn more.
