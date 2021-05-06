





---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.4.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.4.0
feature: Release Information
exl-id: 42cc9cab-6e66-4976-a3b1-ecb9dbaaabf4
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2021.4.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.4.0.

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.4.0 is April 08, 2021.
The next release is planned for May 06, 2021.

### What's New {#what-is-new-april}

* UI updates to the Add and Edit Program workflows to make it more intuitive.

* A user with requisite permissions can now submit the commerce end point via the UI.

* Environment variables can now be scoped to a specific service, either author or publish. Requires AEM Version `2021.03.5104.20210328T185548Z` or higher.

* The **Manage Git** button is displayed on the Pipelines card even when no pipelines have been configured.

* The version of the AEM project archetype used by Cloud Manager has been updated to version 27.

* Projects in the Adobe I/O Developer Console created by Cloud Manager can no longer be unintentionally edited or deleted.

* When a user adds a new environment they will be informed that once an environment is created it cannot be moved to a different region. 

* Environment variables can now be scoped to a specific service, either author or publish. Requires AEM Version 2021.03.5104.20210328T185548Z or higher. 

* The error message when starting a pipeline when an environment was deleted has been clarified.

* OSGi bundles provided by Eclipse projects are now excluded from rule `CQBP-84--dependencies`.

### Bug Fixes {#bug-fixes-cm-april}

* When editing the Experience audit page of a pipeline, an input path starting with a slash `( / )` will no longer result in the step being stuck in pending status.

* When a new production pipeline is created, if no content audit override is added by the user, the default homepage was not audited.

* Issues for the `CloudServiceIncompatibleWorkflowProcess` had the incorrect severity in the downloadable issue CSV file. 

* The `Runmode` check was producing false positives on non-folder nodes.