---
Title: How to connect AEM Adaptive Forms with Azure Blob Storage?
Description: Learn how to create an Azure Blob Storage Configuration in AEM Forms and use it within your Adaptive Forms for efficient data storage.
keywords: Azure Blob Storage integration with AEM Forms, Submitting data to Azure Storage, Creating Azure Storage Configuration in AEM Forms, Using Azure Blob Storage in Adaptive Forms Submit Action
feature: Adaptive Forms, Core Components
exl-id: 0c9f8f85-c4e9-4c79-bd0b-abdcac99a2d4
title: "How to configure a Submit Action for an Adaptive Form?"
role: User, Developer
---
# Submit an Adaptive Form to Azure Blob Storage 

The **[!UICONTROL Submit to Azure Blob Storage]**  Submit Action connects an Adaptive Form with a Microsoft&reg; Azure portal. You can submit the form data, files, attachments, or Document of Record to the connected Azure Storage containers. 

AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md) article.

## Advantages

Some of the advantages of Azure Blob Storage integration with AEM Forms are:

* It helps in streamlining the process of submitting Adaptive Form data, files, attachments, and Document of Record to Azure Storage containers.
* It uses Azure Blob Storage for centralized and organized storage of Adaptive Form submissions.

## Connect AEM Forms with Microsoft® Azure Blob Storage

To use Azure Blob Storage in Adaptive Forms Submit Action: 

1. [Create an Azure Blob Storage Container](#create-a-azure-blob-storage-container-create-azure-configuration): It connects AEM Forms to Azure Storage containers.
2. [Use Azure Storage Configuration in an Adaptive Form ](#use-azure-storage-configuration-in-an-adaptive-form-use-azure-storage-configuartion-in-af): It connects your Adaptive Form to configured Azure Storage containers.

### Create an Azure Blob Storage Container {#create-azure-configuration}

To connect AEM Forms to your Azure Storage containers:
1. Go to your **AEM Forms Author** instance > **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Azure Storage]**.   
1. Once you select the **[!UICONTROL Azure Storage]**, you are redirected to **[!UICONTROL Azure Storage Browser]**.
1. Select a **Configuration Container**. The configuration is stored in the selected Configuration Container. 
1. Click **[!UICONTROL Create]**. The Create Azure Storage Configuration wizard appears. 

    ![Azure Storage Configuration](/help/forms/assets/azure-storage-configuration.png)

1. Specify the **[!UICONTROL Title]**, **[!UICONTROL Azure Storage Account]** and **[!UICONTROL Azure Access key]**. 
    
    * You can retrieve `Azure Storage Account` name and `Azure Access key` from the Storage Accounts in the Microsoft&reg; Azure portal.
<!--

    >[!NOTE]
    >
    > The URL for **[!UICONTROL Azure Blob Endpoint]** is automatically appended to the textbox when a value is entered for **[!UICONTROL Azure Storage Account]**. You can update the Azure Blob End Point URL with your custom domain. Steps to update URL for **[!UICONTROL Azure Blob End Point]**:
    > 1. [Enable the AEM Advance Networking VPN support](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/networking/advanced-networking.html)
    > 1. [Enable dedicated egress IP link](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/networking/advanced-networking.html)
    > 1. [Map custom domain to azure blob storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-custom-domain-name?tabs=azure-portal)
-->

1. Click **[!UICONTROL Save]**.

Now, you can use this Azure Storage container configuration for the submit action in an Adaptive Form.

### Use Azure Storage Configuration in an Adaptive Form {#use-azure-storage-configuartion-in-af}

You can use the created Azure Storage container configuration in an Adaptive Form, to save data or generated Document of Record in Azure Storage container. Perform the following steps to use Azure Storage container configuration in an Adaptive Form as:
1. Create an [Adaptive Form](/help/forms/creating-adaptive-form-core-components.md).

    >[!NOTE]
    >
    > * Select the same [!UICONTROL Configuration Container] for an Adaptive Form, where you have created your OneDrive storage. 
    > * If no [!UICONTROL Configuration Container] is selected, then the global [!UICONTROL Storage Configuration] folders appear in the Submit Action properties window.

1. Select **Submit Action** as **[!UICONTROL Submit to Azure Blob Storage]**.
    ![Azure Blob Storage GIF](/help/forms/assets/azure-submit-video.gif)
    
1. Select the **[!UICONTROL Storage Configuration]**, where you want to save your data.
1. Click **[!UICONTROL Save]** to save the Submit settings.

When you submit the form, the data is saved in the specified Azure Storage container configuration. 
Folder structure to save data is `/configuration_container/form_name/year/month/date/submission_id/data`. 

## Related Articles

{{af-submit-action}}
