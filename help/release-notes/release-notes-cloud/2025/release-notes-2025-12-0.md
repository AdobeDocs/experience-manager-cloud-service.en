---
title: Release Notes for 2025.12.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2025.12.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
feature: Release Information
role: Admin
---
# 2025.12.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2025.12.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2023 or 2024.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2025.12.0) is December 11, 2025. The next feature release (2026.1.0) is planned for January 29, 2026.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the July 2025 Release Overview video for a summary of the features added in the 2025.7.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3440920?quality=12)

-->

## AEM Beta Programs {#aem-beta-programs}

Adobe Experience Manager (AEM) beta programs are a way for customers to get access to prerelease features and code, provide feedback, and guide the future of AEM. 

>[!IMPORTANT]
>
>Beta releases may contain defects and are provided "AS IS" without warranty of any kind. Adobe has no obligation to maintain, correct, update, change, modify or otherwise support (by way of Adobe Support Services or otherwise) the beta releases. Adobe advises customers to use caution and not rely on the correct functioning or performance of beta releases, or on any accompanying documentation or materials. Features and APIs in beta are subject to change without notice. Accordingly, any use of the beta releases is entirely at the customer's own risk.

**Benefits of participating**
Getting early access to features that Adobe is developing lets customers and partners provide feedback and shape product development. It also helps them prepare to adopt new capabilities before general availability.

**Current beta programs**
The following sections list active beta programs.

### Agents in AEM (Beta program) {#agents-in-aem-beta-program}

Gain early access to powerful, new AEM agentic capabilities across production, governance, optimization, discovery, and development. Your feedback directly shapes Adobe's roadmap and final features. See [Overview of Agents in AEM](/help/ai-in-aem/agents/overview.md) to learn more.

This program typically lasts 4-6 weeks, but can be tailored to be flexible around your ability to actively participate. 

To opt in to participate in this program, email [aemagentsteam@adobe.com](mailto:aemagentsteam@adobe.com) and include the following details to the extent possible:

* Names and Adobe ID's of team members who will actively use agents.
* List Specific agents that you or your team will want to use. Or simply say "All Agents."

### AEM Foundation (Beta programs) {#aem-foundation-beta-programs}

