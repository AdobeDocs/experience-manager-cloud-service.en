---
title: How to author forms in AEM?
description: Learn about the various form authoring platforms available in Adobe Experience Manager (AEM) and how to choose the right one based on your requirements.
feature: Edge Delivery Services, Adaptive Forms, Core Components
role: User, Developer
hide: yes
hidefromtoc: yes
---

# How to Author Forms in Adobe Experience Manager (AEM)?

Adobe Experience Manager (AEM) provides a flexible platform for creating forms that are engaging, responsive, dynamic, and adaptive. It offers an intuitive user interface and a rich set of out-of-the-box components for building and managing Adaptive Forms. Forms can be authored with or without a form model or schema, depending on your requirements.

## Key considerations while choosing an authoring platform 

AEM provides multiple form authoring options to create interactive and engaging forms. When selecting a form authoring environment, consider the following factors:

| 📝 **Consideration** | 💡 **What to Ask** |
|----------------------|--------------------|
| **User Expertise** | Who will be authoring the forms—developers, business users, or content authors? |
| **Form Complexity** | Does the form need advanced rules, dynamic sections, or integrations? |
| **Reusability Needs** | Will parts of the form be reused across different forms or projects? |
| **Design Flexibility** | Do you need full control over layout, themes, and styling? |
| **Integration Requirements** | Does the form need to connect to data models, workflows, or external systems? |
| **Ease of Use** | Is the platform intuitive for your team's technical skill level? |
| **Performance & Scalability** | Will the form be used at scale or in high-traffic environments? |
| **Omnichannel Delivery** | Will the form be used on websites, mobile apps, kiosks, or multiple channels? |
| **Publishing Flexibility** | Where will the forms be published on AEM, Edge Delivery, or custom apps? |

## Overview of form authoring methods in AEM

AEM supports multiple authoring methods, each suited for different user needs, technical skill levels, and publishing destinations.

* [Foundation Components](/help/forms/create-adaptive-form-tutorial.md): Use Foundation Components to build traditional, interactive forms. Best suited for forms that integrate with legacy systems or rely on long-established workflows. Forms authored with Foundation Components can be published on AEM only, and are not compatible with Edge Delivery Services.

* [Core Components](/help/forms/creating-adaptive-form-core-components.md): Use Core Components to create modern, responsive, and scalable forms. They support reusability, accessibility, and better performance. Forms authored with Core Components can be published on both AEM and Edge Delivery Services, offering flexibility across platforms.

* [Edge Delivery Services Forms](/help/edge/docs/forms/overview.md): Edge Delivery Services Forms transform the way forms are authored, executed, and processed. By leveraging Edge Delivery Services, organizations can create fast, secure, and highly available digital forms, enhancing user experience and operational efficiency with a rapid development environment. You can author the Edge Delivery Services Forms in two ways:
  * [WYSIWYG Authoring](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md): Use the Universal Editor for visual, drag-and-drop form creation ideal for content authors with limited technical knowledge. Forms authored with Universal Editor are delivered using Edge Delivery Services for fast, lightweight rendering.
  * [Document-Based Authoring](/help/edge/docs/forms/tutorial.md): Use tools like Microsoft Excel or Google Sheets to define form structure and content. This method is useful for business users who prefer spreadsheet-driven input. These forms are typically published through Edge Delivery Services and are suitable for lightweight, high-volume use cases.
