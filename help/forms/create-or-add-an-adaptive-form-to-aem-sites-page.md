---
title: Create or add an Adaptive Form to AEM Sites page
description: Discover how to effortlessly create or seamlessly add an Adaptive Form to your AEM Sites page. Learn step-by-step techniques and best practices for integrating dynamic and customizable forms into your website, optimizing your digital experiences for maximum impact.
feature: Adaptive Forms
hide: yes
hidefromtoc: yes
---

# Create or add an Adaptive Form to AEM Sites page {#create-or-add-an-adaptive-form-to-aem-sites-page}

With AEM Forms, you can seamlessly incorporate adaptive forms into your web pages. This allows your visitors to conveniently fill and submit forms without ever leaving the page they are on. By doing so, they can effortlessly stay engaged with other elements of the website while actively interacting with the form. 

You can take full advantage of this feature by utilizing the following options:

*   **Add a custom form:** Build a brand-new form from scratch, tailoring it specifically to your requirements and design preferences.

*   **Enhance Experience Fragments:** Extend the reach of your forms by adding them to AEM Experience Fragments, allowing for seamless reuse across multiple pages or sites.

*   **Utilize approved templates:** Leverage pre-approved templates to quickly create forms that align with your organization's branding guidelines and design standards.

*   **Add existing forms:** Easily integrate forms that you have already created into your websites, enabling visitors to interact with them directly.

*   **Add multiple forms:**  Add multiple forms to a page to provide multiple choices to users based on their preferences and requirements. These can a combination of brand-new form from scratch and existing forms.

You can use AEM Sites editor to quickly create and add multiple forms to your AEM Sites pages. Using AEM Sites editor allows content authors to create seamless data capture experiences within a Sites page using the power of adaptive forms components including dynamic behavior, validations, data integration, generate document of record and business process automation. It also allows you to use various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager.

## Objective

* Learn to create an Adaptive Form using AEM Sites editor and Expereince Fragment
* Learn to set layout and theme for an Adaptive Form added to an AEM Sites page and 
* Create an Adaptive Form using AEM Sites editor and Expereince Fragment


## Considerations {#consideration}

AEM Forms provide Adaptive Form Container and Adaptive Forms – Embed components. You can use Adaptive Form Container to create and add a new form in an Experience Fragment or AEM Sites page, while Adaptive Forms – Embed component allows you to add an existing Adaptive Form or create a new form using Adaptive Forms editor. 

When you use the Adaptive Form Container to create or add a form, the forms undergo translation and localization through the AEM Sites translation flow. For each language, a separate copy (language copy) of the sites page and corresponding forms is generated and when a content author modifies a rule in a form on the parent page, the same changes must be made in all language copies of the form. Adaptive Form Container also allows you to use various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager.

When you create or add a form using the Adaptive Form-embed component, the forms undergo translation and localization using the AEM Forms translation flow. In this case, a single form is maintained and referenced in all the language copies of the Sites pages. Adaptive Form-embed component does not provide access to various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager.


## Before you start {#before-you-start}

+++  Enable Adaptive Forms Core Components for your environment

Ensure that the [Adaptive Forms Core Components are enabled for your AEM Forms as a Cloud Service environment](enable-adaptive-forms-core-components.md). 

+++ 

+++ Enable **[!UICONTROL Adaptive Forms Container]

