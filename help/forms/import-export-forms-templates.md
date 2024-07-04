---
title: How to import, export, and organize Adaptive Forms or PDF forms on an AEM Forms instance?
description: Learn to migrate Adaptive Forms, PDF forms, themes, and other supporting assets, to and from an AEM instances.
topic-tags: forms-manager
role: Admin, User
feature: Adaptive Forms
exl-id: f5105fb7-b8c0-4656-8095-b21d392746c0
---


| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/forms/manage-administer-aem-forms/import-export-forms-templates)                  |
| AEM as a Cloud Service     | This article   |

# Import or Export Adaptive Forms and AEM Forms assets {#importing-and-exporting-assets-to-aem-forms}

You can move Adaptive Forms and related assets such as Adaptive Form themes, Form Data Model (FDM), Adaptive Form templates, Fragments, and PDF forms between [!DNL AEM Forms] instances.

## Download Adaptive Forms, PDF forms, or related assets {#download-forms-amp-documents-assets}

To download forms or related assets:

1. Log in to your [!DNL Experience Manager Forms] instance.
1. Select **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

   ![Select Forms](/help/forms/assets/select-forms.png)

1. Select the assets, and click the **[!UICONTROL Download]** icon from the upper rail.

   ![Download Forms](/help/forms/assets/download-form.png)

   When you download the form, the **[!UICONTROL Download Asset(s)]** dialog box appears on the screen.

   ![Download forms assets](/help/forms/assets/download-form-assets.png)

1. Click **[!UICONTROL Download]**.

The selected assets are downloaded as an archive (.zip file).

## Upload Adaptive Forms, PDF forms, or related assets {#upload-forms-amp-documents-assets}

You can upload the supported asset types individually or as a ZIP archive. For a ZIP file, the relative paths of all the supported assets are displayed. Unsupported assets inside the ZIP are ignored and not listed. However, if the ZIP archive contains only the unsupported assets, an error message is displayed instead of the pop-up dialog.
To upload a form or a related asset:

1. Log in to your [!DNL Experience Manager Forms] instance.
1. Select **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

   ![Select Forms](/help/forms/assets/select-forms.png)

1. Select **[!UICONTROL Create]** &gt; **[!UICONTROL File Upload]**. A dialog box appears.

   ![Upload Forms](/help/forms/assets/form-upload.png)

1. In the dialog box, browse and select the package or the archive to import. You can also select other supported file types. Select **[!UICONTROL Open]**. The folder or the file name that you select must not include any special characters.

   On the dialog box, verify the details of assets being uploaded, and select **[!UICONTROL Upload]**.

   In case, you upload an existing forms asset, the asset gets updated.

   >[!NOTE]
   >
   > * When a name conflict with different resource types, uploading a package does not replace the existing folder hierarchy. For example, If you have an Adaptive Form named 'Training' at location `/content/dam/formsanddocuments` on one server. You can download the Adaptive Form and upload the form on another server. The second server also has a folder with the name 'Training' at the same location `/content/dam/formsanddocuments`. The upload fails.
   
## Download a theme 

You can export themes in [!DNL AEM Forms] that you can use in other projects or instances. AEM lets you download themes as a zip file, that you can upload on the instance.
To download a theme:

1. Log in to your [!DNL Experience Manager Forms] Author instance.
1. Select **[!UICONTROL Forms]** &gt; **[!UICONTROL Themes]**.

   ![Select Theme](/help/forms/assets/select-theme.png)

1. On the Themes page, select the theme and click the **[!UICONTROL Download]** icon from the upper rail. 

   ![Download Theme](/help/forms/assets/download-theme.png)

   When you download the theme, the **[!UICONTROL Download Asset(s)]** dialog box appears on the screen.

   ![Download theme assets](/help/forms/assets/download-theme-asset.png)

1. Click **[!UICONTROL Download]**.

The selected assets are downloaded as an archive (.zip file).

## Upload a theme {#uploading-a-theme}

You can upload and use themes that others create in your forms. 
To upload a theme:

1. Log in to your [!DNL Experience Manager Forms] instance.
1. In Experience Manager, navigate to **[!UICONTROL Forms]** &gt; **[!UICONTROL Themes]**.

   ![Select Theme](/help/forms/assets/select-theme.png)

1. On the Themes page, click **[!UICONTROL Create]** &gt; **[!UICONTROL File Upload]**.

   ![Upload Theme](/help/forms/assets/theme-upload.png)

1. Browse and select a theme package on your computer and click **[!UICONTROL Upload]**. The uploaded theme becomes available on the Themes page.

## Use folders to organize Adaptive Forms, PDF forms, and related assets  {#folders-and-organizing-assets}

You can uses folders to arrange and organize assets. Organizing documents and assets in a folder allow you to group the files for easy management. You can select a folder and choose to download or delete it. 

### Create a folder {#create-a-folder}

To create a folder:

1. Log in to your [!DNL Experience Manager Forms] instance.
1. Select **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

   ![Select Form](/help/forms/assets/select-forms.png)

