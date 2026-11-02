---
title: Release Notes for Cloud Manager 2026.10.0
description: Learn about the release of Cloud Manager 2026.10.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
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
# Release notes for Cloud Manager 2026.10.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

Learn about the release of Cloud Manager 2026.9.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2026.10.0 in AEM as a Cloud Service is Thursday, October 1, 2026. 

The next planned release is Thursday, November 5, 2026.


## New features - Cloud Manager {#cloud-manager-whats-new}

<!--
* **GitHub Apps for EDS sites**  
    Cloud Manager now exposes an option for managing GitHub App connections on provisioned Edge Delivery Services (EDS) sites. This option allows teams and automation tools to configure GitHub App integrations programmatically, rather than through manual setup for each site. (CMGR-78197) new doc needed
-->

* **Canary deployment support**

    Cloud Manager now supports canary (hybrid) releases at the deployment step. When configuring a production pipeline, teams can roll out code to a subset of production nodes, then promote the release or roll back from the Cloud Manager UI.

    If no action is taken within the configured validation window, Cloud Manager automatically promotes the deployment. This reduces deployment risk for mission-critical applications by allowing teams to validate real traffic behavior before performing a full rollout, and enables faster detection and resolution of issues without impacting all users.

    For more information, see [Use Canary Deployments to Validate Code](/help/implementing/cloud-manager/canary-deployments.md) (CMGR-71220, CMGR-74599)

* **VPN Network Infrastructure — BGP routing and multiple connections**

    The Advanced Networking VPN network infrastructure API now supports BGP (Border Gateway Protocol) dynamic routing alongside static routing, and the previous limit of one VPN connection per infrastructure has been removed. Teams can now configure multiple connections and, with BGP enabled, have routes learned dynamically rather than maintaining static prefixes. Static and BGP connections can coexist in the same infrastructure, providing enterprise networking teams with increased flexibility.

    New API fields support the capability (bgpAsn, bgpPeeringAddress, adobeApipaAddress, and a top-level adobeAsn required whenever a connection uses BGP); see the Cloud Manager API reference for details. (SKYOPS-140538)

    For more information, see [Virtual Private Network (VPN)](/help/security/configuring-advanced-networking.md#vpn)
    

## Beta programs {#private-beta-program}

To obtain access to upcoming features before their general release, you can participate in Cloud Manager's beta programs.

>[!IMPORTANT]
>
>Beta releases contain defects and are provided without warranty of any kind. Adobe has no obligation to maintain, correct, update, change, modify or otherwise support the beta releases. Customers use beta releases at their own risk; do not rely on beta release functionality, performance, or accompanying documentation or materials. Features and APIs in beta are subject to change without notice. Any use of the beta releases is entirely at the customer's own risk.

See also [AEM Beta programs](/help/release-notes/release-notes-cloud/release-notes-current.md#aem-beta-programs)

The following beta program opportunity is currently available:

### Edge Delivery Services with AEM Authoring and flexible publish tier configuration {#eds-with-aem-authoring}

Cloud Manager introduces two capabilities designed to support current delivery architectures.

* **Edge Delivery Services with AEM Authoring**
You can now deliver sites using Edge Delivery Services while continuing to author content in AEM Author mode. Depending on your workflow preferences, you can choose from the following authoring approaches:

    * Document-based authoring
    * AEM-based authoring

For more information, see [Create Edge Delivery site in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md#one-click-edge-delivery-site).

* **Flexible publish tier configuration**

Cloud Manager now lets you configure whether a publish tier is required for your program. This flexibility lets you configure environments that better match your chosen delivery architecture.

For more information, see [Flexible Publish Tier (Beta)](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#flexible-publish-tier).

To join the beta, email [grp-beta_xwalk-publish_config@adobe.com](mailto:grp-beta_xwalk-publish_config@adobe.com) with your Adobe Organization ID and Program ID.


## Bug fixes {#bug-fixes}

* Dynamic Media and Content Hub activation failed for all EDS programs. A placeholder offer used during Edge Delivery Services provisioning disrupted the shared activation batch, causing Dynamic Media with OpenAPI and Content Hub activation to fail across every EDS program. The provisioning flow has been corrected so these activations complete reliably for all EDS programs. (CMGR-80012)

* Custom domain deletions remained pending indefinitely. In some situations, deleting a CDN domain configuration caused the deletion process to stop, blocking further domain changes. The domain-configuration deletions now finish as expected. (CMGR-79997)

* Universal Editor (EDS) site provisioning failed intermittently. Universal Editor site provisioning failed intermittently when a GitHub deployment step exceeded a three-minute timeout. The provisioning flow has been made more resilient so these sites provision reliably. (CMGR-75897)

<!-- There are no significant bug fixes in the July 2026 Cloud Manager release. -->

<!-- ## Known issues {#known-issues} -->

