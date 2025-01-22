---
title: How to add an Adaptive Form to an AEM Sites page?
description: Seamlessly embed Adaptive Forms in an AEM Sites page or a web page hosted outside AEM.
feature: Adaptive Forms
role: Admin, User, Developer
Keywords: Forms AEM Sites, Embed Form to a Sites page, Adaptive Forms AEM Sites, Embed Adaptive Forms to AEM Page, Embed Forms in an AEM Sites page
exl-id: 359b05e8-d8c1-4a77-9e70-6f6b6e668560
---
# Embed an Adaptive Form to an AEM sites page {#embed-an-adaptive-form-to-aem-sites-page}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/embed-adaptive-form-aem-sites.html)                  |
| AEM as a Cloud Service     | This article        |


## Overview {#overview}

AEM Forms allow form developers to seamlessly embed Adaptive Forms in an AEM Sites page or a web page hosted outside AEM. The embedded Adaptive Form is fully functional and users can fill and submit the form without leaving the page. It helps user remain in context of other elements on the web page and simultaneously interact with the form. This allows your users to conveniently fill and submit forms without ever leaving the page they are on. This integration provides a convenient way to reuse Adaptive Forms they have already created. 

You can use AEM Page Editor to quickly embed multiple forms to your AEM Sites pages. Using AEM Page Editor allows content authors to create seamless data capture experiences within a Sites page using the power of Adaptive Forms components including dynamic behavior, validations, data integration, generate document of record and business process automation. It also lets you use various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager.

AEM Forms provide **[!UICONTROL Adaptive Form Container]** and **[!UICONTROL Adaptive Forms – Embed(v2)]** components. You can use **[!UICONTROL Adaptive Forms – Embed(v2)]** component to add an existing Adaptive Form or create a form using Adaptive Forms Editor , while **[!UICONTROL Adaptive Form Container]** to create new form within an Experience Fragment or AEM Sites page.

![An example of an Adaptive Form in an AEM Sites page](/help/forms/assets/adaptive-form-in-sites-page.png)

<!-- For information about embedding an Adaptive Form in an external web page, see [Embed Adaptive Form in external web page](/help/forms/using/embed-adaptive-form-external-web-page.md). 

## Why embed an Adaptive Form in AEM Sites page or AEM Experience Fragment? 

Using **[!UICONTROL Adaptive Forms – Embed(v2)]** in AEM Page Editor lets you create seamless data capture experiences within a Sites page using the power of Adaptive Forms components including dynamic behavior, validations, data integration, generate document of record and business process automation. It also lets you use various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager, enhancing the overall form creation and management experience. Let's explore some of these features:

