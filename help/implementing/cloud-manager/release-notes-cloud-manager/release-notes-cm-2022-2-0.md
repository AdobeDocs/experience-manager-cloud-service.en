---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2022.02.0
description: These are the release notes for Cloud Manager in AEM as a Cloud Service release 2022.02.0.
feature: Release Information
exl-id: da0643a0-78f8-4e9d-9cc9-a1a17067a08c
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2022.02.0 {#release-notes}

This page outlines the release notes for Cloud Manager in AEM as a Cloud Service 2022.02.0.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager in AEM as a Cloud Service 2022.02.0 is February 10, 2022. The next release is planned for March 10, 2022.

## What's New {#what-is-new}

* New accelerated [Web Tier Config pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines) have been introduced to exclusively deploy HTTPD/dispatcher configuration.
  * You must be on AEM version `2021.12.6151.20211217T120950Z` or newer and [opt in to the flexible mode of the dispatcher tools](/help/implementing/dispatcher/disp-overview.md#validation-debug) to use this feature.
  * This feature will be rolled out in a phased approach over the two weeks following the 2022.02.0 release.
* The Cloud Manager landing page experience has been refreshed to deliver improved navigation, easy switching between grid/tile views, and pop-overs for quick program summary.
* A new failing threshold (`< D`) has been added to the [reliability rating metric.](/help/implementing/cloud-manager/code-quality-testing.md#understanding-code-quality-rules)
  * Customers with severe quality issues that impact system stability, primarily related to invalid indexes and workflow processes, will not be able to deploy until those issues are resolved.
* The severity of the `BannedPath` [quality rule](/help/implementing/cloud-manager/code-quality-testing.md#understanding-code-quality-rules) has been changed from blocker to critical.
* The pipeline wizard will inform the user when an AEM environment update may be needed before configuring a [Web Tier Config pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines) associated with it.

## Bug Fixes {#bug-fixes}

* Old git repository passwords are now always invalidated when a new password is generated.
* Updating environment variables through the API no longer interferes with a pipeline execution in rare situations.
