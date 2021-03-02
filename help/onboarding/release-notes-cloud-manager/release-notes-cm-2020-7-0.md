---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.7.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.7.0
---

# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2020.7.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2020.7.0.

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2020.7.0 is July 09, 2020.

## What's New {#whats-new-cloud-manager}

* The environments page has been redesigned.

* Hibernated environments now show a discrete status in Cloud Manager when they are hibernated.

* The number of environment variables per environment has been increased to 200.

* Cloud Manager pipelines now support customer-set variables and secrets. 

   Refer to [Pipeline Variables](/help/onboarding/getting-access-to-aem-in-cloud/build-environment-details.md#pipeline-variables) for more details.

* Authentication-bound Private Maven Repositories are now supported.

* The Cloud Manager build container now supports both Java 8 and Java 11.
  Refer to [Using Java 11 Support](/help/onboarding/getting-access-to-aem-in-cloud/build-environment-details.md#using-java-support) for more details.

### Bug Fixes {#bug-fixes-cm}

* The link from Cloud Manager to the Developer Console was incorrectly active before environments were fully created.

* The link to the Developer Console directly from Cloud Manager did not display the option to de-hibernate/hibernate a Sandbox Program's environment.

* The **Cancel** and **Save** options on the Non-Production Pipeline edit page were not always visible.

* Certain failures in the code quality process could result in the log file not being generated correctly.

* When creating a new program, the suggested name would sometimes return a duplicate of an existing program name.

* Some large pipeline step logs could not be consistently downloaded through the user interface.

* The validation of environment names had an off-by-one error.

* The Environments page would sometimes show publish and dispatcher segments when none was present.

### Known Issues {#known-issues}

* Due to a change in how code coverage is calculated, the *minimum* version of the Jacoco plugin is now 0.7.5.201505241946 (released May 2015). Customers explicitly referencing an older version receive an error message in the code quality process.