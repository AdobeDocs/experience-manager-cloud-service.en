# Snippets {#snippets}

## Headless Trials Promotion {#headless-trials-promotion}

[![Get to know our headless CMS with 30 day trial](./assets/aem-headless-trial-promo.png){align="left"}](https://commerce.adobe.com/business-trial/sign-up?items%5B0%5D%5Bid%5D=649A1AF5CBC5467A25E84F2561274821&cli=headless_exl_banner_campaign&co=US&lang=en)

## Edge Delivery Services Authoring {#edge-delivery-authoring}

[!BADGE For authoring AEM content for Edge Delivery Services, click here.]{type=Positive url="/help/edge/overview.md" tooltip="Authoring AEM content for Edge Delivery Services"}

## See Also {#see-also}

* [Create an AEM Adaptive Form](/help/forms/creating-adaptive-form-core-components.md)
* [Add an AEM Adaptive Form to the AEM Sites page](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md)
* [Apply themes to an AEM Adaptive Form](/help/forms/using-themes-in-core-components.md)
* [Add components to an AEM Adaptive Form](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/introduction#components)
* [Use CAPTCHA in an AEM Adaptive Form](/help/forms/captcha-adaptive-forms-core-components.md)
* [Generate a PDF version (DoR) of an AEM Adaptive Form](/help/forms/generate-document-of-record-core-components.md)
* [Translate an AEM Adaptive Form](/help/forms/using-aem-translation-workflow-to-localize-adaptive-forms-core-components.md)
* [Enable Adobe Analytics for an Adaptive Form to track form usage](/help/forms/enable-adobe-analytics-adaptive-form-using-experience-cloud-setup-automation.md)
* [Connect Adaptive Form to Microsoft SharePoint](/help/forms/configure-submit-actions-core-components.md#submit-to-sharedrive)
* [Connect Adaptive Form to Microsoft Power Automate](/help/forms/configure-submit-actions-core-components.md#microsoft-power-automate)
* [Connect Adaptive Form to Microsoft OneDrive](/help/forms/configure-submit-actions-core-components.md#create-a-onedrive-configuration)
* [Connect Adaptive Form to Microsoft Azure Blob Storage](/help/forms/configure-submit-actions-core-components.md#azure-blob-storage)
* [Connect Adaptive Form to Salesforce](/help/forms/aem-forms-salesforce-integration.md)
* [Use Adobe Sign in an AEM Adaptive Form](/help/forms/working-with-adobe-sign.md)
* [Add a new locale for an Adaptive Form](/help/forms/supporting-new-language-localization-core-components.md)
* [Send Adaptive Form data to a database](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/integrate/use-form-data-model/data-integration)
* [Send Adaptive Form data to a REST endpoint](/help/forms/configure-submit-actions-core-components.md#submit-to-rest-endpoint)
* [Send Adaptive Form data to AEM Workflow](/help/forms/configure-submit-actions-core-components.md#invoke-an-aem-workflow)
* [Use Forms Portal to list AEM Adaptive Forms on an AEM website](/help/forms/configure-forms-portal.md)
* [Add versionings, comments, and annotations to an Adaptive Form](/help/forms/add-comments-annotations-versioning-adaptive-form-core-components.md)
* [Compare Adaptive Forms](/help/forms/compare-forms.md)


## Adaptive Form Submit Actions {#af-submit-action}

* [Send email](/help/forms/configure-submit-action-send-email.md)
* [Submit to SharePoint Document Library](/help/forms/connect-forms-to-sharepoint-document-library.md)
* [Submit to SharePoint List](/help/forms/connect-forms-to-sharepoint-list.md)
* [Submit using Form Data Model](/help/forms/using-form-data-model.md#write-submitted-adaptive-form-data-into-data-sources-write-af)
* [Submit to Azure Blob Storage](/help/forms/configure-submit-action-azure-blob-storage.md)
* [Submit to REST endpoint](/help/forms/configure-submit-action-restpoint.md)
* [Submit to OneDrive](/help/forms/configure-submit-action-onedrive.md)
* [Invoke an AEM Workflow](/help/forms/configure-submit-action-workflow.md)
* [Submit to Power Automate](/help/forms/forms-microsoft-power-automate-integration.md)
* [Submit to Workfront Fusion](/help/forms/submit-adaptive-form-to-workfront-fusion.md)
* [Connect Adaptive Form to Salesforce application](/help/forms/aem-forms-salesforce-integration.md)
* [Connect an Adaptive Form to Microsoft&reg; Dynamics](/help/forms/configure-msdynamics.md)
* [Connect an Adaptive Form to Adobe Marketo Engage](/help/forms/integrate-form-to-marketo-engage.md)
* [Create custom submit action](/help/forms/custom-submit-action-for-adaptive-forms-based-on-core-components.md)

## See also {#see-more-forms-eds}

* [Get started with Edge Delivery Services for AEM Forms](/help/edge/docs/forms/tutorial.md)
* [Create a form using Google Sheets or Microsoft Excel](/help/edge/docs/forms/create-forms.md)
* [Set up your Google Sheets or Microsoft Excel files to start accepting data​](/help/edge/docs/forms/submit-forms.md)
* [Publish your form and start collecting data](/help/edge/docs/forms/publish-forms.md)
* [Customize the look of your forms​](/help/edge/docs/forms/style-theme-forms.md)
* [Add repeatable sections to a form​](/help/edge/docs/forms/repeatable-forms.md)
* [Show a custom thank you message after form submission​](/help/edge/docs/forms/thank-you-page-form.md)
* [Adaptive Form Block components and their properties](/help/edge/docs/forms/form-components.md)
* [Using Form Submission Service](/help/forms/forms-submission-service.md)


## Difference between Rule Editor in Core Components and Rule Editor in Foundation Components {#rule-editor-diff}

The following table demonstrates the difference between the features available in the Rule Editor's Core Components and the Rule Editor's Foundation Components:

<table>
  <tbody>
  <tr>
    <td><strong>Features</strong></td>
    <td><strong>Adaptive Form Foundation Components</strong></td>
    <td><strong>Adaptive Form Core Components</strong></td>   
    </tr>
  </tr>
  <tr>
    <td>Set the drop-down list of options </td>
    <td>The drop-down list of options is set using the Rule Editor's <b>Set Options of</b> property.</td>
    <td>The dropdown options are set using the custom functions. 
   </td>
   </tr>
     </tr>
   <tr>
    <td>Perform mathematical operations on the repeatable panel field </td>
    <td>OOTB Math functions can be applied on repeatable panel fields to perform functions like sum, average using the Rule Editor. Two arguments need to be provided: the first specifies the repeatable panel containing the field, while the second specifies the field within the corresponding repeatable panel. </td>
    <td>Mathematical operations on the repeatable panel field can be performed using the custom functions. You can also apply the mathematical functions directly to the fields of the repeatable panel in Rule Editor.
   </td>
   </tr>
      <tr>
    <td>Validate/Reset field/panel/form rule in 'Then' </td>
    <td>Validate and Reset functions only support form object in Rule Editor. 
   </td>
    <td>Validate and Reset functions support form / panel / field object in Rule Editor. 
   </td>
   </tr>
   <tr>
    <td>ES10 Support </td>
    <td>ES10 is not supported yet. It only supports ES5 JavaScript features. </td>
    <td>Support for modern JavaScript features such as let and arrow functions (ES10 support) within custom functions. 
   </td>
   </tr>
   </tr>
   <tr>
   <td>Service output property</td>
   <td> The Service output property is supported in the <b>Set Value of</b> option of the Rule Editor. </td>
   <td>The <b>Set Value of</b> option does not support the <b>Service output</b> property for invoking APIs in the Rule Editor.
   </td>
   </tr>
   <tr>
   <td>Navigate between the panels</td>
   <td> The <b>Next button</b> and <b>Previous button</b> components are provided to navigate between the panels. A navigation button placed within the container works on its child elements</td>
   <td> The <b>Navigation in Panel</b> rule is available in the rule editor, allowing users to create rules for navigating between the children of panels.
   </td>
   </tr>
   </tr>
   </tr>
  </tbody>
  <table>
  </tbody>

## Rule Editor See Also {#see-also-rule-editor}

* [Introduction to Rule Editor for Adaptive Forms based on Core Components](/help/forms/rule-editor-core-components.md)
* [Operator types and events in rule editor of an Adaptive Form based on Core Components](/help/forms/rule-editor-core-components-events-operators.md)
* [Rule Editor User Interface for Adaptive Forms based on Core Components](/help/forms/rule-editor-core-components-user-interface.md)
* [Different use cases of Rule Editor for an Adaptive Form Based on Core Components](/help/forms/rule-editor-core-components-usecases.md)
* [Difference in various editions of Rule editor](/help/forms/rule-editor-core-components-difference-tables.md)
*  [Using asynchronous functions in an Adaptive Form](/help/forms/using-async-funct-in-rule-editor.md)
* [Invoke Service enhancements in the Visual Rule Editor for forms based on Core Components](/help/forms/invoke-service-enhancements-rule-editor.md)
* [Introduction to Custom Functions for Adaptive Forms based on Core Components](/help/forms/create-and-use-custom-functions.md)
* [Create a Custom Function for an Adaptive Form based on Core Components](/help/forms/custom-function-core-component-create-function.md)
* [Scope object in custom functions](/help/forms/custom-function-core-component-scope-function.md)
* [Examples of developing and using a custom function](/help/forms/custom-function-core-components-use-cases.md)


## Forms Portal{#forms-portal-see-also}

* [Introduction to Forms Portal components](/help/forms/configure-forms-portal.md)
* [List your forms on sites page](/help/forms/list-forms-on-sites-page.md)
* [Save your forms as drafts](/help/forms/save-core-component-based-form-as-draft.md)
* [Add form links to a Sites page](/help/forms/add-form-link-to-aem-sites-page.md)

## Marketo Engage{#marketo-engage-see-also}

* [Integrate Marketo Engage with AEM Forms](/help/forms/integrate-form-to-marketo-engage.md)
* [Configure new form to integrate with Marketo Engage](/help/forms/integrate-adaptive-form-with-marketo-engage.md) 
* [Configure Marketo Engage data source for existing Adaptive Forms](/help/forms/use-marketo-engage-data-source-in-form.md)
* [Configure the submit action to Marketo Engage for existing forms](/help/forms/submit-adaptive-form-to-marketo-engage.md)

## Cloud Manager IP Allow List and front-end pipelines {#allowlist-frontend-pipeline}

>[!IMPORTANT]
>
>The front-end pipeline requires that the following IP Allow List be added to Cloud Manager beforehand.
>If needed, [add the IP Allow List](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md) by copying the block of addresses below. Each address is separated by a comma. Paste the block into the **IP address / CIDR** field of the **Add IP Allow List** dialog box. Place the cursor just after the first comma in the address list and press **Enter**. Save the list. 
>To avoid disruption of running the front-end pipeline, ensure that this IP Allow List is added to Cloud Manager *before* you enable the pipeline.
>
>**Cloud Manager IP Allow List**
>52.254.106.192/28,20.186.185.181,52.254.106.240/28,52.254.107.128/28,52.254.105.192/28,52.254.106.176/28,20.186.185.227,52.254.106.144/28,52.254.107.64/28,20.186.185.239,20.22.83.112,52.254.107.80/28,52.254.107.144/28,52.254.106.224/28,20.14.241.153,52.254.107.0/28,52.254.107.32/28,52.254.106.208/28,40.70.154.136/29,52.254.106.160/28,52.254.107.16/28,52.254.106.0/28,4.152.211.251
>   

## Add a Cloud Manager IP Allow List and front-end pipelines {#add-cm-allowlist-frontend-pipeline}

>[!IMPORTANT]
>
>If you use&mdash;or intend to use&mdash;the front-end pipeline to develop sites, the Cloud Manager IP Allow List must be added beforehand. 
>See [Use of the Cloud Manager IP Allow List with the front-end pipeline](/help/implementing/cloud-manager/ip-allow-lists/introduction.md#allowlists-frontend-pipeline). 

## IP Allow Lists and the Universal Editor {#ip-allow-lists-ue}

>[!IMPORTANT]
>
>[The Universal Editor](/help/implementing/universal-editor/introduction.md) is not compatible with IP allow lists.
>
>If you want to use the Universal Editor, IP allow lists must not be enabled.

## Universal Editor and IP Allow Lists {#ue-ip-allow-lists}

>[!IMPORTANT]
>
>The Universal Editor is not compatible with [IP allow lists](/help/implementing/cloud-manager/ip-allow-lists/introduction.md).
>
>If you want to use the Universal Editor, you must either:
>
>* Not enable IP Allow Lists.
>* [Run your own instance of the Universal Editor Service](/help/implementing/universal-editor/local-dev.md).

## Work with Dynamic Media {#work-with-dynamic-media}

>[!TIP]
>
>Are you new to Dynamic Media? For a quick, high-level overview of Dynamic Media, see [Work with Dynamic Media](/help/assets/dynamic-media/dynamic-media.md).

## See also for Dynamic Media {#see-also-dm}

>[!NOTE]
>
>* Are you new to Dynamic Media? For a quick, high-level overview of Dynamic Media, see [Work with Dynamic Media](/help/assets/dynamic-media/dynamic-media.md).
>
>* Follow [Dynamic Media Best Practices](/help/assets/dynamic-media/dm-best-practices.md) to get the most value.
>
>* Try out Dynamic Media image capabilities with the [Snapshot tool](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-snapshot).
>
>* Ensure smooth video playback with [adaptive video](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/video/dynamic-media-dash).
>
>* Automate cropping of [images with Smart Crop](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/images/smart-crop-feature-video-use).
>
>* Automate cropping of [videos with Smart Crop](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/video/dynamic-media-smart-crop-video).
>
>* Deliver an [interactive 3D-powered experience](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/3d/dynamic-media-3d-feature-video).
>* Other [Dynamic Media resource bank](https://experienceleague.adobe.com/en/docs/experience-manager-learn/assets/dynamic-media/dynamic-media-overview-feature-video-use).

## Log a support ticket {#support-ticket}

If a product issue needs additional investigation and troubleshooting and must meet response SLTs, you can submit a support ticket.

To log a support ticket, you must first register your Edge Delivery site in Cloud Manager. Registering your website with Cloud Manager is recommended to all AEM as a Cloud Service users and [brings a number of benefits](/help/implementing/cloud-manager/edge-delivery/introduction-to-edge-delivery-services.md). See [the Cloud Manager documentation](/help/implementing/cloud-manager/edge-delivery/add-edge-delivery-site.md) for details if you have not already registered your site. 

**To log a support ticket:**

1. [Follow the standard support process](https://experienceleague.adobe.com/?support-tab=home#support) and create a ticket.
1. Add **Edge Delivery** in the title of the ticket.
1. In the description, provide the following details in addition to the problem description:

    * URL of the live website. For example: `www.mydomain.com`.
    * URL of the origin website (`.hlx` URL).

## Universal Editor is Preferred over SPA Editor {#ue-over-spa}

>[!IMPORTANT]
>
>The SPA Editor [has been deprecated](/help/release-notes/release-notes-cloud/release-notes-current.md#sites-deprecated) for new projects. It remains supported by Adobe for existing projects, but should not be used for new projects. The preferred editors for managing headless content in AEM are now:
>
>* [The Universal Editor](/help/edge/wysiwyg-authoring/authoring.md) for visually editing headless content.
>* [The Content Fragment Editor](/help/assets/content-fragments/content-fragments-managing.md) for form-based editing of headless content.
