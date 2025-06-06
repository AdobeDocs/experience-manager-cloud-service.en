---
title: Import and export asset metadata in bulk
description: This article describes how to import and export metadata in bulk.
contentOwner: AG
feature: Metadata
role: User, Admin
exl-id: fb70a068-3ba3-4459-952d-79155d286c42
---
# Import and export asset metadata in bulk {#import-and-export-asset-metadata-in-bulk}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

Adobe Experience Manager Assets lets you import asset metadata in bulk using a CSV file. You can do bulk updates for the recently uploaded assets or the existing assets by importing a CSV file. You can also ingest asset metadata in bulk from third-party system in CSV format.

## Import metadata {#import-metadata}

The metadata import is asynchronous and does not impede the system performance. Simultaneous update of the metadata for multiple assets can be resource-intensive because of the metadata writeback activity using asset microservices. Adobe recommends that you plan any bulk operations during lean server usage so that performance for other users is not impacted.

>[!NOTE]
>
>To import metadata on custom namespaces, first register the namespaces.

1. Navigate to [!DNL Assets] user interface, select **[!UICONTROL Create]** from the toolbar, and select **[!UICONTROL Metadata]** from the menu.
1. In the **[!UICONTROL Metadata Import]** page, click **[!UICONTROL Select File]**. Select the CSV file with the metadata.
1. Provide the following parameters:

   |       Parameter        |      Description  |
   | ---------------------- | ------- |
   | Batch Size             | Number of assets in a batch for which metadata is to be imported. The default value is 50. Maximum value is 100. |
   | Field Separator        | Default value is `,` (a comma). You can specify any other character. |
   | Multi value Delimiter  | Separator for metadata values. Default value is `|`. |
   | Launch Workflows       | False by default. When set to `true` and default settings are in effect for the DAM Metadata WriteBack workflow (that writes metadata to the binary XMP data). Enabling the workflows slows the system down. |
   | Asset Path Column Name | Defines the column name for the CSV file with assets.  |

1. Select **[!UICONTROL Import]** from the toolbar. After the metadata is imported, a notification is sent to your Notification inbox. Navigate to asset property page and verify whether the metadata values are correctly imported for assets.

1. To add date and timestamp to import the metadata, use `YYYY-MM-DDThh:mm:ss.fff-00:00` format for date and time. Date and time are separated by `T`, `hh` is hours in 24-hour format, `fff` is nanoseconds, and `-00:00` is time zone offset. For example, `2020-03-26T11:26:00.000-07:00` is March 26, 2020 at 11:26:00.000 AM PST.

   * The date format is dependent on the column heading and the format in it. For example, if the date is complaint with format `yyyy-MM-dd'T'HH:mm:ssXXX` then the respective column header must be `Date: DateFormat: yyyy-MM-dd'T'HH:mm:ssXXX`. 
   * The default date format is `yyyy-MM-dd'T'HH:mm:ss.SSSXXX`.

<!-- Hidden via cqdoc-17869>

>[!CAUTION]
>
>If the date format does not match `YYYY-MM-DDThh:mm:ss.fff-00:00`, the date values are not set. The date formats of exported metadata CSV file is in the format `YYYY-MM-DDThh:mm:ss-00:00`. If you want to import it, convert it to the acceptable format by adding the nanoseconds value denoted by `fff`.
-->

## Export Metadata {#export-metadata}

You can export metadata for multiple assets in a CSV format. The metadata is exported asynchronously and does not impact the performance of the system. To export metadata, Experience Manager traverses through the properties of the asset node `jcr:content/metadata` and its child nodes and exports the metadata properties in a CSV file.

A few use cases for exporting metadata in bulk are:

* Import the metadata in a third-party system when migrating assets.
* Share asset metadata with a wider project team.
* Test or audit the metadata for compliance.
* Externalize the metadata for separate localization.

>[!NOTE]
>
>Metadata Exports are limited at 1,048,575 Assets, corresponding to the maximum worksheet size in Microsoft Excel. If an exported hierarchy contains more than this number of Assets, only the metadata of the first 1,048,575 Assets will be included in the CSV file.

1. Select the asset folder that contains assets for which you want to export metadata. From the toolbar, select **[!UICONTROL Export metadata]**.
1. In the Metadata Export dialog, specify a name for the CSV file. To export metadata for assets in subfolders, select **[!UICONTROL Include assets in subfolders]**.

   ![Interface and options to export metadata of all assets in a folder](assets/export_metadata_page.png "Interface and options to export metadata of all assets in a folder")

1. Select the desired options. Provide a filename and if necessary a date.

1. In the **[!UICONTROL Properties to be exported]** field, specify whether you want to export all or specific properties. If you choose Selective properties to be exported, add the desired properties.  

1. From the toolbar, select **[!UICONTROL Export]**. A message confirms that the metadata is exported. Close the message.
1. Open the inbox notification for the export job. Select the job and click **[!UICONTROL Open]** from the toolbar. To download the CSV file with the metadata, select **[!UICONTROL CSV Download]** from the toolbar. Click **[!UICONTROL Close]**.

   ![Dialog  to download the CSV file containing metadata exported in bulk](assets/csv_download.png)

   *Figure: Dialog  to download the CSV file containing metadata exported in bulk.*

**See also**

* [Translate Assets](translate-assets.md)
* [Assets HTTP API](mac-api-assets.md)
* [Assets supported file formats](file-format-support.md)
* [Search assets](search-assets.md)
* [Connected assets](use-assets-across-connected-assets-instances.md)
* [Asset reports](asset-reports.md)
* [Metadata schemas](metadata-schemas.md)
* [Download assets](download-assets-from-aem.md)
* [Manage metadata](manage-metadata.md)
* [Search facets](search-facets.md)
* [Manage collections](manage-collections.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

>[!MORELIKETHIS]
>
>* [Import metadata when importing assets in bulk](/help/assets/add-assets.md#asset-bulk-ingestor)
