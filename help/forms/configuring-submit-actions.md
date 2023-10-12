---
title: How to configure a Submit Action for an Adaptive Form?
description: An Adaptive Form provides multiple Submit Actions. A Submit Action defines how an Adaptive Form is processed after submission. You can use built-in Submit Actions or create your own.
exl-id: a4ebedeb-920a-4ed4-98b3-2c4aad8e5f78
---
# Adaptive Form Submit Action {#configuring-the-submit-action}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/configuring-submit-actions.html)                  |
| AEM as a Cloud Service     | This article         |

**Applies to**: ✔️ Adaptive Form Foundation Components. ❌ [Adaptive Form Core Components](/help/forms/configure-submit-actions-core-components.md). Adobe recommends using Core Components to [add Adaptive Forms to an AEM Sites Page](create-or-add-an-adaptive-form-to-aem-sites-page.md) or to [create standalone Adaptive Forms](creating-adaptive-form-core-components.md).

A Submit Action is triggered when a user clicks the **[!UICONTROL Submit]** button on an Adaptive Form. Forms as a Cloud Service provides the following Submit Actions out of the box. 

* [Submit to REST endpoint](#submit-to-rest-endpoint)
* [Send email](#send-email)
* [Submit using Form Data Model](#submit-using-form-data-model)
* [Invoke an AEM Workflow](#invoke-an-aem-workflow)
* [Submit to SharePoint](#submit-to-sharedrive)
* [Submit to OneDrive](#submit-to-onedrive)
* [Submit to Azure Blob Storage](#azure-blob-storage)
* [Submit to Power Automate](#microsoft-power-automate)

You can also [extend the default Submit Actions](custom-submit-action-form.md) to create your own Submit Action. 

You can configure a Submit Action in the **[!UICONTROL Submission]** section of the Adaptive Form Container properties, in the sidebar.

![Configure Submit Action](assets/submission.png)


<!-- [!NOTE]
>
>Send PDF via Email Submit Action is applicable only to Adaptive Forms that use XFA template as form model. 

>[!NOTE]
>
>Ensure that the [AEM_Installation_Directory]\crx-quickstart\temp\datamanager\ASM folder
>exists. The directory is required to temporarily store attachments. If the directory does not exist, create it. -->

<!--

>[!CAUTION]
>
>If you  [prefill](prepopulate-adaptive-form-fields.md) a form template,  a Form Data Model or schema based Adaptive Form with XML or JSON data complaint to a schema (XML schema, JSON schema , form template, or form data model) that is data does not contain &lt;afData&gt;, &lt;afBoundData&gt;, and &lt;/afUnboundData&gt; tags, then the data of unbounded fields (Unbounded fields are Adaptive Form fields without [bindref](prepopulate-adaptive-form-fields.md) property) of the Adaptive Form is lost. 

>[!CAUTION]
>
>If you [prefill](prepopulate-adaptive-form-fields.md) a form template, a Form Data Model or schema based Adaptive Form with XML or JSON data complaint to a schema (XML schema, JSON schema, or form data model) that does not contain &lt;afData&gt;, &lt;afBoundData&gt;, and &lt;/afUnboundData&gt; tags, then the data of unbounded fields (Unbounded fields are Adaptive Form fields without [bindref](prepopulate-adaptive-form-fields.md) property) of the Adaptive Form is lost.


-->

## Submit to REST endpoint {#submit-to-rest-endpoint}

Use the **[!UICONTROL Submit to REST Endpoint]** action to post the submitted data to a rest URL. The URL can be of an internal (the server on which the form is rendered) or an external server.

To post data to an internal server, provide path of the resource. The data is posted the path of the resource. For example, /content/restEndPoint. For such post requests, the authentication information of the submit request is used.

To post data to an external server, provide a URL. The format of the URL is `https://host:port/path_to_rest_end_point`. Ensure that you configure the path to handle the POST request anonymously.

![Mapping for field values passed as Thank You Page parameters](assets/post-enabled-actionconfig.png)

In the example above, user entered information in `textbox` is captured using parameter `param1`. Syntax to post data captured using `param1` is:

`String data=request.getParameter("param1");`

Similarly, parameters that you use for posting XML data and attachments are `dataXml` and `attachments`.

For example, you use these two parameters in your script to parse data to a rest end point. You use the following syntax to store and parse the data:

`String data=request.getParameter("dataXml");`
`String att=request.getParameter("attachments");`

In this example, `data` stores the XML data, and `att` stores attachment data.

The **[!UICONTROL Submit to REST endpoint]** Submit Action submits the data filled in the form to a configured confirmation page as part of the HTTP GET request. You can add the name of the fields to request. The format of the request is:

`{fieldName}={request parameter name}`

As shown in the image below, `param1` and `param2` are passed as parameters with values copied from the **textbox** and **numericbox** fields for the next action.

![Configuring Rest Endpoint Submit Action](assets/action-config.png)

You can also **[!UICONTROL Enable POST request]** and provide a URL to post the request. To submit data to the AEM server hosting the form, use a relative path corresponding to the root path of the AEM server. For example, `/content/forms/af/SampleForm.html`. To submit data to any other server, use absolute path.

>[!NOTE]
>
>To pass the fields as parameters in a REST URL, all the fields must have different element names, even if the fields are placed on different panels.

## Send Email {#send-email}

You can use the **[!UICONTROL Send Email]** Submit Action to send an email to one or more recipients on successful submission of the form. The email generated can contain form data in a predefined format. For example, in the following template, customer name, shipping address, name of the state, and zip code are retrieved from submitted form data.

    ```

    Hi ${customer_Name},

    The following is set as your deafult shipping address:
    ${customer_Name},
    ${customer_Shipping_Address},
    ${customer_State},
    ${customer_ZIPCode}

    Regards,
    WKND 

    ```

>[!NOTE]
>
> * All the form fields must have different element names, even if the fields are placed on different panels of an Adaptive Form.
> * AEM as a Cloud Service requires outbound mail to be encrypted. By default, outbound email is disabled. To activate it, submit a support ticket to [Requesting Access](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html?lang=en#sending-email). 

You can also include attachments and a Document of Record (DoR) to the email. To enable **[!UICONTROL Attach Document of Record]** option, configure the Adaptive Form to generate a Document of Record (DoR). You can enable the option to generate a Document of Record from Adaptive Form properties.



<!-- ## Send PDF via Email {#send-pdf-via-email}

The **Send PDF via Email** Submit Action sends an email with a PDF containing form data, to one or more recipients on successful submission of the form.

>[!NOTE]
>
>This Submit Action is available for XFA-based Adaptive Forms and XSD-based adaption forms that have the Document of Record template. -->

<!-- ## Invoke a forms workflow {#invoke-a-forms-workflow}

The **Submit to Forms workflow** submit option sends a data xml and file attachments (if any) to an existing Adobe LiveCycle or [!DNL AEM Forms] on JEE process.

For information about how to configure the Submit to forms workflow Submit Action, see [Submitting and processing your form data using forms workflows](submit-form-data-livecycle-process.md). -->

## Submit using Form Data Model {#submit-using-form-data-model}

The **[!UICONTROL Submit using Form Data Model]** Submit Action writes submitted Adaptive Form data for the specified data model object in a Form Data Model to its data source. When configuring the Submit Action, you can choose a data model object whose submitted data you want to write back to its data source.

In addition, you can submit a form attachment using a Form Data Model and a Document of Record (DoR) to the data source. For information about form data model, see [[!DNL AEM Forms] Data Integration](data-integration.md).

<!--
## Forms Portal Submit Action {#forms-portal-submit-action}

The **Forms Portal Submit Action** option makes form data available through an [!DNL AEM Forms] portal.

For more information about the Forms Portal and Submit Action, see [Drafts and submissions component](draft-submission-component.md). -->

## Invoke an AEM Workflow {#invoke-an-aem-workflow}

The **[!UICONTROL Invoke an AEM Workflow]** Submit Action associates an Adaptive Form with an [AEM Workflow](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html?lang=en#extending-aem). When a form is submitted, the associated workflow starts automatically on the Author instance. You can save the data file, attachments, and Document of Record to the payload location of the workflow or to a variable. If the workflow is marked for external data storage and configured for an external data storage, then only the variable option is available. You can select from the list of variables available for the workflow model. If the workflow is marked for external data storage at a later stage and not at the time of workflow creation, then ensure that the required variable configurations are in place.

The Submit Action places the following at the payload location of the workflow, or the variable if the workflow is marked for external data storage: 

* **Data file**: It contains data submitted to the Adaptive Form. You can use the **[!UICONTROL Data File Path]** option to specify the name of the file and path of file relative to the payload. For example, the `/addresschange/data.xml` path creates a folder named `addresschange` and places it relative to payload. You can also specify only `data.xml` to send only submitted data without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model. 

* **Attachments**: You can use the **[!UICONTROL Attachment Path]** option to specify the folder name to store the attachments uploaded to the Adaptive Form. The folder is created relative to the payload. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model.
 
* **Document of Record**: It contains the Document of Record generated for the Adaptive Form. You can use the **[!UICONTROL Document of Record Path]** option to specify the name of the Document of Record file and path of file relative to the payload. For example, the `/addresschange/DoR.pdf` path creates a folder named `addresschange` relative to the payload and places the `DoR.pdf` relative to payload. You can also specify only `DoR.pdf` to save only Document of Record without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model.

Before using the **[!UICONTROL Invoke an AEM Workflow]** Submit Action configure the following for the **[!UICONTROL AEM DS settings service]** configuration: 

* **[!UICONTROL Processing Server URL]**: The Processing Server is the server where the Forms or AEM Workflow is triggered. This can be same as the URL of the AEM author instance or another server.

* **[!UICONTROL Processing Server User Name]**: Workflow user's username

* **[!UICONTROL Processing Server Password]**: Workflow user's password

## Submit to SharePoint {#submit-to-sharedrive}

The **[!UICONTROL Submit to SharePoint]** Submit Action connects an Adaptive Form with a Microsoft&reg; SharePoint Storage. You can submit the form data file, attachments, or Document of Record to the connected Microsoft&reg; Sharepoint Storage. To use the **[!UICONTROL Submit to SharePoint]** Submit Action in an Adaptive Form:

1. [Create a SharePoint Configuration](#create-a-sharepoint-configuration-create-sharepoint-configuration): It connects AEM Forms to your Microsoft&reg; Sharepoint Storage.
2. [Use the Submit to SharePoint submit action in an Adaptive Form](#use-sharepoint-configuartion-in-af): It connects your Adaptive Form to configured Microsoft&reg; SharePoint.

### Create a SharePoint Configuration {#create-sharepoint-configuration}

To connect AEM Forms to your Microsoft&reg; Sharepoint Storage:

1. Go to your **AEM Forms Author** instance > **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Microsoft&reg; SharePoint]**.   
1. Once you select the **[!UICONTROL Microsoft&reg; SharePoint]**, you are redirected to **[!UICONTROL SharePoint Browser]**.
1. Select a **Configuration Container**. The configuration is stored in the selected Configuration Container. 
1. Click **[!UICONTROL Create]** > **[!UICONTROL SharePoint Document Library]** from the drop-down list. The SharePoint configuration wizard appears. 

 ![Sharepoint configuration](/help/forms/assets/sharepoint_configuration.png)
1. Specify the **[!UICONTROL Title]**, **[!UICONTROL Client ID]**, **[!UICONTROL Client Secret]** and **[!UICONTROL OAuth URL]**. For information on how to retrieve Client ID, Client Secret, Tenant ID for OAuth URL, see [Microsoft&reg; Documentation](https://learn.microsoft.com/en-us/graph/auth-register-app-v2).
    * You can retrieve the `Client ID` and `Client Secret` of your app from the Microsoft&reg; Azure portal.
    * In the Microsoft&reg; Azure portal, add the Redirect URI as `https://[author-instance]/libs/cq/sharepoint/content/configurations/wizard.html`. Replace `[author-instance]` with the URL of your Author instance.
    * Add the API permissions `offline_access` and `Sites.Manage.All` to provide read/write permissions.
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

### Use SharePoint Configuration in an Adaptive Form {#use-sharepoint-configuartion-in-af}

You can use the created SharePoint configuration in an Adaptive Form, to save data or generated Document of Record in a SharePoint folder. Perform the following steps to use a SharePoint storage configuration in an Adaptive Form as:

1. Create an [Adaptive Form](/help/forms/creating-adaptive-form.md).

    >[!NOTE]
    >
    > * Select the same [!UICONTROL Configuration Container] for an Adaptive Form, where you have created your SharePoint storage. 
    > * If no [!UICONTROL Configuration Container] is selected, then the global [!UICONTROL Storage Configuration] folders appear in the Submit Action properties window.

1. Select **Submit Action** as **[!UICONTROL Submit to SharePoint]**.
    ![Sharepoint GIF](/help/forms/assets/sharedrive-video.gif)
1. Select the **[!UICONTROL Storage Configuration]**, where you want to save your data.
1. Click **[!UICONTROL Save]** to save the Submit settings.

When you submit the form, the data is saved in the specified Microsoft&reg; Sharepoint Storage. 
Folder structure to save data is `/folder_name/form_name/year/month/date/submission_id/data`. 

## Submit to OneDrive {#submit-to-onedrive}

The **[!UICONTROL Submit to OneDrive]** Submit Action connects an Adaptive Form with a Microsoft&reg; OneDrive. You can submit the form data, file, attachments, or Document of Record to the connected Microsoft&reg; OneDrive Storage. To use the [!UICONTROL Submit to OneDrive] Submit Action in an Adaptive Form:

1. [Create a OneDrive Configuration](#create-a-onedrive-configuration-create-onedrive-configuration): It connects AEM Forms to your Microsoft&reg; OneDrive Storage.
2. [Use the Submit to OneDrive submit action in an Adaptive Form](#use-onedrive-configuration-in-an-adaptive-form-use-onedrive-configuartion-in-af): It connects your Adaptive Form to
configured Microsoft&reg; OneDrive.

### Create a OneDrive Configuration {#create-onedrice-configuration}

>[!VIDEO](https://video.tv.adobe.com/v/3424864/connect-aem-adaptive-form-to-onedrive/?quality=12&learn=on)

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

## Submit to Azure Blob Storage {#submit-to-azure-blob-storage}

The **[!UICONTROL Submit to Azure Blob Storage]**  Submit Action connects an Adaptive Form with a Microsoft&reg; Azure portal. You can submit the form data, file, attachments, or Document of Record to the connected Azure Storage containers. To use the  Submit action for Azure Blob Storage: 

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
    
1. Click **[!UICONTROL Save]**.

Now, you can use this Azure Storage container configuration for the submit action in an Adaptive Form.

### Use Azure Storage Configuration in an Adaptive Form {#use-azure-storage-configuartion-in-af}

You can use the created Azure Storage container configuration in an Adaptive Form, to save data or generated Document of Record in Azure Storage container. Perform the following steps to use Azure Storage container configuration in an Adaptive Form as:
1. Create an [Adaptive Form](/help/forms/creating-adaptive-form.md).

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

To set values of a configuration, [Generate OSGi Configurations using the AEM SDK](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/configuring-osgi.html?lang=en#generating-osgi-configurations-using-the-aem-sdk-quickstart), and [deploy the configuration](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/deploy-code.html?lang=en#deployment-process) to your Cloud Service instance.


## Submit to Power Automate {#microsoft-power-automate}

You can configure an Adaptive Form to run a Microsoft&reg; Power Automate Cloud Flow on submission. The configured Adaptive Form sends captured data, attachments, and Document Of Record to Power Automate Cloud Flow for processing. It helps you build custom data capture experience while harnessing the power of Microsoft&reg; Power Automate to build business logics around captured data and automate customer workflows. Here are a few examples of what you can do after integrating an Adaptive Form with Microsoft&reg; Power Automate: 

* Use Adaptive Forms data in a Power Automate business processes
* Use Power Automate to send captured data to more than 500 data sources or any publicly available API  
* Perform complex calculations on captured data
* Save Adaptive Forms data to storage systems at a predefined schedule

Adaptive Forms editor provides the **Invoke a Microsoft&reg; Power Automate flow** submit action to send adaptive forms data, attachments, and Document Of Record are sent to Power Automate Cloud Flow. To use the Submit action to send captured data to Microsoft&reg; Power Automate, [Connect your Forms as a Cloud Service instance with Microsoft&reg; Power Automate](forms-microsoft-power-automate-integration.md)  

After a successful configuration, use the [Invoke a Microsoft&reg; Power Automate flow](forms-microsoft-power-automate-integration.md#use-the-invoke-a-microsoft&reg;-power-automate-flow-submit-action-to-send-data-to-a-power-automate-flow-use-the-invoke-microsoft-power-automate-flow-submit-action) submit action to send data to a Power Automate Flow.  

## Use synchronous or asynchronous submission {#use-synchronous-or-asynchronous-submission}

A Submit Action can use synchronous or asynchronous submission.

**Synchronous submission**: Traditionally, web forms are configured to submit synchronously. In a synchronous submission, when users submit a form, they are redirected to an acknowledgment page, a thank you page, or if there is submission failure, an error page. You can select the **[!UICONTROL Use asynchronous submission]** option to redirect the users to a webpage or show a message on submission.  

![Configure Submit Action](assets/thank-you-setting.png)

**Asynchronous submission**: Modern web experiences like single page applications are gaining popularity where the web page remains static while client-server interaction happens in the background. You can now provide this experience with Adaptive Forms by [configuring asynchronous submission](asynchronous-submissions-adaptive-forms.md).

## Server-Side Revalidation in Adaptive Form {#server-side-revalidation-in-adaptive-form}

Typically, in any online data capture system, developers place someJavaScript validations on client side to enforce a few business rules. But in modern browsers, end users have way to bypass those validations and manually do submissions using various techniques, Such as Web Browser DevTools Console. Such techniques are also valid for Adaptive Forms. A forms developer can create various validation logics, but technically, end users can bypass those validation logics and submit invalid data to the server. Invalid data would break the business rules that a forms author has enforced.

The server-side revalidation feature provides the ability to also run the validations that an Adaptive Forms author has provided while designing an Adaptive Form on the server. It prevents any possible compromise of data submissions and business rules violations represented in terms of form validations.

### What to validate on Server? {#what-to-validate-on-server-br}

All out of the box (OOTB) field validations of an Adaptive Form that are rerun at the server are:

* Required
* Validation Picture Clause
* Validation Expression

### Enabling Server-side Validation {#enabling-server-side-validation-br}

Use the **[!UICONTROL Revalidate on server]** under Adaptive Form Container in the sidebar to enable or disable server-side validation for the current form.

![Enabling Server-Side Validation](assets/revalidate-on-server.png)

Enabling Server-Side Validation

If end-user bypass those validations and submit the forms, the server again performs the validation. If the validation fails at server end, then the submit transaction is stopped. The end user is presented with the original form again. The captured data and submitted data are presented to the user as an error.

>[!NOTE]
>
>Server-side validation validates the form model. You are recommended to create a separate client library for validations and not mix it with other things like HTML styling and DOM manipulation in the same client library.

### Supporting Custom functions in Validation Expressions {#supporting-custom-functions-in-validation-expressions-br}

At times, if there are **complex validation rules**, the exact validation script reside in custom functions and author calls these custom functions from field validation expression. To make this custom function library known and available while performing server-side validations, the form author can configure the name of AEM client library under the **[!UICONTROL Basic]** tab of Adaptive Form Container properties as shown below.

![Supporting Custom functions in Validation Expressions](assets/clientlib-cat.png)

Supporting Custom functions in Validation Expressions

Author can configure customJavaScript library per Adaptive Form. In the library, only keep the reusable functions, which have dependency on jquery and underscore.js third-party libraries.

## Error handling on Submit Action {#error-handling-on-submit-action}

As a part of AEM security and hardening guidelines, configure custom error pages such as 400.jsp, 404.jsp, and 500.jsp. These handlers are called, when on submitting a form 400, 404, or 500 errors appear. The handlers are also called when these error codes are triggered on the Publish node. You can also create JSP pages for other HTTP error codes.

When you prefill a form data model, or schema based Adaptive Form with XML or JSON data complaint to a schema that is data does not contain `<afData>`, `<afBoundData>`, and `</afUnboundData>` tags, then the data of unbounded fields of the Adaptive Form is lost. The schema can be an XML schema, JSON schema, or a Form Data Model. Unbounded fields are Adaptive Form fields without the `bindref` property.

<!-- For more information, see [Customizing Pages shown by the Error Handler](/help/sites-developing/customizing-errorhandler-pages.md). -->
