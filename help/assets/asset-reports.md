---
title: Reports about usage and sharing
description: Reports about your assets in [!DNL Adobe Experience Manager Assets] that help you understand usage, activity, and sharing of your digital assets.
contentOwner: AG
feature: Asset Reports,Asset Management
role: Admin,User
exl-id: ef617b01-0019-4379-8d58-c03215d7e28f
---
# Asset reports {#asset-reports}

Asset reporting lets you assess the utility of your [!DNL Adobe Experience Manager Assets] deployment. With [!DNL Assets], you can generate various reports for your digital assets. The reports provide useful information about your system’s usage, how users interact with assets, and which assets are <!-- downloaded and --> shared.

Use the information in the reports to derive key success metrics to measure the adoption of [!DNL Assets] within your enterprise and by customers.

The [!DNL Assets] reporting framework uses [!DNL Sling] jobs to asynchronously process report requests in an ordered manner. It is scalable for large repositories. Asynchronous report processing increases the efficiency and speed with which reports are generated.

The report management interface is intuitive and includes fine-grained options and controls to access archived reports and view report run statuses (success, failed, and queued).

When a report is generated, you are notified via <!-- through an email (optional) and --> an inbox notification. You can view, download, or delete a report from the report listing page, where all the previously generated reports are displayed.

## Generate reports {#generate-reports}

[!DNL Experience Manager Assets] generates the following standard reports for you:

* Upload
* Expiration
* Modification
* Publish
* [!DNL Brand Portal] publish
* Disk Usage
* Files
* Link Share

<!-- Removed download report.
* Upload
* Download
* Expiration
* Modification
* Publish
* [!DNL Brand Portal] publish
* Disk Usage
* Files
* Link Share
-->

[!DNL Adobe Experience Manager] administrators can easily generate and customize these reports for your implementation. An administrator can follow these steps to generate a report:

1. In [!DNL Experience Manager] interface, click **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Reports]**.

   ![Tools page to navigate assets report](assets/navigation.png)

1. On the [!UICONTROL Asset Reports] page, click **[!UICONTROL Create]** from the toolbar.
1. From the **[!UICONTROL Create Report]** page, choose the report you want to create and click **[!UICONTROL Next]**.

   ![Select report type](assets/choose_report.png)

1. Configure report details such as title, description, thumbnail, and folder path in the CRX repository where the report is stored. By default, the folder path is `/content/dam`. You can specify a different path.

   ![Page to add report details](assets/report_configuration.png)

   Choose the date range for your report. You can choose to generate the report now or at a future date and time.

   >[!NOTE]
   >
   >If you choose to schedule the report later, ensure that you specify the date and time in the Date and Time fields. If you do not specify any value, the report engine treats it as a report that is to be generated instantly.

   Configuration fields may differ based on the type of report you create. For example, the **[!UICONTROL Disk Usage]** report provides options to include asset renditions when calculating the disk space used by assets. You can choose to include or exclude assets in sub-folders for disk usage calculation.

   >[!NOTE]
   >
   >The **[!UICONTROL Disk Usage]** report does not include date range fields because it indicates current disk space usage only.

   ![Details page of Disk Usage report](assets/disk_usage_configuration.png)

   When you create the **[!UICONTROL Files]** report, you can include/exclude sub-folders. However, you cannot include asset renditions for this report.

   ![Details page of Files report](assets/files_report.png)

   The **[!UICONTROL Link Share]** report displays URLs to assets that are shared with external users from within [!DNL Assets]. <!-- It includes email ids of the user who shared the assets, emails ids of users with which the assets are shared, share date, and expiration date for the link. --> The columns are not customizable.

   The **[!UICONTROL Link Share]** report, does not include options for sub-folders and renditions because it merely publishes the shared URLs that appear under `/var/dam/share`.

   ![Details page of Link Share report](assets/link_share.png)

1. Click **[!UICONTROL Next]** from the toolbar.

1. In the **[!UICONTROL Configure Columns]** page, some columns are selected to appear in the report by default. You can select more columns. Cancel the selection of a column to exclude it in the report.

   ![Select or cancel selection of report columns](assets/configure_columns.png)

   To display a custom column name or property path, configure the properties for the asset binary under the `jcr:content` node in CRX. Alternatively, add it through property path picker.

   ![Select or cancel selection of report columns](assets/custom_columns.png)

