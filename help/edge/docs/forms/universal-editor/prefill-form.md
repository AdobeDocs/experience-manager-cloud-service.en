---
title: How to prefill Adaptive Form fields
description: Use existing data to prefill fields of an Adaptive Form. Users can prefill basic information in a form by logging in with their social profiles.
feature: Adaptive Forms, Edge Delivery Services
role: User, Developer
level: Beginner, Intermediate
time: 45-60 minutes
keywords: prefill adaptive form, adaptive forms edge delivery services, adaptive form autofill
exl-id: 7b6224e2-a19c-4146-8545-0ce9d1da9b29
---
# Configuring Prefill Service in Adaptive Forms using Edge Delivery Services

Form prefilling is the process of automatically populating form fields with relevant data from external sources as soon as a user opens the form. By leveraging information from user profiles, databases, saved drafts, or other backend systems, prefilling streamlines the form-filling experience—reducing manual input, minimizing errors, and accelerating completion. This not only enhances user satisfaction but also increases the likelihood of successful form submissions.

## Benefits of Form Prefilling

| Benefit | Description |
|---------|-------------|
| **Faster Completion** | Reduces manual data entry, helping users complete forms quickly |
| **Improved User Experience** | Forms feel more personalized and convenient, especially for returning users |
| **Higher Conversion Rates** | Reduces form abandonment by minimizing required user effort |
| **Reduced Input Errors** | Data from trusted sources decreases typos and incorrect entries |
| **Better Data Quality** | Ensures structured, accurate, and consistent data for backend systems |

## How Prefilling Works

The following diagram illustrates the automatic prefill process that occurs when a user opens an Adaptive Form:

![Form Prefilling Process Flow](/help/edge/docs/forms/universal-editor/assets/prefill-process-flow.svg)

The prefill process involves four key steps:

1. **User Opens Form**: User accesses an Adaptive Form through a URL or navigation
1. **Identify Data Source**: Prefill service determines the configured data source (Form Data Model or Draft service)
1. **Retrieve Data**: System fetches relevant user data based on context, parameters, or user identification
1. **Map and Display**: Data is mapped to form fields using `bindRef` properties and the populated form is displayed to the user

This automated process ensures users see a form pre-populated with their relevant information, significantly improving the user experience and form completion rates.

## Data Structure for Prefilling

Adaptive Forms support two types of fields:

- **Bound fields**: Fields connected to a data source with a non-empty `bindRef` property
- **Unbound fields**: Standalone fields with empty `bindRef` values

The prefill data structure includes:

- **afBoundData**: Contains data for bound fields and panels
- **afUnBoundData**: Contains data for unbound fields

The data format must match your form model:

- **XFA forms**: XML compliant with XFA template schema
- **XML schema forms**: XML matching the schema structure  
- **JSON schema forms**: JSON compliant with the schema
- **Form Data Model (FDM) forms**: JSON matching the FDM structure
- **Schema-less forms**: All fields are unbound and use unbound XML

## Prerequisites

Before configuring prefill services, ensure you have:

### Required Setup

