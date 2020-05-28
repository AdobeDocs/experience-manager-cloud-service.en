---
title: Overview to Content Transfer Tool
description: Overview to Content Transfer Tool
---

# Overview {#overview-content-transfer-tool}

The Content Transfer Tool is a tool developed by Adobe that can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance. 

This tool also transfers principals (users or groups) automatically. 

There are two phases associated with content transfer: 

1. **Extraction**:  Extraction refers to extracting content from the source AEM instance into a temporary area called *migration set*. A *migration set* is a cloud storage area provided by Adobe to temporarily store the transferred content between the source AEM instance and the Cloud Service AEM instance. 

   Refer to [Extraction Process in Content Transfer](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#extraction-process) for more details.

2. **Ingestion**: Ingestion refers to ingesting content from the *migration set* into the target Cloud Service instance. 

   Refer to [Ingestion Process in Content Transfer](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#ingestion-process) for more details.
  
A *migration set* has the following attributes:

* A maximum of four migration sets can be created and maintained at a time during the content transfer activity.
* Each migration set should have a unique name. 
* If a migration set has been inactive for more than 30 days, it will be automatically deleted.
* Whenever you create a migration set, it is associated with a specific environment. You can only ingest into an author or a publish instance of the same environment.

The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity. 

>[!NOTE]
> After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 

In the extraction phase, to ***top-up*** an existing migration set, the *overwrite* option must be disabled. Refer to [Top Up Extraction](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#top-up-extraction-process) for more details.

In the ingestion phase, to apply the delta content on top of the current content, the *wipe* option must be disabled. Refer to [Top Up Ingestion](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md#top-up-ingestion-process) for more details.


## Guidelines and Best Practices {#best-practices}

Follow the section below to understand guidelines and best practices to use the Content Transfer Tool:

* It is advisable to run compaction, data store consistency checks on the repositories before hand to spot potential problems and also reduce the garbage present in the repository. 

* If the AEM Cloud Author Content Delivery Network (CDN) config is configured to have a whitelist of IPs then it should be ensured that the source environment IPs are also added to the whitelist so that the source environment and AEM Cloud environment can communicate with each other.

* In the ingestion phase, it is recommended to run the ingestion using the *wipe* mode enabled where the existing repository (author or publish) in the target AEM Cloud Service environment will be completely deleted and then updated with the migration set data. This mode is much faster than the non-wipe mode,  where the migration set is applied on top of the current content.

* After the content transfer activity is completed, the correct project structure is required in the Cloud Service environment to ensure that the content renders successfully in the Cloud Service environment.