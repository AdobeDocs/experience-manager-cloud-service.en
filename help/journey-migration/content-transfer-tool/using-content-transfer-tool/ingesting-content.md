---
title: Ingesting Content into Cloud Service
description: Learn how to use the Cloud Acceleration Manager to ingest content from your migration set into a destination Cloud Service instance.
exl-id: d8c81152-f05c-46a9-8dd6-842e5232b45e
feature: Migration
role: Admin
---
# Ingesting Content into Cloud Service {#ingesting-content}

## Ingestion Process in the Cloud Acceleration Manager {#ingestion-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_ingestion"
>title="Content Ingestion"
>abstract="Ingestion refers to ingesting content from the migration set into the destination Cloud Service instance. The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/extracting-content#top-up-extraction-process" text="Top Up Extraction"

Follow the steps below to ingest your migration set using the Cloud Acceleration Manager:

1. Go to Cloud Acceleration Manager. Click your project card and click the Content Transfer card. Navigate to **Ingestion Jobs** and click **New Ingestion** 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-01.png)

1. Review the ingestion checklist and ensure that all the steps are completed. These steps are necessary to ensure a successful ingestion. Proceed to the **Next** step only if the checklist is completed.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/Ingestion-checklist.png)

1. Provide the required information to create an ingestion.

   * **Migration Set:** Select the migration set that contains the extracted data as the Source.
     * Migration Sets will expire after a prolonged period of inactivity, so it is expected that the ingestion occurs relatively soon after the extraction has been performed. Review [Migration Set Expiry](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/overview-content-transfer-tool.md#migration-set-expiry) for details.
   
   >[!TIP]
   > If the extraction is running, the dialog will indicate it. Once extraction has completed successfully, the ingestion starts automatically. If the extraction fails or is stopped, the ingestion job will be rescinded.

   * **Destination:** Select the destination environment. This environment is where the content of the migration set is ingested.
     * Ingestions do not support destinations of type Rapid Development Environment (RDE) or Preview, and they do not appear as a possible destination choice, even if the user has access to it.
     * While a migration set can be ingested into multiple destinations simultaneously, a destination can be the target of only one running or waiting ingestion at a time.

   * **Tier:** Select the tier. (Author/Publish).
     * If the source was `Author`, it is recommended to ingest it into the `Author` tier on the target. Similarly, if source was `Publish`, the target should be `Publish` as well.

   >[!NOTE]
   > If the target tier is `Author`, the author instance is shut down during the length of the ingestion and becomes unavailable to users (for example, authors or anyone performing maintenance). The reason is to protect the system, and prevents any changes which could either be lost or cause an ingestion conflict. Ensure that your team is aware of this fact. Also note that the environment appears hibernated during the author ingestion.
   
   >[!NOTE]
   > If the target tier is `Publish`, the publish instance remains running during ingestion.  However, if the compaction process is running while ingestion occurs, a conflict between the two processes is likely to happen.  For this reason the ingestion process 1) disables the compaction timed script so compaction will not start during the ingestion, and 2) checks if compaction is currently running, and if it is, waits for it to complete before the ingestion proceeds.  If the publish ingestion is taking longer than expected, check the ingestion logs for related log statements.

   * **Wipe:** Choose the `Wipe` value
     * The **Wipe** option sets the destination's starting point of the ingestion. If **Wipe** is enabled, the destination including all its content is reset to the version of AEM that is specified in Cloud Manager. If not enabled, the destination maintains its current content as the starting point.
     * This option does **NOT** affect how the ingestion of content will be performed. Ingestion always uses a content replacement strategy and _not_ a content merge strategy so, in both **Wipe** and **Non-Wipe** cases, the ingestion of a migration set will overwrite contents in the same path on the destination. For instance, if the migration set contains `/content/page1` and the destination already contains `/content/page1/product1`, the ingestion removes the entire `page1` path and its subpages, including `product1`, and replace it with the content in the migration set. This means careful planning must be done when performing a **Non-Wipe** ingestion to a destination that contains any content that should be maintained. 
     * Non-wipe ingestions are specifically designed for the top up ingestion use-case. These ingestions are intended to have an incremental amount of new content that has changed since the last ingestion in an existing migration set. Performing non-wipe ingestions outside of this use case could result in very long ingestion times.

   >[!IMPORTANT]
   > If the setting **Wipe** is enabled for the ingestion, it resets the entire existing repository including the user permissions on the target Cloud Service instance. This resetting is true also for an admin user added to the **administrators** group and that user must be added to the administrators group again to start an ingestion.

   * **Pre-Copy:** Choose the `Pre-copy` value
     * You can run the optional pre-copy step to significantly speed up the ingestion. See [Ingesting with AzCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md#ingesting-azcopy) for more details.
     * If ingesting with pre-copy is used (for S3 or Azure Data Store), it is recommended to run `Author` ingestion first alone. Doing so speeds up the `Publish` ingestion when it is run later.

   >[!IMPORTANT]
   > You can initiate an ingestion to the destination environment only if you belong to the local **AEM administrators** group on the destination Cloud Service author service. If you are unable to start an ingestion, see [Unable to Start Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#unable-to-start-ingestion) for more details.

1. Once ingestion choices have been selected, an estimate of its duration may be shown. This is a best-effort estimate based on historical data of similar ingestions.

   * This estimate is not calculated or shown for **non-wipe** ingestions, as CAM does not know how much content is on the target system in this case.
   * This estimate is only calculated and shown if the 'Check Size' values of the extraction were collected and are available.
   * This value is an estimate and, although intelligently calculated, should not be considered exact. Various factors can change the actual duration.
   * While the ingestion is running, this value will also be available in the durations dialog, accessed through the "**View durations**" action of the ingestion.

>[!CONTEXTUALHELP]
>id="aemcloud_cam_ingestion_estimate"
>title="Ingestion Duration Estimate"
>abstract="An approximate duration of a particular ingestion can be displayed to provide a general sense as to how long it will take. Limitations to its accuracy do exist."

   ![image](/help/journey-migration/content-transfer-tool/assets/estimate.png)

1. Click **Ingest**.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam22.png)

1. You can then monitor the ingestion from the Ingestion Jobs list view and use the ingestion's action menu to view the durations and log as the ingestion progresses.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam23.png)

1. Click the **(i)** button in the row for more information about the ingestion job. You can see the duration of each step of the Ingestion when it is running or completed by clicking **...**, and then clicking **View durations**. The information from the extraction is also shown to realize what is being ingested.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam23b.png)

