---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service
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
>From here, you can navigate to release notes of previous versions such as 2024 or 2025.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2026.6.0) is June 25, 2026. The next feature release (2026.7.0) is planned for July 30, 2026.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the May 2026 Release Overview video for a summary of the features added in the 2026.5.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3491490/?quality=12)

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

### Agents in AEM {#agents-in-aem}

If you would like to explore the powerful, new AEM agentic capabilities across production, governance, optimization, discovery, and development, [please learn about how you can access them here.](/help/ai-in-aem/agents/overview.md)

<!--
### Agents in AEM (Explorer program) {#agents-in-aem-beta-program}

Gain early access to powerful, new AEM agentic capabilities across production, governance, optimization, discovery, and development. Your feedback directly shapes Adobe's roadmap and final features. See [Overview of Agents in AEM](/help/ai-in-aem/agents/overview.md) to learn more.

This program typically lasts 4-6 weeks, but can be tailored to be flexible around your ability to actively participate. 

To opt in to participate in this program, email [aemagentsteam@adobe.com](mailto:aemagentsteam@adobe.com) and include the following details to the extent possible:

* Names and Adobe ID's of team members who will actively use agents.
* List Specific agents that you or your team will want to use. Or simply say "All Agents."

Customers selected for participation will be notified directly by Adobe. Participation is subject to eligibility considerations, including customer licensing and limited program capacity. While not all requests can be accommodated initially, additional customers may be considered in future beta waves.
-->

### AEM Foundation (Beta programs) {#aem-foundation-beta-programs}

