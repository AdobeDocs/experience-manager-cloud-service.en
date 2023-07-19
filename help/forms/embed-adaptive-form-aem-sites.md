---
title: Embed an Adaptive Form in AEM Sites page
seo-title: Hwo to add an Adaptive Form to an AEM Sites page?
description: You can use Adaptive Forms -Embed component to add or embed Adaptive Forms to an AEM Sites page to fill and submit a form without leaving the AEM Sites pages.
feature: Adaptive Forms
exl-id: 359b05e8-d8c1-4a77-9e70-6f6b6e668560
---
# Embed an Adaptive Form to an AEM sites page {#embed-an-adaptive-form-to-aem-sites-page}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/embed-adaptive-form-aem-sites.html)                  |
| AEM as a Cloud Service     | This article        |


## Overview {#overview}

AEM Forms allow form developers to seamlessly embed Adaptive Forms in an AEM Sites page or a web page hosted outside AEM. The embedded Adaptive Form is fully functional and users can fill and submit the form without leaving the page. It helps user remain in context of other elements on the web page and simultaneously interact with the form.



<!-- For information about embedding an Adaptive Form in an external web page, see [Embed Adaptive Form in external web page](/help/forms/using/embed-adaptive-form-external-web-page.md). --> 

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

1. To create and embed a new form, on the component toolbar, tap the **Create Form** icon. A window to create the form opens. 

1. Tap the embedded Adaptive Forms - Embed component in the sites page, and then tap ![settings_icon](assets/settings_icon.png) on the action bar. The **[!UICONTROL Edit Adaptive Forms - Embed]** dialog opens.
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

AEM site also allows you to create an Adaptive Form on the fly using the Adaptive Forms - Embed component. Follow the steps to create an Adaptive Form using the **Adaptive Forms - Embed component** on AEM sites page:
1. Open the AEM sites page, in edit mode, in which you want to embed an Adaptive Form.
1. From the Component browser panel, drag-drop the Adaptive Forms - Embed component on the page.
1. Click the **Plus** icon and you are redirected to the form creation wizard.

    ![Adaptive Forms - Embed Component](/help/forms/assets/aemformcontainer.png)

1. You can now embed an Adaptive Form on AEM site pages using the [!UICONTROL AEM Forms Container Component].

## Publishing embedded Adaptive Form {#publishing-embedded-adaptive-form}

Let's consider the following scenarios for publishing an embedded Adaptive Form in AEM sites page:

* If you are publishing the AEM sites page for the first time and it includes an embedded Adaptive Form, publish the sites page and the embedded asset.
* If you modified only the embedded Adaptive Form  in a published site page, publish the original asset and the changes reflect in the published site page. The published site page includes a reference to the asset and does not require republishing the page.
* If you modified the sites page and the embedded Adaptive Form , republish the sites page and the embedded asset.

## Modifying embedded Adaptive Form  {#modifying-embedded-adaptive-form}

AEM sites page maintains a reference to the Adaptive Form  in the Adaptive Forms - Embed. Therefore, all configurations and properties, such as the theme, styles, and submit action, configured in the original Adaptive Form are retained in the embedded Adaptive Form .

To modify any configuration or property of the embedded Adaptive Form, do one of the following.

* Open the original form in adaptive forms  in respective editors and modify them.
* Tap the Adaptive Form  from within the site page in edit mode and then tap **[!UICONTROL Edit in a new window]**. The original form opens in edit mode that you can modify.

>[!NOTE]
>
>The changes made in the original Adaptive Form  automatically reflect in the embedded form. However, republish the Adaptive Form, or the site page to reflect the changes in the published page.

## Considerations and best practices {#considerations-and-best-practices}

Do keep the following points in mind when embedding adaptive forms in AEM sites pages:

* Header and footer in the original form are not included in the embedded form.
* User drafts and submissions of embedded forms are supported and visible in Drafts and Submitted Forms tabs on the Forms Portal.
* The submit action configured on the original form is retained in the embedded form.
* If you have Adobe Analytics configured for the original form, the analytics data of the embedded form is captured in Adobe Analytics. However, it is not available in the forms analytics report.
