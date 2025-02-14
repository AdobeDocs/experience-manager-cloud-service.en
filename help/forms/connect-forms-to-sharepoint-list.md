---
Title: How to send data to a SharePoint List storage on submission of an Adaptive Form?
Description: Learn how to send data from your Adaptive Form to a SharePoint storage like a SharePoint list when you submit the form.
keywords: How to connect SharePoint list for an adpative form?, Submit to SharePoint, Create a SharePoint List Configuration, Use the Submit to SharePoint submit action in an Adaptive Form, Connect an Adaptive Form to Microsoft&reg; SharePoint List.
feature: Adaptive Forms, Core Components
title: How to configure a Submit Action for an Adaptive Form?
role: User, Developer
exl-id: 9ac3e7be-c6fa-4dbc-9aba-b81741ba6c55
---
# Connect an Adaptive Form to Microsoft&reg; SharePoint List {#connect-af-sharepoint-list}

>[!VIDEO](https://video.tv.adobe.com/v/3424820/connect-aem-adaptive-form-to-sharepointlist/?quality=12&learn=on)

To use the [!UICONTROL Submit to SharePoint List] Submit Action in an Adaptive Form:

1. [Create a SharePoint List Configuration](#1-create-a-sharepoint-list-configuration): It connects AEM Forms to your Microsoft&reg; Sharepoint List Storage.
1. [Use the Submit using Form Data Model (FDM) in an Adaptive Form](#2-use-the-submit-using-form-data-model-fdm-in-an-adaptive-form-use-submit-using-fdm): It connects your Adaptive Form to configured Microsoft&reg; SharePoint.

## 1. Create a SharePoint List Configuration 

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


## 2. Use the Submit using Form Data Model (FDM) in an Adaptive Form {#use-submit-using-fdm}

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
