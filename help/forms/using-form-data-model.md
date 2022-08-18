---
title: How to Use Form Data Model?
description: Learn how to create Adaptive Forms and Adaptive Form Fragments based on a form data model. Dig deeper by generating and editing sample data for data model objects in the form data model. You can use this data to preview and test Adaptive Forms.
feature: Form Data Model
role: User
level: Beginner, Intermediate
exl-id: 827ce457-6585-46fb-8e28-1d970a40d949
---
# Use Form Data Model {#use-form-data-model}

 ![data-integration](do-not-localize/data-integeration.png)

[!DNL Experience Manager Forms] data integration lets you use disparate backend data sources to create a Form Data Model that you can use as schema in various Adaptive Forms <!--and interactive communications--> workflows. It requires configuring data sources and creating Form Data Model based on data model objects and services available in data sources. For more information, see the following:

* [[!DNL Experience Manager Forms] Data Integration](data-integration.md)
* [Configure data sources](configure-data-sources.md)
* [Create form data model](create-form-data-models.md)
* [Work with form data model](work-with-form-data-model.md)

A Form Data Model is an extension of JSON schema that you can use to:

* [Create Adaptive Forms and fragments](#create-af)
<!--* [Create interactive communications and building blocks like text, list, and condition fragments](#create-ic)-->
* [Preview with sample data](#preview-ic)
* [using Form Data Model service](#prefill)
* [Write submitted Adaptive Form data back into data sources](#write-af)
* [Invoke services using Adaptive Form rules](#invoke-services)

## Create Adaptive Forms and fragments {#create-af}

You can create [Adaptive Forms](creating-adaptive-form.md) and Adaptive Form Fragments <!-- [Adaptive Form Fragments](adaptive-form-fragments.md) --> based on a form data model. Do the following to use a Form Data Model when creating an Adaptive Form or Adaptive Form Fragment:

1. In Form Model tab on Add Properties screen, select **[!UICONTROL Form Data Model]** in the **[!UICONTROL Select From]** drop-down list.

   ![create-af-1-1](assets/create-af-1-1.png)

1. Tap to expand **[!UICONTROL Select Form Data Model]**. All available form data models are listed.

   Select a from data model.

   ![create-af-2-1](assets/create-af-2-1.png)

1. (**Adaptive Form Fragments only**) You can create an Adaptive Form Fragment based on only one data model object in a form data model. Expand **[!UICONTROL Form Data Model Definitions]** drop-down. It lists all data model objects in the specified form data model. Select a data model object from the list.

   ![create-af-3](assets/create-af-3.png)

   Once the Adaptive Form or Adaptive Form Fragment based on a Form Data Model is created, Form Data Model objects appear in the **[!UICONTROL Data Sources]** tab of the Content browser in Adaptive Form editor.

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

Form Data Model editor allows you to generate and edit sample data for data model objects in the form data model. You can use this data to preview and test <!--interactive communications and--> Adaptive Forms. You must generate the sample data before previewing as described in [Work with form data model](work-with-form-data-model.md#sample).

<!--To preview an interactive communication with sample Form Data Model data:

1. On [!DNL  Experience Manager] author instance, navigate to **[!UICONTROL Forms > Forms & Documents]**.
1. Select an interactive communication and tap **[!UICONTROL Preview]** in the toolbar to select **[!UICONTROL Web Channel]**, **[!UICONTROL Print Channel]**, or **[!UICONTROL Both Channels]** to preview the interactive communication.
1. In the Preview [*channel*] dialog, ensure that **[!UICONTROL Test Data of Form Data Model]** is selected and tap **[!UICONTROL Preview]**.

The interactive communication opens with prefilled sample data.

![web-preview](assets/web-preview.png)-->

To preview an Adaptive Form with sample data, open the Adaptive Form in author mode and tap **[!UICONTROL Preview]**.

## Prefill using Form Data Model service {#prefill}

[!DNL Experience Manager Forms] provides out-of-the-box Form Data Model Prefill Service that you can enable for Adaptive Forms <!--and interactive communications--> based on form data model. The prefill service queries data sources for data model objects in the Adaptive Form <!--and interactive communication--> and accordingly prefills data while rendering the form or the communication.

To enable the Form Data Model Prefill Service for an Adaptive Form, open the Adaptive Form Container properties and select **[!UICONTROL Form Data Model Prefill service]** from the **[!UICONTROL Prefill Service]** drop-down in the Basic accordion. Then, save the properties.

![prefill-service](assets/prefill-service.png)

<!--To configure Form Data Model prefill service in an interactive communication, you can select Form Data Model Prefill Service in the Prefill Service drop-down while creating it or later by modifying the properties.

![edit-ic-props](assets/edit-ic-props.png)

Edit Properties dialog for an interactive communication-->

## Write submitted Adaptive Form data into data sources {#write-af}

When a user submits a form based on a form data model, you can configure the form to write submitted data for a data model object to its data sources. To achieve this use case, [!DNL Experience Manager Forms] provide [Form Data Model Submit Action](configuring-submit-actions.md), available out-of-the-box only for Adaptive Forms based on a form data model. It writes submitted data for a data model object in its data source.

To configure the Form Data Model Submit Action, open Adaptive Form Container properties and select **[!UICONTROL Submit using Form Data Model]** from the Submit Action drop-down under the Submission accordion. Then, browse and select a data model object from the **[!UICONTROL Name of the data model object to submit]** drop-down. Save the properties.

On form submission, data for the configured data model object is written to the respective data source.

<!--![data-submission](assets/data-submission.png)-->

You can also submit form attachments to a data source using binary data model object property. Do the following to submit attachments to a JDBC data source:

1. Add a data model object that includes a binary property to the form data model.
1. In the Adaptive Form, drag-drop the **[!UICONTROL File Attachment]** component from the Components browser onto the Adaptive Form.
1. Tap to select the added component and tap ![settings_icon](assets/configure-icon.svg) to open the Properties browser for the component.
1. In the Bind Reference field, tap ![foldersearch_18](assets/folder-search-icon.svg) and navigate to select the binary property you added in the form data model. Configure other properties, as appropriate.

   Tap ![check-button](assets/save_icon.svg) to save the properties. The attachment field is now bound to the binary property of the form data model.

1. In the Submission section of the Adaptive Form Container properties, enable **[!UICONTROL Submit Form Attachments]**. It submits the attachment in the binary property field to the data source on form submission.

## Invoke services in Adaptive Forms using rules {#invoke-services}

In an Adaptive Form based on a form data model, you can [create rules](rule-editor.md) to invoke services configured in the form data model. The **[!UICONTROL Invoke Services]** operation in a rule lists all available services in the Form Data Model and allows you to select input and output fields for the service. You can also use the **[!UICONTROL Set Value]** rule type to invoke a Form Data Model service and set the value of a field to the output returned by the service.

For example, the following rule invokes a get service that takes Employee Id as input and the values returned are populated in the corresponding Dependent Id, Last Name, First Name, and Gender fields in the form.

![invoke-service](assets/invoke-service.png)

In addition, you can use the `guidelib.dataIntegrationUtils.executeOperation` API to write a JavaScript in the code editor for the rule editor. <!-- For API details, see [API to invoke Form Data Model service](invoke-form-data-model-services.md).-->
