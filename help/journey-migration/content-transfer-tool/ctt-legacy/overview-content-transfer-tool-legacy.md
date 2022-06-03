---
title: Overview to Content Transfer Tool (Legacy)
description: Overview to Content Transfer Tool
hide: yes
hidefromtoc: yes
---
# Content Transfer Tool Overview (Legacy) {#overview-content-transfer-tool}

The Content Transfer Tool is a tool developed by Adobe that can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance. 

This tool also transfers principals (users or groups) automatically. 

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

* A maximum of ten migration sets can be created and maintained at a time during the content transfer activity. 
* Each migration set should have a unique name. 
* If a migration set has been inactive for more than 30 days, it will be automatically deleted.
* Whenever you create a migration set, it is associated with a specific environment. You can only ingest into an author or a publish instance of the same environment.


The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity. 

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 

In the extraction phase, to ***top-up*** an existing migration set, the *overwrite* option must be disabled. Refer to [Top Up Extraction](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/extracting-content.html?lang=en#top-up-extraction-process) for more details.

In the ingestion phase, to apply the delta content on top of the current content, the *wipe* option must be disabled. Refer to [Top Up Ingestion](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/ingesting-content.html?lang=en#top-up-ingestion-process) for more details.

## What's Next {#whats-next}

Once you have learned about Content Transfer Tool and its overview that describes this tool can be used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance, you must review [Prerequisites for Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/prerequisites-content-transfer-tool.html?lang=en).
