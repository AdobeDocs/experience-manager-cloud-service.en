---
title: How to create standalone forms based on Edge Delivery Services template using Universal Editor?
description: This article explains how to use the Universal Editor to create forms by selecting an Edge Delivery Services-based template in the Form Creation Wizard. You can also publish the forms to AEM Edge Delivery Services.
feature: Edge Delivery Services
role: User
hide: yes
hidefromtoc: yes
exl-id: 1eab3a3d-5726-4ff8-90b9-947026c17e22
---
# Creating Adaptive Forms using Universal Editor

<span class="preview"> This feature is available through the early access program. To request access, send an email with your GitHub organization name and repository name from your official address to <a href="mailto:aem-forms-ea@adobe.com">aem-forms-ea@adobe.com</a> . For example, if the repository URL is https://github.com/adobe/abc, the organization name is adobe and the repository name is abc.</span> 

Universal Editor is a versatile visual editor that provides a what-you-see-is-what-you-get (WYSIWYG) experience for editing forms. It simplifies the creation of responsive and user-friendly forms with a drag-and-drop feature, using available Adaptive Forms components like text boxes, radio buttons, and checkboxes.

AEM provides a block, known as the Adaptive Forms Block, to help you easily create Edge Delivery Services Forms to capture and store data uing Universal Editor. You can [create a new AEM Project pre-configured with the Adaptive Forms Block](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#create-a-new-aem-project-pre-configured-with-adaptive-forms-block) or [add the Adaptive Forms Block to an existing AEM Site Project](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#add-adaptive-forms-block-to-your-existing-aem-project).

![Github Repository Workflow](/help/edge/assets/repo-workflow.png){width=50%, align=centre}

This article guides you through the process of creating and authoring the standalone forms with the Universal Editor by selecting an Edge Delivery Services-based template from the Form Creation Wizard. 

## Pre-requisites

* [Set up your GitHub repository](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#get-started-with-the-aem-forms-boilerplate-repository-template) to establish a connection between your AEM environment and the GitHub repository.
* If you are already using Edge Delivery Services, add the latest version of the [Adaptive Forms block](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#add-adaptive-forms-block-to-your-existing-aem-project) to your GitHub repository. 
* The AEM Forms Author instance includes a template based on Edge Delivery Services. Ensure the [latest version of Core Components](https://github.com/adobe/aem-core-forms-components) is installed in your environment.
* Keep the URL of your AEM Forms as a Cloud Service author instance and your GitHub Repository handy. 

## Working with forms in Universal Editor 

With the Universal Editor, you can easily create responsive and interactive standalone forms. You can perform the following actions on forms in Universal Editor:
* [Create a form](#create-a-form)
* [Author a form](#author-a-form)
* [Publish a form](#publish-a-form)
* [Manage a form](#manage-a-form)

>[!NOTE]
>
> You can also [author a form in AEM Site using the Edge Delivery Services Site template in Universal Editor and publish it to Edge Delivery Services](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#create-a-new-aem-project).


### Create a form

   1. Login into your AEM Forms as a Cloud Service author instance.
   1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
   1. Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The Wizard opens. 
   1. In the **Source** tab, select a Edge Delivery Services based form template:

        ![Create EDS Forms](/help/edge/assets/create-eds-forms.png)


      When you select a Edge Delivery Services based template, the **[!UICONTROL Create]** button is enabled. 
   1. (Optional) In the **[!UICONTROL Data Source]** or **[!UICONTROL Submission]** tabs, you can select a data source or submit action.
   1. (Optional) In the **[!UICONTROL Delivery]** tab, you can specify a publishing or unpublishing date for a form. 

   1. Click **[!UICONTROL Create]** and the **Create Form** wizard appears.
   1. Specify the **Name** and **Title**. 
   1. Specify the **GitHub URL**. For example, if your GitHub repository is named `edsforms`, it is located under the account `wkndforms`,the URL is:
    `https://github.com/wkndforms/edsforms`
   1. Click **[!UICONTROL Create]**.

        ![Create Form wizard](/help/edge/assets/create-form-wizard.png)

        As soon as you click **[!UICONTROL Create]**, the form opens in the Universal editor for authoring.

        ![author the form](/help/edge/assets/author-form.png)

       <!-- >[!NOTE]
        >
        > The Edge Delivery Services configuration for the forms based on Edge Delivery Services template is created automatically at the form's configuration container.-->

        When you click **[!UICONTROL Create]**, the form opens in the Universal Editor for authoring. 

### Author a form 

   1. Open the Content browser, and navigate to the **[!UICONTROL Adaptive Form]** component in the **Content tree**.

        ![content tree](/help/edge/assets/content-tree.png)

   1. Click the **[!UICONTROL Add]** icon and add the desired components from the **Adaptive Form Components** list. 
   
        ![add component](/help/edge/assets/add-component.png)

   1. Select the added Adaptive Form component and update its properties using **[!UICONTROL Properties]**.
 
        ![open properties](/help/edge/assets/component-properties.png)

        The below screenshot displays the simple `Registration Form` form authored in the Universal Editor:

        ![contact us form](/help/edge/assets/contact-us.png)

        Now you can [configure and customize the submit actions for forms](/help/edge/docs/forms/universal-editor/submit-action.md).


<!--
## **Edge Delivery Services configuration of form**



   1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Edge Delivery Services Configuration]** on your AEM Forms as a Cloud Service author instance.

        ![Select Edge Delivery Services Configuration](/help/edge/assets/select-eds-conf.png)
   1. Select the folder that matches the form's name. For example, if your form is called 'registration-form' choose the folder `forms/registration-form` and selct the configuration and publish the configuration:

        ![Edge Delivery Services Configuration](/help/edge/assets/aem-instance-eds-configuration.png)

   1. Click **[!UICONTROL Properties]** to see the configuration.   
        ![Automatically created configuration](/help/edge/assets/aem-forms-create-configuration-github.png)

        You can leave the Edge Host option as it is. The form would be published to both preview (.page) and live (.live) environments. 

   1. Click **[!UICONTROL Save and Close]**. The configuration is saved. -->

### Publish a form
    
Now, publish the standalone form to Edge Delivery Services by clicking the **[!UICONTROL Publish]** button in the upper-right corner of the Universal Editor.

![publish form](/help/edge/assets/publish-form.png)

>[!NOTE]
>
> Refer to the [Publish and Deploy](/help/edge/docs/forms/universal-editor/publish-forms.md) article to learn how to publish a form to Edge Delivery Services.

Here's how to access the form on Edge Delivery Services:

* **Staged Version (for testing)**: The staged version displays the unpublished, working version of the form for testing purposes. Use the following URL format to preview the form before it goes live:

    `https://<branch>--<repo>--<owner>.aem.page/content/forms/af/<form_name>`

    For example, if your project's repository is named "edsforms", it's located under the account "wkndforms", and you're using the "main" branch and form as "Registration Form", the staged version URL look like the following:
    `https://main--edsforms--wkndforms.aem.page/content/forms/af/registration-form`

* **Live Version (published form)**:   The live version displays the most recently published version of the form, accessible to end users. Use the following URL format to access the published, live version of the form:

    `https://<branch>--<repo>--<owner>.aem.live/content/forms/af/<form_name>`

    For example, if your project's repository is named "edsforms", it's located under the account "wkndforms", and you're using the "main" branch and form as "Registration Form", the staged version URL look like the following:
    `https://main--edsforms--wkndforms.aem.live/content/forms/af/registration-form`

The URL structure remains the same for both staged and live versions. However, the content you see differs based on the context:

![View published form](/help/edge/assets/eds-view-publish-form.png)

### Manage a form

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
  </tr>-->
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

## Troubleshooting 

Having trouble loading your form? Here are some common issues and how to fix them:

* **Form URL**: Double-check that your form's URL doesn't include the ".html" extension at the end. Edge Deliver Service does not require this extension.

* **AEM Author UR**L: Make sure the AEM Author URL listed in your `fstab.yaml` file is formatted correctly. It should include the following details:

    * The correct GitHub owner
    * The correct repository name
    * The specific branch that you're using for Edge Delivery Services

<!-- * **JSON Display**: If you see only JSON data instead of the actual form, your form block might be outdated. You can update it to the latest version available on https://github.com/adobe-rnd/aem-boilerplate-forms.
-->

## Start creating forms

{{universal-editor-see-also}}
