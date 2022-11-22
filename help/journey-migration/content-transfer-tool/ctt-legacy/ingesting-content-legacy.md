---
title: Ingesting Content into Target (Legacy)
description: Ingesting Content into Target
hide: yes
hidefromtoc: yes
exl-id: 326b3e98-5055-49b5-a005-63fd3ca35202
---
# Ingesting Content into Target (Legacy) {#ingesting-content}

## Ingestion Process in Content Transfer Tool {#ingestion-process}

Follow the steps below to ingest your migration set from the Content Transfer Tool:
   >[!NOTE]
   >You can run the optional pre-copy step to significantly speed up the ingestion phase. Refer to [Ingesting with AzCopy](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en#ingesting-azcopy) for more details. 

1. Select a migration set from **Content Transfer** page and click **Ingest** to start ingestion. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-01.png)

1. The **Migration Set ingestion** dialog box displays. Content can be ingested to either Author instance or Publish instance at a time. Select the instance to ingest content to. Click on **Ingest** to start the ingestion phase. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-02.png)

   >[!IMPORTANT]
   >If ingesting with pre-copy is used (for S3 or Azure Data Store), it is recommended to run Author ingestion first alone. This will speed up the Publish ingestion when it is run later. 

   >[!IMPORTANT]
   >When the **Wipe existing content on Cloud instance before ingestion** option is enabled, it deletes the entire existing repository and creates a new repository to ingest content into. This means that it resets all settings including permissions on the target Cloud Service instance. This is also true for an admin user added to the **administrators** group.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-03.png)

   Additionally, click on **Customer Care** to log a ticket, as shown in the figure below. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-04.png)
   
   Also, refer to [Important Considerations for Using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/guidelines-best-practices-content-transfer-tool.html?lang=en#important-considerations) to learn more.

1. Once the ingestion is complete, the status under **Author ingestion** updates to **FINISHED**.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-05.png)

## Top Up Ingestion {#top-up-ingestion-process}

The Content Transfer Tool has a feature that supports differential content *top-up* where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service.

Once the ingestion process is complete, you can use delta content, by using the top-up ingestion method. Follow the steps below:

1. Navigate to the **Content Transfer** wizard and select the migration set for which you want to perform the top-up ingestion. Click **Ingest** to start the top-up extraction. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/topup-ingest1.png)


1. The **Migration Set ingestion** dialog box displays. 

    ![image](/help/journey-migration/content-transfer-tool/assets-ctt/topup-ingest2.png)

   >[!IMPORTANT]
   >You should disable the **Wipe existing content on Cloud instance before ingestion** option, to prevent deleting the existing content from the previous ingestion activity. Additionally, click on **Customer Care** to log a ticket, as shown in the preceding figure.

## What's Next {#whats-next}

Once you have learned Ingesting Content into Target in Content Transfer Tool, you can view logs upon completion of each step (extraction and ingestion) and look for errors. See [Viewing Logs for a Migration Set](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/viewing-logs.html?lang=en) to learn more.
