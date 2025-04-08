---
title: How to add an Adaptive Form to AEM Sites page?
description: Discover how to create or add an Adaptive Form to your AEM Sites page. Also learn the benefits, and various ways to integrate forms into your website.
feature: Adaptive Forms, Foundation Components
Keywords: AF in Sites editor, af in aem sites, aem sites af, add af to a sites page, af aem sites, af sites, create af in a sites page, adaptive form in aem sites, forms aem sites, add form to a sites page, adaptive forms aem sites, add adaptive forms to aem page, create forms in an aem sites page
exl-id: a1846c5d-7b0f-4f48-9d15-96b2a8836a9d
role: User, Developer
---
# Add an Adaptive Form to an AEM Sites page or Experience Fragment {#create-or-add-an-adaptive-form-to-aem-sites-page}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/create-or-add-an-adaptive-form-to-aem-sites-page.html)                  |
| AEM as a Cloud Service     | This article         |

## Overview {#overview}

With AEM Forms, you can seamlessly add a form to your AEM Sites page. This allows your visitors to conveniently fill and submit forms without ever leaving the page they are on. By doing so, they can effortlessly stay engaged with other elements of the website while actively interacting with the form. 

You can use AEM Page Editor to quickly create and add multiple forms to your AEM Sites pages. Using AEM Page Editor allows content authors to create seamless data capture experiences within a Sites page using the power of adaptive forms components including dynamic behavior, validations, data integration, generate document of record, and business process automation. It also lets you use various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager.

AEM Forms Cloud Service provides Adaptive Form Container and Adaptive Forms – Embed components. You can use Adaptive Form Container to create a form in an AEM Sites page or Experience Fragment, while Adaptive Forms – Embed component lets you add an existing Adaptive Form or create a form using Adaptive Forms Editor. 

![An example of an Adaptive Form in an AEM Sites page](/help/forms/assets/adaptive-form-in-sites-page.png)

## Why use Adaptive Forms Core Components to create an Adaptive Form in AEM Sites page or Experience Fragment? 

If you have created Adaptive Forms Foundation Component or plain HTML based forms for your Sites in the past, Adobe recommends that you use Adaptive Forms Core Components to create an Adaptive Form in AEM Sites page or Expereince Fragment. It lets you use various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager, enhancing the overall form creation and management experience for Adaptive Forms. Let's explore some of these features:

* **Versioning:** AEM Sites pages offer [robust versioning capabilities](/help/sites-cloud/authoring/sites-console/page-versions.md), allowing you to track and manage different versions of your forms. This enables you to make changes and enhancements to forms while maintaining the ability to roll back to previous versions if needed. Versioning ensures a controlled and organized approach to form development and evolution.
* **Targeting (Integration with Adobe Target):** With AEM Sites pages targeting capabilities, you can also [personalize the form experience for different audiences](/help/sites-cloud/integrating/integrating-adobe-target.md). By using user segments and targeting criteria, you can tailor the form's content, design, or behavior to specific groups of users. This enables you to provide a personalized and relevant form experience, increasing engagement and conversion rates.
* **Translation:** AEM Sites [seamless integration with translation services](/help/sites-cloud/administering/translation/overview.md), allowing you to translate forms into multiple languages easily. This feature simplifies the localization process, ensuring that your forms are accessible to a global audience. You can manage translations efficiently within AEM translation projects, reducing time and effort required for multilingual form support. See considerations section for more information on translation.  
* **Multi-site Management and Live Copy:** AEM Sites provide robust [Multi-site Management and Live Copy capabilities](/help/sites-cloud/administering/msm/overview.md), enabling you to create and manage multiple websites within a single environment. This feature now lets you reuse forms across different sites, ensuring consistency and reducing duplication efforts. With centralized control and management, you can efficiently maintain and update forms across multiple websites.
* **Themes:** AEM Sites pages provide a framework for designing and maintaining consistent visual styles across multiple web pages. These define colors, fonts, style sheets, and other visual elements that contribute to the overall look and feel of the website. [You can use the themes designed for an AEM Sites page for an Adaptive Form, saving time and effort](/help/sites-cloud/administering/site-creation/site-themes.md#using-site-themes-using-themes). 
* **Tagging:** AEM Sites pages allow you to [assign tags or labels to a page, an asset, or other content](/help/implementing/developing/introduction/tagging-framework.md). Tags are keywords or metadata labels that provide a way to categorize and organize content based on specific criteria. You can assign one or more tags to pages, assets, or any other content items within AEM to improve search and categorize the assets. 
* **Locking and Unlocking content:** AEM Sites allow users to [control access and modifications to pages](/help/sites-cloud/authoring/page-editor/edit-content.md) within the AEM Sites environment. When a page is locked, it means that it is protected from unauthorized changes or edits by other users. Only the user who has locked the content or a designated administrator can unlock it to allow modifications. 

In addition, Adaptive Forms in AEM Page Editor use [Adaptive Forms Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html#features). These Core Components provide a standard and easier methods to style and customize the components, identical to [AEM Sites WCM Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html).


## How to create or add an Adaptive Form in AEM Sites page or AEM Experience Fragment? {#various-options-to-creat-or-add-an-adaptive-form-in-aem-sites-page-or-aem-experience-fragment}

You can take full advantage of this feature by utilizing the following options:

* **[Create and add a custom Adaptive Form to an AEM Sites page](#create-an-adaptive-form-in-sites-editor-or-experience-fragment):** You can use the Adaptive Form Container component to build a brand-new form from scratch, tailoring it specifically to your requirements and design preferences.

* **[Create and add a custom Adaptive Form to an Experience Fragments](#create-an-adaptive-form-in-sites-editor):** You can extend the reach of your forms by adding them to AEM Experience Fragments, allowing for seamless reuse across multiple pages or sites.

* **[Convert an Adaptive Form to Experience Fragment](#convert-an-adaptive-form-in-sites-page-to-an-experience-fragment):** Convert an Adaptive Form added to an AEM Sites page to an Experience Fragment for reusing the form across multiple AEM Sites pages.

* **[Create and add forms based on approved templates to an AEM Sites page:](/help/forms/embed-adaptive-form-aem-sites.md#embed-form-using-adaptive-form-wizzard-aem-sites)** You can use pre-approved templates to quickly create Adaptive Forms that align with your organization's branding guidelines and design standards. The option is available only for Adaptive Forms created with Adaptive Forms Editor or Adaptive Forms - Embed component. 

* **[Add existing forms to an AEM Sites page:](/help/forms/embed-adaptive-form-aem-sites.md#embed-an-adaptive-form-in-sites-editor)** You can easily integrate forms that you have already created into your websites, enabling visitors to interact with them directly. The option is available only for Adaptive Forms created with Adaptive Forms Editor or Adaptive Forms - Embed component. 


* **Add multiple forms to an AEM Sites page or Experience Fragment:**  You can create or add multiple Adaptive Forms to an AEM Sites page to provide multiple choices to users based on their preferences and requirements. These can a combination of brand-new form from scratch and existing forms. You can use the **[!UICONTROL Adaptive Form Container]** component multiple times to add Adaptive Forms in an AEM Sites page. You can use the **[!UICONTROL Adaptive Forms - Embed]** component multiple times in an AEM Sites page, only if **[!UICONTROL Form covers entire width of the frame]** option is selected. In case the **[!UICONTROL Form covers entire width of the frame]** option is not checked, AEM Sites page supports only one Adaptive Form to exist without an iframe. To add more Adaptive Forms using  the **[!UICONTROL Adaptive Forms - Embed]** component, select **[!UICONTROL Form covers entire width of the frame]** option. 

## Considerations to create an Adaptive Form in AEM Sites page or AEM Experience Fragment {#consideration}

* When you use the Adaptive Form Container to create or add a form, the forms undergo translation and localization through the AEM Sites translation flow. For each language, a separate copy (language copy) of the sites page and corresponding forms is generated and when a content author modifies a rule in a form on the parent page, the same changes must be made in all language copies of the form. Adaptive Form Container also lets you use various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager.

* When you create or add a form using the Adaptive Form-embed component, the forms undergo translation and localization using the AEM Forms translation flow. In this case, a single form is maintained and referenced in all the language copies of the Sites pages. Adaptive Form-embed component does not provide access to various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager.


## Requirements to create or add an Adaptive Form in AEM Sites page or AEM Experience Fragment {#before-you-start-creating-an-adaptive-form}

Before you start creating or an Adaptive Form, enable Adaptive Forms Core Components and add Adaptive Forms Client Libraries to your AEM Sites page:

### Enable Adaptive Forms Core Components for your AEM Cloud Service environment

Ensure that the [Adaptive Forms Core Components are enabled for your AEM Forms as a Cloud Service environment](enable-adaptive-forms-core-components.md). 

###  Add Adaptive Forms Client Libraries to your AEM Sites page or Experience Fragment 

To enable complete functionality of the Adaptive Forms Container component, add the Customheaderlibs and Customfooterlibs client libraries to your AEM Sites page using the deployment pipeline. To add the libraries:

1. Access and clone your [AEM Cloud Service Git Repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/content/managing-code/repositories.html).
1. Open the AEM Cloud Service Git Repository folder in a plan text editor. For example, Microsoft Visual Code.
1. Open the `ui.apps\src\main\content\jcr_root\apps\[your-project]\components\page\customheaderlibs.html` file and add the following code to the file:

    ```
        //Customheaderlibs.html
          
        <sly data-sly-use.clientlib="core/wcm/components/commons/v1/templates/clientlib.html">
        <sly data-sly-call="${clientlib.css @ categories='core.forms.components.runtime.all'}"/>
        </sly> 
    ```

1. Open the `ui.apps\src\main\content\jcr_root\apps\[your-project]\components\page\customfooterlibs.html` file and add the following code to the file:

    ```
        //customfooterlibs.html
        <sly data-sly-use.clientlib="core/wcm/components/commons/v1/templates/clientlib.html">
        <sly data-sly-test="${!wcmmode.edit}" data-sly-call="${clientlib.js @ categories='core.forms.components.runtime.all', async=true}"/>
        </sly> 
    ```

1. Open the `ui.apps\src\main\content\jcr_root\apps\[your-project]\components\xfpage\customheaderlibs.html` file and add the following code to the file:

    ```
        //Customheaderlibs.html
        <sly data-sly-use.clientlib="core/wcm/components/commons/v1/templates/clientlib.html">
        <sly data-sly-call="${clientlib.css @ categories='core.forms.components.runtime.all'}"/>
        </sly> 
    ```

1. Open the `ui.apps\src\main\content\jcr_root\apps\[your-project]\components\xfpage\customfooterlibs.html` file and add the following code to the file:

    ```
        //customfooterlibs.html
        <sly data-sly-use.clientlib="core/wcm/components/commons/v1/templates/clientlib.html">
        <sly data-sly-test="${!wcmmode.edit}" data-sly-call="${clientlib.js @ categories='core.forms.components.runtime.all', async=true}"/>
        </sly> 
    ```

1. [Run the deployment pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/site-creation/enable-front-end-pipeline.html) to deploy the client libraries to your AEM as a Cloud Service environment. 

### Enable Adaptive Forms Container for your AEM Sites page or Experience Fragment 

To enable [!UICONTROL Adaptive Forms Container] component in template's policy, perform the following steps:

1. Open the AEM Sites page or Experience Fragment for editing. To open the page for editing, select the page, and click Edit.
1. Open the template of your Sites or Experience Fragment page. To open the template, go to the [!UICONTROL Page Information] ![Page Information](/help/forms/assets/Smock_Properties_18_N.svg) > [!UICONTROL Edit Template]. It opens the corresponding template in template editor.
1. In the Structure view, click the **[!UICONTROL Policy]** ![Policy](/help/forms/assets/Smock_FeedManagement_18_N.svg) icon in the menu bar. In the **[!UICONTROL Allowed Components]** list and select the **[!UICONTROL Adaptive Forms Container]**  checkbox under the **[AEM Archetype Project Name] - Adaptive Form**.
1. Click **[!UICONTROL Done]**.

>[!VIDEO](https://video.tv.adobe.com/v/3419370?quality=12&learn=on)

+++

## Create an Adaptive Form {#create-an-adaptive-form-in-sites-editor-or-experience-fragment}

You can create a brand-new form from scratch, tailoring it specifically to your requirements and design preferences, directly in an AEM Sites page or in Experience Fragment. For single-use forms, direct authoring to an AEM Sites page is recommended, while Experience Fragments are ideal for forms that need to be reused across multiple pages on your website.

* [Create a form in an AEM Sites page](#create-an-adaptive-form-in-sites-editor)
* [Create a form in an Experience Fragment](#create-an-adaptive-form-in-experience-fragment) 
* [Convert an Adaptive Form in AEM Sites page to an Experience Fragment](#convert-an-adaptive-form-in-sites-page-to-an-experience-fragment) 

### Create a form in an AEM Sites page {#create-an-adaptive-form-in-sites-editor}

You can use the Adaptive Form Container component in AEM Page Editor to create a custom form. The component lets you create a form by dragging and dropping the form components. The form components are based on Core Components. You can easily customize these as per the requirement of your organization. 

>[!VIDEO](https://video.tv.adobe.com/v/3419284?quality=12&learn=on)

To create an Adaptive Form in a Sites page: 

1. Open the AEM Sites page in edit mode.
1. Drag-and-drop the **[!UICONTROL Adaptive Forms Container]** component from the Component Browser to the Sites page. It creates a space on the page for the form. You can use the layout mode to change the Size of the container space. 
1. Drag-and-drop Adaptive Form Core Components to the container space to create the form. 
1. Add the Submit button. 

Next, you [set the Submit Action](#configure-submit-action-for-form) and advanced properties. 

### Create a form in an Experience Fragment {#create-an-adaptive-form-in-experience-fragment}

You can extend the reach of your forms by adding them to AEM Experience Fragments, allowing for seamless reuse across multiple pages or sites. For example, you can include a newsletter signup form within an Experience Fragment. This lets you conveniently reuse the fragment across multiple pages of your website, eliminating the need to recreate the form repeatedly. Any updates or modifications made to the newsletter signup form within the Experience Fragment are automatically propagated to all the pages where it is utilized. This streamlines the process and ensures a seamless user experience while simplifying the management of your website's forms. 

To create an Adaptive Form in an Experience Fragment:

1. Open an Experience Fragment.
1. Drag-and-drop the **[!UICONTROL Adaptive Forms Container]** component from the Component Browser to the Experience Fragment. 
1. Drag-and-drop Adaptive Form Core Components to the container space in the Experience Fragment to create the form. 
1. Add the Submit button. 

Next, you [set the Submit Action](#configure-submit-action-for-form) and advanced properties. 

### Convert a form in AEM Sites page to an Experience Fragment {#convert-an-adaptive-form-in-sites-page-to-an-experience-fragment}

You can convert an existing Adaptive Form in a Sites Page Editor to an Experience Fragment to reuse the form across multiple pages or sites. 

To convert an Adaptive Form in AEM Sites page to an Experience Fragment:

1. Open the AEM Sites page containing the Adaptive Form (in Adaptive Forms Container component) in edit mode.
1. Open the Content Tree, and select the **[!UICONTROL Adaptive Forms Container]** that hosts your Adaptive Form. An AEM Sites page can host multiple Adaptive Forms. So, carefully select the correct Adaptive Forms Container. 
1. On the menu bar, select the ![Convert to experience fragment icon](/help/forms/assets/Smock_FilingCabinet_18_N.svg) Convert to Experience Fragment variation icon. 
    ![Click the file cabinet logo to convert an Adaptive Form in AEM Sites page to an Experience Fragment](/help/forms/assets/convert-form-in-sites-page-to-an-experience-fragment.png)
    
    A dialog box to convert the Adaptive Form container to a new Experience Fragment or add to an existing Experience Fragment appears 
1. On the Convert to Experience Fragment variation dialog box, set values for the following options:

    * **Action:** Select to create an Experience Fragment or Add to an existing Experience Fragment.
    * **Parent path:** Specify path of the folder to host the Experience Fragment in. The option is available only for creating an Experience Fragment. 
    * **Template:** Specify path of the Experience Fragment template. If you do not have an Experience Fragment template, [create it](/help/implementing/developing/extending/experience-fragments.md). The option is available only for adding Adaptive Form to an existing Experience Fragment. 
    * **Fragment title:** Specify title of the Experience Fragment. The title uniquely identifies an Experience Fragment 


## Configure Submit Action for a form in AEM Sites page or Expereince Fragment {#configure-submit-action-for-form}

A Submit Action lets you choose the destination of data captured via an Adaptive Form. It is triggered when a user clicks the Submit button on an Adaptive Form. Adaptive forms include some out of the box submit actions. You can also extend a default submit actions to create your own custom submit action. To configure a Submit Action for your form:

1. Open the AEM Page Editor or Experience Fragment that contains the Adaptive Form.
1. Open the Content Tree, and select the **[!UICONTROL Adaptive Forms Container]** that hosts your Adaptive Form. An AEM Sites page can host multiple Adaptive Forms. So, carefully select the correct Adaptive Forms Container. 
1. Click the Adaptive Form Container properties ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box to configure submit actions opens. 
  ![Click the Wrench icon to open Adaptive Form Container dialog box to configure Submit Action for an Adaptive Form](/help/forms/assets/adaptive-forms-container.png)
1. Select and configure a Submit action, based on your requirements. For detailed information about Submit Actions, see [Adaptive Form Submit Action](/help/forms/configuring-submit-actions.md)


## Configure a Schema or Form Data Model (FDM) for a form in AEM Sites page or Expereince Fragment {#configure-schema-or-data-model-for-form}

You can use the Form Data Model (FDM) to connect a form to a Data Source to send and receive data based on user actions. You can also connect a form to a JSON schema to receive the submitted data in a pre-defined format. Based on the requirement, connect your form to a JSON schema or Form data model(FDM):

* [Create a JSON Schema and upload to your environment](/help/forms/adaptive-form-json-schema-form-model.md)  or, 
* [Create a Form Data Model (FDM)](/help/forms/create-form-data-models.md)

To configure a JSON Schema or Form Data Model (FDM) for your form:

1. Open the AEM Page Editor or Experience Fragment that contains the Adaptive Form.
1. Open the Content Tree, and select the **[!UICONTROL Adaptive Forms Container]** that hosts your Adaptive Form. An AEM Sites page can host multiple Adaptive Forms. So, carefully select the correct Adaptive Forms Container. 
1. Click the Adaptive Form Container properties ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box to configure Data Models opens. 
![Click the Wrench icon to configure a Data Models for the Adaptive Form](/help/forms/assets/form-data-model-adaptive-forms-container.png)
1. Select and configure a JSON Schema or Form Data Model (FDM), based on your requirements. For detailed information about Submit Actions, see [Adaptive Form Submit Action](/help/forms/configuring-submit-actions.md). 

    * When you select the **[!UICONTROL Form Model]** option, use the **[!UICONTROL Select Form Data Model]** option to select a pre-configured Form Data Model (FDM).
    * When you select the **[!UICONTROL Schema]** option, use the **[!UICONTROL Schema]** option to select a JSON schema for your form.

1. Click **[!UICONTROL Done]**.

## Configure a pre-fill service for a form in AEM Sites page or Expereince Fragment {#configure-prefill-service-for-form}

You can use the prefill service to auto fill fields of an Adaptive Form using existing data. When a user opens a form, the values for those fields are prefilled. You can:

* [Create a custom pre-fill service](/help/forms/prepopulate-adaptive-form-fields.md)
* [Use Form Data Model Prefill service](#fdm-prefill-service)

### Use Form Data Model Prefill service to prepopulate fields of a form in AEM Sites page or Expereince Fragment {#fdm-prefill-service}

You can use the Form Data Model Prefill service to prepopulate fields of an Adaptive Form in AEM Sites page or Expereince Fragment using a Form Data Model or a custom pre-fill service. The Form Data Model Prefill service uses the [Get Service of configured Form Data Model](work-with-form-data-model.md#add-data-model-objects-and-services-add-data-model-objects-and-services) to retrieve data. To use Form Data Model Prefill service for an Adaptive Form:

1. Open the AEM Page Editor or Experience Fragment that contains the Adaptive Form.
1. Open the Content Tree, and select the **[!UICONTROL Adaptive Forms Container]** that hosts your Adaptive Form. An AEM Sites page can host multiple Adaptive Forms. So, carefully select the correct Adaptive Forms Container. 
1. Click the Adaptive Form Container properties ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box to configure Data Models opens. 
  ![Click the Wrench icon to open Adaptive Form Container dialog box to configure prefill service for the Adaptive Form](/help/forms/assets/adaptive-forms-container.png)
1. Select a form data model. Open the **[!UICONTROL Basic]** tab. In the prefill service, select **[!UICONTROL Form Data Model Prefill Service]**. 
1. Click **[!UICONTROL Done]**. Your Adaptive form is now configured to use Form Data Model Prefill. You can now, use the [rule editor](rule-editor.md) to create rules to prepopulate fields of the form.


## Redirect the user to a page or show a thank you message on form submission

On submission of a form, you can redirect the user to another webpage or a message. To redirect the user or configure the thank you message:

1. Open the AEM Page Editor or Experience Fragment that contains the Adaptive Form.
1. Open the Content Tree, and select the **[!UICONTROL Adaptive Forms Container]** that hosts your Adaptive Form. An AEM Sites page can host multiple Adaptive Forms. So, carefully select the correct Adaptive Forms Container. 

1. Open the **[!UICONTROL Submission]** tab. 

    * To configure a Redirect URL, for on Submit option, select the **[!UICONTROL Redirect to URL]** option, and browse and select an AEM Sites page, or provide URL of an external page.  
    * To configure a custom or thank you message, for on Submit option, select the **[!UICONTROL Show Message]** option, and provide a message in the **[!UICONTROL Message content]** box. It is a rich text box, you can use the full screen option to view all the available rich text items. 


<!--
## See next

* [Create style or themes for your forms](using-themes-in-core-components.md)
* [Add dynamic behavior to forms using the rule editor](rule-editor.md)
* [Set layout of forms for different screen sizes and device types](/help/sites-cloud/authoring/page-editor/responsive-layout.md)

-->

## See Also {#see-also}

{{see-also}}
* [Add dynamic behavior to forms using the rule editor](rule-editor.md)
* [Set layout of forms for different screen sizes and device types](/help/sites-cloud/authoring/page-editor/responsive-layout.md)


