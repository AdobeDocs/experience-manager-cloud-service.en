---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service
description: Current release notes for [!DNL Adobe Experience Manager] as a Cloud Service.
mini-toc-levels: 2
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
feature: Release Information
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: ed762d86-a04b-452b-a08f-86359bb8ff27
    internal-label: Configuration and operations
subfeature_v2:
  - id: c21ccc2b-e0c8-4853-bf41-f12259ed93f8
    internal-label: Release information
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2026.10.0) is October 29, 2026. The next feature release (2026.11.0) is planned for November 19, 2026.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the May 2026 Release Overview video for a summary of the features added in the 2026.5.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3491490/?quality=12)

-->

## Release Overview {#overview}

The 2026.9.0 release of [!DNL Experience Manager] as a [!DNL Cloud Service] delivers new capabilities across Assets, Forms, and Foundation, with a continued emphasis on AI-assisted authoring and discovery, richer Dynamic Media experiences, and developer productivity.

**Highlights of this release**

* **Smarter Assets discovery and organization** — Content Hub adds AI Search for intent-based, multilingual results, Smart Collections that stay up to date automatically, and custom metadata sorting options.
* **Richer Dynamic Media experiences** — A new, fully customizable video viewer with actionable analytics, AI-generated video captions, multi-caption and multi-audio track support, and attribute-based access control for secure delivery.
* **AI-assisted authoring and development** — AEM agentic capabilities are now generally available in Adobe CX Enterprise Coworker, the AEM MCP Server adds Cloud Manager operations, and IDE agent skills expand with AEM query optimization and additional code-migration patterns.
* **Foundation and platform** — Canary deployments to validate a release against production before it serves live traffic, OpenTelemetry-based APM (Limited Availability), and IMS authentication rich errors for easier troubleshooting.
* **Plan-ahead notices** — Important timelines for Java API deprecations (September 28, 2026) and the upcoming Java 25 runtime upgrade help customers prepare their environments.

A range of beta, early adopter, and Limited Availability programs are also available this release. See the sections below for details.

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

This section highlights new and recently available capabilities for [!DNL Experience Manager Assets]. It includes features that became Generally Available (GA) in the current release, as well as features that are currently in Limited Availability (LA) or Beta. LA and Beta features remain listed in this section until they become generally available.

### [!DNL Experience Manager] as a [!DNL Cloud Service] Assets Limited Availability Features {#assets-limited-availability-features}

#### Native Dynamic Media Template component in Adobe Journey Optimizer {#dynamic-media-component-ajo}

The native Dynamic Media Template component lets marketers add and personalize AEM Dynamic Media templates directly in the Adobe Journey Optimizer email editor. Marketers can select existing templates or import layered PSD files, edit individual layers such as countdown timers, and configure text, CTAs, positioning, and timing without leaving the email editor. This enables governed, personalized, and dynamic email experiences, including open-time countdowns and personalized product content.

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

#### Content Hub: Smart Collections {#smart-collections}

Smart Collections enable you to automatically organize assets based on defined search criteria.
When you create a Smart Collection, the collection stores the search query and filter criteria instead of storing individual assets. Assets that match the configured criteria are automatically displayed in the collection.

Smart Collections automatically remain up to date. When newly approved assets satisfy the configured search criteria, they are automatically added to the collection.

