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
>From here, you can navigate to release notes of previous versions such as 2023 or 2024.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2026.4.0) is April 30, 2026. The next feature release (2026.5.0) is planned for May 28, 2026.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 
## Release Video {#release-video}

Have a look at the April 2026 Release Overview video for a summary of the features added in the 2026.4.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3483060/?quality=12)
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

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### AI Translation Integration {#ai-translation-integration}

AEM users can now leverage Large Language Models (LLMs) for content translation, delivering human-translaton quality at machine translation speed. Similar to traditional third-party translation services, Azure OpenAI can be configured as a translation provider in AEM, with support for additional LLMs planned for future releases. Customers use their own LLM licenses for this capability. Additionally, corporate translation style guides can be uploaded to AEM, enabling the extraction of translation rules to ensure brand and style consistency. See [Configuring AI Translation Integration](/help/sites-cloud/administering/translation/ai-translation-integration.md) for more information.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

**Content Advisor in AEM Sites**

Content Advisor is now available in AEM Sites, introducing intelligent asset discovery from AEM Assets directly. It enables users to effortlessly discover, browse, and reuse the most relevant assets directly within their workflow, eliminating the need to switch contexts.

Content Advisor provides intelligent features for assets such as campaign brief based suggestions, contextual suggestions, access to Dynamic Media renditions, and detailed asset metadata.

Coming soon - Content Advisor support for Adobe Workfront and AJO B2C applications, including ability to discover Content Fragments

### New Features in Dynamic Media {#dynamic-media-new-features}

#### Dynamic Media Template Editor updates {#dynamic-media-template-editor-updates}

**Layer Management Enhancements**

* Drag-and-Drop Layer Reordering: Layers can now be reordered directly in the Layers panel by dragging, providing a faster and more intuitive way to organize layer stacking order beyond the existing Bring Forward or Send Backward actions.
* Copy, Paste & Duplicate: Full support for copying, pasting, and duplicating layers using keyboard shortcuts (Cmd/Ctrl+C, V, D) or the context menu, with support for multi-layer selections.
* Separate Layer Properties Button: Added dedicated Layer Properties button for easier navigation to layer settings, with double-click support on layers for quick access.

**Text Formatting Features**

* Line Spacing Control: New line spacing slider enables precise control over line height in text layers, with full end-to-end support including undo/redo and template save/load.
* All Caps Formatting: Text layers now support All Caps formatting option in the Font Style toolbar alongside Bold, Italic, and Underline.
* Vertical Alignment Options: Added vertical alignment controls for text layers, providing more precise text positioning within text boxes.

**Size & Dimension Controls**

* Aspect Ratio Unlock: Users can now unlock aspect ratio when adjusting size properties, allowing independent width and height adjustments for more flexible layer sizing.
* Copyfit Lines Configuration: Added support for `copyfitlines` and `copyfitmaxlines` settings in text copyfit properties, providing finer control over text fitting behavior.

**Visual Polish**

* Updated icons for Timer and Shape layers with refined Spectrum 2 (S2) design system icons.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### Early Access Features in AEM Forms {#forms-early-access-features}

**Display labels for multi-select dropdown in Submission PDF**
Multi-select dropdown components in Adaptive Forms now render their selected display labels in the [generated Submission PDF](/help/forms/generate-document-of-record-core-components.md), ensuring the document accurately reflects what users see on the form.

**Enhanced accessibility for checkbox, radio button, and panel components**
Adaptive Forms Core Components introduce WCAG 2.2 -compliant semantic markup for [checkbox groups(v2)](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/checkbox-group), [radio button groups(v2)](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/radio-button), and the [Panel component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel). These components leverage `<fieldset>` and `<legend>` HTML elements to establish meaningful relationships between group labels and their options, enabling accurate interpretation by screen readers and other assistive technologies.

