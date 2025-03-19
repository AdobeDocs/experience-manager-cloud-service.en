---
title: How to integrate Form Data Model (FDM) for a form in Universal Editor?
description: Learn to create forms based on a form data model(FDM). Generate and edit sample data for data model objects in the FDM.
feature: Edge Delivery Services, Form Data Model
role: Admin, User
hide: yes
hidefromtoc: yes
exl-id: 9ce51223-57d0-47d8-8868-84b37d4e8e3e
---
# Integrate forms with Form Data Model in Universal Editor

Integrating forms with a Form Data Model (FDM) in Universal Editor allows you to use diverse backend data sources to create a Form Data Model (FDM). You can use the Form Data Model (FDM) as a schema in various form workflows. Configure the data sources and create a Form Data Model (FDM) based on the data model objects and services available in data sources.

## Consideration

* The prefill service for forms in the Universal Editor is currently not supported.

## Prerequistes

Before configuring your form with the Form Data Model in Universal Editor, ensure you have completed the following steps:

* [Configure Data Source](/help/forms/configure-data-sources.md): Set up the data source to connect your form to backend data.
* [Create Form Data Model (FDM)](/help/forms/create-form-data-models.md): Build a data model using data objects and services from the configured data source.
* [Configure Data Model Objects and Services](/help/forms/work-with-form-data-model.md): Map the data model objects and services to ensure smooth data flow between the form and the data source.

## Creating Forms with Form Data Model in Universal Editor

In the Universal Editor, you can create: 
* [Schema-based form](#schema-based-form): A schema-based form uses a data source configured during form creation in the **Data** tab, automatically binding data to form fields.
* [Non-schema-based form](#non-schema-based-form): A non-schema-based form requires you to manually add a data source and bind each field from the content tree. 

![Types of Form in Universal Editor](/help/edge/docs/forms/universal-editor/assets/form-types.png){width="50%" align="center" height="50%"}
 
These methods give you the flexibility to connect data models with forms based on your needs.

### Schema-Based Form

When you create a schema-based form, it is automatically configured with a data source, and the form fields are already linked to the data through data bindings. To create a schema-based form using the Form Creation wizard, perform the following steps:

1.  Log in to your [!DNL Experience Manager Forms] Author instance.
2.  Enter your credentials on the Experience Manager login page. After you are logged in, in the upper-left corner, select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
3.  Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The Wizard opens. In the **Source** tab, select a template:

     ![Edge Delivery Services template](/help/edge/assets/create-eds-forms.png)

    When you select a Edge Delivery Services based template, the **[!UICONTROL Create]** button is enabled. You can go to the **[!UICONTROL Data Source]** or **[!UICONTROL Submission]** tabs to select a data source or submit action.

4. In the **Data** tab, you can select one of the following data models:

    * **Form Data Model (FDM)**: Integrate data model objects and services from data sources into your form. Choose Form Data Model (FDM) if your form requires reading and writing data from multiple sources.

    * **JSON Schema**: Integrate your form with a backend system by associating a JSON schema that defines the data structure. It allows you to add dynamic content using the schema elements. 

        For example, select the created Form Data Model named Pet Form Data Model.

        ![Select Form Data Model](/help/edge/docs/forms/universal-editor/assets/select-petstore-form-data-model.png)


        By default, all fields of the associated JSON schema or Form Data Model (FDM) are automatically selected and converted into corresponding form components, simplifying the authoring process. The wizard also allows you to selectively choose which fields to include in the form using checkboxes.

5. Click **[!UICONTROL Create]** and the **Create Form** wizard appears.
6. Specify the **Name** and **Title**. 
7. Specify the **GitHub URL**. For example, if your GitHub repository is named `edsforms`, it is located under the account `wkndforms`,the URL is:
    `https://github.com/wkndforms/edsforms`
8. Click **[!UICONTROL Create]**.

    ![Create schema based form](/help/edge/docs/forms/universal-editor/assets/create-schema-based-form.png)

    As soon as you click **[!UICONTROL Create]**, the form opens in the Universal editor for authoring. 

    ![author the form](/help/edge/docs/forms/universal-editor/assets/schema-based-form-in-ue.png)

    The form is created using the data elements from the associated data source, with the form fields having preconfigured data binding. 

    ![Automatic Data Binding](/help/edge/docs/forms/universal-editor/assets/schema-based-form-data-binding.png)

    You can now add and [configure the submit action](/help/edge/docs/forms/universal-editor/submit-action.md) for your form.

### Non-Schema-Based Form

When you create a non-schema-based form, no data source is configured. You can edit the form properties later to add a data source and manually configure data bindings for your form fields. Perform the following steps to edit the form properties and add a data source:

1.  Log in to your [!DNL Experience Manager Forms] Author instance.
1.  Enter your credentials on the Experience Manager login page. After you are logged in, in the upper-left corner, select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
1. Select the form for which you want to add data source and click **[!UICONTROL Properties]**.
    ![Open form properties](/help/edge/docs/forms/universal-editor/assets/non-schema-based-edit-properties.png)

    The form properties open.
1. Click to open the **Form Model** tab, and from the **Select From** drop-down menu. You can select one of the following options:

    * **Form Data Model (FDM)**: Create the form using a form data model.
    * **Connector**: Create the form using the Adobe Marketo data source.
    * **Schema**: Create the form using a JSON schema uploaded to AEM Forms.
    * **None**: Create the form from scratch without using any form model.
    
        For example, select the Form Data Model (FDM) 

        ![Select Form Model tab](/help/edge/docs/forms/universal-editor/assets/select-form-model.png)

1. Select the created Form Data Model (FDM) from the drop-down list. For example, select the created Form Data Model named Pet Form Data Model from the drop-down list.
 
    ![Select FDM](/help/edge/docs/forms/universal-editor/assets/select-fdm.png)

    When you select the Form Data Model (FDM), the warning dialog appears. Click **OK** to close the dialog.

    ![Form  Model Wizard](/help/edge/docs/forms/universal-editor/assets/form-model-wizard.png)

1. Click **[!UICONTROL Save & Close]**.
1. Open the form for editing. The form opens in the Universal Editor for authoring.

    ![Non-schema-based form authoring](/help/edge/docs/forms/universal-editor/assets/non-schema-form-authoring.png)

    The form elements present in the associated Form Data Model (FDM) are displayed in the **[!UICONTROL Datasource]** tab of the **[!UICONTROL Content Browser]** in the **Properties Panel**. 

    ![Form Data Source](/help/edge/docs/forms/universal-editor/assets/non-schema-data-source.png)

1. Select the data elements from the **[!UICONTROL Datasource]** tab and click **[!UICONTROL Add]**.

    ![Add data elements](/help/edge/docs/forms/universal-editor/assets/non-schema-add-data-element.png)

    You can also drag-drop these elements to build your Adaptive Form. When you click **[!UICONTROL Add]**, the selected elements from the **[!UICONTROL Datasource]** tab are added to your form, and a tick mark appears in front of the added elements.

    ![Build form](/help/edge/docs/forms/universal-editor/assets/non-schema-form.png)

    You have to manually add data binding to a form element by specifying it in the **Bind Reference** properties of the form element. 
    For example, let’s add a data binding reference to the **Pet Name** text box that is already present in the form:

    ![Manually add data dinding for a form field](/help/edge/docs/forms/universal-editor/assets/non-schema-add-data-binding.png)

   You can now add and [configure the submit action](/help/edge/docs/forms/universal-editor/submit-action.md) for your form.

## See also

{{universal-editor-see-also}}
