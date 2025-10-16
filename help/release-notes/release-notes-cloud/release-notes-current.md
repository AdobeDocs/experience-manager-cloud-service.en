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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2025.9.0) is September 25, 2025. The next feature release (2025.10.0) is planned for October 30, 2025.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the July 2025 Release Overview video for a summary of the features added in the 2025.7.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3440920?quality=12)

-->

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in Experience Manager Sites Prerelease {#prerelease-sites}

The Content Model Editor for AEM Content Fragments has been modernized to align with other React Spectrum–based interfaces in AEM. Its user interface implementation and extensibility model are now consistent with the Content Fragment Editor and Universal Editor. The new Model Editor is now default when opened from the new Content Model Admin UI. Opening a content model in Touch UI opens the Touch UI editor and offers to try out the new editor. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New Features in Assets view {#new-features-assets-view}

**Enhanced Text Formatting with Substrings in Dynamic Media Templates**

You can now apply formatting to substrings within Dynamic Media template text layers. A selected word or phrase is treated as a separate layer, allowing you to adjust its font, font size, color, and more. The substring layer is parameterized so you can update it in real-time using the template's delivery URL

### New Features in Dynamic Media with OpenAPI capabilities {#new-features-dynamic-media-with-openapi}

**Branded and Readable Asset Delivery URLs**

Make Dynamic Media with OpenAPI URLs more human-readable by leveraging Vanity URLs in Dynamic Media with OpenAPI. Vanity URLs allow replacing long, system-generated, hard to memorize UUIDs in asset delivery URLs with short, brand-controlled identifiers. This makes Vanity URLs shorter, easier to read and share, and allow for better alignment with your brand or campaigns. Vanity URLs resolve automatically to the original asset UUID at runtime without disrupting existing workflows.

>[!NOTE]
>
>This feature is available as a Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

<!--

### New Features in Content Hub {#new-features-content-hub}

**Mark Collections as Favourites**

You can now mark collections as Favorites in Content Hub, making it easier to organize and retrieve them. Once added, your favourite collections are conveniently available from the **Favourites** tab on the Content Hub home page.

**Pin collections for quick access**

Content Hub Administrators can now pin collections in Content Hub for quick access. Pinned collections are displayed in a dedicated **Pinned** section on the Collections home page, making it easier to keep important collections within reach.

>[!NOTE]
>
>These features are available as Limited Availability features. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

-->

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in Experience Manager Forms {#new-features-forms}

**Invoke Form Data Model Workflow Step for SharePoint List Attachments**

The Invoke Form Data Model workflow step now supports handling workflow-side metadata for Base64-encoded attachment arrays in SharePoint List–based Form Data Models. With this enhancement, the workflow step can pass, store, and retrieve metadata such as file name, MIME type, and custom properties for each attachment. This capability enables more comprehensive data management and facilitates seamless downstream integration. For details, see [Enhanced support in Invoke Form Data Model workflow step for SharePoint List attachments](/help/forms/aem-forms-workflow-step-reference.md#invoke-form-data-model-fdm-service-step).
 
### Pre-Release features in AEM Forms 

**Rule Editor Enhancements**

The Rule Editor now supports enhanced navigation and allows use of function and mathematical expressions in input parameters.

**Enhanced Navigation with Event Payload Support**
 
The `Navigate To` action in the Invoke Service handlers now supports `EVENT_PAYLOAD`, enabling form authors to configure follow-up actions based on event responses. This enhancement offers greater flexibility in designing post-submission workflows, ensuring smoother transitions and more personalized user experiences. For more information, see [Enhanced Navigation with Event Payload Support](/help/forms/invoke-service-enhancements-rule-editor.md#use-case-5-use-event-payload-in-navigate-to-action-in-invoke-service).

**Function and Mathematical Expression Support in Input Parameters**
 
Input parameters now support both function calls and mathematical expressions, enabling form authors to pass dynamically computed values directly. This enhancement streamlines rule configurations, eliminates the need for extra fields, and makes forms more adaptable to complex logic and calculation-driven scenarios. For more information, see [Function and Mathematical Expression Support in Input Parameters](/help/forms/rule-editor-core-components-user-interface.md#function-and-mathematical-expression-support-in-input-parameters).

### New Early Access Features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program offers a unique opportunity for you to get exclusive access to cutting-edge innovations and help shape their development.

These release notes list the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

**PDF Preview in Interactive Communication Editor**

Users can preview Interactive Communications PDFs without data, with local JSON data files, or with data from a data model, enabling flexible data-driven testing. For more information, see [PDF Preview in Interactive Communication Editor](/help/forms/interactive-communication/pdf-preview-in-interactive-communication-editor-with-different-data-options.md).

**Support of Custom Fonts in Interactive Communication**

The Custom Fonts feature allows users to embed custom or organization-approved fonts in the Interactive Communications, ensuring consistent and branded PDF rendering across devices and platforms. For more information, see [Support of Custom Fonts in Interactive Communication](/help/forms/interactive-communication/add-custom-fonts-to-interactive-communication-editor.md).

**Import and Export Interactive Communications**

This feature enables migration and reuse of Interactive Communications across different environments. You can now export an Interactive Communication along with its associated fragments and data models from one environment and import it into another. For more information, see [Import and Export Interactive Communications](/help/forms/interactive-communication/import-and-export-interactive-communications.md).

<!--
**Forms Optimization opportunities**

Forms Optimization uses AI to analyze your forms and suggest improvements for better performance. It highlights forms with low engagement, flags accessibility issues, and generates AI-powered variations to help increase conversion rates and compliance with WCAG standards.

>[!VIDEO](https://video.tv.adobe.com/v/3469472/) 

Key optimization opportunities include:

* Increasing visibility for forms with low views
* Improving completion rates for forms with low conversions
* Addressing accessibility compliance issues
* Streamlining navigation to enhance user experience

With Forms Optimization, you get automated, data-driven recommendations and variations, making it easier to boost engagement and ensure your forms are effective and inclusive. 
--> 
  
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### New Features in Release Management {#new-features-release-management}

**Pause Automatic Maintenance Updates**

Go‑live days, live events, peak sales—these moments can't break. [Our new self‑service features](/help/implementing/deploying/quiet-hours-update-free-periods.md) stop automatic mainteanance updates when it matters, so your teams stay focused.

* Quiet Hours: Block automatic maintenance during set times each day. Ideal for working hours, nightly runs or morning cutovers.
* Update‑Free Period: Block automatic maintenance for a full week. Use it for launches, promos, or yearly freezes.

>[!NOTE]
>
>Available as a Limited Availability feature on September 25th.
>Email [aemcs-update-free@adobe.com](mailto:aemcs-update-free@adobe.com) to get it activated on your programs.

### New Release of AEM Developer Tools for Eclipse {#aem-develeper-tools-for-eclipse}

Version 1.4.0 of the AEM Developer Tools for Eclipse has been released. This version adds support for Eclipse IDE 2022-12 or newer and has been validated with the current version (2025-09). The tooling now works with modern versions of the AEM Project Archetype and incorporates improvements from the Sling IDE Tooling 1.3.0.

Install from the [Eclipse Marketplace](https://marketplace.eclipse.org/content/aem-developer-tools-eclipse) and see the [AEM Developer Tools page](https://eclipse.adobe.com) for more details.

### Upcoming Java API Deprecations {#java-api-deprecation}

Several deprecated APIs were marked for removal on August 31st and thus should no longer be referenced. You will receive Actions Center notifications if deprecated API usage is detected in your code, and after Nov 13th, notices will appear during Cloud Manager builds to reinforce the importance of removing usage. See the [deprecation article](/help/release-notes/deprecated-removed-features.md#aem-apis) for full details, but for convenience, these APIs are listed below:

+++ Expand to see the Java API deprecations

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

+++

<!--
OSGi properties:

* `org.apache.sling.commons.log.LogManager` (all properties)
* `org.apache.sling.commons.log.LogManager.factory.config` (`org.apache.sling.commons.log.file`, `org.apache.sling.commons.log.pattern`)
* 

-->

### Java 11 Runtime Deprecation {#java11-runtime-deprecation}

The *Java 11 runtime* is deprecated, and most environments have already been upgraded to the higher-performance **Java 21 runtime**.

If your environment could not be upgraded due to unsupported dependencies (see the [Java 21 runtime requirements](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements)), you should have received an email from Adobe with next steps. As described there, Adobe upgraded your **Dev** and **RDE** environments on **September 18, 2025** so you can validate your site and processes and address any issues. Upgrades for **Stage** and **Production** will proceed on **October 14, 2025**.

>[!NOTE]
>
>The runtime version is separate from your code's build version. While we recommend building with Java 21, Java 11 builds are still accepted for now. A separate deprecation notice for Java 11 builds will be shared in the future.

### Enforcement of AEM Java Logs Configuration Policy {#logconfig-policy}

As noted in the April release notes, AEM Java logs must follow a standard format to ensure reliable monitoring across all customer environments. Custom log configurations—such as changes to log formatting, output files, or default log levels—are no longer supported. Logs must remain directed to the default files, and default log levels for AEM product code must be preserved. See full details in the [Logging article](/help/implementing/developing/introduction/logging.md#configuration-loggers).

Starting on **October 30th**, any unsupported custom logging overrides will be ignored. Based on our analysis, most customers will not be impacted and Adobe has contacted customers whose current configuration may be affected.

Please review and update any downstream processes that rely on custom logging behavior. For example:

* If your log forwarding system expects a custom log format, you may need to adjust your ingestion rules.
* If you've previously reduced log verbosity by changing log levels, please note that reverting to default levels may increase log volume.

### Edge Computing (Beta Program) {#edge-computing}

Edge computing allows you to execute JavaScript at the CDN layer, bringing data processing closer to the end user. This reduces latency and enables responsive, dynamic experiences at the edge.

Common use cases include:

* Personalizing content based on geolocation, device type, or user attributes
* Acting as middleware between the CDN and your origin
* Reformatting responses from third-party APIs (and perhaps aggregating multiple API responses) before delivering them to the browser
* Composing and serving server-rendered HTML at the edge using content stitched from various backends
* Exposing an MCP server for LLMs like ChatGPT and Claude to access custom tools

We have a limited number of opportunities available for either AEM Publish Delivery or Edge Delivery Services projects for live production sites. If you're interested in participating or want to learn more, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case.

### Edge Authentication for Edge Delivery Services (Beta Program) {#edge-authentication}

Edge Authentication lets you restrict access to Edge Delivery Services pages to only those who have authenticated with your identity provider (IdP). This is achieved by deploying an OpenID Connect (OIDC) configuration YAML file.

If interested, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case and any questions you may have.

<!--
### CDN Configuration for Edge Delivery Services (Beta Program) {#cdn-eds-beta}

The Adobe-Managed CDN offers flexible configuration options, as described in the [Config Pipeline article](/help/operations/config-pipeline.md#configurations). 

Now in beta, youcan deploy a config pipeline for features including CDN origin selectors, response and request transformations, CDN log forwarding and more. Please reach out to [aemcs-cdn-config-adopter@adobe.com](mailto:aemcs-cdn-config-adopter@adobe.com) with the details of your use case.

-->

### Canary Production Deployments to Test Code Before Accepting Live Traffic (Beta Program) {#canary-beta}

Validate a production build with internal-only test traffic before exposing it to end users. Ship to production, route only canary traffic (using a special header), monitor behavior, then either promote to live traffic or roll back—without impacting customers.

Deploy your code releases to production, but restrict it to only internal test traffic before deciding whether to accept live traffic versus rolling back. 

Email [aemcs-canary-deployments-beta@adobe.com](mailto:aemcs-canary-deployments-beta@adobe.com) to request access and share feedback.

### Snapshots for RDEs (Alpha Program) {#rde-snapshot-program}

In alpha, Rapid Development Environments (RDEs) now support a feature to take a snapshot of the current state of code and content, which can be restored at a later time. This can be useful when syncing code that may need to be reverted, or when switching between development of different features. It's also possible to restore just the mutable content as a known starting point for testing.

Please email [aemcs-rde-support@adobe.com](mailto:aemcs-rde-support@adobe.com) if there's interest in providing feedback on this feature.

### AEM Log-Forwarding to More Destinations (Beta Program) {#log-forwarding-beta}

While logs can be downloaded from Cloud Manager, many organizations find it beneficial to stream those logs to a preferred logging destination. AEM already supports AEM and CDN log forwarding to Azure Blob Storage, Datadog, HTTPS, Elasticsearch (and OpenSearch), and Splunk. This feature is configured in a self-serve manner, and deployed using the Config Pipeline.

Now in beta, you can forward AEM logs to Amazon S3, Sumo Logic, Dynatrace, and your own New Relic account (not the Adobe-provided account). Note that AEM logs (including Apache/Dispatcher) are supported for these logging destinations, but not CDN logs. Email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) for access.

Learn more in the [log forwarding documentation](/help/implementing/developing/introduction/log-forwarding.md).

### Expanded Application Performance Monitoring (APM) (Alpha program) {#apm-alpha}

For observability, AEM Cloud Service currently supports Adobe-provided [New Relic One](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/user-access-new-relic) and customer-managed [Dynatrace](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/dynatrace). As we explore support for additional APM options, please email us at [aemcs-apm-beta@adobe.com](mailto:aemcs-apm-beta@adobe.com) with your preferred vendor or technology, along with use cases.


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
