---
title: Getting Started with Forms on AEM Edge Delivery Services
description: Learn how to create and deliver high-performing forms on Adobe Experience Manager Edge Delivery Services, with an emphasis on the Universal Editor authoring approach.
feature: Edge Delivery Services
exl-id: ecea1e05-d36b-4d63-af9d-c69dafd2f94f
role: Admin, Architect, Developer
---

# Getting Started with Forms on AEM Edge Delivery Services

<!--
<span class="preview"> This is a pre-release feature available through our <a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features">pre-release channel</a>. </span>
-->

Adobe Experience Manager (AEM) Edge Delivery Services (EDS) lets you serve blazing-fast, highly scalable web experiences from the edge. This guide explains **how to build and publish forms for those experiences**—with a clear recommendation hierarchy:

1. **Universal Editor (UE) – Best choice for most teams**  
2. **Document-Based Authoring (Docs/Sheets) – Great for quick, simple forms**  
3. **Document Authoring (DA) – Use to embed forms into DA-authored pages**

By the end you will be able to pick the right authoring method, understand submission options, and follow next steps toward production-ready forms.



## Choosing an Authoring Method

| Team & Requirement | Recommended Method | Why |
|--------------------|--------------------|-----|
| Marketers / Designers need visual control, conditional logic, or AEM integrations | **Universal Editor** | Drag-and-drop, advanced rules, submits to FSS or AEM Publish |
| Content authors already working in Word / Google Docs / Sheets; simple data capture to spreadsheet/email | **Document-Based Authoring** | Familiar tools, fastest path for basic forms |
| Website pages built in **Document Authoring (DA)** | **Embed** a UE or Doc-Based form into the DA page | DA does not build forms itself |


## Authoring Methods in Detail

### Universal Editor 

Universal Editor is a visual, drag-and-drop authoring tool for marketers and designers that combines speed with enterprise-grade power:

- Real-time WYSIWYG editing and device previews.
- Advanced rules and validation UI—no code required.
- Direct integration with AEM assets, workflows, and Form Data Model (FDM).
- Seamless hand-off to developers for custom components in vanilla JS/CSS.
- Flexible submission targets: start simple with the **Forms Submission Service (FSS)** or switch to **AEM Publish submit actions** as your needs grow.

> **Recommendation**: Start every new form project with Universal Editor unless your team is 100 % document-centric and the form is very basic.


### Document-Based Authoring (Docs/Sheets)

Document-Based Authoring is best suited for creating simple, low-complexity forms using familiar tools such as Microsoft Word, Google Docs, or Google Sheets. This method is ideal for content teams who require a fast and straightforward way to build forms.

- Define form fields within a table (Docs) or as rows (Sheets).
- Supports basic field validation and Google reCAPTCHA for spam protection.
- Form submissions are handled exclusively through the Forms Submission Service.
- Instant publishing—any changes made in the source document are immediately reflected on the site without requiring a deployment pipeline.


### Embedding Forms in Document Authoring (DA)

Document Authoring (DA) is designed for creating structured page content and does not support native form creation. To add a form to a DA-authored page, follow these steps:

1. Create the form using the **Universal Editor** (recommended) or Document-Based Authoring.
2. Publish the form to generate a unique URL (for example, `/forms/contact-us`).
3. In your DA page, insert an **Embed Form** block and specify the published form's URL.

<!-- 
## Feature Comparison

| Capability | Universal Editor | Document-Based | Document Authoring |
|------------|-----------------|----------------|--------------------|
| Visual drag-and-drop | ✅ | – | – |
| Advanced rules editor | ✅ | Limited | – |
| Attachments | ✅ | EA | – |
| reCAPTCHA Enterprise | ✅ | ✅ | Depends on embed |
| Submit to spreadsheet/email | ✅ (FSS) | ✅ (FSS) | Via embed |
| Submit to AEM workflows/FDM | ✅ | – | Via UE embed |
| Custom components (JS/CSS) | ✅ | ✅ | Via embed |
| Localization via Sites | ✅ | Manual | Via embed |

-->

## Next Steps

1. **Start with Universal Editor:** See the [Universal Editor getting started guide](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) to begin authoring forms.
2. **Configure Form Submission:** Select and set up your preferred submission method. Refer to [Forms Submission Service](/help/edge/docs/forms/configure-submission-action-for-eds-forms.md) or AEM Publish submit actions for configuration instructions.
3. **Apply Best Practices:** Review [form design best practices](/help/edge/docs/forms/universal-editor/best-practices-eds-forms.md) to ensure accessibility and performance.
4. **Use Document-Based Authoring:** To create forms with Microsoft Excel or Google Sheets, follow the [Document-Based Authoring tutorial](/help/edge/docs/forms/tutorial.md).
5. **Embed Forms in Document Authoring:** If you are building pages in Document Authoring, consult the [DA tutorial](https://www.aem.live/developer/da-tutorial) for instructions on embedding published forms.

> **You are now ready to create your first high-performance form with AEM Edge Delivery Services.**