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

### New features in Experience Manager Sites {#enhancements-sites}

The Content Model Editor for AEM Content Fragments has been modernized to align with other React Spectrum–based interfaces in AEM. Its user interface implementation and extensibility model are now consistent with the Content Fragment Editor and Universal Editor. The new Model Editor is now default when opened from the new Content Model Admin UI. Opening a content model in Touch UI opens the Touch UI editor and offers to try out the new editor. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New Features in Assets view {#new-features-assets-view}

**Enhanced Text Formatting with Substrings in Dynamic Media Templates**

You can now apply formatting to substrings within Dynamic Media template text layers. A selected word or phrase is treated as a separate layer, allowing you to adjust its font, font size, color, and more. The substring layer is parameterized so you can update it in real-time using the template's delivery URL

### New Features in Dynamic Media with OpenAPI capabilities {#new-features-dynamic-media-with-openapi}

**SEO friendly DM with OpenAPI URLs**

Create Vanity URLs for asset delivery in DM with OpenAPI, replacing long system-generated UUIDs with short, readable identifiers. This makes links SEO friendly and better aligned with your brand or campaigns. Vanity URLs resolve automatically to the original asset UUID at runtime without disrupting existing workflows.

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

**Date & Time Input Component**

A [Date & Time component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/date-time-component) is now available, enabling users to select both date and time using a calendar and clock interface, or by manually entering values in a supported format.

**Enhanced Error Handling for File Uploads**

The [File Attachment component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/file-attachment#basic-tab) now automatically validates the uploaded file type against the allowed list. If a user uploads a file in an unsupported format, the form displays an error during submission. The component also checks the file content to validate its type, enhancing the overall security of the form.

**Specified Error Response for Custom Submit Action**

When a [custom submit action](/help/forms/custom-submit-action-troubleshooting.md) encounters an unhandled error, the system returns error code 502. This helps identify that the issue is related to the custom submit action, making debugging easier.

**Excluding Hidden Fields from Document of Record**

A new property allows exclusion of hidden fields from the [Document of Record](/help/forms/generate-document-of-record-core-components.md#document-of-record-settings). By default, this option is not selected and applies to all form fields.

  
### Pre-Release features in AEM Forms 

**Generate and Sync AFP Renditions**

You can now use the [AEM Forms Communication API](/help/forms/document-generation-afp-api.md) to convert an XDP file to AFP format. AFP is a high-performance format widely used in large-scale enterprise printing.

**Enhancements in Rule Editor**

* [Validate Method in Function List](/help/forms/rule-editor-enhancements-use-cases.md#validate-method-in-function-list): The validate and reset methods now support execution at the panel, field, and form levels. Previously, they were only supported at the form level.
* [Modern JavaScript Support](/help/forms/rule-editor-core-components-difference-tables.md): Support for ECMAScript 2019 and later features has been added for custom functions, allowing you to write more efficient, modular, and reusable code.
* [Download DoR Option in Rule Editor](/help/forms/rule-editor-enhancements-use-cases.md#downloaddor-as-ootb-fuction-in-rule-editor): A function to download the Document of Record (DoR) has been added as an out-of-the-box (OOTB) option in the Rule Editor.

  ![Document-of-Record](/help/forms/assets/document-of-record-rn.gif)

* [Dynamic Variables in Rule Editor](/help/forms/rule-editor-enhancements-use-cases.md#support-for-dynamic-variables-in-rules): You can now use dynamic (temporary) variables in the Rule Editor for greater flexibility in defining conditions and actions. Hidden fields are no longer required to store temporary values.
* [Custom Event Based Rules Support](/help/forms/rule-editor-enhancements-use-cases.md#custom-event-based-rules-support): You can now define custom events and trigger rules based on those events.
* [Context-Aware Repeatable Panel Rules](/help/forms/rule-editor-enhancements-use-cases.md#context-based-rule-execution-for-repeatable-panels): In repeatable panels, rules are now executed based on context, instead of being applied only to the last panel instance.
* [Rules Triggered by Parameters](/help/forms/rule-editor-enhancements-use-cases.md#url-and-browser-parameter-based-rules-in-adaptive-forms): The Rule Editor now supports rule execution based on query parameters, UTM parameters, or browser parameters.
* [Form-Specific Custom Functions](/help/edge/docs/forms/universal-editor/rule-editor-universal-editor.md#organizing-custom-functions-across-different-forms): Edge Delivery Services Forms now support form-specific custom function scripts, providing greater flexibility in managing reusable logic.
* [Static Imports for Custom Functions](/help/edge/docs/forms/universal-editor/rule-editor-universal-editor.md#static-imports-for-custom-functions): The Rule Editor in Universal Editor now supports static imports, allowing developers to organize, share, and reuse functions across multiple forms.

### New Early Access Features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program offers a unique opportunity for you to get exclusive access to cutting-edge innovations and help shape their development.

These release notes list the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

**Scribble Signature Component**

You can now use the [Scribble Signature component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/scribble-signature) to help users add their signatures to a form, such as in an agreement form. The component allows users to draw their signature directly within the form using a mouse, stylus, or touchscreen.

**Direct API Integration in Rule Editor**

Adaptive Forms now support [direct API integration](/help/forms/api-integration-in-rule-editor.md) in the Visual Rule Editor without requiring a Form Data Model. Authors can configure APIs using a URL or cURL import, map input/output parameters, and secure calls with authentication.
 
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
>Available as a Limited Availability feature on September 29th.
>Email [aemcs-update-free@adobe.com](mailto:aemcs-update-free@adobe.com) to get it activated on your programs.

### Upcoming Java API Deprecations {#java-api-deprecation}

Several deprecated APIs are targeting removal on August 31st and thus should no longer be referenced. Actions Center notifications are being sent if deprecated API usage is detected, and after September 25th, notices will appear during Cloud Manager builds to reinforce the importance of removing usage. See the [deprecation article](/help/release-notes/deprecated-removed-features.md#aem-apis) for full details, but for convenience, these APIs are listed below:

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

The *Java 11 runtime* is deprecated, and most environments have already been upgraded to the more performant **Java 21 runtime**.

If your environment could not be upgraded due to unsupported dependencies (see [Java 21 runtime requirements](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements)), you would have received an email from Adobe with next steps. As described in the email, Adobe upgraded your dev and RDE environments on September 18th and so you can validate that your site and processes work as expected and fix any issues. The upgrade on stage and production environments will proceeed on **October 14th**.

Note: The runtime version is separate from your code's build version. While we recommend building with Java 21, Java 11 builds are still supported for now. A separate deprecation notice for Java 11 builds will be shared in the future.

### Enforcement of AEM Java Logs Configuration Policy {#logconfig-policy}

As noted in the April release notes, AEM Java logs must follow a standard format to ensure reliable monitoring across all customer environments. Custom log configurations—such as changes to log formatting, output files, or default log levels—are no longer supported. Logs must remain directed to the default files, and default log levels for AEM product code must be preserved. See full details in the [Logging article](/help/implementing/developing/introduction/logging.md#configuration-loggers).

Starting on **September 25th**, any unsupported custom logging overrides will be ignored. Based on our analysis, most customers will not be impacted and Adobe has contacted customers whose current configuration may be affected.

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

Separately from Edge Delivery Services, note that earlier this year we released a feature to configure Open ID Connect [for AEM Cloud Service publish tier projects](/help/security/open-id-connect-support-for-aem-as-a-cloud-service-on-publish-tier.md) to secure AEM pages.

### CDN Configuration for Edge Delivery Services (Beta Program) {#cdn-eds-beta}

The Adobe-Managed CDN offers flexible configuration options, as described in the [Config Pipeline article](/help/operations/config-pipeline.md#configurations). 

Now in beta, youcan deploy a config pipeline for features including CDN origin selectors, response and request transformations, CDN log forwarding and more. Please reach out to [aemcs-cdn-config-adopter@adobe.com](mailto:aemcs-cdn-config-adopter@adobe.com) with the details of your use case.

### Snapshots for RDEs (Alpha Program) {#rde-snapshot-program}

In alpha, Rapid Development Environments (RDEs) now support a feature to take a snapshot of the current state of code and content, which can be restored at a later time. This can be useful when syncing code that may need to be reverted, or when switching between development of different features. It's also possible to restore just the mutable content as a known starting point for testing.

Please email [aemcs-rde-support@adobe.com](mailto:aemcs-rde-support@adobe.com) if there's interest in providing feedback on this feature.

### AEM Log-Forwarding to More Destinations (Beta Program) {#log-forwarding-beta}

While logs can be downloaded from Cloud Manager, many organizations find it beneficial to stream those logs to a preferred logging destination. AEM already supports AEM and CDN log forwarding to Azure Blob Storage, Datadog, HTTPS, Elasticsearch (and OpenSearch), and Splunk. This feature is configured in a self-serve manner, and deployed using the Config Pipeline.

Now in beta, you can forward AEM logs to Amazon S3, Sumo Logic, Dynatrace, and your own New Relic account (not the Adobe-provided account). Note that AEM logs (including Apache/Dispatcher) are supported for these logging destinations, but not CDN logs. Email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) for access.

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
