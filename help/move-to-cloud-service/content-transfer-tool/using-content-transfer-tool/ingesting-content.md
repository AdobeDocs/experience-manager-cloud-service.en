---
title: Ingesting Content into Target in Content Transfer Tool
description: Ingesting Content into Target in Content Transfer Tool
---

# Ingesting Content into Target in Content Transfer Tool {#ingesting-content}

## Ingestion Process in Content Transfer Tool {#ingestion-process}

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

   Additionally, click on **Customer Care** to log a ticket, as shown in the figure above. Also, refer to [Important Considerations for Using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/guidelines-best-practices-content-transfer-tool.html?lang=en#important-considerations) to learn more.

1. Once the ingestion is complete, the status updates to **FINISHED**.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/15-ingestion-complete.png)

## Top Up Ingestion {#top-up-ingestion-process}

The Content Transfer Tool has a feature that supports differential content *top-up* where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service.

Once the ingestion process is complete, you can use delta content, by using the top-up ingestion method. Follow the steps below:

1. Navigate to the *Overview* page and select the migration set for which you want to perform the top-up ingestion. Click **Ingest** to start the top-up extraction. The **Migration Set ingestion** dialog box displays. 

    ![image](/help/move-to-cloud-service/content-transfer-tool/assets/content-ingestion-02.png)

   >[!IMPORTANT]
   >You should disable the **Wipe existing content on Cloud instance before ingestion** option, to prevent deleting the existing content from the previous ingestion activity. Additionally, click on **Customer Care** to log a ticket, as shown in the preceding figure.
