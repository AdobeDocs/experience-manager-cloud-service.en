---

title: "How to Configure a Redirect Page or Thank you message"
description: "Learn how users can be displayed a thank you message or redirected to a webpage that form authors can configure while creating the form."
feature: Adaptive Forms, Edge Delivery Services
role: User
level: Intermediate
---

# Configure Thank You Messages and Redirect URLs

Form fragments are reusable components that eliminate repetitive development work and ensure consistency across your organization's forms. Instead of recreating common sections like contact information, address details, or consent agreements for every form, you can build these elements once as fragments and reuse them across multiple forms.

**What you'll accomplish in this article:**

- Understand the business value and technical capabilities of form fragments
- Create reusable form fragments using Universal Editor
- Integrate fragments into existing forms with proper configuration
- Manage fragment lifecycle and maintain consistency across forms

**Business benefits:**

- **Reduced development time**: Build common form sections once, reuse everywhere
- **Improved consistency**: Standardized layouts and content across all forms
- **Simplified maintenance**: Update a fragment once to reflect changes across all forms that use it
- **Enhanced compliance**: Ensure regulatory sections remain consistent and up-to-date

Form fragments in Edge Delivery Services support advanced capabilities including nested fragments, multiple instances within a single form, and seamless integration with data sources.

## Understanding Form Fragments

Form fragments in Edge Delivery Services provide powerful capabilities for modular form development:

**Core capabilities:**

- **Consistency management**: Fragments maintain identical layouts and content across multiple forms. With a "change once, reflect everywhere" approach, updates to a fragment automatically apply to all forms in Preview mode.
- **Multiple usage**: Add the same fragment multiple times within a single form, each with independent data binding to different data sources or schema elements.
- **Nested structures**: Create complex hierarchies by embedding fragments within other fragments for sophisticated form architectures.

**Technical requirements:**

- **GitHub URL consistency**: Both the fragment and any form using it must specify the same GitHub repository URL
- **Standalone editing**: Fragments can only be modified in their standalone form; changes cannot be made within the host form

**Publication behavior:**

>[!IMPORTANT]
>
>In Preview mode, fragment changes reflect immediately across all forms. In Publish mode, you must republish both the fragment and any forms that use it to see updates.

>[!CAUTION]
>
>Avoid recursive fragment references (nesting a fragment within itself) as this causes rendering errors and unexpected behavior.

## Prerequisites

**Technical setup requirements:**

