---
title: Edge Delivery Services for AEM Forms Overview
description: Learn how to use Edge Delivery Services to create and deliver high-performance forms with AEM Forms, enabling rapid development and streamlined data collection.
feature: Edge Delivery Services
exl-id: ecea1e05-d36b-4d63-af9d-c69dafd2f94f
role: Admin, Architect, Developer
---

# Edge Delivery Services for AEM Forms
 

Edge Delivery Services for AEM Forms is a composable set of services that enables a rapid development environment where authors can update, publish, and launch new forms rapidly. These services deliver exceptional and high impact forms experiences that drive engagement and conversions. These forms experiences are easy to author and develop.

*   **Faster Experiences:** Forms are delivered from a global Content Delivery Network (CDN), ensuring they load quickly for users.
*   **Rapid Development:** A streamlined development process allows for faster updates. Changes can be published without waiting for long pipeline builds.
*   **Flexible Authoring:** Choose from various tools to create forms, including document-based authoring (Microsoft Word, Google Docs/Sheets) or a visual WYSIWYG editor (Universal Editor).

## How it works

With Edge Delivery Services, your form's structure and content can reside in sources like AEM as a Cloud Service, Microsoft SharePoint, or Google Drive. This content is published to a global CDN. When a user visits your site, the form is served directly from the nearest CDN edge server for optimal performance.

![Simplified architecture diagram showing content sources, a CDN, and the user.](/help/forms/assets/eds-simplified-architecture.png)
**Simplified Edge Delivery Services Architecture with Forms**

The data submitted by users can be sent to various destinations, from a simple spreadsheet to a powerful AEM backend for further processing.

## Choosing an authoring method

You have several ways to create forms for your Edge Delivery Services sites. The best method depends on your team's skills, the form's complexity, and your project requirements.

![Decision tree to help choose a form authoring method.](/help/forms/assets/eds-authoring-selection.png)
**Form Authoring Decision Tree**

### Document-Based Authoring

This method allows you to [create forms using Microsoft Word or Google Docs/Sheets](/help/edge/docs/forms/create-forms.md). You define form fields, labels, and types in a document using a specific table format. Edge Delivery Services converts this document into an interactive HTML form.

**Features:**

*   Author in familiar tools: Word, Google Docs, or Google Sheets.
*   Define fields like text inputs, email, dropdowns, checkboxes, and radio buttons.
*   Set basic validation rules, such as required fields.
*   Integrate Google reCAPTCHA for spam protection.
*   Support for file uploads.
*   Submit data directly to a spreadsheet or email address.
*   Extend with custom code via GitHub for advanced components and styling.

**Best for:**

*   Teams who primarily use document editors for content creation.
*   Quickly creating simple to moderately complex forms.
*   Simple data collection to a spreadsheet or email.

Submissions from document-based forms are typically handled by the [AEM Forms Submission Service](/help/forms/forms-submission-service.md), which routes data to a configured spreadsheet or email address.

### Universal Editor Authoring

The [Universal Editor provides a modern, WYSIWYG interface](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) for building forms with a drag-and-drop experience.

**Features:**

*   Visual, drag-and-drop form building with a library of pre-built components.
*   Configure real-time validation and complex business logic (e.g., show/hide fields based on user selections).
*   Live preview for different devices.
*   Deep integration with AEM as a Cloud Service features like Content Fragments, AEM Workflows, and user permissions.
*   AI-assisted form creation and editing through the "Experience Builder."

**Best for:**

*   Building complex forms with conditional logic, multi-step panels, or personalization.
*   Teams (e.g., marketers, business users) who prefer visual tools.
*   Projects requiring strong integration with the AEM backend for data processing and workflows.

Forms built with the Universal Editor can use the [Forms Submission Service](/help/forms/forms-submission-service.md) or be configured to use [submit actions provided OOTB for advanced data handling](/help/edge/docs/forms/configure-submission-action-for-eds-forms.md), such as sending data to an AEM Workflow, a REST endpoint, or to a database.

### Embedding Forms in Document Authoring Pages

