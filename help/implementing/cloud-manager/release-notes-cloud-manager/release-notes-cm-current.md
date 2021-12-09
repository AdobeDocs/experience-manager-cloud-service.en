---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.12.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.12.0
feature: Release Information
---

# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2021.12.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.12.0.

>[!NOTE]
>Refer to [this page](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html) for the current Release Notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager in AEM as a Cloud Service 2021.11.0 is 16 December 2021. The next release is planned for February 2022.

### What's New {#what-is-new}

* Enhancements to information presented in the Activities page
* Minor update to copy in the UI ("TXT value" instead of "TXT record" to remove potential confusion)
* A user with the Deployment Manager role can now initiate the Project/Branch creation wizard for a repository with no branches from the action menu in the repositories page.
* Enhancements to Activity page to surface additional details including Source Code, Commit ID, etc. applicable to pipelines
* An optimization in the OakPal scanning process has been introduced for large packages.
* Front End pipelines now support pipeline variables.
* Cloud Manager self-service feature to add free-form variables (including secrets) at the environment level

### Bug Fixes {#bug-fixes}

* Functional and UI test artifacts were not included in the build step log.
* The logs for the product, functional, and UI test steps were not accessible through the public API.
