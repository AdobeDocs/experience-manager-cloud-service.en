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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2025.4.0) is April 24, 2025. The next feature release (2025.5.0) is planned for June 5, 2025.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the February 2025 Release Overview video for a summary of the features added in the 2025.2.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3440920?quality=12)

-->

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in Experience Manager Sites {#enhancements-sites}

**New Content Fragment Model Admin UI**

Further completing the list of new client-side user interfaces when working with AEM Content Fragments, a new admin UI is now available for content fragment models. The new UI provides a clean and modern list view that allows searching models with filters, and that shows model tags and which content fragments exist that are based on a certain model. Documentation can be found [here](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md). 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### Dynamic Media (Scene7) {#dynamic-media-scene7}

**Dynamic Media (Scene7) not supported in Enhanced Security environments**

Dynamic Media (Scene7) on AEM as a Cloud Service is not HIPAA-ready and cannot be used in AEM environments where Enhanced Security is enabled.

Starting with the April 2025 AEM as a Cloud Service release, a technical restriction prevents Dynamic Media (Scene7) from being configured in environments with Enhanced Security. As a result, the **Dynamic Media Configuration** card under **Tools** > **Cloud Services** is no longer visible in these environments.

Additionally, customers using AEM 6.5 should be aware that the Dynamic Media (Scene7) stack is not HIPAA-ready.

### Dynamic Media Classic {#dynamic-media-classic}

**Reporting**

The Bandwidth tab in the Dynamic Media Classic reporting dashboard is no longer supported as of April 2025. 

See [Bandwidth and Storage, Types of reports](https://experienceleague.adobe.com/en/docs/dynamic-media-classic/using/setup/administration-setup#types-of-reports). 


## New features in Assets View {#new-features-assets-view}

**Asset relations**

The Assets View now supports viewing and editing asset relations in a simplified asset Details panel. Easily add relationships like Source and Derivative to content so that users can more effectively find relevant hero content.

![Assets relation example](/help/assets/assets/asset-relations-example.png)

**Compare versions of an asset**

You can now quickly select and compare any version of an asset with its latest version using the Assets view.

![compare versions of asset](/help/assets/assets/version-compare2.png)

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### Pre-release Features 

* [Universal Editor - Form Fragments](/help/edge/docs/forms/universal-editor/creating-form-fragments.md): The Universal Editor now allows you to create and reuse Form Fragments for Adaptive Forms. These fragments are reusable form sections (e.g., contact details, consent fields) that can be built once and applied across multiple forms. This feature streamlines form creation, ensures consistency, and improves authoring efficiency.
 
* [SharePoint Document Library - Save Attachments with Original Filenames](/help/forms/connect-forms-to-sharepoint-document-library.md#connect-an-adaptive-form-to-microsoft-sharepoint-document-library): You now have the option to save form attachments using their original filenames when storing them in a SharePoint Document Library. This enhancement simplifies the identification and management of uploaded files.

* **Rule Editor**:
    * [Binary Condition with Click Event in "When" Clause](/help/forms/rule-editor-core-components-events-operators.md#available-operator-types-and-events-in-rule-editor): The Rule Editor now allows combining a button click event (_Is Clicked_) with other conditions within the "When" clause. This enables more precise control over rule execution based on user interaction and other factors. Note: When using multiple conditions, the click event must be the first condition listed.
    * [Validation Conditions for Fields and Panels](/help/forms/rule-editor-core-components-usecases.md): The Rule Editor now includes _IsValid_ and _IsNotValid_ conditions. These allow you to check the validation status of specific fields or entire panels (including layouts like Horizontal Tabs, Vertical Tabs, Accordions, and Wizards), facilitating improved form navigation and user experience based on validation results.
* **Improved Scope Management for SharePoint Lists**: SharePoint sites now support all managed paths, for example, /sites and /teams. This enhancement enables broader integration across various SharePoint site structures, offering greater flexibility in connecting to organizational content.
* **Support for Saving Document of Record to SharePoint List**: Forms created using a SharePoint List–based Form Data Model (FDM) can now save the Document of Record (DoR) to SharePoint Lists by configuring the Document of Record Bind Reference field property. This enhancement enables seamless integration of supported form data and documents with SharePoint storage.

### Early Access Features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations, and help shape their development.

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### Adobe Experience Platform (AEP) Integration with Forms

Integration capabilities between Forms and AEP are now available for early adopters.

## CIF Add-on {#cloud-services-cif}

### Enhancements {#enhancements-cif}

* Adding product variant selection for CIF product reference data type
* [Experimental]: JSON+LD in CIF Core Components in PDPs
* [Experimental]: CIF ability to clear cache

### Bug fixes {#bug-fixes-cif}

* Fix search issue in product field
* Product url format not working as expected for #variant_sku
* Unable to Add More Than 20 SKUs to Product List Component

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### OpenAPI-based APIs {#open-apis}

Developers can deeply integrate AEM as Cloud Service features into their own applications and tools. New AEM as a Cloud Service APIs follow the OpenAPI specification, with a goal of being consistent, well-documented, and user-friendly. Credentials for endpoints requiring authentication are generated by creating Adobe Developer Console projects and support OAuth Server-to-Server, Web App, and Single Page App (SPA).

[See the full list](https://developer.adobe.com/experience-cloud/experience-manager-apis/#openapi-based-apis) of OpenAPI-based APIs, [learn more](/help/implementing/developing/open-api-based-apis.md), and try out an [end-to-end tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/openapis/invoke-api-using-oauth-s2s) illustrating configuration and usage.

Watch this video to learn how to configure an authenticated API for later usage:

>[!VIDEO](https://video.tv.adobe.com/v/3457510?quality=12&learn=on)

### CDN Configuration-related Enhancements {#cdn-enhancements}

The Adobe-Managed CDN offers flexible configuration options, as described in the [Config Pipeline article](/help/operations/config-pipeline.md#configurations). Here are a few recent features:

#### Include Additional Properties in CDN Logs {#props-in-cdnlogs}

Useful for scenarios including debugging and data analysis, you can include more information in your CDN logs beyond the default properties by setting the `logProperty` action in [request and response transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#request-transformations).

#### Region, Continent, and Organization Properties as Matching Conditions {#matching-conditions}

CDN rules can now match based on region, continent, and organization for use cases including blocking traffic and redirects. `clientRegion` and `clientContinent` augment the already-supported `clientCountry` to match based on geography, while `clientAsName` and `clientAsNumber` match Autonomous Systems to identify large ISPs, companies, or cloud providers. Learn more about these [newly exposed request properties](/help/security/traffic-filter-rules-including-waf.md#condition-structure).

#### Set Cookie Value {#cookie-attributes}

You can set cookie attributes in [response tranformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#response-transformations).

### Java 21 Support {#java21}

As of the January release, you can build code with Java 21 and Java 17. You gain access to new features like pattern matching, sealed classes, and various performance improvements. For configuration steps, including updating your Maven project and library versions, see the [Build Environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#using-java-support) article.

The more performant Java 21 **runtime** is automatically deployed when a Java 17 or 21 build is detected. However, Adobe also recommends opting into the Java 21 runtime for environments built with Java 11, by emailing [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com). Learn about [Java 21 runtime requirements](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements).

>[!IMPORTANT] 
>
> The Java 21 **runtime** was deployed to your dev/RDE environments in February; it will be applied to your stage/production environments on **April 28 and 29**. Note that **building code** with Java 21 (or Java 17) is independent of the Java 21 runtime -- you must explicitly take steps to build code with Java 21 (or Java 17).

### Enforcement of AEM's Logging Configuration Policy {#logconfig-policy}

To ensure effective monitoring of customer environments, AEM Java logs must maintain a consistent format and should not be overridden by custom configurations. Log output must remain directed to the default files. For AEM product code, default log levels must be preserved. However, it is acceptable to adjust log levels for customer-developed code.

To that end, changes should not be made to the following OSGi properties:
* **Apache Sling Log Configuration** (PID: `org.apache.sling.commons.log.LogManager`) — *all properties*
* **Apache Sling Logging Logger Configuration** (Factory PID: `org.apache.sling.commons.log.LogManager.factory.config`):
  * `org.apache.sling.commons.log.file`
  * `org.apache.sling.commons.log.pattern`

In mid-May, AEM will enforce a policy where any custom modifications to these properties will be ignored. Please review and adjust your downstream processes accordingly. For example, if you use the log forwarding feature:
* If your logging destination expects a custom (non-default) log format, you may need to update your ingestion rules.
* If changes to log levels reduced log verbosity, be aware that the default log levels may result in a significant increase in log volume.

### AEM Log-Forwarding to More Destinations - Beta Program {#log-forwarding-earlyadopter}

Now in beta, you can forward AEM logs to New Relic (using HTTPS), Amazon S3, and Sumo Logic. Note that AEM logs (including Apache/Dispatcher) are supported, but not CDN logs. Email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) for access.

While logs can be downloaded from Cloud Manager, many organizations find it beneficial to stream those logs to a preferred logging destination. AEM already supports (GA) AEM and CDN log forwarding to Azure Blob Storage, Datadog, HTTPS, Elasticsearch (and OpenSearch), and Splunk. This feature is configured in a self-serve manner, and deployed using the Config Pipeline.

Learn more in the [log forwarding documentation](/help/implementing/developing/introduction/log-forwarding.md).

### Edge Computing - Request for Feedback! {#edge-computing-feedback}

Edge computing brings data processing closer to the browser, which has benefits including reduced latency. Adobe would like to hear if you find this technology useful for AEM Publish Delivery and Edge Delivery Services projects. Additionally, let us know what you envision using it for as input into the product roadmap. 

Some possible use cases:

* Authentication with an IdP to gate access to content
* Personalization by rendering dynamic content based on geolocation, device type, user attributes, etc.
* Advanced image manipulation 
* Middleware between the CDN and an origin
* A layer between the browser and a third-party API, perhaps to reformat the API response
* Aggregating data from multiple origins to make it easier for the client browser to render it

Email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with questions and comments!

## [!DNL Experience Manager] Guides {#guides}

You can find a complete list of new and enhanced features of the latest release of Adobe Experience Manager Guides [here](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap).

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
