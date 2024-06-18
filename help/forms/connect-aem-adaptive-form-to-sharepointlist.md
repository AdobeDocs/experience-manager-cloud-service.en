---
title: How to connect AEM Adaptive Form to Microsoft&reg; SharePoint List?
description: Connect an Adaptive Form to Microsoft&reg; SharePoint List. Learn how to configure the Microsoft&reg; SharePoint list and create a Form Data Model (FDM) using the configuration. In addition, you earn how to integrate the FDM with your Adaptive Form.
role: User, Developer
keywords: connect AEM Adaptive Form to Microsoft SharePoint List, connect Adaptive Form to Microsoft SharePoint List, integrate AEM Adaptive Form to Microsoft SharePoint List, integrate Adaptive Form to Microsoft SharePoint List, submit data from an Adaptive Form to SharePoint List, submit AEM workflow to SharePoint List.
hide: yes
hidefromToC: yes
---

# Connect an Adaptive Form to Microsoft&reg; SharePoint List 

<span class="preview"> This is a pre-release feature and accessible through our [pre-release channel](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features). </span>

**Microsoft&reg; SharePoint**: Microsoft&reg; SharePoint enables collaboration by providing dynamic and efficient team sites for all teams, departments, and divisions. It is used to store, organize, share, and access information from any device using any web browser, for example, Microsoft&reg; Edge, Internet Explorer, Chrome, or Firefox. The two main components of **Microsoft&reg; SharePoint** are:

* **Microsoft&reg; SharePoint Document Library**: Microsoft&reg; SharePoint Document Library displays a list of files and folders along with their key information, such as the last modified date and the owner of a file. This feature makes the organization and navigation of files easy.
For instructions on how to integrate a **Microsoft&reg; SharePoint Document Library** with an Adaptive Form, see the [Adaptive Form Submit Action](/help/forms/configuring-submit-actions.md#submit-to-sharepoint) article.

* **Microsoft&reg; SharePoint List**: Microsoft&reg; SharePoint List is a collection of data. You can add columns for different types of data and create views to display data effectively. You can group, filter, sort, and format the lists easily. 

>[!VIDEO](https://video.tv.adobe.com/v/3424820/connect-aem-adaptive-form-to-sharepointlist/?quality=12&learn=on)

## Prerequisites to connect an Adaptive Form to Microsoft&reg; SharePoint List {#prerequisites}

Before connecting an Adaptive Form to Microsoft&reg; SharePoint List, perform the following steps:

1. [Configure Microsoft&reg; SharePoint List](/help/forms/configure-data-sources.md#configure-microsoft-sharepoint-list)
1. [Create a Form Data Model (FDM) using Microsoft&reg; SharePoint List configuration](/help/forms/create-form-data-models.md)
1. [Configure the Form Data Model (FDM) to retrieve and send data](/help/forms/work-with-form-data-model.md#configure-services)
1. [Create an Adaptive Form](/help/forms/creating-adaptive-form-core-components.md)

Now, you can:

* [Connect Microsoft&reg; SharePoint List to an Adaptive Form](#connect-an-adaptive-form-to-microsoft-sharepoint-list-connect-af-sharepoint-list)
* [Connect Microsoft&reg; SharePoint List to an AEM workflow](#connect-sharepoint-list-workflow)

## Connect an Adaptive Form to Microsoft&reg; SharePoint List {#connect-af-sharepoint-list}

To integrate Microsoft&reg; SharePoint List to your Adaptive Form [configure an Adaptive Form to use a Form Data Model (FDM)](/help/forms/creating-adaptive-form-core-components.md#configure-a-schema-or-form-data-model-for-an-adaptive-formconfigure-schema-or-data-model-for-form)

After configuring an Adaptive Form to use a Form Data Model (FDM), you can: 

* [Configure Submit action using a Form Data Model (FDM)](/help/forms/configuring-submit-actions.md#submit-using-form-data-model)
* [Configure Rule Editor to invoke a Form Data Model (FDM)](/help/forms/rule-editor.md#invoke-form-data-model-service-invoke)

## Connect Microsoft&reg; SharePoint List to an AEM workflow {#connect-sharepoint-list-workflow}

To integrate Microsoft&reg; SharePoint List to an AEM Workflow:

1. [Create a workflow to invoke a Form Data model (FDM)](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html)

    <!--
    To create a workflow with the editor:
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

<!-- * For storing data in a tabular format or implementing data permissions, it is advisable to use Microsoft&reg; SharePoint List rather than Microsoft&reg; SharePoint Document Library. -->
* In Microsoft&reg; SharePoint List, the following column types are not supported:
    * image column
    * metadata column
    * person column
    * external data column

## See Also {#see-also}

* [Create a Core-Component based Adaptive Form](/help/forms/creating-adaptive-form-core-components.md)
* [Configure data sources](/help/forms/configuring-submit-actions.md)
* [Create form data model (FDM)](/help/forms/create-form-data-models.md)
* [Use Forms-centric AEM Workflows - Step Reference to automate business processes](/help/forms/aem-forms-workflow-step-reference.md)
* [Create a custom Submit Action for Adaptive Forms](/help/forms/custom-submit-action-form.md)
* [Create or add an Adaptive Form to an AEM Sites page](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md)
* [Embed an Adaptive Form to an AEM Sites page](/help/forms/embed-adaptive-form-aem-sites.md)
* [Create, use, and customize themes in an Adaptive Form](/help/forms/using-themes-in-core-components.md)







