---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.3.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.3.0
---

# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2021.3.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.3.0.

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.3.0 is March 11, 2021.
The next release is planned for April 08, 2021.

## Cloud Manager {#cloud-manager}

### What's New {#what-is-new}

* Customers with environments with pre-existing Custom Domain Name configurations for [IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/check-ip-allow-list-status.md#pre-existing-cdn), [SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/check-status-ssl-certificate.md#pre-existing-cdn) and [Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md#pre-existing-cdn) will see a message about their previously existing configurations and will be able to self-serve via the UI. 

* Users with requisite permissions can now edit a Program, allowing them to do the following in a self-service manner: 
   * Add Sites solution to an existing program with Assets (or vice-versa).
   * Remove Sites (or Assets) from an existing program with both Sites and Assets.
   * Add second, unused solution entitlement either to an existing program or as a new Program.

* **AEM Push Update** label will now be displayed for both Pipeline Execution and Activity screens.

*  If an environment is hibernated but there is also an AEM update available, the **Hibernated** status will take precedence over **Update available**.

* Users can now see their Cloud Manager role(s) by selecting the 'View Cloud Manager Role(s)' option after navigating to the User Profile icon (top right) of Unified Shell. 

* The label **Application for Approval** has been relabeled to **Production Approval** for greater clarity.

* The **Version** label has been relabeled to **Git Tag** in the Production pipeline execution screen.

* The labels which define the behavior when important metrics do not meet the defined threshold have been relabeled to reflect their true behavior: **Cancel Immediately** and **Approve Immediately**.

* The class and method deprecation lists have been updated based on version `2021.3.4997.20210303T022849Z-210225` of the AEM Cloud Service SDK.

* Cloud Manager Production pipeline will now include [Custom UI Testing](/help/implementing/cloud-manager/functional-testing.md#custom-ui-testing) capability.

### Bug Fixes  {#bug-fixes}

* Package versioning was skipped in some cases during AEM push upgrade.

* Some quality issues were not properly discovered when packages were embedded in other packages.

* In obscure situations, the default program name generated upon opening the Add Program dialog could be a duplicate of an existing program name. 

* On occasion, if user navigates away from pipeline execution page immediately after starting a pipeline, an error message is displayed stating that the action failed, although the execution actually starts.

* The build step was unnecessarily restarted when customer builds resulted in invalid packages.

* On occasion, user may see a green "active" status next to an IP Allowlist even when that configuration was not deployed.

* All existing production pipelines will be automatically enabled with the Experience Audit step.