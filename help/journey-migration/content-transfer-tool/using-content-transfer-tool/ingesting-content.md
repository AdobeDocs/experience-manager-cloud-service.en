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
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html#top-up-ingestion-process" text="Top Up Ingestion"

Follow the steps below to ingest your migration set from the Content Transfer Tool:

   >[!NOTE]
   >Did you remember to log a support ticket for this ingestion? See [Important Considerations Before Using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/guidelines-best-practices-content-transfer-tool.html#important-considerations) for that and other considerations to help make the ingestion successful.

1. Go to Cloud Acceleration Manager. Click on your project card and click on the Content Transfer card. Navigate to **Ingestion Jobs** and click on **New Ingestion** 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-01.png)

1. Review the ingestion checklist and ensure that all the steps have been completed. These are necessary steps to ensure a successful ingestion. Proceed to the **Next** step only if the checklist is completed.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/Ingestion-checklist.png)

1. Provide the required information to create a new ingestion.

   * Select the migration set that contains the extracted data as the Source.
     * Migration Sets will expire after a prolonged period of inactivity, so it is expected that the ingestion occurs relatively soon after the extraction has been performed. Review [Migration Set Expiry](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/overview-content-transfer-tool.md#migration-set-expiry) for details.
   * Select the destination environment. This environment is where the content of the migration set is ingested. Select the tier. (Author/Publish). Rapid Development Environments are not supported.

   >[!NOTE]
   >The following notes apply to ingesting content:
   > If the source was Author, it is recommended to ingest it into the Author tier on the target. Similarly, if source was Publish, target should be Publish as well.
   > If the target tier is `Author`, the author instance is shutdown during the length of the ingestion and becomes unavailable to users (for example, authors or anyone performing maintenance). The reason is to protect the system, and prevent any changes which could either be lost or cause an ingestion conflict. Ensure that your team is aware of this fact. Also note that the environment appears hibernated during the author ingestion.
   > You can run the optional pre-copy step to significantly speed up the ingestion phase. Refer to [Ingesting with AzCopy](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md#ingesting-azcopy) for more details.
   > If ingesting with pre-copy is used (for S3 or Azure Data Store), it is recommended to run Author ingestion first alone. Doing so speeds up the Publish ingestion when it is run later.
   > Ingestions do not support a Rapid Development Environment (RDE) destination and do not appear as a possible destination choice, even if the user has access to it.

   >[!IMPORTANT]
   > The following important notices apply to ingesting content:
   > You can initiate an ingestion to the destination environment only if you belong to the local **AEM administrators** group on the destination Cloud Service author service. If you are unable to start an ingestion, refer to [Unable to Start Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#unable-to-start-ingestion) for more details.
   > If the setting **Wipe** is enabled before ingestion, it deletes the entire existing repository and creates a new repository to ingest content into. This means that it resets all settings including permissions on the target Cloud Service instance. This is also true for an admin user added to the **administrators** group. You must be re-added to the administrators group to start an ingestion.

1. Click on **Ingest**

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam22.png)

1. You can then monitor the Ingestion phase from the Ingestion Jobs list view and use the ingestion's action menu to view the log as the ingestion progresses.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam23.png)

1. Click on **(i)** button in the row to get more information about the ingestion job. You can see the duration of each step of the Ingestion when it is executing or completed by clicking on **...** and then on **View durations**. The information from the extraction is also shown to realize what is being ingested.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam23b.png)

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
   
   Also, refer to [Important Considerations for Using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/guidelines-best-practices-content-transfer-tool.html#important-considerations) to learn more.

1. Once the ingestion is complete, the status under **Author ingestion** updates to **FINISHED**.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ingestion-05.png) -->

## Top Up Ingestion {#top-up-ingestion-process}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_ingestion_topup"
>title="Top Up Ingestion"
>abstract="Use the top up feature to move modified content since the previous content transfer activity. Upon completion of Ingestion, check the logs for any error/warnings. Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe Customer Care."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/viewing-logs.html" text="Viewing Logs"

The Content Transfer Tool has a feature that supports differential content *top-up* where it is possible to transfer only changes made since the previous content transfer activity.

>[!NOTE]
>After the initial content transfer, it is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. If you have used the pre-copy step for the 1st full ingestion, you can skip pre-copy for subsequent top-up ingestions (if the top-up migration set size is less than 200GB) because it may add time to the entire process.

Once the ingestion process is complete, to ingest the delta content you will need to run a [Top-Up Extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process) and then use the top-up ingestion method. 

You can do this by creating a new Ingestion Job and ensure that **Wipe** is disabled during the Ingestion phase, as shown below:

![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam24.png)

## Troubleshooting {#troubleshooting}

### CAM Unable to Retrieve the Migration Token {#cam-unable-to-retrieve-the-migration-token}

The automatic retrieval of the migration token may fail for different reasons, including you [setting up an IP allow list via Cloud Manager](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) on the target Cloud Service environment. In such scenarios you will see the following dialog when you attempt to start an ingestion:

![image](/help/journey-migration/content-transfer-tool/assets-ctt/troubleshooting-token.png)

You will need to retrieve the migration token manually by clicking on the "Get token" link on the dialog. This will open another tab that displays the token. You can then copy the token and paste it into the **Migration token input** field. Now, you should be able to start the ingestion.

>[!NOTE]
>
>The token is available to users who belong to the local **AEM administrators** group on the destination Cloud Service author service. 

### Unable to Start Ingestion {#unable-to-start-ingestion}

You can initiate an ingestion to the destination environment only if you belong to the local **AEM administrators** group on the destination Cloud Service author service. If you don't belong to the AEM administrators group, you will see an error as shown below when you try to start an ingestion. You can either ask your administrator to add you to the local **AEM administrators** or ask for the token itself, which you can then paste into the **Migration token input** field.

![image](/help/journey-migration/content-transfer-tool/assets-ctt/error_nonadmin_ingestion.png)

### Unable to reach migration service {#unable-to-reach-migration-service}

After an ingestion is requested, a message like the following may be presented to the user: "The migration service on the destination environment is currently unreachable. Please try again later or contact Adobe support."

![image](/help/journey-migration/content-transfer-tool/assets-ctt/error_cannot_reach_migser.png)

This indicates that the Cloud Acceleration Manager was unable to reach the target environment's migration service to start the ingestion. This can happen for a number of reasons.

>[!NOTE]
> 
> The "Migration token" field is shown because in a few cases retrieving that token is what is actually disallowed. By allowing it to be manually provided, it may allow the user to start the ingestion quickly, without any additional help. If the token is provided, and the message still appears, than retrieving the token was not the problem.

* AEM as a Cloud Service maintains the environment state, and occasionally may need to restart the migration service for a number of normal reasons. If that service is restarting, it cannot be reached, but is usually available soon.
* It is possible another process is being run on the instance. For instance, if Release Orchestrator is applying an update, the system may be busy and the migration service regularly unavailable. That, and the possibility of corrupting the stage or production instance, is why pausing updates during an ingestion is very strongly recommended.
* If an [IP Allowlist has been applied](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) through Cloud Manager, it will block Cloud Acceleration Manager from reaching the migration service. An IP address cannot be added for ingestions because its address is very dynamic. Currently, the only solution is to disable the IP allow list while the ingestion is running.
* There may be other reasons that need investigation. If the ingestion still continues to fail, please contact Adobe Customer Care.

### Automatic Updates through Release Orchestrator is still enabled

Release Orchestrator automatically keeps environments up to date by applying updates automatically. If the update is triggered when an ingestion is being performed, it can cause unpredictable results including the corruption of the environment. That is one of the reasons a support ticket should be logged before starting an ingestion (see "Note" above), so that temporarily disabling the Release Orchestrator can be scheduled.

If Release Orchestrator is still running when an ingestion is being started, the UI will present this message. You may choose to continue anyway, accepting the risk, by checking the field and pressing the button again.

>[!NOTE]
>
> Release Orchestrator is now being deployed to Development environments, so pausing updates on those environments should be done as well.

![image](/help/journey-migration/content-transfer-tool/assets-ctt/error_releaseorchestrator_ingestion.png)

### Top-up Ingestion Failure Due to Uniqueness Constraint Violation

A common cause of a [Top-up Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process) failure is a conflict in node ids. To identify this error, download the ingestion log using the Cloud Acceleration Manager UI and look for an entry like the following:

>java.lang.RuntimeException: org.apache.jackrabbit.oak.api.CommitFailedException: OakConstraint0030: Uniqueness constraint violated property [jcr:uuid] having value a1a1a1a1-b2b2-c3c3-d4d4-e5e5e5e5e5e5: /some/path/jcr:content, /some/other/path/jcr:content

Each node in AEM must have a unique uuid. This error indicates that a node that is being ingested has the same uuid as one that already exists at a different path on the target instance.
This can happen if a node is moved on the source between an extraction and a subsequent [Top-Up Extraction](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/extracting-content.md#top-up-extraction-process).
It can also happen if a node on the target is moved between an ingestion and a subsequent top-up ingestion.

This conflict must be resolved manually. Someone familiar with the content must decide which of the two nodes must be deleted, keeping in mind other content that references it. The solution may require that the top-up extraction is done again without the offending node. 

### Top-up Ingestion Failure Due to Unable to Delete Referenced Node

Another common cause of a [Top-up Ingestion](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/ingesting-content.md#top-up-ingestion-process) failure is a version conflict for a particular node on the target instance. To identify this error, download the ingestion log using the Cloud Acceleration Manager UI and look for an entry like the following:
>java.lang.RuntimeException: org.apache.jackrabbit.oak.api.CommitFailedException: OakIntegrity0001: Unable to delete referenced node: 8a2289f4-b904-4bd0-8410-15e41e0976a8

This can happen if a node on the target is modified between an ingestion and a subsequent top-up ingestion such that a new version has been created. If the ingestion has "include versions" enabled, a conflict may occur since the target now has a more recent version that is being referenced by version history and other content. The ingestion process will be unable to delete the offending version node due to it being referenced.

The solution may require that the top-up extraction is done again without the offending node. Or, creating a small migration set of the offending node, but with "include versions" disabled. 

Best practices indicate that if an ingestion must be run with wipe=false and "include versions"=true it is crucial that content on the target is modified as little as possible, until the migration journey is complete. Otherwise, these conflicts can occur.


## What's Next {#whats-next}

Once you have completed Ingesting Content into Target, you can view logs of each step (extraction and ingestion) and look for errors. See [Viewing Logs for a Migration Set](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/viewing-logs.html) to learn more.
