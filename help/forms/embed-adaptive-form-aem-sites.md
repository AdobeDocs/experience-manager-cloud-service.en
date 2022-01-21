---
title: How to embed an Adaptive Form in an AEM sites page? 
description: You can embed Adaptive Forms in AEM sites pages. Users can fill and submit forms without leaving the site pages.


---

# Embed an Adaptive Form  in AEM sites page {#embed-an-adaptive-form-or-interactive-communication-in-aem-sites-page}

[!DNL AEM Forms] allows form developers to seamlessly embed Adaptive Forms in an AEM Sites page or a web page hosted outside AEM. The embedded Adaptive Form is fully functional and users can fill and submit the form without leaving the page. It helps user remain in context of other elements on the web page and simultaneously interact with the form .

<!-- For information about embedding an Adaptive Form in an external web page, see [Embed Adaptive Form in external web page](/help/forms/using/embed-adaptive-form-external-web-page.md). -->

In AEM Sites page, you can add an Adaptive Form  using:

* **[[!DNL AEM Forms] Container component](#af-component)**
  [!DNL AEM Forms] provides a component that you can add to your site pages. The [!DNL AEM Forms] Container component lets you embed an Adaptive Form.

* **[Asset browser](/help/forms/using/embed-adaptive-form-aem-sites.md#asset-browser)**
  All the forms you create are available under Assets. You can drag-drop the form as an asset on your page.

## Prerequisites {#prerequisites}

To embed an Adaptive Form  in an AEM sites page that uses an editable template, ensure that the AEM Form component is configured as an allowed component in the associated template. For more information, see **Policy & Properties (Layout Container)** section in [Creating Page Templates](/help/sites-authoring/templates.md).

In case of a Sites page using a static template, you need to configure it in the paragraph system of the site page. See [Configuring Components in Design Mode](/help/sites-authoring/default-components-designmode.md) for more information.

## Embedding an Adaptive Form  {#af-component}

To embed an Adaptive Form  using [!DNL AEM Forms] Container component:

1. Open the AEM sites page, in edit mode, in which you want to embed an Adaptive Form .
1. From the Component browser panel, drag-drop the [!DNL AEM Forms] Container component on the page.

   Alternatively, you can search for an Adaptive Form  in the Assets browser and drag-drop it onto the Sites page. It embeds the form in an [!DNL AEM Forms] Container.

   >[!NOTE]
   >
   >Multiple [!DNL AEM Forms] Container components on a page are not supported.

1. Tap the embedded [!DNL AEM Forms] Container component in the sites page, and then tap ![settings_icon](assets/settings_icon.png) on the action bar. The **[!UICONTROL Edit AEM Forms Container]** dialog opens.
1. In the Edit [!DNL AEM Forms] Container dialog, specify the following.

    * **Asset Type:** Select the type of asset to embed. The options are Adaptive Form
    * **Asset Path**: Browse and select the Adaptive Form  to embed. It is auto-populated if you dropped it from the Assets browser.
    * (Adaptive Form only) **Post Submission**: Select the action to trigger on form submission. You can choose to show a thank you message or a thank you page.

        * **Thank You Message**: Write a message using the rich text editor to show on form submission. This option is available only when you choose to show a thank you message.
        * **Thank You Page**: Browse and select the page to display on form submission. This option is available only when you choose to show a thank you page.
        * **Refresh Page on Submission**: Enable to refresh the page containing the embedded Adaptive Form to show the thank you page. Otherwise, the thank you page replaces the Adaptive Form in the [!DNL AEM Forms] container, without refreshing the page. This option is available only when you choose to show a thank you page.

    * **Theme**: Select a theme that defines styling for components of your Adaptive Form . Styling includes appearance properties such as font style, background color, dimensions, and alignment.
    * **Height**: Specify the height of the container. Leave it blank to automatically resize the container.
    * **CSS Client library**: Specify path to a CSS client library.

1. Save the settings. The Adaptive Form  is now embedded in the page.

## Publishing embedded Adaptive Form {#publishing-embedded-adaptive-form}

Let's consider the following scenarios for publishing an embedded asset (Adaptive Form ) in AEM sites page:

* If you are publishing the AEM sites page for the first time and it includes an embedded Adaptive Form , publish the sites page and the embedded asset.
* If you modified only the embedded Adaptive Form  in a published site page, publish the original asset and the changes reflect in the published site page. The published site page includes a reference to the asset and does not require republishing the page.
* If you modified the sites page and the embedded Adaptive Form , republish the sites page and the embedded asset.

## Modifying embedded Adaptive Form {#modifying-embedded-adaptive-form-and-interactive-communication}

AEM sites page maintains a reference to the Adaptive Form in the [!DNL AEM Forms] Container. Therefore, all configurations and properties, such as the theme, styles, and submit action, configured in the original Adaptive Form are retained in the embedded Adaptive Form.

To modify any configuration or property of the embedded Adaptive Form, do one of the following.

* Open the original form in Adaptive Forms  in respective editors and modify them.
* Tap the Adaptive Form  from within the site page in edit mode and then tap **[!UICONTROL Edit in a new window]**. The original form opens in edit mode that you can modify.

>[!NOTE]
>
>The changes made in the original Adaptive Form  automatically reflect in the embedded form. However, republish the Adaptive Form, or the site page to reflect the changes in the published page.

## Considerations and best practices {#considerations-and-best-practices}

Do keep the following points in mind when embedding Adaptive Forms in AEM sites pages:

* Header and footer in the original form are not included in the embedded form.
* User drafts and submissions of embedded forms are supported and visible in Drafts and Submitted Forms tabs on the forms portal.
* The submit action configured on the original form is retained in the embedded form.
* Experience targeting and A/B tests configured on the original form do not work in the embedded form. However, you can use experience targeting on the sites page to present different forms based on user profiles.
* If you have Adobe Analytics configured for the original form, the analytics data of the embedded form is captured in Adobe Analytics. However, it is not available in the forms analytics report.

