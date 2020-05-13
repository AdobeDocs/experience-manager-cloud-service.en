---
title: Adobe Experience Manager as a Cloud Service Release Notes for 2020.5.0
description: Experience Manager Release Notes for 2020.5.0
---

# Release Notes for AEM as a Cloud Service 2020.5.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.5.0.

## Cloud Manager {#cloud-manager}

Follow this section to learn about what is new and the updates for Cloud Manager in AEM as a Cloud Service Release 2020.5.0.

### What's New {#what-is-new}

* Six additional code quality rules have been added to help customers identify potential issues when planning a migration to Cloud Service.
* A new metric *Cloud Service Compatibility* has been added to summarize the number of compatibility-related issues.
* Environments which failed to be created will now be automatically deleted approximately 24 hours after creation failed unless they have already been deleted.
* The performance of the Activity page and the Pipeline Executions List API has been improved.
* The code quality log now contains complete stack traces for exceptions.

### Bug Fixes  {#bug-fixes}

* A misleading card was displayed on the overview page while the production pipeline was running.
* The *DontImplementOrExtendProviderTypesPomCheck* code quality rule could sometimes produce a Null Pointer Exception.
* Some documentation links from the overview page did not work correctly.
* The Create Environment dialog did not render correctly in Safari.
* Certain cards on the overview page did not display entity names correctly.
* In some cases, the Build Image would fail to download customer packages successfully.