- [GitHub repository configured](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#get-started-with-the-aem-forms-boilerplate-repository-template) with connection established between your AEM environment and GitHub repository
- [Latest Adaptive Forms block](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#add-adaptive-forms-block-to-your-existing-aem-project) added to your GitHub repository (for existing Edge Delivery Services projects)
- AEM Forms Author instance with Edge Delivery Services template available
- Access to your AEM Forms as a Cloud Service author instance URL and GitHub repository URL

**Required knowledge and permissions:**

- Basic understanding of form design concepts and component hierarchy
- Familiarity with Universal Editor interface and form creation workflows
- Author-level permissions in AEM Forms to create and manage form assets
- Understanding of your organization's form standards and reusable component requirements 

## Working with Edge Delivery Services Form Fragments

You can create Edge Delivery Services Form Fragments in the Universal Editor and add the created fragments to Edge Delivery Services forms. You can perform the following actions with Edge Delivery Services Form Fragments:

- [Creating form fragments](#creating-form-fragments)
- [Adding form fragments to a form](#adding-form-fragments-to-a-form)
- [Managing form fragments](#managing-form-fragments)

+++ Creating form fragments

To create a form fragment in Universal Editor, perform the following steps:

1. Log in to your AEM Forms as a Cloud Service author instance.
1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
1. Click **Create &gt; Adaptive Form Fragment**.

   ![Create fragment](/help/edge/docs/forms/universal-editor/assets/create-fragment.png)

   The **Create Adaptive Form Fragment** wizard appears.
1. Select the Edge Delivery Services  based template from the **Select Template** tab and click **[!UICONTROL Next]**.
   ![Select Edge Delivery Services template](/help/edge/docs/forms/universal-editor/assets/create-form-fragment.png)

1. Specify title, name, description and tags for the fragment. Ensure that you specify a unique name for the fragment. If another fragment exists with the same name, the fragment fails to create. 
1. Specify the **GitHub URL**. For example, if your GitHub repository is named `edsforms`, it is located under the account `wkndforms`, the URL is `https://github.com/wkndforms/edsforms`.

    ![basic properties](/help/edge/docs/forms/universal-editor/assets/fragment-basic-properties.png)

1. (Optional) Click to open the **Form Model** tab, and from the **Select From** drop-down menu, select one of the following models for the fragment:

   ![Displays model type in the Form Model tab](/help/edge/docs/forms/universal-editor/assets/select-fdm-for-fragment.png)

    - **Form Data Model (FDM)**: Integrate data model objects and services from data sources into your fragment. Choose Form Data Model (FDM) if your form requires reading and writing data from multiple sources.

    - **JSON Schema**: Integrate your form with a backend system by associating a JSON schema that defines the data structure. It allows you to add dynamic content using the schema elements. 
    - **None**: Specifies to create the fragment from scratch without using any form model.

    >[!NOTE]
    >
    > To learn how to integrate forms or fragments with a Form Data Model (FDM) in the Universal Editor to use diverse backend data sources, see [Integrate forms with Form Data Model in Universal Editor](/help/edge/docs/forms/universal-editor/integrate-forms-with-data-source.md).

1. (Optional) Specify the **Publish Date** or **Unpublish Date** for the fragment in the **Advanced** tab.

    ![Advanced tab](/help/edge/docs/forms/universal-editor/assets/advanced-properties-fragment.png)
1. Click **Create** to generate the fragment. A success dialog appears with editing options.

    ![Edit fragment](/help/edge/docs/forms/universal-editor/assets/edit-fragment.png)

1. Click **Edit** to open the fragment in Universal Editor with the default template applied.

    ![Fragment in Universal Editor for authoring](/help/edge/docs/forms/universal-editor/assets/fragment-in-ue.png)

1. **Design your fragment content**: Add form components (text fields, dropdowns, checkboxes) to build the reusable section. For detailed component guidance, see [Getting Started with Edge Delivery Services for AEM Forms using Universal Editor](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#author-forms-using-wysiwyg).

1. **Configure component properties**: Set field names, validation rules, and default values as needed for your use case.

1. **Save and preview**: Save your fragment and use the Preview mode to verify the layout and functionality.

    ![Screenshot of a completed contact details form fragment in the Universal Editor, showing fields for name, phone, email, and address that can be reused across multiple forms](/help/edge/docs/forms/universal-editor/assets/contact-fragment.png)

**Validation checkpoint:**

- Fragment loads without errors in Universal Editor
- All form components render correctly
- Field properties and validation rules work as expected
- Fragment is saved and available in the Forms & Documents console

Once your fragment is complete, you can [integrate it into any Edge Delivery Services form](#adding-form-fragments-to-a-form).

+++


+++ Adding form fragments to a form

This example demonstrates creating an `Employee Details` form that uses the `Contact Details` fragment for both employee and supervisor information sections. This approach ensures consistent data collection while reducing development effort.

To integrate a form fragment into your form:

1. Open the form in edit mode.
1. Add the Form Fragment component to the form.
1. Open the Content browser, and navigate to the **[!UICONTROL Adaptive Form]** component in the **Content tree**.
1. Navigate to the section, where you intend to add a fragment. For example, navigate to the **Employee Details** panel. 

    ![Navigate to section](/help/edge/docs/forms/universal-editor/assets/navigate-to-section.png)

1. Click the **[!UICONTROL Add]** icon and add the **[!UICONTROL Form Fragment]** component from the **Adaptive Form Components** list. 
    ![Add Form Fragment](/help/edge/docs/forms/universal-editor/assets/add-fragment.png)

    When you select the **[!UICONTROL Form Fragment]** component, the fragment gets added to your form. You can configure the properties of the added fragment by opening its **Properties**. For example, hide the title of the fragment from its **Properties**.

    ![Configuring properties of fragment](/help/edge/docs/forms/universal-editor/assets/fragment-properties.png)

1. Select the **Fragment reference** in the **Basic** tab. All the fragments available for your form, depending on the model of the form, appear.
   
    For example, navigate to `/content/forms/af` and select the `Contact Details` fragment.

    ![Select Fragment](/help/edge/docs/forms/universal-editor/assets/select-fragment.png)

1. Click **[!UICONTROL Select]**.

    The form fragment is added by reference to the form and remains synchronized with the standalone form fragment.

    ![Screenshot showing the contact details fragment successfully integrated into an employee form within the Universal Editor, demonstrating how fragments maintain their structure when reused](/help/edge/docs/forms/universal-editor/assets/fragment-in-form.png)

    You can preview the form to see how the form appears in the **Preview** mode.

    ![Preview](/help/edge/docs/forms/universal-editor/assets/preview-form-with-fragment.png)

    Similarly, you can repeat Steps 3 to 7 to insert the `Contact Details` fragment for the `Supervisor Details` panel.

    ![Employee Details form](/help/edge/docs/forms/universal-editor/assets/employee-detail-form-with-fragments.png)

+++



+++ Managing form fragments

You can perform several operations on form fragments using the AEM Forms user interface.

1. Log in to your AEM Forms as a Cloud Service author instance.
1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

1. Select a form fragment and the toolbar displays the following operations you can perform on the selected fragment.

    ![Manage fragment](/help/edge/docs/forms/universal-editor/assets/manage-fragment.png)

    <table>
    <tbody>
    <tr>
   <td><p><strong>Operation</strong></p> </td>
   <td><p><strong>Description</strong></p> </td>
    </tr>
    <tr>
   <td><p>Edit</p> </td>
   <td><p>Opens the form fragment in edit mode.<br /> <br /> </p> </td>
    </tr>
    <tr>
   <td><p>Properties</p> </td>
   <td><p>Provides options to modify the properties of the form fragment.<br /> <br /> </p> </td>
    </tr>
    <td><p>Copy</p> </td>
   <td><p> Provides options to copy the form fragment and paste it at the desired location. <br /> <br /> </p> </td>
    </tr>
   <tr>
   <td><p>Preview</p> </td>
   <td><p>Provides options to preview the fragment as HTML or perform a custom preview by merging data from an XML file with the fragment. <br /> </p> </td>
    </tr>
    <tr>
   <td><p>Download</p> </td>
   <td><p>Downloads the selected fragment.<br /> <br /> </p> </td>
    </tr>
    <tr>
   <td><p>Start Review/Manage Review</p> </td>
   <td><p>Allows initiating and managing a review of the selected fragment.<br /> <br /> </p> </td>
    </tr>
    <!--<tr>
   <td><p>Add Dictionary</p> </td>
   <td><p>Generates a dictionary for localizing the selected fragment. For more information, see <a>Localizing Adaptive Forms</a>.<br /> <br /> </p> </td>
    </tr>-->
    <tr>
   <td><p>Publish / Unpublish</p> </td>
   <td><p>Publishes / unpublishes the selected fragment.<br /> <br /> </p> </td>
    </tr>
    <tr>
   <td><p>Delete</p> </td>
   <td><p>Deletes the selected fragment.<br /> <br /> </p> </td>
    </tr>
    <tr>
   <td><p>Compare</p> </td>
   <td><p>Compares two different form fragments for previewing purposes.<br /> <br /> </p> </td>
    </tr>
    </tbody>
    </table>

+++ 

## Best Practices

**Fragment design and naming:**

- **Use descriptive, unique names**: Choose names that clearly indicate the fragment's purpose (e.g., "contact-details-with-validation" rather than "fragment1")
- **Plan for reusability**: Design fragments to be context-independent so they work across different form types
- **Keep fragments focused**: Create single-purpose fragments rather than complex, multi-function components

**Development workflow:**

- **Test fragments independently**: Verify fragment functionality before integrating into forms
- **Maintain consistent GitHub URLs**: Ensure the same repository URL is used across all related fragments and forms
- **Document fragment purpose**: Include clear descriptions and tags to help team members understand when to use each fragment

**Publication and maintenance:**

- **Coordinate publication**: When updating fragments, plan to republish all dependent forms simultaneously
- **Version control**: Use meaningful commit messages when updating fragments to track changes over time
- **Monitor dependencies**: Keep track of which forms use each fragment to assess update impact

>[!TIP]
>
>Fragment styles, scripts, and expressions are preserved when embedded, so design with this inheritance in mind.

## Summary

You have successfully learned how to leverage form fragments in Edge Delivery Services to improve development efficiency and maintain consistency across your organization's forms. 

**Key accomplishments:**

- **Understanding**: Grasped the business value and technical capabilities of form fragments
- **Creation**: Built reusable form fragments using Universal Editor with proper configuration
- **Integration**: Added fragments to forms with correct reference setup and property configuration  
- **Management**: Explored fragment lifecycle operations and maintenance workflows

**Next steps:**

- Create a library of commonly used fragments for your organization
- Establish naming conventions and governance policies for fragment usage
- Explore advanced integration with [Form Data Models](/help/edge/docs/forms/universal-editor/integrate-forms-with-data-source.md) for dynamic data-driven fragments
- Implement fragment-based form templates for consistent user experiences

Your forms now benefit from modular, maintainable architecture that scales efficiently across projects while ensuring consistent user experiences.

