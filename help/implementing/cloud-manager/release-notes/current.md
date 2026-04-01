---
title: Release Notes for Cloud Manager 2026.4.0
description: Learn about the release of Cloud Manager 2026.4.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2026.4.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- https://wiki.corp.adobe.com/display/DMSArchitecture/%5BKT%5D+Cloud+Manager+2025.08.0+Release -->

Learn about the release of Cloud Manager 2026.3.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2026.4.0 in AEM as a Cloud Service is Thursday, April 2, 2026. 

The next planned release is Thursday, May 7, 2026.


## What's new - Cloud Manager {#cloud-manager-whats-new}

* **Cloud Manager MCP server for AI-powered IDEs**

    You can now use an MCP (Model Context Protocol) server that exposes Cloud Manager Public APIs as tools for AI-enabled IDEs (such as Cursor). After you connect it, you can use conversational prompts to list and manage programs, pipelines, environments, and repositories, helping you move faster without leaving your editor.

    See the documentation [Use MCP with AEM as a Cloud Service](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md).

    See the tutorial [Cloud Manager MCP Server](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/ai/mcp-servers/cloud-manager#).

* **Faster builds with module caching**

    A new build model compiles only changed modules (rather than the entire repo) using module-level caching to shorten build times. It applies to Code Quality non-production pipelines and development Full Stack non-production pipelines.

    See [About using Smart Build in a non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#about-smart-build) and [Add a non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#full-stack-code).

* **Self-serve host connectivity check**

    Cloud Manager now lets you run self-serve checks from your environment. These checks verify host and port reachability and confirm DNS resolution using your program's configured network path, including egress. This capability helps you validate advanced networking and resolve integration issues faster without opening support cases or accessing pods. <!-- SKYOPS-23640 -->

    <!-- See [Network Connectivity Test](/help/security/network-connectivity-test.md) -->

* **Improved stability, performance, and reliability**

    This release includes optimization and maintenance updates that improved the stability, performance, and reliability of Cloud Manager.


## Beta programs {#private-beta-program}

Participate in Cloud Manager's beta programs to get exclusive access to upcoming features before their general release.

>[!IMPORTANT]
>
>Beta releases may contain defects and are provided "AS IS" without warranty of any kind. Adobe has no obligation to maintain, correct, update, change, modify or otherwise support (by way of Adobe Support Services or otherwise) the beta releases. Adobe advises customers to use caution and not rely on the correct functioning or performance of beta releases, or on any accompanying documentation or materials. Features and APIs in beta are subject to change without notice. Accordingly, any use of the beta releases is entirely at the customer's own risk.

See also [AEM Beta programs](/help/release-notes/release-notes-cloud/release-notes-current.md#aem-beta-programs)

The following opportunities are currently available:

### Edge Delivery Services with AEM Authoring and flexible publish tier configuration {#eds-with-aem-authoring}

Cloud Manager introduces two capabilities designed to support modern delivery architectures.

* **Edge Delivery Services with AEM Authoring**
You can now deliver sites using Edge Delivery Services while continuing to author content in AEM Author mode. Depending on your workflow preferences, you can choose between the following authoring approaches:

    * Document-based authoring
    * AEM Author-based authoring

For more information, see [Create Edge Delivery site in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md#one-click-edge-delivery-site).

* **Flexible publish tier configuration**
Cloud Manager now lets you configure whether a publish tier is required for your program. This flexibility lets you set up environments that better match your chosen delivery architecture.

For more information, see [Flexible Publish Tier (Beta)](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#flexible-publish-tier).

To join the Beta, email [grp-beta_xwalk-publish_config@adobe.com](mailto:grp-beta_xwalk-publish_config@adobe.com) with your Adobe Organization ID and Program ID.

### Faster builds with module caching {#quick-build-cm-pipelines}

A new build model compiles only changed modules (rather than the entire repository) using module-level caching to shorten build times. It applies to production pipelines. You control which production pipelines use **Smart Build**.

For more information, see the following:

* [Using Smart Build in a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#about-smart-build).
* [Add a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#full-stack-code).

To join the Beta, email [beta_quickbuild_cmpipelines@adobe.com](mailto:beta_quickbuild_cmpipelines@adobe.com) with your Adobe OrgID and Program ID.

<!-- OLD
### Experience Hub Extensibility and Customization {#exp-hub-extensibility}

[Experience Hub](/help/experience-hub.md) serves as your entry point to AEM, customized for your organization's needs. Tell Adobe about your existing AEM UI Extensions so they can help you enable them in Experience Hub with minimal effort.

![Diagram of Experience Hub extensibility and customization workflow](/help/implementing/cloud-manager/release-notes/assets/experience-hub-extensibility-customization.png)

Embed custom experiences in Experience Hub to extend and personalize your organization's dashboard. In addition to Adobe's built-in widgets, add your own using the [UI Extensibility](https://developer.adobe.com/uix/docs/) framework. Build JavaScript-based UI apps and surface them to your users to meet business-specific requirements and workflows. 

Interested in the beta? Email [beta_exphubextensibility@adobe.com](mailto:beta_exphubextensibility@adobe.com) with your Adobe OrgID and a short description of the customization you intend to create.
-->

<!-- OLD
### Support for Custom Author Domains in Cloud Service

AEM Cloud Service is going to soon support one custom domain per Author environment.
-->



## Bug fixes {#bug-fixes}

There are no significant bug fixes in the April 2026 Cloud Manager release.

<!-- ## Known issues {#known-issues} -->

