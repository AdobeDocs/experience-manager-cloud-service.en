---
title: How to Create Form Fragments for WYSIWYG-Based Authoring
description: Learn how to create form fragments in the Universal Editor and add them to forms.
feature: Edge Delivery Services
role: Admin, User, Developer
hide: yes
hidefromtoc: yes
---

# Creating and using Edge Delivery Services Form Fragments in Universal Editor

Forms often include common sections like contact information, identification details, or consent agreements. The form developers create these sections every time they build a new form, which is repetitive and time-consuming. 
To eliminate this duplication of effort, Universal Editor provides a way to create reusable form segments, such as panels or groups of fields, just once and reuse them across various forms. These reusable, modular, and standalone segments are called form fragments. For example, the same emergency contact fragment can be used in different sections of a form, such as for employee and supervisor contact details.

By the end of the article, you learn how to create and use fragments in forms using the Universal Editor.

## Features of Edge Delivery Services Form Fragments

* **Maintaining consistency with form fragments**
    You can integrate fragments into different forms, helping you maintain consistent layouts and standardized content. With a "change once, reflect everywhere" approach, any update made to a fragment automatically applies to all forms.

* **Adding form fragments multiple times within form**
    You can add a form fragment multiple times within a form and configure its data binding properties to data sources or schemas. 

* **Using fragments within fragments**
    You can create nested form fragments, which means you can add a fragment in another fragment, and can have nested fragment structure.

    >[!NOTE]
    >
    > You cannot nest a fragment within itself, as this can cause recursive references and unintended behavior, leading to errors or rendering issues.

## Considerations while using Edge Delivery Services Form Fragments

* You need to add the same GitHub URL in both the fragment and the form where you intend to use the fragment.
* You cannot edit a form fragment, which is inserted by reference, from within an form. To edit, modify the stand-alone form fragment.

## Prerequisites for creating Edge Delivery Services Form Fragments

* [Set up your GitHub repository](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#get-started-with-the-aem-forms-boilerplate-repository-template) to establish a connection between your AEM environment and the GitHub repository.
* If you are already using Edge Delivery Services, add the latest version of the [Adaptive Forms block](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#add-adaptive-forms-block-to-your-existing-aem-project) to your GitHub repository. 
* The AEM Forms Author instance includes a template based on Edge Delivery Services. Ensure the [latest version of Core Components](https://github.com/adobe/aem-core-forms-components) is installed in your environment.
*  Keep the URL of your AEM Forms as a Cloud Service author instance and your GitHub Repository handy. 

## Working with Edge Delivery Services Form Fragments

You can create Edge Delivery Services Form Fragments in the Universal Editor and add the created fragments to Edge Delivery Services forms. You can perform the following actions with Edge Delivery Services Form Fragments:

* [Creating form fragments](#creating-form-fragments)
* [Adding form fragments to a form](#adding-form-fragments-to-a-form)
* [Managing form fragments](#managing-form-fragments)

### Creating form fragments

To create a form fragment in Universal Editor, perform the following steps:

1. Login into your AEM Forms as a Cloud Service author instance.
1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
1. Click **Create &gt; Adaptive Form Fragment**.

   ![Create fragment](/help/edge/docs/forms/universal-editor/assets/create-fragment.png)

   The **Create Adaptive Form Fragment** wizard appears.
1. Select the Egde Delivery Services  based template from the **Select Template** tab and click **[!UICONTROL Next]**.
   ![Select Edge Delivery Services template](/help/edge/docs/forms/universal-editor/assets/create-form-fragment.png)

1. Specify title, name, description, GitHub URL and tags for the fragment. Ensure that you specify a unique name for the fragment. If another fragment exists with the same name, the fragment fails to create.

    >[!NOTE]
    >
    > If your GitHub repository is named `edsforms`, it is located under the account `wkndforms`,the URL is:
    `https://github.com/wkndforms/edsforms`

    ![basic properties](/help/edge/docs/forms/universal-editor/assets/fragment-basic-properties.png)

1. (Optional) Click to open the **Form Model** tab, and from the **Select From** drop-down menu, select one of the following models for the fragment:

   ![Displays model type in the Form Model tab](/help/edge/docs/forms/universal-editor/assets/select-fdm-for-fragment.png)

    * **Form Data Model (FDM)**: Integrate data model objects and services from data sources into your fragment. Choose Form Data Model (FDM) if your form requires reading and writing data from multiple sources.

    * **JSON Schema**: Integrate your form with a backend system by associating a JSON schema that defines the data structure. It allows you to add dynamic content using the schema elements. 
    * **None**: Specifies to create the fragment from scratch without using any form model.

    >[!NOTE]
    >
    > To learn how to integrate forms or fragments with a Form Data Model (FDM) in the Universal Editor to use diverse backend data sources, [click here](/help/edge/docs/forms/universal-editor/integrate-forms-with-data-source.md).

1. (Optional) Specify the **Publish Date** or **Unpublish Date** for the fragment in the **Advanced** tab.

    ![Adavanced tab](/help/edge/docs/forms/universal-editor/assets/advanced-properties-fragment.png)
1. Click **Create** and a wizard appears. 

    ![Edit fragment](/help/edge/docs/forms/universal-editor/assets/edit-fragment.png)

1. Click **Edit** and the created fragment with a default template opens in Universal Editor for authoring. 

    ![Fragment in Univerasal Editor for authoring](/help/edge/docs/forms/universal-editor/assets/fragment-in-ue.png)

    In edit mode, you can add any form components to the fragment. To learn how to create a fragment in the Universal Editor, refer to the [Getting Started with Edge Delivery Services for AEM Forms using Universal Editor](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md#author-forms-using-wysiwyg) article.

    The below screenshot displays the `contact fragment` created in Universal Editor.

    ![Contact fragment](/help/edge/docs/forms/universal-editor/assets/contact-fragment.png)

    Once you have created the fragment, you can [add the created fragment in the Edge Delivery Services Forms](#adding-form-fragments-in-forms).

### Adding form fragments to a form

Let’s create a simple `Employee Details` form that includes both employee and supervisor information. You can use the `Contact Details` fragment in both the employee and supervisor panels. To use the form fragment in your form, perform the following steps:

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

    The form fragment is added by reference to the form and remains in synchronized with the standalone form fragment. This implies that any modifications made to the fragment are mirrored across all instances where the fragment is incorporated within forms.

    ![Fragment in form](/help/edge/docs/forms/universal-editor/assets/fragment-in-form.png)

    You can preview the form to see how the form appears in the **Preview** mode.

    ![Preview](/help/edge/docs/forms/universal-editor/assets/preview-form-with-fragment.png)

    Similarly, you can repeat Steps 3 to 7 to insert the `Contact Details` fragment for the `Supervisor Details` panel.

    ![Empoyee Details form](/help/edge/docs/forms/universal-editor/assets/employee-detail-form-with-fragments.png)

### Managing form fragments

You can perform several operations on form fragments using the AEM Forms user interface.

1. Login into your AEM Forms as a Cloud Service author instance.
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

## Best Practices 

* Ensure that the fragment name is unique. The fragment fails to create if there is an existing fragment with the same name.
* Any expression, script, or style in a stand-alone form fragment is retained when it is inserted by reference or embedded in an form.
* When you publish a form, the form fragments inserted by reference within the form are published automatically.

## See Also

{{universal-editor-see-also}}