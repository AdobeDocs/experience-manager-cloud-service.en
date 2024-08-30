---
title: Getting Started with Content Transfer Tool
description: Learn how to get started with Content Transfer Tool
exl-id: c0cecf65-f419-484b-9d55-3cbd561e8dcd
feature: Migration
role: Admin
---

# Getting Started with Content Transfer Tool {#getting-started-content-transfer-tool}


## Availability {#availability}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_download"
>title="Download"
>abstract="The Content Transfer Tool can be downloaded as a zip file from the Software Distribution Portal. You can install the package via Package Manager on your source Adobe Experience Manager (AEM) instance. Make sure to download the latest version."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/release-notes/release-notes-current.html" text="Release Notes"
>additional-url="https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html" text="Software Distribution Portal"

The Content Transfer Tool can be downloaded as a zip file from the Software Distribution Portal. You can install the package by way of [Package Manager](/help/implementing/developing/tools/package-manager.md) on your source Adobe Experience Manager (AEM) instance. Make sure to download the latest version. For more details on the latest version, see [Release Notes](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/release-notes/release-notes-current.html).

Only version 2.0.0 and higher is supported, and it is advisable to use the most recent version.

>[!NOTE]
>Download the Content Transfer Tool, from [Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html) portal.

## Source Environment Connectivity {#source-environment-connectivity}

>[!NOTE]
>
>A connection error can also occur if a migration set has been deleted from Cloud Acceleration Manager.

The source AEM instance may be running behind a firewall where it can only reach certain hosts which have been added to an Allow List. To successfully run an extraction, the following endpoints need to be accessible from the instance that is running AEM:

* The Azure blob storage service: `casstorageprod.blob.core.windows.net`

>[!NOTE] 
>If extraction fails due to the following error : "javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target" then this can be resolved by importing the relevant CA certificate.

### Enable SSL Logging {#enable-ssl-logging}

Understanding SSL/TLS connection problems can sometimes be difficult. To troubleshoot connection issues during an extraction process, you can enable SSL logging via the System Console of the source AEM environment by following these steps:

1. Navigate to the Adobe Experience Manager Web Console on your source instance, by going to **Tools > Operations > Web Console** or directly to the URL at *https://serveraddress:serverport/system/console/configMgr*
1. Search for **Content Transfer Tool Extraction Service Configuration**
1. Use the pencil icon button to edit its configuration values 
1. Enable the **Enable ssl logging for extraction** setting, then press **Save**:

   ![image](/help/journey-migration/content-transfer-tool/assets/enable_ssl_logging.png)

>[!NOTE]
>This flag is only for debugging SSL issues. Ensure that the flag is disabled before running the extraction, as it may require a large amount of disk space. This could potentially fill the drive capacity and cause the extraction process to fail.

## Running the Content Transfer Tool {#running-tool}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_demo"
>title="Running Content Transfer Tool"
>abstract="Learn how to use Content Transfer Tool to migrate the content to AEM as a Cloud Service (Author/Publish)."
>additional-url="https://video.tv.adobe.com/v/35460/?quality=12&learn=on" text=" See Demo"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/migration/content-transfer-tool.html#migration" text="Tutorial - using Content Transfer Tool"

The following section applies to the new version of the Content Transfer Tool. Follow this section to learn how to use the Content Transfer Tool to migrate content to AEM as a Cloud Service:

### Extraction Setup Phase {#extraction-setup-phase}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_extraction_setup"
>title="Extraction Setup Phase"
>abstract="Learn how to create and manage a migration set and how to copy the extraction key."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/migration/content-transfer-tool.html#migration" text="Tutorial - using Content Transfer Tool"

<!-- Contextualhelp id "aemcloud_ctt_extraction_setup" must be added here -->

1. Log into Cloud Acceleration Manager (CAM) and click the CAM project that you had created previously to assess your readiness to move to AEM as a Cloud Service. If you haven't created a CAM project, refer to Creating and Managing a Project in CAM.

1. Click the **Content Transfer** card to open the Migration Set List view.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam1.png)

1. Create a Migration Set by clicking **Create Migration Set**.

   >[!NOTE]
   >
   >A maximum of 10 migration sets, including expired sets, can be created per project in Cloud Acceleration Manager.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam2.png)

   The following dialog box is presented. Notice that a migration set will expire after a prolonged period of inactivity. After warnings are displayed on the project card and the migration job table rows for a time period, the migration set will expire and its data will no longer be available. Review [Migration Set Expiry](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/overview-content-transfer-tool.md#migration-set-expiry) for details.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam3.png)

   >[!NOTE]
   >
   >The name must follow the same conventions of an AEM node so cannot contain any of these characters: . / : [ ] | *

1. You should now see your migration list in the list view. Select the three dots symbol (**...**) to open the drop-down and select **Copy Extraction key**. You need this key during the Extraction phase. Copy this Extraction key.

   >[!NOTE]
   >
   >The extraction key enables your source AEM environment to securely connect to the migration set. Treat this key with the same care that you would a password, and never share it over an unsecured medium like email.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam4.png)

