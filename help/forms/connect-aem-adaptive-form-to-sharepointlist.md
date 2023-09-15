---
title: How to connect AEM Adaptive Form to Microsoft® SharePoint List?
description: This article helps you to configure to Microsoft® SharePoint List and connect it to an Adaptive Form. Learn how to configure and use it to create form data models.
role: User, Developer
seo-description: Connect an Adaptive Form to Microsoft SharePoint List. Learn how to configure the Microsoft SharePoint list and create a Form Data Model using the configuration. Further, you will learn how to integrate the FDM with your Adaptive Form.
keywords: connect AEM Adaptive Form to Microsoft SharePoint List, connect Adaptive Form to Microsoft SharePoint List, integrate AEM Adaptive Form to Microsoft SharePoint List, integrate Adaptive Form to Microsoft SharePoint List, submit data from an Adaptive Form to SharePoint List, submit AEM workflow to SharePoint List.
---

# Connect an Adaptive Form to Microsoft® SharePoint Lists 

Microsoft® SharePoint List is a collection of information in a tabular format. The data is stored in rows and columns. Items are referred to as metadata, fields, or properties, while the rows are called the list itself. SharePoint List maintains the list of items with permissions. It is similar to an Excel spreadsheet.

The two main components of Microsoft® SharePoint are:

* **Microsoft® SharePoint Document Libraries**: **: Microsoft® SharePoint Document Libraries are designed for the management of documents such as Word documents, Excel, spreadsheets, images, and more. The Document Libraries allow to attach additional information (metadata) to the documents; hence making categorization and searching easy. For instructions on how to integrate a Microsoft® SharePoint Document Library to an Adaptive Form, see the [Adaptive Form Submit Action](/help/forms/configuring-submit-actions.md#submit-to-sharepoint) article.

* **Microsoft® SharePoint Lists**: Microsoft® SharePoint Lists store structured data in a tabular format. Lists are used to organize and manage various types of data, such as task lists, contact information, inventory records, and more. Lists are customizable, allowing users to define the types of data they want to capture. The choice between them depends on the specific needs and use cases within an organization. 

## Prerequisites to connect an Adaptive Form to Microsoft® SharePoint Lists {#prerequisites}

Before connecting an Adaptive Form to Microsoft® SharePoint Lists, perform the following steps:

1. [Configure Microsoft® SharePoint List](/help/forms/configure-data-sources.md#configure-microsoft-sharepoint-list)
1. [Create a Form Data Model using created Microsoft® SharePoint List configuration](/help/forms/create-form-data-models.md)
1. [Configure services to read and write data from/to a Form Data Model](/help/forms/work-with-form-data-model.md#configure-services)
1. [Create an Adaptive Form](/help/forms/creating-adaptive-form-core-components.md)

Now, you can:

* [Connect Microsoft® SharePoint Lists to an Adaptive Form](#connect-an-adaptive-form-to-microsoft-sharepoint-list-connect-af-sharepoint-list)
* [Connect Microsoft® SharePoint Lists to an AEM workflow](#connect-sharepoint-list-workflow)

## Connect an Adaptive Form to Microsoft® SharePoint List {#connect-af-sharepoint-list}

To integrate Microsoft® SharePoint Lists to your Adaptive Form [configure an Adaptive Form to use a Form Data Model](/help/forms/creating-adaptive-form-core-components.md#configure-a-schema-or-form-data-model-for-an-adaptive-formconfigure-schema-or-data-model-for-form)

After configuring an Adaptive Form to use a Form Data Model, you can: 

* [Configure Submit action using a Form Data Model](/help/forms/configuring-submit-actions.md#submit-using-form-data-model)
* [Configure Rule Editor to invoke a Form Data Model](/help/forms/rule-editor.md#invoke-form-data-model-service-invoke)

## Connect Microsoft® SharePoint Lists to an AEM workflow {#connect-sharepoint-list-workflow}

To integrate Microsoft® SharePoint Lists to an AEM Workflow:

1. [Create a workflow to invoke a Form Data model](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html)

    <!--
    To create a new workflow with the editor, perform the following steps:
    1.  Go to your **AEM Forms Author** instance > **[!UICONTROL Tools]** > **[!UICONTROL Workflow]** > **[!UICONTROL Models]**.
    1.  Click **[!UICONTROL Create]** > **[!UICONTROL Create Model]**. The Add Workflow Model dialog appears. 
    1. Specify **[!UICONTROL Title]** and **[!UICONTROL Name (optional)]**.
    1. Click **[!UICONTROL Done]**. The new model is listed in the Workflow Models console.
    1. Select your new workflow, then use **[!UICONTROL Edit]** to open it for configuration.
    1. Add **[!UICONTROL Invoke Form Data Model Service]** step to your workflow.
    1. Confirm the changes with Sync (editor toolbar) to generate the runtime model.
    -->

1. [Configure Submit action to invoke an AEM Workflow](/help/forms/configuring-submit-actions.md#invoke-an-aem-workflow)


Learn how to [use AEM Workflow](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/workflow/use-workflow.html) to collaborate, manage, and process content in an Adaptive Form.

## Best Practices {#best-practices}

* For storing data in a tabular format or implementing data permissions, it is advisable to use Microsoft® SharePoint Lists rather than Microsoft® SharePoint Document Libraries.
* Use the **Delete by ID** property to remove columns that are no longer in use.
* In Microsoft® SharePoint Lists, the following column types are not supported:


## See Also {#see-also}

* [Create a Core-Component based Adaptive Form](/help/forms/creating-adaptive-form-core-components.md)
* [Configure data sources](/help/forms/configuring-submit-actions.md)
* [Create form data model](/help/forms/create-form-data-models.md)
* [Use Forms-centric AEM Workflows - Step Reference to automate business processes](/help/forms/aem-forms-workflow-step-reference.md)

## Additional Information

* [Create or add an Adaptive Form to an AEM Sites page](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md)
* [Embed an Adaptive Form to an AEM Sites page](/help/forms/embed-adaptive-form-aem-sites.md)
* [Create, use, and customize themes in an Adaptive Form](/help/forms/using-themes-in-core-components.md)







