---
title: Guidelines and best practices for using the Content Transfer Tool
description: Learn the guidelines and best practices for using the Content Transfer Tool.
exl-id: d1975c34-85d4-42e0-bb1a-968bdb3bf85d
feature: Migration
role: Admin
---

# Guidelines and  Best Practices for using Content Transfer Tool {#guidelines}

## Guidelines and Best Practices {#best-practices}

<!-- Alexandru: hiding for now

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_guidelines"
>title="Guidelines and Best Practices"
>abstract="Review guidelines and best practices to use the Content Transfer tool including revision cleanup tasks, Disk space considerations and more."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html" text="Important Considerations for using Content Transfer Tool"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/group-migration.md#important-considerations" text="Important Considerations when Migrating Groups" 

-->

The Content Transfer Tool integrates the content transfer process with Cloud Acceleration Manager. It is required to use this version (2.0 or later, but version 3.0 is now recommended) to gain all the benefits it provides:

* Self-service way to extract a migration set once and ingest it into multiple environments in parallel
* Improved user experience by way of better loading states, guardrails, and error handling 
* Ingestion logs are persisted and are always available for troubleshooting

To start using the newest version, uninstall older versions of the Content Transfer Tool. With version 2.0 and later, you create migration sets and rerun extraction and ingestion on the sets.
Versions earlier than 2.0.0 are not supported, and it is advised that you use the most recent version.

The following Guidelines and Best Practices apply to the new version of the Content Transfer Tool:

