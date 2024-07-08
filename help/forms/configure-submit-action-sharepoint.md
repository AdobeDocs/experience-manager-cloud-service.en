---
Title: How to send data to a SharePoint storage on submission of an Adaptive Form?
Description: Learn how to send data from your Adaptive Form to a SharePoint storage like a SharePoint list or Document library when you submit the form.
keywords: How to connect SharePoint list for an adpative form?, How to connnect SharePoint document library for an adpative form, Submit to SharePoint, Create a SharePoint Document Library Configuration, Use the Submit to SharePoint submit action in an Adaptive Form, Connect an Adaptive Form to Microsoft&reg; SharePoint List.
feature: Adaptive Forms, Core Components
exl-id: e925a750-5fb5-4950-afd3-78551eec985d
title: "How to configure a Submit Action for an Adaptive Form?"
role: User, Developer
---
# Connect an Adaptive Form to Microsoft® SharePoint

The **[!UICONTROL Submit to SharePoint]** submit action allows you to seamlessly connect your Adaptive Form with a Microsoft® SharePoint storage. It sends the form data to the SharePoint storage of your choice after you submit the form. 

AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md)  article.

## Advantages

Some of the advantages of submitting data from an Adaptive Form to the SharePoint storage are:

* It facilitates the direct submission of form data to SharePoint, providing a centralized location for storing and managing information.
* By applying the SharePoint's access control and permissions features, it ensures that only authorized individuals can view or modify the submitted data.

Using **[!UICONTROL Submit to SharePoint]**, you can:

