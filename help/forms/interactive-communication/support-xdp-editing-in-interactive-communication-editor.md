---
title: Support XDP Editing in Interactive Communication Editor
description: Support XDP Editing in Interactive Communication Editor allows existing xdps to be edited inside the Interactive Communication Editor.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
---

# Support XDP Editing in Interactive Communication Editor

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the Forms Experience Builder continues to evolve during the early-adopter program.

## Introduction

The Interactive Communication (IC) Editor now offers seamless **support for editing XDP (XML Data Package) files** within the authoring environment. This enhancement empowers authors to manage, modify, and maintain XDP templates effortlessly, without relying on external tools. With this capability, users can upload, view, and edit XDP files directly in the IC Editor, enabling a unified and efficient design-to-delivery workflow.

## How to Use Support XDP Editing in Interactive Communication Editor

![Find IC Doc](/help/forms/interactive-communication/assets/support-xdp.png)

1. Navigate to **Forms > Forms & Documents**.

1. Upload your .xdp file using the **Create > File Upload** option.

1. Open the XDP in **Interactive Communication Editor**.

1. Make necessary **design or data-binding** changes.

1. Save your changes, updates are automatically reflected in the source XDP file.

## Key Capabilities

- **Upload and Manage XDP Files:**
Upload XDP templates through **Forms Manager**. Once uploaded, they become available for direct editing in the Interactive Communication Editor.

- **Edit Using IC Editor:**
Open and edit XDPs using the IC Editor with full access to existing editing features, including layout adjustments, data binding, styling, and component configuration.

- **Save Back to Source:**
Any modifications made through the IC Editor are saved directly to the original XDP file, maintaining version integrity and simplifying the design workflow.

## Fragment Support

- **Fragment References:**
If an XDP references a fragment, that fragment must exist in **AEM at the same relative path** as defined in the XDP file.
If a fragment is missing, the editor displays a **warning message** indicating that the required fragment is not present.

- **Fragment Reuse in Editor:**
All existing XDP fragments appear in the **Fragments Panel** of the IC Editor.
Authors can **drag and drop** these fragments directly onto the canvas. The references are preserved, ensuring that updates to fragments propagate across all XDPs using them.

## Benefits

- Eliminates dependency on external tools for XDP modification.

- Preserves existing data bindings and fragment relationships.

- Enables consistent design and faster iteration cycles.

## Best Practices

- Ensure all referenced fragments exist in the correct relative path before editing.

- Use version control to manage updates across XDP and fragment dependencies.

- Validate data bindings post-edit to confirm correct rendering.

