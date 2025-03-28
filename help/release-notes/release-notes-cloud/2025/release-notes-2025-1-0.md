---
title: Release Notes for 2025.1.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2025.1.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 085629bf-fb24-4511-af6c-bbbeedcb6b98
---
# 2025.1.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2025.1.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2023 or 2024.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2025.1.0) is January 30, 2025. The next feature release (2025.2.0) is planned for March 4, 2025.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the January 2025 Release Overview video for a summary of the features added in the 2025.1.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3440920?quality=12)

-->

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

**Content Fragment Editor Commenting now generally available**

Easily collaborate with coworkers when authoring AEM Content Fragments by using the new and modernized commenting service in the AEM Content Fragment Editor. 
[Read more](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/authoring?#commenting-on-your-fragment).

**Content Fragment Editor and Admin User Interfaces, updated AEM as a Cloud Service version support**

Minimum supported AEM as a Cloud Service version for new Content Fragment Admin and Editor user interfaces is now 2023.8.13099. Earlier versions from before the general availability release of the new user interfaces are not supported anymore 

### Early Adopter Program {#sites-early-adopter}

**Enhanced Content Fragments** 

Enhanced [Content Fragment referencing with unique ID-based references](/help/headless/graphql-api/uuid-reference-upgrade.md), helping to ensure GraphQL queries for individual content fragments can remain stable even if the fragment was moved to another location. This is now possible with "ByID" queries. While paths can change, potentially breaking "ByPath" queries, UUIDs are stable. The new IDs can also be returned as properties in any query or other applicable API request. Current limitation (2025.1): Page references are not yet supported with unique IDs. If pages are referenced in Content Fragments, this capability should not be used. The limitation is planned to be removed in the next AEM as a Cloud Service release. 

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

### New features in AEM Assets view {#new-features-assets}

**Customize search filters**

Custom Search filters enhance the precision and efficiency of finding relevant information. It allows for more tailored searches, filtering data according to specific attributes such as brand, product, category, or other key identifiers. This improves organization, reduces time spent sifting through irrelevant results, and enables quicker decision-making. It also supports scalability, as large datasets become easier to navigate and analyze.

![custom search filters](/help/assets/assets/custom-search-filters.png)

### New features in Content Hub {#new-features-content-hub}

Description

### Early Access features in AEM Assets {#early-access-features-assets}

**AI-generated video captions** 

AI-generated video captions in Adobe Dynamic Media use artificial intelligence to generate captions automatically for video content. This feature is designed to improve accessibility and enhance the user experience by providing accurate, real-time captions. Captions are generated from the original audio, any additional audio tracks, or extra captions provided in the "Captions and Audio" tab on the video properties page. With support for more than 60 languages, captions can be reviewed and previewed before publishing the video.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in AEM Forms {#forms-new-features}

* **Manage Publication**: You can use the [Manage Publication](/help/forms/manage-publication.md#publish-forms-using-the-manage-publication-option))workflow to publish or unpublish forms across environments, typically from the author instance to the publish and preview instances. It allows users to publish, unpublish, or schedule the publication of content in a streamlined manner.

* **[Auto-save a draft for Core Components based Adaptive Forms](/help/forms/save-core-component-based-form-as-draft.md)**: Users can now benefit from an auto-save feature that saves a partially completed form as a draft automatically. They can return later to finish filling it out on the same or other device. This feature improves conversion rates for organizations by reducing form abandonment, as users do not need to start over form filling from the beginning.

* **[Rule editor enhancements](/help/forms/invoke-service-enhancements-rule-editor.md)**: For Adaptive Forms based on Core Components, you can use the output of Invoke Service to populate drop-down options and set repeatable or individual panels. Additionally, this output can be used to validate other fields. 

* **[Enhance User Experience with Navigation Buttons in Panel Layouts](/help/forms/rule-editor-core-components-usecases.md#navigating-among-panels-using-button)**: You can now add navigation buttons to your panel layouts, such as Horizontal Tabs, Vertical Tabs, Accordions, or Wizard. These buttons enhance the user experience by simplifying transitions between panels, focusing on the selected panel.

 
### Early Access features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations, and help shape their development.

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### [HTML email Templates in Adaptive Forms](/help/forms/html-email-templates-in-adaptive-forms.md)

Adaptive Forms allows you use HTML email templates. HTML email templates enable you to send rich, personalized, and visually appealing emails when a form is submitted. These emails can be customized with form data and enhanced using various email tags, such as images and links. With Adaptive Forms, you can either upload a file containing an HTML template or use a plain-text editor to create these templates.

![HTML email templates](/help/forms/assets/html-email.png)

#### Enhanced Cloud Storage Support: Direct PDF Upload to Azure Blob Storage

AEM Forms Document Generation APIs now support direct upload of generated PDF documents to Azure Blob Storage. This enhancement streamlines storage and retrieval, improving efficiency and integration with cloud workflows.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Java 21 support {#java21}

You can now build code with Java 21, which includes new features (e.g., pattern matching for switch statements, sealed classes) and performance improvements; Java 17 builds are newly supported as well. For configuration steps, including updating your Maven project and library versions, see the [Build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#using-java-support) article.

The more performant Java 21 **runtime** will be automatically deployed when a Java 17 or 21 build is detected. However, we also recommend opting into the Java 21 runtime for environments built with Java 11, by emailing [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com). Learn about [Java 21 runtime requirements](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements).

>[!IMPORTANT] 
>
> Java 21 **runtime** will be gradually deployed to **all** environments (aside from those already built with Java 17 or 21, which already have Java 21 runtime), starting with sandboxes and dev/RDE in February, and then stage/production in April. 

### Sandbox programs support config pipelines {#sandbox-config-pipelines}

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
