---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service
description: Current release notes for [!DNL Adobe Experience Manager] as a Cloud Service.
mini-toc-levels: 2
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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2026.9.0) is September 24, 2026. The next feature release (2026.10.0) is planned for October 29, 2026.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the May 2026 Release Overview video for a summary of the features added in the 2026.5.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3491490/?quality=12)

-->

## Release Overview {#overview}

The 2026.8.0 release of [!DNL Experience Manager] as a [!DNL Cloud Service] delivers new capabilities across Assets, Forms, and Foundation, with a continued emphasis on AI-assisted workflows, content authenticity, and preparing customers for upcoming platform changes.

**Highlights of this release**

* **Content authenticity with C2PA** — Asset renditions now carry C2PA metadata based on the original, and C2PA support extends to Dynamic Media (OpenAPI and Scene7), helping customers label Gen AI content and meet transparency requirements.
* **AI-powered Assets workflows** — Content Hub can generate Dynamic Media renditions on the fly, and Assets Insights now supports the Adobe Analytics 2.0 API with OAuth Server-to-Server authentication ahead of the Analytics 1.4 API retirement.
* **Foundation and platform** — Agentic permission management for real-time ACL auditing, AEM Edge Functions for running JavaScript at the CDN, and IMS authentication rich errors for easier troubleshooting.
* **Plan-ahead notices** — Important timelines for Java API deprecations and the upcoming Java 25 runtime upgrade help customers prepare their environments.

A range of beta, early adopter, and alpha programs are also available this release. See the sections below for details.

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

### AEM Assets (Beta programs) {#aem-assets-beta-programs}

