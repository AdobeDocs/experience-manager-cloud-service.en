---
title: Release Notes for Release 2020.2.0
description: Release Notes for Release 2020.2.0
exl-id: 005c4756-44c6-4af5-9b0c-0fc07bd211a0
---
# Release Notes for AEM as a Cloud Service 2020.2.0 {#release-notes}

This page outlines the general Release Notes for Experience Manager as a Cloud Service 2020.2.0.

## Release Date {#release-date}

The Release Date for Experience Manager as a Cloud Service 2020.2.0 is February 13, 2020.

## Cloud Manager {#cloud-manager}

Follow this section to learn about what is new and the updates for Cloud Manager in AEM as a Cloud Service Release 2020.2.0.

### What's New {#what-is-new}

* The Adobe Experience Manager archetype version has been updated to version 22.
* The Stage and Production environments in Sandbox/Demo programs can now be updated through the Cloud Manager UI.
* URLs used in Experience Cloud notifications were optimized to avoid an extra redirect.
* Pipeline execution steps which timed out now explicitly state this.
* The Code Scanning step now has a downloadable log.
* The spreadsheet containing issues discovered during code scanning now has a column with a link to documentation for the specific rule.

### Bug Fixes  {#bug-fixes}

* Browser security policies would sometimes prevent certain buttons in the pipeline execution screen from working properly.
* The Overview, Environments, and Activity links were sometimes available on the Cloud Manager landing page.
* Certain failures when deploying could erroneously prevent new pipelines from being created.