**Versioning support in Forms Manager**
Forms Manager now [supports versioning for Adaptive Forms (Core Components and Foundation Components)](/help/forms/manage-form-versions-forms-manager.md), form fragments, themes, XDP templates, and binary assets. Create versions, view complete version history, and restore earlier states of your form assets directly from the Forms & Documents console.
  
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation New Features {#foundation-new}

#### IDE AI tooling for AEM Java and Dispatcher Development {#ai-dev}

Java-stack teams are increasingly using AI-assisted development in tools such as Cursor, Claude Code, Visual Studio, and IntelliJ to speed up feature delivery and improve code quality. 

IDE tooling can be used by coding agents to generate and debug AEM code and dispatcher configuration. As one example, the video walkthrough below demonstrates building an AEM component using Agent Skills.  

Learn more about [Local Development with AI Tools](/help/ai-in-aem/local-development-with-ai-tools.md) and feel free to email [aemcs-ai-ide-tools-feedback@adobe.com](mailto:aemcs-ai-ide-tools-feedback@adobe.com) with questions or feedback.


>[!VIDEO](https://video.tv.adobe.com/v/3484978/?learn=on&enablevpops)

#### Experience Governance MCP Server {#gov-mcp-server}

The Experience Governance MCP Server is now generally available (GA). It integrates with AI developer tools and chatbots that support the Model Context Protocol (MCP), allowing you to safeguard brand integrity and compliance using natural language prompts in your chatbot or IDE. You can evaluate content (text, images, pages) against brand governance rules, and retrieve brand configurations and available governance checks.

Learn more about [AEM MCP Servers](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md) and the [Governance Agent](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/ai-in-aem/agents/governance/overview).

#### AEM OIDC on Publish New Features {#aem-oidc-on-publish-new-features}

* Fix: Query parameters from original request are lost after authentication
* Custom Redirect After Authentication in OIDC Authentication [documentation](/help/security/open-id-connect-support-for-aem-as-a-cloud-service-on-publish-tier.md#custom-redirect-after-authentication)

#### Mail Service support for Microsoft Graph API {#mail-service-graph-api}

AEM's Mail Service now supports Microsoft&reg; Outlook (via Microsoft 365) using the Microsoft Graph API. This is particularly helpful for organizations that do not allow SMTP, which is already supported by the Mail Service. Authentication is via OAuth 2.0. [Learn how to configure](/help/security/oauth2-support-for-mail-service.md#microsoft-graph-api).

#### CDN Logs can be Forwarded to Sumo Logic {#sumo-cdn-logforwarding}

The [Log Forwarding feature](/help/implementing/developing/introduction/log-forwarding.md#sumologic) now supports sending CDN logs to Sumo Logic. Previously, log forwarding to Sumo Logic was limited to AEM logs.

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Important Notices {#foundation-notices}

#### IMS Authentication Rich Errors {#ims-auth-rich-errors}

To help troubleshoot IMS integrations, `imsauth` has added support for *rich errors*.

Instead of returning only an HTTP status code, these errors provide additional context to help diagnose and resolve issues that can block authentication and access.

#### Java API Deprecations {#java-api-deprecation}

It is critical to remove usage of deprecated APIs. 

Since **April 14**, Cloud Manager pipelines that contain code using APIs targeting 2/26/2026 removal **fail during the Code Quality** step. Deployments will be blocked until the deprecated API usage is removed. *This may prevent you from releasing time-sensitive updates and could impact your business operations.* 

Starting **June 11, 2026**, environments still using these deprecated APIs **will not receive critical Adobe release updates** and will not be subject to Adobe's standard commitments around performance and availability. As a result, you will not receive new features or bug fixes, application stability and uptime may be negatively affected, and security risk exposure may increase further.

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

#### AEM Edge Functions (Beta Program) {#edge-functions}

[AEM Edge Functions](/help/implementing/developing/introduction/edge-functions.md) allows you to execute JavaScript at the CDN layer, bringing data processing closer to the end user. This reduces latency and enables responsive, dynamic experiences at the edge.

Common use cases include:

* Personalizing content based on geolocation, device type, or user attributes
* Acting as middleware between the CDN and your origin
* Reformatting responses from third-party APIs (and perhaps aggregating multiple API responses) before delivering them to the browser
* Composing and serving server-rendered HTML at the edge using content stitched from various backends
* Exposing an MCP server for AI Assistants like ChatGPT and Claude to access custom tools

We have a limited number of opportunities available for either AEM Publish Delivery or Edge Delivery Services projects for live production sites. If you're interested in participating or want to learn more, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case.

#### Web Tier Config Pipeline Troubleshooting (Beta Program) {#devagent-webtier}

The Development Agent's [pipeline troubleshooting](/help/ai-in-aem/agents/brand-experience/development/development.md) capabilities help developers efficiently diagnose and resolve issues in AEM as a Cloud Service deployments. In addition to supporting Full Stack pipelines (Deployment and Code Quality), the Development Agent now supports troubleshooting for the **Web Tier Config Pipeline** as part of a beta program.

To request access to the beta, email [aem-devagent@adobe.com](mailto:aem-devagent@adobe.com). Pre-existing access to Agents in AEM is required.

#### Replication AI Troubleshooting (Alpha Program) {#replication-ai-troubleshooting-alpha}

Using the AI Assistant in AEM Author and other interfaces, you can troubleshoot replication-related issues such as blocked queues. To join the Alpha Program, email [aem-devagent@adobe.com](mailto:aem-devagent@adobe.com), describing your interest.

#### IDE AI tooling for AEM 6.5 to AEM Cloud Service Migration (Beta Program) {#cm-ide-migration}

Accelerate your migration from AEM 6.5 to AEM as a Cloud Service (Java stack) by using IDE AI tooling to act on the recommendations of the [Best Practices Analyzer Report](/help/journey-migration/best-practices-analyzer/overview-best-practices-analyzer.md).

Email [aemcs-ai-ide-tools-feedback@adobe.com](mailto:aemcs-ai-ide-tools-feedback@adobe.com) for more information and to request access to the feature.

#### AI code migration tool for AEM 6.5 to AEM 6.5 LTS Migration (Alpha Program) {#ai-lts-migration-alpha}

AEM 6.5 customers migrating to AEM 6.5 LTS can use AI tooling in Cloud Manager that generates code to reduce the development effort to the feature.

Email [aem-lts-ai-migration@adobe.com](mailto:aem-lts-ai-migration@adobe.com@adobe.com) for more information and to request access.

#### Edge Authentication for Edge Delivery Services (Beta Program) {#edge-authentication}

Edge Authentication lets you restrict access to Edge Delivery Services pages to only those who have authenticated with your identity provider (IdP). This is achieved by deploying an OpenID Connect (OIDC) configuration YAML file.

If interested, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case and any questions you may have.

#### Canary Production Deployments to Test Code Before Accepting Live Traffic (Beta Program) {#canary-beta}

Validate a production build with internal-only test traffic before exposing it to end users. Ship to production, route only canary traffic (using a special header), monitor behavior, then either promote to live traffic or roll back—without impacting customers.

Email [aemcs-canary-deployments-beta@adobe.com](mailto:aemcs-canary-deployments-beta@adobe.com) to request access and share feedback.

#### Snapshots for RDEs (Beta Program) {#rde-snapshot-program}

In beta, Rapid Development Environments (RDEs) now support a feature [to take a snapshot](/help/implementing/developing/introduction/rapid-development-environments.md#snapshots) of the current state of code and content, which can be restored at a later time. This can be useful when syncing code that may need to be reverted, or when switching between development of different features. It's also possible to restore just the mutable content as a known starting point for testing.

Please email [aemcs-rde-support@adobe.com](mailto:aemcs-rde-support@adobe.com) if there is interest in using and providing feedback on this feature.

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
