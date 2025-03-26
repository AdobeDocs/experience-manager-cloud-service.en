---
title: How can we create Form Data Model (FDM) for an Adaptive Form?
description: Learn to create Adaptive Forms and Fragments based on a form data model(FDM). Generate and edit sample data for data model objects in the FDM.
feature: Adaptive Forms, Form Data Model
role: Admin, User
level: Beginner, Intermediate
exl-id: 827ce457-6585-46fb-8e28-1d970a40d949
---
# Use Form Data Model (FDM) {#use-form-data-model}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/form-data-model/using-form-data-model.html)                  |
| AEM as a Cloud Service     | This article        |


 ![data-integration](do-not-localize/data-integeration.png)

[!DNL Experience Manager Forms] data integration lets you use disparate backend data sources to create a Form Data Model (FDM) that you can use as schema in various Adaptive Forms <!--and interactive communications--> workflows. It requires configuring data sources and creating Form Data Model (FDM) based on data model objects and services available in data sources. For more information, see the following:

* [[!DNL Experience Manager Forms] Data Integration](data-integration.md)
* [Configure data sources](configure-data-sources.md)
* [Create form data model (FDM)](create-form-data-models.md)
* [Work with form data model (FDM)](work-with-form-data-model.md)

A Form Data Model (FDM) is an extension of JSON schema that you can use to:

* [Create Adaptive Forms and fragments](#create-af)
<!--* [Create interactive communications and building blocks like text, list, and condition fragments](#create-ic)-->
* [Preview with sample data](#preview-ic)
* [Using Form Data Model service](#prefill)
* [Write submitted Adaptive Form data back into data sources](#write-af)
* [Invoke services using Adaptive Form rules](#invoke-services)

## Create Adaptive Forms and fragments {#create-af}

You can create [Adaptive Forms](creating-adaptive-form.md) and Adaptive Form Fragments <!-- [Adaptive Form Fragments](adaptive-form-fragments.md) --> based on a form data model (FDM). Do the following to use a Form Data Model (FDM) when creating an Adaptive Form or Adaptive Form Fragment:

1. In Form Model tab on Add Properties screen, select **[!UICONTROL Form Data Model]** in the **[!UICONTROL Select From]** drop-down list.

   ![create-af-1-1](assets/create-af-1-1.png)

2. Select to expand **[!UICONTROL Select Form Data Model]**. All available form data model (FDM) are listed.

   Select a from data model.

   ![create-af-2-1](assets/create-af-2-1.png)

3. (**Adaptive Form Fragments only**) You can create an Adaptive Form Fragment based on only one data model object in a form data model (FDM). Expand **[!UICONTROL Form Data Model Definitions]** drop-down. It lists all data model objects in the specified form data model (FDM). Select a data model object from the list.

   ![create-af-3](assets/create-af-3.png)

   Once the Adaptive Form or Adaptive Form Fragment based on a Form Data Model (FDM) is created, Form Data Model objects appear in the **[!UICONTROL Data Sources]** tab of the Content browser in Adaptive Form editor.

   >[!NOTE]
   >
   >For an Adaptive Form Fragment, only the data model object selected at the time of authoring and its associated data model objects appear in the Data Sources tab.

   ![data-model-objects-tab](assets/data-model-objects-tab.png)

   You can drag-drop data model objects onto the Adaptive Form or fragment to add form fields. The added form fields retain the metadata properties and binding with data model object properties. The binding ensures that the field values are updated in the corresponding data sources on form submission and prefilled when the form is rendered.

<!-- ## Create interactive communications {#create-ic}

You can create an interactive communication based on a Form Data Model that you can use to prefill interactive communication with data from configured data sources. In addition, the building blocks of an interactive communication, such as text, list, and condition document fragments can be based on a form data model.

You can choose a Form Data Model when creating an interactive communication or a document fragment. The following image shows the General tab of the Create Interactive Communication dialog.

![create-ic](assets/create-ic.png)

General tab of Create Interactive Communication dialog

For more information, see:

[Create an interactive communication](create-interactive-communication.md)

[Text in Interactive Communications](texts-interactive-communications.md)

[Conditions in Interactive Communications](conditions-interactive-communications.md)

[List fragments](lists.md) --> 

## Preview with sample data {#preview-ic}

Form Data Model editor lets you generate and edit sample data for data model objects in the form data model (FDM). You can use this data to preview and test <!--interactive communications and--> Adaptive Forms. You must generate the sample data before previewing as described in [Work with form data model](work-with-form-data-model.md#sample).

<!--To preview an interactive communication with sample Form Data Model data:

1. On [!DNL  Experience Manager] author instance, navigate to **[!UICONTROL Forms > Forms & Documents]**.
1. Select an interactive communication and select **[!UICONTROL Preview]** in the toolbar to select **[!UICONTROL Web Channel]**, **[!UICONTROL Print Channel]**, or **[!UICONTROL Both Channels]** to preview the interactive communication.
1. In the Preview [*channel*] dialog, ensure that **[!UICONTROL Test Data of Form Data Model]** is selected and select **[!UICONTROL Preview]**.

The interactive communication opens with prefilled sample data.

![web-preview](assets/web-preview.png)-->

To preview an Adaptive Form with sample data, open the Adaptive Form in author mode and select **[!UICONTROL Preview]**.

## Prefill using Form Data Model service {#prefill}

[!DNL Experience Manager Forms] provides out-of-the-box Form Data Model Prefill Service that you can enable for Adaptive Forms <!--and interactive communications--> based on form data model (FDM). The prefill service queries data sources for data model objects in the Adaptive Form <!--and interactive communication--> and accordingly prefills data while rendering the form or the communication.

To enable the Form Data Model Prefill Service for an Adaptive Form, open the Adaptive Form Container properties and select **[!UICONTROL Form Data Model Prefill service]** from the **[!UICONTROL Prefill Service]** drop-down in the Basic accordion. Then, save the properties.

![prefill-service](assets/prefill-service.png)

<!--To configure Form Data Model prefill service in an interactive communication, you can select Form Data Model Prefill Service in the Prefill Service drop-down while creating it or later by modifying the properties.

![edit-ic-props](assets/edit-ic-props.png)

Edit Properties dialog for an interactive communication-->

## Write submitted Adaptive Form data into data sources {#write-af}

When a user submits a form based on a form data model (FDM), you can configure the form to write submitted data for a data model object to its data sources. To achieve this use case, [!DNL Experience Manager Forms] provide [Form Data Model Submit Action](configuring-submit-actions.md), available out-of-the-box only for Adaptive Forms based on a form data model (FDM). It writes submitted data for a data model object in its data source.

To configure the Form Data Model Submit Action:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the  **[!UICONTROL Submission]** tab. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Submit using Form Data Model]**.

    ![Action configuration](/help/forms/assets/configure-submit-action-invoke-fdm.png)

1. Specify the **[!UICONTROL Data model to submit]**.
1. Click **[!UICONTROL Done]** 

On form submission, data for the configured data model object is written to the respective data source. In addition, you can submit a form attachment using a Form Data Model (FDM) and a Document of Record (DoR) to the data source. For information about form data model (FDM), see [[!DNL AEM Forms] Data Integration](data-integration.md).

<!--![data-submission](assets/data-submission.png)-->

>[!NOTE]
>
> AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md)  article.

You can also submit form attachments to a data source using binary data model object property. Do the following to submit attachments to a JDBC data source:

1. Add a data model object that includes a binary property to the form data model (FDM).
1. In the Adaptive Form, drag-drop the **[!UICONTROL File Attachment]** component from the Components browser onto the Adaptive Form.
1. Select to select the added component and select ![settings_icon](assets/configure-icon.svg) to open the Properties browser for the component.
1. In the Bind Reference field, select ![foldersearch_18](assets/folder-search-icon.svg) and navigate to select the binary property you added in the form data model (FDM). Configure other properties, as appropriate.

   Select ![check-button](assets/save_icon.svg) to save the properties. The attachment field is now bound to the binary property of the form data model (FDM).

1. In the Submission section of the Adaptive Form Container properties, enable **[!UICONTROL Submit Form Attachments]**. It submits the attachment in the binary property field to the data source on form submission.

## Invoke services in Adaptive Forms using rules {#invoke-services}

In an Adaptive Form based on a form data model (FDM), you can [create rules](rule-editor.md) to invoke services configured in the form data model (FDM). The **[!UICONTROL Invoke Services]** operation in a rule lists all available services in the Form Data Model (FDM) and lets you select input and output fields for the service. You can also use the **[!UICONTROL Set Value]** rule type to invoke a Form Data Model service and set the value of a field to the output returned by the service.

For example, the following rule invokes a get service that takes Employee Id as input and the values returned are populated in the corresponding Dependent Id, Last Name, First Name, and Gender fields in the form.

![invoke-service](assets/invoke-service.png)

In addition, you can use the `guidelib.dataIntegrationUtils.executeOperation` API to write a JavaScript in the code editor for the rule editor. <!-- For API details, see [API to invoke Form Data Model service](invoke-form-data-model-services.md).-->

### Invoke a form data model (FDM) using custom functions {#invoke-form-data-model-using-custom-functions}

You can [invoke a form data model from rule editor using custom functions](/help/forms/rule-editor.md#custom-functions-in-rule-editor-custom-functions). To invoke the form data model (FDM) add a form data model to the allowlist. To add a form data model to an allowtlist:

1. Go to Experience Manager web console at `https://server:host/system/console/configMgr`.
1. Locate **[!UICONTROL Adaptive Form-Level Whitelisting of Form Data Model for Service Invocation - Configuration Factory]**.
1. Click ![plus icon](/help/forms/assets/Smock_Add_18_N.svg) icon to add the configuration..
1. Add **[!UICONTROL Content path pattern]** to specify the location of your Adaptive Forms.  By default, the value is `/content/forms/af/(.*)` which includes all the Adaptive Forms. You can also specify the path for a specific Adaptive Form. 
1. Add **[!UICONTROL Form Data Model path pattern]** to specify the location of form data model (FDM). By default, the value is `/content/dams/formsanddocuments-fdm/(.*)` which includes all the Form Data Model (FDM). You can also specify the path for a specific Form Data Model (FDM). 
1. Save the settings. 

The added configuration is saved under the **[!UICONTROL Adaptive Form-Level Whitelisting of Form Data Model for Service Invocation - Configuration Factory]** option.

>[!VIDEO](https://video.tv.adobe.com/v/3423977/adaptive-forms-custom-function-rule-editor)

>[!NOTE]
>
> To invoke a form data model (FDM) from the rule editor using custom functions through an AEM archetype project:
>
>1. [Create a configuration file](https://github.com/adobe/aem-core-forms-components/blob/master/it/config/src/main/content/jcr_root/apps/system/config/com.adobe.aemds.guide.factory.impl.AdaptiveFormFDMConfigurationFactoryImpl~core-components-it.cfg.json).
>1. Set properties of getContentPathPattern and getFormDataModelPathPattern.
>1. Deploy the project. 

## Related Articles

{{af-submit-action}}

