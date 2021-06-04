---
title: Overview to Content Transfer Tool
description: Overview to Content Transfer Tool
exl-id: 4715937e-4c4c-4680-af15-016db4fe7db9
---
# Overview {#overview-content-transfer-tool}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_overview"
>title="Overview"
>abstract="Content Transfer Tool is a tool developed by Adobe that can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance. This tool also transfers principals (users or groups) automatically."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#extraction-process" text="Extraction Process"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#ingestion-process" text="Ingestion Process"

The Content Transfer Tool is a tool developed by Adobe that can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance. 

This tool also transfers principals (users or groups) automatically. 

There are two phases associated with content transfer: 

1. **Extraction**:  Extraction refers to extracting content from the source AEM instance into a temporary area called *migration set*. A *migration set* is a cloud storage area provided by Adobe to temporarily store the transferred content between the source AEM instance and the Cloud Service AEM instance. 

   Refer to [Extraction Process in Content Transfer](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#extraction-process) for more details. 

>[!NOTE]
>
> It is recommended to run the User Mapping Tool as part of the Extraction phase. Refer to [Using User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#cloud-migration) for more details.

1. **Ingestion**: Ingestion refers to ingesting content from the *migration set* into the target Cloud Service instance. 

   Refer to [Ingestion Process in Content Transfer](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#ingestion-process) for more details.
  
A *migration set* has the following attributes:

* A maximum of ten migration sets can be created and maintained at a time during the content transfer activity. 
* Each migration set should have a unique name. 
* If a migration set has been inactive for more than 30 days, it will be automatically deleted.
* Whenever you create a migration set, it is associated with a specific environment. You can only ingest into an author or a publish instance of the same environment.


The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity. 

>[!NOTE]
>
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 

In the extraction phase, to ***top-up*** an existing migration set, the *overwrite* option must be disabled. Refer to [Top Up Extraction](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#top-up-extraction-process) for more details.

In the ingestion phase, to apply the delta content on top of the current content, the *wipe* option must be disabled. Refer to [Top Up Ingestion](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#top-up-ingestion-process) for more details.


## Guidelines and Best Practices {#best-practices}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_guidelines"
>title="Guidelines and Best Practices"
>abstract="Review guidelines and best practices to use the Content Transfer tool including revision cleanup tasks, Disk space considerations and more."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#pre-reqs" text="Important Considerations for using Content Transfer Tool"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#important-considerations" text="Important Considerations for using User Mapping Tool"

Follow the section below to understand guidelines and best practices to use the Content Transfer Tool:

* It is advisable to run [Revision Cleanup](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/deploying/revision-cleanup.html) and [data store consistency checks](https://helpx.adobe.com/experience-manager/kb/How-to-run-a-datastore-consistency-check-via-oak-run-AEM.html) on the **source** repository to identify potential problems and reduce the size of the repository.

* If the AEM Cloud Author Content Delivery Network (CDN) config is configured to have a whitelist of IPs then it should be ensured that the source environment IPs are also added to the allowlist so that the source environment and AEM Cloud environment can communicate with each other.

* In the ingestion phase, it is recommended to run the ingestion using the *wipe* mode enabled where the existing repository (author or publish) in the target AEM Cloud Service environment will be completely deleted and then updated with the migration set data. This mode is much faster than the non-wipe mode,  where the migration set is applied on top of the current content.

* After the content transfer activity is completed, the correct project structure is required in the Cloud Service environment to ensure that the content renders successfully in the Cloud Service environment.

* Before running the Content Transfer Tool, you must ensure that there is enough disk space in the `crx-quickstart` subdirectory of the source AEM instance. This is because the Content Transfer Tool creates a local copy of the repository that is later uploaded to the migration set. 
   The general formula to calculate the require free disk space is as follows:
   `data store size + node store size * 1.5`

     * *data store size*: the Content Transfer Tool uses 64 GB, even if the actual data store is larger.
     * *node store size*: segment store directory size or the MongoDB database size.
  Hence, for a segment store size of 20GB, the required free disk space would be 94GB.
  
* A migration set needs to be maintained throughout the content transfer activity to support content top-ups. Since a maximum of ten migration sets can be created and maintained at a time during the content transfer activity, it is recommended to break up the content repository accordingly to ensure that you do not run out of migration sets.