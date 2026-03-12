---
title: Enable and configure Associate UI for Interactive Communications
description: Learn how to enable Associate View and configure workflow for updates in Interactive Communication Settings so associates can use the Associate UI.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
exl-id: 7c3e8a2b-5f21-4a1e-9e2d-8a4b6c7d8e9f
---
# Enable and configure Associate UI for Interactive Communications

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

This article describes how to enable the Associate UI for an Interactive Communication (IC) and optionally configure an AEM workflow for submissions. Authors perform these steps in **Interactive Communication Settings**.

For an overview of the Associate UI and user roles, see [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md).

## Prerequisites

Before enabling and configuring the Associate UI, ensure you have:

- **Author access** to the Interactive Communication editor.
- An **Interactive Communication** created with the required layout and data bindings.
- **Associate users** added to the **forms-associates** group (required for associates to access the Associate UI).
- **Authors** added to the **forms-associates** group (required for authors to access the Associate UI).

When you are ready to integrate the Associate UI with your application and invoke it on the Publish instance, you will also need a browser with popup support enabled and the IC published. See [Integrate Associate UI in Your Application](/help/forms/interactive-communication/invoke-associate-ui.md) for full integration prerequisites.

## Enable Associate View (Associate UI)

Enable the Associate UI at the document level so the Interactive Communications can be used by associates.

1. Open your Interactive Communication in the editor.
1. From the top action bar or document options, open **Interactive Communication Settings** (or **Settings**).

   ![Interactive Communication Settings - Associate Properties with Enable Associate View Editing](/help/forms/assets/associate-ui-settings.png)

1. In the left panel, ensure **Associate Properties** is selected.
1. On the right, check **Enable Associate View Editing**.
1. Click **Apply Changes**, then save the document.

   ![Interactive Communication Settings - Associate Properties with Enable Associate View Editing](/help/forms/assets/associate-ui-enable-view.png)

A message may remind you to apply changes and save the document to enable Associate View. After saving, the IC is available for associate-driven use.

### Allow Associate UI editing per component

Once Associate View is enabled for the IC, you must turn on **Allow Editing By Associate** for each component that associates should be able to edit. Components without this setting turned on remain read-only in the Associate UI.

1. In the IC editor, select the component (for example, a text field) in the canvas or in the Component Hierarchy.
1. In the right-hand **Properties** panel, expand **Associate Properties**.
1. Turn **Allow Editing By Associate** **On** for that component.
1. Repeat for every component that associates need to edit, then save the document.

![Allow Editing By Associate in component properties](/help/forms/assets/associate-ui-allow-editing-by-associate.png)

>[!NOTE]
>
> **Associate Properties** also include options such as **Typography** (font, size, and styling for the field in the Associate UI), **Tooltip**, and **Patterns** (validations). Use these to control how the component looks and behaves when associates edit it—for example, set validation patterns so associates enter data in the required format.

## Configure workflow for Associate UI

To run an AEM workflow when users submit or update data from the Associate UI, configure the following:

1. In **Interactive Communication Settings**, select **Workflow** in the left panel (under Associate Properties).
1. Turn **Configure Workflow for Update** **On**.
1. In **Select workflow model**, choose the AEM workflow model to run (for example, `conversionWorkflow` or a path such as `/var/workflow/models/submit-workflow-1`).
1. Optionally set **Workflow Success Message** (shown to the user after the workflow completes).
1. Optionally set **Redirection URL** to send the user to a specific page after submission.
1. Click **Apply Changes** and save the document.

   ![Interactive Communication Settings - Workflow configuration for Associate UI](/help/forms/assets/associate-ui-configure-workflow.png)

When you enable a workflow, it runs whenever users submit from the Associate UI. For how submission and workflow work—where they run, who uses which instance, and key considerations—see [Submission workflow for Associate UI](/help/forms/interactive-communication/submission-workflow-associate-ui-ic-pdf.md#submission-and-workflow-behavior). That article also includes an example of a workflow that generates PDF from IC submissions.

## Complete the Associate UI setup

After enabling Associate View and optionally configuring workflow:

1. **Enable editable fields:** In the required sections of the IC, enable the fields that associates are allowed to edit. Set validations and mandatory/read-only behavior as needed.
1. **Publish the IC** so it is available on the Publish instance for associates.
1. Share the published IC link with associates. They authenticate (for example, via [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id)) and open the Associate UI, enter or confirm customer data, and generate the final communication. If you configured a workflow, it runs on submission. For how submission and workflow work, see [Submission workflow for Associate UI](/help/forms/interactive-communication/submission-workflow-associate-ui-ic-pdf.md#submission-and-workflow-behavior).

## See also

- [Associate UI in Interactive Communication Editor](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md)
- [Integrate Associate UI in Your Application](/help/forms/interactive-communication/invoke-associate-ui.md)
- [Submission workflow for Associate UI — IC Generate PDF Output](/help/forms/interactive-communication/submission-workflow-associate-ui-ic-pdf.md) — how submission and workflow work, plus an example workflow that generates PDF from IC submissions.