See [AEM Foundation beta programs](#foundation-early-adopter).

### Cloud Manager (Beta programs) {#cloud-manager-beta-programs}

See [Cloud Manager beta programs](/help/implementing/cloud-manager/release-notes/current.md).


## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

**New version of Figma Plugin for integration with AEM Assets is available**

* Support for video files (MP4, MOV, WebM), Animated files (GIF), and Vector files (SVG) while importing assets from AEM repository to the Figma document.

* Support for checking if there are any updates to the assets that are used in Figma document as compared to the assets that exist in AEM repository and getting the latest version of assets if there are any updates.

* Support for export configurations while exporting PNG (scale) and JPG (image scale and quality) file formats.

   ![Figma plugin](/help/assets/assets/figma-v2-plugin.png)

**Malware detection for uploaded assets**

AEM Assets now includes automatic malware scanning of uploaded files, ensuring that suspicious assets are quarantined before entering the DAM to protect your repository from threats. Administrators can configure scan settings and quarantine retention policies for streamlined security controls.

**AI-Generated metadata – Eligibility Update**

AI-Generated metadata in AEM Assets no longer requires the GenAI Rider to be signed in order to be enabled. The feature is now available to both customers who have signed the GenAI Rider and customers who have not yet been validated. Customers who have explicitly opted out of GenAI usage will continue to have the feature disabled. To manage the feature enablement at the environment-level, please see [Disable AI-generated metadata](/help/assets/enhance-content-discovery-with-ai-generated-metadata.md#disable-ai-generated-metadata). This change will be made for customers on release version 23482 or later.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

<!-- ### Pre-Release features in AEM Forms 

**Rule Editor Enhancements**

The Rule Editor now supports enhanced navigation and allows use of function and mathematical expressions in input parameters.

**Enhanced Navigation with Event Payload Support**
 
The `Navigate To` action in the Invoke Service handlers now supports `EVENT_PAYLOAD`, enabling form authors to configure follow-up actions based on event responses. This enhancement offers greater flexibility in designing post-submission workflows, ensuring smoother transitions and more personalized user experiences. For more information, see [Enhanced Navigation with Event Payload Support](/help/forms/invoke-service-enhancements-rule-editor.md#use-case-5-use-event-payload-in-navigate-to-action-in-invoke-service).

**Function and Mathematical Expression Support in Input Parameters**
 
Input parameters now support both function calls and mathematical expressions, enabling form authors to pass dynamically computed values directly. This enhancement streamlines rule configurations, eliminates the need for extra fields, and makes forms more adaptable to complex logic and calculation-driven scenarios. For more information, see [Function and Mathematical Expression Support in Input Parameters](/help/forms/rule-editor-core-components-user-interface.md#function-and-mathematical-expression-support-in-input-parameters). --> 

### New Early Access Features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program offers a unique opportunity for you to get exclusive access to cutting-edge innovations and help shape their development.

These release notes list the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### Interactive Communication Enhancements 
 
##### Template Locking 

Lock content and layout elements within templates to maintain brand integrity and prevent unauthorised modifications. This ensures design consistency across all communications. 

##### Content Overflow Support 

Introducing the "Allow page breaks within content" option for flowed layouts. This enhancement enables smooth multi-page editing and better text management for complex documents. 

##### XDP File Editing 

The Interactive Communication editor now supports XDP editing, including fragment integration. You can now edit XDP files in a browser instead of Forms Designer that runs only on Microsoft Windows desktop. 

##### Dynamic Page Numbering 

Automatically display "Page # of ##" on master pages for clear, consistent pagination across multi-page documents. 

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

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation New Features {#foundation-new}

#### Upcoming Java API Deprecations {#java-api-deprecation}

Several deprecated APIs were marked for removal on August 31st and thus should no longer be referenced. You will receive Actions Center notifications if deprecated API usage is detected in your code, and after Jan 29th, notices will appear during Cloud Manager builds to reinforce the importance of removing usage. See the [deprecation article](/help/release-notes/deprecated-removed-features.md#aem-apis) for full details, but for convenience, these APIs are listed below:

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

#### Java 11 Runtime Deprecation {#java11-runtime-deprecation}

Adobe upgraded **Stage** and **Production** environments to the higher-performance **Java 21 runtime** on October 14th, 2025. Starting **February 9th**, neither the AEM Cloud Service SDK nor any cloud environments will work with Java 11 runtime.

>[!NOTE]
>
> To take advantage of the latest performance optimizations and language enhancements, it is recommended to build with Java 17 or Java 21  (preferred). Building with Java 8 and Java 11 remains supported for now but will be deprecated in an upcoming release. A separate communication will be issued prior to deprecation. See the *build time requirements* section of [this article](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements).
>

#### Enforcement of AEM Java Logs Configuration Policy {#logconfig-policy}

As noted in the April release notes, AEM Java logs must follow a standard format to ensure reliable monitoring across all customer environments. Custom log configurations—such as changes to log formatting, output files, or default log levels—are no longer supported. Logs must remain directed to the default files, and default log levels for AEM product code must be preserved. See full details in the [Logging article](/help/implementing/developing/introduction/logging.md#configuration-loggers).

Starting on **January 29th**, any unsupported custom logging overrides will be ignored. Based on our analysis, most customers will not be impacted and Adobe has contacted customers whose current configuration may be affected.

Please review and update any downstream processes that rely on custom logging behavior. For example:

* If your log forwarding system expects a custom log format, you may need to adjust your ingestion rules.
* If you've previously reduced log verbosity by changing log levels, please note that reverting to default levels may increase log volume.

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Early Adopter Features {#foundation-early-adopter}

#### Pause Automatic Maintenance Updates {#pause-updates}

Go‑live days, live events, peak sales—these moments can't break. [Our new self‑service features](/help/implementing/deploying/quiet-hours-update-free-periods.md) stop automatic mainteanance updates when it matters, so your teams stay focused.

* Quiet Hours: Block automatic maintenance during set times each day. Ideal for working hours, nightly runs or morning cutovers.
* Update‑Free Period: Block automatic maintenance for a full week. Use it for launches, promos, or yearly freezes.

>[!NOTE]
>
>Available as a Limited Availability feature on September 25th.
>Email [aemcs-update-free@adobe.com](mailto:aemcs-update-free@adobe.com) to get it activated on your programs.
>

#### Edge Computing (Beta Program) 

Edge computing allows you to execute JavaScript at the CDN layer, bringing data processing closer to the end user. This reduces latency and enables responsive, dynamic experiences at the edge.

Common use cases include:

* Personalizing content based on geolocation, device type, or user attributes
* Acting as middleware between the CDN and your origin
* Reformatting responses from third-party APIs (and perhaps aggregating multiple API responses) before delivering them to the browser
* Composing and serving server-rendered HTML at the edge using content stitched from various backends
* Exposing an MCP server for LLMs like ChatGPT and Claude to access custom tools

We have a limited number of opportunities available for either AEM Publish Delivery or Edge Delivery Services projects for live production sites. If you're interested in participating or want to learn more, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case.

#### Edge Authentication for Edge Delivery Services (Beta Program) {#edge-authentication}

Edge Authentication lets you restrict access to Edge Delivery Services pages to only those who have authenticated with your identity provider (IdP). This is achieved by deploying an OpenID Connect (OIDC) configuration YAML file.

If interested, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case and any questions you may have.

#### Canary Production Deployments to Test Code Before Accepting Live Traffic (Beta Program) {#canary-beta}

Validate a production build with internal-only test traffic before exposing it to end users. Ship to production, route only canary traffic (using a special header), monitor behavior, then either promote to live traffic or roll back—without impacting customers.

Deploy your code releases to production, but restrict it to only internal test traffic before deciding whether to accept live traffic versus rolling back. 

Email [aemcs-canary-deployments-beta@adobe.com](mailto:aemcs-canary-deployments-beta@adobe.com) to request access and share feedback.


#### Snapshots for RDEs (Beta Program) {#rde-snapshot-program}

In beta, Rapid Development Environments (RDEs) now support a feature to take a snapshot of the current state of code and content, which can be restored at a later time. This can be useful when syncing code that may need to be reverted, or when switching between development of different features. It's also possible to restore just the mutable content as a known starting point for testing.

Please email [aemcs-rde-support@adobe.com](mailto:aemcs-rde-support@adobe.com) if there's interest in using and providing feedback on this feature.

#### Accelerate AEM Development with AI (Alpha Program) {#ai-dev-alpha}

AEM Java-stack teams are increasingly using AI-assisted development in tools such as Cursor, Claude Code, Visual Studio, and IntelliJ to speed up feature delivery and improve code quality. We're gathering real-world experiences to help shape future Adobe-supported AI capabilities.

Share what's working for your team—and what you'd like Adobe to provide—by emailing [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com).

#### Expanded Application Performance Monitoring (APM) (Alpha program) {#apm-alpha}

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