To enable [!UICONTROL Adaptive Forms Container] component in template's policy, perform the following steps:

  1. Open the AEM Sites page for editing. To open the page for editing, select the page, and click Edit.
  1. Open the template of your Sites page. To open the template, go to the [!UICONTROL Page Information] ![Page Information](/help/forms/assets/Smock_Properties_18_N.svg) > [!UICONTROL Edit Template]. It open the corresponding template in template editor.
  1. In the Structure view, click the **[!UICONTROL Policy]** ![Policy](/help/forms/assets/Smock_FeedManagement_18_N.svg) icon in the menu bar. In the **[!UICONTROL Allowed Components]** list and select the **[!UICONTROL Adaptive Forms Container]**  checkbox under the **[AEM Archetype Project Name] - Adaptive Form**.
  1. Click **[!UICONTROL Done]**.

  >[!VIDEO](https://video.tv.adobe.com/v/3419370?quality=12&learn=on)

+++


+++  Add Adaptive Forms Client Libraries to your AEM Sites page

To enable complete functionality of the Adaptive Forms Container component, add the Customheaderlibs and Customfooterlibs client libraries to your AEM Sites page using the deployment pipeline. To add the libraries:

  1.  Access and clone your [AEM Cloud Service Git Repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/content/managing-code/repositories.html).
  1.  Open the AEM Cloud Service Git Repository folder in a plan text editor. For example, Microsoft Visual Code.
  1.  Open the `ui.apps/src/main/content/jcr_root/apps/[your-project]/components/page/.content.xml` file for editing and note down the value of `sling:resourceSuperType`. For example, note down the value `core/wcm/components/page/v3/page`.


        ![sling resource](/help/forms/assets/slingresource.png)
  
  1.  Navigate to `  ui.apps\src\main\content\jcr_root\apps\[your-project]\components\page\` `ui.apps/src/main/content/jcr_root/apps` and create a folder structure identical to value noted down in previous step. For example, if the value is similar to example in the previous step, the final node structure is `ui.apps/src/main/content/jcr_root/apps/core/wcm/components/page/v3/page`
    
        ![overlay structure](/help/forms/assets/overlaystructure.png)

  1.  Create `customheaderlibs.html` and `customfooterlibs.html` files at the node structure created in previous step and add the following content to the files:

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

  1.  [Run the deployment pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/site-creation/enable-front-end-pipeline.html) to deploy the client libraries to your AEM as a Cloud Service environment. 

+++ 

## Create an Adaptive Form {#create-an-adaptive-form-in-sites-editor-or-experience-fragment}

You can create a brand-new form from scratch, tailoring it specifically to your requirements and design preferences, directly in an AEM sites page or in Experience Fragment. For single-use forms, direct authoring to an AEM sites page is recommended, while Experience Fragments are ideal for forms that need to be reused across multiple pages on your website.

* [Create a form in an AEM Sites page](#create-an-adaptive-form-in-sites-editor)
* [Create a form in an Experience Fragment](#create-an-adaptive-form-in-experience-fragment) 

### Create a form in an AEM Sites page {#create-an-adaptive-form-in-sites-editor}

You can use the Adaptive Form Container component in AEM Sites editor to create a custom form. The component allows you to create a form by dragging and dropping the form components. The form components are based on Core Components. You can easily customize these as per the requirement of your organization. 

>[!VIDEO](https://video.tv.adobe.com/v/3419284?quality=12&learn=on)

To create an Adaptive Form in a Sites page: 

1. Open the AEM Sites page in edit mode.
1. Drag-and-drop the **[!UICONTROL Adaptive Forms Container]** component from the Component Browser to the Sites page. It creates a space on the page for the form. You can use the layout mode to change the Size of the container space. 
1. Drag-and-drop Adaptive Form Core Components to the container space to create the form. 
1. Add the Submit button. 

Next, you set the Submit action and advanced properties. 

### Create a form in an Experience Fragment {#create-an-adaptive-form-in-experience-fragment}

You can extend the reach of your forms by adding them to AEM Experience Fragments, allowing for seamless reuse across multiple pages or sites. For example, you can include a newsletter signup form within an Experience Fragment. This allows you to conveniently reuse the fragment across multiple pages of your website, eliminating the need to recreate the form repeatedly. Any updates or modifications made to the newsletter signup form within the Experience Fragment are automatically propagate to all the pages where it is utilized. This streamlines the process and ensures a seamless user experience while simplifying the management of your website's forms. 

To create an Adaptive Form in an Experience Fragment:

## Change Layout of an Adaptive Form {#change-layout-of-an-adaptive-form}

In AEM Sites page, use the [Layout mode](/help/sites-cloud/authoring/features/responsive-layout.md) to resize an Adaptive Form Container component added to an AEM Sites page. 
