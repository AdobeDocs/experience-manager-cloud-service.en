---
Title: How to submit data from an Adaptive Form to Microsoft® OneDrive?
Description: Explore the streamlined process of connecting AEM Forms with Microsoft® OneDrive using the Submit to OneDrive Submit Action. Learn the step-by-step guide to configure OneDrive and set up submission actions for efficient data storage and retrieval
keywords: AEM Forms OneDrive Integration, Connect to Microsoft OneDrive, OneDrive Configuration Setup with AEM forms
feature: Adaptive Forms, Core Components
exl-id: dbfa4094-1b92-4a7c-a799-f66973d27054
title: "How to configure a Submit Action for an Adaptive Form?"
role: "User, Developer"
---
# Submit an Adaptive Form to Microsoft® OneDrive 

The **[!UICONTROL Submit to OneDrive]** Submit Action connects an Adaptive Form with a Microsoft&reg; OneDrive. You can submit the form data, files, attachments, or Document of Record to the connected Microsoft&reg; OneDrive Storage. 

AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md)  article.

## Advantages

Some of the advantages of seamless integration of AEM Forms and Microsoft® OneDrive are:

* Cross-device accessibility of OneDrive ensures that stored form data is readily available on different platforms. Users can access the submitted data, attachments, and documents from desktops, laptops, tablets, and mobile devices, enhancing accessibility and flexibility.
* OneDrive integration with AEM forms provides a reliable and scalable solution for efficient data storage. All Adaptive Form submissions, such as files, attachments, and Document of Record, can be conveniently saved in OneDrive, ensuring organized and accessible data.

## Connect OneDrive to an Adaptive Form

>[!VIDEO](https://video.tv.adobe.com/v/3424864/connect-aem-adaptive-form-to-onedrive/?quality=12&learn=on)

Configuring OneDrive for AEM Forms submission, perform the following steps:

1. [Create a OneDrive Configuration](#create-a-onedrive-configuration-create-onedrive-configuration): It connects AEM Forms to your Microsoft&reg; OneDrive Storage.
2. [Use the Submit to OneDrive submit action in an Adaptive Form](#use-onedrive-configuration-in-an-adaptive-form-use-onedrive-configuartion-in-af): It connects your Adaptive Form to configured Microsoft&reg; OneDrive.

### Create a OneDrive Configuration {#create-onedrice-configuration}

To connect AEM Forms to your Microsoft&reg; OneDrive Storage:

1. Go to your **AEM Forms Author** instance > **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Microsoft&reg; OneDrive]**.   
1. Once you select the **[!UICONTROL Microsoft&reg; OneDrive]**, you are redirected to **[!UICONTROL OneDrive Browser]**.
1. Select a **Configuration Container**. The configuration is stored in the selected Configuration Container. 
1. Click **[!UICONTROL Create]**. The OneDrive configuration wizard appears. 

    ![OneDrive Configuration Screen](/help/forms/assets/onedrive-configuration.png)

1. Specify the **[!UICONTROL Title]**, **[!UICONTROL Client ID]**, **[!UICONTROL Client Secret]** and **[!UICONTROL OAuth URL]**. For information on how to retrieve Client ID, Client Secret, Tenant ID for OAuth URL, see [Microsoft&reg; Documentation](https://learn.microsoft.com/en-us/graph/auth-register-app-v2).
    * You can retrieve the `Client ID` and `Client Secret` of your app from the Microsoft&reg; Azure portal.
    * In the Microsoft&reg; Azure portal, add the Redirect URI as `https://[author-instance]/libs/cq/onedrive/content/configurations/wizard.html`. Replace `[author-instance]` with the URL of your Author instance.
    * Add the API permissions `offline_access` and `Files.ReadWrite.All` to provide read/write permissions.
    * Use OAuth URL: `https://login.microsoftonline.com/tenant-id/oauth2/v2.0/authorize`. Replace `<tenant-id>` with the `tenant-id` of your app from the Microsoft&reg; Azure portal.

    >[!NOTE]
    >
    > The **client secret** field is mandatory or optional depends upon your Azure Active Directory application configuration. If your application is configured to use a client secret, it is mandatory to provide the client secret.
    
1. Click **[!UICONTROL Connect]**. On a successful connection, the `Connection Successful` message appears. 

1. Now, select **[!UICONTROL OneDrive Container]** > **[OneDrive Folder]**  to save the data. 

    >[!NOTE]
    >
    >* By default, `forms-ootb-storage-adaptive-forms-submission` is present at OneDrive Container. 
    > * Create a folder as `forms-ootb-storage-adaptive-forms-submission`, if not already present by clicking **Create Folder**.

Now, you can use this OneDrive storage configuration for the submit action in an Adaptive Form. 

### Use OneDrive Configuration in an Adaptive Form {#use-onedrive-configuartion-in-af}

You can use the created OneDrive storage configuration in an Adaptive Form, to save data or generated Document of Record in a OneDrive folder. Perform the following steps to use OneDrive storage configuration in an Adaptive Form as:
1. Create an [Adaptive Form](/help/forms/creating-adaptive-form.md).

    >[!NOTE]
    >
    > * Select the same [!UICONTROL Configuration Container] for an Adaptive Form, where you have created your OneDrive storage. 
    > * If no [!UICONTROL Configuration Container] is selected, then the global [!UICONTROL Storage Configuration] folders appear in the Submit Action properties window.

1. Select **Submit Action** as **[!UICONTROL Submit to OneDrive]**.
    ![OneDrive GIF](/help/forms/assets/onedrive-video.gif)
1. Select the **[!UICONTROL Storage Configuration]**, where you want to save your data.
1. Click **[!UICONTROL Save]** to save the Submit settings.

When you submit the form, the data is saved in the specified Microsoft&reg; OneDrive Storage. 
Folder structure to save data is `/folder_name/form_name/year/month/date/submission_id/data`. 

## Related Articles

{{af-submit-action}}