## Top Up Ingestion {#top-up-ingestion-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_ingestion_topup"
>title="Top Up Ingestion"
>abstract="Use the top-up feature to move content modified since the previous content transfer activity. Upon completion of Ingestion, check the logs for any errors or warnings. Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe Customer Care."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/viewing-logs" text="Viewing Logs"

The Content Transfer Tool has a feature that allows the extraction of differential content by performing a *top-up* of the migration set. This allows the migration set to be modified to include only the content that has changed since the previous extraction without having to extract all the content again.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. If you have used the pre-copy step for the first ingestion, you can skip pre-copy for subsequent top-up ingestions (if the top-up migration set size is less than 200 GB). The reason is that it may add time to the entire process.

To ingest differential content after some ingestions are complete, you must run a [Top-Up Extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process), and then use the ingestion method with the **Wipe** option **disabled**. Be sure to read the **Wipe** explanation above to avoid losing content already on the destination. 

Begin by creating an Ingestion Job and ensure that **Wipe** is disabled during the ingestion, as shown below:

![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam24.png)

## Troubleshooting {#troubleshooting}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_ingestion_troubleshooting"
>title="Content Ingestion Troubleshooting"
>abstract="Refer to the ingestion logs and the documentation to find solutions to common reasons why an ingestion can fail and find the way to fix the problem. Once fixed, the ingestion can be run again."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/validating-content-transfers" text="Validating Content Transfers"

### CAM Unable to Retrieve the Migration Token {#cam-unable-to-retrieve-the-migration-token}

The automatic retrieval of the migration token may fail for different reasons, including you [setting up an IP allow list via Cloud Manager](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) on the target Cloud Service environment. In such scenarios, you see the following dialog box when you attempt to start an ingestion:

![image](/help/journey-migration/content-transfer-tool/assets-ctt/troubleshooting-token.png)

