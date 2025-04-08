---
title: How to create an Adaptive Form based on Core Components?
description: Learn how to create an Adaptive Form using [!DNL Experience Manager Forms]. Adaptive Forms are responsive HTML5 forms that streamline information gathering and processing. Dig deeper on how to create an Adaptive Form based on a Form Data Model (FDM) and XML or JSON schema.
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner
exl-id: 1e812d93-4ba5-4589-b59b-2f564d754b0f
---
# Create an Adaptive Form (Core Components) {#creating-an-adaptive-form-core-components}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-core-components/create-an-adaptive-form-core-components.html)                |
| AEM as a Cloud Service     | This article        |


Adaptive Forms let you create forms that are engaging, responsive, dynamic, and adaptive. AEM Forms provides business user-friendly wizard to quickly create Adaptive Forms. The wizard has a quick tab navigation to easily select pre-configured template, styling, fields, and submission options to create an Adaptive Form. 

Before you start, learn about the type of Forms components available to you: 

*   [Adaptive Forms Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html?lang=en): These are standardized data capture components. These components provide customization capabilities, reduced development time, and lower maintenance costs for your digital enrollment experiences. A developer can easily customize and style these components. Adobe recommends using these modern and extensible components to develop Adaptive Forms.  

*   [Adaptive Forms Foundation Components](creating-adaptive-form.md): These are classic (old) data capture components. You can continue to use these to edit your existing foundation components based Adaptive Form. If you are creating new forms, Adobe recommends using  [Adaptive Forms Core Components](creating-adaptive-form-core-components.md) to create an Adaptive Forms. 

![Wizard to create an Adaptive Form](/help/release-notes/assets/wizard.png)


## Pre-requisites

You require the following to create an Adaptive Form:

