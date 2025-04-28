---
title: How to create standalone forms based on Core Component or Edge Delivery Services templates and publish them on Edge Delivery Services
description: This article explains how to create Adaptive Forms by selecting a Core Component-based or Edge Delivery Services-based templates in the Form Creation Wizard. You can also publish the forms to AEM Edge Delivery Services.
feature: Edge Delivery Services
role: User
hide: yes
hidefromtoc: yes
exl-id: 1eab3a3d-5726-4ff8-90b9-947026c17e22
---

# From Authoring to Publishing: AEM Forms on Edge Delivery Services

<span class="preview"> This feature is available through the early access program. To request access, send an email with your GitHub organization name and repository name from your official address to <a href="mailto:aem-forms-ea@adobe.com">aem-forms-ea@adobe.com</a> . For example, if the repository URL is https://github.com/adobe/abc, the organization name is adobe and the repository name is abc.</span> 

Adobe Experience Manager (AEM) lets you create forms that are engaging, responsive, and dynamic. It offers multiple authoring methods, each suited to different requirements and levels of user expertise.​

This article focuses on the approach where forms are authored within the AEM environment and published through Edge Delivery Services. Forms built using Core Component-based templates can be published on both AEM and Edge Delivery Services, offering flexibility in deployment. In contrast, forms authored using Edge Delivery Services-based templates can only be published on Edge Delivery Services.​

![Author and Publish Adaptive Form](/help/edge/docs/forms/universal-editor/assets/author-publish-af.png){width=50% align=center}

## Advantages of authoring forms in AEM and publishing using Edge Delivery Services:

* **Preservation of existing AEM workflows**: Organizations can continue using their established AEM workflows and governance structures, ensuring consistency and control over content creation.​

* **Enhanced performance**: Publishing through Edge Delivery Services results in faster rendering times, improving the user experience and reducing page load times.​

* **Improved SEO**: Edge Delivery Services is designed to deliver content with high Google Lighthouse scores, which can lead to better search engine optimization and increased visibility.​

* **Flexible deployment options**: Forms built with Core Components can be published on both AEM and Edge Delivery Services, offering flexibility in deployment strategies.​
  
## Before you start

Before you begin authoring forms in AEM and publishing them through Edge Delivery Services, ensure the following prerequisites are met:

