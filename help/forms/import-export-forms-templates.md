---
title: Import, export and organize Adaptive Forms, PDF forms, and other assets
seo-title: Learn to import, export, and organize Adaptive Forms, PDF forms, and other assets on an[!DNL AEM Forms] instance
description: Looking to migrate Adaptive Forms and assets to and from an AEM instances? Learn here how to import and export Adaptive Forms, PDF forms, themes, and other supporting assets from an [!DNL AEM Forms] instance. 
seo-description: Looking to migrate Adaptive Forms and assets to and from an AEM instances? Learn here how to import and export Adaptive Forms, PDF forms, themes, and other supporting assets from an [!DNL AEM Forms] instance. 
topic-tags: forms-manager
exl-id: f5105fb7-b8c0-4656-8095-b21d392746c0
---
# Import, export, and organize Adaptive Forms, PDF forms, and other assets{#importing-and-exporting-assets-to-aem-forms}

You can move Adaptive Forms and related assets such as Adaptive Form themes, Form Data Models, Adaptive Form templates, document fragments, and PDF forms between [!DNL AEM Forms] instances. You can import and export assets in CRX package or binary file formats. 

When you export an Adaptive Form, the content policies, and templates are not exported. Use [Package Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/overview.html?lang=en#how-rolling-deployments-work) to export such assets. 

## Download Adaptive Forms, PDF forms, or  related assets {#download-forms-amp-documents-assets}

To download forms or related assets:

1. Log in to your [!DNL AEM Forms] instance.
1. Tap **[!UICONTROL Adobe Experience Manager]** ![adobeexperiencemanager](assets/adobeexperiencemanager.png) icon &gt; **[!UICONTROL Navigation]** ![compass](assets/Smock_Compass_18_N.svg) icon &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
1. Select the assets and tap the **[!UICONTROL Download]** icon.
1. In the Download Asset(s), choose one of the following options, and tap **[!UICONTROL Download]**.

    * **Download as CRX Package:** Use the option to download and move all selected assets and related dependencies from an [!DNL AEM Forms] instance to another. It downloads all assets and folders as a CRX package including the forms authored in AEM (Adaptive Forms and Adaptive Form Fragments), form sets, form data model, form templates, PDF documents, and referenced resources (XSDs and images). 
      The advantage of downloading assets as a package is that it also downloads referenced by selected assets. For example, If you have an Adaptive Form that uses a form template, XSD, and an image. When you select this Adaptive Form and download it as a package, the downloaded package also contains the form template, XSD, and the image. All the metadata properties (including custom properties) associated with the asset are also downloaded.

    * **Download asset(s) as binary files:** Use the option to download only form templates (XDP), PDF forms (PDF), document (PDF), and resources (images, schemas, stylesheets). You can edit these assets with external applications. It downloads the assets that have binaries, such as images, PDFs, and other supported formats  as a .zip file.
      You cannot download Adaptive Forms, Adaptive Form Fragments, themes, and form sets with **[!UICONTROL Download asset(s) as binary files]** option. To download these assets, you should use **[!UICONTROL Download as CRX Package]** option.

   The selected assets are downloaded as an archive (.zip file).

   >[!NOTE]
   >
   >Both AEM package and binary files are downloaded as an archive (.zip file). The templates for the assets do not get downloaded along with the assets. You need to export the asset templates separately.

## Upload Adaptive Forms, PDF forms, or  related assets {#upload-forms-amp-documents-assets}

You can upload the supported asset types individually or as a ZIP archive. For a ZIP file, the relative paths of all the supported assets are displayed. Unsupported assets inside the ZIP are ignored and not listed. However, if the ZIP archive contains only the unsupported assets, an error message is displayed instead of the pop-up dialog.
To upload a form or a related asset:

1. Log in to your [!DNL AEM Forms] instance.
1. Tap **[!UICONTROL Adobe Experience Manager]** ![adobeexperiencemanager](assets/adobeexperiencemanager.png) icon &gt; **[!UICONTROL Navigation]** ![compass](assets/Smock_Compass_18_N.svg) icon &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
1. Tap **[!UICONTROL Create]** &gt; **[!UICONTROL File Upload]**. A dialog box appears.
1. In the dialog box, browse and select the package or the archive to import. You can also select other supported file types. Tap **[!UICONTROL Open]**. The folder or the file name that you select must not include any special characters.

   On the dialog box, verify the details of assets being uploaded, and tap **[!UICONTROL Upload]**.

   In case, you upload an existing forms asset, the asset gets updated.

   >[!NOTE]
   >
   > * When a name conflict with different resource types, uploading a package does not replace the existing folder hierarchy. For example, If you have an Adaptive Form named 'Training' at location /content/dam/formsanddocuments on one server. You download the Adaptive Form and upload the form on another server. The second server also has a folder with the name 'Training' at the same location /content/dam/formsanddocuments. The upload fails.
   > * Only a member of the `form-power-user` group can upload XDP files.


## Download a theme {#downloading-a-theme}

You can export themes in [!DNL AEM Forms] that you can use in other projects or instances. AEM lets you download themes as a zip file, that you can upload on the instance.

To download a theme:

1. Log in to your [!DNL AEM Forms] instance.
1. Tap **[!UICONTROL Adobe Experience Manager]** ![adobeexperiencemanager](assets/adobeexperiencemanager.png) icon &gt; **[!UICONTROL Navigation]** ![compass](assets/Smock_Compass_18_N.svg) icon &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Themes]**.
1. Select the theme and tap **[!UICONTROL Download]**. The theme is downloaded as an archive (.zip file).

