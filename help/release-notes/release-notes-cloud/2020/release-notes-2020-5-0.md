---
title: Adobe Experience Manager as a Cloud Service Release Notes for 2020.5.0
description: Experience Manager Release Notes for 2020.5.0
exl-id: 8570d2c3-6d55-4914-94b2-f5d162e0c285
---
# Release Notes for AEM as a Cloud Service 2020.5.0 {#release-notes}

This page outlines the general Release Notes for Experience Manager as a Cloud Service 2020.5.0.

## Release Date {#release-date}

The release date for [!DNL Experience Manager] as a Cloud Service 2020.5.0 is May 07, 2020.

## What's New in AEM Sites {#aem-sites}

Follow this section to learn about what is new and the updates for AEM Sites in AEM as a Cloud Service Release 2020.5.0.

* Detailed job information now available after processing bulk page moves and roll outs as asynchronous jobs.
* When copying/pasting a page tree, now offering to choose between pasting only the root page or also the sub-pages of the tree.
* AEM Experience Fragments exported to Adobe Target workspaces now appear as unique offer types and offer sources in Target.
* MSM - using *publish* trigger now successfully rolls out delete events for components in live copy source, that is, deleting components in a live copy that were deleted in live copy source.
* MSM - live copy components are now being renamed to *_msm_moved* after same component rollout from live copy source.


## What's New in Cloud Manager {#cloud-manager}

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
