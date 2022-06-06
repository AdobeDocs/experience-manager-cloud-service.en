---
title: Ingesting Content into Target
description: Ingesting Content into Target
exl-id: d8c81152-f05c-46a9-8dd6-842e5232b45e
---
# Ingesting Content into Target {#ingesting-content}

## Ingestion Process in Content Transfer Tool {#ingestion-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_ingestion"
>title="Content Ingestion"
>abstract="Ingestion refers to ingesting content from the migration set into the target Cloud Service instance. The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#top-up-ingestion-process" text="Top Up Ingestion"

Follow the steps below to ingest your migration set from the Content Transfer Tool:
   >[!NOTE]
   >You can run the optional pre-copy step to significantly speed up the ingestion phase. The pre-copy step is most effective for the 1st full extraction and ingestion. Refer to [Ingesting with AzCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md#ingesting-azcopy) for more details. 

1. Go to Cloud Acceleration Manager. Click on your project card and click on the Content Transfer card. Navigate to **Ingestion Jobs** and click on **New Ingestion** 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-01.png)

1. Provide the required information to create a new ingestion.

   * Select the migration set that you just extracted as the Source
   * Select the destination environment. This is where the content of the migration set will be ingested. Select the tier. (Author/Publish).

   >[!NOTE]
   >
   >If the source was Author, it is recommended to ingest it into the Author tier on the target. Similarly, if source was Publish, target should be Publish as well.

   >[!NOTE]
   >
   >You can run the optional pre-copy step to significantly speed up the ingestion phase. Refer to [Ingesting with AzCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md#ingesting-azcopy) for more details.
   > 
   >If ingesting with pre-copy is used (for S3 or Azure Data Store), it is recommended to run Author ingestion first alone. This will speed up the Publish ingestion when it is run later.

   >[!IMPORTANT]
   >
   >You will be able to kick-off an ingestion to the destination environment only if you belong to the local **AEM administrators** group in the Cloud Service instance you are transferring content. If you don't belong to the AEM administrators group, you will see an error as shown below when you try to start an ingestion.
   >![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam21.png)

   >[!IMPORTANT]
   >
   >If the setting **Wipe** is enabled before ingestion, it deletes the entire existing repository and creates a new repository to ingest content into. This means that it resets all settings including permissions on the target Cloud Service instance. This is also true for an admin user added to the **administrators** group. You will need to be re-added to the administrators group in order to start an ingestion.

1. Click on **Ingest**

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam22.png)

1. You can then monitor the Ingestion phase from the Ingestion Jobs list view

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam23.png)

1. Once Ingestion is completed, click on (i) button on the top right corner of the screen to get more information about the ingestion job. 

<!-- Alexandru: hiding temporarily, until it's reviewed 

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

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-05.png) -->

## Top Up Ingestion {#top-up-ingestion-process}

>[!CONTEXTUALHELP] 
>id="aemcloud_ctt_ingestion_topup" title="Top Up Ingestion" 
>abstract="Use the top up feature to move  modified content since the previous content transfer activity. Upon completion of Ingestion, check the logs for any error/warnings. Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe Customer Care." 
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/viewing-logs.html?lang=en" text="Viewing Logs"

The Content Transfer Tool has a feature that supports differential content *top-up* where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. If you have used the pre-copy step for the 1st full ingestion, you can skip pre-copy for subsequent top-up ingestions (if the top-up migration set size is less than 200GB) because it may add time to the entire process.

Once the ingestion process is complete, to ingest the delta content you will need to run a [Top-Up Extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process) and then use the top-up ingestion method. 

You can do this by creating a new Ingestion Job and ensure that **Wipe** is disabled during the Ingestion phase, as shown below:

![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam24.png)



## What's Next {#whats-next}

Once you have learned Ingesting Content into Target in Content Transfer Tool, you can view logs upon completion of each step (extraction and ingestion) and look for errors. See [Viewing Logs for a Migration Set](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/viewing-logs.html?lang=en) to learn more.