1. Select **[!UICONTROL Create]** &gt; **[!UICONTROL Folder]**.

   ![Create Folder](/help/forms/assets/create-folder.png)

   The **[!UICONTROL Add Folder]** dialog box appears.
1. Enter the **[!UICONTROL Title]**. The **[!UICONTROL Name]** automatically populates as you type the **[!UICONTROL Title]**.

   ![Add Folder](/help/forms/assets/add-folder.png)

1. Click **[!UICONTROL Create]**.

   >[!NOTE]
   >
   >By default, the value of the name field is automatically populated from the title. The name can only contain alphanumeric characters, or the hyphen (-) and underscore (_) special characters. Any other special characters entered in the title are automatically replaced with a hyphen and you are prompted to confirm the new name. You can choose to continue with the suggested name or edit it further.

A new folder with the title you defined is displayed at the current location in the asset listing.

If a folder exists with the name specified, the submission fails with an error. You can view the error message by hovering over the error ![aem6forms_error_alert](assets/Smock_Alert_18_N.svg) icon that appears beside the name field.

You can select the created folder to go inside the folder and create assets or folders within the folder. Further, you can select a folder and choose to queue it for download, delete it, or edit its name.

### Create copies of one or more assets {#create-copies-of-one-or-more-assets-or-letters}

You can use an existing assets to quickly create an asset with similar properties, content, and inherited assets.

To create copies of assets:

