---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2022.01.0
description: These are the release notes for Cloud Manager in AEM as a Cloud Service release 2022.01.0.
feature: Release Information
exl-id: 2dfdc943-0518-40ea-8712-1dabb97eeaa9
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2022.01.0 {#release-notes}

This page outlines the release notes for Cloud Manager in AEM as a Cloud Service 2022.01.0.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager in AEM as a Cloud Service 2022.01.0 is January 20, 2022. The next release is planned for February 10, 2022.

## What's New {#what-is-new}

* Cloud Manager will [avoid rebuilding the code base when it detects that the same git commit is used](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/setting-up-project.md#build-artifact-reuse) in multiple full-stack pipeline executions.
* Accessing the AEM environment log now requires the **Deployment Manager** product profile. Users without this profile will see a disabled button in the user interface.
*  The UI will not allow front-end pipeline configuration for a program where Sites is not enabled as a solution. 
* Upon generating a git password, the expiration date will be displayed.

## Bug Fixes {#bug-fixes}

* Null pointer exceptions encountered by some front-end pipeline deployments have been corrected.
* Environment variables can now be added, updated, and deleted when an environment is running an outdated version of AEM.
* The build image step will no longer be marked as ERROR for pipelines that used the scheduled step in certain rare cases.
* For programs with only one repository, the pipeline execution screen will now display the repository name.
