---
title: How to use AEM Forms for business process automation (BPM)?
seo-title: Rapidly build Adaptive Forms-based processes, automate document services operations, and use Adobe Sign with AEM workflows
description: Use AEM Forms Workflow to automate and rapidly build business process workflows. For example, review and approval, PDF Generation, Adobe Sign workflows.
uuid: 797ba0f7-a378-45ac-9f82-fa9a952027be
topic-tags: publish, document_services
feature: Adaptive Forms
role: User, Developer
hide: yes
hidefromtoc: yes
exl-id: f0fec4a9-b214-4931-bf09-5898b082481e
---
# Forms-centric workflow on OSGi {#forms-centric-workflow-on-osgi}

 ![Hero Image](do-not-localize/header.png)

Enterprises collect data from hundreds and thousands of forms, various back-end systems, and online or offline data sources. They also have a dynamic set of users to take decisions on the data, which involves iterative review and approval processes.

Along with review and approval workflows for internal and external audiences, large organizations and businesses have repetitive tasks. For example, converting a PDF document to another format. When done manually, these tasks take up much time and resources. Enterprises also have legal requirements to digitally sign a document and archive form data for later use in pre-defined formats.

## Introduction to Forms-centric workflow on OSGi {#introduction-to-forms-centric-workflow-on-osgi}

You can use AEM Workflows to rapidly build Adaptive Forms-based workflows. These workflows can be used for review and approvals, business process flows, to start document services, integrate with Adobe Sign signature workflow, and similar operations. For example, credit card application processing, employee leave approval workflows, saving a form as a PDF document. Moreover, these workflows can be used within an organization or across network firewall.

With Forms-centric workflow on OSGi, you can rapidly build and deploy workflows for various tasks on the OSGi stack, without having to install the full-fledged Process Management capability on JEE stack. The development and management of workflows uses the familiar AEM Workflow and AEM Inbox capabilities. Workflows form the basis of automating real-world business processes that span multiple software systems, networks, departments, and even organizations.

