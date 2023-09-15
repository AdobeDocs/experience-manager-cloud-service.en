---
title: Ingesting Content into Cloud Service
description: Learn how to use the Cloud Acceleration Manager to ingest content from your migration set into a destination Cloud Service instance.
exl-id: d8c81152-f05c-46a9-8dd6-842e5232b45e
---
# Ingesting Content into Cloud Service {#ingesting-content}

## Ingestion Process in the Cloud Acceleration Manager {#ingestion-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_ingestion"
>title="Content Ingestion"
>abstract="Ingestion refers to ingesting content from the migration set into the destination Cloud Service instance. The Content Transfer Tool has a feature that supports differential content top-up where it is possible to transfer only changes made since the previous content transfer activity."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/extracting-content.html#top-up-extraction-process" text="Top Up Extraction"

Follow the steps below to ingest your migration set using the Cloud Acceleration Manager:

   >[!NOTE]
   >Did you remember to log a support ticket for this ingestion? See [Important Considerations Before Using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/guidelines-best-practices-content-transfer-tool.html#important-considerations) for that and other considerations to help make the ingestion successful.

1. Go to Cloud Acceleration Manager. Click your project card and click the Content Transfer card. Navigate to **Ingestion Jobs** and click **New Ingestion** 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-01.png)

1. Review the ingestion checklist and ensure that all the steps are completed. These steps are necessary to ensure a successful ingestion. Proceed to the **Next** step only if the checklist is completed.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/Ingestion-checklist.png)

