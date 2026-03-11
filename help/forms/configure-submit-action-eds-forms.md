---
title: How to Configure a Submit Action for an Adaptive Form?
description: An Adaptive Form provides multiple Submit Actions. A Submit Action defines how an Adaptive Form is processed after submission. You can use built-in Submit Actions or create your own.
keywords: how to select submit action for an adaptive form, connect an adaptive form to sharepoint list, connect an adaptive form to sharepoint document library, connect an adaptive form to form data model (FDM)
feature: Adaptive Forms, Edge Delivery Services
role: User, Developer
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 3f8950c3-9022-4e9f-b3ed-723245201e45
---
# Submit Actions for Edge Delivery Services Forms

| Version | Article Link |
|---------|-----------------------------|
| AEM 6.5 | [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/configuring-submit-actions.html) |
| AEM as a Cloud Service (Foundation Components) | [Click here](/help/forms/configuring-submit-actions.md) |
| AEM as a Cloud Service (Core Components) | [Click here](/help/forms/configure-submit-actions-core-components.md) |
| AEM as a Cloud Service (Edge Delivery Services) | This article |

Submit Actions define what happens when a user submits a form, such as storing data, triggering workflows, or integrating with third-party systems. The type of submit actions you can configure depends on the authoring method used to create Edge Delivery Services Forms.

You can create Edge Delivery Services Forms using either the [Universal Editor](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) or by using [Document Based Forms](/help/edge/docs/forms/overview.md) authoring, and configure the forms with different submit actions accordingly.

## Submit Actions for Forms created in Universal Editor 

The following submit actions are supported by [Adaptive Forms authored in the Universal Editor](/help/edge/docs/forms/universal-editor/create-forms.md):

* [Send Email](/help/forms/configure-submit-action-send-email.md)
* [Invoke a Power Automate Flow](/help/forms/forms-microsoft-power-automate-integration.md)
* [Submit to SharePoint](/help/forms/configure-submit-action-sharepoint.md)
* [Invoke Workfront Fusion](/help/forms/submit-adaptive-form-to-workfront-fusion.md)
* [Submit using Form Data Model (FDM)](/help/forms/integrate-adaptive-form-with-fdm.md)
* [Submit to Azure Blob Storage](/help/forms/configure-submit-action-azure-blob-storage.md)
* [Submit to REST Endpoint](/help/forms/configure-submit-action-restpoint.md)
* [Submit to OneDrive](/help/forms/configure-submit-action-onedrive.md)
* [Invoke an AEM Workflow](/help/forms/configure-submit-action-workflow.md)
* [Submit to Marketo Engage](/help/forms/submit-adaptive-form-to-marketo-engage.md)
* [Submit to Adobe Experience Platform (AEP)](/help/forms/aem-forms-aep-connector.md)
* [Submit to Spreadsheet](/help/forms/forms-submission-service.md)

<!--You can also submit an Adaptive Form in the Universal Editor to other storage or CRM integrations:

* [Connect Adaptive Form to Salesforce](/help/forms/aem-forms-salesforce-integration.md)
* [Connect an Adaptive Form to Microsoft&reg; Dynamics OData](/help/forms/ms-dynamics-odata-configuration.md)-->

You can configure the submit action for forms created in the Universal Editor using the **Submission** tab of the **Edit Form Properties** extension.

<!--**How to Configure Submit Action for Forms authored in Universal Editor?**
You can configure the submit action for forms created in the Universal Editor using the **Submission** tab of the **Edit Form Properties** extension.

![Form properties icon](/help/forms/assets/ue-form-properties-icon.png)

![Universal Editor Form Properties](/help/forms/assets/ue-form-properties.png)-->

>[!NOTE]
>
> * If you do not see the **Edit Form Properties** icon in your Universal Editor interface, enable the **Edit Form Properties** extension in the Extension Manager. 
> * Refer to the [Extension Manager Feature Highlights](https://developer.adobe.com/uix/docs/extension-manager/feature-highlights/#enablingdisabling-extensions) article to learn how to enable or disable extensions in the Universal Editor.

## Submit Actions for Document Based Forms 

Document Based Forms support submission only to spreadsheets. To learn how to set up your spreadsheet to receive submitted data, see the instructions in the [Set up your Google Sheets or Microsoft Excel files to start accepting data](/help/edge/docs/forms/submit-forms.md) article.

## See Also {#see-also}

{{af-submit-action}}
