---
title: Extracting Content from Source (Legacy)
description: Extracting Content from Source
hide: yes
hidefromtoc: yes
exl-id: 9f43356c-ba51-48bc-97f5-f1f5db81e7f3
---
# Extracting Content from Source (Legacy) {#extracting-content}

## Extraction Process in Content Transfer Tool {#extraction-process}

Follow the steps below to extract your migration set from the Content Transfer Tool:
   >[!NOTE]
   >If Amazon S3 or Azure Data Store is used as the type of data store, you can run the optional pre-copy step to significantly speed up the extraction phase. To do so you will need to configure an `azcopy.config` file before running extraction. Refer to [Handling Large Content Repositories](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en) for more details. 

   >[!IMPORTANT]
   >You should run User Mapping tool before extracting content from source. See [Using the User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/user-mapping-tool/using-user-mapping-tool.html?lang=en) for more details.

1. Select a migration set from **Content Transfer** wizard and click **Extract** to start extraction. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/extraction-01.png) 

1. The **Migration Set extraction** dialog box displays and click on **Extract** to start the extraction phase.  

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/extraction-02.png) 

   >[!NOTE]
   >You have the option to overwrite staging container during the extraction phase.

   >[!IMPORTANT]
   >If the User Mapping has not been run on this migration set prior to extracting content from source, you will see a warning displaying that User Mapping step is pending, as shown in the figure below. Click on **Map Users** to run the User Mapping tool.
   >![image](/help/journey-migration/content-transfer-tool/assets-ctt/user-mapping-extract.png) 
  
1. The **Extraction** field now displays the **RUNNING** status to indicate that the extraction is in-progress.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/extraction-03.png) 

   Once the extraction is complete, the status of the migration set updates to **FINISHED** and a *solid green* cloud icon displays under the **INFO** field.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/extraction-04.png) 

   >[!IMPORTANT]
   >The UI has an auto-reload feature that reloads the **Content Transfer** wizard every 30 seconds.
   >When extraction phase is started, write lock is created and released after *60 seconds*. So, if an extraction is stopped, you need to wait for a minute for lock to be released before starting extraction again.

## Top-Up Extraction {#top-up-extraction-process}

The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 
>Additionally, it is essential that the content structure of existing content is not changed from the time the initial extraction is taken to when the top-up extraction is run. Top-ups cannot be run on content whose structure has been changed since the initial extraction. Please ensure you restrict this during the migration process.

Once the extraction process is complete, you can transfer delta content, by using the top-up extraction method. 

Follow the steps below:

1. Navigate to the **Content Transfer** wizard and select the migration set for which you want to perform the top-up extraction. Click **Extract** to start the top-up extraction. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/extraction-05.png)

1. The **Migration Set extraction** dialog box displays. Click on **Extract**.

   >[!IMPORTANT]
   >You should disable the **Overwrite staging container during extraction** option.
   >![image](/help/journey-migration/content-transfer-tool/assets-ctt/extraction-06.png)


## What's Next {#whats-next}

Once you have learned Extracting Content from Source in Content Transfer Tool, you are now ready to learn the Ingestion Process in Content Transfer Tool. See [Ingesting Content into Target](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md) to learn how to ingest your migration set from the Content Transfer Tool.
