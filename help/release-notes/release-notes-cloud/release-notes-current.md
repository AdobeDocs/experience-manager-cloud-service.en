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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2025.2.0) is March 4, 2025. The next feature release (2025.3.0) is planned for March 27, 2025.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the February 2025 Release Overview video for a summary of the features added in the 2025.2.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3440920?quality=12)

-->

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in AEM Sites {#new-features-sites}

**Content Fragment Auto-Tagging** 

When creating Content Fragments, it is now possible to automatically inherit tags that were assigned to the content model. This allows for powerful automatic classification of content stored in Content Fragments.

**Content Fragment UUID Support** 

Content Fragment UUID support is now GA. The new capability does not alter the path-based behavior of operations within AEM, such as move, rename, rollout, where paths are automatically being adjusted, but it can make external consumption of Content Fragments easier and more stable, especially when using GraphQL queries that directly target individual fragments with ByPath queries. Such queries can break if a fragment path changes. When using the new ById query type, the query now remains stable as the UUID of a fragment does not change in cases where paths do.

**Dynamic Media with OpenAPI support in Content Fragment Editor and GraphQL** 

Assets that are stored in different AEM as a Cloud Service Programs than Content Fragments, and that are enabled with the new Dynamic Media with OpenAPI capability, can now be used in Content Fragments. The image selector in the new Content Fragment Editor does now allow selecting "remote" repositories as the source for image assets to be referenced in the fragment. And on delivery of such content fragments using AEM GraphQL, the JSON response now includes required properties for remote assets (assetId, repositoryId) so client applications can create respective Dynamic Media with OpenAPI URLs to fetch the image.

**Content Fragment Editor Rollout**

We will continue enabling the new Spectrum UI-based Content Fragment Editor in AEM as a Cloud Service. After becoming the default for all Cloud Service Developer environments in November 2024, it will be set as default for all Stage environments on April 1, 2025, and for all Production environments on May 1, 2025. In all cases, users will still have the option to revert to the traditional Content Fragment Editor in AEM Touch UI.

**Translation HTTP API** 

The AEM Translation HTTP REST API that has been in early adopter mode for a while is now GA. Documentation can be found [here](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/translation/). The API allows automating required steps in the translation management process for content in AEM.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in AEM Assets {#new-features-assets}

**Dynamic Media new packaging structure**

A refreshed Dynamic Media packaging structure is now available to better align with market expectations and support tracking. The new packaging structure comprises:

* Dynamic Media Prime, which includes Dynamic Media with OpenAPIs and video to enhance delivery.

* Dynamic Media Ultimate adds delivery and transformation features to meet heavier usage requirements.

You must have Assets as a Cloud Service Prime or Ultimate to benefit from the new packaging structure.

**AI-generated video captions** 

AI-generated video captions in Adobe Dynamic Media use artificial intelligence to generate captions automatically for video content. This feature is designed to improve accessibility and enhance the user experience by providing accurate captions. Captions are generated from the original audio, any additional audio tracks, or extra captions are provided in the "Captions and Audio" tab on the video properties page. With support for more than 60 languages, captions can be reviewed and previewed before publishing the video.

**Customize search filters**

Custom Search filters enhance the precision and efficiency of finding relevant information. It allows for more tailored searches, filtering data according to specific attributes such as brand, product, category, or other key identifiers. This improves organization, reduces time spent sifting through irrelevant results, and enables quicker decision-making. It also supports scalability, as large datasets become easier to navigate and analyze.

![customize search filters](/help/assets/assets/custom-search-filters.png)


### Early Access features in Content Hub {#early-access-content-hub}

Content Hub now allows you to view and download Dynamic and Smart Crop renditions in addition to the existing static renditions. As a Content Hub administrator, you can also configure the availability of these renditions to users using the Configuration User Interface.

![dynamic renditions](/help/assets/assets/download-single-asset-renditions-dynamic.png)



## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}
 
### Early Access features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations, and help shape their development.

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### HTML Email Templates in Adaptive Forms

Adaptive Forms allows you to use [HTML email templates](/help/forms/html-email-templates-in-adaptive-forms.md). HTML email templates enable you to send rich, personalized, and visually appealing emails when a form is submitted. These emails can be customized with form data and enhanced using various email tags, such as images and links. With Adaptive Forms, you can either upload a file containing an HTML template or use a plain-text editor to create these templates.

![HTML email templates](/help/forms/assets/html-email.png)

#### Enhanced Cloud Storage Support: Direct PDF Upload to Azure Blob Storage

AEM Forms Document Generation APIs now allows you to [directly upload generated PDF documents](/help/forms/early-access-ea-features.md#doc-generation-api) to Azure Blob Storage. This enhancement streamlines storage and retrieval, improving efficiency and integration with cloud workflows.


## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Java 21 support {#java21}

As mentioned in the January release notes, you can now build code with Java 21, which includes new features (e.g., pattern matching for switch statements, sealed classes) and performance improvements; Java 17 builds are newly supported as well. For configuration steps, including updating your Maven project and library versions, see the [Build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#using-java-support) article.

The more performant Java 21 **runtime** will be automatically deployed when a Java 17 or 21 build is detected. However, we also recommend opting into the Java 21 runtime for environments built with Java 11, by emailing [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com). Learn about [Java 21 runtime requirements](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements).

>[!IMPORTANT] 
>
> In February, the Java 21 **runtime** was deployed to dev/RDE environments (aside from those already built with Java 17 or 21, which already have Java 21 runtime). Java 21 will be applied to stage/production environments in April. 

### Edge Computing - Request for Feedback! {#edge-computing-feedback}

Edge computing brings data processing closer to the browser, which has benefits including reduced latency. Adobe would like to hear if you find this technology useful for AEM Publish Delivery and Edge Delivery Services projects. Additionally, let us know what you envision using it for as input into the product roadmap. 

Some possible use cases:
* Authentication with an IdP to gate access to content
* Rendering dynamic (personalized, localized) content based on geolocation, device type, user attributes, etc.
* Advanced image manipulation 
* Middleware between the CDN and an origin
* A layer between the browser and a third-party API, perhaps to reformat the API response
* Aggregating data from multiple origins to make it easier for the client browser to render it

Email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with questions and comments!

### OpenAPI-based APIs - Early Adopter Program {#open-apis-earlyadopter}

Developers can deeply integrate AEM as Cloud Service features into their own applications and tools. New AEM as a Cloud Service APIs follow the OpenAPI specification, with a goal of being consistent, well-documented, and user-friendly. Credentials for endpoints requiring authentication are generated by creating Adobe Developer Console projects.

Learn more about [OpenAPI-based AEM APIs](/help/implementing/developing/open-api-based-apis.md) and try out an [end-to-end tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/invoke-openapi-based-aem-apis) illustrating configuration and usage.

Concretely, the API endpoints listed below are available as part of an early adopter program. If interested, email [aem-apis@adobe.com](mailto:aem-apis@adobe.com) describing how you intend to make use of them.

* [Sites Content Fragments APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/)
* [Assets APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/assets/author/)
* [Sites and Assets Folders APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/folders/)
* [Forms Communications APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/)

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