### Populating the Migration Set {#populating-the-migration-set}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_populate_migrationset" 
>title="Populate Migration Set"
>abstract="After creating a migration set, it must be populated with the content from the source instance that must be moved to the AEM as a Cloud Service environment. To do this, the Content Transfer Tool must be installed on the source instance."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/extracting-content.html" text="Extracting Content"

To populate the migration set you created in the Cloud Acceleration Manager, install the latest version of the Content Transfer Tool on your source Adobe Experience Manager (AEM) instance. To learn how to populate the migration set, follow this section.

1. After installing the latest version of the Content Transfer Tool on your source Adobe Experience Manager instance, go to **Operations - Content Migration**

1. Click **Create Migration Set**.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam5.png)

1. Paste the extraction key that was copied from CAM earlier into the Extraction key input field of **Create Migration Set** form. After you do this, the Migration set name and Cloud Acceleration Manager (CAM) Project name fields are automatically populated. These should match the Migration Set name in CAM and the CAM project name that you created. You can now add content paths. After you have added content paths, save the migration set. You can run the extraction with either versions included or excluded.

   >[!NOTE]
   >
   >Make sure that the extraction key is valid and is not near its expiration. You can get this information in the **Create Migration Set** dialog after you paste the extraction key. If you get a connection error, see [Source Environment Connectivity](#source-environment-connectivity) for more information.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam6.png)

1. Next, select the following Parameters to create a Migration Set:

   1. **Include Version**: Select as required. When versions are included, the path `/var/audit` is automatically included to migrate audit events.

      ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam7.png)

      >[!NOTE]
      >If you intend to include versions as part of a migration set, and are performing top-ups with `wipe=false`, then you must disable version purging due to a current limitation in the Content Transfer Tool. If you prefer to keep version purge enabled and are performing top-ups into a migration set, then you must perform the ingestion as `wipe=true`.


   1. **Paths to be included**: Use path browser to select paths which need to be migrated. Path picker accepts input by typing or by selection. 

      >[!IMPORTANT]
      >Following paths are restricted while creating a migration set:
      >* `/apps`
      >* `/libs`
      >* `/home`
      >* `/etc` (some `/etc` paths are allowed to be selected in CTT)

1. Click **Save** after you populate all the fields in the **Create Migration Set** details screen.

<!-- 1. You will view your migration set in the **Content Transfer** wizard, as shown in the figure below.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ctt07.png)

   All the existing migration sets are displayed on the **Content Transfer** wizard with their current status and status information. You may see some of these icons described below.

   * A *red cloud* indicates that you cannot complete the extraction process.
   * A *green cloud* indicates that you can complete the extraction process.
   * A *yellow icon* indicates that you did not create the existing migration set and the specific one is created by some other user in the same instance.

1. Select a migration set and click **Properties** to view or edit the migration set properties. While editing properties, it is not possible to change the **Migration Set name** or the **Service URL**. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ctt06.png) -->

### Determining migration set size {#migration-set-size}

After creating a migration set, it is highly recommended to run a size check on the migration set before starting an Extraction process. 
By running a size check on the migration set, you are able to:

* Determine if there is sufficient disk space in the `crx-quickstart` subdirectory to complete extraction successfully.
* Determine if the migration set size falls within supported product limits and avoid failed content ingestions.

Follow the steps below to run a size check:

1. Select a migration set and click **Check Size**. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam8.png)

1. This opens up the **Check Size** dialog.  

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam9.png)

1. Click **Check Size** to start the process. You will then return to the migration set list view, and you should see a message indicating that **Check Size** is running.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam10.png)

1. After **Check Size** process is completed, the status changes to **FINISHED**. Select the same migration set and click **Check Size** to view results. Below is an example of **Check Size** results with no warnings.
 
   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam11.png)
   
 1. If the **Check Size** results indicate that either there is insufficient disk space, or the migration set exceeds product limits, or both, a **WARNING** status is displayed.

<!--   ![image](/help/journey-migration/content-transfer-tool/assets/CTT_CheckSize_image6.png)
   
   Below is an example of **Check Size** results with warnings.
 
   ![image](/help/journey-migration/content-transfer-tool/assets/CTT_CheckSize_image7.png) -->


## What's Next {#whats-next}

Once you have learned how to create a migration set, you are now ready to learn about Extraction and Ingestion Processes in Content Transfer Tool. Before you learn these processes, you must review [Handling Large Content Repositories](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/handling-large-content-repositories.md) to significantly speed-up the extraction and ingestion phases of the content transfer activity to move content to AEM as a Cloud Service.
