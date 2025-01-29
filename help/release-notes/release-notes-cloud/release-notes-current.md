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

Turn quickly any Edge Delivery page into a page template. This ability lets you start a new page with a pre-defined structure & content instead of a blank page. [Read more](/help/sites-cloud/authoring/universal-editor/templates.md).

**[!DNL Edge Delivery Services] CSV Importer for publishing via an AEM instance**

Manage your Edge Delivery spreadsheet data (for example, redirects) efficiently in your favorite spreadsheet tool and upload it to AEM via the new CSV importer. [Read more](/help/edge/wysiwyg-authoring/tabular-data.md#importing).

**Content Fragment Editor Commenting now generally available**

Easily collaborate with coworkers when authoring AEM Content Fragments by using the new and modernized commenting service in the AEM Content Fragment Editor. 
[Read more](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/authoring?#commenting-on-your-fragment).

**Content Fragment Editor and Admin User Interfaces, updated AEM as a Cloud Service version support**

Minimum supported AEM as a Cloud Service version for new Content Fragment Admin and Editor user interfaces is now 2023.8.13099. Earlier versions from before the general availability release of the new user interfaces are not supported anymore 

### Prerelease capabilities in AEM Sites

Enhanced [Content Fragment referencing with unique ID-based references](/help/headless/graphql-api/uuid-reference-upgrade.md), ensuring stable links that remain valid even when assets or fragments are moved, eliminating the need for updates or re-publishing. Current limitation: Page references are not yet supported with unique IDs. If pages are referenced in Content Fragments, this capability should not be used.

### Early Adopter Program {#sites-early-adopter}

**AEM REST OpenAPI for Content Fragment Delivery**

The [AEM REST OpenAPI for Content Fragment Delivery](/help/headless/aem-rest-openapi-content-fragment-delivery.md) is available now for AEM as a Cloud Service.

### Deprecated Features {#sites-deprecated}

#### SPA Editor {#spa-editor}

[The SPA Editor](/help/implementing/developing/hybrid/introduction.md) has been deprecated for new projects starting with release 2025.1.0. The SPA Editor remains supported for existing projects, but should not be used for new projects.

The preferred editors for managing headless content in AEM are now:

* [The Universal Editor](/help/edge/wysiwyg-authoring/authoring.md) for visual editing.
* [The Content Fragment Editor](/help/assets/content-fragments/content-fragments-managing.md) for form-based editing.

#### PWA Features {#pwa-features}

[The progressive web app (PWA) features](/help/sites-cloud/authoring/sites-console/enable-pwa.md) for AEM Sites are now deprecated for new projects starting with release 2025.1.0. This feature remains supported for existing projects, but should not be used for new projects

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Assets view {#assets-view-new-features}

**Dynamic Media templates**

Personalize image and text banners on-the-fly with an easy-to-use WYSIWYG Dynamic Media Template Editor, by embedding the URL in any 1st or 3rd party application, to drive highly engaging experiences with real time banner content updates.

![dynamic renditions](/help/assets/assets/dm-templates-smart-text-resize.png)

**Dynamic Media delivery report**

Gain delivery insights for assets delivered through Dynamic Media, including asset-level delivery counts, referrer details, asset paths in AEM Assets, and unique asset IDs. Generate reports for all assets in the AEM Assets repository or specific folder hierarchies. These insights let you measure the ROI of delivered assets, evaluate channel performance, and make informed decisions for asset management.

**Asset relations**

The Assets View now supports viewing and editing asset relations in a simplified asset Details panel. Easily add relationships like Source and Derivative to content so that uses can more effectively find relevant hero content.

**Reprocess assets**

Assets view now supports reprocessing assets available in a folder. You can select to either use the **Full Process** option or use advanced options, such as, default preview renditions, metadata, post-processing workflow, and processing profile.

### Early access features in Dynamic Media {#dm-early-access}

**AI-generated video captions** 

AI-generated video captions in Adobe Dynamic Media use artificial intelligence to generate captions automatically for video content. This feature is designed to improve accessibility and enhance the user experience by providing accurate, real-time captions. Captions are generated from the original audio, any additional audio tracks, or extra captions provided in the "Captions and Audio" tab on the video properties page. With support for more than 60 languages, captions can be reviewed and previewed before publishing the video.

**Dynamic Media Multi-audio and caption**

[Multi-caption and multi-audio track support for videos in Dynamic Media](/help/assets/dynamic-media/video.md#about-msma) - You can now easily add multiple captions and multiple audio tracks to a primary video. This capability means that your videos are accessible to a global audience. You can customize a single, published primary video to a global audience in multiple languages and adhere with accessibility guidelines for different geographical regions. Authors can also manage the captions and audio tracks from a single tab in the user interface.



## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in AEM Forms {#forms-new-features}

* **[Update Adobe Sign scopes easily](/help/forms/adobe-sign-integration-adaptive-forms.md)**: You can modify the scopes of an Adobe Sign configuration directly from the AEM Cloud Configurations page, making it quicker and easier to update existing configurations.

* **[Asynchronous function support for Adaptive Forms](/help/forms/using-async-funct-in-rule-editor.md)**: When your Adaptive Form requires asynchronous operations, such as external processes or data retrieval, you can use custom functions. These functions can then be configured in the Rule Editor to handle the operations efficiently.

### Pre-release features in AEM Forms {#forms-new-prerelease-features}

* **Manage Publication**: You can use the "Manage Publication" workflow to publish or unpublish forms across environments, typically from the author instance to the publish and preview instances. It allows users to publish, unpublish, or schedule the publication of content in a streamlined manner.

* **[Auto-save a draft for Core Components based Adaptive Forms](/help/forms/save-core-component-based-form-as-draft.md)**: Users can now benefit from an auto-save feature that saves a partially completed form as a draft automatically. They can return later to finish filling it out on the same or other device. This feature improves conversion rates for organizations by reducing form abandonment, as users do not need to start over form filling from the beginning.

* **[Rule editor enhancements](/help/forms/invoke-service-enhancements-rule-editor.md)**: For Adaptive Forms based on Core Components, you can use the output of Invoke Service to populate drop-down options and set repeatable or individual panels. Additionally, this output can be used to validate other fields. 

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
    * Remove Signature Field: Deletes a specified Signature Field.


<!-- 
* **Hamburger Menu Layout in Adaptive Forms**: Adaptive Forms now offers a responsive hamburger menu layout for mobile devices. This collapsible menu organizes form sections, making navigation more 
intuitive and improving the mobile form-filling experience.

* **Masked Field with Eye Icon (Password Box Component)**: The Password Box is a text input field that masks the characters typed into it by displaying placeholder symbols. It allows users to securely input sensitive information, such as passwords and enables them to toggle visibility on demand using the eye icon.

-->

## Automated Forms Conversion Service 

* **[Convert PDF Forms to Core Components based Adaptive Forms](https://experienceleague.adobe.com/en/docs/aem-forms-automated-conversion-service/using/convert-existing-forms-to-adaptive-forms)**: You can now use the Automated Forms Conversion Service to transform PDF forms, AcroForms, or XFA-based forms into Core Components based Adaptive Forms. 


>[!IMPORTANT] 
>
> Interested in joining the Early Access Program for any Forms innovation? Send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) with the list of capabilities that you are interested in.## CIF Add-on {#cloud-services-cif}

## CIF Add-on {#cif}

### Bug fixes {#bug-fixes-cif}

* Fixed UI tests to work properly with Core CIF components.
* Resolved issue with category URL format not functioning as expected in the cloud instance.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Java 21 support {#java21}

You can now build code with Java 21, which includes new features (e.g., pattern matching for switch statements, sealed classes) and performance improvements; Java 17 builds are newly supported as well. For configuration steps, including updating your Maven project and library versions, see the [Build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#using-java-support) article.

The more performant Java 21 **runtime** will be automatically deployed when a Java 17 or 21 build is detected. However, we recommend opting into the Java 21 runtime for environments built with Java 11, by emailing [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com). Learn about [Java 21 runtime requirements](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements).

>[!IMPORTANT] 
>
> Java 21 **runtime** will be gradually deployed to **all** environments (aside from those already built with Java 17 or 21, which already have Java 21 runtime), starting with sandboxes and dev/RDE in February, and then stage/production in April. 

### Sandbox program support config pipelines {#sandbox-config-pipelines}

Sandbox programs now support config pipelines, which can be configured in Cloud Manager to deploy yaml files persisted in git. 

[Learn more](/help/operations/config-pipeline.md) about config pipelines, which allow for configuration of the CDN, log forwarding, and version purge/audit log purge maintenance tasks.

### OpenAPI-based APIs - Early Adopter Program {#open-apis-earlyadopter}

Developers can deeply integrate AEM as Cloud Service features into their own applications and tools. New AEM as a Cloud Service APIs follow the OpenAPI specification, with a goal of being consistent, well-documented, and user-friendly. Credentials for endpoints requiring authentication are generated by creating Adobe Developer Console projects.

Learn more about [OpenAPI-based AEM APIs](/help/implementing/developing/open-api-based-apis.md) and try out an [end-to-end tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/invoke-openapi-based-aem-apis) illustrating configuration and usage.

Concretely, the API endpoints listed below are available as part of an early adopter program. If interested, email [aem-apis@adobe.com](mailto:aem-apis@adobe.com) describing how you intend to make use of them.

* [Sites Content Fragments APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/)
* [Assets APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/assets/author/)
* [Sites and Assets Folders APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/folders/)
* [Forms Communications APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/)

### Edge Computing - Request for Feedback! {#edge-computing-feedback}

Edge computing brings data processing closer to the browser, which has benefits including reduced latency. Adobe would love to hear if you find this technology useful for AEM Publish Delivery and Edge Delivery Services projects. Additionally, let us know what you envision using it for as input into the product roadmap. Email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with questions and comments!

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
