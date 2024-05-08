---
title: How to add or create an Adaptive Form Core Components in AEM Sites page?
description: Use Adaptive Form Core Components in an AEM Sites page to fill and submit a form without leaving the AEM Sites pages.
feature: Adaptive Forms
hide: yes
hidefromtoc: yes
---
# Create or add an Adaptive Form using AEM Sites Editor {#add-an-adaptive-form-to-aem-sites-page}

You can seamlessly author or embed Adaptive Forms in an AEM Sites page to allow your users to fill and submit a form without leaving the Sites page. It helps user remain in context of other elements of the web page and simultaneously interact with the form. 
 
You can choose one the following methods to create or add an Adaptive Form to an AEM Sites page:

* **Create an Adaptive Form using Adaptive Forms Container component**: The [Adaptive Form Container](#af-container-component) component lets you build digital enrollment experiences by utilizing Adaptive Forms components directly within the AEM Sites editor. This integration provides a seamless experience to AEM Sites authors who want to create and manage forms within their AEM Sites pages.
 
* **Add an existing Adaptive Form**: The [Adaptive Forms - Embed(v2)](#embed-existing-af) component lets you easily add a pre-existing Adaptive Form into a page within AEM Sites. This feature enhances the adaptability and reusability of Adaptive Forms. This integration provides a convenient way for customers to reuse Adaptive Forms they have already created. 

* **Use Adaptive Forms Wizard to create a form**: Use the [Adaptive Forms - Embed(v2)](#embed-new-af) component to create an Adaptive Form from within the AEM Sites editor using Form Creation wizard. The form is saved as an external entity. You can reuse this form in other Sites pages and standalone forms also. 

* **Add multiple Adaptive Forms in an AEM Sites page**: To add multiple Adaptive Forms in an AEM Sites page, use the AEM Forms container components - [Adaptive Forms - Embed(v2)](#embed-new-af) and [Adaptive Form Container](#af-container-component). In case, you need to add more than one Adaptive Form as a div within an AEM Sites page, you can use the Adaptive Form Container component.

You can use the Rule Editor to add or control the dynamic behavior of Adaptive Form components. For example, hide or show a component. The Rule Editor is not available for non-Adaptive Form components. So, use your diligence while using non-Adaptive Form components in AEM Forms Container component.

## Create an Adaptive Form using Adaptive Forms Container component {#af-container-component}

The [!UICONTROL Adaptive Form Container] component allows building digital enrollment experiences using Adaptive Forms components in the AEM Sites editor. You can create an Adaptive Form by dragging and dropping the form components. 

### Prerequisites {#prerequisites-af-container}

+++ Enable **[!UICONTROL Adaptive Forms Container]** component.

  To enable [!UICONTROL Adaptive Forms Container] component in template's policy, perform the following steps:

  1. Go to the [!UICONTROL Page Information] > [!UICONTROL Edit Template]
  1. Click the [!UICONTROL Policy] and select the **[!UICONTROL Adaptive Forms Container]**  checkbox under the **[AEM Archetype Project Name] - Adaptive Form**.
  1. Click **[!UICONTROL Done]**.

  >[!VIDEO](https://video.tv.adobe.com/v/3419370?quality=12&learn=on)

+++

+++ Include Adaptive Forms Client Libraries to AEM Sites page

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

>[!VIDEO](https://video.tv.adobe.com/v/3419284?quality=12&learn=on)

Your form is ready. When you publish the AEM Sites page, it automatically publishes the Adaptive Form and its associated referenced assets.

#### Configure Adaptive Form Container Properties {#configure-additional-settings-container}

You can customize the advanced settings of the [!UICONTROL Adaptive Form Container] component. For example, 

* You can configure the Prefill Service to load an Adaptive Form with pre-filled values on a Site's page. 
* You can configure the Data Model settings to associate the Adaptive Form with a data source. 
* You can configure the submit actions to send the data on Microsoft&reg; OneDrive, Microsoft&reg; OneDrive, or other data sources on submission of a form. You can also create and select a custom Submit action for your Adaptive Forms.

To set the properties for the **[!UICONTROL Adaptive Forms Container]** component, click the ![settings_icon](/help/forms/assets/Smock_Wrench_18_N.svg) on the action bar. The **[!UICONTROL Edit Adaptive Forms Container]** dialog opens. 

![Edit Dialog](/help/forms/assets/adaptiveformcontainer-editdialog.png)

In the [!UICONTROL Edit Adaptive Forms Container] dialog, you can specify the following.
* **Basic Tab**
  * **Prefill Service**: You can use the prefill service to auto fill fields of an Adaptive Form using existing data. When a user opens a form, the values for those fields are prefilled. For information on prefill service, see [Prefill Adaptive Form fields](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/prepopulate-adaptive-form-fields.html#configuring-prefill-service-using-configuration-manager)
  * **Client library Category**: Specify the [JavaScript functions](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/add-rules-and-use-expressions-in-an-adaptive-form/rule-editor.html?lang=en#custom-functions) that are used in expressions and supported by Adaptive Forms.
* **Data Model**: A Data Model lets you integrate entities and services from disparate data sources to an Adaptive Form. Choose **[!UICONTROL Form Data Model]** if the Adaptive Form that you are creating involves fetching and writing data from and to multiple data source.
  * **Form data model**: A Form Data Model (FDM) lets an Adaptive Form communicate with disparate data sources. For information, on configuring a data source, see [Configure data sources](/help/forms/configure-data-sources.md).
  * **Schema**: Schema represents the structure in which data is produced or consumed by the back-end system in your organization. You can [associate the schema to an Adaptive Form](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/create-an-adaptive-form-on-forms-cs/adaptive-form-json-schema-form-model.html) and use its elements to add dynamic content to an Adaptive Form.

    >[!NOTE]
    >
    > After configuring the Form data model (FDM), you cannot change the associated Form Model. However, it is possible to modify the schema associated with the Form data model (FDM). 

* **Submission Tab**
   
  * **Redirect to URL** 
    * **Redirect URL/Path**: Specifies the URL or path to which an Adaptive Form is redirected after the submission.
   
    * **Submit Action**: A submit action is triggered when a user clicks the Submit button on an Adaptive Form. You can [configure the submit action on Adaptive Form](/help/forms/configuring-submit-actions.md). Adaptive forms provide the following submit actions out of the box:
      * Submit to REST endpoint
      * Send email
      * Submit using Form Data Model (FDM)
      * Invoke an AEM Workflow
      * Submit to SharePoint
      * Submit to OneDrive
      * Submit to Azure Blob Storage

  You can also [extend the default Submit Actions](custom-submit-action-form.md) to create your own custom Submit Action.  

* **Show Message**
  * **Message Content**: Write a message using the rich text editor to show on form submission. This option is available only when you choose to show a thank you message.

## Embed an Adaptive Form  {#aem-container-component}

Using **[!UICONTROL Adaptive Forms - Embed (V2)]** component, you can either embed new Adaptive Form or embed an existing Adaptive Form in the Site's page. The [!UICONTROL Adaptive Forms - Embed(v2)] component lets you:

* [Add an existing Adaptive Form](#embed-new-af)

* [Create and add a new Adaptive Form](#embed-existing-af)

### Prerequisites {#prerequisites}

+++ Enable the **Adaptive Forms - Embed** component.

  To enable [!UICONTROL Adaptive Forms - Embed(v2)] component in template's policy, perform the following steps:

  1. Go to the [!UICONTROL Page Information] > [!UICONTROL Edit Template]

  1. Click the [!UICONTROL Policy] and select the **[!UICONTROL Adaptive Form - Embed (v2)]** checkbox under the **[!UICONTROL [AEM Archetype Project Name] - Forms]** group .
  1. Click **[!UICONTROL Done]**.

  >[!VIDEO](https://video.tv.adobe.com/v/3419369?quality=12&learn=on)

+++

+++ Include Adaptive Forms Client Libraries to AEM Sites page

  When the **[!UICONTROL When form covers entire width of a page]** option is selected  in the **[!UICONTROL Form Containers]** configure dialog box and **Adaptive Forms using core components** are used, it is necessary to include the clientlibs on your corresponding Site's page. 

  ![Overlay Gif](/help/forms/assets/overlaycorecomponent.gif)

   To use Adaptive Forms components in an AEM Sites page, include the `Customheaderlibs` and `Customfooterlibs` client libraries to the AEM Sites page using the AEM Archetype/Git Repository and deployment pipeline.

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

      The `customfooterlibs.html` is used for JavaScript and the `customheaderlibs.html` for the CSS.

1. [Run the pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/site-creation/enable-front-end-pipeline.html) to deploy the changes. 

+++

### Add an existing Adaptive Form to AEM Sites page {#embed-existing-af}

1. Open the AEM Sites page in edit mode.
1. From the Component browser panel, drag-drop the [!UICONTROL Adaptive Forms - Embed] component on the page. 
1. Select the [!UICONTROL Adaptive Forms - Embed] component in the sites page and select ![settings_icon](/help/forms/assets/Smock_Wrench_18_N.svg) on the action bar. The **[!UICONTROL Edit Adaptive Forms - Embed]** dialog opens.
1. Browse and select the Adaptive Form to embed in the [!UICONTROL Asset Path]. 
1. Save the settings. The Adaptive Form  is now embedded in the page.

 >[!VIDEO](https://video.tv.adobe.com/v/3419368?quality=12&learn=on)
 


### Create and add new Adaptive Form to AEM Sites page {#embed-new-af}

1. Open the AEM Sites page in edit mode.
1. From the Component browser panel, drag-drop the [!UICONTROL Adaptive Forms - Embed(v2)] component on the page.
1. Click the **Plus** icon and you are redirected to the form creation wizard.

      ![Adaptive Forms - Embed Component](/help/forms/assets/aemformcontainer.png)

1. Create a new Adaptive Form from the [!UICONTROL Form Creation] wizard.
1. The [!UICONTROL Asset Path] already includes the path of a created Adaptive Form
1. Save the settings. The Adaptive Form  is now embedded in the page.

 >[!VIDEO](https://video.tv.adobe.com/v/3419366/adaptive-form-aem-forms?quality=12&learn=on)
 
#### Configure Adaptive Form - Embed(v2) Properties {#configure-adaptive-form-embed}

You can customize the advanced settings of the [!UICONTROL Adaptive Form - Embed(v2)] component. In the [!UICONTROL Edit Adaptive Forms - Embed(v2)] dialog, you can specify the following.

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

### Publish added Adaptive Forms using Adaptive Form - Embed(v2) component  {#publish-embedded-adaptive-form}

Consider the following scenarios for publishing added Adaptive Forms using the **[!UICONTROL Adaptive Form - Embed(v2)]** component: 

* When you publish an AEM Sites page for the first time, the forms added to the Sites page are published automatically. 
* When you modify an Adaptive Form added to an already published Sites page, manually publish the corresponding Adaptive Forms. 
* When you modify a Sites page and the corresponding Adaptive Forms, republish the Sites page and all the Adaptive Forms added to the Sites page.

### Modify added Adaptive Forms using Adaptive Form - Embed(v2) component  {#modifying-embedded-adaptive-form}

To modify any configuration or property of an Adaptive Form, do one of the following:

* Open the original form in an Adaptive Form  in respective editor and modify them.
* Select the Adaptive Form  from within the site page in edit mode and then select **[!UICONTROL Edit in a new window]**. The original form opens in edit mode that you can modify.

## Change Layout of an Adaptive Form added to an AEM Sites page {#change-layout-af-aem-sites-page} 

In AEM Sites page, the [Layout mode](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/authoring/features/responsive-layout.html?#defining-layouts-layout-mode) enables you to resize an Adaptive Form that is created or added to an AEM Sites page.

![AF-layout-support](/help/forms/assets/afsite-layoutsupport.gif)

AEM sites page maintains a reference to the Adaptive Form. When you translate an AEM Sites page, it automatically translates an Adaptive Form and its associated referenced assets using the [translation projects](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/reusing-content/translation/managing-projects.html?lang=en#adding-pages-assets-to-a-translation-job) into other languages.

## Best practices {#best-practices}

* Header and footer in the original form are not included in the embedded form.
* User drafts and submissions of embedded forms are supported and visible in Drafts and Submitted Forms tabs on the Forms Portal.

>[!MORELIKETHIS]
>
>* [Embed adaptive form based on core components to an external web page](/help/forms/embed-adaptive-form-core-components-external-web-page.md)
>* [Embed adaptive form in external web page](/help/forms/embed-adaptive-form-external-web-page.md)