*   **Enable Adaptive Forms Core Components for your environment**: When you create a program, the Adaptive Forms Core Components already enabled for your environment. If you have a Forms as a Cloud Service environment based on Archetype 39 or earlier, [Enable Adaptive Forms Core Components for your environment](enable-adaptive-forms-core-components.md). On enabling the Core Components for your environment, the **Adaptive Forms (Core Component)** templates and themes are added to your environment. If your AEM SDK version older than 2023.02.0, [ensure that you have `prerelease` flag enabled on your environment](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html?lang=en#new-features) as Adaptive Forms Core Components were part of pre-prelease before the 2023.02.0 release.   

*   **An Adaptive Form template**: A template provides a basic structure and defines appearance (layouts and styles) of an Adaptive Form. It has pre-formatted components containing certain properties and content structure. It also provides the options to define a theme and a submit action. The theme defines the look and feel and submit action defines the action to take on submission of an Adaptive Form. For example, sending the collected data to a data source. The cloud service provides an OOTB template, named blank:

    * The `blank` template is included with every fresh AEM Forms as a Cloud Service program.
    * You can install the reference package, via Package Manager, to add the `blank` template to your AEM Forms as a Cloud Service program. 
    * You can also [create an Adaptive Forms template (Core Components)](/help/forms/template-editor-core-components.md) from scratch.
    * You can also deploy [sample templates](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/sample-themes-templates-form-data-models-core-components.html) to your environment. These help you start creating forms swiftly.

*   **An Adaptive Form theme**: A theme contains styling details for the components and panels. Styles include properties such as background colors, state colors, transparency, alignment, and size. When you apply a theme, the specified style reflects on the corresponding components.  The `Canvas` template is included with every fresh AEM Forms as a Cloud Service program. You can also deploy [sample themes](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/sample-themes-templates-form-data-models-core-components.html) to your environment. These help you start styling your forms and provide a base structure to create or customize a theme as per your business requirements.

    <!-- * You can install the reference package, via package manager, to add the `Canvas` template to your AEM Forms as a Cloud Service program.
    * You can also [create an Adaptive Forms theme (Core Components)](template-editor.md) and deploy it to your AEM Forms as a Cloud Service program. --> 

*   **Permissions**: Add your users to [!DNL forms-users] group. The members of the [!DNL forms-users] group have permissions to create an Adaptive Form. For detailed list of forms-specific user groups, see [Groups and permissions](forms-groups-privileges-tasks.md).

<!--
>[!NOTE]
>
>
> In addition to the given themes and templates when you enable Core Components, you can also deploy the latest out-of-the box [sample themes and templates](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/sample-themes-templates-form-data-models-core-components.html) to your AEM environment for use in Core Components based Adaptive Forms.
-->

## Create an Adaptive Form  {#create-an-adaptive-form-core-components}

1.  Log in to your [!DNL Experience Manager Forms] Author instance. It can be a Cloud instance or a local development instance.

1.  Enter your credentials on the Experience Manager login page. After you are logged in, in the upper-left corner, select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

1.  Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The Wizard opens. In the Source tab, select a template:

    ![Core Components Template](/help/forms/assets/core-components-template.png)

    When you select a template, a theme and submit action specified in the template are auto-selected, and the **[!UICONTROL Create]** button is enabled. You can go to the **[!UICONTROL Style]** or **[!UICONTROL Submission]** tabs to select a different theme or submit action. If the selected template does not specify a theme, the create button remains disabled. You can go to the **[!UICONTROL Styles]** tab to manually select a theme.

    >[!NOTE]
    >
    >
    > If you do not have, **Adaptive Forms (Core Component)** template on your environment, [Enable Adaptive Forms Core Components for your environment](setup-local-development-environment.md#enable-adaptive-forms-core-components-for-an-existing-aem-archetype-based-project). On enabling the Core Components for your environment, the **Adaptive Forms (Core Component)** template is added to your environment.  

1.  In the **[!UICONTROL Style]** tab, select a theme:

    *   When the selected template specifies a theme, the theme is auto selected in the wizard. You can also choose a different theme from the Style tab.
    
    *   If the selected template does not specify a theme, you can use the Style tab to choose a theme. The **[!UICONTROL Create]** button is enabled only after a theme is selected. 

1.  (Optional) In the Data Tab, select a data model:

    *   **Form data model (FDM)**: A [Form Data Model](data-integration.md) lets you integrate entities and services from disparate data sources to an Adaptive Form. Choose Form Data Model (FDM) if the Adaptive Form that you are creating involves fetching and write data from and to multiple data source.
    
    *   **JSON Schema**: [JSON schema](adaptive-form-json-schema-form-model.md) Our Core-Components-based Adaptive Form allows for seamless integration with your organization's back-end system by providing the ability to associate a JSON schema, which represents the structure of the data being produced or consumed. This association enables authors to dynamically add content to the Adaptive Form using the elements of the schema. The elements of the schema are easily accessible in the Data Model Objects tab of the Content browser during the authoring process, and all fields are automatically added to any created Adaptive Form.

    By default all fields of the associated JSON schema are automatically selected and converted into corresponding Adaptive Form components, streamlining the authoring process. The wizard offers the added convenience of allowing you to selectively choose which fields should be included in the Adaptive Form through the use of checkboxes. 

1.  In the **[!UICONTROL Submission]** tab, select a submit action:

    *   When you select a template, the submit action specified in the template is auto-selected. You can select a different submit action from the Submission tab. The **[!UICONTROL  Submission]** tab displays all the available submit actions. 
    
    *   When the selected template does not specify a submit action, you can use the **[!UICONTROL Submission]** tab to select a submit action

1.  (Optional) In the **[!UICONTROL Delivery]** tab, you can specify a publishing or unpublishing date for an Adaptive Form. 
   
1.  Select **[!UICONTROL Create]**. A dialog to specify title, name, and location to save the Adaptive Form appears:

    * **[!UICONTROL Title]** Specifies the display name of the form. The title helps you identify the form in the [!DNL Experience Manager Forms] user interface.
    * **[!UICONTROL Name:]** Specifies the name of the form. A node with the specified name is created in the repository. As you start typing a title, value for the name field is automatically generated. You can change the suggested value. The name field can include only alphanumeric characters, hyphens, and underscores. All the invalid inputs are replaced with a hyphen.
    * **[!UICONTROL Path:]** Specifies the location at which the Adaptive Form is to be saved. You can save the Adaptive Form directly at `/content/dam/formsanddocuments` or create a folder such as `/content/dam/formsanddocuments/adaptiveforms` to save an Adaptive Form. Ensure that you create the folder before using it in the path. The **[!UICONTROL Path]** field does not create a folder automatically. 

1.  Select **[!UICONTROL Create]**. An Adaptive Form is created and opens in the Adaptive Forms editor. The editor displays the contents available in the template.  Based on the type of Adaptive Form, the form elements present in the associated <!--XFA form template, XML schema or --> JSON schema or Form Data Model (FDM) are displayed in the **[!UICONTROL Data Model Objects]** tab of the **[!UICONTROL Content Browser]** in the sidebar. You can also drag-drop these elements to build your Adaptive Form.

Now, you can drag-and-drop the [Adaptive Forms Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html) to Adaptive Forms container to design and create the form. You can also visit [https://aemcomponents.dev/](https://aemcomponents.dev/) to view available core components in action.

>[!NOTE]
>
> You can also [create Adaptive Forms using XFA form templates (*.XDP files)](/help/forms/create-adaptive-form-using-xfa-templates.md). It enables you to save time by reusing fields from XDP files directly in Adaptive Forms.

## Configure Submit Action for an Adaptive Form {#configure-submit-action-for-form}

A Submit Action lets you choose the destination of data captured via an Adaptive Form. It is triggered when a user clicks the Submit button on an Adaptive Form. Adaptive forms include some out of the box submit actions. You can also extend a default submit actions to create your own custom submit action. To configure a Submit Action for your form:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 

1. Click the  **[!UICONTROL Submission]** tab. 

    ![Click the Wrench icon to open Adaptive Form Container dialog box to configure a submit action](/help/forms/assets/adaptive-forms-submit-message.png)

1. Select and configure a **[!UICONTROL Submit action]**, based on your requirements. For detailed information about Submit Actions, see [Adaptive Form Submit Action](/help/forms/configuring-submit-actions.md)

<!--
    
    ![Click the Wrench icon to open Adaptive Form Container dialog box to configure Data Models for the Adaptive Form Container component](/help/forms/assets/adaptive-forms-container.png)

-->

## Redirect the user to a page or show a thank you message on form submission

On submission of a form, you can redirect the user to another webpage or a message. To redirect the user or configure the thank you message:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens.  
1. Open the **[!UICONTROL Submission]** tab. 

    ![Click the Wrench icon to open Adaptive Form Container dialog box to configure a redirect page or thank you message](/help/forms/assets/adaptive-forms-redirect-message.png)

    * To configure a Redirect URL, for on Submit option, select the **[!UICONTROL Redirect to URL]** option, and browse and select an AEM Sites page, or provide URL of an external page.  
  
    * To configure a custom or thank you message, for on Submit option, select the **[!UICONTROL Show Message]** option, and provide a message in the **[!UICONTROL Message content]** box. It is a rich text box, you can use the full screen option to view all the available rich text items. 

## Configure a Schema or Form Data Model (FDM) for an Adaptive Form{#configure-schema-or-data-model-for-form}

You can use the Form Data Model (FDM) to connect a form to a Data Source to send and receive data based on user actions. You can also connect a form to a JSON schema to receive the submitted data in a pre-defined format. Based on the requirement, connect your form to a JSON schema or Form data model (FDM):

* [Create a JSON Schema and upload to your environment](/help/forms/adaptive-form-json-schema-form-model.md)  
* [Create a Form Data Model (FDM)](/help/forms/create-form-data-models.md) 

### Configure a JSON Schema or Form Data Model (FDM) for your form

To configure a JSON Schema or Form Data Model (FDM) for your form:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Open the **[!UICONTROL Data Model]** tab. 
    
    ![Click the Wrench icon to open Adaptive Form Container dialog box to configure a JSON schema or form data model (FDM)](/help/forms/assets/adaptive-forms-select-form-data-model-or-json-schema.png)

1. Select and configure a JSON Schema or Form Data Model (FDM), based on your requirements: 

    * When you select the **[!UICONTROL Form Model]** option, use the **[!UICONTROL Select Form Data Model]** option to select a pre-configured Form Data Model (FDM).
    * When you select the **[!UICONTROL Schema]** option, use the **[!UICONTROL Schema]** option to select a JSON schema for your form.

1. Click **[!UICONTROL Done]**.

## Configure a pre-fill service  {#configure-prefill-service-for-form}

You can use the prefill service to auto fill fields of an Adaptive Form using existing data. When a user opens a form, the values for those fields are prefilled. You can:

* [Create a custom pre-fill service](/help/forms/prepopulate-adaptive-form-fields.md)
* [Use Form Data Model Prefill service](#fdm-prefill-service)

### Use Form Data Model Prefill service to prepopulate fields of an Adaptive Form {#fdm-prefill-service}

You can use the Form Data Model Prefill service to prepopulate fields of an Adaptive Form using a Form Data Model or a custom pre-fill service. The Form Data Model Prefill service uses the [Get Service of configured Form Data Model](work-with-form-data-model.md#add-data-model-objects-and-services-add-data-model-objects-and-services) to retrieve data. To use Form Data Model Prefill service for an Adaptive Form:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the Adaptive Form Container properties ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box to configure Data Models opens. 
![Click the Wrench icon to open Adaptive Form Container dialog box to configure a redirect page or thank you message](/help/forms/assets/adaptive-forms-container-prefill-service.png)
1. Select a form data model (FDM). Open the **[!UICONTROL Basic]** tab. In the prefill service, select **[!UICONTROL Form Data Model Prefill Service]**. 
1. Click **[!UICONTROL Done]**. Your Adaptive form is now configured to use Form Data Model Prefill. You can now, use the [rule editor](rule-editor.md) to create rules to prepopulate fields of the form.

## Edit Form Model properties of an Adaptive Form {#edit-form-model}

1.  Select the Adaptive Form and select ![Page information](/help/forms/assets/Smock_Properties_18_N.svg) > **[!UICONTROL Open Properties]**. The Form Properties page opens. 

1. Go to the **[!UICONTROL Form Model]** tab and choose a form model. If the Adaptive Form is without a form model, you have the freedom to choose either a JSON schema or a form data model (FDM). On the other hand, if the Adaptive Form is already based on a form model, you have the option to switch to another form model of the same type. For instance, if the form is using a JSON schema, you can easily switch to another JSON schema, and similarly if the form is using a Form Data Model (FDM), you can switch to another Form Data Model (FDM). 

1. Select **[!UICONTROL Save]** to save the properties.


## How to rename an AEM Adaptive Form ? {#rename-an-AEM-Adaptive-Form}

To rename an adaptive form, perform the following steps:

1. Select an adaptive form in your AEM Forms user interface.
1. Click on the **Properties** located on the upper rail. 
1. Change the name of the form in the **Title** tab, as shown in the image below.
1. Click **Save and Close**.

![Rename an AEM Adaptive Form](/help/forms/assets/change-af-name.png)

<!--

## See next

* [Create style or themes for your forms](using-themes-in-core-components.md)
* [Add dynamic behavior to forms using the rule editor](rule-editor.md)
* [Set layout of forms for different screen sizes and device types](/help/sites-cloud/authoring/page-editor/responsive-layout.md)
* [Sample themes templates and form data models](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/sample-themes-templates-form-data-models-core-components.html)

-->

## See Also {#see-also}

{{see-also}}
* [Add dynamic behavior to forms using the rule editor](/help/forms/rule-editor-core-components.md)
* [Set layout of forms for different screen sizes and device types](/help/sites-cloud/authoring/page-editor/responsive-layout.md)