Once set up, these workflows can be triggered manually to complete a defined process or run programmatically when users submit a form <!-- or [correspondence management](cm-overview.md) letter-->. <!-- With this enhanced AEM Workflow capabilities, [!DNL AEM Forms] offers two distinct, yet similar, capabilities. As part of your deployment strategy, you need to decide which one works for you. See a [comparison](capabilities-osgi-jee-workflows.md) of the Forms-centric AEM Workflows on OSGi and Process Management on JEE. Moreover, for the deployment topology see, [Architecture and deployment topologies for [!DNL AEM Forms]]((aem-forms-architecture-deployment.md). -->

Forms-centric workflow on OSGi extends [AEM Inbox](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/sites/authoring/getting-started/inbox.html#authoring) and provides extra components (steps) for AEM Workflow editor to add support for [!DNL AEM Forms]-centric workflows. <!-- The extended AEM Inbox has functionalities similar to [[!DNL AEM Forms] Workspace](introduction-html-workspace.md). Along with managing human-centric workflows (Approval, Review, and so on), you can use AEM workflows to automate [document services](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-step-ref.html#extending-aem)-related operations (for example, Generate PDF) and electronically signing (Adobe Sign) documents. -->

All [!DNL AEM Forms] workflow steps support the use of variables. Variables enable workflow steps to hold and pass metadata across steps at runtime. You can create different types of variables for storing different types of data. You can also create variable collections (array) for storing multiple instances of related, same-typed data. Typically, you use a variable or a collection of variables when you need to make a decision based on the value that it holds or to store information that you need later in a process. For more information on using variables in these Forms-centric workflow components (steps), see [Forms-centric workflow on OSGi - Step Reference](aem-forms-workflow-step-reference.md). For information on creating and managing variables, see [Variables in AEM workflows](variable-in-aem-workflows.md).

The following diagram depicts end-to-end procedure to create, run, and monitor a Forms-centric workflow on OSGi.

![introduction-to-aem-forms-workflow](assets/introduction-to-aem-forms-workflow.jpg)

## Before you start {#before-you-start}

* A workflow is a representation of a real-world business process. Keep your real-world business process and list of the participants of the business process ready. Also, keep the collateral (Adaptive Forms, PDF Documents, and more) ready before start creating a workflow.
* A workflow can have multiple stages. These stages are displayed in the AEM Inbox and help report progress of the workflow. Divide your business process into logical stages.
* You can configure the assign task step of AEM Workflows to send email notifications to the users or assignees. So, [enable email notifications](#configure-email-service).
* A workflow can also use Adobe sign for digital signatures. If you plan to use Adobe Sign in a workflow, the [configure Adobe Sign for [!DNL AEM Forms]](adobe-sign-integration-adaptive-forms.md) before using it in a workflow.

## Create a workflow model {#create-a-workflow-model}

A workflow model consists of logic and flow of a business process. It is made up of a series of the steps. These steps are AEM components. You can extend workflow steps with parameters and scripts to provide more functionality and control, as required. [!DNL AEM Forms] provides a few steps in addition to AEM steps available out of the box. For a detailed list of AEM and [!DNL AEM Forms] steps, see [AEM Workflow Step Reference](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-step-ref.html#extending-aem) and [Forms-centric workflow on OSGi - Step Reference](aem-forms-workflow.md).

AEM provides an intuitive user interface to create a workflow model using the provided workflow steps. For step-by-step instructions to create a workflow model, see [Creating Workflow Models](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/sites/authoring/workflows/overview.html#workflows). The following example provides step-by-step instructions to create a workflow model for an approval and review workflow:

>[!NOTE]
>
>You must be a member of the workflow-editor group to create or edit a workflow model.

### Create a model for an approval and review workflow {#create-a-model-for-an-approval-and-review-workflow}

Approval and review workflow are for the tasks which require human intervention to make decisions. The following example creates a workflow model for a mortgage loan application to be filled by a front-office banking agent. Once the application is filled, it is sent for approval. Later on, the approved application is sent to the applicant for electronic signatures using Adobe Sign.

The example is available as a package attached below. Import and install the example using the package manager. You can also perform the following steps to manually create the workflow model for the application:

The example creates a workflow model a mortgage application to be filled by a front-office banking agent. Once filled the application is sent for approval. Later on, the approved application is sent to the customer for electronic signatures using Adobe Sign. You can import and install the example using the package manager.

[Get File](assets/example-mortgage-loan-application.zip)

1. Open the Workflow Models console. The default URL is `https://[server]:[port]/libs/cq/workflow/admin/console/content/models.html/etc/workflow/models`
1. Select **Create**, then **Create Model**. The Add Workflow Model dialog appears.
1. Enter the **Title** and **Name** (optional). For example, a mortgage application. Select **Done**.
1. Select the created workflow model and select **Edit**. Now, you can add workflow steps to build business logic. When you first create a workflow model, it contains:

    * The steps: Flow Start and Flow End. These steps represent the beginning and end of the workflow. These steps are required and cannot be edited or removed.
    * An example Participant step named Step 1. This step is configured to assign a work item to the admin user. Remove this step.

1. Enable email notifications. You can configure Forms-centric workflow on OSGi to send email notifications to the users or assignees. Perform the following configurations to enable email notifications:

    1. Go to AEM configuration manager at `https://[server]:[port]/system/console/configMgr`.
    1. Open the **[!UICONTROL Day CQ Mail Service]** configuration. Specify a value for the **[!UICONTROL SMTP server host name]**, **[!UICONTROL SMTP server port]**, and **[!UICONTROL "From" address]** fields. Click **[!UICONTROL Save]**.
    1. Open the **[!UICONTROL Day CQ Link Externalizer]** configuration. In the **[!UICONTROL Domains]** field, specify the actual hostname/IP address and port number for local, author, and publish instances. Click **[!UICONTROL Save]**.

1. Create workflow stages. A workflow can have multiple stages. These stages are displayed in the AEM Inbox and report progress of the workflow.

   To define a stage, select the ![info-circle](assets/info-circle.png) icon to open workflow model properties, open the **Stages** tab, add stages for the workflow model, and select **Save & Close**. For the example mortgage application, create stages: loan request, loan request status, to be signed documents, and signed loan document.

1. Drag-and-drop the **Assign Task** steps browser to the workflow model. Make it the first step of the model.

   The assign task component assigns the task, created by workflow, to a user or group. Along with assigning the task, you can use the component to specify an Adaptive Form or a non-interactive PDF for the task. The Adaptive Form is required to accept input from users and non-interactive PDF or a read-only Adaptive Form is used for review only workflows.

   You can also use the step to control the behavior of the task. For example, creating an automatic Document of Record, assign the task to a specific user or group, the path of the submitted data, the path of data to be pre-populated, and default actions. For detailed information about the options of the assign task step, see [Forms-centric workflow on OSGi - Step Reference](aem-forms-workflow.md) document.

   ![workflow-editor](assets/workflow-editor.png)

   For the mortgage application example, configure the assign task step to use a Read-only Adaptive Form and display PDF Document once the task is complete. Also, select to user group allowed to approve the loan request. On the **Actions** tab, disable the **Submit** option. Create an **actionTaken** variable of String data type and specify the variable as the **Route Variable**. For example, actionTaken. Also, add the Approve and Reject routes. The routes are displayed as separate actions (buttons) in AEM Inbox. The workflow selects a branch based on the action (button) a user taps.

   You can import the example package, available for download in the starting of the section, for the complete set of values of all the fields of the assign task step configured for example, mortgage application.

1. Drag-and-drop the OR Split component from step browser to the workflow model. The OR Split creates a split in the workflow, after which only one branch is active. This step enables you to introduce conditional processing paths into your workflow. You add workflow steps to each branch as required.

   You can define routing expression for a branch using a rule definition, ECMA script, or an external script.

   Use the expression editor to create routing expressions for Branch 1 and Branch 2. These routing expressions help choose a branch based on the user action in AEM Inbox.

   **Routing expression for Branch 1**

   When a user taps **Approve** in AEM Inbox, Branch 1 is activated.

   ![OR Split example](assets/orsplit_branch1_active_new.png)

   **Routing expression for Branch 2**

   When a user taps **Reject** in AEM Inbox, Branch 2 is activated.

   ![OR Split example](assets/orsplit_branch2_active_new.png)

   For information on creating routing expressions using variables, see [Variables in [!DNL AEM Forms] workflows](variable-in-aem-workflows.md).

1. Add other workflow steps to build the business logic.

   For the mortgage example, add a generate Document of Record, two assign task steps, and a sign document step to Branch 1 of the model, as displayed in the image below. One assign task step is to display and send **to be signed loan documents to the applicant** and another assign task component is **to display signed documents**. Also, add an assign task component to branch 2. It is activated, when a user taps Reject in AEM Inbox.

   For the complete set of values of all the fields of the assign task steps, Document of Record step, and sign document step configured for example, mortgage application, import the example package, available for download in the starting of this section.

   The workflow model is ready. You can launch the workflow through various methods. For details, see [Launch a Forms-centric workflow on OSGi](#launch).

   ![workflow-editor-mortgage](assets/workflow-editor-mortgage.png)

## Create a Forms-centric Workflow Application {#create-a-forms-centric-workflow-application}

The application is the Adaptive Form associated with the workflow. When an application is submitted through Inbox, it launches the associated workflow. To make a Forms workflow available as an application in AEM Inbox and [!DNL AEM Forms] App, do the following to create a workflow application:

>[!NOTE]
>
>You must be a member of the fd-administrator group to be able to create and manage workflow applications.

1. On your AEM author instance, go to ![tools-1](assets/tools-1.png) > **[!UICONTROL Forms]** > **[!UICONTROL Manage Workflow Application]** and taps **[!UICONTROL Create]**.
1. In the Create Workflow Application window, provide inputs for the following fields, and taps **Create**. A new application is created and is listed in the Workflow Applications screen.

<table>
 <tbody>
  <tr>
   <td>Field</td>
   <td>Description</td>
  </tr>
  <tr>
   <td>Title</td>
   <td>The title is visible in AEM Inbox and helps users choose an application. Keep it descriptive. For example, Savings Account Opening Application.<br /> </td>
  </tr>
  <tr>
   <td>Name </td>
   <td>Specify the name of the application. All the characters other than alphabets, numbers, hyphens, and underscores are replaced with hyphens. </td>
  </tr>
  <tr>
   <td>Description</td>
   <td>The description is visible in AEM Inbox. Provide detailed information about the application in the description fields. For example, Purpose of the application.<br /> </td>
  </tr>
  <tr>
   <td>Adaptive Form</td>
   <td><p>Specify the path of an Adaptive Form. When a user starts an application, the specified Adaptive Form is displayed.</p> <p><strong>Note</strong>: Workflow applications do not support forms and PDF documents which are longer than one page or require scrolling on Apple iPad. When an application is opened on Apple iPad and the Adaptive Form or the PDF document is longer than a page, the form fields and content from the second page are lost.</p> </td>
  </tr>
  <tr>
   <td>Access Group</td>
   <td><p>Select a group. The application is visible in AEM Inbox only to the members of the selected group. The access group option makes all the groups of the [!DNL workflow-users] group available for selection. </p> <br /> </td>
  </tr>
  <tr>
   <td>Prefill Service</td>
   <td>Select a <a href="prepopulate-adaptive-form-fields.md#aem-forms-custom-prefill-service" target="_blank">prefill service</a> for the Adaptive Form.<br /> </td>
  </tr>
  <tr>
   <td>Workflow Model</td>
   <td>Select a <a href="aem-forms-workflow.md#create-a-workflow-model">workflow model</a> for the application. A workflow model consists of logic and flow of the business process. </td>
  </tr>
  <tr>
   <td>Data File Path</td>
   <td>Specify the path of the data file in crx-repository. The path is relative to Adaptive Form payload and contains the name of the data file. Always include the complete name of the file including extension, if applicable. For example, [payload]/data.xml. </td>
  </tr>
  <tr>
   <td>Attachment Path</td>
   <td>Specify the path of attachments folder in crx-repository. The attachment path is relative to payload location. For example, [payload]/data.xml. </td>
  </tr>
  <tr>
   <td>Document of Record Path</td>
   <td>Specify the path of Document of Record file in crx-repository. The path is relative to Adaptive Form payload location. Always include the complete name of the file including extension, if applicable. For example, [payload]/DOR/creditcard.pdf.</td>
  </tr>
 </tbody>
</table>

## Launch a Forms-centric workflow on OSGi {#launch}

You can launch or trigger a Forms-centric workflow by:

* [Submitting an application from AEM Inbox](#inbox)
* [Submitting an application from [!DNL AEM Forms] App](#afa)

* [Submitting an Adaptive Form](#af)
* [Using watched folder](#watched)

* [Submitting an interactive communication or a letter](#letter)

### Submitting an application from AEM Inbox {#inbox}

The workflow application you created is available as an application in Inbox. Users who are members of [!DNL workflow-users] group can fill and submit the application that triggers the associated workflow. 

<!-- ### Submitting an application from [!DNL AEM Forms] App {#afa}

The [!DNL AEM Forms] app syncs with an [!DNL AEM Forms] server and lets you change the form data, tasks, workflow applications, and saved information (drafts/templates) in your account. For more information, see [[!DNL AEM Forms] app]((aem-forms-app.md) and related articles.-->

### Submitting an Adaptive Form {#af}

You can configure the Submit Actions of an Adaptive Form to start a workflow on submission of the Adaptive Form. Adaptive Forms provides the **Invoke an AEM Workflow** Submit Action to start a workflow on submission of an Adaptive Form. For detailed information about the Submit Action, see [Configuring the Submit Action](configuring-submit-actions.md). To submit an Adaptive Form through the [!DNL AEM Forms] app, enable Sync With [!DNL AEM Forms] App in the Adaptive Form properties.

<!-- You can configure an Adaptive Form to sync, submit, and trigger a workflow from [!DNL AEM Forms] app. For details, see [working with a form]((working-with-form.md). -->

<!-- ### Using a watched folder {#watched}

An administrator (a member of fd-administrators group) can configure a network folder to run a pre-configured workflow when a user places a file (such as a PDF file) in the folder. After the workflow completes, it can save the result file to a specified output folder. Such a folder is known as [Watched Folder](watched-folder-in-aem-forms.md). Perform the following procedure to configure a watched folder to launch a workflow:

1. On your AEM author instance, go to ![tools-1](assets/tools-1.png) > **[!UICONTROL Forms]** > **[!UICONTROL Configure Watched Folder]**. A list of already configured watched folders is displayed.
1. Select **[!UICONTROL New]**. A list of fields is displayed. Specify a value for the following fields to configure a Watched Folder for a workflow:

<table>
 <tbody>
  <tr>
   <td>Field</td>
   <td>Description</td>
  </tr>
  <tr>
   <td><span class="uicontrol">Name</code></td>
   <td>Specify the name of the Watched Folder. This field support only alphanumeric.</td>
  </tr>
  <tr>
   <td><span class="uicontrol">Path</code></td>
   <td>Specify the physical location of the Watched Folder. In a clustered environment, use a shared network folder that is accessible from AEM cluster node.</td>
  </tr>
  <tr>
   <td><span class="uicontrol">Process Files Using</code></td>
   <td>Select the <span class="uicontrol">Workflow </code>option. </td>
  </tr>
  <tr>
   <td><span class="uicontrol">Workflow Model</code></td>
   <td>Select a workflow model.<br /> </td>
  </tr>
  <tr>
   <td><span class="uicontrol">Output File Pattern</code></td>
   <td>Specify the directory structure for output files and directories. </a>.</td>
  </tr>
 </tbody>
</table>

1. Select **Advanced**. Specify a value for the following field and taps **Create**. The Watched Folder is configured to launch a workflow. Now, whenever a file is placed in the input directory of the Watched Folder, the specified workflow is triggered.

   | Field |Description |
   |---|---|
   | Payload Mapper Filter |When you create a watched folder, it creates a folder structure in the crx-repository. The folder structure can serve as a payload to the workflow. You can write a script to map an AEM Workflow to accept inputs from the watched folder structure. An out of the box implementation is available and listed in the Payload Mapper Filter. If you do not have a custom implementation, select the default implementation. |

   The Advanced tab contains more fields. Most of these fields contain a default value. To learn about all the fields, see the [Create or Configure a watched folder]((admin-help/configuring-watched-folder-endpoints.md) article. --> 

<!-- ### Submitting an interactive communication or a letter {#letter}

You can associate and execute a Forms-centric workflow on OSGi on submission of an interactive communication or a letter. In correspondence management workflows are used for post processing interactive communications and letters. For example, emailing, printing, faxing, or archiving final letters. For detailed steps, see [Post processing of interactive communications and letters](submit-letter-topostprocess.md).

## Additional Configurations {#additional-configurations}

### Configure email service {#configure-email-service}

You can use the Assign Task and Send Email steps of AEM Workflows to send an email. Perform the following steps to specify email servers and other configurations required to send email:

1. Go to AEM configuration manager at `https://[server]:[port]/system/console/configMgr`.
1. Open the **[!UICONTROL Day CQ Mail Service]** configuration. Specify a value for the **[!UICONTROL SMTP server host name]**, **[!UICONTROL SMTP server port]**, and **[!UICONTROL "From" address]** fields. Click **[!UICONTROL Save]**.
1. Open the **[!UICONTROL Day CQ Link Externalizer]** configuration. In the **[!UICONTROL Domains]** field, specify the actual hostname/IP address and port number for local, author, and publish instances. Click **[!UICONTROL Save]**. -->

### Purge workflow instances {#purge-workflow-instances}

Minimizing the number of workflow instances increases the performance of the workflow engine, so you can regularly purge completed or running workflow instances from the repository. For detailed information see, [Regular Purging of Workflow Instances](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/maintenance.html) purging of workflow instances