1. Click **[!UICONTROL Create]** from the toolbar. A message notifies that report generation has been initiated.
1. On the [!UICONTROL Asset Reports] page, the report generation status is based on the current state of the report job, for example [!UICONTROL Success], [!UICONTROL Failed], [!UICONTROL Queued], or [!UICONTROL Scheduled]. The same status appears in the notifications inbox.To view the report page, click the report link. Alternatively, select the report, and click **[!UICONTROL View]** from the toolbar.

   ![A generated report](assets/report_page.png)

   Click **[!UICONTROL Download]** from the toolbar to download the report in CSV format.

## Add custom columns to reports {#add-custom-columns}

You can add custom columns to the following reports to display more data for your custom requirements:

<!-- Remove download report.
* Upload
* Download
* Expiration
* Modification
* Publish
* [!DNL Brand Portal] publish
* Files
-->

* Upload
* Expiration
* Modification
* Publish
* [!DNL Brand Portal] publish
* Files

To add custom columns to these reports, follow these steps:

1. In the [!DNL Manager interface], click **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Reports]**.
1. On the [!UICONTROL Asset Reports] page, click **[!UICONTROL Create]** from the toolbar.

1. From the **[!UICONTROL Create Report]** page, choose a report to create. Click **[!UICONTROL Next]**.

1. Configure the report details such as title, description, thumbnail, folder path, and date range as applicable. Click **[!UICONTROL Next]**.

1. Select the applicable information from the list of **[!UICONTROL Default Columns]**. To display a custom column, specify the name of the column under **[!UICONTROL Custom Columns]**.

   ![Specify name for custom column of report](assets/custom_columns-1.png)

1. Add the property path under the `jcr:content` node in CRXDE using the property path picker. Alternatively, type the path in the property path field.

   ![Map the property path from paths in jcr:content](assets/property_picker.png)

   To add more custom columns, click **[!UICONTROL Add]** and repeat the above steps.

1. Click **[!UICONTROL Create]** from the toolbar. A message notifies that the report generation is initiated.

<!-- TBD: How to configure purge now? Is it using OSGi configurations?

## Configure purging service {#configure-purging-service}

To remove reports that you no longer require, configure the DAM Report Purge service from the web console to purge existing reports based on their quantity and age.

1. Access the web console (configuration manager) from `https://[aem_server]:[port]/system/console/configMgr`.
1. Open the **[!UICONTROL DAM Report Purge Service]** configuration.
1. Specify the frequency (time interval) for the purging service in the `scheduler.expression.name` field. You can also configure the age and the quantity threshold for reports.
1. Save the changes.
-->

## Troubleshooting information {#tips-troubleshoot}

* If the [!UICONTROL Disk Usage Report] does not generate and if you are using [!DNL Dynamic Media], ensure that all assets are proceed correctly. To resolve, reprocess the assets and generate the report again.

<!-- These notes were present in generate report section above. Removing commented text from in between the instructions to preserve the numbering of the ordered list.

TBD: How do enable this in CS now? Is it done using some OSGi config now?
   >[!NOTE]
   >
   >Before you can generate an **[!UICONTROL Asset Downloaded]** report, ensure that the Asset Download service is enabled. From the web console (`https://[aem_server]:[port]/system/console/configMgr`), open the **[!UICONTROL Day CQ DAM Event Recorder]** configuration, and select the **[!UICONTROL Asset Downloaded (DOWNLOADED)]** option in Event Types if not already selected.
-->

<!-- Removed download report.
   >[!NOTE]
   >
   >By default, the Content Fragments and link shares are included in the asset [!UICONTROL Download] report. Select the appropriate option to create a report of link shares or to exclude Content Fragments from the download report.

   >[!NOTE]
   >
   >The [!UICONTROL Download] report displays details of only those assets which are downloaded after selecting individually or are downloaded using Quick Action. However, it does not include the details of the assets that are inside a downloaded folder.
-->
