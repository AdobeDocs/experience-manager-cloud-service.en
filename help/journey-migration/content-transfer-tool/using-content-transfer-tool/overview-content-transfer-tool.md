---
title: Overview to Content Transfer Tool
description: Learn how to use the Content Transfer Tool to transfer content from an on-premise AEM instance to AEM as a Cloud Service
exl-id: cfc0366a-2139-4d9d-b5bc-0b65bef4013c
feature: Migration
role: Admin
---

# Overview {#overview-content-transfer-tool}

>[!CONTEXTUALHELP] 
>id="aemcloud_ctt_overview" 
>title="Overview" 
>abstract="Content Transfer Tool is a tool developed by Adobe that can be used to initiate the migration of existing content from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance. This tool also transfers groups automatically."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/guidelines-best-practices-content-transfer-tool.html" text="Guidelines and Best Practices"

The Content Transfer Tool is a tool developed by Adobe that can be used to initiate the migration of existing content from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance. 

This tool also transfers groups automatically.  See [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md) for more information.

The Content Transfer Tool integrates the content transfer process with Cloud Acceleration Manager. This empowers the user with all the benefits it provides:

* Self-service way to extract a migration set once and ingest it into multiple environments in parallel
* Improved user experience via better loading states, guardrails and error handling
* Ingestion logs are persisted and are always available for troubleshooting
* Validation and Principal migration reports are available for validating

## Phases in Content Transfer Tool {#phases-content-transfer-tool}

There are two phases associated with content transfer: 

1. **Extraction**:  Extraction refers to extracting content from the source AEM instance into a temporary area called *migration set*. A *migration set* is a cloud storage area provided by Adobe to temporarily store the transferred content between the source AEM instance and the Cloud Service AEM instance. 

   See [Extraction Process in Content Transfer](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md) for more details.

1. **Ingestion**: Ingestion refers to ingesting content from the *migration set* into the target Cloud Service instance. 

   See [Ingestion Process in Content Transfer](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md) for more details.

## Attributes of a Migration Set {#attributes-migration-set}
 
A migration set has the following attributes:

* With the new version, you can create a maximum of ten migration sets within a project created in Cloud Acceleration Manager.
* Each migration set should have a unique name. 

The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity. 

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 

In the extraction phase, to ***top-up*** an existing migration set, the *overwrite* option must be disabled. See [Top Up Extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process) for more details.

In the ingestion phase, to apply the delta content on top of the current content, the *wipe* option must be disabled. See [Top Up Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process) for more details.

## Migration Set Expiry {#migration-set-expiry}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_migrationset_expiry"
>title="Expiration of a Migration Set"
>abstract="Learn about the expiry of a migration set."

All migration sets will eventually expire after a prolonged period of inactivity of approximately 45 days. After indicators are displayed on the project card and the migration job table rows for a period of time, the migration set will expire and its data will no longer be available. The expiry time can easily be extended by acting upon the migration set by:

* editing its description
* getting its extraction key
* performing an extraction to it
* performing an ingestion from it

The expiry of a migration set can be monitored on the Migration Set row. A helpful visual indicator that a migration set is approaching its expiry date also added the project's card.

![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam29.png)

## What's Next {#whats-next}

Once you have learned about Content Transfer Tool and its overview that describes this tool can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance, you must review [Prerequisites for Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/prerequisites-content-transfer-tool.md).
