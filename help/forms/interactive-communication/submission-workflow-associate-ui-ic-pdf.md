---
title: Submission workflow for Associate UI — IC Generate PDF Output
description: Understand how submission and workflow work for Associate UI, and follow an example workflow that generates PDF from Interactive Communication (IC) JSON.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
exl-id: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
---
# Submission workflow for Associate UI

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

This article explains how submission and workflow work when you enable a workflow for the Associate UI. It then walks through how to configure a submission workflow. The walkthrough uses generating a PDF from the Interactive Communication (IC) payload as an example; you can adapt the steps for other workflow types.

## Submission and workflow behavior {#submission-and-workflow-behavior}

When you enable **Configure Workflow for Update** for an Associate UI, submissions from the Associate UI can trigger an AEM workflow. The following explains where workflows run, who uses which environment, and how to plan for data and access.

### Where workflows run

AEM workflows always run on the **Author** instance. It does not matter whether the person submitting is an author or an associate—the workflow runs on Author. Plan your user groups and where you store workflow data with this in mind.

### Where associates use the Associate UI

Customer-facing associates use the Associate UI on the **Publish** instance only. You publish the Interactive Communication and expose the Associate UI through your Publish environment (for example, via your application or dispatcher). Associates do not use the Author instance. For step-by-step integration and how to invoke the Associate UI on the Publish instance, see [Integrate Associate UI in Your Application](/help/forms/interactive-communication/invoke-associate-ui.md).

### When an author submits from the Author instance

Authors can open the Associate UI on the Author instance—for example, to test the Interactive Communication or to submit on behalf of a customer. When they submit, the request is handled on Author and the workflow runs there. For this to work, the author must be in both **forms-associates** (to access the Associate UI) and **workflow-users** (to run the workflow).

### When an associate submits from the Publish instance

Associates open the Associate UI on the Publish instance, using the integration you set up. When they submit, the submission is sent to the Author instance and the workflow runs on Author. Associates sign in on Publish (for example, via [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id)) and do not need access to Author. To set up how associates open the Associate UI on Publish, see [Integrate Associate UI in Your Application](/help/forms/interactive-communication/invoke-associate-ui.md).

## Configure a submission workflow

The following steps show how to create a workflow that runs when users submit from the Associate UI. Here we use **rendering the IC to PDF** as an example, with the out-of-box **IC Render PDF Output** step. When a user submits from the Associate UI, the payload is sent to the workflow; this step uses the **communicationDom** (IC-JSON) from the payload to produce the PDF.

### Payload structure

The workflow receives a JSON payload. The **communicationDom** field holds the IC-JSON used for PDF generation. The **IC Render PDF Output** step uses it as the template input.

| Field | Description |
|-------|-------------|
| communicationDom | IC-JSON for PDF generation |
| auditMetadata | Auditing info |
| submitData | Submitted form data (JSON) |
| prefillData | Prefill data (JSON) |
| referer, cookies, queryString, clientIP, userAgent, formSubmitter | Request metadata |

### Create the workflow model

1. **Basic:** Create a workflow model (for example, add a workflow as **pdfrenderworkflow**). 

   ![Workflow model Basic tab](/help/forms/assets/associate-ui-add-workflow.png)

1. **Variables:** Add variables that match the payload and step: **communicationDom** (JSON), **auditMetadata** (JSON), **outputDocument** (Document).

   ![Workflow variables](/help/forms/assets/associate-ui-add-variables.png)

1. **Step:** Add the **IC Render PDF Output** step.
   ![Add Workflow step](/help/forms/assets/associate-ui-add-step.png)

1. In its **Input** tab, set **Select template (JsonObject)** to **Variable** → **communicationDom**. Save the step and the model.

   ![IC Render PDF Output — Input tab](/help/forms/assets/associate-ui-input-variable.png)

1. In its **Output** tab, set **Select template (JsonObject)** to **Variable** → **communicationDom**. Save the step and the model.
  
   ![Workflow variables and canvas](/help/forms/assets/assocaite-ui-output-variable.png)

### Wire the workflow to Associate UI

In [Enable and configure Associate UI](/help/forms/interactive-communication/enable-configure-associate-ui.md), enable Associate View and in **Workflow** set **Configure Workflow for Update** to On and select this workflow model. Publish the IC and [integrate the Associate UI](/help/forms/interactive-communication/invoke-associate-ui.md) so submissions trigger this workflow.

   ![Interactive Communication Settings - Workflow configuration for Associate UI](/help/forms/assets/associate-ui-configure-workflow.png)

When **Externalize workflow data storage** is enabled, configure the externaliser so workflow data is stored in your external storage (for example, Azure). See [Externalize workflow data](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/forms/create-aem-workflow/externalize-workflow.html).

## See also

- [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md)
- [Enable and configure Associate UI for Interactive Communications](/help/forms/interactive-communication/enable-configure-associate-ui.md)
- [Integrate Associate UI in Your Application](/help/forms/interactive-communication/invoke-associate-ui.md)
- [Externalize workflow data](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/forms/create-aem-workflow/externalize-workflow.html)
