---
Title: How to configure a SharePoint Site with limited access using authorization scope?
Description: Learn how to configure SharePoint Site with limited access using the authorization scope.
keywords: How to configure SharePoint Site with limited access?, Configure SharePoint with limited access, Using authorization scope to limit access for SharePoint Site.
feature: Adaptive Forms, Core Components
role: User, Developer
exl-id: 3230bab2-c1aa-409d-9f01-c42cf88b1135
---
<span class="preview"> The feature is available under the early adopter program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

# Configure SharePoint Site with limited access using authorization scope

The purpose of limited or restricted access is to enhance security management by allowing administrators to control user access to a particular SharePoint Site or a group of SharePoint Sites. The permission level is useful when you need to grant a user or group access to a specific Site without allowing them to view any other non-allowed SharePoint Sites.

## Advantages to configure SharePoint Site with the limited access 

Advantages to provide limited access to SharePoint Site:

* **Enhanced security**: By limiting access, you can ensure that only authorized personnel have the ability to view or manipulate sensitive information, reducing the risk of unauthorized access.

* **Principle of least privilege**: It provides users with the minimum levels of access—or permissions—needed to perform their job functions. This minimizes each user's exposure to sensitive parts of the network, which can protect against potential internal threats.

* **Data protection**: Restricted access helps in safeguarding critical data against exposure. It ensures that only users who need to see the data can access it, which is essential for complying with data protection regulations.

* **Accidental data loss prevention**: With fewer people able to modify content, the chances of accidental deletions or alterations of important data is significantly reduced.

* **Controlled Data Flow**: It helps in controlling the flow of information within and outside the organization, ensuring that data does not end up in the wrong hands.

## Configure SharePoint with limited access using authorization scope

Follow the steps below to configure SharePoint Sites with limited access using authorization scopes:

1. [Create an application with the `Sites.Selected` permission scope in Azure portal](#create-an-application-with-the-limited-permission-in-the-azure-portal)
1. [Set the authorization scope at AEM instance](#set-the-authorization-scope-at-aem-instance)

### Create an application with the limited permission in the Azure portal

Create an application in [Microsoft Azure portal](https://portal.azure.com/#home) with the `Sites.Selected` permission scope in Microsoft's Graph API. 

![SharePoint Selected Site](/help/forms/assets/sharepoint-selected-site.png)

For information on how to retrieve `Client ID`, `Client Secret` and `Tenant ID` for `OAuth URL`, see [Microsoft&reg; Documentation](https://learn.microsoft.com/en-us/graph/auth-register-app-v2).
* In the Microsoft&reg; Azure portal, add the Redirect URI as `https://[author-instance]/libs/cq/sharepoint/content/configurations/wizard.html`. Replace `[author-instance]` with the URL of your Author instance.
* Add the `offline_access` and `Sites.Selected` permissions scope in Microsoft's Graph API to provide restricted access to Sites.
* For OAuth URL: `https://login.microsoftonline.com/tenant-id/oauth2/v2.0/authorize`. Replace `<tenant-id>` with the `tenant-id` of your app from the Microsoft&reg; Azure portal.

To use the `Sites.Selected` API permission requires an application registered in the Azure portal with the appropriate permissions set for SharePoint Online Sites. This setup ensures that the application has the necessary authorization to interact with the SharePoint Site within the defined scope, thereby providing the required limited access. 
    
Refer to the [blog article - Develop Applications that use Sites.Selected permissions for SPO sites](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476) for instructions on developing applications that use `Sites.Selected` permissions for SharePoint Online Sites.

### Set the authorization scope at AEM instance

To provide limited access to a Microsoft SharePoint Site, it is essential to set the authorization scope correctly. To set the authorization scope and connect AEM Forms to your Microsoft&reg; SharePoint storage:

1. Go to your **AEM Forms Author** instance > **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Microsoft&reg; SharePoint]**.   
1. Once you select the **[!UICONTROL Microsoft&reg; SharePoint]**, you are redirected to **[!UICONTROL SharePoint Browser]**.
1. Select a **Configuration Container**. The configuration is stored in the selected Configuration Container. 
1. Click **[!UICONTROL Create]** > **[!UICONTROL SharePoint Document Library]** from the drop-down list. The SharePoint configuration wizard appears. 

    ![SharePoint Site Limited Site Access](/help/forms/assets/sharepoint-doc-library-limited-scopes.png)

1. Specify the **[!UICONTROL Title]**, **[!UICONTROL Client ID]** and **[!UICONTROL Client Secret]**. For information on how to retrieve Client ID and Client Secret, see [Microsoft&reg; Documentation](https://learn.microsoft.com/en-us/graph/auth-register-app-v2).
    
1. Use OAuth URL as `https://login.microsoftonline.com/tenant-id/oauth2/v2.0/authorize`. Replace `<tenant-id>` with the `tenant-id` of your app from the Microsoft&reg; Azure portal.

    >[!NOTE]
    >
    > The **client secret** field is mandatory or optional depends upon your Azure Active Directory application configuration. If your application is configured to use a client secret, it is mandatory to provide the client secret.

1. Add the `offline_access Sites.Selected` in the `Authorization Scope` field. When you add the `offline_access Sites.Selected` scope in the `Authorization Scope` textbox field, the `SharePoint Site ID` textbox becomes visible on the screen. 

1. Specify the SharePoint Site ID. To learn how to retrieve the SharePoint Site ID, refer to the [Extra Bytes](#extra-bytes) section.

1. Click **[!UICONTROL Check Site Connection]**. On a successful connection, the `Connection Successful` message appears. 

1. Now, select **SharePoint Site** > **Document Library** > **SharePoint Folder**, to save the data.

    >[!NOTE]
    >
    >* By default, `forms-ootb-storage-adaptive-forms-submission` is present at selected SharePoint Site.
    >* Create a folder as `forms-ootb-storage-adaptive-forms-submission`, if not already present in the `Documents` library of the selected SharePoint Site by clicking **Create Folder**.

Now, you can use this [SharePoint Sites configuration for the submit action in an Adaptive Form](/help/forms/configure-submit-action-sharepoint.md#use-sharepoint-document-library-configuration-in-an-adaptive-form-use-sharepoint-configuartion-in-af). 

## Extra Bytes

To retrieve the value of the `SharePoint Site ID`:
1. Go to the [Microsoft Graph Explorer APIs](https://developer.microsoft.com/en-us/graph/graph-explorer).
1. In the left pane, under the `SharePoint Sites` APIs, click `Search for a SharePoint site by keyword`.
1. Replace the placeholder `contoso` with the actual name of your SharePoint Site to fetch the corresponding Site ID.

    ![SharePoint Document Library ID](/help/forms/assets/sharepoint-site-id.png)

Upon clicking the `Run Query` button, the Site ID is displayed on the screen.