1. Provide the required information to create an ingestion.

   * Select the migration set that contains the extracted data as the Source.
     * Migration Sets will expire after a prolonged period of inactivity, so it is expected that the ingestion occurs relatively soon after the extraction has been performed. Review [Migration Set Expiry](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/overview-content-transfer-tool.md#migration-set-expiry) for details.
   * Select the destination environment. This environment is where the content of the migration set is ingested. Select the tier. (Author/Publish). Rapid Development Environments are not supported.

   >[!NOTE]
   >The following notes apply to ingesting content:
   > If the source was Author, it is recommended to ingest it into the Author tier on the target. Similarly, if source was Publish, target should be Publish as well.
   > If the target tier is `Author`, the author instance is shut down during the length of the ingestion and becomes unavailable to users (for example, authors or anyone performing maintenance). The reason is to protect the system, and prevent any changes which could either be lost or cause an ingestion conflict. Ensure that your team is aware of this fact. Also note that the environment appears hibernated during the author ingestion.
   > You can run the optional pre-copy step to significantly speed up the ingestion. See [Ingesting with AzCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md#ingesting-azcopy) for more details.
   > If ingesting with pre-copy is used (for S3 or Azure Data Store), it is recommended to run Author ingestion first alone. Doing so speeds up the Publish ingestion when it is run later.
   > Ingestions do not support a Rapid Development Environment (RDE) destination and do not appear as a possible destination choice, even if the user has access to it.

   >[!IMPORTANT]
   > You can initiate an ingestion to the destination environment only if you belong to the local **AEM administrators** group on the destination Cloud Service author service. If you are unable to start an ingestion, see [Unable to Start Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#unable-to-start-ingestion) for more details.

   * Choose the `Wipe` value
     * The **Wipe** option sets the destination's starting point of the ingestion. If **Wipe** is enabled, the destination including all its content is reset to the version of AEM that is specified in Cloud Manager. If not enabled, the destination maintains its current content as the starting point.
     * Note that this option does **NOT** affect how the ingestion of content will be performed. Ingestion always uses a content replacement strategy and _not_ a content merge strategy so, in both **Wipe** and **Non-Wipe** cases, the ingestion of a migration set will overwrite contents in the same path on the destination. For instance, if the migration set contains `/content/page1` and the destination already contains `/content/page1/product1`, the ingestion will remove the entire `page1` path and its subpages, including `product1`, and replace it with the content in the migration set. This means careful planning must be done when performing a **Non-Wipe** ingestion to a destination that contains any content that should be maintained. 

   >[!IMPORTANT]
   > If the setting **Wipe** is enabled for the ingestion, it resets the entire existing repository including the user permissions on the target Cloud Service instance. This resetting is true also for an admin user added to the **administrators** group and that user must be added to the administrators group again to start an ingestion.

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
>abstract="Use the top-up feature to move modified content since the previous content transfer activity. Upon completion of Ingestion, check the logs for any error/warnings. Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe Customer Care."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/viewing-logs.html" text="Viewing Logs"

The Content Transfer Tool has a feature that allows the extraction of differential content by performing a *top-up* of the migration set. This allows the migration set to be modified to include only the content that has changed since the previous extraction without having to extract all the content again.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. If you have used the pre-copy step for the first ingestion, you can skip pre-copy for subsequent top-up ingestions (if the top-up migration set size is less than 200 GB). The reason is that it may add time to the entire process.

To ingest differential content after some ingestions are complete, you must run a [Top-Up Extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process), and then use the ingestion method with the **Wipe** option **disabled**. Be sure to read the **Wipe** explanation above to avoid losing content already on the destination. 

Begin by creating an Ingestion Job and ensure that **Wipe** is disabled during the ingestion, as shown below:

![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam24.png)

## Troubleshooting {#troubleshooting}

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
* It is possible that another process is being run on the instance. For example, if Release Orchestrator is applying an update, the system may be busy and the migration service regularly unavailable. That, and the possibility of corrupting the stage or production instance, is why pausing updates during an ingestion is highly recommended.
* If an [IP Allowlist has been applied](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) through Cloud Manager, it blocks Cloud Acceleration Manager from reaching the migration service. An IP address cannot be added for ingestions because its address is dynamic. Currently, the only solution is to disable the IP allow list while the ingestion is running.
* There may be other reasons that need investigation. If the ingestion still continues to fail, contact Adobe Customer Care.

### Automatic Updates through Release Orchestrator is still enabled

Release Orchestrator automatically keeps environments up to date by applying updates automatically. If the update is triggered when an ingestion is performed, it can cause unpredictable results including the corruption of the environment. A good reason to log a customer support ticket before starting an ingestion (see "Note" above), so that temporarily disabling the Release Orchestrator can be scheduled.

If Release Orchestrator is still running when an ingestion is being started, the user interface presents this message. You may choose to continue anyway, accepting the risk, by checking the field and pressing the button again.

>[!NOTE]
>
> Release Orchestrator is now being deployed to Development environments, so pausing updates on those environments should be done as well.

![image](/help/journey-migration/content-transfer-tool/assets-ctt/error_releaseorchestrator_ingestion.png)

### Top-up Ingestion Failure Due to Uniqueness Constraint Violation

A common cause of a [Top-up Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process) failure is a conflict in node ids. To identify this error, download the ingestion log using the Cloud Acceleration Manager UI and look for an entry like the following:

>java.lang.RuntimeException: org.apache.jackrabbit.oak.api.CommitFailedException: OakConstraint0030: Uniqueness constraint violated property [jcr:uuid] having value a1a1a1a1-b2b2-c3c3-d4d4-e5e5e5e5e5e5: /some/path/jcr:content, /some/other/path/jcr:content

Each node in AEM must have a unique uuid. This error indicates that a node that is being ingested has the same uuid as one that exists elsewhere at a different path on the destination instance.
This situation can happen if a node is moved on the source between an extraction and a subsequent [Top-Up Extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process).
It can also happen if a node on the destination is moved between an ingestion and a subsequent top-up ingestion.

This conflict must be resolved manually. Someone familiar with the content must decide which of the two nodes must be deleted, keeping in mind other content that references it. The solution may require that the top-up extraction is done again without the offending node. 

### Top-up Ingestion Failure Due to Unable to Delete Referenced Node

Another common cause of a [Top-up Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process) failure is a version conflict for a particular node on the destination instance. To identify this error, download the ingestion log using the Cloud Acceleration Manager UI and look for an entry like the following:
>java.lang.RuntimeException: org.apache.jackrabbit.oak.api.CommitFailedException: OakIntegrity0001: Unable to delete referenced node: 8a2289f4-b904-4bd0-8410-15e41e0976a8

This can happen if a node on the destination is modified between an ingestion and a subsequent **Non-Wipe** ingestion such that a new version has been created. If the migration set was extracted with "include versions" enabled, a conflict may occur since the destination now has a more recent version that is being referenced by version history and other content. The ingestion process will be unable to delete the offending version node due to it being referenced.

The solution may require that the top-up extraction is done again without the offending node. Or, creating a small migration set of the offending node, but with "include versions" disabled. 

Best practices indicate that if an **Non-Wipe** ingestion must be run using a migration set that includes versions (i.e. extracted with "include versions"=true), it is crucial that content on the destination is modified as little as possible, until the migration journey is complete. Otherwise, these conflicts can occur.


## What's Next {#whats-next}

When the ingestion has succeeded, AEM indexing will start automatically. See [Indexing after Migrating Content](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/indexing-content.md) for more information.

Once you have completed Ingesting Content into Cloud Service, you can view logs of each step (extraction and ingestion) and look for errors. See [Viewing Logs for a Migration Set](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/viewing-logs.md) to learn more.
