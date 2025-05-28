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


The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2025.5.0) is June 5, 2025. The next feature release (2025.6.0) is planned for June 26, 2025.

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
* [Improved Scope Management for SharePoint Lists](/help/forms/connect-forms-to-sharepoint-list.md): SharePoint sites now support all managed paths, for example, /sites and /teams. This enhancement enables broader integration across various SharePoint site structures, offering greater flexibility in connecting to organizational content.
* [Support for Saving Document of Record to SharePoint List](/help/forms/generate-document-of-record-core-components.md#bind-adaptive-form-components-with-template-fields): Forms created using a SharePoint List–based Form Data Model (FDM) can now save the Document of Record (DoR) to SharePoint Lists by configuring the Document of Record Bind Reference field property. This enhancement enables seamless integration of supported form data and documents with SharePoint storage.

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

###  Updated Deprecation Process #{#updated-deprecation-process}

Adobe regularly reviews features, libraries, APIs, and configurations to ensure they meet standards for performance, security, and value. Occasionally, capabilities are marked for deprecation, and usage must stop by the specified removal date. Adobe communicates these deprecations by sending email notifications, pausing Cloud Manager builds (which you can resume after acknowledging the notice), and eventually failing those builds until references to deprecated items are removed. After the removal date, continued usage may result in delayed AEM upgrades, potentially impacting your environment’s security, performance, reliability, and availability.

Expand the list below see the list of deprecated APIs and OSGi configuration which must be removed within the next few weeks. The deprecation article (list) has more details, including the removal date.

<details>
  <summary>Expand to see the deprecations</summary>

Java APIs:
* `org.apache.sling.commons.auth`
* `org.apache.felix.webconsole`
* `org.eclipse.jetty`
* `com.mongodb`
* `org.apache.abdera`
* `org.apache.felix.http.whiteboard`
* `org.apache.cocoon.xml`
* `ch.qos.logback`
* `org.slf4j.spi`
* `org.slf4j.event`
* `org.apache.log4j`
* `com.google.common`
* `com.drew.*`
* `org.apache.jackrabbit.oak.plugins.blob`
* `org.apache.jackrabbit.oak.plugins.memory`

OSGi properties:

* `org.apache.sling.commons.log.LogManager` (all properties)
* `org.apache.sling.commons.log.LogManager.factory.config` (`org.apache.sling.commons.log.file`, `org.apache.sling.commons.log.pattern`)
 
</details>

### Java 11 Runtime Deprecation {#java11-runtime-deprecation}

The Java 11 runtime is now deprecated and most customers have been automatically upgraded to the more performant **Java 21 runtime**, for all their environments.

If your environment(s) could not be upgraded due to an unsupported dependency, Adobe has already reached out with an email and will again reach out with details specific to your scenario on how to resolve. All dependencies must be resolved by September 9th, 2025 so your environments can be safely upgraded to the Java 21 runtime.

Note that the Java 21 runtime is independent of whether your code is built with Java 21 (recommended) or with an earlier version. Building with Java 11 is still supported, but a deprecation will be announced in the future.

### Enforcement of AEM's Logging Configuration Policy {#logconfig-policy}

As detailed in April release notes, to ensure effective monitoring of customer environments, AEM Java logs must maintain a consistent format and must not be overridden by custom configurations. Log output must remain directed to the default files. For AEM product code, default log levels must be preserved. However, it is acceptable to adjust log levels for customer-developed code. See details in the [Logging article](/help/implementing/developing/introduction/logging.md#configuration-loggers).

AEM will enforce a policy in mid-June for most customers, where any custom modifications to these properties will be ignored. Adobe will send an email to customers who, based on our records, may be relying on custom modifications; for those customers, custom configuration will be ignored in September.

Please review and adjust your downstream processes accordingly. For example, if you use the log forwarding feature:
* If your logging destination expects a custom (non-default) log format, you may need to update your ingestion rules.
* If changes to log levels reduced log verbosity, be aware that the default log levels may result in a significant increase in log volume.

### Default for Version Purge and Audit Log Purge Maintenance Tasks {#mt-defaults}

In July 2025, newly created environments will have default values applied for Version Purge and Audit Log Purge Maintenance Tasks. See details in the [Maintenance Tasks article](/help/operations/maintenance.md#default). Work in progress...

### CDN configuraton for Edge Delivery Services (Beta) {#cdn-eds-beta}

The Adobe-Managed CDN offers flexible configuration options, as described in the [Config Pipeline article](/help/operations/config-pipeline.md#configurations). 

Now in a beta, deploy a config pipeline for features including CDN log forwarding, origin selectors, response and request transformations, and more. Please reach out to [aemcs-new-devconsole-ui-beta@adobe.com](mailto:aemcs-new-devconsole-ui-beta@adobe.com) with the details of your use case.

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