* [Headless Authoring](https://experienceleague.adobe.com/en/docs/experience-manager-headless-adaptive-forms/using/tutorial/build-engaging-forms-using-core-components-and-headless-adaptive-forms-aem-forms-cloud-service): Use APIs to render forms as JSON for any frontend—such as React, Angular, mobile apps, or kiosks—without depending on AEM. Currently, only Core Components support headless delivery. Headless forms are ideal for omnichannel use cases and are consumed independently of AEM's page rendering, making them flexible for custom front-end deployments.

### Comparative analysis of AEM form authoring methods

​The following table offers a concise comparison of various AEM form authoring methods, highlighting the approaches, features, publishing options, and ideal use cases to assist in selecting the most suitable method for your needs.

| **Consideration**| **Foundation Components** | **Core Components** | **Universal Editor (WYSIWYG)**  | **Document-based Authoring** | **Headless Authoring** |
|--------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Ideal For**            | Maintaining legacy forms and workflows within AEM                   | Scalable, modern forms with complex workflows and integrations         | Creating forms for Edge Delivery Service sites with complex requirements | Quick prototyping or basic forms without advanced submission services    | Omnichannel experiences across platforms (web, mobile, kiosks, etc.)    |
| **User Expertise**       | Developers, Content Authors     | Developers, Advanced Authors                                           | Business Users, Content Authors | Business Users  | Developers  |
| **Form Complexity** | Basic forms | Complex forms with dynamic sections| Complex forms with custom actions | Simple forms  | Highly complex, API-driven forms  |
| **Design Flexibility**   | Limited   | High (CSS/JS customization)  | Moderate (based on templates) | Limited | High (frontend framework control)                                       |
| **Integration Capability** | Basic AEM workflows | Advanced (data models, workflows)  | Integrated with external systems | Basic (Google Sheets, Excel)   | Full control via APIs  |
| **Publishing Method**    | AEM only   | AEM and Edge Delivery Services| Edge Delivery Services | Edge Delivery Services| Any frontend via APIs|
| **Performance & SEO**    | Standard | Improved over Foundation Components  | High Google Lighthouse scores for faster rendering and better SEO| High Google Lighthouse scores for faster rendering and better SEO        | Depends on implementation  |
| **Omnichannel Delivery** | Limited | Moderate  | Moderate   | Limited | High|

<!--
| **Form authoring methods** | **Key Approach** | **Features** | **Publishing Method** | **Use Cases** |
|-----------------------------|------------------|--------------|-----------------------|---------------|
| **Foundation Components** | Classic AEM authoring interface designed for standard web pages. | Includes basic components like text, images, tables, and charts. Limited reuse capabilities and primarily web-based. | Published on AEM only. | Best for maintaining legacy forms and workflows within AEM. |
| **Core Components** | Provides a modern, flexible approach with high customization capabilities. | Component-based authoring within AEM, offering high customization with CSS and JS. Built around accessibility guidelines and integrated with AEM Sites. | Published on AEM and Edge Delivery Services. | Suitable for scalable, modern forms with complex workflows and integrations. |
| **Universal Editor (WYSIWYG)** | Offers a WYSIWYG interface for intuitive form creation. | Forms are designed using an intuitive drag-and-drop interface. These forms inherit look and feel from the configured Edge Delivery Services GitHub repository for the corresponding form. | Published on Edge Delivery Services, achieving high Google Lighthouse scores for faster rendering and better SEO. | Ideal for creating forms for Edge Delivery Service sites and pages, especially scenarios involving complex forms, workflows, custom actions, or integrations with external systems. |
| **Document-based Authoring** | Uses familiar tools like Google Docs and Microsoft Office for form creation. | Forms are designed using spreadsheets, with data directly submitted to Google Sheets or Microsoft Excel. These forms are faster to create and deploy. No prior knowledge of AEM is required to develop custom components and styles for these forms. | Published on Edge Delivery Services, achieving high Google Lighthouse scores for faster rendering and better SEO. | Ideal for quick prototyping or basic forms where advanced submission services are not needed. Well-suited for surveys, registration, or feedback forms requiring data storage in spreadsheets. |
| **Headless Authoring** | Enables API-driven content creation for omnichannel delivery. | Full control via frontend frameworks, allowing content delivery across various platforms through APIs. | Can be integrated with any frontend via APIs. | Ideal for omnichannel experiences across platforms, suitable for web, mobile, kiosks, and more. |-->

### Feature comparison of AEM form authoring methods

The following table provides a detailed comparison of key features across different AEM form authoring methods, assisting in selecting the most suitable approach for your requirements.​

| **Capability**                          | **Foundation Components** | **Core Components** | **Universal Editor (WYSIWYG)** | **Document-based Authoring** | **Headless Authoring** |
|-----------------------------------------|---------------------------|---------------------|-------------------------------|-----------------------------|------------------------|
| **Unified Composition with Sites**      | ❌                        | ✅                  | ✅                            | ❌                          | ❌                     |
| **Embedding Form Support**              | ✅                        | ✅                  | ✅                            | ✅                          | ✅                     |
| **Rules (Dynamic Behavior)**            | Advanced rules editor with custom functions | Advanced rules editor with custom functions | Advanced rules editor with custom functions | Limited: Show/hide, compute value, custom functions | Limited: Requires custom implementation |
| **Attachment Support**                  | ✅                        | ✅                  | ✅                            | ℹ️ (Early Access)           | ❌                     |
| **CAPTCHA Support**                     | reCAPTCHA v2/Enterprise, hCaptcha (EA), Turnstile (EA) | reCAPTCHA v2/Enterprise, hCaptcha (EA) | reCAPTCHA Enterprise       | reCAPTCHA Enterprise   | Requires custom integration |
| **Submission Features**                 | REST endpoint, Email, Form Data Model (FDM), Invoke AEM Workflow, SharePoint, OneDrive, Azure Blob Storage, Power Automate, Workfront Fusion (EA) | REST endpoint, Email, Form Data Model (FDM), Invoke AEM Workflow, SharePoint, OneDrive, Azure Blob Storage, Power Automate, Workfront Fusion (EA) | REST endpoint, Email, Form Data Model (FDM), Invoke AEM Workflow, SharePoint, OneDrive, Azure Blob Storage, Power Automate, Workfront Fusion (EA) | Only Spreadsheet        | Custom API endpoints   |
| **Data Schema**                         | FDM, Custom               | FDM, Custom         | FDM, Custom                   | Custom                      | Custom                 |
| **Pre-fill**                            | ✅                        | ✅                  | 💡 (via Wizard)               | ✅                          | Custom implementation  |
| **Fragments**                           | ✅                        | ✅                  | ✅                            | ✅                          | ❌                     |
| **Visual Rule Editor**                  | ✅                        | ✅                  | ✅                            | ❌                          | ❌                     |
| **Localization**                        | ✅                        | ✅                  | 💡 (via Sites)                | ℹ️ (Excel - Manual, Google Sheets Function) | Custom implementation |
| **Data Schema (Data Tree)**             | ✅                        | ✅                  | 💡 (via UI Extension)         | ❌                          | Custom implementation  |
| **Template Support**                    | ✅                        | ✅                  | Only Initial Content, No Policy | ❌                          | Custom implementation  |
| **Portal**                              | ✅                        | ✅                  | ❌                            | ❌                          | ❌                     |
| **DoR Authoring**                       | ✅                        | ✅                  | 💡 (via Derlina)              | ❌                          | ❌                     |
| **DoR Generation**                      | ✅                        | ✅                  | 💡 (FORMS-2475 New)           | ❌                          | ❌                     |
| **Theme**                               | ✅                        | ✅                  | ℹ️ (at project level)          | ℹ️ (at project level)        | Custom implementation  |
| **Custom Component**                    | ✅                        | ✅                  | ✅                            | ✅                          | ✅                     |
| **OOTB & Custom Functions**             | ✅                        | ✅                  | ✅                            | ✅                          | ✅                     |
| **Fragment Reference**                  | ✅                        | ❌                  | ❌                            | ❌                          | ❌                     |
| **Sign Integration**                    | ✅                        | ❌                  | ❌                            | ❌                          | ❌                     |
| **RTL Support**                         | ❌                        | ✅                  | 💡                            | 💡                          | Custom implementation  |
| **Experimentation**                     | ❌                        | ❌                  | ✅                            | ✅                          | Custom implementation  |
| **Task Management via Workfront**       | ❌                        | ❌                  | ✅                            | ❌                          | ❌                     |
| **Personalization Extension**           | ❌                        | ❌                  | 💡                            | ❌                          | Custom implementation  |
| **Editor Customization**                | ❌                        | ❌                  | ✅ (via UI Extension)          | ❌                          | Custom implementation  |
| **Submit Action**                       | ✅                        | ✅                  | ✅                            | Only Spreadsheet            | Custom implementation  |


## Related Article

* [Document-based authoring using Microsoft Excel or Google Sheets](/help/edge/docs/forms/create-forms.md)
* [Universal Editor for WYSIWYG authoring](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/wysiwyg-authoring/authoring)
* [Create an Adaptive Form (Foundation Components)](/help/forms/creating-adaptive-form.md)
* [Create an Adaptive Form (Core Components)](/help/forms/create-an-adaptive-form.md)
