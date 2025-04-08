---
title: Which workflow steps are available for on AEM Forms Cloud Service to create a workflow or for business process automation (BPM)?
description: Forms-centric workflows allow you to rapidly build Adaptive Forms-based workflows. You can use Adobe Sign to e-sign documents, create forms-based business processes, retrieve and send data to multiple data sources, and send email notifications
exl-id: e1403ba6-8158-4961-98a4-2954b2e32e0d
google-site-verification: A1dSvxshSAiaZvk0yHu7-S3hJBb1THj0CZ2Uh8N_ck4
keywords: Use AEM workflows, using assign task steps, convert to PDF/A step, Generate document of recored step, use workflows, Sign document step, Genertae printed output step, Generate non interactive PDF output
feature: Adaptive Forms, Workflow
role: Admin, User
---

# Use Forms-centric AEM Workflows - Step Reference to automate business processes {#forms-centric-workflow-on-osgi-step-reference}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/workflows/aem-forms-workflow-step-reference.html)                  |
| AEM as a Cloud Service     | This article            |

You use workflow models . A model helps you define and execute a series of steps. You can also define model properties, such as whether the workflow is transient or uses multiple resources. You can [include various AEM Workflow steps in a model to achieve the business logic](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html?lang=en#extending-aem). 

## Forms-centric steps {#forms-workflow-steps}

Forms-centric workflow steps perform AEM Forms-specific operations in an AEM Workflow. These steps allow you to rapidly build an Adaptive Forms based Forms-centric workflow on OSGi. These workflows can be used for developing basic review- and approval-workflows, internal and across- the-firewall business processes. You can also use Forms Workflow steps to:

* Create business processes, post-submission workflows, and backend workflows to manage enrollment processes.

* Create and assign tasks to a user or group.

* Use [!DNL Adobe Sign] in an AEM Workflow to send a document for  signing.

* Generate a Document of Record on-demand or on form submission.

* Connect a workflow model with various data sources to easily save and retrieve data.

* Use the email step to send notification emails and other attachments on completion of an action and at the start or completion of a  workflow.

>[!NOTE]
>
>If the workflow model is marked for an external storage, then for all the Forms Workflow steps, you can select only the variable option to store or retrieve data files and attachments.
 
## Assign task step {#assign-task-step}

The assign task step creates a work item and assigns it to a user or group. Along with assigning the task, the component also specifies the Adaptive Form or non-interactive PDF for the task. The Adaptive Form is required to accept input from users and non-interactive PDF or a read-only Adaptive Form is used for review only workflows.

You can also use the component to control the behavior of the task. For example, creating an automatic Document of Record, assigning the task to a specific user or group, specifying the path of the submitted data, specifying the path of data to be pre-populated, and specifying default actions. The Assign Task step has the following properties:

* **[!UICONTROL Title]**: Title of the task. The title is displayed in the AEM Inbox.
* **[!UICONTROL Description]**: Explanation of the operations being performed in the task. This information is useful for other process developers when you are working in a shared development environment.  

* **[!UICONTROL Thumbnail Path]**: Path of the task thumbnail. If no path is specified, for an Adaptive Form a default thumbnail is displayed and for Document of Record, a default icon is displayed.
* **[!UICONTROL Workflow Stage]**: A workflow can have multiple stages. These stages are displayed in the AEM Inbox. You can define these stages in the properties of the model (Sidekick &gt; Page &gt; Page Properties &gt; Stages).
* **[!UICONTROL Priority]**: Selected priority is displayed in the AEM Inbox. The available options are High, Medium, and Low. The default value is Medium.
* **[!UICONTROL Due Date]**: Specify the number of days or hours after which the task is marked overdue. If you select **[!UICONTROL Off]**, then the task is never marked overdue. You can also specify a time-out handler to perform specific tasks after the task is overdue.

* **[!UICONTROL Days]**: The number of days before which the task is to be completed. The number of days are counted after the task is assigned to a user. If a task is not complete and crosses the number of days specified in the Days field, then if it is selected, a timeout handler is triggered after the due date.
* **[!UICONTROL Hours]**: The number of hours before which the task is to be completed. The number of hours are counted after the task is assigned to a user. If a task is not complete and crosses the number of hours specifies in the Hours field, then if it is selected, a timeout handler is triggered after the due hours.
* **[!UICONTROL Time-out after Due Date]**: Select this option to enable the Timeout Handler selection field.
* **[!UICONTROL Timeout Handler]**: Select the script to be executed when the assign task step crosses the due date. Scripts placed in the CRX-repository at [apps]/fd/dashboard/scripts/timeoutHandler are available for selection. The specified path does not exist in crx-repository. An administrator creates the path before using it.
* **[!UICONTROL Highlight the action and comment from the last task in Task Details]**: Select this option to display the last action that was taken and comment received on the task details section of a task.
* **[!UICONTROL Type]**: Choose the type of document to be filled when the workflow is started. You can choose an Adaptive Form, read-only Adaptive Form, a non-interactive PDF document. 

<!-- , Interactive Communication Agent UI, or Interactive Communication Web Channel Document. -->


* **[!UICONTROL Use Adaptive Form]**: Specify the method to locate the input Adaptive Form. This option is available if you select Adaptive Form or Read-only Adaptive Form from the Type drop-down list. You can use the Adaptive Form submitted to the workflow, available at an absolute path, or available at a path in a variable. You can use a variable of type String to specify the path.  
  You can associate multiple Adaptive Forms with a workflow. As a result, you can specify an Adaptive Form on the runtime using the available input methods.

<!-- 

* **[!UICONTROL Use Interactive Communication]**: Specify the method to locate the input interactive communication. You can use the interactive communication submitted to the workflow, available at an absolute path, or available at a path in a variable. You can use a variable of type String to specify the path. This option is available if you select Interactive Communication Agent UI or Interactive Communication Web Channel Document from the Type drop-down list. 

> [!NOTE]
>
>You must have cm-agent-users and workflow-users group assignments to access Interactive Communications Agent UI in AEM inbox.  

--> 

* **[!UICONTROL Adaptive Form Path]**: Specify the path of the Adaptive Form. You can use the Adaptive Form that is submitted to the workflow, available at an absolute path, or retrieve the Adaptive Form from a path stored in a variable of string data type.
* **[!UICONTROL Select input PDF using]**: Specify the path of a non-interactive PDF document. The field is available when you choose a non-interactive PDF document in the Type field. You can select the input PDF using the path that is relative to the payload, saved at an absolute path, or using a variable of Document data type. For example, [Payload_Directory]/Workflow/PDF/credit-card.pdf. The path does not exist in crx-repository. An administrator creates the path before using it. You require a Document of Record option enabled or form template based Adaptive Forms for using the PDF Path option.
* **[!UICONTROL For completed task, render the Adaptive Form as]**: When a task is marked complete, you can render the Adaptive Form as a read-only Adaptive Form or a PDF document. You require a Document of Record option enabled or form template based Adaptive Forms for rendering the Adaptive Form as Document of Record.
* **[!UICONTROL Pre-populated]**: The following fields listed below serve as inputs to the task:

    * **[!UICONTROL Select input data file using]**: Path of input data file (.json, .xml, .doc, or form data model (FDM)). You can retrieve the input data file using a path that is relative to the payload or retrieve the file stored in a variable of Document, XML, or JSON data type. For example, the file contains the data submitted for the form through an AEM Inbox application. An example path is [Payload_Directory]/workflow/data.
    * **[!UICONTROL Select input attachments using]**: Attachments available at the location are attached to the form associated with the task. The path can be relative to the payload or retrieve the attachment stored in a variable of a document. An example path is [Payload_Directory]/attachments/. You can specify attachments placed relative to the payload or use a document type (Array list > Document) variable to specify an input attachment for the Adaptive Form.
    
    <!-- 
    
    * **[!UICONTROL Choose input JSON]**: Select an input JSON file using a path that is relative to payload or stored in a variable of Document, JSON, or Form Data Model (FDM) data type. This option is available if you select Interactive Communication Agent UI or Interactive Communication Web Channel Document from the Type drop-down list.

    * **[!UICONTROL Choose a custom prefill service]**: Select the prefill service to retrieve the data and prefill the Interactive Communication Web channel document or the Agent UI.  
    
    * **[!UICONTROL Use the prefill service of the interactive communication selected above]**: Use this option to use the prefill service of the Interactive Communication defined in the Use Interactive Communication drop-down list. 
    
    -->

    * **[!UICONTROL Request Attribute Mapping]**: Use the Request Attribute Mapping section to define the [name and value of the request attribute](work-with-form-data-model.md#bindargument). Retrieve the details from the data source based on the attribute name and value specified in the request. You can define a request attribute value using a literal value or a variable of String data type.  
    
     <!--  
     
     The prefill service and request attribute mapping options are available only if you select Interactive Communication Agent UI or Interactive Communication Web Channel Document from the Type drop-down list. 
     
     -->

* **[!UICONTROL Submitted information]**: The following fields listed below serve as output locations to the task:

    * **[!UICONTROL Save output data file using]**: Save the data file (.json, .xml, .doc, or form data model (FDM)). The data file contains information submitted through the associated form. You can save the output data file using a path that is relative to the payload or store it in a variable of Document, XML, or JSON data type. For example, [Payload_Directory]/Workflow/data, where data is a file.
    * **[!UICONTROL Save attachments using]**: Save the form attachments provide in a task. You can save the attachments using a path that is relative to the payload or store it in a variable of array list of Document data type.
    * **[!UICONTROL Save Document of Record using]**: Path to save a Document of Record file. For example, [Payload_Directory]/DocumentofRecord/credit-card.pdf. You can save the Document of Record using a path that is relative to the payload or store it in a variable of Document data type. If you select the **[!UICONTROL Relative to Payload]** option, The Document of Record is not generated if the path field is left empty. This option is available only if you select Adaptive Form from the Type drop-down list.
    
    <!-- 
    
    * **[!UICONTROL Save Web Channel data using]**: Save the Web Channel data file using a path that is relative to the payload or store it in a variable of Document, JSON, or Form Data Model (FDM) data type. This option is available only if you select Interactive Communication Agent UI from the Type drop-down list. c
    * **[!UICONTROL Save PDF document using]**: Save the PDF document using a path that is relative to the payload or store it in a variable of Document data type. This option is available only if you select Interactive Communication Agent UI from the Type drop-down list.
    <!-- * **[!UICONTROL Save layout template using]**: Save the layout template using a path that is relative to the payload or store it in a variable of Document data type. The [layout template](layout-design-details.md) refers to an XDP file that you create using Forms Designer. This option is available only if you select Interactive Communication Agent UI from the Type drop-down list. 
    
    -->

* **[!UICONTROL Assignee]** &gt; **[!UICONTROL Assign options]**: Specify the method to assign the task to a user. You can dynamically assign the task to a user or a group using the Participant Chooser script or assign the task to a specific AEM user or group.
* **[!UICONTROL Participant Chooser]**: The option is available when the **[!UICONTROL Dynamically to a user or group]** option is selected in the Assign options field. You can use an ECMAScript or a service to dynamically select a user or a group. For more information, see [Dynamically assign a workflow to the users](https://helpx.adobe.com/experience-manager/kb/HowToAssignAWorkflowDynamicallyToParticipants.html) and [Creating a custom Adobe Experience Manager Dynamic Participant step](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/overview.html?lang=en&CID=RedirectAEMCommunityKautuk).

* **[!UICONTROL Participants]**: The field is available when the **[!UICONTROL com.adobe.granite.workflow.core.process.RandomParticipantChooser]** option is selected in the **[!UICONTROL Participant Chooser]** field. The field lets you select users or groups for the RandomParticipantChooser option.

* **[!UICONTROL Assignee]**: The field is available when the **[!UICONTROL com.adobe.fd.workspace.step.service.VariableParticipantChooser]** is selected in the **[!UICONTROL Participant Chooser]** field. The field lets you select a variable of String data type to define the assignee.

* **[!UICONTROL Arguments]**: The field is available when a script other than the RandomParticipantChoose script is selected in the Participant Chooser field. The field lets you provide a list of a comma-separated argument for the script selected in the Participant Chooser field.  

* **[!UICONTROL User or Group]**: The task is assigned to a selected user or group. The option is available when the **[!UICONTROL To a specific user or group option]** is selected in the **[!UICONTROL Assign options]** field. The field lists all the users and groups of the [!DNL workflow-users] group.  
  The **[!UICONTROL User or Group]** drop-down menu lists the users and groups that the logged-in user has access to. The username display depends on if you have access permissions on the **[!UICONTROL users]** node in the crx-repository for that particular user. 

* **[!UICONTROL Send Notification Email]**: Select this option to send email notifications to the assignee. These notifications are sent when a task is assigned to a user or a group. You can use the **[!UICONTROL Recipient Email Address]** option to specify the mechanism to retrieve the email address.

* **[!UICONTROL Recipient Email Address]**: You can store an email address in a variable, use a literal to specify a permanent email address, or use the default email address of the assignee specified in the profile of the assignee. You can use the literal or a variable to specify the email address of a group. The variable option is helpful in dynamically retrieving and using an email address. The **[!UICONTROL Use default email address of the assignee]** option is only for a single assignee. In this case, the email address stored in the assignees user profile is used.

* **[!UICONTROL HTML Email Template]**: Select the email template for the notification email. To edit a template, modify the file located at /libs/fd/dashboard/templates/email/htmlEmailTemplate.txt in crx-repository.
* **[!UICONTROL Allow Delegation To]**: AEM Inbox provides an option to the logged in user to delegate the assigned workflow to another user. You are allowed to delegate within the same group or to the workflow user of another group. If the task is assigned to a single user and the **[!UICONTROL allow delegation to members of the assignee group]** option is selected, then it is not possible to delegate the task to another user or group.
* **[!UICONTROL Share Settings]**: AEM Inbox provides options to share a single or all the tasks in the inbox with another user:
    * When the **[!UICONTROL Allow assignee to share explicitly in inbox]** option is selected, the user can select the task in AEM Inbox and share it with another AEM user. 
    * When the **[!UICONTROL Allow assignee to share via inbox sharing]** option is selected and users share their Inbox items or allows other users to access their Inbox items, only tasks with the previously mentioned option enabled are shared with other users.
    * When the **[!UICONTROL Allow assignee to delegate using 'Out of Office' settings]** is selected. The assignee can enable the option to delegate the task to other users along with other Out of Office options. Any new tasks assigned to the out-of-office user are automatically delegated (assigned) to the users mentioned in out-of-office settings.
    
     It allows other users to pick assignees tasks while is out of the office and unable to work on assigned tasks. 

* **[!UICONTROL Actions]** &gt; **[!UICONTROL Default Actions]**: Out of the box, Submit, Save, and Reset actions are available. All the default actions are enabled, by default. 
* **[!UICONTROL Route Variable]**: Name of the route variable. The route variable captures custom actions that a user selects in the AEM Inbox.
* **[!UICONTROL Routes]**: A task can branch to different routes. When selected in AEM Inbox, the route returns a value and the workflow branches based on the selected route. You can either store routes in a variable of array of String data types or select **[!UICONTROL Literal]** to add routes manually.

* **[!UICONTROL Route Title]**: Specify the title for the route. It is displayed in the AEM Inbox.
* **[!UICONTROL Coral Icon]**: Specify an HTML attribute of a coral icon. Adobe CorelUI library provides a vast set of touch-first icons. You can choose and use an icon for the route. It is displayed along with the title in the AEM Inbox. If you store the routes in a variable, the routes use a default 'Tags' coral icon.
* **[!UICONTROL Allow assignee to add comment]**: Select this option to enable comments for the task. An assignee can add the comments from within the AEM Inbox at the time of task submission.
* **[!UICONTROL Save comment in variable]**: Save the comment in a variable of String data type. This option displays only if you select the **[!UICONTROL Allow assignee to add comment]** checkbox.

* **[!UICONTROL Allow assignee to add attachments to the task]**: Select this option to enable attachments for the task. An assignee can add the attachments from within the AEM Inbox at the time of task submission. You can also limit the maximum size **[!UICONTROL (Maximum File Size)]** of an attachment. The default size is 2 MB. 

* **[!UICONTROL Save output task attachments using]**: Specify the location of the attachment folder. You can save output task attachments using a path relative to the payload or in a variable of an array of document data types. This option displays only if you select the **[!UICONTROL Allow assignee to add attachments to the task]** checkbox and select **[!UICONTROL Adaptive Form]**, **[!UICONTROL Read-only Adaptive Form]**, or **[!UICONTROL Non-interactive PDF document]** from the **[!UICONTROL Type]** drop-down list in the **[!UICONTROL Form/Document]** tab.

* **[!UICONTROL Use custom metadata]**: Select this option to enable the custom metadata field. Custom metadata is used in email templates.
* **[!UICONTROL Custom Metadata]**: Select a custom metadata for the email templates. The custom metadata is available in crx-repository at apps/fd/dashboard/scripts/metadataScripts. The specified path does not exist in crx-repository. An administrator creates the path before using it. You can also use a service for the custom metadata. You can also extend the `WorkitemUserMetadataService` interface to provide custom metadata.
* **[!UICONTROL Show Data from Previous Steps]**: Select this option to enable assignees to view previous assignees, action already taken on the task, comments added to the task, and Document of Record of the completed task, if available. 
* **[!UICONTROL Show Data from Subsequent Steps]**: Select this option to enable the current assignee to view the action taken and comments added to task by subsequent assignees. It also allows the current assignee to view a Document of Record of the completed task, if available.
* **[!UICONTROL Visibility of data type]**: By default, an assignee can view a Document of Record, assignees, action taken, and comments that previous and subsequent assignees have added. Use the visibility of data type option to limit the type of data visible to the assignees.

>[!NOTE]
>
>The options to save the Assign Task step as draft and to retrieve the history of the Assign Task step are disabled when you configure an AEM workflow model for external data storage. Also, in Inbox, the option to save is disabled. 

## Convert to PDF/A step {#convert-pdfa}

PDF/A is an archival format for long-term preservation of the document's content, by embedding the fonts and uncompressing the file. As a result, a PDF/A document is typically larger than a standard PDF document. You can use the ***Convert to PDF/A*** step in an AEM Workflow to convert your PDF documents to PDF/A format. 

The convert to PDF/A step has the following properties:

**[!UICONTROL Input Document]**: The input document can be relative to the payload, have an absolute path, can be provided as a payload or stored in a variable of Document data type.

**[!UICONTROL Conversion Options]**: Using this property, the settings for converting PDF documents to PDF/A documents are specified. Various options available under this tab are:
* **[!UICONTROL Compliance]**: Specifies the standard to which the output PDF/A document must comply. It supports different PDF standards such as PDF/A-1b, PDF/A-2b, or PDF/A-3b.
* **[!UICONTROL Result Level]**: Specifies the result level as PassFail, Summary, or Detailed, for the conversion output.
* **[!UICONTROL Color Space]**: Specifies the predefined color space as S_RGB, COATED_FOGRA27, JAPAN_COLOR_COATED or SWOP, that can be used for output PDF/A files. 
* **[!UICONTROL Optional Content]**: Allow specific graphic objects and/or annotations to be visible in output PDF/A document, only when a specified set of criteria is met.

**[!UICONTROL Output Documents]**: Specifies the location to save the output file. The output file can be saved at a location relative to the payload, overwrites the payload, if the payload is a file, or in a variable of Document data type. 


## Send Email Step {#send-email-step}

Use the email step to send an email, for example, an email with a Document of Record, link of an Adaptive Form <!-- , link of an interactive communication-->, or with an attached PDF document. Send Email step supports [HTML email](https://en.wikipedia.org/wiki/HTML_email). HTML emails are responsive and adapt to the recipients' email client and screen size. You can use an HTML email template to define the appearance, color-scheme, and behavior of the email.

The email step uses Day CQ Mail Service to send emails. Before using the email step, ensure that the email service is configured. Email support only HTTP and HTTPs protocols, by default. [Contact the support team](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines.html?lang=en#sending-email) to enable ports to send emails and  enable SMTP protocol for your environment. The restriction helps improve the security of the platform.

The email step has the following properties:

**[!UICONTROL Title]**: Title of the step helps identify the step in the workflow editor.

**[!UICONTROL Description]**: Explanation is useful for other process developers when you are working in a shared development environment.

**[!UICONTROL Email Subject]**: Subject can be retrieved from a workflow metadata, specified manually, or retrieved from the value stored in a variable. Select from the following options:

* **[!UICONTROL Literal]** Manually specify a subject.
* **[!UICONTROL Retrieve from Workflow metadata]** - Retrieve the subject from a metadata property.
* **[!UICONTROL Variable]** - Retrieve the subject from the value stored in a variable of string data type.

**[!UICONTROL HTML Email Template]**: HTML template for the email. You can specify variables in an email template. The Email Step extracts and displays all the variables included in a template for inputs.

**[!UICONTROL Email Template Metadata]**: Value of the email template variables can be a user-specified value, the path of an asset on the author or the publish server, image, or a workflow metadata property.

* **[!UICONTROL Literal]**: Use the option when you know the exact value to specify. For example, [example@example.com](mailto:example@example.com).

* **[!UICONTROL Workflow Metadata]**: Use the option when the value to use is saved in a workflow metadata property. After selecting the option, enter the metadata property name in the empty text box below the Workflow Metadata option. For example, emailAddress.

<!-- 

* **[!UICONTROL Asset URL]**: Use the option to embed a web link of an interactive communication to the email. After selecting the option, browse and choose the interactive communication to embed. The asset can reside on the author or the publish server. 

-->

* **[!UICONTROL Image]**: Use the option to embed an image to the email. After selecting the option, browse and choose the image. The image option is available only for the image tags (&lt;img src="&#42;"/&gt;) available in the email template.

**[!UICONTROL Sender's / Recipient's Email Address]**: Select the **[!UICONTROL Literal]** option to manually specify an email address or select the **[!UICONTROL Retrieve from Workflow metadata]** option to retrieve the email address from a metadata property. You can also specify a list of metadata property arrays for the **[!UICONTROL Retrieve from Workflow metadata]** option. Select the **[!UICONTROL Variable]** option to retrieve the e-mail address from the value stored in a variable of string data type.

* **[!UICONTROL File Attachment]**: The asset available at the specified location is attached to the email. The path of the asset can be relative to the payload or absolute path. An example path is [Payload_Directory]/attachments/.

Select the **[!UICONTROL Variable]** option to retrieve the file attachment stored in a variable of Document, XML, or JSON data type.

**[!UICONTROL File Name]**: Name of the email attachment file. The Email Step changes the original file name of the attachment to the specified file name. The name can be specified manually or retrieved from a workflow metadata property or a variable. Use the **[!UICONTROL Literal]** option when you know the exact value to specify. Use the **[!UICONTROL Variable]** option to retrieve the file name from the value stored in a variable of string data type. Use the **[!UICONTROL Retrieve from a Workflow Metadata]** option when the value to use is saved in a workflow metadata property.

## Generate Document of Record step {#generate-document-of-record-step}

When a form is filled or submitted, you can keep a record of the form, in print or in document format. This record is referred as a Document of Record (DoR). You can use the Generate Document of Record step to create a read-only or interactive PDF version of an Adaptive Form. The PDF version contains information filled-in to the form along with the layout of the Adaptive Form.

The Document of Record step has the following properties:

**[!UICONTROL Use Adaptive Form]**: Specify the method to locate the input Adaptive Form. You can use the Adaptive Form submitted to the workflow, available at an absolute path, or available at a path in a variable. You can use a variable of String data type to specify the path in the **[!UICONTROL Select variable to resolve]** field.  
You can associate multiple Adaptive Forms with a workflow. As a result, you can specify an Adaptive Form on the runtime using the available input methods.

**[!UICONTROL Adaptive Form Path]**: Specify the path of the Adaptive Form. The field is available when you select the **[!UICONTROL Available at an absolute path]** option from the **[!UICONTROL Use Adaptive Form]** field.

**[!UICONTROL Select Input data using]**: Path of the input data for the Adaptive Form. You can keep the data at a location relative to the payload, specify an absolute path of the data, or retrieve data stored in a variable of Document, JSON, or XML data type. The input data is merged with the Adaptive Form to create a Document of Record.

**[!UICONTROL Select Input attachment path using]**: Path of the attachments. These attachments are included in the Document of Record. You can keep the attachments at a location relative to the payload, specify an absolute path of the attachments, or retrieve attachments stored in a variable of array of Document data type.

If you specify the path of a folder, for example, attachments, all the files directly available in the folder are attached to Document of Record. If any files are available in the folders directly available in the specified attachment path, the files are included in Document of Record as attachments. If there are any folders in directly available folders, those folders are skipped.

**[!UICONTROL Save Generated Document of Record using below options]**: Specify the location to keep a Document of Record file. You can choose to overwrite the payload folder, place the Document of Record at a location within the payload directory, or store the Document of Record in a variable of Document data type.

**[!UICONTROL Locale]**: Specify the language of the Document of Record. Select **[!UICONTROL Literal]** to select the locale from a drop-down list or select **[!UICONTROL Variable]** to retrieve the locale from the value stored in a variable of string data type. Define the locale code while storing the value for the locale in a variable. For example, specify **en_US** for English and **fr_FR** for French.

## Invoke DDX step {#invokeddx}

Document Description XML (DDX) is a declarative markup language whose elements represent building blocks of documents. These building blocks include PDF and XDP documents, and other elements such as comments, bookmarks, and styled text. DDX defines a set of operations, which can be applied on one or more input documents to generate one or more output documents. A single DDX can be used with a range of source documents. You can use the ***Invoke DDX step*** in an AEM Workflow to perform various operations, like Assembling Disassembling documents, Creating, and modifying Acrobat and XFA Forms, and others described in the [DDX Reference documentation](https://helpx.adobe.com/content/dam/help/en/experience-manager/forms-cloud-service/ddxRef.pdf).                    

Invoke DDX step has the following properties: 

**[!UICONTROL Input Documents]**: Used to set properties of an input document. Various options available under this tab are:
* **[!UICONTROL Specify DDX Using]**: Specifies the input document relative to the payload, have an absolute path, can be provided as payload, or stored in a variable of Document data type.
* **[!UICONTROL Create Map from Payload]**: Add all the documents under the payload folder to Input Document's Map for the invoke API in Assembler. The node name for each document is used as a key in the map.
* **[!UICONTROL Input Document's Map]**: Option is used to add multiple entries using the **[!UICONTROL ADD]** button. Each entry represents the document's key in the map and the document's source.

**[!UICONTROL Environment Options]**: This option is used to set processing settings for invoke API. Various options available under this tab are:
* **[!UICONTROL Validate Only]**: Checks the validity of the input DDX document.
* **[!UICONTROL Fail on Error]**: Boolean value to indicate whether the invoke API service fails, if there is an error or not. By default, its value is set to False.
* **[!UICONTROL First Bates Number]**: Specifies the number, which is self-incrementing. This self-incrementing number is displayed on each consecutive page automatically.  
* **[!UICONTROL Default Style]**: Sets the default style for the output file.

>[!NOTE]
>
>Environment options are kept in sync with HTTP APIs.

**[!UICONTROL Output Documents]**: Specifies the location to save the output file. Various options available under this tab are:
* **[!UICONTROL Save Output in Payload]**: Saves output documents under the payload folder, or overwrites the payload, in case, the payload is a file.
* **[!UICONTROL Output Document's Map]**: Specifies the location to save each document file explicitly, by adding one entry per document. Each entry represents the document and the location, where to save it. If there are multiple output documents, this option is used.   

## Invoke Form Data Model (FDM) Service step {#invoke-form-data-model-service-step}

You can use [[!DNL AEM Forms] Data Integration](data-integration.md) to configure and connect to disparate data sources. These data sources can be a web service, REST service, OData service, and CRM solution. [!DNL AEM Forms] Data Integration lets you create a Form Data Model (FDM) encompassing various services to perform data retrieval, addition, updating operations on the configured database. You can use the **[!UICONTROL Invoke Data Model Service step]** to select a Form Data Model (FDM) and use the services of the FDM to retrieve, update, or add data to disparate data sources.

To explain inputs for fields of the step, the following database table and JSON file are used as an example :

**[!UICONTROL Sample CustomerDetails table]**

<table>
 <tbody> 
  <tr> 
   <td>Property</td> 
   <td>Value<br /> </td> 
  </tr> 
  <tr> 
   <td>FirstName<br /> </td> 
   <td>Sarah<br /> </td> 
  </tr> 
  <tr> 
   <td>LastName</td> 
   <td>Rose</td> 
  </tr> 
  <tr> 
   <td>Customer ID</td> 
   <td>1</td> 
  </tr> 
  <tr> 
   <td>Email Address<br /> </td> 
   <td>srose@we.info</td> 
  </tr> 
 </tbody> 
</table>

**[!UICONTROL Sample JSON file]**

```json
  { 
    customer: { 
     firstName: "Sarah", 
     lastName:"Rose", 
     customerId: "1", 
     emailAddress:"srose@we.info" 
   }, 
    insurance: {
     customerId: "1", 
    policyType: "Premium,
    policyNumber: "Premium-521499",
    customerDetails: { 
     firstName: "Sarah",
     lastName: "Rose",
     customerId: "1",
     emailAddress: "srose@we.info" 
    }
   }
  }

```

The Invoke Form Data Model (FDM) Service step has the below listed fields to facilitate Form Data Model (FDM) operations:

* **[!UICONTROL Title]**: Title of the step. It helps identify the steps in the workflow editor.
* **[!UICONTROL Description]**: Explanation useful for other process developers when you are working in a shared development environment.  

* **[!UICONTROL Form Data Model Path]**: Browse and select a Form Data Model (FDM) present on the server.  

* **[!UICONTROL Errors and Validations]**: The option lets you capture error messages and specify validation options for data retrieved and sent to data sources. With these changes, you can ensure data passed to the Invoke Form Data Model (FDM) Service step adheres to the data constraints defined by the data source. For more details, see [Automated validation of input data](work-with-form-data-model.md#automated-validation-of-input-data)

* **[!UICONTROL Validation level]**: There are three categories of validations: Basic, Full, and OFF:

  * Full: All the constraints are validated. 
  * Basic: Only required and nullable constraints
  * OFF: No validation takes place. 

* **[!UICONTROL Terminate Workflow on Failure]**: When a constraint fails to validate, the workflow is stopped. 

* **[!UICONTROL Store Error Code in Variable]**: You can store an error code in a [String type variable](variable-in-aem-workflows.md).

* **[!UICONTROL Store Error Message in Variable]**: You can store an error message in a [String type variable](variable-in-aem-workflows.md).

* **[!UICONTROL Store Error Details in Variable]**: You can store an error detail in a [JSON type variable](variable-in-aem-workflows.md).

* **[!UICONTROL Service]**: List of the services that the selected Form Data Model (FDM) provides.
* **[!UICONTROL Input for services]** &gt; **[!UICONTROL Provide input data using literal, variable, or workflow metadata, and a JSON file]**: A service can have multiple arguments. Select the option to obtain the value of the service arguments from a workflow metadata property, a JSON object, a variable, or directly enter the value in the provided text box:

  * **[!UICONTROL Literal]**: Use the option when you know the exact value to specify. For example, srose@we.info.
  * **[!UICONTROL Variable]**: Use the option to retrieve the value stored in a variable.
  * **[!UICONTROL Retrieve from Workflow Metadata]**: Use the option when the value to use is saved in a workflow metadata property. For example, emailAddress.

  * **[!UICONTROL Relative to Payload]**: Use the option to retrieve the file attachment saved at a path relative to the payload. Select the option and specify either the folder name which includes the file attachment or specify the file attachment name in the text box.
  
    For example, if the Relative to Payload folder in the CRX repository includes a file attachment at the `attachment\attachment-folder` location, specify `attachment\attachment-folder` in the text box after selecting the **[!UICONTROL Relative to Payload]** option.

  * **[!UICONTROL JSON Dot Notation]**: Use the option when the value to use is in a JSON file. For example, insurance.customerDetails.emailAddress. The JSON Dot Notation option is available only if Map input fields from the input JSON option are selected.
  * **[!UICONTROL Map input fields from input JSON]**: Specify the path of a JSON file to obtain the input value of some service arguments from the JSON file. The path of the JSON file can be relative to the payload, an absolute path, or you can select an input JSON document using a variable of JSON or Form Data Model (FDM) type.

* **[!UICONTROL Input for services]** &gt; **[!UICONTROL Provide input data using variable or a JSON file]**: Select the option to obtain values for all the arguments from a JSON file saved at an absolute path, at a path relative to the payload, or in a variable.
* **[!UICONTROL Select Input JSON document using]**: The JSON file containing values for all the service arguments. The path of the JSON file can be **[!UICONTROL relative to the payload]** or an **[!UICONTROL absolute path]**. You can also retrieve the input JSON document using a variable of JSON or Form Data Model (FDM) data type.

* **[!UICONTROL JSON Dot Notation]**: Leave the field blank to use all the objects of the specified JSON file as input for service arguments. To read a specific JSON object from the specified JSON file as input for service arguments, specify dot notation for the JSON object, for example, If you have a JSON similar to the one listed at the start of the section, specify insurance.customerDetails to provide all the details of a customer as input to the service.
* **[!UICONTROL Output of service]** &gt; **[!UICONTROL Map and write output values to variable or metadata]**: Select the option to save the output values as properties of the workflow instance metadata node in crx-repository. Specify the name of the metadata property and select the corresponding service output attribute to be mapped with the metadata property, for example, map the phone_number returned by output service with the phone_number property of workflow metadata. Similarly, you can store the output in a variable of Long data type. When you select a property for the **[!UICONTROL Service output attribute to be mapped]** option, only variables capable of storing data of the selected property are populated for the **[!UICONTROL Save the output to]** option.

* **[!UICONTROL Output of service]** &gt; **[!UICONTROL Save output to variable or a JSON file]**: Select the option to save the output values in a JSON file at an absolute path, at a path relative to the payload, or in a variable . 
* **[!UICONTROL Save Output JSON document using below options]**: Save the output JSON file. The path of the output JSON file can be relative to the payload or an absolute path. You can also save the output JSON file using a variable of JSON or Form Data Model (FDM) data type.



## Sign Document step {#sign-document-step}

The Sign Document step enables you to use [!DNL Adobe Sign] to sign documents. When you use the [!DNL Adobe Sign] Workflow step to Sign an Adaptive Form, the form can be passed across recipients one after another or can be sent to all the recipients simultaneously, depending on the configuration of the workflow step. [!DNL Adobe Sign] enabled Adaptive Forms are submitted to Experience Manager Forms Server, only after all the recipients complete the signing process.

By default, the [!DNL Adobe Sign] Scheduler service checks (polls) recipient response after every 24 hours. You can [change the default interval for your environment](adobe-sign-integration-adaptive-forms.md#for-aem-workflows-only-configure-dnl-adobe-acrobat-sign-scheduler-to-sync-the-signing-status-configure-adobe-sign-scheduler-to-sync-the-signing-status). 

 The Sign Document step has the following properties:

* **[!UICONTROL Agreement Name]**: Specify the title of the agreement. The agreement name becomes part of the subject and body text of the email sent to the signers. You can either store the name in a variable of String data type or select **[!UICONTROL Literal]** to add the name manually.

* **[!UICONTROL Locale]**: Specify the language for the email and verification options. You can either store the locale in a variable of String data type or select **[!UICONTROL Literal]** to choose the locale from the list of available options. You must define the locale code while storing the value for the locale in a variable. For example, specify **[!UICONTROL en_US]** for English and **[!UICONTROL fr_FR]** for French.

* **[!UICONTROL Adobe Sign Cloud Configuration]**: Choose an [!DNL Adobe Sign] Cloud Configuration. If you have not configured [!DNL Adobe Sign] for [!DNL AEM Forms], see [Integrate Adobe Sign with [!DNL AEM Forms]](adobe-sign-integration-adaptive-forms.md).

* **[!UICONTROL Select Document to be signed using]**: You can choose a document from a location relative to the payload, use the payload as the document, specify an absolute path of the document, or retrieve the document stored in a variable of Document data type.
* **[!UICONTROL Days Until Deadline]**: A document is marked due (passed deadline) after there is no activity on the task for the number of days specifies in the **[!UICONTROL Days Until Deadline]** field. The number of days are counted after the documentation is assigned to a user for signing.
* **[!UICONTROL Reminder Email Frequency]**: You can send a reminder email at a daily or weekly interval. The week is counted from the day the documentation is assigned to a user for signing.
* **[!UICONTROL Signature Process]**: You can choose to sign a document in a sequential or a parallel order. In sequential order, one signer receives the document at a time for signing. After the first signer completes signing the document, the document is sent to the second signer, and so on. In parallel order, multiple signers can sign a document at a time.
* **[!UICONTROL Redirection URL]**: Specify a redirection URL. After the document is signed, you can redirect the assignee to a URL. Usually, this URL contains a thank you message or further instructions.
* **[!UICONTROL Workflow Stage]**: A workflow can have multiple stages. These stages are displayed in the AEM Inbox. You can define these stages in the properties of the model ( **[!UICONTROL Sidekick]** &gt; **[!UICONTROL Page]** &gt; **[!UICONTROL Page Properties]** &gt; **[!UICONTROL Stages]**).
* **[!UICONTROL Select Recipients]**: Specify the method to choose recipients for the document. You can dynamically assign the workflow to a user or a group or manually add details of a recipient. When you select Manually in the drop-down list, you add recipient details such as Email, Role, and Authentication method.

    >[!NOTE]
    >
    >* In the Role section, you can specify the recipient role as Signer, Approver, Acceptor, Certified Recipient, Form Filler, and Delegator.
    >* If you select Delegator in the Role option, the Delegator can assign the sign task to another recipient.
    >* If you have configured an authentication method for [!DNL Adobe Sign], based on your configuration you select an authentication method such as Phone based authentication, Social Identity based authentication, Knowledge based authentication, Government Identity based authentication.
  
* **[!UICONTROL Script or service to select recipients]**: The option is available only if you select the Dynamically option in the Select Recipients field. You can specify an ECMAScript or a service to choose signers and verification options for a document.
* **[!UICONTROL Recipient Details]**:  The option is available only if the Manually option is selected in the Select Recipients field. Specify an email address and choose an optional verification mechanism. Before selecting a 2-step verification mechanism, ensure that the corresponding verification option is enabled for the configured [!DNL Adobe Sign] account. You can use a variable of String data type to define values for Email, Country Code, and Phone Number fields. The Country Code and Phone Number fields are display only if you select Phone Verification from the 2-step verification drop-down list.
* **[!UICONTROL Signed Document]**: You can save the status of the Signed Document to Variable. To add an electronic signature audit trail for greater security and legality to your Signed Document, you can Include Audit Report. You can save the Signed Document using the Variable or Payload folder.

    >[!NOTE]
    >
    > The Audit Report is appended to the last page of the signed document.

<!--
## Document Services steps {#document-services-steps}

AEM Document services are a set of services for creating, assembling, and securing PDF Documents. [!DNL AEM Forms] provides a separate AEM Workflow step for each document service.

Similar to other [!DNL AEM Forms] workflow steps, such as Assign Task, Send Email, and Sign Document, you can use variables in all AEM Document services steps. For more information on creating and managing variables, see [Variables in AEM workflows](variable-in-aem-workflows.md).
 
### Apply Document Time Stamp step {#apply-document-time-stamp-step}

Add time stamp to a document. You provide document details such as input document path, input document name, location to store exported data. You may choose to overwrite existing payload file, choose a different file name to store data in a different file under payload folder, provide an absolute path to the data, or store data in a variable of Document data type.

### Convert to image step {#convert-to-image-step}

Converts a PDF document to list of images. Supported image formats are JPEG, JPEG2000, PNG, and TIFF. The following information applies to conversions to TIFF images:

* A multi-page TIFF file is generated.
* Some annotations are not included in TIFF images. Annotations that require Acrobat to generate their appearance are not included.

### Convert to PDF/A step {#convert-to-pdf-a-step}

Converts a PDF document to PDF/A format using the options provided. The PDF/A version of Portable Document Format (PDF) is specialized for archiving and long-term preservation of documents.

### Convert to PS step {#convert-to-ps-step}

Convert PDF documents to PostScript. When converting to PostScript, you can use the conversion operation to specify the source document and whether to convert to PostScript level 2 or 3. The PDF document you convert to a PostScript file must be non-interactive.

### Create PDF from specified type step {#create-pdf-from-specified-type-step}

Generate a PDF document from an input file. The input document can be relative to the payload, have an absolute path, can be payload itself, or stored in a variable of Document data type.

### Create PDF from URL/HTML/ZIP step {#create-pdf-from-url-html-zip-step}

Generates a PDF document from supplied URL, HTML, and ZIP file.

### Export Data step {#export-data-step}

Exports data from a PDF forms or XDP file. It requires you to enter the file path of Input Document and the Export Data Format. The options for Export Data Format are Auto, XDP and XmlData.

### Export PDF to specified type step {#export-pdf-to-specified-type-step}

Converts a PDF document to a selected format.

### Generate Non-Interactive PDF step {#generatenoninteractive}

Generate a Non-Interactive PDF. It provides various customization options.

>[!NOTE]
>
>You can use variables to specify the template file for input documents. Store the path of the template file in a variable of String data type.

### Import Data step {#import-data-step}

Merges form data into a PDF form. You can import form data into a PDF form.

### Invoke DDX step {#invokeddx}

Executes the DDX file on the specified map of input documents and returns the manipulated PDF documents.

>[!NOTE]
>
>You can use variables to specify the DDX file for input documents. Store the DDX file in a variable of Document or XML data type.

### Optimize PDF step {#optimize-pdf-step}

Optimizes PDF files by reducing their size. The result of this conversion is PDF files that may be smaller than their original versions. This operation also converts PDF documents to the PDF version specified in the optimization parameters.

Optimization settings specify how files are optimized. Here are example settings:

* Target PDF version
* Discarding objects such as JavaScript actions and embedded page thumbnails
* Discarding user data such as comments and file attachments
* Discarding invalid or unused settings
* Compressing uncompressed data or using more efficient compression algorithms
* Removing embedded fonts
* Setting transparency values

### Render PDF Form step {#renderpdf}

Renders a form created in Form Designer (XDP) to a PDF form.

>[!NOTE]
>
>You can use variables to specify the template file for input documents. Store the path of the template file in a variable of String data type.

### Secure Document step {#secure-document-step}

Encrypt, Sign, and certify a document. [!DNL AEM Forms] supports both password based and certificate base encryption. You can also choose between various algorithms for signing documents. For example, SHA-256 and SH-512. You can also use the workflow step to reader extend PDF documents. The workflow step provides option to enable barcode decoding, digital signatures, import and export of PDF data, and other options.

### Send to Printer step {#send-to-printer-step}

Send a document directly to a printer. It supports the following printing access mechanisms:

* **[!UICONTROL Direct accessible printer]**: A printer that is installed on the same computer is called a direct accessible printer, and the computer is named printer host. This type of printer can be a local printer that is connected to the computer directly.
* **[!UICONTROL Indirect accessible printer]**: The printer that is installed on a print server is accessed from other computers. Technologies such as the common UNIX&reg; printing system (CUPS) and the Line Printer Daemon (LPD) protocol are available to connect to a network printer. To access an indirect accessible printer, specify the print server's IP or host name. Using this mechanism, you can send a document to an LPD URI when the network has an LPD running. The mechanism lets you route the document to any printer that is connected to the network that has an LPD running.
    -->

## Generate Printed Output Step {#generatePrintedOutput}

The step generates a PCL, PostScript, ZPL, IPL, TPCL, or DPL output given a form design and data file. The data file is merged with the form design and formatted for printing. The output generated by this step can be sent directly to a printer or saved as a file. It is recommended that you use this step when you want to use form designs or data from an application. If your form designs are on the network, local file system, or HTTP location, use the generatePrintedOutput operation.

For example, your application requires that you merge a form design with a data file. The data contains hundreds of records. In addition, it requires that the output is sent to a printer that supports ZPL. The form design and your input data are in an application. Use the generatePrintedOutput operation to merge each record with a form design and send the output to a printer that supports ZPL.

The Generate Printed Output step has the following properties:

**[!UICONTROL Input properties]**

* **[!UICONTROL Select template file using]**: Specify the path of the template file. You can select the template file using the path that is relative to the payload, saved at an absolute path, or using a variable of Document data type. For example, [Payload_Directory]/Workflow/data.xml. If the path does not exist in crx-repository, an administrator can create the path before using it. Moreover, you can also accept the payload as the input data file.

* **[!UICONTROL Select data document using]**: Specify the path of an input data file. You can select the input data file using the path that is relative to the payload, saved at an absolute path, or using a variable of Document data type. For example, [Payload_Directory]/Workflow/data.xml. If the path does not exist in crx-repository, an administrator can create the path before using it.

* **[!UICONTROL Printer Format]**: A Print Format value that specifies the page description language to use, when an XDC file is not provided, to generate the output stream. If you provide a literal value, select one of these values:

  * **[!UICONTROL color PCL]**: Use the option to specify an XDC file for PCL.
  * **[!UICONTROL Generic PostScript]**: Use the option to specify a generic XDC file for PostScript.
  * **[!UICONTROL ZPL 300 DPI]**: Use ZPL 300 DPI. The zpl300.xdc is used.
  * **[!UICONTROL ZPL 600 DPI]**: Use ZPL 600 DPI. The zpl600.xdc file is used.
  * **[!UICONTROL IPL 300 DPI]**: Use IPL 300 DPI. The ipl300.xdc is used.
  * **[!UICONTROL IPL 400 DPI]**: Use IPL 400 DPI. The ipl400.xdc file is used.
  * **[!UICONTROL TPCL 600 DPI]**: Use TPCL 600 DPI. The tpcl600.xdc file is used.
  * **[!UICONTROL PostScript Plain]**: Use the option to specify a plain text XDC file for PostScript.
   * **[!UICONTROL DPL300DPI]**: Use DPL 300 DPI. The dpl300.xdc is used.
  * **[!UICONTROL DPL400DPI]**: Use DPL 400 DPI. The dpl400.xdc is used.
  * **[!UICONTROL DPL600DPI]**: Use DPL 600 DPI. The dpl600.xdc is used.
  * **[!UICONTROL HP_PCL_5e]**: Use the option to support multiple Canon devices. 
  

**[!UICONTROL Output Properties]**

* **[!UICONTROL Save output document using]**: Specify the location to save the output file. You can save the output file at a location that is relative to the payload, in a variable, or specify an absolute location to save the output file. If the path does not exist in crx-repository, an administrator can create the path before using it.

**[!UICONTROL Advanced Properties]**

* **[!UICONTROL Select Content Root location using]**: Content root is a string value that specifies the URI, absolute reference, or location in the repository to retrieve relative assets used by the form design. For example, if the form design references an image relatively, such as `../myImage.gif`, `myImage.gif` must be at `repository://`. The default value is `repository://`, which points to the root level of the repository.

  When you pick an asset from your application, the Content Root URI path must have the correct structure. For example, if a form is picked from an application named SampleApp, and is placed at `SampleApp/1.0/forms/Test.xdp`, the Content Root URI must be specified as `repository://administrator@password/Applications/SampleApp/1.0/forms/`, or `repository:/Applications/SampleApp/1.0/forms/` (when authority is null). When the Content Root URI is specified this way, the paths of all referenced assets in the form are resolved against this URI.

* **[!UICONTROL Select XCI file using]**: XCI files are used to describe fonts and other properties that are used for form design elements. You can keep an XCI file relative to the payload, at an absolute path, or using a variable of Document data type.

* **[!UICONTROL Locale]**: Specifies the language used for generating the PDF document. If you provide a literal value, select a language from the list or select one of these values:
  * **[!UICONTROL To use server default]**:
    (Default) Use the Locale setting configured on the [!DNL AEM Forms] Server. The Locale setting is configured using the Administration Console. (See [Designer Help](https://helpx.adobe.com/content/dam/help/en/experience-manager/6-5/forms/pdf/using-designer.pdf).)

  * **[!UICONTROL To use custom value]**:
    Type the Locale code in the literal box or select a string variable containing the locale code. For a complete list of supported locale codes, see https://docs.oracle.com/javase/1.5.0/docs/guide/intl/locale.doc.html.

* **[!UICONTROL Copies]**: An integer value that specifies the number of copies to generate for the output. The default value is 1.

* **[!UICONTROL Duplex Printing]**:  A Pagination value that specifies whether to use two-sided or single-sided printing. Printers that support PostScript and PCL use this value. If you provide a literal value, select one of these values:
    * **[!UICONTROL Duplex Long Edge]**: Use two-sided printing and print using long-edge pagination. 
    * **[!UICONTROL Duplex Short Edge]**: Use two-sided printing and print using short-edge pagination. 
    * **[!UICONTROL Simplex]**: Use single-sided printing.
    
## Generate Non Interactive PDF Output step &nbsp; {#generatePDFdocuments}

1. Drag the Generate Non Interactive PDF Output workflow under the Forms Workflow tab in Sidekick.
1. Double-click the added workflow step to edit the component.
1. In the Edit component dialog, configure input documents, output documents, and additional parameters, and click **[!UICONTROL OK]**.

### Input documents {#input-documents-3}

* **Template File**: Specifies the location of the XDP template. It is a mandatory field.

* **Data Document**: Specifies the location of the data xml that must be merged with the template.

### Output document {#output-document}

**Output Document**: Specifies the name of the generated PDF form.

### Additional parameters {#additional-parameters-1}

* **Content Root**: Specifies the path to the folder in the repository where fragments or images used in the input XDP template are stored.
* **Locale**: Specifies the default locale for generated PDF form.
* **Acrobat Version**: Specifies the targeted Acrobat version for the generated PDF form.
* **Linearized PDF**: Specifies whether to optimize the generated PDF for web viewing.
* **Tagged PDF**: Specifies whether to make the generated PDF accessible.
* **XCI document**: Specifies the path to the XCI file.

## See Also {#see-also}

* [Variables in Forms-centric AEM Workflows](/help/forms/variable-in-aem-workflows.md)
* [Configure Out of Office setting](/help/forms/configure-out-of-office-settings.md)

<!--

>[!MORELIKETHIS]
>
>* [Forms-centric workflow on OSGi](/help/forms/aem-forms-workflow.md)
>* [Use AEM translation workflow to localize Adaptive Forms and Document of Record](/help/forms/using-aem-translation-workflow-to-localize-adaptive-forms.md)

-->