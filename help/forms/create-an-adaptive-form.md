---
title: How to create an Adaptive Form?
description: Learn how to create mobile-responsive Adaptive Forms with our step-by-step tutorial. These forms adapt seamlessly across devices, ensuring a smooth experience.
keywords: Adaptive Forms, Responsive Forms, HTML5 Forms
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner
hide: yes
hidefromtoc: yes
exl-id: 6f1c3fe7-b61e-47ce-b565-15b4904db092
---
# Create an Adaptive Form {#creating-an-adaptive-form}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/creating-adaptive-form.html)                  |
| AEM as a Cloud Service     | This article   |

Adaptive Forms let you create forms that are engaging, responsive, dynamic, and adaptive. AEM Forms provides business user-friendly wizard to quickly create Adaptive Forms. The wizard has a quick tab navigation to easily select pre-configured template, styling, fields, and submission options to create an Adaptive Form. 

![Wizard to create an Adaptive Form](/help/release-notes/assets/wizard.png){width="100%" align="center"}

Before you start, learn about the type of Forms components available to you: 

* [Adaptive Forms Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html?lang=en): These are standardized data capture components. These components provide customization capabilities, reduced development time, and lower maintenance costs for your digital enrollment experiences. A developer can easily customize and style these components. You can visit [https://aemcomponents.dev/](https://aemcomponents.dev/) to view available core components in action **Adobe recommends using these modern and extensible components to develop Adaptive Forms**.  

* [Adaptive Forms Foundation Components](creating-adaptive-form.md): These are classic (old) data capture components. You can continue to use these to edit your existing foundation components based Adaptive Form. If you are creating new forms, Adobe recommends using  [Adaptive Forms Core Components to create an Adaptive Forms](#create-an-adaptive-form-core-components). 

>[!BEGINTABS]

>[!TAB Create Adaptive Forms with Core Components (Recommended)]

You require the following to create an Adaptive Form:

* **Enable Adaptive Forms Core Components for your environment**: When you create a program, the Adaptive Forms Core Components already enabled for your environment. If you have a Forms as a Cloud Service environment based on Archetype 39 or earlier, [Enable Adaptive Forms Core Components for your environment](enable-adaptive-forms-core-components.md). On enabling the Core Components for your environment, the **Adaptive Forms (Core Component)** template and canvas theme is added to your environment. If your AEM SDK version older than 2023.02.0, [ensure that you have `prerelease` flag enabled on your environment](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html?lang=en#new-features) as Adaptive Forms Core Components were part of pre-prelease before the 2023.02.0 release.   

* **An Adaptive Form template**: A template provides a basic structure and defines appearance (layouts and styles) of an Adaptive Form. It has pre-formatted components containing certain properties and content structure. It also provides the options to define a theme and a submit action. The theme defines the look and feel and submit action defines the action to take on submission of an Adaptive Form. For example, sending the collected data to a data source. The cloud service provides an OOTB template, named blank:

    * The `blank` template is included with every fresh AEM Forms as a Cloud Service program.
    * You can install the reference package, via Package Manager, to add the `blank` template to your AEM Forms as a Cloud Service program. 
    * You can also [create an Adaptive Forms template (Core Components)](template-editor.md) from scratch.

* **An Adaptive Form theme**: A theme contains styling details for the components and panels. Styles include properties such as background colors, state colors, transparency, alignment, and size. When you apply a theme, the specified style reflects on the corresponding components.  The `Canvas` template is included with every fresh AEM Forms as a Cloud Service program.
    <!-- * You can install the reference package, via package manager, to add the `Canvas` template to your AEM Forms as a Cloud Service program.
    * You can also [create an Adaptive Forms theme (Core Components)](template-editor.md) and deploy it to your AEM Forms as a Cloud Service program. --> 

* **Permissions**: Add your users to [!DNL forms-users] group. The members of the [!DNL forms-users] group have permissions to create an Adaptive Form. For detailed list of forms-specific user groups, see [Groups and permissions](forms-groups-privileges-tasks.md).


## Create an Adaptive Form {#create-an-adaptive-form-core-components}

1. Log in to your [!DNL Experience Manager Forms] Author instance. It can be a Cloud instance or a local development instance.

1. Enter your credentials on the Experience Manager login page. After you are logged in, in the upper-left corner, select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

1. Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The Wizard opens. In the Source tab, select a template:

    ![Core Components Template](/help/forms/assets/core-components-template.png){width="100%" align="center"}

    When you select a template, a theme and submit action specified in the template are auto-selected, and the **[!UICONTROL Create]** button is enabled. You can go to the **[!UICONTROL Style]** or **[!UICONTROL Submission]** tabs to select a different theme or submit action. If the selected template does not specify a theme, the create button remains disabled. You can go to the **[!UICONTROL Styles]** tab to manually select a theme.

    >[!NOTE]
    >
    >
    > If you do not have, **Adaptive Forms (Core Component)** template on your environment, [Enable Adaptive Forms Core Components for your environment](setup-local-development-environment.md#enable-adaptive-forms-core-components-for-an-existing-aem-archetype-based-project). On enabling the Core Components for your environment, the **Adaptive Forms (Core Component)** template is added to your environment.  

1. In the **[!UICONTROL Style]** tab, select a theme:

    * When the selected template specifies a theme, the theme is auto selected in the wizard. You can also choose a different theme from the Style tab.
    
    * If the selected template does not specify a theme, you can use the Style tab to choose a theme. The **[!UICONTROL Create]** button is enabled only after a theme is selected. 

1. (Optional) In the Data Tab, select a data model:

    * **Form data model**: A [Form Data Model(FDM)](data-integration.md) lets you integrate entities and services from disparate data sources to an Adaptive Form. Choose Form Data Model (FDM) if the Adaptive Form that you are creating involves fetching and write data from and to multiple data source.
    
    * **JSON Schema**: [JSON schema](adaptive-form-json-schema-form-model.md) Our Core-Components-based Adaptive Form allows for seamless integration with your organization's back-end system by providing the ability to associate a JSON schema, which represents the structure of the data being produced or consumed. This association enables authors to dynamically add content to the Adaptive Form using the elements of the schema. The elements of the schema are easily accessible in the Data Model Objects tab of the Content browser during the authoring process, and all fields are automatically added to any created Adaptive Form.

    By default all fields of the associated JSON schema are automatically selected and converted into corresponding Adaptive Form components, streamlining the authoring process. The wizard offers the added convenience of allowing you to selectively choose which fields should be included in the Adaptive Form through the use of checkboxes. 

1. In the **[!UICONTROL Submission]** tab, select a submit action:

    * When you select a template, the submit action specified in the template is auto-selected. You can select a different submit action from the Submission tab. The **[!UICONTROL  Submission]** tab displays all the available submit actions. 
    
    * When the selected template does not specify a submit action, you can use the **[!UICONTROL Submission]** tab to select a submit action

1. (Optional) In the **[!UICONTROL Delivery]** tab, you can specify a publishing or unpublishing date for an Adaptive Form. 
   
1. Select **[!UICONTROL Create]**. A dialog to specify title, name, and location to save the Adaptive Form appears:

    * **[!UICONTROL Title]** Specifies the display name of the form. The title helps you identify the form in the [!DNL Experience Manager Forms] user interface.
    * **[!UICONTROL Name:]** Specifies the name of the form. A node with the specified name is created in the repository. As you start typing a title, value for the name field is automatically generated. You can change the suggested value. The name field can include only alphanumeric characters, hyphens, and underscores. All the invalid inputs are replaced with a hyphen.
    * **[!UICONTROL Path:]** Specifies the location at which the Adaptive Form is to be saved. You can save the Adaptive Form directly at `/content/dam/formsanddocuments` or create a folder such as `/content/dam/formsanddocuments/adaptiveforms` to save an Adaptive Form. Ensure that you create the folder before using it in the path. The **[!UICONTROL Path]** field does not create a folder automatically. 

1. Select **[!UICONTROL Create]**. An Adaptive Form is created and opens in the Adaptive Forms editor. The editor displays the contents available in the template.  Based on the type of Adaptive Form, the form elements present in the associated <!--XFA form template, XML schema or --> JSON schema or Form Data Model (FDM) are displayed in the **[!UICONTROL Data Model Objects]** tab of the **[!UICONTROL Content Browser]** in the sidebar. 

Now, you can drag-and-drop the [Adaptive Forms Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html?lang=en#components) or schema elements to build your Adaptive Form.  


## Edit Form Model properties of an Adaptive Form {#edit-form-model-core-components-based-adaptive-forms}

1. Select the Adaptive Form and select ![Page information](/help/forms/assets/Smock_Properties_18_N.svg) > **[!UICONTROL Open Properties]**. The Form Properties page opens. 

1. Go to the **[!UICONTROL Form Model]** tab and choose a form model. If the Adaptive Form is without a form model, you have the freedom to choose either a JSON schema or a form data model (FDM). On the other hand, if the Adaptive Form is already based on a form model, you have the option to switch to another form model of the same type. For instance, if the form is using a JSON schema, you can easily switch to another JSON schema, and similarly if the form is using a Form Data Model (FDM), you can switch to another Form Data Model (FDM). 

1. Select **[!UICONTROL Save]** to save the properties.

>[!TAB Create Adaptive Forms with Foundation Components]

You require the following to create an Adaptive Form:

* **Permissions**: Add your users to [!DNL forms-users] to provide them permissions to create an Adaptive Form. For detailed list of forms-specific user groups, see [Groups and permissions](forms-groups-privileges-tasks.md).

* **An Adaptive Form theme**: A theme contains styling details for the components and panels. Styles include properties such as background colors, state colors, transparency, alignment, and size. When you apply a theme, the specified style reflects on the corresponding components. You can [create a theme](themes.md) or [import an existing theme](import-export-forms-templates.md#uploading-a-theme). You can also deploy the [latest archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/using.html#create-project) for some sample themes.

* **An Adaptive Form template**: A template provides a basic structure and defines appearance (layouts and styles) of an Adaptive Form. It has pre-formatted components containing certain properties and content structure. It also provides the options to define a theme and a submit action. The theme defines the look and feel and submit action defines the action to take on submission of an Adaptive Form. For example, sending the collected data to a data source. The cloud service supports two types of templates: 

    * **Editable template**: You can [create a](template-editor.md) or [import an existing editable template](migrate-to-forms-as-a-cloud-service.md). You can also deploy the [latest archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/using.html?lang=en#:~:text=The%20AEM%20Archetype%20is%20made%20up%20of%20modules%3A,and%20request%20filters.%20it.tests%3A%20are%20Java-based%20integration%20tests.) to get some sample editable templates. 

    * **Static template**: These are legacy templates and are recommended only for customers migrating from Adobe Managed Services (AMS) and on-premise AEM Forms installations (AEM 6.5 Forms or earlier). These let you continue to use your existing investment in static templates. When you create an Adaptive Form, use an Editable template.


## Create an Adaptive Form {#create-an-adaptive-form-foundation-components}

1. Access [!DNL Experience Manager Forms] Author instance. It can be a Cloud instance or a local development instance.

1. Enter your credentials on the Experience Manager login page.

   After you are logged in, in the upper-left corner, select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

1. Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The Wizard opens.
1. In the Source tab, select a template: 

   * When you select an Editable template, a theme and submit action specified in the template are auto-selected, and the **[!UICONTROL Create]** button is enabled. You can go to the **[!UICONTROL Style]** or **[!UICONTROL Submission]** tabs to select a different theme or submit action. If the selected Editable template does not specify a theme, the create button remains disabled. You can go to the **[!UICONTROL Styles]** tab to manually select a theme.
   
      >[!NOTE]
      >
      > You can also create [!UICONTROL Document of Record] template using an Adaptive Forms editor. For more information, see [Document of Record Support in Adaptive Form Editor](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md#document-of-record-support-in-adaptive-form-editor-dor-support-in-adaptiveform).

   * When you select a static template, the data, style, submission, delivery, and preview options are not available. When you are create a Adaptive Form, it is recommended to use an Editable template.

1. In the **[!UICONTROL Style]** tab, select a theme:

   * When the selected template specifies a theme, the theme is auto selected in the wizard. You can also choose a different theme from the Style tab.
   * If the selected template does not specify a theme, you can use the Style tab to choose a theme. The **[!UICONTROL Create]** button is enabled only after a theme is selected. 

1. (Optional) In the **[!UICONTROL Data]** tab, select a data model:

   * **Form data model**: A [Form Data Model (FDM)](data-integration.md) lets you integrate entities and services from disparate data sources to an Adaptive Form. Choose Form Data Model (FDM) if the Adaptive Form that you are creating involves fetching and write data from and to multiple data source.
   
   * **JSON Schema**: [JSON schema](adaptive-form-json-schema-form-model.md) represents the structure in which data is produced or consumed by the back-end system in your organization. You can associate the schema to an Adaptive Form and use its elements to add dynamic content to the Adaptive Form. The elements of the schema are available for use in the Data Model Objects tab of the Content browser when authoring Adaptive Forms and all the fields are also added to created Adaptive Form.

   By default, all the fields of the data model are selected. When you create the Adaptive Form, all the selected data model fields are converted to corresponding Adaptive Form components. The wizard provides you checkboxes to select only those fields which should be included in the Adaptive Form.
   
   <!-- 
   
   If your JSON schema contains a fragment, the fragment is considered a single unit. You can select or deselect a complete fragment and all the fields of the fragment are selected or deselected accordingly. 
   
   -->

1. In the **[!UICONTROL Submission]** tab, select a submit action:

   * When you select a template, the submit action specified in the template is auto-selected. You can select a different submit action from the Submission tab. The **[!UICONTROL  Submission]** tab displays all the available submit actions. 

   * When the selected template does not specify a submit action, you can use the **[!UICONTROL Submission]** tab to select a submit action

1. (Optional) In the Delivery tab, you can specify a publishing or unpublishing date for an Adaptive Form.  

1. Select **[!UICONTROL Create]**. A dialog to specify title, name, and location to save the Adaptive Form appears:
 
   * **[!UICONTROL Title]** Specifies the display name of the form. The title helps you identify the form in the [!DNL Experience Manager Forms] user interface.
   * **[!UICONTROL Name:]** Specifies the name of the form. A node with the specified name is created in the repository. As you start typing a title, value for the name field is automatically generated. You can change the suggested value. The name field can include only alphanumeric characters, hyphens, and underscores. All the invalid inputs are replaced with a hyphen.
   * **[!UICONTROL Path:]** Specifies the location at which the Adaptive Form is to be saved. You can save the Adaptive Form directly at `/content/dam/formsanddocuments` or create a folder such as `/content/dam/formsanddocuments/adaptiveforms` to save an Adaptive Form. Ensure that you create the folder before using it in the path. The **[!UICONTROL Path:]** field does not create a folder automatically. 

1. Select **[!UICONTROL Create]**. An Adaptive Form is created and opens in the Adaptive Forms editor. The editor displays the contents available in the template. It also displays the sidebar to customize the created form according to the needs.

   Based on the type of Adaptive Form, the form elements present in the associated <!--XFA form template, XML schema or --> JSON schema or Form Data Model (FDM) are displayed in the **[!UICONTROL Data Model Objects]** tab of the **[!UICONTROL Content Browser]** in the sidebar. You can also drag-drop these elements to build your Adaptive Form.

<!-- ## Create an Adaptive Form based on a Form Data Model {#fdm}

[Data integration](data-integration.md) lets you integrate multiple data sources and bring their entities and services together to create a form data model. It is an extension of JSON schema. You can use a Form Data Model to create an Adaptive Form. The entities or data model objects configured in a Form Data Model are available as data model objects for form authoring. They are bound to respective data sources and used to prefill a form and write submitted data back to the respective data sources. You can also call services configured in a Form Data Model using Adaptive Form rules.

To use a Form Data Model for creating an Adaptive Form:

1. In Form Model tab on Add Properties screen, select **[!UICONTROL Form Data Model]** in the **[!UICONTROL Select From]** drop-down list.

   ![Create an Adaptive Form](assets/create-af-1-1.png)

1. Select to expand **[!UICONTROL Select Form Data Model]**. All available form data models are listed.Select a from data model.

>[!NOTE]
>
>You can also change the Form Data Model for an Adaptive Form. For detailed steps, see [Edit Form Model properties of an Adaptive Form](#edit-form-model).

## Create an Adaptive Form based on XML or JSON schema {#create-an-adaptive-form-based-on-xml-or-json-schema}

XML and JSON schemas represent the structure in which data is produced or consumed by the back-end system in your organization. You can associate a schema to an Adaptive Form and use its elements to add dynamic content to the Adaptive Form. The elements of the schema are available in the Data Model Object tab of the content browser for authoring Adaptive Forms. You can drag-drop the schema elements to build the form.

See the following documents to understand how to design XML or JSON schema for authoring Adaptive Forms.

* [Creating Adaptive Forms using XML schema](adaptive-form-xml-schema-form-model.md)
* [Creating Adaptive Forms using JSON schema](adaptive-form-json-schema-form-model.md)

Do the following to use XML or JSON schema as form model for an Adaptive Form:

1. On the **[!UICONTROL Add Properties]** step of Adaptive Form creation page, select on the **[!UICONTROL Form Model]** tab.
1. In the Form Model tab, select **[!UICONTROL Schema]** from the **[!UICONTROL Select From]** drop-down field.

1. Select **[!UICONTROL Select Schema]** and do one of the following:

    * **[!UICONTROL Upload from disk]** - Select this option and select Upload Schema Definition to browse and upload an XML schema or JSON schema from your file system. The uploaded schema file resides with the form and is not accessible to other Adaptive Forms.
    * **[!UICONTROL Search in repository]** - Select this option to select from the list of schema definition files available in the repository. Select the XML or JSON schema file as form model. The selected schema is associated with the form by reference and is accessible for use in other Adaptive Forms.

      Ensure that the JSON schema filename ends with **.schema.json**. For example: mySchema.schema.json

   ![Selecting XML or JSON schema](assets/upload-schema.png)
**Figure:** *Selecting XML or JSON schema*

1. (For XML schema only) After you select or upload an XML Schema, specify a root element of the selected XSD file to map with the Adaptive Form.

   ![Selecting XSD root element](assets/xsd-root-element.png)
**Figure:** *Selecting XSD root element*

>[!NOTE]
>
>You can also change the schema for an Adaptive Form. For detailed steps, see [Edit Form Model properties of an Adaptive Form](#edit-form-model2). -->

## Edit Form Model properties of an Adaptive Form {#edit-form-model-foundation-components}

You can change the form model for an Adaptive Form (JSON-based or Form Data Model (FDM)). You cannot change from one form model to another.

1. Select the Adaptive Form and select the **Properties** icon.
1. Open the **[!UICONTROL Form Model]** tab and do one the following.

    * If the Adaptive Form is without a form model, you can choose another form model and accordingly select <!-- a form template, --> XML or JSON schema, or form data model (FDM).
    * If the Adaptive Form is based on a form model, you can choose another <!-- form template, --> XML or JSON schema, or Form Data Model (FDM) for the same form model.

1. Select **[!UICONTROL Save]** to save the properties.

You can also modify the form model properties from the Adaptive Form editor or Adaptive Form template editor. 

1. Select the **[!UICONTROL Adaptive Form container (Root)]** component.
1. Click ![Configure Icon](/help/forms/assets/configure-icon.svg) icon to open the **[!UICONTROL Properties]** of the Adaptive Form container.
1. Select the **[!UICONTROL Data Model]** tab and do one the following:

    * If the Adaptive Form is without a form model, you can choose a form model and accordingly select <!-- a form template, --> XML or JSON schema, or form data model (FDM).
    * If the Adaptive Form is based on a form model, you cannot change the form model. You can choose another <!-- form template, --> XML or JSON schema, or Form Data Model (FDM) for the same form model as applicable.
1. Select ![Save](/help/forms/assets/check-button.png) to save the properties.

 ![FDM-Schema-Support](/help/forms/assets/fdmsupport.png){width="100%" align="center"}

>[!NOTE]
>
> You can also save an Adaptive Form as a template. For more information, see [Create a template using an Adaptive Form](/help/forms/template-editor.md#saving-an-adaptive-form-as-template-saving-adaptive-form-as-template).

>[!ENDTABS]


## Next Steps

* [Use Adobe Sign with Forms](working-with-adobe-sign.md)
* [Use Google reCaptcha in with Forms](captcha-adaptive-forms.md)
* [Add repeatable section to a form](create-forms-repeatable-sections.md)
* [Pre-populate fields of a form](prepopulate-adaptive-form-fields.md)

>[!MORELIKETHIS]
>
>* [Create an Adaptive Form](/help/forms/creating-adaptive-form-core-components.md)