* **Versioning:** AEM Sites pages offer [robust versioning capabilities](/help/sites-cloud/authoring/sites-console/page-versions.md), allowing you to track and manage different versions of your forms. This enables you to make changes and enhancements to forms while maintaining the ability to roll back to previous versions if needed. Versioning ensures a controlled and organized approach to form development and evolution.
* **Targeting (Integration with Adobe Target):** With AEM Sites pages targeting capabilities, you can also [personalize the form experience for different audiences](/help/sites-cloud/integrating/integrating-adobe-target.md). By using user segments and targeting criteria, you can tailor the form's content, design, or behavior to specific groups of users. This enables you to provide a personalized and relevant form experience, increasing engagement and conversion rates.
* **Translation:** AEM Sites [seamless integration with translation services](/help/sites-cloud/administering/translation/overview.md), allowing you to translate forms into multiple languages easily. This feature simplifies the localization process, ensuring that your forms are accessible to a global audience. You can manage translations efficiently within AEM translation projects, reducing time and effort required for multilingual form support. See considerations section for more information on translation.  
* **Multi-site Management and Live Copy:** AEM Sites provide robust [Multi-site Management and Live Copy capabilities](/help/sites-cloud/administering/msm/overview.md), enabling you to create and manage multiple websites within a single environment. This feature now lets you reuse forms across different sites, ensuring consistency and reducing duplication efforts. With centralized control and management, you can efficiently maintain and update forms across multiple websites.
* **Themes:** AEM Sites pages provide a framework for designing and maintaining consistent visual styles across multiple web pages. These define colors, fonts, style sheets, and other visual elements that contribute to the overall look and feel of the website. [You can use the themes designed for an AEM Sites page for an Adaptive Form, saving time and effort](/help/sites-cloud/administering/site-creation/site-themes.md#using-site-themes-using-themes). 
* **Tagging:** AEM Sites pages allow you to [assign tags or labels to a page, an asset, or other content](/help/implementing/developing/introduction/tagging-framework.md). Tags are keywords or metadata labels that provide a way to categorize and organize content based on specific criteria. You can assign one or more tags to pages, assets, or any other content items within AEM to improve search and categorize the assets. 
* **Locking and Unlocking content:** AEM Sites allow users to [control access and modifications to pages](/help/sites-cloud/authoring/page-editor/edit-content.md) within the AEM Sites environment. When a page is locked, it means that it is protected from unauthorized changes or edits by other users. Only the user who has locked the content or a designated administrator can unlock it to allow modifications. 

In addition, Adaptive Forms in AEM Page Editor use [Adaptive Forms Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html?lang=en#features). These Core Components provide a standard and easier methods to style and customize the components, identical to [AEM Sites WCM Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html?lang=en).

--> 

## How to create or embed an Adaptive Form in AEM Sites page or in AEM Experience Fragment? {#various-options-to-create-or-embed-an-adaptive-form-in-aem-sites-page-or-aem-experience-fragment}

You can take full advantage of this feature by using the following options:

* **[Create an Adaptive Form using approved templates and embed it to an AEM Sites page](#embed-form-using-adaptive-form-wizzard-aem-sites):** You can use pre-approved templates to quickly create and embed Adaptive Forms that align with your organization's branding guidelines and design standards.  

* **[Embed existing forms to an AEM Sites page](#embed-an-adaptive-form-in-sites-editor):** You can easily integrate forms that you have already created into your websites, enabling visitors to interact with them directly.  

* **[Convert an embedded Adaptive Form to Experience Fragment](#convert-an-adaptive-form-in-sites-page-to-an-experience-fragment):** Convert an embedded Adaptive Form added to an AEM Sites page to an Experience Fragment for reusing the form across multiple AEM Sites pages.

* **[Create and add a custom Adaptive Form to an AEM Sites page](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md#create-an-adaptive-form-in-sites-editor-or-experience-fragment):** You can use the **[!UICONTROL Adaptive Form Container]** component to build a brand-new form from scratch, tailoring it specifically to your requirements and design preferences.

* **[Create and add a custom Adaptive Form to an Experience Fragments](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md#create-an-adaptive-form-in-sites-editor):** You can extend the reach of your forms by adding them to AEM Experience Fragments, allowing for seamless reuse across multiple pages or sites.

* **Add multiple forms to an AEM Sites page or Experience Fragment:**  You can create or add multiple Adaptive Forms to an AEM Sites page to provide multiple choices to users based on their preferences and requirements. You can use AEM Page Editor to quickly embed multiple forms to your AEM Sites pages. You can use the **[!UICONTROL Adaptive Form Container]** component multiple times to add Adaptive Forms in an AEM Sites page. You can use the **[!UICONTROL Adaptive Forms - Embed]** component multiple times in an AEM Sites page, only if **[!UICONTROL Form covers entire width of the frame]** option is selected. In case the **[!UICONTROL Form covers entire width of the frame]** option is not checked, AEM Sites page supports only one Adaptive Form to exist without an iframe. To add more Adaptive Forms using  the **[!UICONTROL Adaptive Forms - Embed]** component, select **[!UICONTROL Form covers entire width of the frame]** option. 

## Considerations to embed an Adaptive Form in AEM Sites page or AEM Experience Fragment {#consideration}

* When you create or add a form using the **[!UICONTROL Adaptive Forms – Embed(v2)]** component, the forms undergo translation and localization using the AEM Forms translation flow. In this case, a single form is maintained and referenced in all the language copies of the Sites pages. **[!UICONTROL Adaptive Forms – Embed(v2)]** component does not provide access to various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager.

* When you use the **[!UICONTROL Adaptive Form Container]** to create a form, the forms undergo translation and localization through the AEM Sites translation flow. For each language, a separate copy (language copy) of the sites page and corresponding forms is generated and when a content author modifies a rule in a form on the parent page, the same changes must be made in all language copies of the form. **[!UICONTROL Adaptive Form Container]** also lets you use various features of AEM Sites pages like, versioning, targeting, translation, and multi-site manager.


## Requirements to embed an Adaptive Form in AEM Sites page or AEM Experience Fragment {#before-you-start-embedding-an-adaptive-form}

Before you start embedding a new Adaptive Form or a pre-existing Adaptive Form using **[!UICONTROL Adaptive Forms – Embed(v2)]**, enable **Adaptive Forms Core Components** and add **Adaptive Forms Client Libraries** to your AEM Sites page:

### Enable Adaptive Forms Core Components for your AEM Cloud Service environment

Ensure that the [Adaptive Forms Core Components are enabled for your AEM Forms as a Cloud Service environment](enable-adaptive-forms-core-components.md). 

### Add Adaptive Forms Client Libraries to your AEM Sites page or Experience Fragment 

When the **[!UICONTROL When form covers entire width of a page]** option is selected in the **[!UICONTROL Form Containers]** configure dialog box and Adaptive Forms using Core Components are used, it is necessary to include the client libraries on your corresponding Site's page. 

![When form covers entire width of a page option is selected and adaptive form with core components are used](/help/forms/assets/overlaycorecomponent.gif)


Add the **Customheaderlibs** and **Customfooterlibs** client libraries to your AEM Sites page using the deployment pipeline. To add the client libraries:

  1. Access and clone your [AEM Cloud Service Git Repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/content/managing-code/repositories.html).
  1. Open the AEM Cloud Service Git Repository folder in a plan text editor. For example, Microsoft&reg; Visual Code.
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
 
### Enable Adaptive Forms – Embed(v2) for your AEM Sites page or Experience Fragment 

To enable **[!UICONTROL Adaptive Forms – Embed(v2)]** component in template's policy, perform the following steps:

  1. Open the AEM Sites page or Experience Fragment for editing. To open the page for editing, select the page, and click **[!UICONTROL Edit]**.
  1. Open the template of your Sites or Experience Fragment page. To open the template, go to the **[!UICONTROL Page Information]** ![Page Information](/help/forms/assets/Smock_Properties_18_N.svg) > **[!UICONTROL Edit Template]**. It opens the corresponding template in template editor.
  1. In the Structure view, click the **[!UICONTROL Policy]** ![Policy](/help/forms/assets/Smock_FeedManagement_18_N.svg) icon in the menu bar. In the **[!UICONTROL Allowed Components]** list and select the **[!UICONTROL Adaptive Forms – Embed(v2)]**  checkbox under the **[AEM Archetype Project Name] - Adaptive Form**.
  1. Click **[!UICONTROL Done]**.

>[!VIDEO](https://video.tv.adobe.com/v/3419369?quality=12&learn=on)

## Embed an Adaptive Form using the Adaptive Forms - Embed(v2) component {#embed-an-adaptive-form-in-sites-editor-or-experience-fragment}

Use the **[!UICONTROL Adaptive Forms - Embed(v2)]** component to create an Adaptive Form directly within the AEM Sites editor using the Form Creation wizard. The resulting form is saved as an external entity, allowing for its reuse in other Sites pages and standalone forms. You can embed a brand-new form from scratch, tailoring it specifically to your requirements and design preferences, directly in an AEM Sites page or in Experience Fragment. For single-use forms, direct authoring to an AEM Sites page is recommended, while Experience Fragments are ideal for forms that must be reused across multiple pages on your website. 

You can easily embed a new form using **[!UICONTROL Adaptive Forms - Embed(v2)]**.  For example, imagine incorporating a new contact us form into an AEM Sites page or AEM Experience Fragment. Any updates or modifications made to the contact form within the AEM Sites page or Experience Fragment automatically apply to all the pages where it is deployed. This simplifies the management of your website's forms, ensuring a seamless user experience while streamlining the overall process.

Using **[!UICONTROL Adaptive Forms - Embed(v2)]**, you can:

* [Embed new form using the Adaptive Forms Wizard in AEM Sites Page](#embed-form-using-adaptive-form-wizzard-aem-sites)
* [Embed new form using the Adaptive Forms Wizard in an Experience Fragment](#embed-form-using-adaptive-form-wizzard-experience-fragment)
* [Embed an existing Adaptive Form in an AEM Sites page](#embed-an-adaptive-form-in-sites-editor)
* [Embed an existing form in an Experience Fragment](#embed-an-adaptive-form-in-experience-fragment)
* [Convert an Adaptive Form in AEM Sites page to an Experience Fragment](#convert-an-adaptive-form-in-sites-page-to-an-experience-fragment) 

### Embed new form using the Adaptive Forms Wizard in AEM Sites Page {#embed-form-using-adaptive-form-wizzard-aem-sites}

Steps to embed new form to an AEM Sites page are:

1. Open the AEM Sites page in edit mode.
1. From the Component browser panel, drag-drop the **[!UICONTROL Adaptive Forms - Embed(v2)]** component on the page.
1. Click the **Plus** icon and you are redirected to the form creation wizard.

      ![Adaptive Forms - Embed Component](/help/forms/assets/aemformcontainer.png)

1. Create a new Adaptive Form from the **[!UICONTROL Form Creation]** wizard.
The **[!UICONTROL Asset Path]** already includes the path of a created Adaptive Form
1. Save the settings. The Adaptive Form  is now embedded in the page.

 >[!VIDEO](https://video.tv.adobe.com/v/3419366/adaptive-form-aem-forms?quality=12&learn=on)

 Next, you can [set the Submit Action](/help/forms/configuring-submit-actions.md) and advanced properties of an embedded Adaptive Form using the Form creation wizard. 


### Embed new form using the Adaptive Forms Wizard in an Experience Fragment {#embed-form-using-adaptive-form-wizzard-experience-fragment}

Steps to embed new form to an Experience Fragment are:

1. Open the Experience Fragment in edit mode.
1. From the Component browser panel, drag-drop the **[!UICONTROL Adaptive Forms - Embed(v2)]** component on the page.
1. Click the **Plus** icon and you are redirected to the form creation wizard.

    ![Adaptive Forms - Embed Component](/help/forms/assets/aemformcontainer.png)

1. Create a new Adaptive Form from the **[!UICONTROL Form Creation]** wizard.
The **[!UICONTROL Asset Path]** already includes the path of a created Adaptive Form
1. Save the settings. The Adaptive Form  is now embedded in the Experience Fragment.

Next, you can [set the Submit Action](/help/forms/configuring-submit-actions.md) and advanced properties of an embedded Adaptive Form using the Form creation wizard. 

### Embed an existing Adaptive form in an AEM Sites page {#embed-an-adaptive-form-in-sites-editor}

With the **[!UICONTROL Adaptive Forms - Embed(v2)]** component, you can effortlessly integrate a pre-existing Adaptive Form into a page within AEM Sites. This feature significantly enhances the adaptability and reusability of Adaptive Forms, offering customers a convenient way to reuse forms they have already created. For example, imagine incorporating a contact form to an AEM Sites page, eliminating the need to recreate the form multiple times.

To embed an existing Adaptive Form in a Sites page: 

1. Open the AEM Sites page in edit mode.
1. Drag-and-drop the **[!UICONTROL Adaptive Forms - Embed(v2)]** component from the Component Browser to the Sites page. 
1. Select the **[!UICONTROL Adaptive Forms - Embed]** component in the Sites page and select ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) on the action bar. The **[!UICONTROL Edit Adaptive Forms - Embed(v2)]** dialog opens.
1. Browse and select the Adaptive Form to embed in the **[!UICONTROL Asset Path]**.
1. Save the settings. The Adaptive Form is now embedded in the page.

>[!VIDEO](https://video.tv.adobe.com/v/3419368?quality=12&learn=on)

Next, you can [set the Submit Action](/help/forms/configuring-submit-actions.md) and advanced properties of an embedded Adaptive Form using the Form creation wizard. 

### Embed an Existing Adaptive Form in an Experience Fragment {#embed-an-adaptive-form-in-experience-fragment}

You can also extend the accessibility of your forms by embedding them to AEM Experience Fragment. To embed an Adaptive Form in an Experience Fragment:

1. Open an Experience Fragment in edit mode.
1. Drag-and-drop the **[!UICONTROL Adaptive Forms - Embed(v2)]** component from the Component Browser to the Experience Fragment. 
1. Select the **[!UICONTROL Adaptive Forms - Embed]** component in the Experience Fragment and select ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) on the action bar. The **[!UICONTROL Edit Adaptive Forms - Embed(v2)]** dialog opens.
1. Browse and select the Adaptive Form to embed in the **[!UICONTROL Asset Path]**.
1. Save the settings. The Adaptive Form is now embedded to the Experience Fragment. 

Next, you can [set the Submit Action](/help/forms/configuring-submit-actions.md) and advanced properties of an embedded Adaptive Form using the Form creation wizard.

### Convert a form in AEM Sites page to an Experience Fragment {#convert-an-adaptive-form-in-sites-page-to-an-experience-fragment}

You can convert an existing Adaptive Form in a Sites Page Editor to an Experience Fragment to reuse the form across multiple pages or sites. 

To convert an Adaptive Form in AEM Sites page to an Experience Fragment:

1. Open the AEM Sites page containing the Adaptive Form (in Adaptive Forms Container component) in edit mode.
1. Open the Content Tree, and select the **[!UICONTROL Adaptive Forms Container]** that hosts your Adaptive Form. An AEM Sites page can host multiple Adaptive Forms. So, carefully select the correct Adaptive Forms Container. 
1. On the menu bar, select the ![Convert to experience fragment variation icon](/help/forms/assets/Smock_FilingCabinet_18_N.svg) Convert to Experience Fragment variation icon. 

    ![Click the file cabinet logo to convert an Adaptive Form in AEM Sites page to an Experience Fragment](/help/forms/assets/convert-form-in-sites-page-to-an-experience-fragment.png)

    A dialog box to convert the Adaptive Form container to a new Experience Fragment or add to an existing Experience Fragment appears.

1. On the **[!UICONTROL Convert to Experience Fragment]** variation dialog box, set values for the following options:

    * **Action:** Select to create an Experience Fragment or Add to an existing Experience Fragment.
    * **Parent path:** Specify path of the folder to host the Experience Fragment in. The option is available only for creating new Experience Fragment. 
    * **Template:** Specify path of the Experience Fragment template. If you do not have an Experience Fragment template, [create it](/help/implementing/developing/extending/experience-fragments.md). The option is available only for adding Adaptive Form to an existing Experience Fragment. 
    * **Fragment title:** Specify title of the Experience Fragment. The title uniquely identifies an Experience Fragment. 
    * **Fragment tags:** Specify tag of the Experience Fragment. The tag uniquely identifies category of an Experience Fragment. 

## Configure Adaptive Form-Embed(v2) properties

You can customize the advanced settings of the **[!UICONTROL Adaptive Form - Embed(v2)]** component. In the **[!UICONTROL Edit Adaptive Forms - Embed]** dialog, you can specify the following:

* **Asset Path**: Browse and select an Adaptive Form to embed. It is auto-populated if you dropped it from the Assets browser.
* **Post Submission** : Select the action to trigger on form submission. You can choose to show a thank you message or a thank you page.
    * **Show Thank You Message**: Write a message using the rich text editor to show on form submission. This option is available only when you choose to show a thank you message.
    * **Show Thank You Page**: Browse and select the page to display on form submission. This option is available only when you choose to show a thank you page.
    * **Redirect to thank you page**: Enable the option to replace the page containing the embedded Adaptive Form with thank you page. Otherwise, the thank you page replaces the Adaptive Form in the **[!UICONTROL Adaptive Forms - Embed(v2)]** component, without refreshing underlying sites the page. This option is available only when you choose to show a thank you page.
    * **Thankyou Message**: Brief confirmation or acknowledgment that is displayed on the screen after successfully submitting a form.
    * **Thankyou Page**:  Browse and select the page to display after successfully submitting a form.

* **Use Page Language**: Use local of the AEM Sites page instead locale of Adaptive Form. This option is only applicable for Adaptive Form (Foundation).
* **Set Focus on Form**: Select to set the focus on the first field of the Adaptive Form. This option is only applicable for Adaptive Form (Foundation).
* **Theme**: Select a theme that defines styling for components of your Adaptive Form. Styling includes appearance properties such as font style, background color, dimensions, and alignment. This option is only applicable for Adaptive Form (Foundation).

    >[!NOTE]
    >
    > You can use the **Use Page Language**, **Set Focus on Form** and **Theme** options only for Adaptive Form (Foundation). 

* **Form covers entire width of the frame**: 
An inline frame (iframe) is an HTML element that loads an Adaptive Form to an AEM Sites page.

    * If the **[!UICONTROL Form covers entire width of the frame]** checkbox is checked, an Adaptive Form occupies the full width of the container in which it is placed. In this case, an iframe is not used to render the form. The layout and design of an Adaptive Form adapt to span the entire width of the container, making it responsive and capable of adjusting to different screen sizes. This option lets you embed multiple Adaptive Forms within an AEM Sites page.

        >[!NOTE]
        >
        > To embed multiple forms in an AEM Sites page, select **[!UICONTROL Form covers entire width of the frame]** checkbox. 

    * If the **[!UICONTROL Form covers entire width of the frame]** checkbox is not checked, an Adaptive Form does not cover the entire width of the container. Instead, an iframe is used to render the form, which cannot be extended beyond a specific width. This approach is useful when an Adaptive Form has definite boundaries and must coexist with other AEM components next to it within the container. If this option is not checked, it allows only one Adaptive Forms in AEM Sites page to embed without an iframe.

        >[!NOTE]
        >
        > AEM Sites page supports only one Adaptive Form to exist without an iframe. To add more Adaptive Forms using  the **[!UICONTROL Adaptive Forms - Embed]** component, select **[!UICONTROL Form covers entire width of the frame]** option. 

* **Height**: Specify the height of the container. Leave it blank to automatically resize the container.
* **CSS Client library**: Specify path to a CSS client library.

<!--
In AEM Sites page, you can add an Adaptive Form using:

* **Adaptive Forms - Embed component**
   Adaptive Forms - Embed component enables AEM Sites authors to include an existing Adaptive Form within an AEM Sites page, thereby enhancing the reusability of adaptive forms. Existing Adaptive Forms can be used standalone or embedded in the site page. This integration provides a convenient way for customers to reuse Adaptive Forms they have already created.

* **Asset browser**
  All the forms are available under Assets. You can drag-drop the form as an asset on your page.

## Prerequisites {#prerequisites}

 To embed an Adaptive Form in an AEM Sites page that uses an editable template, ensure that the AEM Form component is configured as an allowed component in the associated template. 

In case **Adaptive Forms - Embed component** is not visible in the **Component browser panel** of AEM sites page, perform the following steps as illustrated in the video.

>[!VIDEO](https://video.tv.adobe.com/v/3410544)

In case Sites page is using a static template, you need to configure it in the paragraph system of the site page. 

## Embedding an Adaptive Form {#af-component}

To embed an Adaptive Form using the **[!UICONTROL Adaptive Forms - Embed]** component:

1. Open the AEM sites page, in edit mode, in which you want to embed an Adaptive Form.
1. From the Component browser panel, drag-drop the [!UICONTROL Adaptive Forms - Embed] component on the page. Alternatively, you can search for an Adaptive Form in the Assets browser and drag-drop it onto the Sites page. You can add a new Adaptive Form or embed an existing Adaptive Form. 

   >[!NOTE]
   >
   >Multiple Adaptive Forms - Embed components on a page are not supported.

1. To create and embed a new form, on the component toolbar, select the **Create Form** icon. A window to create the form opens. 

1. Select the embedded Adaptive Forms - Embed component in the sites page, and then select ![settings_icon](assets/settings_icon.png) on the action bar. The **[!UICONTROL Edit Adaptive Forms - Embed]** dialog opens.
1. In the Edit Adaptive Forms - Embed dialog, specify the following.

    **Asset Type:** Select the type of asset to embed. 
    * **Asset Path**: Browse and select the Adaptive Form to embed. It is auto-populated if you dropped it from the Assets browser.
    * **Post Submission** : Select the action to trigger on form submission. You can choose to show a thank you message or a thank you page.
        * Show

        * **Thank You Message**: Write a message using the rich text editor to show on form submission. This option is available only when you choose to show a thank you message.
        * **Thank You Page**: Browse and select the page to display on form submission. This option is available only when you choose to show a thank you page.
           * **Redirect to thank you page**: Enable the option to replace the page containing the embedded Adaptive Form with thank you page. Otherwise, the thank you page replaces the Adaptive Form in the [!UICONTROL Adaptive Forms - Embed] component, without refreshing underlying sites the page. This option is available only when you choose to show a thank you page.
    * **Use Page Language**: Use local of the AEM Sites page instead locale of Adaptive Form.
    * **Set Focus on Form**: Select to set the focus on the first field of the Adaptive Form.
    * **Theme**: Select a theme that defines styling for components of your Adaptive Form. Styling includes appearance properties such as font style, background color, dimensions, and alignment.
    * **Form covers entire width of the frame**: If checked, iframe is not used to render the form. 
    * **Height**: Specify the height of the container. Leave it blank to automatically resize the container.
    * **CSS Client library**: Specify path to a CSS client library.

1. Save the settings. The Adaptive Form  is now embedded in the page.


AEM site also lets you create an Adaptive Form on the fly using the Adaptive Forms - Embed component. Follow the steps to create an Adaptive Form using the **Adaptive Forms - Embed component** on AEM sites page:
1. Open the AEM sites page, in edit mode, in which you want to embed an Adaptive Form.
1. From the Component browser panel, drag-drop the Adaptive Forms - Embed component on the page.
1. Click the **Plus** icon and you are redirected to the form creation wizard.

    ![Adaptive Forms - Embed Component](/help/forms/assets/aemformcontainer.png)

1. You can now embed an Adaptive Form on AEM site pages using the [!UICONTROL AEM Forms Container Component].
-->

## Publish embedded Adaptive Form {#publishing-embedded-adaptive-form}

Let's consider the following scenarios for publishing an embedded Adaptive Form in AEM sites page:

* If you are publishing the AEM sites page for the first time and it includes an embedded Adaptive Form, publish the sites page and the embedded asset.
* If you modified only the embedded Adaptive Form  in a published site page, publish the original asset and the changes reflect in the published site page. The published site page includes a reference to the asset and does not require republishing the page.
* If you modified the sites page and the embedded Adaptive Form , republish the sites page and the embedded asset.

## Modify embedded Adaptive Form  {#modifying-embedded-adaptive-form}

To modify any configuration or property of the embedded Adaptive Form, do one of the following.

* Open the original form in an Adaptive Form  in respective editor and modify them.
* Select the Adaptive Form  from within the site page in edit mode and then select **[!UICONTROL Edit in a new window]**. The original form opens in edit mode that you can modify.

>[!NOTE]
>
>The changes made in the original Adaptive Form  automatically reflect in the embedded form. However, republish the Adaptive Form, or the Site's page to reflect the changes in the published page.

## Best practices {#best-practices}

Do keep the following points in mind when embedding Adaptive Forms in AEM sites pages:

* Header and footer in the original form are not included in the embedded form.
* User drafts and submissions of embedded forms are supported and visible in Drafts and Submitted Forms tabs on the Forms Portal.
* The submit action configured on the original form is retained in the embedded form.
* If you have Adobe Analytics configured for the original form, the analytics data of the embedded form is captured in Adobe Analytics. However, it is not available in the forms analytics report.

## See Also {#see-also}

* [Create Core Component based standalone Adaptive Forms](/help/forms/creating-adaptive-form-core-components.md)
* [Create Core component based Adaptive Form directly in an AEM Sites page](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md)
