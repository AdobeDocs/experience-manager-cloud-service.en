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

AEM users can now leverage Large Language Models (LLMs) for content translation, delivering human-translation quality at machine-translation speed. Similar to traditional third-party translation services, Azure OpenAI can be configured as a translation provider in AEM, with support for additional LLMs planned for future releases. Customers use their own LLM licenses for this capability. Additionally, corporate translation style guides can be uploaded to AEM, enabling the extraction of translation rules to ensure brand and style consistency. See [Configuring AI Translation Integration](/help/sites-cloud/administering/translation/ai-translation-integration.md) for more information.

### Content Fragment Editor {#cf-editor}

The new Content Fragment Editor now allows you to preview the JSON representation of a content fragment. This helps validate the content structure independently of rendering and restores parity with the previous Content Fragment Editor in AEM Touch UI for this capability.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

**Content Advisor now available for Adobe Workfront and non-Adobe applications**

Content Advisor is now available for Adobe Workfront and non-Adobe (third-party) applications, extending intelligent asset discovery and content reuse beyond Adobe Express and AEM Sites. This release brings the full Content Advisor experience, including AI-powered search, context-aware recommendations, campaign brief–based discovery, access to Dynamic Media renditions, Content Fragment discovery, filters, and asset metadata to Adobe Workfront workflows and external applications.

You can now discover, evaluate, and reuse approved assets from AEM Assets directly within your preferred applications, enabling consistent asset usage, improved efficiency, and streamlined content creation across both Adobe and non-Adobe applications.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New Features in AEM Forms

* **Override reCAPTCHA cloud configuration with OSGi**  
reCAPTCHA Enterprise project IDs, site keys, and secrets that you keep with your source files can resolve to different values on each Cloud Service environment after you [add the Context-Aware Configuration override and deploy through Cloud Manager](/help/forms/captcha-adaptive-forms.md#override-recaptcha-osgi).

* **Certificate-based authentication**  
Adaptive Forms that submit to a Microsoft SharePoint list now support [certificate-based authentication](/help/forms/connect-forms-to-sharepoint-list.md#certificate-based-authentication) alongside OAuth URL authentication. For certificate-based sign-in, register a certificate alias and tenant details in AEM and Microsoft Azure.

* **Rule Editor Enhancements**

  * The Adaptive Forms rule editor now supports the simplified grammar for [Dispatch Event and On Trigger Event rules for out-of-the-box (OOTB) triggers and for custom events](/help/forms/rule-editor-enhancements-use-cases.md#simplified-grammar-for-ootb-and-custom-events), so authors are not limited to grammar on custom triggers only. 
  * When rules on Adaptive Forms based on Core Components now include the [File Attachment component together with other conditions using AND or OR logic](/help/forms/rule-editor-enhancements-use-cases.md#combined-when-conditions-with-the-file-attachment-component), so the rule runs its actions only when the attachment state and the other checks all evaluate as intended.
  
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


>[!VIDEO](https://video.tv.adobe.com/v/3486258/?learn=on&enablevpops)

#### Claude Connector {#aem-claude-connector}

Claude users can browse Anthropic’s [Connector marketplace](https://claude.ai/settings/connectors) to 1-click install the [Adobe Experience Manager Connector](/help/ai-in-aem/mcp-support/setup-claude.md#aem-claude-connector). This MCP server exposes a growing set of tools to interact with AEM, including editing content through prompting.

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
