---
title: How to configure Unified Storage Connector for AEM Forms?
description: Learn how to manage Unified Storage Connector for AEM Forms. Use the Unified Storage Connector to connect AEM Forms to external data storages.
---

# Manage Unified Storage Connector for AEM Forms {#manage-unified-storage-connector}

You can use Unified Storage Connector to connect AEM Forms to external data storages. 

For example, you can fill values for fields in an adaptive form and submit it to an AEM Workflow. You can further configure AEM Workflows to store data in an external storage, such as the Microsoft Azure storage server. Use the Unified Storage Connector to create a connection between AEM Workflows and the external storage.

## Connect AEM Workflows with a Microsoft Azure storage server {#connect-workflows-with-azure}

Create an Azure storage configuration and refer to that configuration using the Unified Storage Connector. You can then configure AEM Workflow models to externalize the data storage to connect them to an Azure storage server. 

### Create [!DNL Azure] storage configuration {#create-azure-storage-configuration}

Before executing these steps, ensure that you have an [!DNL Azure] storage account and an access key to authorize the access to the [!DNL Azure] storage account.

Perform the following steps to create an [!DNL Azure] storage configuration: 

1. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Cloud Services]** &gt; **[!UICONTROL Azure Storage]**.
1. Select a folder to create the configuration and tap **[!UICONTROL Create]**.
1. Specify a title for the configuration in the **[!UICONTROL Title]** field.
1. Specify the name of the [!DNL Azure] storage account in the **[!UICONTROL Azure Storage Account]** field.
1. Specify the key to access Azure storage account in the **[!UICONTROL Azure Access Key]** field and tap **[!UICONTROL Save]**.

### Configure Unified Storage Connector for AEM Workflows {#configure-unified-storage-connector-workflows}

Perform the following steps to configure Unified Storage Connector for AEM Workflows:

1. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Unified Storage Connector]**.

1. In the **[!UICONTROL Workflow]** section, Select **[!UICONTROL Azure]** from the Storage drop-down list.
1.  Specify the [configuration path for the Azure storage configuration](#create-azure-storage-configuration) in the **[!UICONTROL Storage Configuration Path]** field.
1. Tap **[!UICONTROL Publish]** and then tap **[!UICONTROL Save]** to save the configuration.

### Configure an AEM Workflow model for external data storage {#configure-workflow-external-data-storage}

Perform the following steps to configure an AEM Workflow model for an external data storage:

1. Navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Workflow]** &gt; **[!UICONTROL Models]**.
1. Select a model name and tap **[!UICONTROL Edit]**.
1. Tap the Page Information icon and tap **[!UICONTROL Open Properties]**.
1. Select **[!UICONTROL Externalize workflow data storage]**.
1. Tap **[!UICONTROL Save & Close]** to save the properties.

>[!NOTE]
>
>The options to save the Assign Task step as draft and to retrieve the history of the Assign Task step are not available when you configure an AEM workflow model for external data storage.

### Guidelines for AEM Workflows for external data storage {#guidelines-workflows-external-data-storage}

The following are the guidelines when you are using AEM Workflows and storing data to external data storages, such as Microsoft Azure storage server:

* Use variables to store data while defining input and output data files and attachments in workflow model steps. Do not select **[!UICONTROL Relative to Payload]** and **[!UICONTROL Available at an absolute path]** options. The **[!UICONTROL Relative to Payload]** and **Available at an absolute path** options do not display automatically once you [configure an AEM Workflow model for external data storage](#configure-workflow-external-data-storage).

* Use variables to store data file and attachments while submitting an adaptive form to an AEM Workflow. Do not select **[!UICONTROL Relative to Payload]** option while submitting an adaptive form to an AEM Workflow. The **[!UICONTROL Relative to Payload]** option do not display automatically once you [configure an AEM Workflow model for external data storage](#configure-workflow-external-data-storage).

* Do not use a custom AEM Workflow step in a workflow model to store data in the CRX DE repository.

* When you [configure an AEM Workflow model for external data storage](#configure-workflow-external-data-storage), do not create custom columns for AEM Inbox based on the data of a workflow.