* [Connect an Adaptive Form to SharePoint Document Library](#connect-af-sharepoint-doc-library)
* [Connect an Adaptive Form to SharePoint List](#connect-af-sharepoint-list)

## Connect an Adaptive Form to SharePoint Document Library {#connect-af-sharepoint-doc-library}

To use the **[!UICONTROL Submit to SharePoint Document Library]** Submit Action in an Adaptive Form:

1. [Create a SharePoint Document Library Configuration](#create-a-sharepoint-configuration-create-sharepoint-configuration): It connects AEM Forms to your Microsoft&reg; Sharepoint Storage.
2. [Use the Submit to SharePoint submit action in an Adaptive Form](#use-sharepoint-configuartion-in-af): It connects your Adaptive Form to configured Microsoft&reg; SharePoint.

### Create a SharePoint Document Library configuration {#create-sharepoint-configuration}

To connect AEM Forms to your Microsoft&reg; Sharepoint Document Library storage:

1. Go to your **AEM Forms Author** instance > **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Microsoft&reg; SharePoint]**.   
1. Once you select the **[!UICONTROL Microsoft&reg; SharePoint]**, you are redirected to **[!UICONTROL SharePoint Browser]**.
1. Select a **Configuration Container**. The configuration is stored in the selected Configuration Container. 
1. Click **[!UICONTROL Create]** > **[!UICONTROL SharePoint Document Library]** from the drop-down list. The SharePoint configuration wizard appears. 

    ![Sharepoint configuration](/help/forms/assets/sharepoint_configuration.png)
1. Specify the **[!UICONTROL Title]**, **[!UICONTROL Client ID]**, **[!UICONTROL Client Secret]** and **[!UICONTROL OAuth URL]**. For information on how to retrieve Client ID, Client Secret, Tenant ID for OAuth URL, see [Microsoft&reg; Documentation](https://learn.microsoft.com/en-us/graph/auth-register-app-v2).
    * You can retrieve the `Client ID` and `Client Secret` of your app from the Microsoft&reg; Azure portal.
    * In the Microsoft&reg; Azure portal, add the Redirect URI as `https://[author-instance]/libs/cq/sharepoint/content/configurations/wizard.html`. Replace `[author-instance]` with the URL of your Author instance.
    * Add the API permissions `offline_access` and `Sites.Manage.All` to provide read/write permissions.The `Sites.Manage.All` is a permission scope in Microsoft's Graph API that grants an application the ability to manage all aspects of SharePoint Sites such as deleting or modifying Sites.  
     
        >[!NOTE]
        >
        > You can also [configure the SharePoint Sites with limited access](/help/forms/configure-sharepoint-site-limited-access.md) by using the `Sites.Selected` permission scope in Microsoft's Graph API. The `Sites.Selected` is a permission scope in Microsoft's Graph API that allows more granular and restricted access to SharePoint sites. 

    * Use OAuth URL: `https://login.microsoftonline.com/tenant-id/oauth2/v2.0/authorize`. Replace `<tenant-id>` with the `tenant-id` of your app from the Microsoft&reg; Azure portal.

    >[!NOTE]
    >
    > The **client secret** field is mandatory or optional depends upon your Azure Active Directory application configuration. If your application is configured to use a client secret, it is mandatory to provide the client secret.
    
1. Click **[!UICONTROL Connect]**. On a successful connection, the `Connection Successful` message appears. 

1. Now, select **SharePoint Site** > **Document Library** > **SharePoint Folder**, to save the data.

    >[!NOTE]
    >
    >* By default, `forms-ootb-storage-adaptive-forms-submission` is present at selected SharePoint Site.
    >* Create a folder as `forms-ootb-storage-adaptive-forms-submission`, if not already present in the `Documents` library of the selected SharePoint Site by clicking **Create Folder**.

Now, you can use this SharePoint Sites configuration for the submit action in an Adaptive Form. 

### Use SharePoint Document Library Configuration in an Adaptive Form {#use-sharepoint-configuartion-in-af}

You can use the created SharePoint Document Library configuration in an Adaptive Form, to save data or generated Document of Record in a SharePoint folder. Perform the following steps to use a SharePoint Document Library storage configuration in an Adaptive Form as:

1. Create an [Adaptive Form](/help/forms/creating-adaptive-form-core-components.md).

    >[!NOTE]
    >
    > * Select the same [!UICONTROL Configuration Container] for an Adaptive Form, where you have created your SharePoint Document Library storage. 
    > * If no [!UICONTROL Configuration Container] is selected, then the global [!UICONTROL Storage Configuration] folders appear in the Submit Action properties window.

1. Select **Submit Action** as **[!UICONTROL Submit to SharePoint]**.
    ![Sharepoint GIF](/help/forms/assets/sharedrive-video.gif)
1. Select the **[!UICONTROL Storage Configuration]**, where you want to save your data.
1. Click **[!UICONTROL Save]** to save the Submit settings.

When you submit the form, the data is saved in the specified Microsoft&reg; Sharepoint Document Library Storage. 
Folder structure to save data is `/folder_name/form_name/year/month/date/submission_id/data`. 

## Connect an Adaptive Form to Microsoft&reg; SharePoint List {#connect-af-sharepoint-list}

>[!VIDEO](https://video.tv.adobe.com/v/3424820/connect-aem-adaptive-form-to-sharepointlist/?quality=12&learn=on)

To use the [!UICONTROL Submit to SharePoint List] Submit Action in an Adaptive Form:

1. [Create a SharePoint List Configuration](#create-sharepoint-list-configuration): It connects AEM Forms to your Microsoft&reg; Sharepoint List Storage.
1. [Use the Submit using Form Data Model (FDM) in an Adaptive Form](#use-submit-using-fdm): It connects your Adaptive Form to configured Microsoft&reg; SharePoint.

### Create a SharePoint List Configuration {#create-sharepoint-list-configuration}

To connect AEM Forms to your Microsoft&reg; Sharepoint List:

1. Go to **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Microsoft&reg; SharePoint]**.   
1. Select a **Configuration Container**. The configuration is stored in the selected Configuration Container. 
1. Click **[!UICONTROL Create]** > **[!UICONTROL SharePoint List]** from the drop-down list. The SharePoint configuration wizard appears.  
1. Specify the **[!UICONTROL Title]**, **[!UICONTROL Client ID]**, **[!UICONTROL Client Secret]** and **[!UICONTROL OAuth URL]**. For information on how to retrieve Client ID, Client Secret, Tenant ID for OAuth URL, see [Microsoft&reg; Documentation](https://learn.microsoft.com/en-us/graph/auth-register-app-v2).
    * You can retrieve the `Client ID` and `Client Secret` of your app from the Microsoft&reg; Azure portal.
    * In the Microsoft&reg; Azure portal, add the Redirect URI as `https://[author-instance]/libs/cq/sharepointlist/content/configurations/wizard.html`. Replace `[author-instance]` with the URL of your Author instance.
    * Add the API permissions `offline_access` and `Sites.Manage.All` in the **Microsoft&reg; Graph** tab to provide read/write permissions. Add `AllSites.Manage` permission in the **Sharepoint** tab to interact remotely with SharePoint data.
    * Use OAuth URL: `https://login.microsoftonline.com/tenant-id/oauth2/v2.0/authorize`. Replace `<tenant-id>` with the `tenant-id` of your app from the Microsoft&reg; Azure portal.

      >[!NOTE]
      >
      > The **client secret** field is mandatory or optional depends upon your Azure Active Directory application configuration. If your application is configured to use a client secret, it is mandatory to provide the client secret.

1. Click **[!UICONTROL Connect]**. On a successful connection, the `Connection Successful` message appears.
1. Select **[!UICONTROL SharePoint Site]** and **[!UICONTROL SharePoint List]** from the drop-down list.
1. Select **[!UICONTROL Create]** to create the cloud configuration for the Microsoft&reg; SharePointList.


### Use the Submit using Form Data Model (FDM) in an Adaptive Form {#use-submit-using-fdm}

You can use the created SharePoint List configuration in an Adaptive Form, to save data or generated Document of Record in a SharePoint List. Perform the following steps to use a SharePoint List in an Adaptive Form as:

1. [Create a Form Data Model (FDM) using Microsoft&reg; SharePoint List configuration](/help/forms/create-form-data-models.md)
1. [Configure the Form Data Model (FDM) to retrieve and send data](/help/forms/work-with-form-data-model.md#configure-services)
1. [Create an Adaptive Form](/help/forms/creating-adaptive-form-core-components.md)
1. [Configure Submit action using a Form Data Model (FDM)](/help/forms/using-form-data-model.md)

When you submit the form, the data is saved in the specified Microsoft&reg; Sharepoint List Storage. 

>[!NOTE]
>
> In Microsoft&reg; SharePoint List, the following column types are not supported:
> * image column
> * metadata column
> * person column
> * external data column

## Related Articles

{{af-submit-action}}
