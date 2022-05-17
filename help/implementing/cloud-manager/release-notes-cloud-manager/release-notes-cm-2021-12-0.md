---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.12.0
description: These are the release notes for Cloud Manager in AEM as a Cloud Service release 2021.12.0.
feature: Release Information
---

# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2021.12.0 {#release-notes}

This page outlines the release notes for Cloud Manager in AEM as a Cloud Service 2021.12.0.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager in AEM as a Cloud Service 2021.12.0 is December 16, 2021. The next release is planned for January 20, 2022.

## What's New {#what-is-new}

* The commit hash, which is already visible in the UI, is now also provided in the API.
* The Activity page now includes a pop-over for running pipelines that provides a summary of pipeline details at-a-glance.
* Updates to include additional details presented in the Activities page were added.
* The Learn tab in Cloud Manager now includes quick access to API guides and associated resources.
* A user with the Deployment Manager role can now initiate the Project/Branch creation wizard for a repository with no branches from the action menu on the repositories page.
* The Deployment Manager, who is in the add or edit pipeline workflow, is now informed on how to create a branch or project if the selected repository has no branches.
* A new Cloud Manager self-service feature was added to allow [adding free-form variables and secrets at the environment level.](/help/implementing/cloud-manager/environment-variables.md)
* With the new [Reference Demos Add-On](/help/journey-sites/demos-add-on/overview.md) (available on 17 December 2021), the latest demo code bases for AEM products can be installed and be ready to be deployed via the new [quick site creation tool](/help/journey-sites/quick-site/overview.md) in Sites.
* Front-end pipelines now support pipeline variables.
* Screens can now be enabled in the Program Edit dialog for all sandboxes.
* The guidance provided by the call-to-action card in the overview page has been refreshed to accurately reflect its association with the production full stack pipeline.
* Enhancements to Activity page were added to surface additional details applicable to pipelines including source code, commit ID, etc.
* Minor update were made to the UI when copying TXT entries ("TXT value" instead of "TXT record") to remove potential confusion.
* [The documentation related to certificate errors](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md#certificate-errors) has been updated to cover additional examples along with trouble-shooting steps.
* An option is now available in the front-end pipeline execution to reject or approve before deployment to production.
* The version of the AEM Project Archetype used by Cloud Manager has been updated to version 32.


## Bug Fixes {#bug-fixes}

* Functional and UI test artifacts were not included in the build step log.
* The logs for the product, functional, and UI test steps were not accessible through the public API.
* In rare cases, the link from the environment details page to the publish or preview service would be non-functional.
* Full stack production pipelines remain named "Production Pipeline" even when the user inputs a different name in the name field. 
