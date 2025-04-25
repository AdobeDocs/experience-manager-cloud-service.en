---
title: Release Notes for 2025.3.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2025.3.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
feature: Release Information
role: Admin
---
# 2025.3.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2025.3.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2023 or 2024.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2025.3.0) is March 27, 2025. The next feature release (2025.4.0) is planned for April 24, 2025.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the February 2025 Release Overview video for a summary of the features added in the 2025.2.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3440920?quality=12)

-->

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Dynamic Media {#new-features-dynamic-media}

**Long form support for videos delivered using Dynamic Media with Open API**

Dynamic Media with OpenAPI now supports long form videos. The long form videos can support up to 50GB and 2 hours.

### Dynamic Media Classic {#dmc} 

<!-- CARRY OVER TO APRIL 2025 RELEASE NOTES -->

The Bandwidth tab in the Dynamic Media Classic reporting dashboard is no longer supported as of April 2025. 

See [Bandwidth and Storage, Types of reports](https://experienceleague.adobe.com/en/docs/dynamic-media-classic/using/setup/administration-setup#types-of-reports). 


## New features in Assets view {#new-features-assets-view}


**Support for root tags**

AEM Assets now supports mapping a tag property in a metadata form to custom metadata. In addition, as an administrator, you can restrict the availability of tags to users by restricting access to a specific root tag and the tags that exist under the root tag.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}
 
### Early Access features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations, and help shape their development.

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### HTML Email Templates in Adaptive Forms

Adaptive Forms allows you to use [HTML email templates](/help/forms/html-email-templates-in-adaptive-forms.md). HTML email templates enable you to send rich, personalized, and visually appealing emails when a form is submitted. These emails can be customized with form data and enhanced using various email tags, such as images and links. With Adaptive Forms, you can either upload a file containing an HTML template or use a plain-text editor to create these templates.

![HTML email templates](/help/forms/assets/html-email.png)

#### Enhanced Cloud Storage Support: Direct PDF Upload to Azure Blob Storage

AEM Forms Document Generation APIs now let you [directly upload generated PDF documents](/help/forms/early-access-ea-features.md#doc-generation-api) to Azure Blob Storage. This enhancement streamlines storage and retrieval, improving efficiency and integration with cloud workflows.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Java 21 support {#java21}

As of the January release, you can build code with Java 21 and Java 17. You gain access to new features like pattern matching, sealed classes, and various performance improvements. For configuration steps, including updating your Maven project and library versions, see the [Build Environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#using-java-support) article.

The more performant Java 21 **runtime** is automatically deployed when a Java 17 or 21 build is detected. However, Adobe also recommends opting into the Java 21 runtime for environments built with Java 11, by emailing [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com). Learn about [Java 21 runtime requirements](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements).

>[!IMPORTANT] 
>
> The Java 21 **runtime** was deployed to your dev/RDE environments in February; it will be applied to your stage/production environments on **April 28 and 29**. Note that **building code** with Java 21 (or Java 17) is independent of the Java 21 runtime -- you must explicitly take steps to build code with Java 21 (or Java 17).

### AEM Log-Forwarding to more destinations - Beta Program {#log-forwarding-earlyadopter}

Now in beta, you can forward AEM logs to New Relic (using HTTPS), Amazon S3, and Sumo Logic. Note that AEM logs (including Apache/Dispatcher) are supported, but not CDN logs. Email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) for access.

While logs can be downloaded from Cloud Manager, many organizations find it beneficial to stream those logs to a preferred logging destination. AEM already supports (GA) AEM and CDN log forwarding to Azure Blob Storage, Datadog, HTTPS, Elasticsearch (and OpenSearch), and Splunk. This feature is configured in a self-serve manner, and deployed using the Config Pipeline.

Learn more in the [log forwarding documentation](/help/implementing/developing/introduction/log-forwarding.md).

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

Learn more about [OpenAPI-based AEM APIs](/help/implementing/developing/open-api-based-apis.md) and try out an [end-to-end tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/openapis/invoke-api-using-oauth-s2s) illustrating configuration and usage.

Concretely, the API endpoints listed below are available as part of an early adopter program. If interested, email [aem-apis@adobe.com](mailto:aem-apis@adobe.com) describing how you intend to make use of them.

* [Sites Content Fragments APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/)
* [Assets APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/assets/author/)
* [Sites and Assets Folders APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/folders/)
* [Forms Communications APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/)

### New AEM Developer Console (Public Beta) {#aem-developer-console-beta}

Try out a revamped [AEM Developer Console](/help/implementing/developing/introduction/aem-developer-console.md), which offers a more interactive experience for debugging code in Cloud environments.

Anyone can access the public beta by clicking the *New Console Available* button in the current AEM Developer Console. Adobe welcomes feedback, which you can email to [aemcs-new-devconsole-ui-beta@adobe.com](mailto:aemcs-new-devconsole-ui-beta@adobe.com)

## [!DNL Experience Manager] Guides {#guides}

You can find a complete list of new and enhanced features of the latest release of Adobe Experience Manager Guides [here](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/release-notes/cloud-release-notes/2025-releases/2502-release/whats-new-2025-02-0).

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
