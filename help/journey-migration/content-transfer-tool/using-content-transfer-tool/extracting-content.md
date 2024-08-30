---
title: Extracting Content from Source
description: Learn how to extract content from a source Adobe Experience Manager (AEM) instance to later transfer it to a Cloud Service AEM instance.
exl-id: c5c08c4e-d5c3-4a66-873e-96986e094fd3
feature: Migration
role: Admin
---
# Extracting Content from Source {#extracting-content}

## Extraction Process in Content Transfer Tool {#extraction-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_extraction"
>title="Content Extraction"
>abstract="Extraction refers to extracting content from the source Adobe Experience Manager (AEM) instance into a temporary area called migration set. A migration set is a cloud storage area provided by Adobe to temporarily store the transferred content between the source AEM instance and the Cloud Service AEM instance."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html#top-up-extraction-process" text="Top Up Extraction"


Follow the steps below to extract your migration set from the Content Transfer Tool:

>[!NOTE]
>If Amazon S3, Azure Data Store, or File Data Store is used as the type of data store, you can run the optional pre-copy step to increase the speed of the extraction phase. The pre-copy step is most effective for the first full extraction and ingestion. See [Handling Large Content Repositories](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md) for more details.

1. Select a migration set from the **Content Transfer** wizard and click **Extract** to start extraction. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam12.png)

   >[!TIP]
   >An ingestion can now be scheduled to start automatically immediately after an extraction succeeds. See [Ingesting Content into Target](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md) for more information.

   >[!IMPORTANT]
   >
   >Make sure that the Extraction key is valid and is not near its expiration. If it is close to its expiration date, you can renew the Extraction key by selecting the migration set and clicking Properties. Click **Renew**. This takes you to the Cloud Acceleration Manager where you can click **Copy Extraction Key**. Every time you click **Copy Extraction Key**, a new Extraction key is generated which is valid for 14 days from the time of creation.
   >![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam13.png)

1. This brings up the Extraction dialog. Click **Extract** to start the extraction phase.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam14c.png) 

   >[!NOTE]
   >You can optionally overwrite the staging container during the extraction phase. If **Overwrite staging container** is disabled, it can speed up extractions for subsequent migrations where the content paths or include versions settings have not changed. However, if the content paths or include versions settings have changed, then **Overwrite staging container** should be enabled.

1. The **Extraction** field now displays the **RUNNING** status to indicate that the extraction is in-progress.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam15.png) 

   You can click **View Progress** to get a granular view of the on-going extraction.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam16.png)

   You can also monitor the Extraction phase progress from Cloud Acceleration Manager by visiting the Content Transfer page, and see it in more detail by clicking **...** > **View details**.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam17.png)

1. When Extraction is completed, review the other columns like **Source** and **Paths** for details of the migration set that you populated. Clicking **...** > **View details** to see details, including the duration of each step of the extraction. View this dialog box during the extraction so you can see how the steps are progressing. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam18b.png)


## Top-Up Extraction {#top-up-extraction-process}

The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. If you have used the pre-copy step for the first full extraction, you can skip pre-copy for subsequent top-up extractions (if the top-up migration set size is less than 200 GB). The reason is because it may add time to the entire process.
>Also, it is essential that the content structure of existing content is not changed from the time the initial extraction is taken to when the top-up extraction is run. Top-ups cannot be run on content whose structure has been changed since the initial extraction. Ensure that you restrict this during the migration process.

Once the extraction process is complete, you can transfer delta content, by using the top-up extraction method. 

Follow the steps below:

1. Navigate to the **Content Transfer** wizard and select the migration set for which you want to perform the top-up extraction. Click **Extract** to start the top-up extraction. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam19.png)

1. The **Migration Set extraction** dialog box displays. Click **Extract**.

   >[!IMPORTANT]
   >You should disable the **Overwrite staging container during extraction** option.
   >![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam20.png)


## What's Next {#whats-next}

After you have learned Extracting Content from Source in Content Transfer Tool, you are now ready to learn the Ingestion Process in Content Transfer Tool. See [Ingesting Content into Target](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md) where you can learn how to ingest your migration set from the Content Transfer Tool.