Retrieve the migration token manually by clicking the "Get token" link on the dialog box. Another tab is opened that displays the token. You can then copy the token and paste it into the **Migration token input** field. Now, you should be able to start the ingestion.

>[!NOTE]
>
>The token is available to users who belong to the local **AEM administrators** group on the destination Cloud Service author service. 

### Unable to Start Ingestion {#unable-to-start-ingestion}

You can initiate an ingestion to the destination environment only if you belong to the local **AEM administrators** group on the destination Cloud Service author service. If you do not belong to the AEM administrators group, you see an error as shown below when you try to start an ingestion. You can either ask your administrator to add you to the local **AEM administrators** or ask for the token itself, which you can then paste into the **Migration token input** field.

![image](/help/journey-migration/content-transfer-tool/assets-ctt/error_nonadmin_ingestion.png)

### Unable to reach migration service {#unable-to-reach-migration-service}

After an ingestion is requested, a message like the following may be presented to the user: "The migration service on the destination environment is unreachable. If so, try again later or contact Adobe support."

![image](/help/journey-migration/content-transfer-tool/assets-ctt/error_cannot_reach_migser.png)

This message indicates that the Cloud Acceleration Manager was unable to reach the target environment's migration service to start the ingestion. This situation can happen for various reasons.

>[!NOTE]
> 
> The "Migration token" field is shown because in a few cases retrieving that token is what is actually disallowed. By allowing it to be manually provided, it may allow the user to start the ingestion quickly, without any additional help. If the token is provided, and the message still appears, then retrieving the token was not the problem.

* AEM as a Cloud Service maintains the environment state, and occasionally must restart the migration service for various normal reasons. If that service is restarting, it cannot be reached, but is available eventually.
* It is possible that another process is being run on the instance. For example, if [AEM Version Updates](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/aem-version-updates) is applying an update, the system may be busy and the migration service regularly unavailable. Once that process is done, the start of the ingestion can be attempted again. 
* If an [IP Allowlist has been applied](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) through Cloud Manager, it blocks Cloud Acceleration Manager from reaching the migration service. An IP address cannot be added for ingestions because its address is dynamic. Currently, the only solution is to disable the IP allowlist during the ingestion and indexing process.
* There may be other reasons that need investigation. If the ingestion or indexing continues to fail, contact Adobe Customer Care.

### AEM Version Updates and Ingestions {#aem-version-updates-and-ingestions}

[AEM Version Updates](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/deploying/aem-version-updates) are automatically applied to environments to keep them up to date with the most recent AEM as a Cloud Service version. If the update is triggered when an ingestion is performed, it can cause unpredictable results including the corruption of the environment.

If the "AEM Version Updates" is onboarded on the destination program, the ingestion process attempts to disable its queue before it starts. When the ingestion is complete, the version updater state is returned to how it was before the ingestions started.

>[!NOTE]
>
> There is no longer a need to log a support ticket to get "AEM Version Updates" disabled.

If "AEM Version Updates" is active (that is, updates are running or are queued to be run), the ingestion will not begin and the user interface presents the following message. Once the updates are complete, the ingestion can be started. Cloud Manager can be used to see the current state of the pipelines of the program.

>[!NOTE]
>
> "AEM Version Updates" is run in the environment's pipeline and waits until the pipeline is clear. If updates are queued for longer than expected, ensure that a custom workflow does not have the pipeline unintentionally locked. 

![image](/help/journey-migration/content-transfer-tool/assets-ctt/error_releaseorchestrator_active.png)

### Ingestion Failure Due to Cloud Environment Not In Ready State {#ingestion-failure-due-to-cloud-environment-not-in-ready-state}

>[!CONTEXTUALHELP]
>id="aemcloud_cam_ingestion_troubleshooting_cloud_environment_not_in_ready_state"
>title="Cloud Environment Not In Ready State"
>abstract="In rare instances the target cloud environment may be experiencing unexpected issues, which will cause the ingestion to fail."

In rare instances the ingestion's target Cloud Service environment may be experiencing unexpected issues. As a result the ingestion will fail since the environment is not in the expected ready state. Check the ingestion log to reveal more details of the error state encountered. 

Ensure the author environment is available and wait a few minutes before re-attemting the ingestion. If the problem persists, reach out to customer support with the error state encountered.

