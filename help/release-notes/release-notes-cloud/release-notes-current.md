---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current release notes for [!DNL Adobe Experience Manager] as a Cloud Service.
mini-toc-levels: 1
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
feature: Release Information
role: Admin
---
# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2023 or 2024.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2025.1.0) is January 30, 2025. The next feature release (2025.2.0) is planned for February 27, 2025.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the January 2025 Release Overview video for a summary of the features added in the 2025.1.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3440920?quality=12)

-->

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

**[!DNL Edge Delivery Services] Page templates with Universal Editor authoring**

Turn quickly any Edge Delivery page into a page template. This allows you to start a new page with a pre-defined structure & content instead of a blank page. [Read more](/help/sites-cloud/authoring/universal-editor/templates.md).

**[!DNL Edge Delivery Services] CSV Importer for publishing via an AEM instance**

Manage your Edge Delivery spreadsheet data (e.g. redirects) efficiently in your favorite spreadsheet tool and upload it to AEM via the new CSV importer. [Read more](/help/edge/wysiwyg-authoring/tabular-data.md#importing).

### Prerelease capabilities in AEM Sites

Enhanced [Content Fragment referencing with unique ID-based references](/help/headless/graphql-api/uuid-reference-upgrade.md), ensuring stable links that remain valid even when assets or fragments are moved, eliminating the need for updates or re-publishing. Current limitation: Page references are not yet supported with unique IDs. If pages are referenced in Content Fragments, this capability should not be used.

### Early Adopter Program {#sites-early-adopter}

**AEM REST OpenAPI for Content Fragment Delivery**

The [AEM REST OpenAPI for Content Fragment Delivery](/help/headless/aem-rest-openapi-content-fragment-delivery.md), is available now for AEM as a Cloud Service.

### Deprecated Features {#sites-deprecated}

[The SPA Editor](/help/implementing/developing/hybrid/introduction.md) has been deprecated for new projects starting with release 2025.1.0. The SPA Editor remains supported for existing projects, but should not be used for new projects.

The preferred editors for managing headless content in AEM are now:

* [The Universal Editor](/help/edge/wysiwyg-authoring/authoring.md) for visual editing.
* [The Content Fragment Editor](/help/assets/content-fragments/content-fragments-managing.md) for form-based editing of headless content.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### Early access features in Dynamic Media {#dm-early-access}

**AI-generated video captions** 

AI-generated video captions in Adobe Dynamic Media use artificial intelligence to generate captions automatically for video content. This feature is designed to improve accessibility and enhance the user experience by providing accurate, real-time captions. The AI analyzes the video's audio track to transcribe speech and create captions, which can be edited for accuracy or customization. These captions help meet accessibility requirements and improve video engagement for audiences who rely on or prefer text-based video support. 

To get early access to AI-generated captions support on your Dynamic Media account, [create and submit an Adobe Customer Support case](/help/assets/dynamic-media/video.md##enable-dash).

**Dynamic Media delivery report**

Get delivery insights for assets delivered with Dynamic Media, with asset level delivery count, referrer information, asset path in AEM Assets and unique asset ID. Reports can be generated for all assets delivered via Dynamic Media for AEM Assets repository or for a specific folder hierarchy in AEM Assets. Insights help measure ROI of assets delivered, measure channel performance, and help take informed asset management tasks for assets.

To get early access to Dynamic Media Delivery Report on your Dynamic Media account, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

### New features in Assets view {#assets-view-new-features}

**Dynamic Media panel**

Assets view now enables you to access Dynamic Media and Dynamic Media with OpenAPI renditions from a separate panel made available to you. You can choose to copy the delivery URL or download the renditions based on the asset and rendition type. For more information, see [Dynamic Media renditions](/help/assets/renditions.md#dynamic-media-renditions) and [Dynamic Media with OpenAPI capabilities renditions](/help/assets/renditions.md#dm-with-openapi-renditions).

![dynamic renditions](/help/assets/assets/dm-scene7-renditions.png)

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in AEM Forms {#forms-new-features}

* **[Update Adobe Sign scopes easily](/help/forms/adobe-sign-integration-adaptive-forms.md)**: You can modify the scopes of an Adobe Sign configuration directly from the AEM Cloud Configurations page, making it quicker and easier to update existing configurations.

* **[Asynchronous function support for Adaptive Forms](/help/forms/using-async-funct-in-rule-editor.md)**: When your Adaptive Form requires asynchronous operations, such as waiting for external processes or data retrieval, you can implement these operations with custom functions and configure them in the Rule Editor.

### Pre-release features in AEM Forms {#forms-new-prerelease-features}

* **Manage Publication**: You can use the Manage Publication workflow to publish or unpublish forms across environments, typically from the author instance to the publish and preview instance(s). It allows users to publish, unpublish, or schedule the publication of content in a streamlined manner.

* **[Auto-save a draft for Core Components based Adaptive Forms](/help/forms/save-core-component-based-form-as-draft.md)**: Users can now benefit from an auto-save feature that saves a partially completed form as a draft automatically. They can return later to finish filling it out on the same or other device. This feature improves conversion rates for organizations by reducing form abandonment, as users do not need to start over form filling from the beginning.

* **[Rule editor enhancements](/help/forms/invoke-service-enhancements-rule-editor.md)**: For Adaptive Forms based on Core Components, you can now populate dropdown options using the output of Invoke Service, set repeatable panels using the output of Invoke Service, set individual panels using the output of Invoke Service and use the output parameter of Invoke Service to validate other fields. 

* **[Enhance User Experience with Navigation Buttons in Panel Layouts](/help/forms/rule-editor-core-components-usecases.md#navigating-among-panels-using-button)**: You can now add navigation buttons to your panel layouts, such as Horizontal Tabs, Vertical Tabs, Accordions, or Wizard. These buttons enhance the user experience by simplifying transitions between panels, focusing on the selected panel.

 
### Early Access features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations, and help shape their development.

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### Integrations

* **[Integrate Adaptive Forms with Adobe Marketo Engage](/help/forms/integrate-form-to-marketo-engage.md)**: AEM Forms as a Cloud Service now includes an easy-to-use option to connect Adaptive Forms with Adobe Marketo Engage. This integration allows you to create Adaptive Forms directly with Marketo Engage's lead capture and related custom objects. You can now prefill form fields with data from Marketo Engage and submit data back to automate workflows like smart campaigns and email automation. You can also connect an Adaptive Form with the Munchkin library to track the number of visits, clicks, and form submissions.

#### Adaptive Forms and HTML5 Forms

* **[Create Adaptive Forms based on existing XFA template](/help/forms/create-adaptive-form-using-xfa-templates.md)**: You can now create Core Component-based Adaptive Forms using XFA form templates (*.XDP files). This capability facilitates AEM Forms On-Premise customers with existing investments in XFA technology to adopt AEM Forms as a Cloud Service.

* **HTML5 Forms (XFA-based Web Forms)**: Now, AEM Forms On-Premise customers using XFA technology can effortlessly transition to AEM Forms as a Cloud Service while preserving their existing user experience with HTML5 Forms (XFA-based Web Forms). This capability enables the rendering of XFA form templates in HTML5 format, making forms accessible on devices that do not support XFA-based PDF forms.

   ![HTML Forms (XFA-based Web Forms)](/help/forms/assets/html-forms-xfa-based-web-forms.png) 


* **[Base64 Encoded String Support for File Attachment](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/file-attachment#basic-tab)**: The File Attachment component in Adaptive Forms based on Core Components now includes an option to submit attached files as Base64-encoded strings.

#### Interactive Communications and Communication APIs

* **Interactive Communication Editor**: The Interactive Communication Editor is a user-friendly, graphical Communication design tool that simplifies the creation of personalized, data-driven correspondences and runs in any modern browser. It supports seamless data integration, intricate logic definition, and rich media integration, ensuring professional and compliant document, Communication, and template generation for various business needs. 

   ![Interactive Communication Editor](/help/forms/assets/ic-editor.png)


* **[PDF/A Compliance Enhancements](/help/forms/aem-forms-cloud-service-communications-introduction.md#convert-to-and-validate-pdfa-compliant-documents)**: You can now use Communication APIs to convert PDF documents to PDF/A formats (1a, 2a, 3a) for archival purposes while ensuring accessibility and verifying compliance with these standards.


* **[Signature API (Document Assurance)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance)**: A new RESTful API in Communication APIs enables easy management of PDF signatures. It supports operations like:
    * Clear Signature: Removes a signature from a specified field.
    * Remove Signature Field: Deletes a specified signature field.


<!-- 
* **Hamburger Menu Layout in Adaptive Forms**: Adaptive Forms now offers a responsive hamburger menu layout for mobile devices. This collapsible menu organizes form sections, making navigation more 
intuitive and improving the mobile form-filling experience.

* **Masked Field with Eye Icon (Password Box Component)**: The Password Box is a text input field that masks the characters typed into it by displaying placeholder symbols. It allows users to securely input sensitive information, such as passwords and enables them to toggle visibility on demand using the eye icon.

-->

## Automated Forms Conversion Service 

* **[Convert PDF Forms to Core Components based Adaptive Forms](https://experienceleague.adobe.com/en/docs/aem-forms-automated-conversion-service/using/convert-existing-forms-to-adaptive-forms)**: You can now use Automated Forms Conversion Service to transform PDF forms, AcroForms, or XFA-based forms into Core Components based Adaptive Forms. 


>[!IMPORTANT] 
>
> Interested in joining the Early Access Program for any Forms innovation? Send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) with the list of capabilities that you are interested in.## CIF Add-on {#cloud-services-cif}

## CIF Add-on {#cif}

### Bug fixes {#bug-fixes-cif}

* Fixed UI tests to work properly with Core CIF components.
* Resolved issue with category URL format not functioning as expected in the cloud instance.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Improved Tree Replication Performance (and deprecation of Publish Content Tree Workflow) {#tree-replication-performance}

[Tree Activation Workflow Step](/help/operations/replication.md#tree-activation) is a new workflow model step recommended for replicating deep content hierarchies. Of note, it allows independent replications (e.g., through quick publish or manage publication) to proceed in parallel with the in-progress tree replication workflow. This is particularly useful if you need to publish some time-sensitive content while a bulk replication is still in-progress. Tree Replication Step replaces Publish Content Tree Workflow and its related Workflow Step, which are now deprecated. 

### OpenAPI-based APIs - Early Adopter Program {#open-apis-earlyadopter}

Developers can deeply integrate AEM as Cloud Service features into their own applications and tools. New AEM as a Cloud Service APIs will follow the OpenAPI specification, with a goal of being consistent, well-documented, and user-friendly. Credentials for endpoints requiring authentication will be generated by creating Adobe Developer Console projects.

Learn more about [OpenAPI-based AEM APIs](/help/implementing/developing/open-api-based-apis.md) and try out an [end-to-end tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/invoke-openapi-based-aem-apis) illustrating configuration and usage.

Concretely, the API endpoints listed below are available as part of an early adopter program. If interested, email [aem-apis@adobe.com](mailto:aem-apis@adobe.com) describing how you intend to make use of them.
* [Sites Content Fragments APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/)
* [Assets APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/assets/author/)
* [Sites and Assets Folders APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/folders/)
* [Forms Communications APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/)

### Edge Computing - Request for Feedback! {#edge-computing-feedback}

Edge computing brings data processing closer to the browser, which has benefits including reduced latency. As input into the roadmap, we'd love to hear if you'd find this technology useful for AEM Publish Delivery and Edge Delivery Services projects and what you envision using it for. Email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with questions and comments!

### New AEM Developer Console (Public Beta) {#aem-developer-console-beta}

Try out a revamped [AEM Developer Console](/help/implementing/developing/introduction/aem-developer-console.md), which offers a more interactive experience for debugging code in Cloud environments.

Anyone can access the public beta by clicking the *New Console Available* button in the current AEM Developer Console. Adobe welcomes feedback, which you can email to [aemcs-new-devconsole-ui-beta@adobe.com](mailto:aemcs-new-devconsole-ui-beta@adobe.com)

## [!DNL Experience Manager] Guides {#guides}

You can find a complete list of new and enhanced features of the latest release of Adobe Experience Manager Guides [here](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/release-notes/cloud-release-notes/2024-releases/2410-release/2410-0-release/whats-new-2024-10-0).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).

## Universal Editor {#universal-editor}

You can find a complete list of Universal Editor releases [here](/help/release-notes/universal-editor/current.md).

## Generate Variations {#generate-variations}

You can find a complete list of Generate Variations releases [here](/help/generative-ai/release-notes-generate-variations.md).

## Experience Cloud Release Notes {#experience-cloud}

You can find information about releases of other Experience Cloud applications [here](https://experienceleague.adobe.com/en/docs/release-notes/experience-cloud/current).
