---
title: Manage reports in Assets view
description: Access the data in the reports section of Assets view to assess product and feature usage and derive insights on key success metrics.
exl-id: 26d0289e-445a-4b8e-a5a1-b02beedbc3f1
feature: Asset Insights, Asset Reports
role: User, Admin, Developer
---
# Manage reports {#manage-reports}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

Asset reporting provides administrators with visibility into activity of the Adobe Experience Manager Assets View environment. This data provides useful information about how users interact with content and the product. All users can access the Insights dashboard and the ones who are assigned to the Administrators product profile can create user-defined reports. 

## Access reports {#access-reports}

All users who are assigned to the AEM Administrators product profile can access the Insights dashboard or create user-defined reports in Assets view.

To access reports, navigate to **[!UICONTROL Reports]** under **[!UICONTROL Settings]**.

![Reports](assets/reports.png)

<!--
In the **[!UICONTROL Reports]** screen, various components are shown in the tabular format which includes the following:

* **Title**: Title of the report
* **Type**: Determines whether the report is uploaded or downloaded to the repository
* **Description**: Provide details of the report that was given during uploading/downloading the report
* **Status**: Determines whether the report is completed, under progress, or deleted.
* **Author**: Provides email of the author who has uploaded/downloaded the report.
* **Created**: Gives information of the date when the report was generated.
-->

## Create a Report {#create-report}

The AEM Assets view environment offers comprehensive reporting capabilities through the Reports dashboard. This capability enables users to generate and download CSV reports detailing asset uploads and downloads within specified time frames-ranging from once-off to daily, weekly, monthly, or yearly intervals. 

**To create a report:** 

1. Navigate to **Reports** and click **Create report** (from the top right). The **create report** dialog box displays the below fields: 
![create-report](/help/assets/assets/executed-reports1.svg)

   **In Configuration tab:** 

   1. **Report type:** Select among [!UICONTROL upload], [!UICONTROL download], or [Dynamic Media Delivery Report](#dynamic-media-delivery-reports) type.
   1. **Title:** Add a title to the report.
   1. **Description:** Add an optional description to the report.
   1. **Select folder path:** Select a folder path to generate the report of uploaded and downloaded assets within that specific folder. For example, if you need the report of assets uploaded to a folder then specify the path to that folder.
   1. **Select date interval:** Select the date range to view upload or download activity within the folder.
   <br>

   >[!NOTE]
   >
   > Assets view converts all local time zones to Coordinated Universal Time (UTC).

   **In Columns Tab:** Select the column names to display in the report. The following table explains the use of all columns: 

   <table>
    <tbody>
     <tr>
      <th><strong>Column name</strong></th>
      <th><strong>Description</strong></th>
      <th><strong>Report Type</strong></th>
     </tr>
     <tr>
      <td>Title</td>
      <td>The title of the asset.</td>
      <td>Upload and Download</td>
     </tr>
     <tr>
      <td>Path</td>
      <td>The folder path where the asset is available in Assets view.</td>
      <td>Upload, Download, and Dynamic Media Delivery</td>
     </tr>
     <tr>
      <td>MIME Type</td>
      <td>The MIME type for the asset.</td>
      <td>Upload and Download</td>
     </tr>
     <tr>
      <td>Size</td>
      <td>The size of the asset in bytes.</td>
      <td>Upload and Download</td>
     </tr>
     <tr>
      <td>Downloaded By</td>
      <td>The email ID of the user who downloaded the asset.</td>
      <td>Download</td>
     </tr>
     <tr>
      <td>Download Date</td>
      <td>The date when the asset download action is performed.</td>
      <td>Download</td>
     </tr>
     <tr>
      <td>Author</td>
      <td>The author for the asset.</td>
      <td>Upload and Download</td>
     </tr>
     <tr>
      <td>Creation Date</td>
      <td>The date when the asset is uploaded to Assets view.</td>
      <td>Upload and Download</td>
     </tr>
     <tr>
      <td>Modified Date</td>
      <td>The date when the asset is last modified.</td>
      <td>Upload and Download</td>
     </tr>
     <tr>
      <td>Expired</td>
      <td>The expiration status of the asset.</td>
      <td>Upload and Download</td>
     </tr>
     <tr>
      <td>Downloaded By User Name</td>
      <td>The name of the user who downloaded the asset.</td>
      <td>Download</td>
     </tr> 
     <tr>
      <td>Referrer</td>
      <td>The URL where the asset is delivered or included</td>
      <td>Dynamic Media Delivery</td>
     </tr>  
     <tr>
      <td>Hits</td>
      <td>The number of times the asset is delivered (delivery count)</td>
      <td>Dynamic Media Delivery</td>
     </tr>          
    </tbody>
   </table>

## Dynamic Media Delivery Reports {#dynamic-media-delivery-reports}

Get delivery insights for assets delivered with Dynamic Media, with asset level delivery count, referrer information, asset path in AEM Assets and unique asset ID. Reports can be generated for all assets delivered via the Dynamic Media for AEM Assets repository or for a specific folder hierarchy in AEM Assets. Moreover, Dynamic Media Delivery Reports insights help measure ROI of assets delivered, measure channel performance, and help take informed asset management tasks for assets.

<!--
>[!NOTE]
> 
>To get early access to the Dynamic Media Delivery Report on your Dynamic Media account, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).
-->

