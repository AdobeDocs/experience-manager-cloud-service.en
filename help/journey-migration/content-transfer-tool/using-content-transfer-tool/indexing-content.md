---
title: Indexing after Migrating Content
description: Learn how the migration process will index the ingested content on the destination Cloud Service instance.
---
# Indexing after Migrating Content {#Indexing-content}

## Indexing {#aem-indexing-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_indexing"
>title="Content Indexing"
>abstract="AEM Indexing refers to indexing of the Cloud Service instance after migrating content to it. The indexing is done to bring the performance to an optimum speed for a good experience."

Once the Cloud Acceleration Manager completes the ingestion of content into your Cloud Service instance, it is ready to be used. Initially
the content is not indexed though which will reduce performance greatly. For the instance to have optimum performance providing a good user
experience, the migration process will automatically start indexing the content. There is nothing to be done, except to monitor the indexing
progress.

> For information on how to start an ingestion, please see [Ingesting Content into Cloud Service](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md).

The following steps show the general flow you can expect to see in the UI during indexing. Some labels provide helpful context in
tooltips, so be sure to hover over items to learn more about the current indexing status.

To begin, go to Cloud Acceleration Manager. Click your project card and then click the Content Transfer card. Navigate to **Ingestion Jobs** 
and see the jobs listed.

>[!NOTE]
>You can view or download the indexing logs by using the ingestion job's actions, using the ... dropdown. The logs will be available after
>the indexing job is complete.

### Pending

This is how the ingestion job's row will appear when the ingestion is running, before the indexing job has been started. There is no action
required from the user. If the ingestion fails for whatever reason, the queueing of the index job will be rescinded, and not be started.

![image](/help/journey-migration/content-transfer-tool/assets-indexing/pending.png)

### Running

When the ingestion succeeds, the indexing job is initiated automatically. The ingestion job row will show a progress icon for the AEM indexing
status. You may open the duration dialog to see the simple progress of the job. 

![image](/help/journey-migration/content-transfer-tool/assets-indexing/running.png)

### Complete

When the indexing job succeeds the instance is ready to be used at optimum performance. At this point the indexing job logs
will be available to view or download in order to inspect them.

![image](/help/journey-migration/content-transfer-tool/assets-indexing/complete.png)

### Errors

The indexing of the destination cloud service instance will most likely succeed. In some cases, it can fail and the ingestion job row will
appear as follows. In all cases, you can find out some details of the failure by hovering over the failure status, and it may provide
more information to help you determine next steps. At this point the indexing job logs will be available to view or download in order to
help discover the source of the failure. If the next step is not clear, please contact Adobe Support with details of the ingestion and
the indexing log.

![image](/help/journey-migration/content-transfer-tool/assets-indexing/failed.png)

## What's Next {#whats-next}

Once you have completed Indexing Content into Target, the migration process will being to index your destination assuming the ingestion was successful. 
You can view logs of the ingestion and extraction steps and look for details and errors. See [Viewing Logs for a Migration Set](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/viewing-logs.html) to learn more.
