---
title: Getting Started with Content Transfer Tool (Legacy)
description: Getting Started with Content Transfer Tool
hide: yes
hidefromtoc: yes
---
# Getting Started with Content Transfer Tool (Legacy) {#getting-started-content-transfer-tool}


## Availability {#availability}

The Content Transfer Tool can be downloaded as a zip file from the Software Distribution Portal. You can install the package via [Package Manager](/help/implementing/developing/tools/package-manager.md) on your source Adobe Experience Manager (AEM) instance. Make sure to download the latest version. For more details on the latest version, refer to [Release Notes](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html).

>[!NOTE]
>Download the Content Transfer Tool, from [Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html) portal.

## Source Environment Connectivity {#source-environment-connectivity}

The source AEM instance may be running behind a firewall where it can only reach certain hosts which have been added to an Allow List. In order to successfully run an extraction, the following endpoints will need to be accessible from the instance that is running AEM:

* The target AEM as a Cloud Service environment: `author-p<program_id>-e<env_id>.adobeaemcloud.com`
* The Azure blob storage service: `*.blob.core.windows.net`
* The User Mapping IO endpoint: `usermanagement.adobe.io`

To test connectivity to the target AEM as a Cloud Service environment, issue the following cURL command from the shell of the source instance (replace `program_id`, `environment_id`, and `migration_token`):

`curl -i https://author-p<program_id>-e<environment_id>.adobeaemcloud.com/api/migration/migrationSet -H "Authorization: Bearer <migration_token>"`

>[!NOTE]
>If an `HTTP/2 200` is received, a connection to AEM as a Cloud Service was successful.

## Running the Content Transfer Tool {#running-tool}

>[!VIDEO](https://video.tv.adobe.com/v/35460/?quality=12&learn=on)


Follow this section to learn how to use Content Transfer Tool to migrate the content to AEM as a Cloud Service (Author/Publish):

1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **Content Migration**.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ctt01.png)

1. Select the **Content Transfer** option from **Content Migration** wizard.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ctt02.png)


1. The console below appears when you create the first migration set. Click on **Create Migration Set** to create a new migration set. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ctt03.png)
   
   >[!NOTE]
   >If you have existing migration sets, the console will display the list of existing migration sets with their current status.


1. Populate the fields in **Create Migration Set** screen, as described below.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ctt04.png)
   
   1. **Name**: Enter the name of the migration set.
      >[!NOTE]
      >No special characters are allowed for the migration set name.

   1. **Cloud Service Configuration**: Enter the destination AEM as a Cloud Service Author URL.

      >[!NOTE]
      >You can create and maintain a maximum of ten migration sets at a time during the content transfer activity.
      >Additionally, you have to create a migration separately for each of the specific environments - *Stage*, *Development*, or *Production*.

   1. **Access Token**: Enter the access token.

      >[!NOTE]
      >You can retrieve the access token by using the **Open access token** button. You need to ensure that you belong to the 'Administrators' group in the target Cloud Service instance.

   1. **Parameters**: Select the following parameters to create the migration set:

      1. **Include Version**: Select as required. When versions are included, the path `/var/audit` is automatically included to migrate audit events.

         ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ctt05.png)

         >[!NOTE]
         >If you intend to include versions as part of a migration set, and are performing top-ups with `wipe=false`, then you must disable version purging due to a current limitation in the Content Transfer Tool. If you prefer to keep version purge enabled and are performing top-ups into a migration set, then you must perform the ingestion as `wipe=true`.

         
       1. **Paths to be included**: Use path browser to select paths which need to be migrated. Path picker accepts input by typing or by selection.

            >[!IMPORTANT]
            >Following paths are restricted while creating a migration set:
            >* `/apps`
            >* `/libs`
            >* `/home`
            >* `/etc` (some `/etc` paths are allowed to be selected in CTT)

1. Click on **Save** after you populate all the fields in the **Create Migration Set** details screen.

1. You will view your migration set in the **Content Transfer** wizard, as shown in the figure below.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ctt07.png)

   All the existing migration sets are displayed on the **Content Transfer** wizard with their current status and status information. You may see some of these icons described below.

   * A *red cloud* indicates that you cannot complete the extraction process.
   * A *green cloud* indicates that you can complete the extraction process.
   * A *yellow icon* indicates that you did not create the existing migration set and the specific one is created by some other user in the same instance.

1. Select a migration set and click on **Properties** to view or edit the migration set properties. While editing properties, it is not possible to change the **Migration Set name** or the **Service URL**. 

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/ctt06.png)
   
### Determining migration set size and disk space {#migration-set-size}

After creating a migration set, it is highly recommended to run a size check on the migration set before starting an Extraction process. 
By running a size check on the migration set, you will be able to:
* Determine if there is sufficient disk space in the `crx-quickstart` subdirectory to complete extraction successfully.
* Determine if the migration set size falls within supported product limits and avoid failed content ingestions.

Follow the steps below to run a size check:

1. Select a migration set and click on **Check Size**. 

   ![image](/help/journey-migration/content-transfer-tool/assets/CTT_CheckSize_image1.png)

1. This will open up the **Check Size** dialog.  

   ![image](/help/journey-migration/content-transfer-tool/assets/CTT_CheckSize_image2.png)

1. Click on **Check Size** to start the process. You will then return to the migration set list view and you should see a message indicating that **Check Size** is running.

   ![image](/help/journey-migration/content-transfer-tool/assets/CTT_CheckSize_image3.png)


1. Once **Check Size** process is completed, the status will change to either **FINISHED**. Select the same migration set and click on **Check Size** to view results.

   ![image](/help/journey-migration/content-transfer-tool/assets/CTT_CheckSize_image4.png)
   
   Below is an example of **Check Size** results with no warnings.
 
   ![image](/help/journey-migration/content-transfer-tool/assets/CTT_CheckSize_image5.png)
   
 1. If the **Check Size** results indicate that either there is insufficient disk space and/or the migration set exceeds product limits, **WARNING** status will be displayed.

   ![image](/help/journey-migration/content-transfer-tool/assets/CTT_CheckSize_image6.png)
   
   Below is an example of **Check Size** results with warnings.
 
   ![image](/help/journey-migration/content-transfer-tool/assets/CTT_CheckSize_image7.png)


## What's Next {#whats-next}

Once you have learned how to create a migration set, you are now ready to learn about Extraction and Ingestion Processes in Content Transfer Tool. Before you learn these processes, you must review [Handling Large Content Repositories](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en) to significantly speed up the extraction and ingestion phases of the content transfer activity to move content to AEM as a Cloud Service.
