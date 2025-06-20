---
title: How to Configure a Submit Action for an Adaptive Form?
description: An Adaptive Form provides multiple Submit Actions. A Submit Action defines how an Adaptive Form is processed after submission. You can use built-in Submit Actions or create your own.
keywords: how to select submit action for an adaptive form, connect an adaptive form to sharepoint list, connect an adaptive form to sharepoint document library, connect an adaptive form to form data model (FDM) 
feature: Adaptive Forms, Edge Delivery Services
role: User, Developer
---

# Submit Actions for Edge Delivery Services Forms

| Version | Article Link |
|---------|-----------------------------|
| AEM 6.5 | [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/configuring-submit-actions.html) |
| AEM as a Cloud Service (Foundation Components) | [Click here](/help/forms/configuring-submit-actions.md) |
| AEM as a Cloud Service (Core Components) | [Click here](/help/forms/configure-submit-actions-core-components.md) |
| AEM as a Cloud Service (Edge Delivery Services) | This article |

You can create Edge Delivery Services forms using the Universal Editor or create document based forms.

The [Universal Editor](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) is a WYSIWYG authoring tool designed for creating modern, responsive forms using AEM as a Cloud Service.

[Document Based Forms](/help/edge/docs/forms/overview.md) submit data directly to a Microsoft Excel or Google Sheets file to simplify data processing or trigger an existing business workflow.

## Configure Submit Action for Edge Delivery Services Forms

You can configure submit actions for:

* Forms created in Universal Editor
* Document Based forms

## Configure Submit Action for Forms Created in Universal Editor

Submit Actions define what happens when a user submits a form. For example, storing data, triggering workflows, or integrating with third party systems. Adaptive Forms created using the Universal Editor support various [out of the box submit actions](#submit-actions-supported-by-adaptive-forms-created-in-universal-editor).

### Considerations

You can configure the submit action for forms created in the Universal Editor using the **Submission** tab of the **Edit Form Properties** extension.

![Form properties icon](/help/forms/assets/ue-form-properties-icon.png)

If you do not see the **Edit Form Properties** icon in your Universal Editor interface, enable the **Edit Form Properties** extension in the Extension Manager.

Refer to the [Extension Manager Feature Highlights](https://developer.adobe.com/uix/docs/extension-manager/feature-highlights/#enablingdisabling-extensions) article to learn how to enable or disable extensions in the Universal Editor.

Once enabled, open a form in the Universal Editor and navigate to **Form Settings** to configure the submit action.

The submit actions in the Universal Editor are configured through the **Submission** tab of the **Edit Form Properties** extension.

![Universal Editor Form Properties](/help/forms/assets/ue-form-properties.png)


You can also configure different actions for an Adaptive Form submissions.

* **Prefill Service** - Adaptive Forms support prefill service, enabling forms to populate specific fields with known information as soon as the user opens the form. This enhances usability by reducing repetitive data entry common fields like name, email address, or account number can be pre-populated based on available data. 
* **Thankyou** - This option allows user to configure a page for each form, to which the form users are redirected after submitting an Adaptive Form. You can also add a message that is displayed when the Adaptive Form is successfully submitted. 

### Submit Actions Supported by Adaptive Forms Created in Universal Editor 

The following submit actions are supported by Adaptive Forms in the Universal Editor:

* [Send Email](/help/forms/configure-submit-action-send-email.md)
* [Invoke a Power Automate Flow](/help/forms/forms-microsoft-power-automate-integration.md)
* [Submit to SharePoint](/help/forms/configure-submit-action-sharepoint.md)
* [Invoke Workfront Fusion](/help/forms/submit-adaptive-form-to-workfront-fusion.md)
* [Submit using Form Data Model (FDM)](/help/forms/using-form-data-model.md)
* [Submit to Azure Blob Storage](/help/forms/configure-submit-action-azure-blob-storage.md)
* [Submit to REST Endpoint](/help/forms/configure-submit-action-restpoint.md)
* [Submit to OneDrive](/help/forms/configure-submit-action-onedrive.md)
* [Invoke an AEM Workflow](/help/forms/configure-submit-action-workflow.md)
* [Submit to Marketo Engage](/help/forms/submit-adaptive-form-to-marketo-engage.md)
* [Submit to Adobe Experience Platform (AEP)](/help/forms/aem-forms-aep-connector.md)
* [Submit to Spreadsheet](/help/forms/forms-submission-service.md)

You can also submit an Adaptive Form in the Universal Editor to other storage or CRM integrations:

* [Connect Adaptive Form to Salesforce](/help/forms/aem-forms-salesforce-integration.md)
* [Connect an Adaptive Form to Microsoft&reg; Dynamics OData](/help/forms/ms-dynamics-odata-configuration.md)

<!-- Additionally, you can [customize the default Submit Actions](/help/forms/custom-submit-action-form.md) to align with specific organizational requirements. -->

## Supported Submit Actions for Document Based Forms

Document Based Forms support submission only to spreadsheets.  
To learn how to set up your spreadsheet to receive submitted data, see the instructions in the [Set up your Google Sheets or Microsoft Excel files to start accepting data](/help/edge/docs/forms/submit-forms.md) article.

## See Also {#see-also}

{{af-submit-action}}
