---
title: How to create standalone Adaptive Forms using Universal Editor?
description: This article explains how to create Adaptive Forms using Form Creation wizard in AEM author instance and publish forms to AEM Edge Delivery Services.
feature: Edge Delivery Services
role: User
hide: yes
hidefromtoc: yes
---

# Author Adaptive Forms using Universal Editor (WYSIWYG)

This article guides you through the process of authoring the standalone forms with the Universal Editor by selecting an Edge Delivery Services-based template from the Form Creation Wizard. You can also publish the authored forms with Universal Editor to AEM Edge Delivery Services.

<!--To publish forms to Edge Delivery Services, you must first establish a connection between your AEM environment and your GitHub repository. Once connected, you can author the forms using the Universal Editor, which follows a WYSIWYG (What You See Is What You Get) approach for a seamless and consistent user experience with Sites.-->

Before you start, learn about the type of Forms components available to you: 

* [Edge Delivery Services for AEM Forms](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) is a composable set of services that enables a rapid development environment where authors can update, publish, and launch new forms rapidly using Universal Editor. The Universal Editor simplifies form creation for Adobe Edge Delivery Services with a user-friendly, visual WYSIWYG interface. 

* [Adaptive Forms Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html?lang=en): These are standardized data capture components. These components provide customization capabilities, reduced development time, and lower maintenance costs for your digital enrollment experiences. A developer can easily customize and style these components. You can visit [https://aemcomponents.dev/](https://aemcomponents.dev/) to view available core components in action **Adobe recommends using these modern and extensible components to develop Adaptive Forms**.  

* [Adaptive Forms Foundation Components](creating-adaptive-form.md): These are classic (old) data capture components. You can continue to use these to edit your existing foundation components based Adaptive Form. If you are creating new forms, Adobe recommends using  [Adaptive Forms Core Components to create an Adaptive Forms](#create-an-adaptive-form-core-components).



## Pre-requisites

* Set up your GitHub repository following the provided [tutorial](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#get-started-with-the-aem-forms-boilerplate-repository-template).
* If you are already using Edge Delivery Services, add the latest version of the [Adaptive Forms block](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#add-adaptive-forms-block-to-your-existing-aem-project) to your GitHub repository. 
* The AEM Forms Author instance includes a template based on Edge Delivery Services. Ensure the [latest version of Core Components](https://github.com/adobe/aem-core-forms-components) is installed in your environment.
* Keep the URL of your AEM Forms as a Cloud Service author instance and your GitHub Repository handy. 
 
## Author an Adaptive Form using Universal Editor

With the Universal Editor, you can easily create responsive and interactive standalone forms using ready-made components like text fields, checkboxes, and radio buttons. It offers powerful features such as dynamic rules, smooth data integration, and customization options, allowing you to build forms according to your exact requirements.

To author an Adaptive Form using Universal Editor, perform the followng steps:

1. **Create an Adaptive Form on AEM Forms author instance**

   1. Access your AEM Forms as a Cloud Service author instance.
   1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.1.  Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The Wizard opens. 
   1. In the **Source** tab, select a Edge Delivery Services based form template:

        ![Create EDS Forms](/help/edge/assets/create-eds-forms.png)

   1. Click **[!UICONTROL Create]** and the **Create Form** wizard appears.
   1. Specify the **GitHub URL**. For example, if your GitHub repository is named "edsforms", it's located under the account "wkndforms",the URL is:
    `https://github.com/wkndforms/edsforms`
   1. Click **[!UICONTROL Create]**.

        ![Create Form wizard](/help/edge/assets/create-form-wizard.png)

        As soon as you click **[!UICONTROL Create]**, the form opens in the Universal editor for authoring.

        ![author the form](/help/edge/assets/author-form.png)

        >[!NOTE]
        >
        > The Edge Delivery Services configuration for the forms based on Edge Delivery Services template is created automatically at the form's configuration container.

1. **Locate your form's configuration container in AEM author instance**

   1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Edge Delivery Services Configuration]** on your AEM Forms as a Cloud Service author instance.

        ![Select Edge Delivery Services Configuration](/help/edge/assets/select-eds-conf.png)
   1. Select the folder that matches the form's name. For example, if your form is called 'contactus' choose the folder `forms/contactus` and selct the configuration and publish the configuration:

        ![Edge Delivery Services Configuration](/help/edge/assets/aem-instance-eds-configuration.png)

   1. Click **[!UICONTROL Properties]** to see the configuration.   
        ![Automatically created configuration](/help/edge/assets/aem-forms-create-configuration-github.png)

        You can leave the Edge Host option as it is. The form would be published to both preview (.page) and live (.live) environments. 

   1. Click **[!UICONTROL Save and Close]**. The configuration is saved. 

1. **Author the form in the Universal Editor**

    When you click **[!UICONTROL Create]**, the form opens in the Universal Editor for authoring. 

   1. Open the Content browser, and navigate to the **[!UICONTROL Adaptive Form]** component in the **Content tree**.

        ![content tree](/help/edge/assets/content-tree.png)

   1. Click the **[!UICONTROL Add]** icon and add the desired components from the **Adaptive Form Components** list. 
   
        ![add component](/help/edge/assets/add-component.png)

   1. Select the added Adaptive Form component and update its properties using **[!UICONTROL Properties]**.
 
        ![open properties](/help/edge/assets/component-properties.png)

        The below screenshot displays the simple "ContactUs" form authored in the Universal Editor:

        ![contact us form](/help/edge/assets/contact-us.png)

        Now you can [configure and customize Form Submit Actions](/help/edge/docs/forms/universal-editor/submit-action.md).

## Publish and preview the form
    
Now, publish the standalone form to Edge Delivery Services by clicking the **[!UICONTROL Publish]** button in the upper-right corner of the Universal Editor.

![publish form](/help/edge/assets/publish-form.png)

>[!NOTE]
>
> Refer to the [Publish and Deploy](/help/edge/docs/forms/universal-editor/publish-forms.md) article to learn how to publish a form to Edge Delivery Services.

Here's how to access the form on Edge Delivery Services:

* **Staged Version (for testing)**: The staged version displays the unpublished, working version of the form for testing purposes. Use the following URL format to preview the form before it goes live:

    `https://<branch>--<repo>--<owner>.aem.page/content/forms/af/<form_name>`

    For example, if your project's repository is named "edsforms", it's located under the account "wkndforms", and you're using the "main" branch and form as "contactus", the staged version URL look like the following:
    https://main--edsforms--wkndforms.aem.page/content/forms/af/contactus

* **Live Version (published form)**:   The live version displays the most recently published version of the form, accessible to end users. Use the following URL format to access the published, live version of the form:

    `https://<branch>--<repo>--<owner>.aem.live/content/forms/af/<form_name>`

    For example, if your project's repository is named "edsforms", it's located under the account "wkndforms", and you're using the "main" branch and form as "contactus", the staged version URL look like the following:
    https://main--edsforms--wkndforms.aem.live/content/forms/af/contactus

The URL structure remains the same for both staged and live versions. However, the content you see differs based on the context:

![View published form](/help/edge/assets/eds-view-publish-form.png)

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