See [AEM Assets beta programs](#assets-beta-program-features).

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

**C2PA metadata support**

Renditions of assets now [supports C2PA metadata based on the original, enabling easy labelling of Gen AI manipulated content](/help/assets/c2pa-metadata-assets-view.md). This helps Experience Manager customers comply with Gen AI labelling laws; customers should validate compliance with regulations on their own. Metadata can be inspected using any C2PA inspection tool. See [Adobe C2PA inspection tool](https://contentauthenticity.adobe.com/inspect). 

New JCR properties for a C2PA manifest (dam:hasC2PAManifest) and Gen AI (dam:isAiGenerated) labels are available on Assets processed with an embedded C2PA manifest. The Gen AI label property can be used in cases where C2PA is not utilized. This is not recommended since management of the property is manual and many of the Adobe and 3rd party tools use C2PA.

**Assets Insights now supports Adobe Analytics 2.0 API**

Assets Insights in AEM Admin View now [supports the Adobe Analytics 2.0 API with OAuth Server-to-Server authentication, enabling continued access to current asset usage insights following the retirement of the Adobe Analytics 1.4 API](/help/assets/assets-insights.md). Customers can reconfigure their Assets Insights integration to resume synchronization of impressions and clicks from Adobe Analytics, including data collected during the transition period, without losing existing insights data.

### New Features in Dynamic Media {#new-features-dynamic-media}

**C2PA metadata support in Dynamic Media**

You can now [apply C2PA metadata to assets in Dynamic Media with OpenAPI capabilities](/help/assets/c2pa-metadata.md) and Dynamic Media Scene7. C2PA metadata embeds secure metadata that helps viewers verify an asset's origin, edit history, and whether generative AI was used during its creation, enabling greater transparency and trust in digital content.

### New features in Content Hub {#new-features-content-hub}

**Generate on-the-fly Dynamic Media renditions in Content Hub**

[Generate on-the-fly Dynamic Media renditions in Content Hub to quickly create asset variations tailored to different channels and content needs](/help/assets/generate-on-the-fly-dynamic-media-renditions.md). This eliminates the need to maintain multiple pre-generated renditions, making it easier to adapt and reuse assets across experiences. With optimized renditions available on demand, teams can accelerate content activation and deliver the right asset variation for every experience.

### [!DNL Experience Manager] as a [!DNL Cloud Service] Assets Limited Availability Features {#assets-limited-availability-features}

#### Dynamic Media with OpenAPI capabilities: Multi-caption and multi-audio track support for videos {#multi-caption-multi-audio}

Dynamic Media with OpenAPI capabilities now support [multiple captions and multiple audio tracks for video assets](/help/assets/multi-audio-multi-caption.md). It enables organizations to deliver localized and accessible video experiences to global audiences by associating multiple language-specific caption and audio tracks with a single primary video. Authors can efficiently manage these tracks from a unified interface, simplifying multilingual content delivery and supporting regional accessibility requirements.

#### Dynamic Media with OpenAPI capabilities: AI-generated video captions {#ai-generated-video-captions} 

AI-generated video captions in Dynamic Media with OpenAPI capabilities [use artificial intelligence to generate captions automatically for video content](/help/assets/generate-translate-captions.md). This feature is designed to improve accessibility and enhance the user experience by providing accurate, real-time captions. The AI analyzes the video's audio track to transcribe speech and create captions, which can be edited for accuracy or customization. These captions help meet accessibility requirements and improve video engagement for audiences who rely on or prefer text-based video support.

#### Dynamic Media with OpenAPI capabilities: Secure Delivery with Attribute-based Access Control {#secure-delivery-attribute-based-access-control}

Attribute-based access control lets admins govern access to Dynamic Media with OpenAPI capabilities assets using metadata-driven rules defined for each user group. IMS-based restrictions allow DAM admins and brand managers to restrict delivery of specific assets to designated Adobe IMS users or groups. Users outside the permitted list receive a 404 response, and the asset is not delivered. This provides a secure way to manage asset delivery for campaigns, product launches, and other controlled distribution scenarios.


#### Dynamic Media: New Video Viewer {#new-video-viewer}

The [new video viewer delivers a performant, accessible, and fully customizable playback experience](/help/assets/dynamic-media/new-video-viewer.md). Configurable playback modifiers, including autoplay, loop, and muted, give you complete control over viewer behavior. Custom CSS support ensures a consistent, on-brand experience across all touchpoints. Actionable analytics track views, watch time, completion rate, and engagement score, providing your teams with meaningful insights into video performance.

#### Content Hub: AI Search {#ai-search-content-hub}

AEM Assets Content Hub now includes [AI Search, an advanced search capability that understands the meaning and intent behind user queries instead of relying only on exact keyword matches](/help/assets/search-assets-content-hub.md#ai-search-aem-assets-content-hub). AI Search delivers more accurate and context relevant results by recognizing relationships between words, concepts, and user intent. It supports multilingual queries, handles misspellings and typos, understands synonyms, and surfaces relevant assets even when users do not use exact metadata terms. 

For example, a search for `Woman drinking coffee` can also return assets tagged with related terms such as `Lady`, `Girl`, `Latte`, or `Cappuccino`. 

Administrators can enable or disable AI Search in Content Hub using the Configurations menu by selecting either AI Search or traditional keyword search.

#### Content Hub: Custom Sorting options {#custom-sorting-options-content-hub}

Content Hub now allows administrators to [enable custom metadata fields as sorting options on the Content Hub home page](/help/assets/search-assets-content-hub.md#configure-sorting-aem-assets-content-hub). In addition to the default sorting options, Size, Modified, Name, and Relevance, administrators can configure business-specific metadata fields such as Channel, Region, SKU, or Campaign to help users organize search results more effectively.


### [!DNL Experience Manager] as a [!DNL Cloud Service] Assets Beta Features {#assets-beta-program-features}


#### Dynamic Media: Video Engagement Report {#video-engagement-report}

Turn video playback into actionable insight by providing per-video engagement metrics for the New Video Viewer, including views, impressions, watch time, completion rate, and engagement score, delivered as a monthly CSV to help teams measure content performance.

To participate or learn more, send an email to `dm-beta-feedback@adobe.com`.

#### Dynamic Media: Operations and Error Report {#operations-and-error-report}

Give teams visibility into delivery health by reporting operational activity such as delivery request counts, smart crops, video encodes, and templates created, while surfacing failed delivery URLs with their referrer and failure count so issues can be pinpointed and fixed.

To participate or learn more, send an email to `dm-beta-feedback@adobe.com`.

#### Dynamic Media: Auto Reflow and Auto Translate {#auto-reflow-and-auto-translate}

Eliminate repetitive redesign and manual localization by using AI to automatically adapt a single master template into layouts that fit different formats and aspect ratios (web, social, display, and email) and to instantly translate text across languages, all while preserving the visual integrity of the design, turning one master asset into variants across many device sizes and locales.

To participate or learn more, send an email to `dm-beta-feedback@adobe.com`.

#### Content Hub: Smart Collections {#smart-collections}

Smart Collections enable you to automatically organize assets based on defined search criteria.
When you create a Smart Collection, the collection stores the search query and filter criteria instead of storing individual assets. Assets that match the configured criteria are automatically displayed in the collection.

Smart Collections automatically remain up to date. When newly approved assets satisfy the configured search criteria, they are automatically added to the collection.

To participate or learn more, send an email to `aemcontenthubbeta@adobe.com`.

#### Multi-portal Content Hub {#multi-portal-content-hub}

Deliver tailored Content Hub experiences for each brand or business unit, while managing content centrally from a single source of truth.

To participate or learn more, send an email to `aemcontenthubbeta@adobe.com`.


#### AI-powered content onboarding and content supply chain automation {#ai-powered-content-onboarding-content-supply-chain-automation}

The Content Supply Chain Agent provides two cooperating AI-powered agents:

* **CSC Blueprint Agent** maps your end-to-end content supply chain, identifies gaps and anti-patterns, and helps define an agreed future state and prioritized action plan.
* **CSC Integration Agent** implements governed content and metadata movement between systems through configured connections, supporting both one-time migrations and recurring synchronization.

To participate or learn more, send an email to `aem-assets-coinnovation-interest@adobe.com`.

#### UI Extensibility for Assets View {#ui-extensibility-assets-view-beta}

Assets View supports UI Extensibility, a developer-first capability that empowers customers to tailor the out-of-the-box experience to meet their specific business requirements.
Customers can leverage existing stable extension points by following Adobe's developer documentation to build and deploy extensions with minimal effort. For use cases where a required extension point is not yet available, Adobe works directly with customers to explore the requirements and assess the technical feasibility of delivering new extensibility APIs tailored to their needs, and may deliver such new APIs as **Beta Releases**.
Additionally, Adobe has developed a **GenAI-powered extension generation tool** currently available in an internal early adoption phase. This tool can significantly accelerate extension development time. Customers participating in this beta program will receive access to the tool and are encouraged to share feedback to help shape its evolution.
To participate or learn more, send an email to `ASSETSVIEWUIEXTENSIBILITY@adobe.com`.

#### Brand Aware Metadata (BAM) {#brand-aware-metadata-beta}

AEM Assets now supports Brand Aware Metadata, an AI-powered capability that automatically generates custom metadata for assets when uploaded or re-processed. This reduces the need for manual entry by orders of magnitude, helping teams find assets and deliver new experiences much faster. Customers maintain a library of prompts that define how AI should populate any given metadata field, tailored to their own brand vocabulary and taxonomy. This prompt library includes a playground to preview results and a prompt optimizer that automatically drafts suggested improvements.

Adobe is actively expanding BAM's capabilities through direct co-innovation with customers. Where a specific use case is not yet supported, Adobe works with participating customers to understand their needs and may deliver expanded capabilities as the beta progresses. Customers in this program gain early access to new features as they ship and are encouraged to share feedback that directly shapes the roadmap.

To participate or learn more, send an email to `AEM-ASSETS-BRANDAWAREMETADATA@adobe.com`.

<!--

#### Assets Onboarding Agent {#assets-onboarding-agent-beta}

If your organization is new to Experience Manager Assets, you can opt in to the **Assets Onboarding Agent Beta program**, which gives you access to the following AEM Brand Experience AI skills for onboarding:

* Guides users through DAM setup and migration planning by using a conversational workflow to capture business needs and recommend how an AEM Assets deployment should be structured.

* Creates core AEM Assets configuration artifacts such as folder hierarchies, tag taxonomies, metadata forms, and can help execute bulk import jobs to accelerate onboarding.

**Why participate?**

* Go live faster with a ready-to-use DAM environment by eliminating repetitive, manual steps with AI assistance.

* Lower operational overhead with automated configuration and preparation of folders, tags, metadata and asset imports.

* Improve consistency, governance, and ensure adherence to best practices through a curated setup experience with intelligent recommendations tailor-made for your business.

To participate or learn more, send an email to `GRP-AEM-ONBOARDING-AGENT@adobe.com`.

-->

#### Assets Sourcing portal for AEM Assets {#asset-sourcing-aem-assets}

[The Assets Sourcing Portal](/help/assets/asset-sourcing-portal-for-aem-assets.md) provides a secure, self-service experience for collecting assets from external contributors without granting them access to Adobe Experience Manager Assets. Contributors can upload assets, provide the required metadata, and submit content directly to a designated intake location while administrators maintain control over asset organization and governance.

Adobe works with participating customers to understand their needs and may deliver expanded capabilities as the limited availability program progresses. Customers in this program gain early access to new features as they ship and are encouraged to share feedback that directly shapes the roadmap.

To participate or learn more, send an email to `AEM-Assets-Sourcing-Portal@adobe.com`.

#### Support for additional asset types in Adobe Express integration {#assets-express-integration-asset-types-beta}

Adobe Express integration with Assets helps all users create and edit on-brand content and increase content reuse. We have worked on supporting a growing list of asset / file types to be supported by the integration, and some of them are available early to customers  interested in using them:

**Asset view UI - "Open in Express"** to import an asset into a new Express document in the embedded Express editor:

* **.mp4** video assets

**Assets plugin in Adobe Express** to import an asset into the current Express document:

* **.ai** Adobe Illustrator assets
* **.indd** Adobe InDesign assets
* **.mov** video assets
* **.mp3** audio assets
* **.gif** animated assets

To participate or learn more, send an email to `aem-assets-express@adobe.com`.


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

<!--

#### API Integration Tool for Dynamic Form Data

Form authors can now use the API Integration Tool to build forms that fetch and fill in data from external REST APIs, based on what the user does in the form. This no-code tool supports use cases like address auto-completion, dynamic dropdown lists, and real-time validation. For more information, see [API Integration Tool for Dynamic Form Data](/help/forms/api-integration-tool-dynamic-form-data.md).

-->

### Early Access Features in AEM Forms

#### Table component in Adaptive Forms based on Core Components

Adaptive Forms based on Core Components can now include a Table component to present complex, structured data in tabular layouts. Government and financial services forms often require tabular layouts for numeric data, line items, and multi-column inputs. The Table component supports:
- Structured row and column authoring with header and body rows
- Repeatable rows with add and remove actions at runtime
- Column sorting with ascending and descending order
- Disable sorting on individual columns for accessibility compliance
- Proportional column widths
- Merge and split table row cells
- Replace default text box cells with other Adaptive Form components
- Row-level calculations using the Rule Editor
- Table rendering in Submission PDF (Document of Record).
 
For more information, see [Add a table to an Adaptive Form (Core Components)](/help/forms/adaptive-forms-tables-core-components.md).

#### Document conversion APIs

Added support for new [document conversion APIs](/help/forms/aem-forms-communication-api-overview.md#document-conversion-apis) that enable applications to convert documents to supported formats and optimize PDFs for printing and processing. The following APIs are available:
- **HTML to PDF** – Converts HTML documents to PDF while preserving page layout and styling.
- **PostScript (PS) to PDF** – Converts PostScript documents to PDF.
- **PDF to Image** – Converts PDF documents into one or more image files.
- **PDF to PostScript (PS)** – Converts PDF documents to PostScript format.
- **Flatten PDF Transparency** – Flattens transparent objects in PDF documents to improve compatibility with print and document processing workflows.

#### Locale support for Interactive Communication

Interactive Communication Editor now allows authors to [configure the locale for an Interactive Communication](/help/forms/interactive-communication/support-localization.md). The selected locale determines language and region-specific formatting, such as dates, numbers, and currencies, enabling localised content for different audiences

#### Virus scanning and custom validation for file attachments

Validate file attachments in Adaptive Forms before or on submission using custom validation logic, such as integrating a malware or virus scanning service. You can use form rules to trigger validation, or configure validation to run on form submission. Both approaches reject invalid or infected files before persistence, helping protect sensitive data and systems. For details, see [Implement a custom validator](/help/forms/scan-file-attachments-custom-validator.md) and [Tutorial: Antivirus scanning integration](/help/forms/scan-file-attachments-clamav.md).

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation New Features {#foundation-new}

#### Canary Deployments - Validate Features Before Accepting Live Traffic {#canary-deployments}

[Canary deployments] let you validate a new release against production infrastructure before it serves customer traffic. Available **October 1st** for AEM Cloud Service implementations.

Deploy the build alongside your current stable release on the publish tier, then route selected requests to it with a request header. All other traffic continues to be served by the stable release, unaffected. The author tier remains on the stable version throughout.

During the validation window of 3 hours, you can:

* Promote the canary release to serve all live traffic, or
* Cancel it and keep the current release running.

#### New capabilities in AEM MCP {#aem-mcp}

[AEM MCP Server](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md) allows you to configure a single URL in your chat application or coding agent to access a growing set of capabilities. 

In addition to Content operations (pages, content fragments, and assets) and Experience Governance checks, AEM MCP now supports Cloud Manager operations to manage programs, environments, and pipelines.

Cloud Manager operations were previously only available through the deprecated domain-specific MCPs. Customers using those should switch to the AEM MCP Server.

The AEM MCP Server is also used by the [AEM Claude Connector](/help/ai-in-aem/mcp-support/setup-claude.md#install-adobe-experience-manager-connector) and [AEM ChatGPT Plugin](/help/ai-in-aem/mcp-support/setup-chatgpt.md#install-adobe-experience-manager-plugin).

<!--

- Cloud Migration: fetch Best Practices Analyzer (BPA) findings from Cloud Acceleration Manager (CAM) by migration pattern or severity level, enabling AI agents to drive code migration from AEM 6.x to AEM as a Cloud Service. 

-->

#### OpenTelemetry for Application Performance Monitoring (APM) (Limited Availability) {#optel}

In Limited Availability (see note below for access), AEM as a Cloud Service supports [OpenTelemetry](/help/implementing/developing/introduction/opentelemetry-apm-integration.md). OTel is an open, industry-standard way to get traces, metrics, and logs together, sent to the APM provider of your choice.

Use this integration to:

* Investigate slow or failing requests
* Track JVM health and resource usage over time
* Build dashboards and alerts for your AEM tiers
* Correlate AEM behavior with other services during incidents

OpenTelemetry will be in Limited Availability on **October 1st**. To get on the list for access, email [aemcs-otel-access@adobe.com](mailto:aemcs-otel-access@adobe.com), describing your use case and how you intend on ingesting the data. 

#### AEM Query Optimization in the Code Assessment Agent Skill (IDE AI Tooling) {#code-assessment-skill}

AI coding agents (Claude Code, Cursor, GitHub Copilot, and similar tools) have broad knowledge of AEM’s underlying technologies, but don’t necessarily know best practices for generating and optimizing code or how to debug common AEM development issues. For this, Adobe provides installable agent skills, which instruct your coding agent. 

Available **October 1st**, one such skill – code assessment – has expanded its capabilities to include query optimization. It checks whether a JCR/Oak query is actually served by an index — and flags index definitions that look correct but are subtly misconfigured in ways that cause missed queries or silently incomplete results.

If interested in AI tooling for developers, consider watching the Adobe Developers Live 2026 session [*AI-Powered development with AEM CS & AEM Edge Functions*](https://www.youtube.com/watch?v=9SWWG3b3oNc).

#### New Capabilities in Cloud Migration Agent Skill {#cloud-migration-skill}

The [AI-Assisted Code Migration](/help/journey-migration/cloud-migration-skill/overview-cloud-migration-skill.md) skill migrates AEM 6.5 (or earlier) Java-stack projects to AEM as a Cloud Service in the IDE. The skill now generates a read-only migration runbook that assesses the whole project and lists every applicable pattern before it changes any code.

The skill now includes these patterns:

* Legacy UI: Classic UI, ExtJS, and Coral 2 dialogs convert to Coral 3, and custom ExtJS design widgets migrate to Granite UI.
* Template modernization: static templates convert to editable templates with AEM Modernize Tools rewrite rules.
* Guava cache to Caffeine: Guava cache usage switches to Caffeine, the supported Cloud Service cache library.
* Dispatcher configuration conversion: AMS and on-premise Apache HTTPD and Dispatcher configurations convert to the Cloud Service structure.
* Unsupported run mode (URC) detection: the skill flags OSGi configuration folders with unsupported run modes and reorders them safely where possible.
* Vault package dependency detection: the skill flags `filevault-package-maven-plugin` (or `content-package-maven-plugin`) configurations that are missing a `<dependencies>` block, which blocks Cloud Service package deploys.

Existing supported patterns include Sling Scheduler, ResourceChangeListener, Replication API, OSGi EventListener and EventHandler, Assets API, HTL lint fixes, and OSGi configuration conversion.

For more information, see [AI-Assisted Code Migration to AEM as a Cloud Service](/help/journey-migration/cloud-migration-skill/overview-cloud-migration-skill.md).

#### Permission Management Agentic Capabilities in AEM {#permission-management-in-aem}

Ask plain-language questions about who can do what on a content path, and the governance agent audits effective ACLs on your author environment in real time — explaining access decisions and their source policies, listing who holds a given privilege, pinpointing what causes a denial, and recommending groups for grants that follow the least privilege principle. For more information, see [Permission Management in AEM](/help/ai-in-aem/agents/governance/overview.md#permission-management-in-aem)‎

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Important Notices {#foundation-notices}

#### IMS Authentication Rich Errors {#ims-auth-rich-errors}

To help troubleshoot IMS integrations, `imsauth` has added support for *rich errors*.

Instead of returning only an HTTP status code, these errors provide additional context to help diagnose and resolve issues that can block authentication and access.

#### Java API Deprecations {#java-api-deprecation}

It is critical to remove usage of deprecated APIs before **September 28, 2026**.

Since **April 14, 2026**, Cloud Manager pipelines that contain code using APIs targeting 2/26/2026 removal **fail during the Code Quality** step. Deployments will be blocked until the deprecated API usage is removed. *This may prevent you from releasing time-sensitive updates and could impact your business operations.* 

Starting **September 28, 2026**, environments still using these deprecated APIs **will not receive critical Adobe release updates** and will not be subject to Adobe's standard commitments around performance and availability. As a result, you will not receive new features or bug fixes, application stability and uptime may be negatively affected, and security risk exposure may increase further.

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

#### Preparing for Java 25: AEM Cloud Service Runtime Upgrade Timeline

Java 25 is the next long-term support (LTS) release after Java 21, delivering improvements across performance, developer productivity, and security:

- **Performance** — Reduced memory footprint, more efficient garbage collection, and faster JVM warm-up benefit cloud-native deployments.
- **Developer productivity** — Cleaner object initialization, more expressive pattern matching, and simplified concurrent task management reduce boilerplate and improve code clarity.
- **Security** — Modernized cryptographic key derivation API to simplify common security workflows.

To help organizations plan testing and validation ahead of the necessary Java 25 runtime upgrade, Adobe is providing the following target dates. Any updates to this timeline will be communicated via release notes.

| Timeframe | Milestone |
|---|---|
| **Mid-October 2026** | AEM Cloud Service SDK supports Java 25 runtime. The Java 25 JDK is available for download from the Adobe Software Distribution portal. |
| **November 2026** | Customers are encouraged to optionally enable the Java 25 runtime in their Cloud environments to validate behavior. Early adoption maximizes time to surface and resolve issues. |
| **February – May 2027** | Adobe will gradually migrate lower environments (RDE, Dev) to the Java 25 runtime. Customers should validate behavior and report unexpected issues, and are encouraged to enable staging and production environments as well. A temporary rollback to Java 21 is available while resolving any problems. |
| **June 2027** | All environment runtimes (including staging and production) migrate to Java 25. Java 21 runtime is decommissioned. The AEM Cloud Service SDK will no longer support Java 21. |

AEM Cloud Service continues to support compiling customer code with Java 11, Java 17, and Java 21. However, Adobe recommends building with Java 25 (once available in AEM) to take full advantage of the latest language features and performance improvements.

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Early Adopter Features {#foundation-early-adopter}

#### Edge Authentication for Edge Delivery Services (Beta Program) {#edge-authentication}

Edge Authentication lets you restrict access to Edge Delivery Services pages to only those who have authenticated with your identity provider (IdP). This is achieved by deploying an OpenID Connect (OIDC) configuration YAML file.

If interested, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case and any questions you may have.

#### CX Enterprise Coworker: AEM Developer-Focused Capabilities (Beta Program) {#coworker-ai-troubleshooting-beta}

Today for developers, Coworker supports AI prompts to drive Cloud Manager. We're further expanding agentic AI support for developer use cases — troubleshooting, insights, and productivity — in areas including:

* **CDN and dispatcher** (e.g., *Why is my site slow? Why do I see stale content?*)
* **Replication** (e.g., *Why is my replication queue blocked?*)
* **Workflows** (e.g., *List any failed workflows*)
* **Code modernization** (e.g., *Propose a patch to replace deprecated APIs*)

To join the Beta Program, email [aem-devagent@adobe.com](mailto:aem-devagent@adobe.com) describing your interest.

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