* Ensure that you have a Github Repository configured for Edge Delivery Services.
  * If you do not have a repository, [new AEM project pre-configured with the Adaptive Forms Block](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#create-a-new-aem-project-pre-configured-with-adaptive-forms-block).
  * If you have a repository, Add the Adaptive Forms Block to your existing repository. Detailed instructions are available in the [Getting Started with Edge Delivery Services for AEM Forms](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#add-adaptive-forms-block-to-your-existing-aem-project).
* Establish a connection between your AEM environment and GitHub repository. [How to do it?](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#get-started-with-the-aem-forms-boilerplate-repository-template)

<!--A decision flow diagram to guide the setup and publishing of Adaptive Forms:

![Github Repository Workflow](/help/forms/assets/repo-workflow.png){width=auto}

## Authoring forms in AEM and publishing them to Edge Delivery Services

Follow these steps to author forms in AEM and publish them on Edge Delivery Services:

[1. Choose a template and create the form](#choose-a-template-and-create-the-form)

[2. Author the form](#author-the-form)

[3. Publish a form](#publish-a-form)

### Choose a template and create the form 

You can create forms on an AEM instance for publishing to Edge Delivery Services using:

>[!BEGINTABS]

>[!TAB Edge Delivery Services-based template]

Perform the following steps to choose the template and create the form:

1. Login in to your AEM Forms as a Cloud Service author instance.
1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
1. Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The Wizard opens.
1. In the **Source** tab, select an **Edge Delivery Services-based template**:

      ![Create EDS Forms](/help/edge/assets/create-eds-forms.png)

      When you select an **Edge Delivery Services-based template**, the **[!UICONTROL Create]** button is enabled. 
1. (Optional) In the **[!UICONTROL Data Source]** or **[!UICONTROL Submission]** tabs, you can select a data source or submit action.
1. (Optional) In the **[!UICONTROL Delivery]** tab, you can specify a publishing or unpublishing date for a form. 
1. Click **[!UICONTROL Create]** and the **Create Form** wizard appears:
   
    1. Specify the **Name** and **Title**. 
    1. Specify the **GitHub URL**. For example, if your GitHub repository is named `edsforms`, it is located under the account `wkndforms`,the URL is:
    `https://github.com/wkndforms/edsforms`

    ![Create Form wizard](/help/edge/assets/create-form-wizard.png)

    When you click **[!UICONTROL Create]**, the form opens in the Universal Editor for authoring.

    ![author the form](/help/edge/assets/author-form.png)
1. Click **[!UICONTROL Create]** to create the form. Now, you can [author the form using the Universal Editor](#author-the-form).

>[!TAB Core Component-based template]

Perform the following steps to choose the template and create the form:

1. Login in to your AEM Forms as a Cloud Service author instance.
1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
1. Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The Wizard opens.
1. In the **Source** tab, select a **Core Component based template** and a **theme**, the **[!UICONTROL Create]** button is enabled.:
          
  ![Core Component based template](/help/forms/assets/core-component-based-template.png)

1. (Optional) In the **[!UICONTROL Data Source]** or **[!UICONTROL Submission]** tabs, you can select a data source or submit action.
1. (Optional) In the **[!UICONTROL Delivery]** tab, you can specify a publishing or unpublishing date for a form. 
1. Click **[!UICONTROL Create]** and the **Create Form** wizard appears for:
     1. Specify the **Name** and **Title**.
     2. Specify the location in the **Path** field where the Adaptive Form is to be saved.
          
      ![Create Form Wizard](/help/forms/assets/create-cc-form.png)

      When you click **[!UICONTROL Create]**, the form opens in the Adaptive Form Editor for authoring. 

      ![Adaptive Form Editor](/help/forms/assets/af-editor-form.png)

1. Click **[!UICONTROL Create]** to create the form. Now, you can [author the form using the Adaptive Form Editor](#author-the-form).

>[!ENDTABS]

### Author the form

The forms created using the Edge Delivery Services-based template open in the [Universal Editor](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) for authoring. However, the forms created using the Core Component-based template open in the Adaptive Form Editor for authoring.

Perform the following steps to author forms using the Universal Editor for Edge Delivery Services-based template or using Adaptive Form Editor for  Core Component based template:

>[!BEGINTABS]

>[!TAB Edge Delivery Services-based template]
  

 1. Open the Content browser, and navigate to the **[!UICONTROL Adaptive Form]** component in the **Content tree**.

    ![content tree](/help/edge/assets/content-tree.png)

 1. Click the **[!UICONTROL Add]** icon and add the desired components from the **Adaptive Form Components** list. 
    ![add component](/help/edge/assets/add-component.png)

     The screenshot below displays the `Registration Form` authored in the Universal Editor:

     ![contact us form](/help/edge/assets/contact-us.png)

  >[!NOTE]
  >
  > For detailed instructions on authoring an Adaptive Form using the Universal Editor, [click here](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#author-forms-using-wysiwyg).

  Now you can [configure and customize the submit actions for forms](/help/edge/docs/forms/universal-editor/submit-action.md).

>[!TAB Core Component-based template]

  1. Click **[!UICONTROL Insert component]** in the **Drag components here** section.

     ![Drag components here](/help/forms/assets/drag-components-af-editor.png)

  1. Add the desired components from the **Adaptive Form Components** list. 

     ![Add components](/help/forms/assets/add-component-af.png)

   The screenshot below displays the `Enrollment Form` authored in the Adaptive Form Editor:

   ![Adaptive Form Editor](/help/forms/assets/af-editor-form.png)

  >[!NOTE]
  >
  > For detailed guidance on creating an Adaptive Form based on the Core Component template, [click here](/help/forms/creating-adaptive-form-core-components.md).

  Now you can [configure the submit actions for forms](/help/forms/configure-submit-actions-core-components.md).

>[!ENDTABS]

### Publish the Form

To publish an Adaptive Form on Edge Delivery Services, you need to [create an Edge Delivery Services Configuration on an AEM](#create-an-edge-delivery-services-configuration) instance. 

#### Create an Edge Delivery Services Configuration

Perform the following steps to create the Edge Delivery Services Configuration:

>[!BEGINTABS]
>[!TAB For forms created using the Edge Delivery Services-based template]


  The Edge Delivery Services configuration for forms based on the Edge Delivery Services-based template is created automatically in the form's configuration container.

  ![Edge Delivery Services Configuration](/help/edge/assets/aem-instance-eds-configuration.png)

>[!TAB For forms created using the Core Component-based template]

  1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Edge Delivery Services Configuration]** on your AEM Forms as a Cloud Service author instance.

     ![Select Edge Delivery Services Configuration](/help/edge/assets/select-eds-conf.png)

  1. Select the folder that matches the form's name. For example, if your form is called `enrollment-form`, choose the folder `forms/enrollment-form` and click **[!UICONTROL Create]** > **[!UICONTROL Configuration]**:

     ![Edge Delivery Services Configuration](/help/forms/assets/create-eds-conf.png)

  1. Click the **[!UICONTROL Edge Delivery Services Configuration]** and click **[!UICONTROL Properties]** to open the properties:   
     
     ![Automatically created configuration](/help/forms/assets/eds-conf.png)

     The Edge Delivery Services Configuration appears.

  1. Specify the following in the Edge Delivery Services Configuration:

     * **Organization**: Specify your GitHub organization name.

     * **Site Name**: Specify your GitHub repository name.
     * **Branch**: Specify the branch name. Leave the textbox empty if using the main branch.
     * **(Optional) Edge Host**: Leave the Edge Host option as it is. The form is published to both preview (.page) and live (.live) environments.
     * **(Optional) Site Authentication Token**: Use the Site Authentication Token to securely authenticate requests between your AEM instance and Edge Delivery Services.

  1. Click **[!UICONTROL Save and Close]**. The configuration is created.

>[!ENDTABS]

#### Access the form on Edge Delivery Services

To access the form on Edge Delivery Services, it is mandatory to publish the form. Perform the following steps to publish the form:

>[!BEGINTABS]
>[!TAB On Universal Editor]

   1. Publish the form by clicking the **[!UICONTROL Publish]** button in the upper-right corner of the Universal Editor.

  ![publish form](/help/edge/assets/publish-form.png)

   >[!NOTE]
   >
   > Refer to the [Publish and Deploy](/help/edge/docs/forms/universal-editor/publish-forms.md) article to learn how to publish a form to Edge Delivery Services.

>[!TAB On Adaptive Form Editor]

  1. From the Experience Manager Forms console, navigate to the parent folder and select a form that you want to publish.

  1. Click **[!UICONTROL Publish]**  option from the toolbar, take a look at all the reference assets that would be published with form.

  ![Publish Form on Adaptive Form Editor](/help/forms/assets/publish-af-editor.png)

  >[!NOTE]
  >
  > Refer to the [Manage Publication in Experience Manager Forms](/help/forms/manage-publication.md) article to learn how to publish a form on Adaptive Form Editor.

>[!ENDTABS]

* **Staged Version (for testing)**: The staged version displays the unpublished, working version of the form for testing purposes. Use the following URL format to preview the form before it goes live:

    `https://<branch>--<repo>--<owner>.aem.page/content/forms/af/<form_name>`

    

* **Live Version (published form)**:   The live version displays the most recently published version of the form, accessible to end users. Use the following URL format to access the published, live version of the form:

    `https://<branch>--<repo>--<owner>.aem.live/content/forms/af/<form_name>`

     The URL structure remains the same for both staged and live versions. However, the content you see differs based on the context.

The below screenshots compares staged and live form URLs and visual previews for forms created using Edge Delivery Services-based and Core Component-based templates:

>[!BEGINTABS]
>[!TAB Accessing forms created using Edge Delivery Services-based Template]

  <table border="1" style="width: 100%; border-collapse: collapse; text-align: left;">
    <thead>
    <tr>
      <th style="width: 20%;"><strong>Version</strong></th>
      <th style="width: 80%;"><strong>Image</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td>Staged Version</td>
      <td><img src="/help/forms/assets/registration-form-staged-version.png" alt="Staged version of registration form" style="width: 100%; height: auto;" /></td>
    </tr>
    <tr>
      <td>Live Version</td>
      <td><img src="/help/forms/assets/registration-form-live-version.png" alt="Live version of registration form" style="width: 100%; height: auto;" /></td>
    </tr>
    </tbody>
  </table>

>[!TAB Accessing forms created using Core Component-based Template]

  <table border="1" style="width: 100%; border-collapse: collapse; text-align: left;">
  <thead>
    <tr>
      <th style="width: 20%;"><strong>Version</strong></th>
      <th style="width: 80%;"><strong>Image</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Staged Version</td>
      <td><img src="/help/forms/assets/enrollment-form-staged-version.png" alt="Staged version of enrollment form" style="width: 100%; height: auto;" /></td>
    </tr>
    <tr>
      <td>Live Version</td>
      <td><img src="/help/forms/assets/enrollment-form-live-version.png" alt="Live version of enrollment form" style="width: 100%; height: auto;" /></td>
    </tr>
  </tbody>
  </table>

>[!ENDTABS]

## Troubleshooting 

Having trouble loading your form? Here are some common issues and how to fix them:

* **Form URL**: Double-check that your form's URL doesn't include the ".html" extension at the end. Edge Deliver Service does not require this extension.

* **AEM Author UR**L: Make sure the AEM Author URL listed in your `fstab.yaml` file is formatted correctly. It should include the following details:

    * The correct GitHub owner
    * The correct repository name
    * The specific branch that you're using for Edge Delivery Services

## Start creating forms

{{universal-editor-see-also}}

<!-- * **JSON Display**: If you see only JSON data instead of the actual form, your form block might be outdated. You can update it to the latest version available on https://github.com/adobe-rnd/aem-boilerplate-forms.

### Managing a form

You can perform several operations on form using the AEM Forms user interface.

1. Login into your AEM Forms as a Cloud Service author instance.
1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

1. Select a form and the toolbar displays the following operations you can perform on the selected form.

<table>
 <tbody>
  <tr>
   <td><p><strong>Operation</strong></p> </td>
   <td><p><strong>Description</strong></p> </td>
  </tr>
  <tr>
   <td><p>Edit</p> </td>
   <td><p>Opens the form in edit mode.<br /> <br /> </p> </td>
  </tr>
    <tr>
   <td><p>Properties</p> </td>
   <td><p>Provides options to modify the properties of the form.<br /> <br /> </p> </td>
  </tr>
  <td><p>Copy</p> </td>
   <td><p> Provides options to copy the form  and paste it at the desired location. <br /> <br /> </p> </td>
  </tr>
   <tr>
   <td><p>Preview</p> </td>
   <td><p>Provides options to preview the form as HTML or perform a custom preview by merging data from an XML file with the form. <br /> </p> </td>
  </tr>
  <tr>
   <td><p>Download</p> </td>
   <td><p>Downloads the selected form.<br /> <br /> </p> </td>
  </tr>
  <tr>
   <td><p>Start Review/Manage Review</p> </td>
   <td><p>Allows initiating and managing a review of the selected form.<br /> <br /> </p> </td>
  </tr>
  <!--<tr>
   <td><p>Add Dictionary</p> </td>
   <td><p>Generates a dictionary for localizing the selected fragment. For more information, see <a>Localizing Adaptive Forms</a>.<br /> <br /> </p> </td>
  </tr>
  <tr>
   <td><p>Publish / Unpublish</p> </td>
   <td><p>Publishes / unpublishes the selected form.<br /> <br /> </p> </td>
  </tr>
  <tr>
   <td><p>Delete</p> </td>
   <td><p>Deletes the selected form.<br /> <br /> </p> </td>
  </tr>
  <tr>
   <td><p>Compare</p> </td>
   <td><p>Compares two different form for previewing purposes.<br /> <br /> </p> </td>
  </tr>
 </tbody>
</table> 


## How Edge Delivery Services Forms Work?

Users can author Edge Delivery Services Forms using document-based authoring tools such as Google Drive, SharePoint, or the Universal Editor (WYSIWYG authoring), while leveraging the basic styling, behaviour and components available in the GitHub repository. Once authored, Edge Delivery Services Forms can send data to any platform using the Forms Submission Service.

![How Edge Delivery Services Forms works](/help/edge/docs/forms/assets/eds-forms-working.png)

### Key components of Edge Delivery Services Forms

The key components of Edge Delivery Servies Forms are:

* **GitHub Repository**: The GitHub repository serves as a boilerplate for creating Edge Delivery Services Forms. The forms leverage basic styling and functionality from the repository and allow users to add customizations and custom components to the Edge Delivery Services Forms.

* **Form Authoring**: Edge Delivery Services Forms support two types of authoring: WYSIWYG and document-based authoring. Document-based authoring enables users to create forms using familiar tools like Google Docs and Microsoft Office. WYSIWYG authoring allows users to design forms visually using the Universal Editor, making it easy for non-technical users to create and manage forms. Universal Editor offers an intuitive form creation experience and provides access to numerous form capabilities.

* **Forms Submission Service**: The Forms Submission Service allows you to store data from forms submissions on any platform, such as OneDrive, SharePoint, or Google Sheets, making it easy to access and manage form data within your preferred system.-->