## Upload a theme {#uploading-a-theme}

You can upload and use themes that others create in your forms. To upload a theme:

1. In Experience Manager, navigate to **[!UICONTROL Forms]** &gt; **[!UICONTROL Themes]**.
1. On the Themes page, click **[!UICONTROL Create]** &gt; **[!UICONTROL File Upload]**.
1. In the File Upload prompt, browse and select a theme package on your computer and click **[!UICONTROL Upload]**. The uploaded theme is available on the themes page.

<!-- ## Import and export assets in Correspondence Management {#import-and-export-assets-in-correspondence-management}

To share assets, such as data dictionaries, letters, and document fragments, between two different implementations of Correspondence Management, you can create and share .cmp files. A .cmp file can include one or more data dictionaries, letters, document fragments, and forms.

### Export Document Fragments, Letters, and/or Data Dictionaries {#export-document-fragments-letters-and-or-data-dictionaries}

1. In the letters, document fragments, or data dictionary pages, tap and select the assets you want to export to a single package, and then tap Queue For Download. The assets are lined-up for export.
1. As required, repeat the above step to add letters, document fragments, and data dictionaries.
1. Tap **Download**.
1. Correspondence Management displays Download Asset(s) dialog with a list of assets in the export list.

   ![export](assets/export.png)

1. To view the dependencies that are exported, Tap Resolve. Or skip to the next step. Even if you do not tap resolve, the dependencies are still exported.
1. To download the .cmp file, tap **OK**.
1. Correspondence Management downloads a .cmp file to your computer.

   The .cmp file includes the exported assets. You can share the .cmp file with others. Other users can import the .cmp file in a different server to get all the assets in the new server.

### Export all the Correspondence Management assets as a package {#export-all-the-correspondence-management-assets-as-a-package}

Use this option to download all the Correspondence Management assets and related dependencies as a package from an [!DNL AEM Forms] instance.

