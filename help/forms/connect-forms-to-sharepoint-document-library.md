---
Title: How to integrate Adaptive Form to a SharePoint Document Library?
Description: This article explains how to send data from your Adaptive Form to a SharePoint  Document library when you submit the form.
keywords: How to connnect SharePoint document library for an adpative form, Submit to SharePoint, Create a SharePoint Document Library Configuration, Use the Submit to SharePoint submit action in an Adaptive Form, AEM Forms Data Model SharePoint Document Library, Forms Data Model SharePoint Document Library, Integrate Forms Data Model to SharePoint Document Library
feature: Adaptive Forms, Core Components
role: User, Developer
exl-id: a00b4a93-2324-4c2a-824f-49146dc057b0
---
# Connect an Adaptive Form to Microsoft® SharePoint Document Library {#connect-af-sharepoint-doc-library}

>[!VIDEO](https://video.tv.adobe.com/v/3444368/formautomation-productivitytools-adaptiveforms--sharepointintegration-documentlibrary/?quality=12&learn=on)

To use the **[!UICONTROL Submit to SharePoint Document Library]** Submit Action in an Adaptive Form:

1. [Create a SharePoint Document Library Configuration](#1-create-a-sharepoint-document-library-configuration): It connects AEM Forms to your Microsoft&reg; Sharepoint Storage.
2. [Use the Submit to SharePoint submit action in an Adaptive Form](#2-use-sharepoint-document-library-configuration-in-an-adaptive-form): It connects your Adaptive Form to configured Microsoft&reg; SharePoint.

## 1. Create a SharePoint Document Library configuration

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

1. The `offline_access Sites.Selected` permission scope in Microsoft's Graph API that allows more granular and restricted access to SharePoint sites. The `offline_access Sites.Manage.All` permission scope in Microsoft's Graph API that allows full access to SharePoint sites.   
1. Click **[!UICONTROL Connect]**. On a successful connection, the `Connection Successful` message appears. 

1. Now, select **SharePoint Site** > **Document Library** > **SharePoint Folder**, to save the data.

    >[!NOTE]
    >
    >* By default, `forms-ootb-storage-adaptive-forms-submission` is present at selected SharePoint Site.
    >* Create a folder as `forms-ootb-storage-adaptive-forms-submission`, if not already present in the `Documents` library of the selected SharePoint Site by clicking **Create Folder**.

Now, you can use this SharePoint Sites configuration for the submit action in an Adaptive Form. 

### 2. Use SharePoint Document Library Configuration in an Adaptive Form

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

## Related Articles

{{af-submit-action}}
