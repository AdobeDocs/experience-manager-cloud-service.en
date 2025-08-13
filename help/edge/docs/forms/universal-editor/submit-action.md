---
title: How to Configure a Submit Action for an Adaptive Form?
description: An Adaptive Form provides multiple Submit Actions. A Submit Action defines how an Adaptive Form is processed after submission. You can use built-in Submit Actions or create your own.
keywords: how to select submit action for an adaptive form, connect an adaptive form to sharepoint list, connect an adaptive form to sharepoint document library, connect an adaptive form to form data model (FDM)
feature: Adaptive Forms, Edge Delivery Services
role: User, Developer
exl-id: beee9be7-8215-496b-9fb9-61fba000a055
---
# Adaptive Form Submit Action

| Version | Article Link |
|---------|-----------------------------|
| AEM 6.5 | [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/configuring-submit-actions.html) |
| AEM as a Cloud Service (Foundation Components) | [Click here](/help/forms/configuring-submit-actions.md) |
| AEM as a Cloud Service (Core Components) | [Click here](/help/forms/configure-submit-actions-core-components.md) |
| AEM as a Cloud Service (Edge Delivery Services) | This article |


Form submission is the critical final step in the user journey—it's where collected data is processed and actions are taken. This document provides a comprehensive guide to configuring and managing submit actions for Adaptive Forms in Universal Editor.

## What You'll Learn

By the end of this document, you'll understand how to:

- Configure different types of submit actions for your forms
- Set up REST endpoint submissions for integration with external systems
- Configure email submissions for form responses
- Implement custom submit actions for specific business needs
- Handle form validation and error scenarios during submission

## Target Audience

This guide is designed for:

- **Form developers** implementing submission logic
- **System integrators** connecting forms to backend systems
- **Business analysts** defining form workflows
- **Technical architects** designing form submission processes

## Submit Actions for Forms created in Universal Editor 

The following submit actions are supported by [Adaptive Forms authored in the Universal Editor](/help/edge/docs/forms/universal-editor/create-forms.md):

- [Send Email](/help/forms/configure-submit-action-send-email.md)
- [Invoke a Power Automate Flow](/help/forms/forms-microsoft-power-automate-integration.md)
- [Submit to SharePoint](/help/forms/configure-submit-action-sharepoint.md)
- [Invoke Workfront Fusion](/help/forms/submit-adaptive-form-to-workfront-fusion.md)
- [Submit using Form Data Model (FDM)](/help/forms/integrate-adaptive-form-with-fdm.md)
- [Submit to Azure Blob Storage](/help/forms/configure-submit-action-azure-blob-storage.md)
- [Submit to REST Endpoint](/help/forms/configure-submit-action-restpoint.md)
- [Submit to OneDrive](/help/forms/configure-submit-action-onedrive.md)
- [Invoke an AEM Workflow](/help/forms/configure-submit-action-workflow.md)
- [Submit to Marketo Engage](/help/forms/submit-adaptive-form-to-marketo-engage.md)
- [Submit to Adobe Experience Platform (AEP)](/help/forms/aem-forms-aep-connector.md)
- [Submit to Spreadsheet](/help/forms/forms-submission-service.md)

<!--You can also submit an Adaptive Form in the Universal Editor to other storage or CRM integrations:

* [Connect Adaptive Form to Salesforce](/help/forms/aem-forms-salesforce-integration.md)
* [Connect an Adaptive Form to Microsoft&reg; Dynamics OData](/help/forms/ms-dynamics-odata-configuration.md)-->

You can configure the submit action for forms created in the Universal Editor using the **Submission** tab of the **Edit Form Properties** extension.

**How to Configure Submit Action for Forms authored in Universal Editor?**
You can configure the submit action for forms created in the Universal Editor using the **Submission** tab of the **Edit Form Properties** extension.

![Form properties icon](/help/forms/assets/ue-form-properties-icon.png)

![Universal Editor Form Properties](/help/forms/assets/ue-form-properties.png)

>[!NOTE]
>
> - If you do not see the **Edit Form Properties** icon in your Universal Editor interface, enable the **Edit Form Properties** extension in the Extension Manager. 
> - Refer to the [Extension Manager Feature Highlights](https://developer.adobe.com/uix/docs/extension-manager/feature-highlights/#enablingdisabling-extensions) article to learn how to enable or disable extensions in the Universal Editor.