[Document Authoring (DA)](https://www.aem.live/developer/da-tutorial) is an Adobe-hosted service for managing website content for Edge Delivery Services. While DA is not a form-building tool itself, you can use it to author web pages and then embed forms created with other methods.

**How it Works:**

1.  **Create the Form:** Build your form using either Document-Based Authoring or the Universal Editor.
2.  **Publish the Form:** Ensure the form is published and accessible at its own URL.
3.  **Embed in DA:** On your Document Authoring page, add a block that references the form's URL to embed it.

This approach is for teams that use Document Authoring as their primary content management system for Edge Delivery Services sites.

## Authoring Method Comparison

| Criteria                         | Document-Based Authoring              | Universal Editor (WYSIWYG)             | Forms in Document Authoring (DA)         |
|----------------------------------|---------------------------------------|-----------------------------------------|-------------------------------------------|
| **Primary Authoring Tool**     | Word/Google Docs/Sheets               | Browser (AEM Universal Editor)          | N/A (Forms are *embedded*)                |
| **Team Skill Level**           | Familiar with document editors        | Comfortable with visual web tools       | Uses DA for page content                  |
| **Typical Form Complexity**    | Simple to Moderate                    | Moderate to Complex, Enterprise-grade   | Depends on the embedded form              |
| **Submission Options** | Forms Submission Service (to Sheet/Email) | Forms Submission Service, AEM Publish (Workflow, Form Data Model, third-party integrations)   | Follows embedded form's setup           |
| **AEM Backend Integration**    | Minimal                               | High (with AEM Publish submission)      | Indirectly, via embedded Universal Editor form          |
| **Best For...**                | Rapid creation of simple forms by content teams, quick data capture. | Marketers and business users needing visual control, complex forms, or deep AEM integration. | Sites where primary content is managed in DA. |

<!-- 
## Detailed Feature Comparison

| **Capability**                        | **Universal Editor (WYSIWYG)** | **Document-based Authoring** | **Document Authoring (DA)** |
|-----------------------------------------|-------------------------------|-----------------------------|-----------------------------|
| **Unified Composition with Sites**    | ✅                            |                              | ✅ (with embedded forms)     |
| **Embedding Form Support**            | ✅                            | ✅                          | ✅ (embed from Universal Editor or Docs)   |
| **Rules (Dynamic Behavior)**          | Advanced rules editor with custom functions | Limited: Show/hide, compute value, custom functions | Depends on embedded form     |
| **Attachment Support**                | ✅                            | ℹ️ (Early Access)           | Depends on embedded form     |
| **CAPTCHA Support**                   | reCAPTCHA Enterprise          | reCAPTCHA Enterprise       | Depends on embedded form     |
| **Submission Features**               | REST, Email, FDM, Workflow, SharePoint, OneDrive, Azure Blob, Power Automate, Workfront Fusion (EA) | Only Spreadsheet            | Follows embedded form's setup |
| **Data Schema**                       | FDM, Custom                   | Custom                      | Based on embedded form       |
| **Pre-fill**                          | 💡 (via Wizard)               | ✅                          | Depends on embedded form     |
| **Fragments**                         | ✅                            | ✅                          | Depends on embedded form     |
| **Visual Rule Editor**                | ✅                            |                              |                              |
| **Localization**                      | 💡 (via Sites)                | ℹ️ (Excel/Sheets manual)    | Depends on embedded form     |
| **Template Support**                  | Only Initial Content          |                              |                              |
| **Theme**                             | ℹ️ (at project level)         | ℹ️ (at project level)        | ℹ️ (based on hosting site)    |
| **Custom Component**                  | ✅                            | ✅                          | ✅ (if embedded component supports it) |
| **Experimentation**                   | ✅                            | ✅                          | Depends on embed context     |
| **Submit Action**                     | ✅                            | Only Spreadsheet            | Based on embedded form       |
-->



## Next Steps

*   [Create a Form with Document-Based Authoring](/help/edge/docs/forms/tutorial.md)
*   [Learn about Universal Editor for Forms](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md)
*   [Configure Form Submission Actions](/help/edge/docs/forms/configure-submission-action-for-eds-forms.md)
*   [Learn about Document Authoring (DA)](https://www.aem.live/developer/da-tutorial) 
