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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2026.1.0) is January 29, 2026. The next feature release (2026.2.0) is planned for February 26, 2026.

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

Customers selected for participation will be notified directly by Adobe. Participation is subject to eligibility considerations, including customer licensing and limited program capacity. While not all requests can be accommodated initially, additional customers may be considered in future beta waves.

### AEM Foundation (Beta programs) {#aem-foundation-beta-programs}

See [AEM Foundation beta programs](#foundation-early-adopter).

### Cloud Manager (Beta programs) {#cloud-manager-beta-programs}

See [Cloud Manager beta programs](/help/implementing/cloud-manager/release-notes/current.md).

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### Content MCP Server {#content-MCP}

AEM Cloud Service now includes **Content MCP Servers**, providing a standardized way for AI-powered experiences to work with AEM content through MCP-compatible tools.

Developers and power users working in chat apps and agent platforms can connect AEM to custom copilots and automations, so content work becomes part of end-to-end business workflows.

AEM provides two servers:

1. **Read-only Content MCP Server** - for retrieving content safely
1. **Read/Write Content MCP Server** - for making changes to content

These MCP servers include tools for working with **Pages**, **Content Fragments**, and **Assets**, and can be used from the following MCP clients: **ChatGPT**, **Claude**, **Cursor**, and **Microsoft Copilot Studio**.

Learn more in [Using MCP with AEM Cloud Service](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md). For questions or feedback, email [aemcs-mcp-feedback@adobe.com](mailto:aemcs-mcp-feedback@adobe.com).

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

**AI Search**

AI Search introduces an intelligent, context-aware search experience that goes beyond traditional keyword matching by understanding the meaning and intent behind user queries. Powered by AI and machine learning, it delivers more accurate results even when queries are phrased differently, contain misspellings, use synonyms, or are submitted in different languages, helping users find relevant content faster with less effort.

For more information, see AI Search in [Assets view](/help/assets/search-assets-view.md#ai-search) and [Admin view](/help/assets/search-assets.md#ai-search).

**Desktop App 3.0.1 release**

[Desktop App 3.0.1 (December 20, 2025)](https://experienceleague.adobe.com/en/docs/experience-manager-desktop-app/using/release-notes) improves reliability, performance, and stability across key workflows. This release ensures consistent folder naming by fixing sync issues with AEM Author, allows uninterrupted use of the app during active transfers, enhances UI responsiveness through asynchronous processing, optimizes large file transfers with pagination, and resolves stability issues including Author server restarts and crashes during large folder uploads and downloads.

**Adobe Asset Link CEP 2026.01.0 release**

 [Adobe Asset Link CEP 2026.01.0](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html) introduces a new Relink missing links option in InDesign that automatically relinks other missing assets from the same AEM folder. The feature matches assets based on filename, significantly reducing manual effort when restoring broken links.


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

**Enhancements to the Footnote Placeholder in Adaptive Forms (Foundation Components)**

* Added [multi-line support with line breaks](/help/forms/footnotes-richtextsupport.md), enabling clearer and more expressive presentation of footnote content.
* Footnotes now remain persistently visible within the Footnote Placeholder, regardless of the visibility of associated panels, ensuring consistent access to critical information.
   ![Footnote Description](/help/forms/assets/footnote-description.png){height=50%}

### New Early Access Features in AEM Forms {#forms-new-early-access-features}

**Retrieve values from a JSON array**

Expanded custom function capabilities to [extract values from JSON arrays](/help/forms/invoke-service-enhancements-rule-editor.md#retrieve-property-values-from-a-json-array), received via an API call, and bind them directly to Adaptive Form fields. You can now develop business logic and rules with minimal manual data mapping.

**Run the Associate UI on a Publish instance**

You can now run the [Associate UI](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md) directly on Publish instances. This allows your agents to access the Associate UI and easily personalize communications for your customers.

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

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Important Notices {#foundation-notices}

#### Java API Deprecations {#java-api-deprecation}

The deprecated APIs targeting 2/26/2026 removal should no longer be used in code. To prevent deployment blocks, remove API usage before March 26, 2026. Important dates:

* **Starting January 26, 2026**: Actions Center notification emails are sent **weekly per environment** as a reminder to remove usage of these APIs.
* **February 26, 2026**: Cloud Manager pipelines that contain code using these APIs will **pause** during the **Code Quality** step. A Deployment Manager, Project Manager, or Business Owner can override the issue to allow the pipeline to proceed.
* **March 26, 2026**: Cloud Manager pipelines that contain code using these APIs will **fail** during the **Code Quality** step, **blocking deployments** of new code until the usage is removed.
* **April 30, 2026**: Environments still using these APIs may **no longer receive critical Adobe release updates**.

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

Adobe upgraded **Stage** and **Production** environments to the higher-performance **Java 21 runtime** on October 14th, 2025. Starting **February 9th** (gradual rollout through February 11th), neither the AEM Cloud Service SDK nor any cloud environments will work with Java 11 runtime.

>[!NOTE]
>
> To take advantage of the latest performance optimizations and language enhancements, it is recommended to build with Java 17 or Java 21  (preferred). Building with Java 8 and Java 11 remains supported for now but will be deprecated in an upcoming release. A separate communication will be issued prior to deprecation. See the *build time requirements* section of [this article](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#runtime-requirements).
>

#### Enforcement of AEM Java Logs Configuration Policy {#logconfig-policy}

AEM Java logs must follow a standard format to ensure reliable monitoring across all customer environments. Custom log configurations—such as changes to log formatting, output files, or default log levels—are no longer supported. Logs must remain directed to the default files, and default log levels for AEM product code must be preserved. See full details in the [Logging article](/help/implementing/developing/introduction/logging.md#configuration-loggers).

Any unsupported custom logging overrides *are now ignored*. Most customers were not impacted and Adobe has contacted customers whose current configuration may be affected.

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

#### AEM Edge Functions (Beta Program) {#edge-functions}

AEM Edge Functions (referred to in earlier release notes as *Edge Computing*) allows you to execute JavaScript at the CDN layer, bringing data processing closer to the end user. This reduces latency and enables responsive, dynamic experiences at the edge.

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

Please email [aemcs-rde-support@adobe.com](mailto:aemcs-rde-support@adobe.com) if there is interest in using and providing feedback on this feature.

#### AI tooling for IDEs for AEM Java and Dispatcher Development (Beta Program) {#ai-dev-beta}

Java-stack teams are increasingly using AI-assisted development in tools such as Cursor, Claude Code, Visual Studio, and IntelliJ to speed up feature delivery and improve code quality. Join the beta to:

* Share real-world experiences to help shape future Adobe-supported AI capabilities
* Try out IDE tooling that can be used by AI agents to generate and debug AEM code and dispatcher configuration

Email [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com) for more information.

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