* Run [Revision Cleanup](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/deploying/revision-cleanup.html) and [data store consistency checks](https://experienceleague.adobe.com/docs/experience-cloud-kcs/kbarticles/KA-16550.html) on the **source** repository so you can identify potential problems and reduce the size of the repository.

* In the ingestion phase, Adobe recommends that you run the ingestion using the *wipe* mode enabled where the existing repository (Author or Publish) in the target Adobe Experience Manager (AEM) Cloud Service environment is deleted. Then, update with the migration set data. This mode is faster than the non-wipe mode,  where the migration set is applied on top of the current content.

* After the content transfer activity is completed, the correct project structure is required in the Cloud Service environment to ensure that the content renders successfully in the Cloud Service environment.

* Before running the Content Transfer Tool, you must ensure that there is enough disk space in the `crx-quickstart` subdirectory of the source AEM instance. This is because the Content Transfer Tool creates a local copy of the repository that is later uploaded to the migration set. 
   The general formula to calculate the required free disk space is as follows:
   `data store size + node store size * 1.5`

* *data store size*: the Content Transfer Tool uses 64 GB, even if the actual data store is larger.
* *node store size*: segment store directory size or the MongoDB database size.
Hence, for a segment store size of 20 GB, the required free disk space would be 94 GB.
  
* A migration set must be maintained throughout the content transfer activity to support content top-ups. A maximum of 10 migration sets per project in Cloud Acceleration Manager can be created and maintained at a time during the content transfer activity. If more than 10 migration sets are needed, create a second project in Cloud Acceleration Manager. However, this requires additional project management and out-of-product governance to avoid overwriting content on the target by multiple users.

* Avoid altering the installation directory of the CTT tool. By default, the installation takes place in the crx-quickstart/cloud-migration path. This specific location is internally used by other libraries. Modifying this path can result in extraction issues.

## Important Considerations Before Using Content Transfer Tool {#important-considerations}

Follow the section below to understand the important considerations while running the Content Transfer tool:

* The minimum system requirement for Content Transfer Tool is AEM 6.3 + and Java&trade; 8. If you are on a lower AEM version, upgrade your content repository to AEM 6.5 to use the Content Transfer Tool.

* Java&trade; must be configured on the AEM environment, so that the `java` command can be executed by the user who starts AEM.

* The Content Transfer Tool can be used with the following types of Data Store: File Data Store, S3 Data Store, Shared S3 Data Store, and Azure Blob Store Data Store.

* If you are using a *Sandbox Environment*, ensure that your environment is current and upgraded to the latest release. If you are using a *Production Environment*, it is automatically updated.

* To start an ingestion, you must belong to the local AEM **administrators** group in the Cloud Service instance you are transferring content to. Unprivileged users cannot start ingestions without manually providing the migration token.

* If the setting **Wipe existing content on Cloud instance before ingestion** option is enabled, it deletes the entire existing repository and creates a new repository to ingest content into. This means that it resets all settings including permissions on the target Cloud Service instance. It is also true for an admin user added to the **administrators** group. The user must be readded to the **administrators** group to retrieve the access token for the Content Transfer Tool.

* The extraction key is valid for 14 days from the time that it was created or renewed. It can be renewed at any time. If the extraction key has expired, you cannot perform an extraction.

* The Content Transfer Tool (CTT) does not perform any kind of content analysis before transferring content from the source instance to the target instance. For example, CTT does not differentiate between published and unpublished content while ingesting content into a Publish environment. Whatever content is specified in the migration set is ingested into the chosen target instance. A user can ingest a migration set into an Author instance or Publish instance or both. Adobe recommends that while moving content to a Production instance, CTT be installed on the source Author instance to move content to the target Author instance. And, similarly, install CTT on the source Publish instance to move content to the target Publish instance. See [Running the Content Transfer Tool on a Publish instance](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html#running-tool) for more details.

* The groups transferred by the Content Transfer Tool are only those groups that are required by the content to satisfy permissions. The _Extraction_ process copies the entire `/home/groups` into the migration set. For more information, see [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md). The _Ingestion_ process copies all groups referenced in the migrated content ACLs. See [Migrating Closed User Groups](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/closed-user-groups-migration.md) for extra considerations for groups used in a Closed User Group (CUG) policy.

* During the extraction phase, the Content Transfer Tool is executed on an active AEM source instance.

* The *Ingestion Phase* for the Author scales down the whole Author deployment. It means that the Author AEM is unavailable during the whole ingestion process. Also ensure that no Cloud Manager pipelines are executed while you are running the *Ingestion* phase. 

* When using `Amazon S3` or `Azure` as the data store on the source AEM system, the data store should be configured so that the blobs stored cannot be deleted (garbage collected). This ensures integrity of index data and failure to configure this way may result in failed extractions due to lack of integrity of this index data.

* If you are using custom indexes, you must ensure to configure  the custom indexes with `tika` node before running Content Transfer Tool. See [Preparing the New Index Definition](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/operations/indexing.html#preparing-the-new-index-definition) for more details.

* If you intend to do top-ups, the content structure of existing content must not change from the time the initial extraction is taken to when the top-up extraction is run. Top-ups cannot be run on content whose structure has been changed since the initial extraction. Ensure that you restrict this during the migration process.

* If you intend to include versions as part of a migration set, and are performing top-ups with `wipe=false`, then you must disable version purging due to a current limitation in the Content Transfer Tool. If you prefer to keep version purge enabled and are performing top-ups into a migration set, then you must perform the ingestion as `wipe=true`.

* The Content Transfer Tool (CTT) does not support merge ingestions. To consolidate content from multiple systems into a single Cloud Service instance, only versions from one source system can be migrated. This process requires the use of migrations with the wipe=false parameter, which may result in extended ingestion times due to the incremental nature of the operation. If possible, consolidate content onto a single source systems before beginning your migration to eliminate the need to merge content.

* A migration set expires after a prolonged period of inactivity, after which its data is no longer available. Review [Migration Set Expiry](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html#migration-set-expiry) for more details.

## What's Next {#whats-next}

Once you have learned the guidelines, best practices, and the important considerations for using Content Transfer Tool, you are now ready to install and use the tool, starting with creation of a migration set. See [Getting Started with Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/getting-started-content-transfer-tool.md).
