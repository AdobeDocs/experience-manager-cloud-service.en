---
title: Manage Licensed Assets on Content Hub
description: Learn about adding a license field to the asset metadata form, applying the License metadata property to asset folders, and approving assets with licenses for use.
exl-id: ac3aad9f-c7b3-47a7-9314-a2f8277f0d3e
---
# Manage Licensed Assets on Content Hub {#manage-licensed-assets-on-content-hub}

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

>[!AVAILABILITY]
>
>Content Hub guide is now available in PDF format. Download the entire guide and use Adobe Acrobat AI Assistant to answer your queries. 
>
>[!BADGE Content Hub Guide PDF]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/content-hub.pdf"}

As an administrator, edit the metadata form to include the asset license field so that it displays in Asset properties in the AEM author environment. You can then approve the asset as well as its license to make the asset licensed and available on Content Hub.

Execute the following steps:

1. Edit the metadata form to include a new text field to include the license details. Map the text field to `dc:license` property. For more information on how to add fields to a metadata form and define properties, see [Setup Metadata Forms](/help/assets/metadata-assets-view.md#metadata-forms).
![zip extraction](/help/assets/assets/metadata-form-edit.png)
1. Apply the metadata form to the asset folder to apply the settings incorporated in step 1. For information on how to assign a metadata form to the asset folder, see [Assign metadata form to a folder](/help/assets/metadata-assets-view.md#metadata-forms).
1. [Approve the licensed PDF](/help/assets/manage-organize-assets-view.md#set-asset-status)
1. Select the asset and click **Details** to view its properties. In the license field added in Step 1, define the absolute path for the asset license that has been approved in Step 3 or already approved earlier. The Content Hub absolute path follows this standard pattern: `/content/dam/(The asset's folder hierarchy within the DAM repository)/(asset_name).(file_extension)`. For example, /content/dam/teamA/projects/documents/file1.pdf
![absolute path](/help/assets/assets/absolute-path.png)
1. Approve the asset to make it available in Content Hub and click **Save**. For information on how to approve an asset, see [Set asset status](/help/assets/manage-organize-assets-view.md#set-asset-status).