### Top-up Ingestion Failure Due to Uniqueness Constraint Violation {#top-up-ingestion-failure-due-to-uniqueness-constraint-violation}

>[!CONTEXTUALHELP]
>id="aemcloud_cam_ingestion_troubleshooting_uuid"
>title="Uniqueness Constraint Violation"
>abstract="A common cause of a non-wipe ingestion failure is a conflict in node ids. Only one of the conflicting nodes can exist."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/ingesting-content#top-up-ingestion-process" text="Top-up Ingestion"

A common cause of a [Top-up Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process) failure is a conflict in node ids. To identify this error, download the ingestion log using the Cloud Acceleration Manager UI and look for an entry like the following:

>java.lang.RuntimeException: org.apache.jackrabbit.oak.api.CommitFailedException: OakConstraint0030: Uniqueness constraint violated property [jcr:uuid] having value a1a1a1a1-b2b2-c3c3-d4d4-e5e5e5e5e5e5: /some/path/jcr:content, /some/other/path/jcr:content

Each node in AEM must have a unique uuid. This error indicates that a node that is being ingested has the same uuid as one that exists at a different path on the destination instance. This situation can happen for two reasons:

* A node is moved on the source between an extraction and a subsequent [Top-Up Extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process)
  * _REMEMBER_: For Top-Up extractions, the node will still exist in the migration set, even if it no longer exists on the source.
* A node on the destination is moved between an ingestion and a subsequent top-up ingestion.

This conflict must be resolved manually. Someone familiar with the content must decide which of the two nodes must be deleted, keeping in mind other content that references it. The solution may require that the top-up extraction is done again without the offending node. 

### Top-up Ingestion Failure Due to Unable to Delete Referenced Node {#top-up-ingestion-failure-due-to-unable-to-delete-referenced-node}

>[!CONTEXTUALHELP]
>id="aemcloud_cam_ingestion_troubleshooting_referenced_node"
>title="Unable to Delete Referenced Node"
>abstract="A common cause of a non-wipe ingestion failure is a version conflict for a particular node on the destination instance. The versions of the node must be remedied."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/ingesting-content#top-up-ingestion-process" text="Top-up Ingestion"

Another common cause of a [Top-up Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process) failure is a version conflict for a particular node on the destination instance. To identify this error, download the ingestion log using the Cloud Acceleration Manager UI and look for an entry like the following:

>java.lang.RuntimeException: org.apache.jackrabbit.oak.api.CommitFailedException: OakIntegrity0001: Unable to delete referenced node: 8a2289f4-b904-4bd0-8410-15e41e0976a8

This can happen if a node on the destination is modified between an ingestion and a subsequent **Non-Wipe** ingestion such that a new version has been created. If the migration set was extracted with "include versions" enabled, a conflict may occur since the destination now has a more recent version that is being referenced by version history and other content. The ingestion process is unable to delete the offending version node due to it being referenced.

The solution may require that the top-up extraction is done again without the offending node. Or, creating a small migration set of the offending node, but with "include versions" disabled. 

Best practices indicate that if a **Non-Wipe** ingestion must be run using a migration set that includes versions, it is crucial that content on the destination is modified as little as possible, until the migration journey is complete. Otherwise, these conflicts can occur.

### Ingestion Failure Due to Large Node Property Values {#ingestion-failure-due-to-large-node-property-values}

>[!CONTEXTUALHELP]
>id="aemcloud_cam_ingestion_troubleshooting_bson"
>title="Large Node Property"
>abstract="A common cause of an ingestion failure is exceeding the maximum size of node property values. Follow the documentation, including those related to the BPA report, to remedy this situation."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/prerequisites-content-transfer-tool" text="Migration Prerequisites"

Node property values stored in MongoDB cannot exceed 16 MB. If a node value exceeds the supported size, the ingestion fails and the log will contain either:

* a `BSONObjectTooLarge` error and specify which node exceeded the maximum, or 
* a `BsonMaximumSizeExceededException` error, which indicates there is a node likely containing unicode characters that is exceeding the maximum size **

This is a MongoDB restriction.

