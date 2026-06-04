---
title: Release Notes for Cloud Manager 2026.6.0
description: Learn about the release of Cloud Manager 2026.6.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2026.6.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- 
https://wiki.corp.adobe.com/display/DMSArchitecture/%5BKT%5D+Cloud+Manager+2025.08.0+Release 
-->

Learn about the release of Cloud Manager 2026.6.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2026.6.0 in AEM as a Cloud Service is Thursday, June 4, 2026. 

The next planned release is Thursday, July 9, 2026.


## What's new - Cloud Manager {#cloud-manager-whats-new}

* **Customer-managed keys (CMK) self-service**
    Customers can now configure Customer-Managed Keys directly from Cloud Manager, without requiring Adobe support involvement. A new CMK option is available during program creation, in program edit settings, and on the Environment details page.

    CMK status is displayed on program cards.

    
    
    
    
    
     and in the license dashboard, giving administrators clear visibility into encryption configuration across all environments. This simplifies compliance workflows for organizations that require control over their own encryption keys. 

<!-- CMGR-74880 -->

    KT: KT - CMK configuration for Cloud Service programs

* **Environment variable limit increased to 400**
    Cloud Manager now supports up to 400 environment variables per environment, doubled from the previous limit of 200. 

    Pipeline variables remain capped at 200. The UI enforces the correct limit per context and prevents additions beyond the allowed threshold.

    This change supports customers with more complex deployment configurations that require a larger number of environment-specific settings.

<!--CMGR-76755 · CMGR-76753 -->


## Beta programs {#private-beta-program}

To get exclusive access to upcoming features before their general release, you can participate in Cloud Manager's beta programs.

>[!IMPORTANT]
>
>Beta releases contain defects and are provided "AS IS" without warranty of any kind. Adobe has no obligation to maintain, correct, update, change, modify or otherwise support (by way of Adobe Support Services or otherwise) the beta releases. Customers use beta releases at their own risk and should not rely on the correct functioning or performance of beta releases, or on any accompanying documentation or materials. Features and APIs in beta are subject to change without notice. Any use of the beta releases is entirely at the customer's own risk.

See also [AEM Beta programs](/help/release-notes/release-notes-cloud/release-notes-current.md#aem-beta-programs)

The following beta program opportunities are currently available:

### Edge Delivery Services with AEM Authoring and flexible publish tier configuration {#eds-with-aem-authoring}

Cloud Manager introduces two capabilities designed to support modern delivery architectures.

* **Edge Delivery Services with AEM Authoring**
You can now deliver sites using Edge Delivery Services while continuing to author content in AEM Author mode. Depending on your workflow preferences, you can choose from the following authoring approaches:

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

To join the Beta, email [beta_quickbuild_cmpipelines@adobe.com](mailto:beta_quickbuild_cmpipelines@adobe.com) with your Adobe Organization ID and Program ID.

<!-- 
OLD
### Experience Hub Extensibility and Customization {#exp-hub-extensibility}

[Experience Hub](/help/experience-hub.md) serves as your entry point to AEM, customized for your organization's needs. Tell Adobe about your existing AEM UI Extensions so they can help you enable them in Experience Hub with minimal effort.

![Diagram of Experience Hub extensibility and customization workflow](/help/implementing/cloud-manager/release-notes/assets/experience-hub-extensibility-customization.png)

Embed custom experiences in Experience Hub to extend and personalize your organization's dashboard. In addition to Adobe's built-in widgets, add your own using the [UI Extensibility](https://developer.adobe.com/uix/docs/) framework. Build JavaScript-based UI apps and surface them to your users to meet business-specific requirements and workflows. 

Interested in the beta? Email [beta_exphubextensibility@adobe.com](mailto:beta_exphubextensibility@adobe.com) with your Adobe OrgID and a short description of the customization you intend to create.
-->

<!-- 
OLD
### Support for Custom Author Domains in Cloud Service

AEM Cloud Service is going to soon support one custom domain per Author environment.
-->



## Bug fixes {#bug-fixes}

* **Environment stuck in Updating with no active operation**
    An issue is now resolved where environments could become permanently stuck in an Updating state even when no pipeline run or configuration change was in progress. Affected environments can now be managed normally without requiring manual intervention from Adobe support. (CMGR-77133)
* **Advanced Networking - wrong port-forward rule deleted on duplicate source ports**
    When two port-forwarding rules in Advanced Networking shared the same source port (portOrig), deleting one rule would incorrectly remove the other. Cloud Manager now correctly identifies and removes only the intended rule. (CMGR-77019)

<!-- There are no significant bug fixes in the June 2026 Cloud Manager release. -->

<!-- ## Known issues {#known-issues} -->

