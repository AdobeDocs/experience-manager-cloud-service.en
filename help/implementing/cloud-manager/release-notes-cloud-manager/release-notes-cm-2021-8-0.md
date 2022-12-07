---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.8.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.8.0
feature: Release Information
exl-id: cf1d5c4f-404a-4ced-90f2-273c710adc0f
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2021.8.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.8.0.

>[!NOTE]
>To see the current Release Notes for Adobe Experience Manager as a Cloud Service, click [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html).

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.8.0 is August 12, 2021.

### What's New {#what-is-new}

* Cloud Service customers can now view Service Level Agreement (SLA) reports in Cloud Manager. This will be made available progressively over the next few months.
   See [SLA Reporting](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/sla-reporting.html) to learn more.

* The type and severity of the IndexType and `IndexDamAssetLucene` quality rules has been changed. These are now both Bugs of Blocker *serverity*.

* New Oak index quality rules have been introduced to cover asynchronous and tika configurations.

* Increase max SSL certs per program to 50.

* Self-service capability to allow users to create and manage multiple repositories via Cloud Manager UI.

* SonarQube was unnecessarily reading Git history data. On large code bases, this could lead to an unnecessary build performance penalty.

* There is now an API available to invalidate the Maven dependency cache per pipeline.
 
* The version of the AEM Project Archetype used by Cloud Manager has been updated to version 29. 

### Bug Fixes {#bug-fixes}

* Update Available status should not be displayed when the latest release is less than the current release.

* Initial onboarding was failing for new organizations with very long names.

* Occasionally, when a pipeline is triggered twice for some reason, it results in one of the executions failing with *cannot update pipeline execution status* error.