For example, if Correspondence Management has a letter that uses an image and text, the downloaded package also contains the image and the text related to the letter. All the metadata properties (including custom properties) associated with the asset are also downloaded. Once you have downloaded the package (.cmp), you can [import the package to a different [!DNL AEM Forms] instance](import-export-forms-templates.md#p-upload-forms-documents-assets-p).

To download all the Correspondence Management assets and related dependencies as a package, complete the following steps:

1. Log in to [!DNL AEM Forms] server as a forms user.
1. Tap **Adobe Experience Manager** in the Global Navigation bar.
1. Tap tools ( ![tools](assets/tools.png)) and then tap **Forms**.
1. Tap **Export Correspondence Management Assets**.

   ![publish-cmp-assets-1](assets/publish-cmp-assets-1.png)

   ( ``The Export All Correspondence Management Assets page appears and displays the information about the last time the Export process was attempted and a link to download the last successfully exported package.

   ![export-last-run-details](assets/export-last-run-details.png)

1. Tap **Export** and, in the confirm message, tap **OK**.

   After a batch process is complete, the last run details and the link to download the package are updated. This includes information such as the Administrator login and if the batch run successfully or failed. The assets are exported to a package and the Download Exported Package link appears.

   >[!NOTE]
   >
   >The Export All Assets process cannot be canceled once initiated. Also, while the export all operation is in process, do not create, delete, modify, or publish any assets or initiate Publish All Assets process.a

1. Tap the **Download Exported Package** link to download the package file.

   To add the assets in the package to another instance of Correspondence Management, [import the package to an [!DNL AEM Forms] instance](import-export-forms-templates.md#p-upload-forms-documents-assets-p).

<!-- ### Import Document Fragments, Letters and/or Data Dictionaries into Correspondence Management {#import-document-fragments-letters-and-or-data-dictionaries-into-correspondence-management}

You can import assets that are exported into a .cmp file. A .cmp file can have one or more letters, data dictionaries, document fragments, and dependent assets.

>[!NOTE]
>
>While importing old Correspondence Management assets for migration, log in using an Admin account. For more information on Migrating old Correspondence Management assets, see [Migrate Correspondence Management assets to AEM 6.1 forms](migration-utility.md).

1. On the data dictionary, letters, or document fragments page, tap **Create &gt; File Upload** and select the .cmp file.
1. Correspondence Management displays the Import Assets dialog with the list of assets that are imported. Tap **Import**.

   After importing the assets, the following properties of the assets are updated while the other properties remain the same:

    * Author: Displays the ID of the user that imported the asset to the server
    * Modified: The time when the asset was imported to the server

   >[!NOTE]
   >
   >For you to be able to upload XDPs (as part of the cmp file or otherwise), you need to be a part of forms-power-users group. For access rights, contact the administrator. --> 

## Export a workflow application {#export-a-workflow-application}

You can use the package manager to export workflow applications. The procedure is as listed below:

1. Open [!DNL AEM Forms] package manager. URL of package manager is `https://[server]:[port]/crx/packmgr`.
1. Click **[!UICONTROL Create Package]**. The **[!UICONTROL New Package]** dialog box appears.
1. Specify the name, version, and group for the package. Click **[!UICONTROL OK]**.
1. Click **[!UICONTROL Edit]** and open the **[!UICONTROL Filters]** tab. Click **[!UICONTROL Add Filter]**. Specify the path of the workflow application. For example, /etc/fd/dashboard/startpoints/homemortgage. Click **[!UICONTROL Add rule]**.

1. Open the **[!UICONTROL Advanced]** tab. Select **[!UICONTROL Merge]** or **[!UICONTROL Overwrite]** in ACL Handling field. Click **[!UICONTROL Save]**.
1. Click **[!UICONTROL Build]** to create the package.

   After the package is built, you can download the package and import it to the other server. The workflow application appears on the server where the package is uploaded.

   >[!NOTE]
   >
   >For the workflow application to work properly, also export the corresponding Adaptive Form and workflow model with the work application.

## Use folders to organize Adaptive Forms, PDF forms, and related assets  {#folders-and-organizing-assets}

You can uses folders to arrange and organize assets. Organizing documents and assets in a folder allow you to group the files for easy management. You can select a folder and choose to download or delete it. To create a folder, complete the following steps:

### Create a folder {#create-a-folder}

1. Log in to your [!DNL AEM Forms] instance.
1. Tap Experience Manager ![adobeexperiencemanager](assets/adobeexperiencemanager.png) icon &gt; navigation ![compass](assets/Smock_Compass_18_N.svg) icon&gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
1. Tap **[!UICONTROL Create]** &gt; **[!UICONTROL Folder]**.
1. Enter the following details:

    * **[!UICONTROL Title]**: Display name for the folder
    * **[!UICONTROL Name]**: *(Mandatory)* The node name under which you want to store the folder in the repository

   >[!NOTE]
   >
   >By default, the value of the name field is automatically populated from the title. The name can only contain alphanumeric characters, or the hyphen (-) and underscore (_) special characters. Any other special characters entered in the title are automatically replaced with a hyphen and you are prompted to confirm the new name. You can choose to continue with the suggested name or edit it further.

1. A new folder with the title you defined is displayed at the current location in the asset listing.

   If a folder exists with the name specified, the submission fails with an error. You can view the error message by hovering over the error ![aem6forms_error_alert](assets/Smock_Alert_18_N.svg) icon that appears beside the name field.

   You can tap the newly created folder to go inside the folder and create assets or folders within the folder. Further, you can select a folder and choose to queue it for download, delete it, or edit its name.


<!-- ### Create copies of one or more assets or letters {#create-copies-of-one-or-more-assets-or-letters}

You can use an existing assets to quickly create an asset with similar properties, content, and inherited assets.

Complete the following steps to create copies of assets and letters:

1. On the relevant assets page, select one or more assets. The UI displays the Copy icon.
1. Tap **[!UICONTROL Copy]**. The UI displays the **[!UICONTROL Paste]** icon. You can also choose to go/navigate inside a folder before you paste. Different folders can contain assets with same names. For more information on folders, see [Folders and organizing assets](#folders-and-organizing-assets).
1. Tap **[!UICONTROL Paste]**. The **[!UICONTROL Paste]** dialog appears. The system auto generates names and titles to the new copies of assets/letters, but you can edit the titles and names of the assets/letters.

   If you are copying and pasting the assets/letters at the same place, a suffix "-CopyXX" gets added to the existing name of the asset/letter. If no title existed for the copied asset/letter, the auto generated title field remains blank.

1. If required, edit the Title and Name with which you want to save the copy of the asset/letter.
1. Tap **[!UICONTROL Paste]**. New copies of the copied assets are created.

## Search {#search-forms}

You ca use the top bar **[A]** to search your content. When you search for assets, a side panel is displayed. You can also tap ![assets-browser-content-only](assets/assets-browser-content-only.png) &gt; Filter **[B]** to invoke the side panel. Using the various filters in the side panel, you can narrow down your search. The side panel also allows you to save your searches.

![search_topbar](assets/search_topbar.png)

**A.** Search **B.** Filter

![Side panel - Filters](assets/search_sidepanel.png)

Side panel - Filters

On the side panel, you can use the following to narrow down your search results:

* Search Directory
* Tags
* Search Criteria; for example, Modified Dates, Publish Status, LiveCopy Status.

The side panel also allows you to save your search settings with names of your choice.

For more information and instructions on using search, filters, saved search, and side panel, see [Search](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/indexing.html). -->
