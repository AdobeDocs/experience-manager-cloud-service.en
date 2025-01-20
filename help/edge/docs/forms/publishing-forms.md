---
title: Publishing Forms for Edge Delivery Services
description: Learn how forms publishing works with Edge Delivery Services and how to publish AEM forms with Edge Delivery Services.
feature: Edge Delivery Services
role: User
hide: yes
hidefromtoc: yes
---

# Publishing Forms for Edge Delivery Services 

This article guides you through the process of publishing forms to AEM Edge Delivery Services.
To publish forms to Edge Delivery Services, you must first establish a connection between your AEM environment and your GitHub repository. Once connected, you can author the forms using the Universal Editor, which follows a WYSIWYG (What You See Is What You Get) approach for a seamless and consistent user experience with Sites.

## Pre-requisites

* New to Adaptive Forms? Set up your GitHub repository following the provided [tutorial](/help/edge/docs/forms/tutorial.md#add-adaptive-forms-block-to-your-existing-aem-project).
* If you are already using Edge Delivery Services, add the latest version of the [Adaptive Forms block](/help/edge/docs/forms/tutorial.md#) to your GitHub repository. 
* The AEM Forms Author instance includes a template based on Edge Delivery Services. Ensure the [latest version of Core Components](https://github.com/adobe/aem-core-forms-components) is installed in your environment.
* Keep the URL of your AEM Forms as a Cloud Service author instance and your GitHub Repository handy. 

##  Publish Forms for Edge Delivery Services 

To publish forms for Edge Delivery Services, perform the below steps:

[1. Link GitHub Repository to AEM instance](#link-github-repository-to-aem-instance)

[2. Link AEM instance to GitHub Repository](#link-aem-instance-to-github-repository)
  
### Link GitHub Repository to AEM instance

To link [your project on the GitHub Repository](/help/edge/docs/forms/tutorial.md) to the AEM Forms Author instance, perform the following steps: 

1. Go to your GitHub repository that you have created or configured for your Edge Delivery Services.
1. Open the `fstab.yaml` file for editing.
1. Update the `fstab.yaml` file in your GitHub repository with the URL of your AEM Forms as a Cloud Service instance.
   
   ```javascript
    mountpoints:
    /:
        url: [author-instance-url]/bin/franklin.delivery/[Github owner]/[Github Repository]/[Github branch] 
        type: "markup"
        suffix: ".html"
   ```

   For example,if your GitHub repository is named "aemcrosswalk", it's located under the account "wkndform", and you are using the "main" branch, the author instance URL look like the following:

   ```
        mountpoints:
            /:
            url: https://author-p133911-e1313554.adobeaemcloud.com/bin/franklin.delivery/wkndform/aemcrosswalk/main
            type: "markup"
            suffix: ".html"

   ```

1. Commit the changes to the `fstab.yaml` file.
 
### Link AEM instance to GitHub Repository

To link the AEM Forms Author instance to [your project on the GitHub Repository](/help/edge/docs/forms/tutorial.md), perform the following steps:

[1. Create an Adaptive Form based on the Edge Delivery Services template](#1-create-an-adaptive-form-based-on-the-edge-delivery-services-template)

[2. Locate your form's configuration container in AEM author instance](#2-locate-your-forms-configuration-container-in-aem-author-instance)

[3. Author the form in the Universal Editor](#3-author-the-form-in-the-universal-editor)

[4. Publish and preview the form](#4-publish-and-preview-the-form)

#### 1. Create an Adaptive Form based on the Edge Delivery Services template

1. Access your AEM Forms as a Cloud Service author instance.
1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.1.  Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The Wizard opens. In the Source tab, select a Edge Delivery Services based formtemplate:

    ![Create EDS Forms](/help/edge/assets/create-eds-forms.png){width=50%, align-center}

1. Click **[!UICONTROL Create]** and the **Create Form** wizard appears.
1. Specify the **GitHub URL**. For example, if your GitHub repository is named "aemcrosswalk", it's located under the account "wkndform",the URL is:
    `https://github.com/wkndform/aemcrosswalk`
1. Click **[!UICONTROL Create]**.

    ![Create Form wizard](/help/edge/assets/create-form-wizard.png){width=50%, align-center}

    As soon as you click **[!UICONTROL Create]**, the form opens in the Universal editor for authoring.

    ![author the form](/help/edge/assets/author-form.png){width=50%, align-center}

    >[!NOTE]
    >
    > The Edge Delivery Services configuration for the forms based on Edge Delivery Services template is created automatically at the form's configuration container.

#### 2. Locate your form's configuration container in AEM author instance

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** >  **[!UICONTROL Edge Delivery Services Configuration]** on your AEM Forms as a Cloud Service author instance.
1. Select the folder that matches the form's name. For example, if your form is called 'contact-us' choose the folder `forms/contact-us` and selct the configuration and publish the configuration:

    ![Edge Delivery Services Configuration](/help/forms/assets/aem-instance-eds-configuration.png){width=50%, align-center}

1. Click **[!UICONTROL Properties]** to see the configuration.   
    ![Automatically created configuration](/help/edge/assets/aem-forms-create-configuration-github.png){width=50%, align-center}

    You can leave the Edge Host option as it is. The form would be published to both preview (.page) and live (.live) environments. 

1. Click **[!UICONTROL Save and Close]**. The configuration is saved. 

#### 3. Author the form in the Universal Editor

When you click **[!UICONTROL Create]**, the form opens in the Universal Editor for authoring. 

1. Open the Content browser, and navigate to the **[!UICONTROL Adaptive Form]** component in the **Content tree**.

    ![content tree](/help/edge/assets/content-tree.png){width=50%, align-center}

1. Click the **[!UICONTROL Add]** icon and add the desired components from the **Adaptive Form Components** list. 
   
    ![add component](/help/edge/assets/add-component.png){width=50%, align-center}

1. Select the added Adaptive Form component and update its properties using **[!UICONTROL Properties]**.
 
    ![open properties](/help/edge/assets/component-properties.png){width=50%, align-center}

    The below screenshot displays the simple "Contact Us" form authored in the Universal Editor:

    ![contact us form](/help/edge/assets/contact-us.png){width=50%, align-center}

#### 4. Publish and preview the form
    
Now, publish the form to Edge Delivery Services by clicking the **[!UICONTROL Publish]** button in the upper-right corner of the Universal Editor.

![publish form](/help/edge/assets/publish-form.png){width=50%, align-center}


Here's how to access the form on Edge Delivery Services:

* **Staged Version (for testing)**: The staged version displays the unpublished, working version of the form for testing purposes. Use the following URL format to preview the form before it goes live:

    `https://<branch>--<repo>--<owner>.aem.page/content/forms/af/<form_name>`

    For example, if your project's repository is named "aemcrosswalk", it's located under the account "wkndform", and you're using the "main" branch and form as "contact us", the staged version URL look like the following:
    https://main--aemcrosswalk--wkndform.aem.page/content/forms/af/contact-us

* **Live Version (published form)**:   The live version displays the most recently published version of the form, accessible to end users. Use the following URL format to access the published, live version of the form:

    `https://<branch>--<repo>--<owner>.aem.live/content/forms/af/<form_name>`

    For example, if your project's repository is named "aemcrosswalk", it's located under the account "wkndform", and you're using the "main" branch and form as "contact us", the staged version URL look like the following:
    https://main--aemcrosswalk--wkndform.aem.live/content/forms/af/contact-us

The URL structure remains the same for both staged and live versions. However, the content you see differs based on the context:

![View published form](/help/edge/assets/eds-view-publish-form.png){width=50%, align-center}

## Troubleshooting 

Having trouble loading your form? Here are some common issues and how to fix them:

* **Form URL**: Double-check that your form's URL doesn't include the ".html" extension at the end. Edge Deliver Service does not require this extension.

* **AEM Author UR**L: Make sure the AEM Author URL listed in your `fstab.yaml` file is formatted correctly. It should include the following details:

    * The correct GitHub owner
    * The correct repository name
    * The specific branch that you're using for Edge Delivery Services

<!-- * **JSON Display**: If you see only JSON data instead of the actual form, your form block might be outdated. You can update it to the latest version available on https://github.com/adobe-rnd/aem-boilerplate-forms.
-->

## See also

{{see-more-forms-eds}}