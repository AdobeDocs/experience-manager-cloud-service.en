---
title: Add an Adaptive Form (Core Components) in AEM Sites page
seo-title: How to add an Adaptive Form (Core Components) to an AEM Sites page?
description: You can use Adaptive Form (Core Components) in an AEM Sites page to fill and submit a form without leaving the AEM Sites pages.
feature: Adaptive Forms
hide: yes
hidefromtoc: yes
---
# Add Adaptive Forms to an AEM Sites page {#add-an-adaptive-form-to-aem-sites-page}

## Overview {#overview}

You can seamlessly author or embed Adaptive Forms in an AEM Sites page to allow your users to fill and submit a form without leaving the Sites page. It helps user remain in context of other elements of the web page and simultaneously interact with the form. 
 
You can choose one the following methods to author or embed an Adaptive Form in an AEM Sites page:

* **Create an Adaptive Form by dragging and dropping form components to Adaptive Forms Container Component**: Use the [Adaptive Forms Container](#af-container-component) component to create a space within your web page that would host the Adaptive Form. You can drag and drop Adaptive Form component in this space to create a form. For example, see the below video to learn how to create an Adaptive Form using [!UICONTROL Adaptive Forms Container] component:

>[!VIDEO](/help/forms/assets/formcreationbyadaptiveformcontainer.mp4)

The [Adaptive Form Container](#af-container-component) component  allows you to build digital enrollment experiences by utilizing Adaptive Forms components directly within the AEM Sites editor. This integration provides a seamless experience to AEM Sites authors who want to create and manage forms within their AEM Sites pages.
 
* **Embed an existing Adaptive Form**: The [Adaptive Forms - Embed](#embed-existing-af) component allows you to easily incorporate a pre-existing Adaptive Form into a page within AEM Sites. For example, embed an Adaptive Form using the [!UICONTROL Adaptive Forms - Embed] component in Site's page as illustrated in the following video: 

>[!VIDEO](/help/forms/assets/embednewform_embed.mp4)

This feature enhances the adaptability and reusability of Adaptive Forms. This integration provides a convenient way for customers to reuse Adaptive Forms they have already created. 

* **Use Adaptive Forms Wizard to create a form**:

  Use the [Adaptive Forms - Embed](#embed-new-af) component to create an Adaptive Form from within the AEM Sites editor using Form Creation wizard. The form is saved as an external entity. You can reuse this form in other Sites pages and standalone forms also. 
For example, see the below video to learn how to create and embed a newly created Adaptive Form using the [!UICONTROL Adaptive Forms - Embed] component in Site's page. 

>[!VIDEO](/help/forms/assets/createnewform_embed.mp4)

### Consideration {#considerations}
 
You can us the Rule Editor to add or control the dynamic behavior of Adaptive Form components. For example, hide or show a component. The Rule Editor is not available for non-Adaptive Form components. So, use your diligence while using non-Adaptive Form components in AEM Forms Container component.

## Create an Adaptive Form using Adaptive Forms Container Component {#af-container-component}

The [!UICONTROL Adaptive Form Container] component allows building digital enrollment experiences using Adaptive Forms components in the AEM Sites editor. You can create an Adaptive Form by dragging and dropping the form components. 

### Prerequisites {#prerequisites-af-container}

+++ Enable **[!UICONTROL Adaptive Forms Container]** component in the associated template's policy.

  To enable [!UICONTROL Adaptive Forms Container] component in template's policy, perform the following steps:
  1. Go to the [!UICONTROL Page Information] > [!UICONTROL Edit Template]
  1. Click the [!UICONTROL Policy] and select the **Core Components Examples - Adaptive Form** checkbox.
  1. Click [!UICONTROL Done].

  >[!VIDEO](/help/forms/assets/adaptiveformcontainer.mp4)

+++

+++ Include the clientlibs on Site's page

  To use Adaptive Forms components in an AEM Sites page, include the Customheaderlibs and Customfooterlibs client libraries to the AEM Sites page using the AEM Archetype/Git Repository and deployment pipeline.

  1. Open your [AEM Forms Archetype or Cloned Git Repository](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html) project in a text editor. For example, Visual Studio Code. 
  1. Navigate to `ui.apps/src/main/content/jcr_root/apps/corecomponents/components/page/.content.xml`.
  1. Copy the value of `sling:resourceSuperType`. For instance, the value is `core/wcm/components/page/v3/page`.

      ![sling resource](/help/forms/assets/slingresource.png)

  1. Create the similar structure at the location `ui.apps/src/main/content/jcr_root/apps` same as `core/wcm/components/page/v3/page`.

      ![overlay structure](/help/forms/assets/overlaystructure.png)

  1. Add `customheaderlibs.html` and `customfooterlibs.html` files.

        ```
        //Customheaderlibs.html
        <sly data-sly-use.clientlib="core/wcm/components/commons/v1/templates/clientlib.html">
            <sly data-sly-call="${clientlib.css @ categories='core.forms.components.runtime.all'}"/>
        </sly> 

        //customfooterlibs.html
        <sly data-sly-use.clientlib="core/wcm/components/commons/v1/templates/clientlib.html">
            <sly data-sly-test="${!wcmmode.edit}" data-sly-call="${clientlib.js @ categories='core.forms.components.runtime.all', async=true}"/>
        </sly> 
        ```

      The customfooterlibs.html is used for JavaScript and the customheaderlibs.html for the css.

1. [Run the pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/site-creation/enable-front-end-pipeline.html) to deploy the changes. 

+++

### Create an Adaptive Form using Adaptive Forms Container component {#create-af-using-af-container}


To create an Adaptive Form using [!UICONTROL Adaptive Forms Container] component:

1. Open the AEM Sites page in edit mode.
1. From the Component browser panel, drag-drop the **[!UICONTROL Adaptive Forms Container]** component on the page. 
1. Create an Adaptive Form using the Adaptive Forms components. 
1. Save the settings. 

>[!VIDEO](/help/forms/assets/af-container.mp4)

Your form is ready. When you publish the AEM Sites page, it automatically publishes an Adaptive Form and its associated referenced assets.

#### Configure Adaptive Form Container Properties {#configure-additional-settings-container}

You can customize the advanced settings of the [!UICONTROL Adaptive Form Container] component. For example, you can configure the Prefill Service to load an Adaptive Form with pre-filled values on a Site's page. You configure the Data Model settings to associate the Adaptive Form with a data model. If you want to save the data on OneDrive or SharePoint when submitting an Adaptive Form, you configure the settings for Submission action. You can also add a custom Submit action for your Adaptive Forms.

To set the properties for the **[!UICONTROL Adaptive Forms Container]** component, click the ![settings_icon](/help/forms/assets/Smock_Wrench_18_N.svg) on the action bar. The **[!UICONTROL Edit Adaptive Forms Container]** dialog opens. 

![Edit Dialog](/help/forms/assets/adaptiveformcontainer-editdialog.png)

In the [!UICONTROL Edit Adaptive Forms Container] dialog, you can specify the following.
* **Basic Tab**
  * **Prefill Service**: You can use the prefill service to auto fill fields of an Adaptive Form using existing data. When a user opens a form, the values for those fields are prefilled. For information on prefill service, see [Prefill Adaptive Form fields](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/prepopulate-adaptive-form-fields.html#configuring-prefill-service-using-configuration-manager)
  * **Client library Category**: Specify the [JavaScript functions](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/add-rules-and-use-expressions-in-an-adaptive-form/rule-editor.html?lang=en#custom-functions) that are used in expressions and supported by Adaptive Forms.
* **Data Model**: A Data Model lets you integrate entities and services from disparate data sources to an Adaptive Form. Choose **[!UICONTROL Form Data Model]** if the Adaptive Form that you are creating involves fetching and writing data from and to multiple data source.
  * **Form data model**: A Form Data Model lets an Adaptive Form communicate with disparate data sources. For information, on configuring a data source, see [Configure data sources.](/help/forms/configure-data-sources.md)
  * **Schema**: Schema represents the structure in which data is produced or consumed by the back-end system in your organization. You can [associate the schema to an Adaptive Form](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/create-an-adaptive-form-on-forms-cs/adaptive-form-json-schema-form-model.html) and use its elements to add dynamic content to an Adaptive Form.

    >[!NOTE]
    >
    > After configuring the Form data model, you can not change the associated Form Model. However, it is possible to modify the schema associated with the Form data model. 

* **Submission Tab**
   
  * **Redirect to URL** 
    **Redirect URL/Path**: Specifies the URL or path to which an Adaptive Form is redirected after the submit action.
   
    **Submit Action**: A submit action is triggered when a user clicks the Submit button on an Adaptive Form. You can [configure the submit action on Adaptive Form](/help/forms/configuring-submit-actions.md). Adaptive forms provide a few out of the box submit actions:
      * Submit to REST endpoint
      * Send email
      * Submit using Form Data Model
      * Invoke an AEM Workflow
      * Submit to SharePoint
      * Submit to OneDrive
      * Submit to Azure Blob Storage

  You can also [extend the default Submit Actions](custom-submit-action-form.md) to create your own custom Submit Action.  

* **Show Message**
  * **Message Content**: Write a message using the rich text editor to show on form submission. This option is available only when you choose to show a thank you message.

## Embed an existing Adaptive Form  {#aem-container-component}

Using **[!UICONTROL Adaptive Forms - Embed]** component, you can either embed new Adaptive Form or embed an existing Adaptive Form in the Site's page. The [!UICONTROL Adaptive Forms - Embed] component allows you to:

* [Embe an existing Adaptive Form](#embed-new-af)

* [Create and embed a new Adaptive Form](#embed-existing-af)

### Prerequisites {#prerequisites}

+++ Enable the **Adaptive Forms - Embed** component in the associated template's policy.

  To enable [!UICONTROL Adaptive Forms - Embed] component in template's policy, perform the following steps:
  1. Go to the [!UICONTROL Page Information] > [!UICONTROL Edit Template]
  1. Click the [!UICONTROL Policy] and select the **Core Content** checkbox.
  1. Click [!UICONTROL Done].

  >[!VIDEO](/help/forms/assets/enableadaptiveform-embedtemplate.mp4)

+++

+++ Include the clientlibs on Site's page

  When the **[!UICONTROL When form covers entire width of a page]** option is selected  in the **[!UICONTROL Form Containers]** configure dialog box and **Adaptive Forms using core components** are used, it is necessary to include the clientlibs on your corresponding Site's page. 

  ![Overlay Gif](/help/forms/assets/overlaycorecomponent.gif)

   To use Adaptive Forms components in an AEM Sites page, include the Customheaderlibs and Customfooterlibs client libraries to the AEM Sites page using the AEM Archetype/Git Repository and deployment pipeline.

  1. Open your [AEM Forms Archetype or Cloned Git Repository](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html) project in a text editor. For example, Visual Studio Code. 
  1. Navigate to `ui.apps/src/main/content/jcr_root/apps/corecomponents/components/page/.content.xml`.
  1. Copy the value of `sling:resourceSuperType`. For instance, the value is `core/wcm/components/page/v3/page`.

      ![sling resource](/help/forms/assets/slingresource.png)

  1. Create the similar structure at the location `ui.apps/src/main/content/jcr_root/apps` same as `core/wcm/components/page/v3/page`.

      ![overlay structure](/help/forms/assets/overlaystructure.png)

  1. Add `customheaderlibs.html` and `customfooterlibs.html` files.

      ```
      //Customheaderlibs.html
      <sly data-sly-use.clientlib="core/wcm/components/commons/v1/templates/clientlib.html"
          data-sly-use.form="com.adobe.cq.forms.core.components.models.aemform.AEMForm">
          <sly data-sly-test="${form.formVersion=='2.1' && !wcmmode.edit}" data-sly-call="${clientlib.css @ categories='core.forms.components.runtime.all'}"/>
      </sly>

      //customfooterlibs.html
      <sly data-sly-use.clientlib="core/wcm/components/commons/v1/templates/clientlib.html"
        data-sly-use.form="com.adobe.cq.forms.core.components.models.aemform.AEMForm">
        <sly data-sly-test="${form.formVersion=='2.1' && !wcmmode.edit}" data-sly-call="${clientlib.js @ categories='core.forms.components.runtime.all', async=true}"/>
      </sly>
      ```

      The customfooterlibs.html is used for JavaScript and the customheaderlibs.html for the CSS.

1. [Run the pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/site-creation/enable-front-end-pipeline.html) to deploy the changes. 

+++

### Embed new Adaptive Form {#embed-new-af}

1. Open the AEM Sites page in edit mode.
1. From the Component browser panel, drag-drop the [!UICONTROL Adaptive Forms - Embed] component on the page.
1. Click the **Plus** icon and you are redirected to the form creation wizard.

      ![Adaptive Forms - Embed Component](/help/forms/assets/aemformcontainer.png)

1. Create a new Adaptive Form from the [!UICONTROL Form Creation] wizard.
1. The [!UICONTROL Asset Path] already includes the path of a created Adaptive Form
1. Save the settings. The Adaptive Form  is now embedded in the page.

### Embed existing Adaptive Form {#embed-existing-af}

1. Open the AEM Sites page in edit mode.
1. From the Component browser panel, drag-drop the [!UICONTROL Adaptive Forms - Embed] component on the page. 
1. Tap the [!UICONTROL Adaptive Forms - Embed] component in the sites page and tap ![settings_icon](/help/forms/assets/Smock_Wrench_18_N.svg) on the action bar. The **[!UICONTROL Edit Adaptive Forms - Embed]** dialog opens.
1. Browse and select the Adaptive Form to embed in the [!UICONTROL Asset Path]. 
1. Save the settings. The Adaptive Form  is now embedded in the page.

#### Configure Adaptive Form _ Embed Properties

You can customize the advanced settings of the [!UICONTROL Adaptive Form - Embed] component. In the [!UICONTROL Edit Adaptive Forms - Embed] dialog, you can specify the following.
* **Asset Path**: Browse and select the Adaptive Form to embed. It is auto-populated if you dropped it from the Assets browser.
* **Post Submission** : Select the action to trigger on form submission. You can choose to show a thank you message or a thank you page.
  * **Show Thank You Message**: Write a message using the rich text editor to show on form submission. This option is available only when you choose to show a thank you message.
  * **Show Thank You Page**: Browse and select the page to display on form submission. This option is available only when you choose to show a thank you page.
  * **Redirect to thank you page**: Enable the option to replace the page containing the embedded Adaptive Form with thank you page. Otherwise, the thank you page replaces the Adaptive Form in the [!UICONTROL Adaptive Forms - Embed] component, without refreshing underlying sites the page. This option is available only when you choose to show a thank you page.
* **Use Page Language**: Use local of the AEM Sites page instead locale of Adaptive Form.
* **Set Focus on Form**: Select to set the focus on the first field of the Adaptive Form.
* **Form covers entire width of the frame**: If checked, iframe is not used to render the form. 
* **Height**: Specify the height of the container. Leave it blank to automatically resize the container.
* **CSS Client library**: Specify path to a CSS client library.

### Publish embedded Adaptive Form {#publishing-embedded-adaptive-form}

Let's consider the following scenarios for publishing an embedded Adaptive Form in AEM sites page:

* If you are publishing the AEM sites page for the first time and it includes an embedded Adaptive Form, publish the sites page and the embedded asset.
* If you modified only the embedded Adaptive Form  in a published site page, publish the original asset and the changes reflect in the published site page. The published site page includes a reference to the asset and does not require republishing the page.
* If you modified the sites page and the embedded Adaptive Form , republish the sites page and the embedded asset.

### Modify embedded Adaptive Form  {#modifying-embedded-adaptive-form}

To modify any configuration or property of the embedded Adaptive Form, do one of the following.

* Open the original form in an Adaptive Form  in respective editor and modify them.
* Tap the Adaptive Form  from within the site page in edit mode and then tap **[!UICONTROL Edit in a new window]**. The original form opens in edit mode that you can modify.

>[!NOTE]
>
>The changes made in the original Adaptive Form  automatically reflect in the embedded form. However, republish the Adaptive Form, or the Site's page to reflect the changes in the published page.

### Best practices {#best-practices}

* Header and footer in the original form are not included in the embedded form.
* User drafts and submissions of embedded forms are supported and visible in Drafts and Submitted Forms tabs on the Forms Portal.

[In AEM Sites page, the Layout mode](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/authoring/features/responsive-layout.html?#defining-layouts-layout-mode) enables you to resize an Adaptive Form that has been created or embedded within a page of an AEM Site.

![AF-layout-support](/help/forms/assets/afsite-layoutsupport.gif)

AEM sites page maintains a reference to the Adaptive Form. When you translate an AEM Sites page, it automatically translates an Adaptive Form and its associated referenced assets using the [translation projects](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/reusing-content/translation/managing-projects.html?lang=en#adding-pages-assets-to-a-translation-job) into other languages.

