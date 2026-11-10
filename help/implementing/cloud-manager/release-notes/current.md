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

* **Java 23 opt-in**

  To support performance improvements and modern Java features, AEM Cloud Service environments are adding support for running with Java 25. As part of the initial rollout, Cloud Manager added opt-in options for building and deploying AEM projects

  * For pipeline build steps, set `.cloudmanager/java-version` to 25  in the repository branch used by your pipeline. Building with Java 25 also enables Java 25 for the target AEM runtime for the deployed environments.
  * To try the Java 25 runtime without changing your build JDK, set the Cloud Manager environment variable `AEM_JAVA_25_OPT_IN` to `true`. Runtime opt-in requires being upgraded to the latest AEM release.
  * Validate your application in development and stage before enabling it in production; configure the variable separately for each environment. 

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

* Deleting an environment left outdated CDN configuration and persistent alerts. Deleting an environment did not update the associated Fastly CDN configuration, which left outdated configuration behind and triggered continuous monitoring alerts. The deletion flow now updates the CDN configuration correctly. (CMGR-79320)
* Code quality scan fails on large projects. The code quality (SonarQube) scan generates multi-gigabyte debug logs and is terminated when scanning certain bundled libraries, causing the build to fail. The scan has been corrected so it completes normally on affected projects. (CMGR-80025)
* Environments remain in an Updating state. An environment remains in an Updating state with pipelines blocked, even after the underlying operation has finished. The environment lifecycle has been corrected so affected environments return to a usable state without manual intervention. (CMGR-78361)
* Smart Build restores modules with an incorrect version. After a Smart Build cache restore, some restored modules keep an older project version (and in some cases ui.content was not installed), producing an inconsistent build. Module restoration now preserves the correct version so Smart Build output matches a full build. (CMGR-80941)
* Sites usage CSV export showed month labels shifted by one month. On the License > Sites Usage Details page, the CSV export shows month labels shifted one month earlier for users in time zones behind UTC. The export now shows the correct month labels regardless of the user's time zone. (CMGR-80903)
* Clearer error attribution for configuration pipelines. Configuration pipeline failures are now attributed more accurately. Configuration pipeline failures are now attributed more accurately, including invalid customer YAML, infrastructure timeouts, and missing configuration files. (CMGR-80486, CMGR-73381, CMGR-81046)
* Clearer error messages for SSL certificate operations. Creating, updating, or deleting an SSL certificate returns a generic error with no detail when something goes wrong. These operations now return specific, actionable error messages. (CMGR-72997)
* Reusing an access token name no longer overwrites the existing token. Reusing an existing access token name within a program overwrites the shared token and creates duplicate access secrets. Cloud Manager now handles token name reuse correctly, preventing accidental overwrites and duplicates. (CMGR-81236)
* Clone Environment now works with Service Principals. The Clone Environment flow has been fixed so it works correctly for environments that use Service Principal authentication. (CMGR-80934)

<!-- There are no significant bug fixes in the July 2026 Cloud Manager release. -->

<!-- ## Known issues {#known-issues} -->

