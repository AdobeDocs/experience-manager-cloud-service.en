---
title: How to integrate Form Data Model (FDM) for a form in Universal Editor?
description: Learn to create forms based on a form data model(FDM). Generate and edit sample data for data model objects in the FDM.
feature: Edge Delivery Services, Form Data Model
role: Admin, User
exl-id: 9ce51223-57d0-47d8-8868-84b37d4e8e3e
---

# Integrate Forms with Form Data Model (FDM)

Connect your forms to backend data sources using FDM to enable data binding, validation, and submission workflows.

## Prerequisites

Complete these steps before integrating FDM with your forms:

1. **[Configure Data Source](/help/forms/configure-data-sources.md)**: Set up backend connections
2. **[Create Form Data Model](/help/forms/create-form-data-models.md)**: Define data structure and services  
3. **[Configure Data Model Objects](/help/forms/work-with-form-data-model.md)**: Map data relationships

## Considerations

If you do not see the **Data Sources** icon in your Universal Editor interface or **Bind Reference** property in the right property panel, enable the **Data source** extension in the **Extension Manager**.

![Screenshot of the Universal Editor Extension Manager interface showing available extensions including the Data Sources extension that can be enabled for form integration](/help/edge/docs/forms/universal-editor/assets/extension-manager.png)

Refer to the [Extension Manager Feature Highlights](https://developer.adobe.com/uix/docs/extension-manager/feature-highlights/#enablingdisabling-extensions) article to learn how to enable and disable extensions in the Universal Editor.

## Choose Your Form Type

Universal Editor supports two form creation approaches:

| Aspect | Schema-Based Form | Non-Schema-Based Form |
|--------|-------------------|----------------------|
| **Setup Complexity** | Simple (automatic binding) | Manual (field-by-field binding) |
| **Use Case** | New forms with defined data structure | Existing forms or flexible requirements |
| **Data Source** | Required during creation | Can be added later |
| **Binding** | Automatic field binding | Manual binding per field |

![Types of Form in Universal Editor](/help/edge/docs/forms/universal-editor/assets/form-types.png){width="50%" align="center" height="50%"}

## Schema-Based Form

Schema-based forms automatically configure data sources and bind form fields to data. This approach is ideal for new forms with well-defined data structures.

### Create Schema-Based Form

1. **Access Forms Console**
   - Log in to your [!DNL Experience Manager Forms] Author instance
   - Navigate to **[!UICONTROL Adobe Experience Manager]** > **[!UICONTROL Forms]** > **[!UICONTROL Forms & Documents]**

2. **Start Form Creation**
   - Select **[!UICONTROL Create]** > **[!UICONTROL Adaptive Forms]**
   - Choose an Edge Delivery Services template
   - Click **[!UICONTROL Create]** when enabled

   ![Edge Delivery Services template](/help/edge/assets/create-eds-forms.png)

3. **Configure Data Model**
   - Go to the **Data** tab
   - Select **Form Data Model (FDM)** for multiple data sources or **JSON Schema** for single backend system
   - Choose your created FDM (e.g., Pet Form Data Model)

   ![Select Form Data Model](/help/edge/docs/forms/universal-editor/assets/select-petstore-form-data-model.png)

4. **Complete Form Setup**
   - Enter **Name** and **Title**
   - Specify **GitHub URL** (e.g., `https://github.com/wkndforms/edsforms`)
   - Click **[!UICONTROL Create]**

   ![Create schema based form](/help/edge/docs/forms/universal-editor/assets/create-schema-based-form.png)

### Verify Schema-Based Form

The form opens in Universal Editor with pre-configured data binding:

![Screenshot of the Universal Editor showing a schema-based form with pre-populated form fields and the Content Browser displaying available data source elements](/help/edge/docs/forms/universal-editor/assets/schema-based-form-in-ue.png)

![Automatic Data Binding](/help/edge/docs/forms/universal-editor/assets/schema-based-form-data-binding.png)

## Non-Schema-Based Form

Non-schema forms require manual data source configuration and field binding. This approach offers flexibility for existing forms or complex requirements.

### Create Non-Schema-Based Form

1. **Access Form Properties**
   - Log in to your [!DNL Experience Manager Forms] Author instance
   - Navigate to **[!UICONTROL Adobe Experience Manager]** > **[!UICONTROL Forms]** > **[!UICONTROL Forms & Documents]**
   - Select your form and click **[!UICONTROL Properties]**

   ![Open form properties](/help/edge/docs/forms/universal-editor/assets/non-schema-based-edit-properties.png)

2. **Configure Form Model**
   - Open the **Form Model** tab
   - Select **Form Data Model (FDM)** from the **Select From** dropdown
   - Choose your FDM from the list

   ![Select Form Model tab](/help/edge/docs/forms/universal-editor/assets/select-form-model.png)

   ![Select FDM](/help/edge/docs/forms/universal-editor/assets/select-fdm.png)

3. **Confirm Configuration**
   - Click **OK** in the warning dialog
   - Click **[!UICONTROL Save & Close]**

   ![Form  Model Wizard](/help/edge/docs/forms/universal-editor/assets/form-model-wizard.png)

### Add Data Elements

1. **Open Form for Editing**
   - The form opens in Universal Editor

   ![Non-schema-based form authoring](/help/edge/docs/forms/universal-editor/assets/non-schema-form-authoring.png)

2. **Access Data Source Elements**
   - Go to the **[!UICONTROL Datasource]** tab in the **[!UICONTROL Content Browser]**
   - View available data elements from your FDM

   ![Form Data Source](/help/edge/docs/forms/universal-editor/assets/non-schema-data-source.png)

3. **Add Elements to Form**
   - Select data elements and click **[!UICONTROL Add]**
   - Or drag-drop elements to build your form

   ![Add data elements](/help/edge/docs/forms/universal-editor/assets/non-schema-add-data-element.png)

   ![Screenshot showing the Universal Editor with a non-schema form being built by dragging and dropping data elements from the Data Source tab into the form structure](/help/edge/docs/forms/universal-editor/assets/non-schema-form.png)

### Add Manual Data Binding

For existing form fields, add data binding through the **Bind Reference** property:

1. **Open Field Properties**
   - Select the form field for binding
   - Open its properties panel

2. **Configure Bind Reference**
   - Go to the **Bind Reference** property
   - Click the **Browse** icon

   ![Manually add data dinding for a form field](/help/edge/docs/forms/universal-editor/assets/non-schema-add-data-binding.png)

3. **Select Data Element**
   - Choose from the data source tree in the **Select a Bind Reference** wizard
   - Select the desired data element and click **Select**

   ![select data bind refernce](/help/edge/docs/forms/universal-editor/assets/select-bind-reference.png)

   ![select data element](/help/edge/docs/forms/universal-editor/assets/select-data-element.png)

4. **Verify Binding**
   - The form field now binds to the data element
   - The binding appears in the **Bind Reference** property

   ![Automatic Data Binding](/help/edge/docs/forms/universal-editor/assets/schema-based-form-data-binding.png)

## Verify Integration

After completing the integration:

1. **Test data binding**: Verify form fields display correct data
2. **Validate submissions**: Ensure data saves to configured sources
3. **Check error handling**: Test with invalid data scenarios

## Next Steps

Configure [submit actions](/help/edge/docs/forms/universal-editor/submit-action.md) to complete your form workflow.
