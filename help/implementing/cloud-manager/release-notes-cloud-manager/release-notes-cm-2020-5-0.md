---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.5.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.5.0
feature: Release Information
exl-id: 9f534858-d18f-4224-8b94-9583a05aed95
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2020.5.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2020.5.0.

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2020.5.0 is May 07, 2020.

## What's New {#whats-new-cloud-manager}

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
