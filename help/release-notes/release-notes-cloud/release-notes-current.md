---
title: Adobe Experience Manager as a Cloud Service Release Notes for 2020.7.0
description: Experience Manager Release Notes for 2020.7.0
---

# Release Notes for AEM as a Cloud Service 2020.7.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.7.0.

## What's New in Cloud Manager {#cloud-manager}

Follow this section to learn about what is new and the updates for Cloud Manager in AEM as a Cloud Service Release 2020.7.0.

### Release Date {#release-date}

The Release Date for [!UICONTROL Cloud Manager] Version 2020.7.0 is July 09, 2020.

### What's New {#what-is-new-cloud-manager}

* The environments page has been redesigned.

* Hibernated environments now show a discrete status in Cloud Manager when they are hibernated.

* The number of environment variables per environment has been increased to 200.

* The Cloud Manager build container now supports both Java 8 and Java 11.

### Bug Fixes {#bug-fixes-cm}

* The link from Cloud Manager to the Developer Console was incorrectly active before environments were fully created.

* The link to the Developer Console directly from Cloud Manager did not display the option to de-hibernate/hibernate a Sandbox Program's environment.

* The **Cancel** and **Save** options on the Non-Production Pipeline edit page were not always visible.

* Certain failures in the code quality process could result in the log file not being generated correctly.

* When creating a new program, the suggested name would sometimes return a duplicate of an existing program name.

* Some large pipeline step logs could not be consistently downloaded through the user interface.

* The validation of environment names had an off-by-one error.

* The Environments page would sometimes show publish and dispatcher segments when none was present.