---
title: Release Notes for 2025.5.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2025.5.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
feature: Release Information
role: Admin
---
# 2025.5.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2025.5.0 version of [!DNL Experience Manager] as a Cloud Service.

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

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

**AI-Generated metadata**

AEM Assets now uses [AI to automatically generate metadata, including Title, Description, and Keywords](/help/assets/metadata-assets-view.md#ai-smart-tags). These AI-generated fields enhance metadata accuracy, making the assets easier to search, categorize, and recommend. This approach not only improves efficiency by eliminating manual tagging but also ensures consistency and scalability across large volumes of digital content.

![AI generated metadata](/help/assets/assets/enhanced-smart-tags.png)

**Integration with Figma**

AEM Assets integrates natively with Figma, which allows designers to directly access the assets stored in AEM Assets from within the Figma User Interface. You can place content managed in AEM Assets in the Figma canvas and then save new or edited content in AEM Assets repository.

![Integration with Figma](/help/assets/assets/figma-integration.png)


### New Features in Content Hub {#new-features-content-hub}

**Attribute-based Access Control (ABAC)**

Content Hub now allows you to apply rule-based restrictions to access assets. Asset permissions ensure governance and also makes sure that only the relevant assets are accessible to users.

The asset restriction rules are based on metadata and if the conditions defined in the rule match the asset metadata, the asset gets displayed to the user groups.

Some of the key benefits of Attribute-based Access Control include:

* Eliminates the dependency on folder structure for permissions

* Allows administrators to upload assets and retroactively determine permission structures

* Reduces number of duplicates - improves asset integrity. Duplicates are needed in folder based permissions when same assets are shared with different groups.

**UI Branding**

Content Hub now allows administrators to customize the user interface with brand-specific elements, including banner images, banner titles and body text, as well as primary and secondary colors. These enhancements help ensure brand consistency, simplify user onboarding, and build trust.

![UI Branding](/help/assets/assets/content-hub-ui-branding.png)

**Public link sharing**

Content Hub now supports generating shareable links to allow external users, without application access, to view asset metadata or download assets.

![UI Branding](/help/assets/assets/public-and-private-link.png)

**Collections governance**

Content Hub now lets you control access to collections during creation, ensuring only authorized users can view or manage grouped assets. It ensures improved security, better collaboration, organized asset management, and simplified governance.

![Collections governance](/help/assets/assets/collection-permissions.png)

>[!NOTE]
>
>Collections governance is a limited availability feature. You can get it enabled  by creating a support ticket.

**Download multiple assets as a ZIP**

Content Hub now also allows you to download the selected assets and their renditions in a ZIP file and not as separate files simplifying file management for you.

**Dynamic Media renditions in Content Hub**

Access all your Dynamic Media preset renditions and smart-crops for download, directly from within the Content Hub User Interface.

​![Dynamic Media renditions](/help/assets/assets/dm-renditions-content-hub.png)

### New Features in Dynamic Media {#new-features-dynamic-media}

**Dynamic Media native integration with AJO B2C​**

Native integration of Experience Manager (AEM) Dynamic Media with Journey Optimizer (AJO) B2C, enabling marketers to easily embed AEM Dynamic Media assets (rendition and DM Template) into AJO content and deliver real-time updates and hyper-personalized experiences across channels.

​![Dynamic Media renditions](/help/assets/assets/dm-ajo-integration.png)

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

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

###  Updated Deprecation Process {#updated-deprecation-process}

Adobe regularly reviews features, libraries, APIs, and configurations to ensure they meet standards for performance, security, and value. When capabilities no longer meet these standards, they are marked for deprecation and usage must stop by a specified removal date. Leading up to this date, Adobe will remind customers with email notifications, and actions that need to be taken in Cloud Manager before proceeding with or deploying new builds. Failure to take the necessary action may result in an inability to upgrade to new versions of AEM leading to potential impacts around security, performance, reliability, and availability.

See the [deprecation article](/help/release-notes/deprecated-removed-features.md) for further information.

#### Deprecated Java APIs and OSGi configuration nearing removal dates {#deprecated-near-removals}

Expand the list below to view the deprecated APIs and OSGi configurations that must no longer be used. For full details—including removal timelines—refer to the deprecation article.

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
* `com.drew`
* `org.bson`
* `org.apache.jackrabbit.oak.plugins.blob`
* `org.apache.jackrabbit.oak.plugins.memory`

OSGi properties:

* `org.apache.sling.commons.log.LogManager` (all properties)
* `org.apache.sling.commons.log.LogManager.factory.config` (`org.apache.sling.commons.log.file`, `org.apache.sling.commons.log.pattern`)
 
</details>

### Java 11 Runtime Deprecation {#java11-runtime-deprecation}

The **Java 11 runtime** is now deprecated, and most environments have already been upgraded to the more performant **Java 21 runtime**.

If your environment couldn't be upgraded due to unsupported dependencies (see [Java 21 runtime requirements](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements)), you should have received an email from Adobe with specific next steps. Please ensure all required updates are completed by **August 28, 2025**, so your environment can be upgraded without disruption.

Note: The runtime version is separate from your code's build version. While we recommend building with Java 21, Java 11 builds are still supported for now. A separate deprecation notice for Java 11 builds will be shared in the future.

### Enforcement of AEM Java Logs Configuration Policy {#logconfig-policy}

As noted in the April release notes, AEM Java logs must follow a standard format to ensure reliable monitoring across all customer environments. Custom log configurations—such as changes to log formatting, output files, or default log levels—are no longer supported. Logs must remain directed to the default files, and default log levels for AEM product code must be preserved. See full details in the [Logging article](/help/implementing/developing/introduction/logging.md#configuration-loggers).

Starting in **late August**, any unsupported custom logging overrides will be ignored. Based on our analysis, most customers will not be impacted and Adobe will directly contact any customers whose current configuration may be affected.

Please review and update any downstream processes that rely on custom logging behavior. For example:

* If your log forwarding system expects a custom log format, you may need to adjust your ingestion rules.
* If you've previously reduced log verbosity by changing log levels, please note that reverting to default levels may increase log volume.

### Default Purging of Older Versions and Audit Logs {#mt-defaults}

Currently, content versions and audit logs have their associated *purge maintenance tasks* disabled by default and thus no data is removed unless explicitly configured via their respective OSGi properties. 

However, to optimize repository performance, starting in **late June 2025**, purging will be enabled by default, following these guidelines:

#### Content Versions {#mt-content}

* **New environments** (created after an upcoming date (to be communicated later)
  * Versions older than **30 days** will periodically be deleted.
  * The most recent five versions within the last 30 days are retained, along with the most recent version and the current version, regardless of their age.

* **Existing environments** (created before this upcoming date):
  * Versions older than **7 years** will periodically be deleted.
  * All versions within the past 7 years are retained.
  * This high default threshold prevents unintended removal of recent data. However, it is recommended to configure lower values to optimize repository performance.

* You may modify these defaults through OSGi configuration overrides.

#### Audit Log {#mt-auditlogs}

* **New environments** (created after an upcoming date, which will be communicated separately):
  * Replication, DAM, and page audit logs older than **7 days** will periodically be deleted.
  * All events are logged by default.

* **Existing environments** (created before this upcoming date):
  * Replication, DAM, and page audit logs older than **7 years** will periodically be deleted.
  * All events are logged by default.
  * This high default threshold prevents unintended removal of recent data. However, it is recommended to configure lower values to optimize repository performance.

* You may modify these defaults through OSGi configuration overrides.

For more details, see the [Maintenance Tasks article](/help/operations/maintenance.md#defaults).

### Edge Computing (Alpha Program) {#edge-computing}

Edge computing allows you to execute JavaScript at the CDN layer, bringing data processing closer to the end user. This reduces latency and enables responsive, dynamic experiences at the edge.

Common use cases include:

* Authenticating users with an identity provider before granting access to content
* Personalizing content based on geolocation, device type, or user attributes
* Acting as middleware between the CDN and your origin
* Reformatting responses from third-party APIs (and perhaps aggegating multiple APIs responses) before delivering them to the browser
* Composing and serving server-rendered HTML at the edge using content stitched from various backends

We have a limited number of opportunities available for either AEM Publish Delivery or Edge Delivery Services projects for live production sites. If you're interested in participating or want to learn more, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case.

### CDN Configuration for Edge Delivery Services (Beta Program) {#cdn-eds-beta}

The Adobe-Managed CDN offers flexible configuration options, as described in the [Config Pipeline article](/help/operations/config-pipeline.md#configurations). 

Now in a beta, deploy a config pipeline for features including CDN origin selectors, response and request transformations, and more. Please reach out to [aemcs-cdn-config-adopter@adobe.com](mailto:aemcs-cdn-config-adopter@adobe.com) with the details of your use case.

### AEM Log-Forwarding to More Destinations (Beta Program) {#log-forwarding-beta}

While logs can be downloaded from Cloud Manager, many organizations find it beneficial to stream those logs to a preferred logging destination. AEM already supports AEM and CDN log forwarding to Azure Blob Storage, Datadog, HTTPS, Elasticsearch (and OpenSearch), and Splunk. This feature is configured in a self-serve manner, and deployed using the Config Pipeline.

Now in beta, you can forward AEM logs to Amazon S3, Sumo Logic, and your own New Relic account (not the Adobe-provided account). Note that AEM logs (including Apache/Dispatcher) are supported for these logging destinations, but not CDN logs. Email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) for access.

Learn more in the [log forwarding documentation](/help/implementing/developing/introduction/log-forwarding.md).

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
