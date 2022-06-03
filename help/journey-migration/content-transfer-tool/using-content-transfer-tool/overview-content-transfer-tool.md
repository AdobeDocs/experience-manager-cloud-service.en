---
title: Overview to Content Transfer Tool
description: Overview to Content Transfer Tool
exl-id: cfc0366a-2139-4d9d-b5bc-0b65bef4013c
---
# Overview {#overview-content-transfer-tool}


>[!CONTEXTUALHELP] 
>id="aemcloud_ctt_overview" 
>title="Overview" 
>abstract="Content Transfer Tool is a tool developed by Adobe that can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance. This tool also transfers principals (users or groups) automatically."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/guidelines-best-practices-content-transfer-tool.html?lang=en" text="Guidelines and Best Practices"

<!-- Alexandru: Old version of contextual help, keep for failover/debugging
>[!CONTEXTUALHELP]
>id="aemcloud_ctt_overview"
>title="Overview"
>abstract="Content Transfer Tool is a tool developed by Adobe that can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance. This tool also transfers principals (users or groups) automatically."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#extraction-process" text="Extraction Process"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#ingestion-process" text="Ingestion Process" -->

The Content Transfer Tool is a tool developed by Adobe that can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance. 

This tool also transfers principals (users or groups) automatically. 

A new version of the Content Transfer Tool is available which integrates the content transfer process with Cloud Acceleration Manager. It is highly recommended to switch over to this new version in order to leverage all the benefits it provides:

* Self-service way to extract a migration set once and ingest it into multiple environments in parallel
* Improved user experience via better loading states, guardrails, and error handling
* Ingestion logs are persisted and are always available for toubleshooting 

To start using the new version (v2.0.10) <!-- update when version is available --> you will need to uninstall older versions of the Content Transfer Tool because there was a major architectural change in the tool. 

>[!NOTE]
>
> For situations where a migration is already in progress, you may continue using the prior version of CTT until the migration is complete. For documentation related to the prior version of CTT, refer to the [legacy documentation](/help/journey-migration/content-transfer-tool/ctt-legacy/overview-content-transfer-tool-legacy.md).

## Phases in Content Transfer Tool {#phases-content-transfer-tool}

There are two phases associated with content transfer: 

1. **Extraction**:  Extraction refers to extracting content from the source AEM instance into a temporary area called *migration set*. A *migration set* is a cloud storage area provided by Adobe to temporarily store the transferred content between the source AEM instance and the Cloud Service AEM instance. 

   Refer to [Extraction Process in Content Transfer](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/extracting-content.html) for more details. 

    >[!NOTE]
    > It is recommended to run the User Mapping Tool as part of the Extraction phase. See [Using User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/user-mapping-tool/using-user-mapping-tool.html) for more details.

1. **Ingestion**: Ingestion refers to ingesting content from the *migration set* into the target Cloud Service instance. 

   See [Ingestion Process in Content Transfer](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/ingesting-content.html) for more details.

## Attributes of a Migration Set {#attributes-migration-set}
  
A migration set has the following attributes:

* With the new version, you can create a maximum of five migration sets within a project created in Cloud Acceleration Manager.
* Each migration set should have a unique name. 

The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity. 

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 

In the extraction phase, to ***top-up*** an existing migration set, the *overwrite* option must be disabled. Refer to [Top Up Extraction](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/extracting-content.html?lang=en#top-up-extraction-process) for more details.

In the ingestion phase, to apply the delta content on top of the current content, the *wipe* option must be disabled. Refer to [Top Up Ingestion](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/ingesting-content.html?lang=en#top-up-ingestion-process) for more details.

## What's Next {#whats-next}

Once you have learned about Content Transfer Tool and its overview that describes this tool can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance, you must review [Prerequisites for Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/prerequisites-content-transfer-tool.html?lang=en).
