---
title: How to integrate Form Data Model (FDM) for a form with Adaptive Form?
description: Learn to create forms based on a form data model(FDM). Generate and edit sample data for data model objects in the FDM.
feature: Edge Delivery Services, Adaptive Forms, Form Data Model
role: Admin, User
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: f08fb365-8750-4b81-9877-c382e7aebba0
---
# Integrate forms with Form Data Model

Integrating forms with a Form Data Model (FDM) allows you to use diverse backend data sources to create a Form Data Model (FDM). You can use the Form Data Model (FDM) as a schema in various form workflows. Configure the data sources and create a Form Data Model (FDM) based on the data model objects and services available in data sources.

## Advantages of Integrating Forms with Form Data Model (FDM)

* **Seamless Backend Connectivity**: Connect forms to various backend systems (e.g., databases, REST APIs, SOAP services, CRMs) without custom code. This enables real-time data exchange and reduces integration effort.
* **Centralized Data Schema** The Form Data Model serves as a unified data schema that simplifies mapping and management of data objects and services used across multiple forms and workflows.

* **Improved Form Prefill and Submission**: Easily configure prefill and submission actions using Form Data services, ensuring accurate and up-to-date data retrieval and storage.

* **Support for Dynamic Workflows**: Form Data Model can be integrated with workflows to automate business processes based on submitted or retrieved data, enhancing overall efficiency.

## Prerequistes

Before configuring your form with the Form Data Model, ensure you have completed the following steps:

* [Configure Data Source](/help/forms/configure-data-sources.md): Set up the data source to connect your form to backend data.
* [Create Form Data Model (FDM)](/help/forms/create-form-data-models.md): Build a data model using data objects and services from the configured data source.
* [Configure Data Model Objects and Services](/help/forms/work-with-form-data-model.md): Map the data model objects and services to ensure smooth data flow between the form and the data source.

>[!BEGINTABS]

>[!TAB Foundation Component]

Perform the following steps to configure Form Data Model with Adaptive Form based on Foundation Component as:

1. Open the Adaptive Form for editing and navigate to **[!UICONTROL Submission]** section of the Adaptive Form Container properties. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Submit Using Form Data Model]**.

    ![submit using Form Data Model](/help/forms/assets/submit-uisng-fdm-fc.png)

1. Select the created **[!UICONTROL Data Model to submit]** configuration.
   To submit attachments to the database select **Submit form attachments**. The Document of Recore (DoR) is saved in database by selecting **Submit Document of Record**.
1. Click **[!UICONTROL Save]** to save the Submit settings.

>[!TAB Core Component]

Perform the following steps to configure Form Data Model with Adaptive Form based on Core Component as:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the  **[!UICONTROL Submission]** tab. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[Submit Using Form Data Model]**.

    ![submit using Form Data Model](/help/forms/assets/submit-uisng-fdm-cc.png)

1. Select the created **[!UICONTROL Data Model to submit]** configuration.
   To submit attachments to the database select **Submit form attachments**. The Document of Recore (DoR) is saved in database by selecting **Submit Document of Record**.
1. Click **[!UICONTROL Save]** to save the Submit settings.

>[!TAB Universal Editor]

Perform the following steps to configure Form Data Model with Adaptive Form authored in Universal as:

1. Open the Adaptive Form for editing.
1. Click the **Edit Form Properties** extension on the editor. 

    The **Form Properties** dialog appears.
    
    >[!NOTE]
    >
    > * If you do not see the **Edit Form Properties** icon in your Universal Editor interface, enable the **Edit Form Properties** extension in the Extension Manager. 
    > * Refer to the [Extension Manager Feature Highlights](https://developer.adobe.com/uix/docs/extension-manager/feature-highlights/#enablingdisabling-extensions) article to learn how to enable or disable extensions in the Universal Editor.

1. Click **Submission** tab and select **[!UICONTROL Submit using Form Data Model]**.

    ![OneDrive GIF](/help/forms/assets/submit-uisng-fdm-ue.png)
    If you select **Save Attachments with Original Name**, the attachments are stored in the folder using their original filenames. You can also save Document of Record (DoR) in the Azure Blob Storage.

1. Select the **[!UICONTROL Storage Configuration]**, where you want to save your data.
1. Click **[!UICONTROL Save&Close]**

For detailed instructions on how to integrate forms authored in the Universal Editor, refer to the article [Integrate Forms with Form Data Model in Universal Editor](/help/edge/docs/forms/universal-editor/integrate-forms-with-data-source.md). 

>[!ENDTABS]

## Related Articles

{{af-submit-action}}