See [AEM Foundation beta programs](#foundation-early-adopter).

### Cloud Manager (Beta programs) {#cloud-manager-beta-programs}

See [Cloud Manager beta programs](/help/implementing/cloud-manager/release-notes/current.md).

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Content Hub {#new-features-content-hub}

**AI Search**

AEM Assets Content Hub now includes AI Search, an advanced search capability that understands the meaning and intent behind user queries instead of relying only on exact keyword matches. AI Search delivers more accurate and context-aware results by recognizing relationships between words, concepts, and user intent. It supports multilingual queries, handles misspellings and typos, understands synonyms, and surfaces relevant assets even when users do not use exact metadata terms. 

For example, a search for `Woman drinking coffee` can also return assets tagged with related terms such as `Lady`, `Girl`, `Latte`, or `Cappuccino`. 

Administrators can enable or disable AI Search in Content Hub using the Configurations menu by selecting either AI Search or traditional keyword search.


**Custom Sorting options**

Content Hub now allows administrators to enable custom metadata fields as sorting options on the Content Hub home page. In addition to the default sorting options, Size, Modified, Name, and Relevance, administrators can configure business-specific metadata fields such as Channel, Region, SKU, or Campaign to help users organize search results more effectively.

**Asset Search and Download Event Support for Delivery APIs**

AEM Assets Delivery APIs now support asset search and asset download events, enabling organizations to track and respond to how assets are discovered and consumed across connected applications and experiences. These events help improve visibility into asset usage patterns, support analytics and reporting workflows, and simplify integrations with external systems and automation processes. 

With event-driven insights, teams can better understand content engagement and build more connected digital asset workflows. For more details, see the [API documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/asset_downloaded).

>[!IMPORTANT]
>
>These features are available as Limited Availability features. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

### New features in Dynamic Media with OpenAPI capabilities {#new-features-dynamic-media-openapi}

**Video Smart Crops**

Dynamic Media with OpenAPI capabilities now support Video Smart Crops for video assets in AEM Assets. Video Smart Crops use AI-powered analysis to automatically keep the primary subject in focus across different aspect ratios and devices, helping deliver optimized viewing experiences on web and mobile. Once enabled and configured by administrators, organizations can generate smart cropped video outputs for approved assets and dynamically deliver the most appropriate framing during playback.

**Multi-caption and multi-audio track support for videos**

Dynamic Media with OpenAPI capabilities now support multiple captions and multiple audio tracks for video assets. It enables organizations to deliver localized and accessible video experiences to global audiences by associating multiple language-specific caption and audio tracks with a single primary video. Authors can efficiently manage these tracks from a unified interface, simplifying multilingual content delivery and supporting regional accessibility requirements.

>[!IMPORTANT]
>
>These features are available as Limited Availability features. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New Features in AEM Forms

* **Versioning support in Forms Manager**
Forms Manager now [supports versioning for Adaptive Forms (Core Components and Foundation Components)](/help/forms/manage-form-versions-forms-manager.md), form fragments, themes, XDP templates, and binary assets. Create versions, view complete version history, and restore earlier states of your form assets directly from the Forms & Documents console.

* **Override reCAPTCHA cloud configuration with OSGi**  
reCAPTCHA Enterprise project IDs, site keys, and secrets that you keep with your source files can resolve to different values on each Cloud Service environment after you [add the Context-Aware Configuration override and deploy through Cloud Manager](/help/forms/captcha-adaptive-forms.md#override-recaptcha-osgi).

* **Certificate-based authentication**  
Adaptive Forms that submit to a Microsoft SharePoint list now support [certificate-based authentication](/help/forms/connect-forms-to-sharepoint-list.md#certificate-based-authentication) alongside OAuth URL authentication. For certificate-based sign-in, register a certificate alias and tenant details in AEM and Microsoft Azure.

* **Rule Editor Enhancements**

  * The Adaptive Forms rule editor now supports the simplified grammar for [Dispatch Event and On Trigger Event rules for out-of-the-box (OOTB) triggers and for custom events](/help/forms/rule-editor-enhancements-use-cases.md#simplified-grammar-for-ootb-and-custom-events), so authors are not limited to grammar on custom triggers only. 
  * When rules on Adaptive Forms based on Core Components now include the [File Attachment component together with other conditions using AND or OR logic](/help/forms/rule-editor-enhancements-use-cases.md#combined-when-conditions-with-the-file-attachment-component), so the rule runs its actions only when the attachment state and the other checks all evaluate as intended.
  
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation New Features {#foundation-new}

#### Conversational AI Interface for Cloud Manager Questions {#devagent-cloudmanager}

The Development Agent expands to handling questions related to Cloud Manager through the [Cloud Manager Job](/help/ai-in-aem/agents/brand-experience/development/development.md#cloud-manager-job). In AI Assistant, retrieve information about programs, environments, and pipelines (e.g., execution status). Quickly find links to error logs, access logs, and build logs. 

#### Enhancements to Pipeline Troubleshooting Agent Job {#devagent-pipeline-troubleshooting}

The Development Agent's [pipeline troubleshooting job](/help/ai-in-aem/agents/brand-experience/development/development.md#cloud-manager-pipeline-troubleshooting) help developers diagnose and resolve issues in AEM as a Cloud Service deployments. New features include:

* Support for Web Tier Config Pipeline - In addition to supporting Full Stack pipelines (Deployment and Code Quality), the Development Agent now supports troubleshooting for the **Web Tier Config Pipeline**

* Experience Hub Widget for failed pipelines - IT roles will see a new widget highlighting pipeline failures. A clickable button initates the pipeline troubleshooting job in AI Assistant.

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Important Notices {#foundation-notices}

#### IMS Authentication Rich Errors {#ims-auth-rich-errors}

To help troubleshoot IMS integrations, `imsauth` has added support for *rich errors*.

Instead of returning only an HTTP status code, these errors provide additional context to help diagnose and resolve issues that can block authentication and access.

#### Java API Deprecations {#java-api-deprecation}

It is critical to remove usage of deprecated APIs. 

Since **April 14**, Cloud Manager pipelines that contain code using APIs targeting 2/26/2026 removal **fail during the Code Quality** step. Deployments will be blocked until the deprecated API usage is removed. *This may prevent you from releasing time-sensitive updates and could impact your business operations.* 

Starting **June 24, 2026**, environments still using these deprecated APIs **will not receive critical Adobe release updates** and will not be subject to Adobe's standard commitments around performance and availability. As a result, you will not receive new features or bug fixes, application stability and uptime may be negatively affected, and security risk exposure may increase further.

See the [deprecation article](/help/release-notes/deprecated-removed-features.md#aem-apis) for full details, but for convenience, these APIs are listed below:

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
* `org.apache.jackrabbit.oak.plugins.memory`

+++

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Early Adopter Features {#foundation-early-adopter}

#### AEM Edge Functions (Public Beta Program) {#edge-functions}

[AEM Edge Functions](/help/implementing/developing/introduction/edge-functions.md) is now in public beta so you can self-serve try it out without contacting Adobe.

This feature allows you to execute JavaScript at the CDN layer, bringing data processing closer to the end user. This reduces latency and enables responsive, dynamic experiences at the edge. It's available for both AEM Java Stack and Edge Delivery Services projects.

Common use cases include:

* Personalizing content based on geolocation, device type, or user attributes
* Acting as middleware between the CDN and your origin
* Reformatting responses from third-party APIs (and perhaps aggregating multiple API responses) before delivering them to the browser
* Composing and serving server-rendered HTML at the edge using content stitched from various backends

*By using the AEM Edge Functions Beta, you acknowledge that it is still in development and that you should not rely on the correct functioning of the technology or availability of data. This feature is provided as-is,
may change without notice, and is not covered by production SLAs.*


#### Snapshots for RDEs (*Public Beta* Program) {#rde-snapshot-program}

Snapshots for Rapid Development Environments (RDEs) is now in public beta so you can self-serve try it out without contacting Adobe.

RDEs now support a feature [to take a snapshot](/help/implementing/developing/introduction/rapid-development-environments.md#snapshots) of the current state of code and content, which can be restored at a later time. This can be useful when syncing code that may need to be reverted, or when switching between development of different features. It's also possible to restore just the mutable content as a known starting point for testing.

*By using the RDE Snapshots Beta, you acknowledge that it is still in development and that you should not rely on the correct functioning of the technology or availability of data. While we have tested this feature extensively, there is a small possibility that your RDE could become unstable. If this occurs, a reset will restore it to a working state.*


#### Manage Quiet Hours and Update Free Periods with the AEM AI Assistant (Limited Availability) {#quiet-hours-ai}

You can now view, create, and edit Quiet Hours and Update Free Periods directly through the AEM AI Assistant.
The key benefit is fewer scheduling errors. As you make a request, the assistant guides you through what is possible and flags the limits that apply, such as the three-period cap, the mandatory one-week gap between periods, and the planned maintenance exclusion windows you cannot schedule over. So instead of discovering a constraint after a failed configuration, Business Owners and Deployment Managers are steered to a valid schedule in the same conversation. This protects critical business windows from automatic maintenance updates while reducing back-and-forth and misconfiguration.

#### Replication AI Troubleshooting (Beta Program) {#replication-ai-troubleshooting-alpha}

Using the AI Assistant in AEM Author and other interfaces, you can troubleshoot replication-related issues such as blocked queues. To join the Beta Program, email [aem-devagent@adobe.com](mailto:aem-devagent@adobe.com), describing your interest.

#### Edge Authentication for Edge Delivery Services (Beta Program) {#edge-authentication}

Edge Authentication lets you restrict access to Edge Delivery Services pages to only those who have authenticated with your identity provider (IdP). This is achieved by deploying an OpenID Connect (OIDC) configuration YAML file.

If interested, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case and any questions you may have.

#### Canary Production Deployments to Test Code Before Accepting Live Traffic (Beta Program) {#canary-beta}

Validate a production build with internal-only test traffic before exposing it to end users. Ship to production, route only canary traffic (using a special header), monitor behavior, then either promote to live traffic or roll back—without impacting customers.

Email [aemcs-canary-deployments-beta@adobe.com](mailto:aemcs-canary-deployments-beta@adobe.com) to request access and share feedback.

#### AEM Code Assessment and auto-fix via IDE AI agent (Beta Program) {#ide-ai-aemcode-issues}

Java-stack teams using [AI-assisted development](/help/ai-in-aem/local-development-with-ai-tools.md) in tools like Cursor, Claude Code, Visual Studio, and IntelliJ can now go further: a new IDE agent skill detects and auto-fixes issues directly in your AEM codebase, reducing review cycles and catching problems earlier in development.

This feature is in beta. Join the program to try it and share feedback with the team at [aemcs-ai-ide-tools-feedback@adobe.com](mailto:aemcs-ai-ide-tools-feedback@adobe.com).

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