### Prerequisites {#prereqs-dynamic-media-delivery-reports}

You should have a Dynamic Media license to create and use this report.

>[!IMPORTANT]
> 
>* Reports are provided for assets delivered via Dynamic Media.
>* Reports are generated for the first 1 million rows. To capture all files within this limit, consider including the referrer column for smaller folders.
>* Reports can be generated for the past 3 months only.

### Create a Dynamic Media Delivery Report{#create-dynamic-media-delivery-report}

1. Create a Dynamic Media Delivery Report, using the steps mentioned in [Create a report](#create-report). 

1. Select **[!UICONTROL Dynamic Media Delivery]** from the **[!UICONTROL Report type]** drop-down list.

   ![Dynamic Media Delivery Report drop-down](assets/dynamic-media-delivery-report-option.png)


1. In the **[!UICONTROL Columns]** tab, you can select the **[!UICONTROL Referrer]** column to include it in your report.

   ![Referrer](assets/referrer.png)

   All the columns of the downloaded report are read-only, except the **Referrer** column, which you can modify to include or exclude from the report. <!--Choosing a referrer displays the number of visitors received from each referred report that directs traffic to the site. It offers insights into the sources of traffic and the origin of the visitors. Such insights help measure ROI of delivered assets, measure channel performance, and help take informed asset management tasks for assets.-->

### Actions performed on Dynamic Media Delivery Report {#actions-performed-dynamic-media-delivery-reports}

After creating the report, you can perform the following actions:

* **[!UICONTROL Delete]**: You can delete the selected report.
* **[!UICONTROL Download CSV]**: You can download the selected report in a CSV format. The downloaded report consists of the Name, Path, DynamicMediaID, Referrer, Hits columns.
    * **Referrer** column lists the URL where the asset is delivered or included.

    * **Hits** column lists the number of times the asset is delivered (delivery count).

To delete or download the Dynamic Media Delivery Report as CSV, see [View and download existing report](#View-and-download-existing-report).

   ![Downloaded CSV on Dynamic Media Delivery Report](assets/csv-dynamic-media-delivery-report.png)


## View and download existing report {#View-and-download-existing-report}

Existing reports display under the **Executed Reports** tab. Click **Reports** and select **Executed Reports** to view all the created reports with the status as **completed**, indicating they are ready to download. To download the report in CSV format or delete the report, select the report row. Then select **Download CSV** or **Delete**.
![view and download existing reports](/help/assets/assets/view-download-existing-report.png)


## Schedule a Report {#schedule-report}

In the AEM Assets view UI, **Schedule Report** sets up an automatic generation of reports at specified future intervals such as daily, weekly, monthly, or yearly. This feature helps streamline recurring reporting needs and ensures timely data updates. While **Create Report** generates reports for past dates. Completed reports are listed under **Executed Reports** and upcoming reports are found under **Scheduled Reports**. 

To schedule a report, follow the steps below: 

1. Click Reports from the left pane and then click Create report (from top right).
1. The report dialog box displays the below information:
   1. **Report type:** Select between the upload and download type. 
   1. **Title:** Add a title to the report. 
   1. **Description**: Add an optional description to the report. 
   1. **Select folder path:** Select a folder path to generate a report for assets that will be uploaded to or downloaded from that specific folder in the future. 
   1. Toggle **Schedule report:** Toggle to schedule the report for a later time or for its repeated occurrence.
   ![schedule report](/help/assets/assets/schedule-reports1.svg) 

   1. **Choose frequency:** Specify the interval for generating the report (for example, daily, weekly, monthly, yearly, or once) and set the date and time to run the report along with the end date for recurrence. For a one-time report, select the date range for the report on the selected activity type in the AEM environment. For example, if you need a report on downloaded assets from the 10th to the 29th (future dates) of a specific month, select these dates in the **Select date interval** field.  

   >[!NOTE]
   >
   > Assets view converts all local time zones to Coordinated Universal Time (UTC).

## View Scheduled Reports {#view-scheduled-reports}

Scheduled reports display under **Scheduled Reports** tab in a systematically organized manner. All the completed reports for each scheduled report are stored within a single report folder. Click![expand collapse](/help/assets/assets/expand-icon1.svg)to view the completed reports. For example, if you have scheduled a daily report, all completed reports are grouped together in one folder. This organization simplifies both the navigation and discoverability of reports. To view scheduled reports, click **Reports** and then click **Scheduled Reports**. All the scheduled reports display, with their status as ongoing or completed. Completed reports are ready to download.  
![scheduled report](/help/assets/assets/scheduled-reports-tab.png) 

## Edit and Cancel Scheduled Reports {#edit-cancel-scheduled-reports} 

1. Navigate to the **Scheduled Reports** tab. 
1. Select the report row. 
1. Click **Edit**. 
1. Click **Cancel Schedule** and then click **Confirm**, to cancel the scheduled report. For canceled reports, the next run time becomes empty and the status shows canceled. 
![edit and cancel scheduled report](/help/assets/assets/cancel-edit-scheduled-reports.png)

### Resume Schedule {#resume-schedule}

To resume the canceled schedule, select the report row and click **Resume Schedule**. When resumed, the next runtime entries display again and the status shows ongoing. 
![resume schedule](/help/assets/assets/resume-schedule.png) 

   >[!NOTE]
   >
   > If you resume a canceled report before the scheduled end date, the reports from the cancellation date to the resumption date automatically generates.

## View Insights {#view-live-statistics}

Assets view enables you to view real-time data for your Assets view environment with the Insights dashboard. You can view real-time event metrics during the last 30 days or for the last 12 months. 

   <!--![Toolbar options when you select an asset](assets/assets-view-live-statistics.png)-->

Click **[!UICONTROL Insights]** available in the left navigation pane to view the following automatically generated charts:

* **Downloads**: The number of assets downloaded from the Assets view environment in the last 30 days or 12 months represented using a line graph.
![insights-downloads](/help/assets/assets/insights-downloads2341.svg)

* **Uploads**: The number of assets uploaded to the Assets view environment in the last 30 days or 12 months represented using a line graph.
![insights-uploads](/help/assets/assets/insights-uplods2.svg)
<!--* **Asset Count by Size**: The division of count of assets based on their range of various sizes from 0 MB to 100 GB.-->

* **Storage usage**: The storage usage, in bytes, for the Assets view environment represented using a bar chart.
![insights-uploads](/help/assets/assets/insights-storage-usage1.svg)
<!--* **Delivery**: The graph depicts the count of assets as the delivery dates.-->

<!--* **Asset Count by Asset Type**: Represents count of various MIME types of the available assets. For example, application/zip, image/png, video/mp4, application/postscripte.-->

* **Top Searches**: View top searched terms along with the number of times those terms are searched within your Assets view environment in the last 30 days or 12 months represented in a tabular format.
![insights-uploads](/help/assets/assets/insights-top-search.svg)
  <!--
   ![Insights](assets/insights1.png)
   ![Insights](assets/insights2.png)
   -->
* **Asset Count by size:** Segments the total asset count in your Assets View environment into different size ranges, highlighting the count and percentage of assets in each size range, represented by a donut chart.
![insights-assets-count-by-size](/help/assets/assets/insights-assets-count-by-size.svg)
* **Asset Count by Asset Type:** Segments the total asset count in your Assets View environment, highlighting the count and percentage of assets based on their file types, represented by a donut chart.
![insights-assets-count-by-size](/help/assets/assets/insights-assest-count-by-asset-type1.svg)