- [GitHub repository configured for Edge Delivery Services](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#create-a-new-aem-project-pre-configured-with-adaptive-forms-block)
- [Adaptive Forms Block added to your project](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#add-adaptive-forms-block-to-your-existing-aem-project)
- [Data source configured](/help/forms/configure-data-sources.md)
- [Form Data Model (FDM) created](/help/forms/create-form-data-models.md)

### Access Requirements

- Access to AEM Forms as a Cloud Service
- Permissions to create and edit forms
- Universal Editor access with required extensions enabled

>[!TIP]
>
> You can also edit forms to integrate Form Data Model (FDM) in the Universal Editor to fetch data from various backend sources. For details, refer to the [Integrate forms with Form Data Model in Universal Editor](/help/edge/docs/forms/universal-editor/integrate-forms-with-data-source.md) article.

## Prefill Service Options

The Universal Editor provides two prefill service options:

| Service Type | Purpose | Data Source | Best For |
|--------------|---------|-------------|----------|
| **Form Portal Draft Prefill** | Resumes partially completed forms | Saved drafts in Forms Portal | Continuing incomplete applications |
| **Form Data Model Prefill** | Populates fields from external systems | Backend databases via FDM | Auto-filling user profile data |

### Detailed Comparison

| Feature | Draft Prefill Service | FDM Prefill Service |
|---------|----------------------|---------------------|
| **Authentication** | Requires user login for draft access | Configurable based on data source |
| **Setup Complexity** | Minimal configuration | Requires FDM setup and mapping |
| **Data Type** | Static saved data | Real-time dynamic data |
| **Use Case** | Resume saved applications | Prefill from user profiles or databases |


## Configure Prefill Service for a Form

+++Phase 1: Setting Up Form Data Model

### Step 1: Create Form Data Model

1. Log in to your AEM Forms as a Cloud Service instance
1. Navigate to **Adobe Experience Manager** > **Forms** > **Data Integrations**
1. Select **Create** > **Form Data Model**
1. Choose your **Data Source Configuration** and select the configured **Data Source**

   ![Created Form Data Model](/help/edge/docs/forms/universal-editor/assets/create-fdm.png)

   >[!TIP]
   >
   >For detailed instructions on creating Form Data Models, see [Create Form Data Model](/help/forms/create-form-data-models.md).

### Step 2: Configure FDM Services

1. Go to **Adobe Experience Manager** > **Forms** > **Data Integrations**
1. Open your Form Data Model in edit mode
1. Select a data model object and click **Edit Properties**
1. Configure **Read** and **Write** services for the selected data model objects

   ![Configure read write service](/help/edge/docs/forms/universal-editor/assets/configure-reda-write-service.png)

1. Configure service arguments:

   - Click the edit icon for the read service argument
   - Bind the argument to a **User Profile Attribute**, **Request Attribute**, or **Literal value**
   - Specify the binding value (e.g., `petid` for a pet registration form)

   ![Configure pet id argument](/help/edge/docs/forms/universal-editor/assets/pet-id-arguments.png)

1. Click **Done** to save the argument and **Save** to save the FDM

   >[!NOTE]
   >
   > Learn more about configuring FDM services in [Work with Form Data Model (FDM)](/help/forms/work-with-form-data-model.md).

+++

+++Phase 2: Creating and Configuring the Adaptive Form

### Step 3: Create an Adaptive Form

1. Navigate to **Adobe Experience Manager** > **Forms** > **Forms & Documents**
1. Select **Create** > **Adaptive Forms**
1. In the **Source** tab, select an Edge Delivery Services template:

   ![Edge Delivery Services template](/help/edge/assets/create-eds-forms.png)

1. Click **Create** to open the **Create Form** wizard

   >[!NOTE]
   >
   > You can configure the data source from the **Data** tab or later by editing the form properties. 

1. Specify the form details:

   - **Name**: Enter a descriptive name for your form
   - **Title**: Provide a user-friendly title
   - **GitHub URL**: Enter your repository URL (e.g., `https://github.com/wkndforms/edsforms`)

1. Click **Create**

   ![Create schema based form](/help/edge/docs/forms/universal-editor/assets/create-schema-based-form1.png)

The form opens in the Universal Editor for authoring.

### Step 4: Configure Form Data Source
  
1. Select your form and click **Properties**

   ![Select Form Properties](/help/edge/docs/forms/universal-editor/assets/select-form-properties1.png)
        
2. Open the **Form Model** tab
3. From the **Select From** dropdown, choose **Form Data Model (FDM)**
4. Select your created Form Data Model (e.g., PetFDM) from the dropdown
 
   ![Select Form Model tab](/help/edge/docs/forms/universal-editor/assets/select-form-model1.png)
   
5. Click **Save & Close**
6. Open the form for editing in Universal Editor

The form elements from your FDM appear in the **Datasource** tab of the **Content Browser**.

### Step 5: Add Data Binding to Form Fields

1. Select data elements from the **Datasource** tab
2. Click **Add** or drag-and-drop elements to build your form

   ![Screenshot of Universal Editor showing schema-based form](/help/edge/docs/forms/universal-editor/assets/ue-form.png)

3. Add data binding to form fields:

   - Select a form field
   - In the **Properties** panel, find the **Bind Reference** property
   - Select the appropriate data binding reference

     ![Data Binding](/help/edge/docs/forms/universal-editor/assets/schema-based-form-data-binding1.png)

+++

+++Phase 3: Configuring Prefill Service

### Step 6: Enable Required Extensions

Ensure these extensions are enabled in Universal Editor:

1. **AEM Form Properties Extension**

   - Open **Extension Manager** in Universal Editor
   - Enable the **AEM Form Properties** extension

   ![Form properties icon](/help/edge/docs/forms/universal-editor/assets/form-edit-properties.png)

1. **Data Source Extension**

   - Enable the **Data source** extension if you don't see the **Data Sources** icon

   ![Screenshot of Universal Editor Extension Manager](/help/edge/docs/forms/universal-editor/assets/extension-manager.png)

   >[!TIP]
   >
   > For detailed instructions on managing extensions, see [Extension Manager Feature Highlights](https://developer.adobe.com/uix/docs/extension-manager/feature-highlights/#enablingdisabling-extensions).

### Step 7: Configure Prefill Service

1. Open your Adaptive Form in Universal Editor
2. Click the **AEM Form Properties** extension icon

   ![Select Form Properties Icon](/help/edge/docs/forms/universal-editor/assets/select-fdm-properties-icon.png)

3. Click the **Prefill** tab
4. Select **Form Data Model Prefill Service**

   ![Select Prefill service](/help/edge/docs/forms/universal-editor/assets/select-fdm-prefill.png)

5. Click **Save & Close**

+++

+++Phase 4: Testing Your Prefill Configuration

### Step 8: Preview and Test

1. Go to **Forms** > **Forms and Documents**
2. Select your Adaptive Form
3. Choose **Preview as HTML**
4. Test prefilling by appending parameters to the URL:

   `https://your-preview-url.com?<bindreferencefield>=<value>`

   **Example:**

   https://your-preview-url.com?petid=12345

   ![Prefill Form](/help/edge/docs/forms/universal-editor/assets/prefill-form.png)

The form should automatically populate with data based on the provided parameter.

+++

## Examples

### Sample Prefill Data Structures

**JSON Example for FDM-based Form:**

```

  {
    "afBoundData": {
      "user": {
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1-555-0123"
      }
    },
    "afUnBoundData": {
      "additionalInfo": "User preferences loaded"
    }
  }

```

**XML Example for XFA-based Form:**

```

  <?xml version="1.0" encoding="UTF-8"?>
  <afData>
    <afBoundData>
      <user>
        <firstName>John</firstName>
        <lastName>Doe</lastName>
        <email>john.doe@example.com</email>
      </user>
    </afBoundData>
  </afData>

```

### Example Prefill URLs

The URLs below are for illustration purposes only and will not work as-is. Replace the host and parameters with those relevant to your own environment when testing prefill functionality.

**Basic prefill test:**

`https://preview.example.com/form.html?userId=12345`

**Multiple parameter test:**

`https://preview.example.com/form.html?userId=12345&category=premium`


## Troubleshooting

+++Common Issues and Solutions

| Issue | Possible Cause | Solution |
|-------|----------------|----------|
| **Form fields not prefilling** | Incorrect `bindRef` values | Verify `bindRef` matches FDM field names exactly |
| **Data format errors** | Mismatched data structure | Ensure prefill data matches form model schema |
| **Service not found** | FDM configuration issues | Check FDM services are properly configured and saved |
| **Authentication errors** | Data source connectivity | Verify data source credentials and connectivity |
| **Partial data loading** | Missing field mappings | Ensure all required fields have proper data bindings |

+++

+++Debugging Steps

1. **Verify FDM Configuration:**

   - Check if services are configured correctly
   - Test FDM services independently
   - Validate data source connectivity

2. **Check Form Configuration:**

   - Confirm form is associated with correct FDM
   - Verify field `bindRef` values
   - Test form without prefill first

3. **Test Data Flow:**

   - Use browser developer tools to inspect network requests
   - Check console for JavaScript errors
   - Validate response data format

4. **Common Error Messages:**

   - "Prefill service not found": Check service configuration
   - "Data binding failed": Verify `bindRef` accuracy
   - "Invalid data format": Ensure data matches schema

+++

## Best Practices

+++Configuration Best Practices

- **Use descriptive naming**: Name your FDMs and services clearly
- **Validate data schemas**: Ensure data structure matches form requirements
- **Test incrementally**: Configure and test one field at a time
- **Document mappings**: Keep track of field-to-data mappings

+++

+++Performance Optimization

- **Minimize data volume**: Only prefill necessary fields
- **Use caching**: Configure appropriate caching for frequently accessed data
- **Optimize queries**: Ensure database queries are efficient
- **Monitor performance**: Track form load times with prefill enabled

+++

+++Security Considerations

- **Validate input parameters**: Always validate URL parameters
- **Sanitize data**: Clean data before prefilling forms
- **Implement access controls**: Ensure users can only access their own data
- **Use HTTPS**: Always use secure connections for data transmission

+++

+++User Experience Guidelines

- **Provide feedback**: Show loading indicators during data fetch
- **Handle errors gracefully**: Display helpful error messages
- **Allow overrides**: Let users modify prefilled data
- **Maintain consistency**: Use consistent prefill behavior across forms

+++

## Frequently Asked Questions

+++How do I test if prefilling is working correctly?

Preview your form and append prefill parameters to the URL using this format: `?<bindreferencefield>=<value>`. Ensure the field has a valid `bindRef` that matches your data structure. Use browser developer tools to inspect network requests and verify data is being fetched correctly.

+++

+++What data formats are supported for prefilling Adaptive Forms?

Adaptive Forms support multiple formats depending on your form model:

- **XFA forms**: XML matching the XFA schema
- **JSON schema forms**: JSON data compliant with the schema  
- **FDM forms**: JSON that maps to the data model structure
- **XML schema forms**: XML matching the schema structure

+++

+++Can I prefill both bound and unbound fields?

Yes, you can prefill both types of fields. Bound fields use the `afBoundData` section and must match your form model schema. Unbound fields use the `afUnBoundData` section and can contain any additional data.

+++

+++What should I do if only some fields are prefilling?

Check that all fields have correct `bindRef` values that match your FDM exactly. Verify that your data source contains all the required fields and that the data structure matches your form model schema.

+++

+++Can I use multiple prefill services in one form?

You can configure one primary prefill service per form. However, you can combine different data sources within a single Form Data Model to achieve similar functionality.

+++

+++How do I handle authentication for prefill services?

Authentication depends on your data source configuration. For FDM-based prefilling, configure authentication in your data source settings. For draft prefilling, users typically need to be logged in to access their saved drafts.

+++



## Related Topics

- [Integrate forms with Form Data Model in Universal Editor](/help/edge/docs/forms/universal-editor/integrate-forms-with-data-source.md)
- [Create Form Data Models](/help/forms/create-form-data-models.md)
- [Work with Form Data Model (FDM)](/help/forms/work-with-form-data-model.md)
- [Configure Data Sources](/help/forms/configure-data-sources.md)
- [Getting Started with Edge Delivery Services for AEM Forms](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md)