See the `Node property value in MongoDB` note in [Prerequisites for Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/prerequisites-content-transfer-tool.md) for more information and a link to an Oak tool that could help find all the large nodes. Once all nodes with large sizes are remedied, run the extraction and ingestion again.

To possibly avoid this restriction, run the [Best Practices Analyzer](/help/journey-migration/best-practices-analyzer/using-best-practices-analyzer.md) on the source AEM instance and review the findings it presents, particularly the ["Unsupported Repository Structure" (URS)](https://experienceleague.adobe.com/en/docs/experience-manager-pattern-detection/table-of-contents/urs) pattern.

>[!NOTE]
>
>[Best Practices Analyzer](/help/journey-migration/best-practices-analyzer/using-best-practices-analyzer.md) version 2.1.50+ will report on large nodes containing unicode characters that exceed the maximum size. Please ensure you are running the latest version. BPA versions prior to 2.1.50 will not identify and report on these large nodes and they will need to be discovered separately using the prerequisite Oak tool mentioned above.

### Ingestion Failure Due to Unexpected Intermittent Errors {#ingestion-failure-due-to-unexpected-intermittent-errors}

>[!CONTEXTUALHELP]
>id="aemcloud_cam_ingestion_troubleshooting_intermittent_errors"
>title="Unexpected Intermittent Errors"
>abstract="At times unexpected intermittent downstream service errors may occur and unfortunately the only recourse is to simply retry the ingestion."

At times unexpected intermittent issues could lend themselves to failed ingestions where unfortunately the only recourse is to retry the ingestion. Investigate the ingestion log to uncover the cause of the failure and see if it aligns with any of the errors listed below, where a retry should be attempted. 

#### MongoDB issues {#mongo-db-issues}

* `Atlas prescale timeout error` - The ingestion phase will attempt to prescale the target cloud database to a suitable size that aligns with the size of the migration set content being ingested. Infrequently, this operation does not complete within the expected timeframe.
* `Exhausted mongo restore retries` - Attempts to restore a local dump of the ingested migration set contents to the cloud database has been exhausted. This indicates an overall health/network issue with MongoDB, that often heals itself after a few minutes.
* `Mongo network error` - At times, establishing a connection to MongoDB can fail, causing the ingestion process to exit early and report it as failed. A simple retry of the ingestion should be attempted.

### Ingestion Rescinded {#ingestion-rescinded}

>[!CONTEXTUALHELP]
>id="aemcloud_cam_ingestion_troubleshooting_rescinded"
>title="Ingestion Rescinded"
>abstract="The extraction that the ingestion was waiting for did not finish successfully. The ingestion was rescinded because it could not be executed."

An ingestion that was created with a running extraction as its source migration set waits patiently until that extraction succeeds, and at that point starts normally. If the extraction fails or is stopped, the ingestion and its indexing job will not begin but is rescinded. In this case, check the extraction to determine why it failed, remedy the problem and start extracting again. Once the fixed extraction is running, a new ingestion can be scheduled. 

### Deleted Asset not present after re-running ingestion

In general, modifying the cloud environment data in between ingestions is not recommended. 

When an asset is deleted from the Cloud Service destination using the Assets Touch UI, the node data is deleted, but the asset blob with the image is not immediately deleted. It is marked for deletion so that it no longer appears in the UI; however, it remains in the datastore until garbage collection occurs and the blob is removed.

In the scenario where a previously migrated asset is deleted, and the next ingestion is run before the garbage collector has completed deleting the asset, ingesting the same migration set will not restore the deleted asset. When the ingestion checks on the cloud environment for the asset, there is no node data; therefore, the ingestion will copy the node data to the cloud environment. However, when it checks the blob store, it sees that the blob is present and skips copying the blob over. That is why the metadata is present post-ingestion when you look at the asset from the Touch UI, but the image is not. Please remember that migration sets and content ingestion were not designed to handle this case. They aim to add new content to the cloud environment and not restore previously migrated content.

## What's Next {#whats-next}

When the ingestion has succeeded, AEM indexing will start automatically. See [Indexing after Migrating Content](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/indexing-content.md) for more information.

Once you have completed Ingesting Content into Cloud Service, you can view logs of each step (extraction and ingestion) and look for errors. See [Viewing Logs for a Migration Set](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/viewing-logs.md) to learn more.