1. Log in to your [!DNL Experience Manager Forms] instance.
1. On the relevant assets page, select one or more assets. The UI displays the **[!UICONTROL Copy]** icon.
1. Select **[!UICONTROL Copy]**. The UI displays the ![Paste icon](/help/forms/assets/Smock_Paste_18_N.svg) icon. 

   ![Copy asset](/help/forms/assets/copy-asset.png)

   You can also choose to go/navigate inside a folder before you paste. Different folders can contain assets with the same names. For more information on folders, see [Folders and organizing assets](#folders-and-organizing-assets).
1. Select **[!UICONTROL Paste]**. 
   
     ![Paste asset](/help/forms/assets/paste-asset.png)
   
1. The **[!UICONTROL Paste]** dialog appears. The system auto generates names and titles to the new copies of assets, but you can edit the titles and names of the assets.

   If you are copying and pasting the assets at the same place, a suffix "-CopyXX" gets added to the existing name of the `asset`. If no title existed for the copied asset, the auto generated title field remains blank.

      ![Paste asset at new location](/help/forms/assets/paste-click-asset.png)

   If necessary, edit the **[!UICONTROL Title]** with which you want to save the copy of the asset. The **[!UICONTROL Name]** automatically populates as you type the **[!UICONTROL Title]**.
1. Select **[!UICONTROL Paste]**. New copies of the copied assets are created. 

## Search {#search-forms}

When you have a large number of assets, searching for the right asset is time-consuming. You can perform a text-based search for a specific asset on the asset page.

To search the asset:

1. Log in to your [!DNL Experience Manager Forms] instance.
1. Click the ![search icon](assets/folder-search-icon.svg) search icon.

   ![Search Form](/help/forms/assets/search-form.png)

1. Enter the name of the asset you wish to search for in the search bar.

1. A list of related assets appears. Select the desired asset from the displayed asset list.

   ![Search assets](/help/forms/assets/search-bar.png) 

For more information and instructions on using search, see [Search](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/indexing.html). 

## Export or create a package {#export-a-workflow-application}

You can use packages to install new content, install new functionality, transfer content between instances, and back up content.
To export or create a package:

1. Log in to your [!DNL Experience Manager Forms] instance.
1. Navigate to **[!UICONTROL Tools]** ![hammer](assets/hammer.png) &gt; **[!UICONTROL Deployment]** &gt; **[!UICONTROL Packages]**.

   ![Package Manager](/help/forms/assets/package-manager.png)

1. Click **[!UICONTROL Create Package]**.

   ![Create package](/help/forms/assets/create-package.png)   
   
   When **[!UICONTROL Create Package]** is clicked, the **[!UICONTROL New Package]** dialog box appears.
1. Specify the package name, version, and group for the package. 
   
   ![New package](/help/forms/assets/new-package.png)  

   * **Package Name** - Select a descriptive name to help you identify the contents of the package.

   * **Version** - It is a textual field to indicate a version. This is appended to the package name to form the name of the zip file.

   * **Group** - This is the target group (or folder) name. Groups help you organize your packages. A folder is created for the group if it does not already exist. If you leave the group name blank, it creates the package in the main package list.

1. Click **[!UICONTROL OK]**.

   Once the package is created, it appears at the top of the list of packages.

1. Click **[!UICONTROL Edit]**.
   
   ![Edit Package](/help/forms/assets/edit-package.png)
    
1. Open the **[!UICONTROL Filters]** tab.
   
   ![Open filter tab](/help/forms/assets/add-filter-package.png)
   
1.  Click **[!UICONTROL Add Filter]**. 
   
      ![Add filter](/help/forms/assets/add-filter.png)

      You can specify the path of the package. You can also add rules and other validations for the package.

      ![Add path](/help/forms/assets/add-path.png)

1. Click **[!UICONTROL Save]** after you are finished editing the settings.
1. Click **[!UICONTROL Build]** to create the package.
    
     ![Build path](/help/forms/assets/build-package.png)

   After the package is built, you can download the package and import it to the other server. The workflow application appears on the server where the package is uploaded.

   >[!NOTE]
   >
   >For the workflow application to work properly, also export the corresponding Adaptive Form and workflow model with the work application.

   Once a package is uploaded to AEM, you can modify its settings. You can also download or delete the package.

<!-- ## Import and export assets in Correspondence Management {#import-and-export-assets-in-correspondence-management}

To share assets, such as data dictionaries, letters, and document fragments, between two different implementations of Correspondence Management, you can create and share .cmp files. A .cmp file can include one or more data dictionaries, letters, document fragments, and forms.

### Export Document Fragments, Letters, and/or Data Dictionaries {#export-document-fragments-letters-and-or-data-dictionaries}

1. In the letters, document fragments, or data dictionary pages, select and select the assets you want to export to a single package, and then select Queue For Download. The assets are lined-up for export.
1. As required, repeat the above step to add letters, document fragments, and data dictionaries.
1. Select **Download**.
1. Correspondence Management displays Download Asset(s) dialog with a list of assets in the export list.

   ![export](assets/export.png)

1. To view the dependencies that are exported, Select Resolve. Or skip to the next step. Even if you do not select resolve, the dependencies are still exported.
1. To download the .cmp file, select **OK**.
1. Correspondence Management downloads a .cmp file to your computer.

   The .cmp file includes the exported assets. You can share the .cmp file with others. Other users can import the .cmp file in a different server to get all the assets in the new server.

### Export all the Correspondence Management assets as a package {#export-all-the-correspondence-management-assets-as-a-package}

Use this option to download all the Correspondence Management assets and related dependencies as a package from an [!DNL AEM Forms] instance.

For example, if Correspondence Management has a letter that uses an image and text, the downloaded package also contains the image and the text related to the letter. All the metadata properties (including custom properties) associated with the asset are also downloaded. Once you have downloaded the package (.cmp), you can [import the package to a different [!DNL AEM Forms] instance](import-export-forms-templates.md#p-upload-forms-documents-assets-p).

To download all the Correspondence Management assets and related dependencies as a package, complete the following steps:

1. Log in to [!DNL AEM Forms] server as a forms user.
1. Select **Adobe Experience Manager** in the Global Navigation bar.
1. Select tools ( ![tools](assets/tools.png)) and then select **Forms**.
1. Select **Export Correspondence Management Assets**.

   ![publish-cmp-assets-1](assets/publish-cmp-assets-1.png)

   ( ``The Export All Correspondence Management Assets page appears and displays the information about the last time the Export process was attempted and a link to download the last successfully exported package.

   ![export-last-run-details](assets/export-last-run-details.png)

1. Select **Export** and, in the confirm message, select **OK**.

   After a batch process is complete, the last run details and the link to download the package are updated. This includes information such as the Administrator login and if the batch run successfully or failed. The assets are exported to a package and the Download Exported Package link appears.

   >[!NOTE]
   >
   >The Export All Assets process cannot be canceled once initiated. Also, while the export all operation is in process, do not create, delete, modify, or publish any assets or initiate Publish All Assets process.a

1. Select the **Download Exported Package** link to download the package file.

   To add the assets in the package to another instance of Correspondence Management, [import the package to an [!DNL AEM Forms] instance](import-export-forms-templates.md#p-upload-forms-documents-assets-p).

<!-- ### Import Document Fragments, Letters and/or Data Dictionaries into Correspondence Management {#import-document-fragments-letters-and-or-data-dictionaries-into-correspondence-management}

You can import assets that are exported into a .cmp file. A .cmp file can have one or more letters, data dictionaries, document fragments, and dependent assets.

>[!NOTE]
>
>While importing old Correspondence Management assets for migration, log in using an Admin account. For more information on Migrating old Correspondence Management assets, see [Migrate Correspondence Management assets to AEM 6.1 forms](migration-utility.md).

1. On the data dictionary, letters, or document fragments page, select **Create &gt; File Upload** and select the .cmp file.
1. Correspondence Management displays the Import Assets dialog with the list of assets that are imported. Select **Import**.

   After importing the assets, the following properties of the assets are updated while the other properties remain the same:

    * Author: Displays the ID of the user that imported the asset to the server
    * Modified: The time when the asset was imported to the server

   >[!NOTE]
   >
   >For you to be able to upload XDPs (as part of the cmp file or otherwise), you need to be a part of forms-power-users group. For access rights, contact the administrator. --> 

## See Also {#see-also}

{{see-also}}
