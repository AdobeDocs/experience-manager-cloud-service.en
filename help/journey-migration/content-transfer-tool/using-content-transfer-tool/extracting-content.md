---
title: Extracting Content from Source
description: Extracting Content from Source
exl-id: c5c08c4e-d5c3-4a66-873e-96986e094fd3
---
# Extracting Content from Source {#extracting-content}

## Extraction Process in Content Transfer Tool {#extraction-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_extraction"
>title="Content Extraction"
>abstract="Extraction refers to extracting content from the source AEM instance into a temporary area called migration set. A migration set is a cloud storage area provided by Adobe to temporarily store the transferred content between the source AEM instance and the Cloud Service AEM instance."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#top-up-extraction-process" text="Top Up Extraction"


Follow the steps below to extract your migration set from the Content Transfer Tool:

   >[!NOTE]
   >If Amazon S3 or Azure Data Store is used as the type of data store, you can run the optional pre-copy step to significantly speed up the extraction phase. To do so you will need to configure an `azcopy.config` file before running extraction. Refer to [Handling Large Content Repositories](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en) for more details. 

   >[!IMPORTANT]
   >You should run User Mapping tool before extracting content from source. See [Using the User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/user-mapping-tool/using-user-mapping-tool.html?lang=en) for more details.

1. Select a migration set from **Content Transfer** wizard and click **Extract** to start extraction. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam12.png) 

   >![IMPORTANT]
   >
   >Make sure that the Extraction key is valid and is not close to its expiration. If it's close to its expiration date, you can renew the Extraction key by selecting the migration set and clicking on Properties. Click on **Renew**. This will take you to the Cloud Acceleration Manager where you can click on **Copy Extraction Key**. Every time you click on **Copy Extraction Key**, a new Extraction key is generated which is valid for 14 days from the time of creation.
   >[!image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam13.png)

1. This will bring up the Extraction dialog. Click on **Extract** to start the extraction phase.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam14.png) 

   >[!NOTE]
   >You have the option to overwrite the staging container during the extraction phase. If **Overwrite staging container** is disabled it can speed up extractions for subsequent migrations where the content paths or include versions settings have not changed. However, if the content paths or include versions settings have changed, then **Overwrite staging container** should be enabled.

   >[!IMPORTANT]
   >If the User Mapping has not been run on this migration set prior to extracting content from source, you will see a warning displaying that User Mapping step is pending, as shown in the figure above. Click on **Map Users** to run the User Mapping tool.
  
1. The **Extraction** field now displays the **RUNNING** status to indicate that the extraction is in-progress.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam15.png) 

   You can click on **View Progress** to get a granular view of the on-going extraction.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam16.png)

   You can also monitor the Extraction phase progress from Cloud Acceleration Manager by visiting the Content Transfer page.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam17.png)

1. Once Extraction is completed, review the other columns like **Source** and **Paths** for details of the migration set that you populated by clicking on **...** and then on **View details**. 
 
   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam18.png)   


## Top-Up Extraction {#top-up-extraction-process}

The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. 
>Additionally, it is essential that the content structure of existing content is not changed from the time the initial extraction is taken to when the top-up extraction is run. Top-ups cannot be run on content whose structure has been changed since the initial extraction. Please ensure you restrict this during the migration process.

Once the extraction process is complete, you can transfer delta content, by using the top-up extraction method. 

Follow the steps below:

1. Navigate to the **Content Transfer** wizard and select the migration set for which you want to perform the top-up extraction. Click **Extract** to start the top-up extraction. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam19.png)

1. The **Migration Set extraction** dialog box displays. Click on **Extract**.

   >[!IMPORTANT]
   >You should disable the **Overwrite staging container during extraction** option.
   >![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam20.png)


## What's Next {#whats-next}

Once you have learned Extracting Content from Source in Content Transfer Tool, you are now ready to learn the Ingestion Process in Content Transfer Tool. See [Ingesting Content into Target](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md) to learn how to ingest your migration set from the Content Transfer Tool.
