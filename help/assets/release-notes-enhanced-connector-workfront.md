---
title: Release Notes for [!DNL Workfront for Experience Manager enhanced connector]
description: Release Notes for [!DNL Workfront for Experience Manager enhanced connector]
exl-id: 12de589d-fe5d-4bd6-b96b-48ec8f1ebcb6
feature: Release Information
role: Admin
---
# Release Notes for [!DNL Workfront for Experience Manager enhanced connector] {#release-notes-enhanced-connector-workfront}

The following section outlines the general Release Notes for [!DNL Workfront for Experience Manager enhanced connector].

The release date for the latest version 1.9.20 of [!DNL Workfront for Experience Manager enhanced connector] is September 06, 2024.

## Release highlights {#release-highlights}

The latest version of the [!DNL Workfront for Experience Manager enhanced connector] includes the following bug fix:

* MIME type is lost while uploading and creating a new version of an existing asset.

>[!NOTE]
>
>AEM 6.4 has reached the end of extended support. See our [technical support periods](https://helpx.adobe.com/support/programs/eol-matrix.html). Find the supported versions [here](https://experienceleague.adobe.com/docs/?lang=en).

>[!IMPORTANT]
>
>Adobe recommends you [upgrade to the latest 1.9.20 version](/help/assets/workfront-connector-install.md) of the [!DNL Workfront for Experience Manager enhanced connector].

## Known Issues {#known-issues}

* While configuring project linked folders with AEM 6.4, Experience Manager do not save the values for **[!UICONTROL sub-folders]** and **[!UICONTROL Create linked folder in projects with portfolio]** fields. The value for the **[!UICONTROL sub-folders]** field updates to **[!UICONTROL undefined]** and the value for the **[!UICONTROL Create linked folder in projects with portfolio]** field updates to **[!UICONTROL Default Portfolio]** automatically after saving the configuration.

* When you are using the classic Workfront experience, the **[!UICONTROL Send to]** option available in the **[!UICONTROL More]** drop-down list does not allow you to select the target destination within Experience Manager. The **[!UICONTROL Send to]** option works correctly using the **[!UICONTROL Document Actions]** drop-down list. The **[!UICONTROL Send to]** option works correctly for **[!UICONTROL More]** drop-down list and the **[!UICONTROL Document Actions]** drop-down list available in the new Workfront experience.

## Previous releases {#previous-releases}

### April 2024 release {#april-2024-release}

* Failure to close HTTP clients is causing out-of-memory issues.


### March 2024 release {#march-2024-release}

* Processing multi-asset uploads from Workfront encounters issues.
* Not adding closing quotes when using Workfront to search for folders in Experience Manager results in `SERVER_ERROR`.

### February 2024 release {#february-2024-release}

* Enable toggle feature to allow AEM Cloud customers to configure and set up a connector.

* Closing the `resourceResolver` without explicitly closing the underlying session causes session leaks in AEM instances. It is crucial to explicitely close the session, as auto-closing the Resource Resolver does not implicitly close the session.

### January 2024 release {#january-2024-release}

* The [!DNL Workfront] configuration in [!DNL CRX DE] currently does not store the `project ID`, causing errors when applying read-only permission. Learn more about how to [configure permissions](https://experienceleague.adobe.com/docs/experience-manager-65/content/assets/integrations/workfront-connector-configure.html#linked-folders).

* No public documentation on how to add custom property to the out of the box index definition. Learn more about [adding custom property](https://experienceleague.adobe.com/docs/experience-manager-65/content/assets/integrations/workfront-connector-configure.html#metadata-schema-mapping).

* Deleting connection configurations on the enhanced connector significantly affects event subscriptions and other saved configurations, causing them to point to an old URL.

* Installing the forms add-on package does not install the **[!UICONTROL Toggle Router]**, leading to the failure of the [!DNL WFEC AMS environment Toggle] feature.

* Enabling event subscriptions on EWC setup results in repeated API call failures with `HTTP 400` error when setting up [!DNL Workfront] enhanced connector for the 1st time.

* Deleting comments on linked folder assets at Workfront fails to find the linked folder path on AEM.

* Insufficient support for large file assets in AEM results in a 4-byte size issue.

* No request time processing for critical flows in linked folder, document update, and note update.

### November 2023 release {#nov-2023-release}

* While viewing the list of AEM folders, the dialog takes more than a minute to load.
* Authorized [!DNL Workfront] users are consistently receiving authentication failure error logs.

### October 2023 release {#october-2023-release}

* When event subscriptions are disabled under Advanced Settings, you can still select the options to **Subscribe to document update events to update AEM asset metadata**, **Publish all project assets to Brand Portal upon project completion**, and **Enable Comment Sync**.

* Some of the assets stored in Experience Manager do not render appropriately when you preview them in Workfront.

* While reconfiguring Experience Manager connection with Workfront, event subscriptions such as comment sync update, delete, document update are not created successfully.

* Major API performance improvements for linked folder creation, update, enable linked folder, comment sync enable and disable, advance settings save on connector.

### September 2023 release {#september-2023-release}

* Experience Manager enhanced connector fetches all event subscriptions from Workfront while deleting an event subscription for a project, which leads to a performance impact on the application.

* When an asset is sent from Workfront to Experience Manager, the asset MIME type is not set to `dc:format` attribute within Experience Manager.

* Workfront project IDs stored on Experience Manager enhanced connector include duplicates.

### August 2023 release {#august-2023-release}

* Unable to create linked folders in Experience Manager, as there is no user account associated with the linked folder.

* Race conditions during metadata updates for an asset in Experience Manager.

### June 2023 release {#june-2023-release}

* When you have advanced networking configured, there are issues while sending content from Adobe Workfront to AEM as a Cloud Service.


### May 2023 release {#may-2023-release}

* Workfront returns a 409 HTTP response for duplicate event subscriptions based on a REST call from Experience Manager to Workfront, which leads to a null pointer exception.

### April 2023 release {#april-2023-release}

[!DNL Workfront for Experience Manager enhanced connector] version 1.9.9, released on April 10, 2023 includes the following updates:

* Experience Manager displays an `DateTimeParseException` exception when it receives last modified date from Workfront during linked folder creation.

* Issues while creating multiple linked project folders within a short duration.

* Inability to configure a threshold limit on the number of new set of project linked folders.

### March 2023 release {#march-2023-release}

[!DNL Workfront for Experience Manager enhanced connector] version 1.9.8, released on March 03, 2023 includes the following updates:

* Performance improvements in Experience Manager while creating project linked folders in Workfront.

* Comment deletions in Workfront are now reflected in Experience Manager.

* Capability to manage blocking net-new customers on Experience Manager as a Cloud Service from configuring the connector.

### January 2023 release {#january-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] version 1.9.7, released on February 02, 2023 includes the following updates:

* The metadata editor does not list Workfront custom forms properties after installing the 1.9.6 release.

* The dev console displays `/content/dam/jcr:content/metadata/wfProjectURL not found` error message after installing the Workfront enhanced connector and opening the Assets home page.

### December 2022 release {#december-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] version 1.9.6, released on December 09, includes the following updates:

**Enhancement**

<!--

* Workfront enhanced connector now lets you use new search parameters to be more specific while defining folder names on large repositories.

-->

* Workfront enhanced connector now supports performing full-text search on assets and folders.

**Bug Fixes**

* The Document Version metadata does not synchronize appropriately between Workfront and Experience Manager.
* Issues while creating a folder that is linked to Experience Manager in Workfront when the folder is using a schema that is missing definition in the global configuration.
* The metadata schema editor form stops responding when you click any field due to a load time that is longer than expected. Added specific OSGi configuration for custom forms to resolve the issue. The names of the custom forms that you add to the metadata schema editor are available in the logs.

### November 2022 release {#november-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] version 1.9.5, released on November 11, includes the following updates:

* When you define only one value for a multi-value field in Workfront, the field value is not appropriately mapped to Experience Manager.

* Experience Manager displays the `SERVER_ERROR` on the **[!UICONTROL Link External Files and Folders]** screen while accessing the asset folders due to invalid permissions on `/content/dam/collections`.

* Enabling the **[!UICONTROL Publish Assets to Brand Portal]** option on the Workfront enhanced connector configuration page creates an incorrect event. The event does not get deleted even after disabling the option.

  To resolve the issue:
  
  1. Upgrade to version 1.9.5 of the enhanced connector.

  1. Disable the **[!UICONTROL Publish Assets to Brand Portal]** option under advanced settings.

  1. Enable the **[!UICONTROL Publish Assets to Brand Portal]** option.

  1. Delete the wrong event subscriptions.
  
     1. Perform GET calls to `/attask/eventsubscription/api/v1/subscriptions?page=<page-number>`

        Execute one API call for each page number.

     1. Search for the following text to find event subscriptions that match the following URL and do not have an `objId`:

        ```
             "objId": "",
            "url": "<your-aem-domain>/bin/workfront-tools/events/linkedfolderprojectupdate<your-aem-domain>/
        ```

        Ensure that the content between `"objId": "",` and `"url"` matches the JSON response. The recommended method to do this is to copy from any Event Subscription that has an `objId` and then delete the number.

     1. Note the event subscription ID.

     1. Delete the wrong event subscription. Make a Delete API call to `<your-aem-domain>/attask/eventsubscription/api/v1/subscriptions/<event-subscription-ID-from-previous-step>`

        `200` as the response code signifies successful deletion of wrong event subscriptions.
    >[!NOTE]
    >
    >If you have already deleted the wrong event subscriptions before executing the steps mentioned in this procedure, you can skip the last step of this procedure.

### October 2022 release {#october-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] version 1.9.4, released on October 07, includes the following updates:

* Unable to view Event Subscriptions tab on the enhanced connector configuration page due to many events.

* Workfront is not able to fetch the list of existing folders in a project, which is resulting in creation of duplicate folders.

### September 2022 release {#september-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] version 1.9.3, released on September 16, includes the following updates:

* Unable to upload a file that is more than 8 GB.
* Issues while auto-publishing assets that are sent from Workfront to AEM.
* The Root path field is not available for the Tags field while editing a default Metadata Schema Form.
* Issues while adding new versions in Workfront using AEM workflows.
* When you execute an AEM search for assets available in Workfront, AEM displays an error message.
* When you create an AEM workflow for task creation from an asset and do not define a parent task name, the task is not created in Workfront.

### August 2022 release {#august-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] version 1.9.2, released on August 03, includes the following updates:

* The **[!UICONTROL Upload Document]** workflow step fails to attach a document to Workfront. 

* The **[!UICONTROL Upload Document]** workflow step fails to attach a document to Tasks and Issues in Workfront. The workflow step attaches a document to Projects successfully.

### July 2022 release {#july-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] version 1.9.1 includes the following updates:

* Added support for authentication between Experience Manager and Workfront applications using Workfront API key for instances that are migrated to Adobe IMS.

* When you link external files or folders, the Workfront application displays the `SERVER_ERROR` error message. The error message refers to an unauthorized exception due to a mismatch in API keys.

* When you execute a Create Task workflow for an asset, the Null Pointer exception displays in the log messages.

* When you enable the `Replace Spaces with DASH` configuration option under Advanced Settings in Experience Manager, it results in duplicate folder creation in Workfront.

### June 2022 release {#june-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] now includes the following updates:

* When you upload via a linked folder or use the `Send To` action available in Workfront to upload assets to Experience Manager as a Cloud Service, the assets get corrupted and cannot be opened in Adobe Photoshop.

### March 2022 release {#march-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] now includes the following updates:

* You can now create linked folders between Adobe Workfront and AEM Assets as a Cloud Service even if there are multiple project linked folder configurations.

* Added support for event subscription pagination.

* Added support for AEM 6.4.x.

* Added support for proxy environments.

* Several bug fixes based on partner and customer feedback.

>[!MORELIKETHIS]
>
>* [Integrate [!DNL Workfront for Experience Manager enhanced connector] with Experience Manager 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/integrations/workfront-integrations.html?lang=en)
