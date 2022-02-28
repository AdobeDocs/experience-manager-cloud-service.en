---
title: How to configure Azure storage?
description: Learn how to integrate forms with Azure storage server.
exl-id: 606383b3-293c-43d2-9ba0-5843c4e0caa8
---
# Configure [!DNL Azure] storage {#configure-azure-storage}

[[!DNL Experience Manager Forms] Data Integration](data-integration.md) provides an [!DNL Azure] storage configuration to integrate forms with [!DNL Azure] storage services. The Form Data Model can be used to create Adaptive Forms that interact with [!DNL Azure] server to enable business workflows. For example:

* Write data into [!DNL Azure] on Adaptive Form submission.
* Write data in [!DNL Azure] through custom entities defined in Form Data Model and vice versa.
* Query [!DNL Azure] server for data and prepopulate Adaptive Forms.
* Read data from [!DNL Azure] server.

## Create [!DNL Azure] storage configuration {#create-azure-storage-configuration}

Before executing these steps, ensure that you have an [!DNL Azure] storage account and an access key to authorize the access to the [!DNL Azure] storage account.

1. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Cloud Services]** &gt; **[!UICONTROL Azure Storage]**.
1. Select a folder to create the configuration and tap **[!UICONTROL Create]**.
1. Specify a title for the configuration in the **[!UICONTROL Title]** field.
1. Specify the name of the [!DNL Azure] storage account in the **[!UICONTROL Azure Storage Account]** field.
1. Specify the key to access Azure storage account in the **[!UICONTROL Azure Access Key]** field and tap **[!UICONTROL Save]**.

## Create Form Data Model {#create-azure-form-data-model}

After creating the [!DNL Azure] storage configuration, you can [create the Form Data Model](create-form-data-models.md). Specify the folder that contains the [!DNL Azure] configuration in the **[!UICONTROL Data Source Configuration]** field while creating the Form Data Model. You can then select the configuration from the list of configurations that exist in the specified folder name.

### Add [!DNL Azure] services to the Form Data Model {#add-azure-services}

After creating the Form Data Model and data model objects, you can add [!DNL Azure] services to the Form Data Model.

To add [!DNL Azure] services:

1. In the Edit mode, select the services from the **[!UICONTROL Services]** section in the left pane and tap **[!UICONTROL Add Selected]**. The selected services display in the **[!UICONTROL Services]** tab of the Form Data Model.

   ![Add Selected Services](assets/select-services.png)

1. In the **[!UICONTROL Services]** tab, select the service and **[!UICONTROL Edit Properties]**. Based on the service, define the input or output model objects for the service.

1. Tap **[!UICONTROL Save]** to save the form data model.

   The following table describes the available [!DNL Azure] services:

    <table>
    <tbody>
     <tr>
      <th><strong>Service Name</strong></th>
      <th><strong>Description</strong></th>
     </tr>
     <tr>
      <td>Get Blob from Azure</td>
      <td>Retrieve data stored as a Blob in Azure storage using an ID or a name</td>
     </tr>
     <tr>
      <td>Get Blob with binaries URL from Azure</td>
      <td>Retrieve data stored as a Blob with URL for binaries in Azure storage using an ID or a name</td>
     </tr>
     <tr>
      <td>Save Blob in Azure</td>
      <td>Use a Blob ID to save data in Azure storage</td>
     </tr>
     <tr>
      <td>Update Blob in Azure</td>
      <td>Use a Blob ID to update data in Azure storage</td>
     </tr>
     <tr>
      <td>Retrieve list of Blob IDs from Azure</td>
      <td>Retrieve a list of Blob IDs from Azure based on the number defined in the input request.</td>
     </tr>
     <tr>
      <td>Retrieve SAS URLs for Blobs from Azure</td>
      <td>Retrieve SAS URLs for Blobs from Azure based on Blob IDs in the input request.</td>
     </tr>
     <tr>
      <td>Delete Blob from Azure</td>
      <td>Use a Blob ID to delete data from Azure storage</td>
     </tr>
    </tbody>
   </table>

### Define a data model object property as a search key {#define-data-model-object-as-metadata}

To define a data model object property as a search key:

1. In the **[!UICONTROL Model]** tab, select the data model object property and tap **[!UICONTROL Edit Properties]**.
1. Switch the **[!UICONTROL Search Key]** toggle option to the ON state. This option is available only for primary data types.
1. Tap **[!UICONTROL Done]** and then tap **[!UICONTROL Save]** to save the Form Data Model.

After defining data model object properties as search keys, the hash values are stored in Azure index tags and Base64 encoded values are stored in the Azure metadata.

>[!NOTE]
>
>Only 10 search keys are allowed per Azure entity since Azure only allows 10 tags per Blob and properties value marked as search keys are stored in Azure index tags after hashing. 
