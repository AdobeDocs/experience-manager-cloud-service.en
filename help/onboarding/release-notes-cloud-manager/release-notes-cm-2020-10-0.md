---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.10.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.10.0
feature: Release Information
exl-id: 129d0dd8-3d6e-4cf0-b42e-5526f5cf0836
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2020.10.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2020.10.0.

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2020.10.0 is October 01, 2020.

## Cloud Manager {#cloud-manager}

### What's New {#what-is-new}

* The Environments page has been redesigned.

* Hibernated environments now show a discrete status in Cloud Manager when they are hibernated.

* The Cloud Manager build container now supports compiling projects using either Java 8 or Java 11. Support for Java 11 is provided by the Maven toolchains system.

* The number of environment variables per environment has been increased to 200.

* The Environment card on the Overview page will now list up to three environments. Users can select the **Show All** button to navigate to the Environment summary page to view a table with a complete list of environments.
   Refer to [Viewing Environment](/help/implementing/cloud-manager/manage-environments.md#viewing-environment) for more details.
 

### Bug Fixes {#bug-fixes-cloud-manager}

* The link from Cloud Manager to the Developer Console was incorrectly active before environments were fully created.

* The link to the Developer Console directly from Cloud Manager did not display the option to de-hibernate/hibernate a Sandbox Program's environment.

* The Cancel and Save buttons on the Non-Production Pipeline Edit page were not always visible.

* Certain failures in the code quality process could result in the log file not being generated correctly.

* When creating a new program, the suggested name would sometimes return a duplicate of an existing program name.

* Some large pipeline step logs could not be consistently downloaded through the user interface.

* The validation of environment names had an off-by-one error.

* The Environments page would sometimes show publish and dispatcher segments when none was present.
