---
title: Manage reports in Assets view
description: Access the data in the reports section of Assets view to assess product and feature usage and derive insights on key success metrics.
exl-id: c7155459-05d9-4a95-a91f-a1fa6ae9d9a4
---
# Manage reports {#manage-reports}

>[!CONTEXTUALHELP]
>id="assets_reports"
>title="Reports"
>abstract="Asset reporting provides administrators with visibility into activity of the Adobe Experience Manager Assets view environment. This data provides useful information about how users interact with content and the product. All users who are assigned to the Administrators product profile can access the Insights dashboard or create user-defined reports."

Asset reporting provides administrators with visibility into activity of the Adobe Experience Manager Assets view environment. This data provides useful information about how users interact with content and the product. 

## Access reports {#access-reports}

All users who are assigned to the Assets view Administrators product profile can access the Insights dashboard or create user-defined reports in Assets view.

## View Insights {#view-live-statistics}

Assets view enables you to view real-time data for your Assets view environment with the Insights dashboard. You can view real-time event metrics during the last 30 days or for the last 12 months. 

![Toolbar options when you select an asset](assets/assets-essentials-live-statistics.png)

Click **[!UICONTROL Insights]** available in the left navigation pane to view the following automatically generated charts:

* **Downloads**: The number of assets downloaded from the Assets view environment in the last 30 days or 12 months represented using a line chart.

* **Uploads**: The number of assets uploaded to the Assets view environment in the last 30 days or 12 months represented using a line chart.

* **Top Searches**: View top searched terms along with the number of times those terms are searched within your Assets view environment in the last 30 days or 12 months represented in a tabular format.

<!--

* **Storage usage**: The storage usage, in gigabytes (GB), for the Assets view environment, for the last 30 days or 12 months represented using a bar chart.

-->

## Create a Download report {#create-download-report}

To create a Download report:

1. Navigate to **[!UICONTROL Settings]** > **[!UICONTROL Reports]** and click **[!UICONTROL Create Report]**.

1. In the [!UICONTROL Configuration] tab, specify the report type as **[!UICONTROL Download]**.

1. Specify a title and an optional description for the report.

1. Select the folder path, which comprises the assets to execute the report on, using the **[!UICONTROL Select Folder Path]** field.

1. Select the date interval for the report.

   >[!NOTE]
   >
   > Assets view converts all local time zones to Coordinated Universal Time (UTC).

1. In the [!UICONTROL Columns] tab, select the column names that you need to display in the report.

1. Click **[!UICONTROL Create]**.

   ![Download Report](assets/download-reports-config.png)

The following table explains the use of all columns that you can add to the report:

<table>
    <tbody>
     <tr>
      <th><strong>Column name</strong></th>
      <th><strong>Description</strong></th>
     </tr>
     <tr>
      <td>Title</td>
      <td>The title of the asset.</td>
     </tr>
     <tr>
      <td>Path</td>
      <td>The folder path where the asset is available in Assets view.</td>
     </tr>
     <tr>
      <td>MIME Type</td>
      <td>The MIME type for the asset.</td>
     </tr>
     <tr>
      <td>Size</td>
      <td>The size of the asset in bytes.</td>
     </tr>
     <tr>
      <td>Downloaded By</td>
      <td>The email ID of the user who downloaded the asset.</td>
     </tr>
     <tr>
      <td>Download Date</td>
      <td>The date when the asset download action is performed.</td>
     </tr>
     <tr>
      <td>Author</td>
      <td>The author for the asset.</td>
     </tr>
     <tr>
      <td>Creation Date</td>
      <td>The date when the asset is uploaded to Assets view.</td>
     </tr>
     <tr>
      <td>Modified Date</td>
      <td>The date when the asset is last modified.</td>
     </tr>
     <tr>
      <td>Expired</td>
      <td>The expiration status of the asset.</td>
     </tr>
     <tr>
      <td>Downloaded By User Name</td>
      <td>The name of the user who downloaded the asset.</td>
     </tr>           
    </tbody>
   </table>

## Create an Upload report {#create-upload-report}

To create an Upload report:

1. Navigate to **[!UICONTROL Settings]** > **[!UICONTROL Reports]** and click **[!UICONTROL Create Report]**.

1. In the [!UICONTROL Configuration] tab, specify the report type as **[!UICONTROL Upload]**.

1. Specify a title and an optional description for the report.

1. Select the folder path, which comprises the assets to execute the report on, using the **[!UICONTROL Select Folder Path]** field.

1. Select the date interval for the report.

1. In the [!UICONTROL Columns] tab, select the column names that you need to display in the report.

1. Click **[!UICONTROL Create]**.

   ![Upload Report](assets/upload-reports-config.png)

The following table explains the use of all columns that you can add to the report:

<table>
    <tbody>
     <tr>
      <th><strong>Column name</strong></th>
      <th><strong>Description</strong></th>
     </tr>
     <tr>
      <td>Title</td>
      <td>The title of the asset.</td>
     </tr>
     <tr>
      <td>Path</td>
      <td>The folder path where the asset is available in Assets view.</td>
     </tr>
     <tr>
      <td>MIME Type</td>
      <td>The MIME type for the asset.</td>
     </tr>
     <tr>
      <td>Size</td>
      <td>The size of the asset.</td>
     </tr>
     <tr>
      <td>Author</td>
      <td>The author for the asset.</td>
     </tr>
     <tr>
      <td>Creation Date</td>
      <td>The date when the asset is uploaded to Assets view.</td>
     </tr>
     <tr>
      <td>Modified Date</td>
      <td>The date when the asset is last modified.</td>
     </tr>
     <tr>
      <td>Expired</td>
      <td>The expiration status of the asset.</td>
     </tr>              
    </tbody>
   </table>

## View existing reports {#view-report-list}

After [creating the report](#create-download-report), you can view the list of existing reports and select to download them in a CSV format or delete them.

To view the list of reports, navigate to **[!UICONTROL Settings]** > **[!UICONTROL Reports]**.

For each report, you can view report title, the type of the report, description specified while creating the report, status of the report, email ID of the author who created the report, and report creation date.

`Completed ` status of the report represents that the report is ready for download.

![List of reports](assets/list-of-reports.png)


## Download a CSV report {#download-csv-report}

To download a report in CSV format:

1. Navigate to **[!UICONTROL Settings]** > **[!UICONTROL Reports]**.

1. Select a report and click **[!UICONTROL Download CSV]**.

The selected report downloads in CSV format. The columns that display in the CSV report depends on the columns that you select while [creating the report](#create-download-report).

## Delete a report {#delete-report}

To delete a report:

1. Navigate to **[!UICONTROL Settings]** > **[!UICONTROL Reports]**.

1. Select a report and click **[!UICONTROL Delete]**.

1. Click **[!UICONTROL Delete]** again to confirm.