>[!VIDEO](https://video.tv.adobe.com/v/3503809)


### [!DNL Experience Manager] as a [!DNL Cloud Service] Assets Beta Features {#assets-beta-program-features}

#### Content Advisor browser extension {#content-advisor-browser-extension}

Use the power of AEM Content Advisor for AEM Assets, in the application of your choice with the browser extension available [here](https://chromewebstore.google.com/detail/aem-content-advisor/hgagfaikdinmneghfgjjocmfidmnadga).

**Why you will love it?**

* **Zero setup, zero code.** Install it, sign in, and start working. No integration, no custom connectors, no developer tickets.

* **Smarter suggestions, on your terms.** Recommendations come from the whole page, or narrow them by selecting a region, highlighting text, or choosing an image. The more precisely you point, the sharper the results.

* **Pick exactly what you need.** Choose any asset or any Dynamic Media rendition (the right size, format, or crop) and send it straight to your editor. Insert, drag and drop, or copy URL to the clipboard.

* **Works where you author.** AEM (Cloud Service, Adobe Managed Services, or On-premise), other Adobe CX Enterprise products (where AEM Assets native integration does not exist), and third-party tools such as Google Docs/WordPress/Microsoft Powerpoint, and any other web application.

For more information, see [Use AEM Content Advisor with the browser extension](/help/assets/content-advisor-browser-extension.md).


To send feedback, participate or learn more, send an email to `aem-content-advisor-feedback@adobe.com`.


#### Dynamic Media: Video Engagement Report {#video-engagement-report}

Turn video playback into actionable insight by providing per-video engagement metrics for the New Video Viewer, including views, impressions, watch time, completion rate, and engagement score, delivered as a monthly CSV to help teams measure content performance.

To participate or learn more, send an email to `dm-beta-feedback@adobe.com`.

#### Dynamic Media: Operations and Error Report {#operations-and-error-report}

Give teams visibility into delivery health by reporting operational activity such as delivery request counts, smart crops, video encodes, and templates created, while surfacing failed delivery URLs with their referrer and failure count so issues can be pinpointed and fixed.

To participate or learn more, send an email to `dm-beta-feedback@adobe.com`.

#### Dynamic Media Template: Auto Translate {#auto-translate}

Eliminate repetitive manual localization by using AI to automatically translate text and turn a single master template into variants across multiple locales, while preserving the visual integrity of your designs.

To participate or learn more, send an email to `dm-beta-feedback@adobe.com`.

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

#### Dispatcher Insights and Workflow Inspection Agentic Capabilities in CX Enterprise Coworker {#capabilities-cx}

Two new developer-related agentic capabilities are now generally available in [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview). Developers and administrators can use them to investigate workflow activity and dispatcher behavior in AEM as a Cloud Service in plain language, without opening the user interface or searching log files by hand.

[**AEM Workflow Inspection**](/help/ai-in-aem/agentic-capabilities/brand-experience/development/use-cases.md#aem-workflow-inspection) lets you check on workflow activity directly from Coworker. Ask which workflows are running or suspended, get a status summary, see what's waiting in your workflow inbox, or find out why a workflow failed. You can look up a specific workflow, browse available workflow models, and ask follow-up questions as you troubleshoot.

Example prompts:

- *What workflows are running?*
- *Are any running or suspended workflows showing recorded errors?*
- *What's in my workflow inbox?*

[**AEM Dispatcher Insights**](/help/ai-in-aem/agentic-capabilities/brand-experience/development/use-cases.md#aem-dispatcher-insights) helps you understand how your Dispatcher and Apache web tier handle requests. Coworker can analyze cache performance, investigate traffic and delivery issues, and review your security configuration. It covers three areas:

- **Caching and performance:** includes dispatcher cache hit ratio insights, query-parameter caching, cache headers and expiration, stale content and invalidation, slow responses.
- **Traffic and request handling:** includes traffic patterns and bots, 4xx and 5xx errors, filter and endpoint routing, multi-site and hostname routing, redirects and vanity URLs, and header forwarding.
- **Security:** includes sensitive-path exposure, security headers, permission-sensitive caching, and an overall review of your Dispatcher configuration.

Example prompts:

- *Summarize Dispatcher cache performance for production today and compare it with yesterday.*
- *Why is this page still showing old content after publication?*
- *Investigate the intermittent 502 and 503 responses in production between 10:00 and 11:00 UTC today.*

#### New capabilities in AEM MCP {#aem-mcp}

[AEM MCP Server](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md) allows you to configure a single URL in your chat application or coding agent to access a growing set of capabilities. 

In addition to Content operations (pages, content fragments, and assets) and Experience Governance checks, AEM MCP now supports Cloud Manager operations to manage programs, environments, and pipelines.

Cloud Manager operations were previously only available through the deprecated domain-specific MCPs. Customers using those should switch to the AEM MCP Server.

The AEM MCP Server is also used by the [AEM Claude Connector](/help/ai-in-aem/mcp-support/setup-claude.md#install-adobe-experience-manager-connector) and [AEM ChatGPT Plugin](/help/ai-in-aem/mcp-support/setup-chatgpt.md#install-adobe-experience-manager-plugin).

<!--

- Cloud Migration: fetch Best Practices Analyzer (BPA) findings from Cloud Acceleration Manager (CAM) by migration pattern or severity level, enabling AI agents to drive code migration from AEM 6.x to AEM as a Cloud Service. 

-->

#### OpenTelemetry for Application Performance Monitoring (APM) (Limited Availability) {#otel}

Now in Limited Availability (see note below for access), AEM as a Cloud Service supports [OpenTelemetry](/help/implementing/developing/introduction/opentelemetry-apm-integration.md). OTel is an open, industry-standard way to get traces, metrics, and logs together, sent to the APM provider of your choice. Also see advanced [custom instrumentation](/help/implementing/developing/introduction/opentelemetry-custom-instrumentation.md) documentation and [tutorials](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/observability-via-opentelemetry/opentelemetry-in-aem).

To get on the list for access, email [aemcs-otel-access@adobe.com](mailto:aemcs-otel-access@adobe.com), describing where you intend on ingesting the data. 

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Important Notices {#foundation-notices}

#### IMS Authentication Rich Errors {#ims-auth-rich-errors}

To help troubleshoot IMS integrations, `imsauth` has added support for *rich errors*.

Instead of returning only an HTTP status code, these errors provide additional context to help diagnose and resolve issues that can block authentication and access.

#### Mandatory migration from Adobe’s built-in APM integration (New Relic) to OpenTelemetry {#otel-migration|

OpenTelemetry is replacing Adobe’s built-in APM integration (New Relic), which will be disabled at the end of **November 2026**. If your organization is using the built-in New Relic APM integration, see the [FAQ](/help/implementing/developing/introduction/opentelemetry-apm-integration.md#faq) for more information.

#### Winter 2027 Java API Deprecations {#java-api-deprecation}

In **April 2027**, a set of deprecated Java APIs will be removed and it is critical to take action in order to achieve security compliance. Applications that have not removed APIs will not receive new features or bug fixes, and application stability and uptime may be negatively affected, and security risk exposure may increase.

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

<!--

#### Jackson bundle upgrade affects the GlobalLink connector {#jackson-upgrade-globallink-connector}

AEM 6.5 LTS SP3 upgrades the Jackson bundle. This change affects deployments that use the GlobalLink translation connector.
 
If you use the `gs4tr-globallink-adaptors-aem.core` bundle at a version earlier than 3.4.4.7, upgrade the bundle to a compatible version. Version 3.4.4.7 or later works with the upgraded jackson bundle in SP3.
 
>[!NOTE]
>
>Upgrade the `gs4tr-globallink-adaptors-aem.core` bundle to 3.4.4.7 or later before or during the SP3 update to avoid compatibility issues with the GlobalLink connector.

-->

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


#### CX Enterprise Coworker: Developer-Focused Capabilities (Beta Program) {#coworker-ai-troubleshooting-beta}

Today for developers, Coworker supports AI prompts to drive Cloud Manager. We're further expanding agentic AI support for developer use cases — troubleshooting, insights, and productivity — in areas including:

* **CDN ** (e.g., *Did my site experience any traffic spikes?*, *What's my cache hit ratio?*)
* **Replication** (e.g., *Why is my replication queue blocked?*)
* **Code modernization** (e.g., *Propose a patch to replace deprecated APIs*)

To join the Beta Program, email [aem-devagent@adobe.com](mailto:aem-devagent@adobe.com) describing your interest.

#### mTLS Authentication for Log Forwarding (Beta Program) {#mtls-log-forwarding-beta}

Log Forwarding now supports mutual TLS (mTLS) client certificate authentication for Splunk, Elasticsearch/OpenSearch, and HTTPS destinations, for both AEM logs (including Apache/Dispatcher) and CDN logs. AEM as a Cloud Service presents a client certificate when it connects to your logging destination, so the destination can verify that the logs come from your environment.

mTLS for Log Forwarding is in beta. To join the Beta Program, email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) with your program ID and environment IDs. Learn more in the [log forwarding documentation](/help/implementing/developing/introduction/log-forwarding.md#mtls).

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
