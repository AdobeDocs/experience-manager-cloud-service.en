---
title: Adobe Experience Manager as a Cloud Service Release Notes for 2020.7.0
description: Experience Manager Release Notes for 2020.7.0
---

# Release Notes for AEM as a Cloud Service 2020.7.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.7.0.

## Release Date {#release-date}

The release date for [!DNL Experience Manager] as a Cloud Service 2020.7.0 is July 31, 2020.

## What's New in Core Components {#whats-new-core-components}

Release 2.11.0 of the [Core Components](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/introduction.html) is now available as part of AEM Sites including:

* Introduction of a new [PDF Viewer Component](https://aemcomponents.dev/content/core-components-examples/library/page-authoring/pdf-viewer.html)
* Core Component [support of AMP](https://docs.adobe.com/content/help/en/experience-manager-core-components/developing/amp.html)
* Compatibility with version 1.0.2 of the [Adobe Client Data Layer](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/developing/data-layer/overview.html)
* Bug fixes and code quality improvements

## What's New in Cloud Manager {#cloud-manager}

Follow this section to learn about what is new and the updates for Cloud Manager in AEM as a Cloud Service Release 2020.7.0.

### Release Date {#release-date-cm}

The Release Date for [!UICONTROL Cloud Manager] Version 2020.7.0 is July 09, 2020.

### What's New {#what-is-new-cloud-manager}

* The environments page has been redesigned.

* Hibernated environments now show a discrete status in Cloud Manager when they are hibernated.

* The number of environment variables per environment has been increased to 200.

* The Cloud Manager build container now supports both Java 8 and Java 11.

* Cloud Manager pipelines now support customer-set variables and secrets. 
   Refer to [Pipeline Variables](/help/onboarding/getting-access-to-aem-in-cloud/creating-aem-application-project.md#pipeline-variables) for more details.

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

* Due to a change in how code coverage is calculated, the _minimum_ version of the Jacoco plugin is now 0.7.5.201505241946 (released May 2015). Customers explicitly referencing an older version will receive an error message in the code quality process.

## What's New in Cloud Readiness Analyzer {#cloud-readiness-analyzer}

Follow this section to learn about what is new and the updates for Cloud Readiness Analyzer Release v1.0.2.

### Bug Fixes {#cra-bug-fixes}

* Earlier version of the CRA could not be run on Adobe Experience Manager (AEM) 6.1. Explicit support to allow users in the administrators group was added.

   Refer to [Installing CRA on AEM 6.1](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/moving/cloud-migration/cloud-readiness-analyzer/using-cloud-readiness-analyzer.html#installing-on-aem61) for more details.

* The expiration timestamp displayed on the summary report was incorrect.

* CRA was detecting duplicate custom components.

* On AEM 6.1, the content inspection was exiting before completing the full inspection. Exception handling was added to allow the inspector to skip and continue until the full inspection is completed.

## What's New in AEM Cloud Services  {#whats-new-cloud-services}

AEM Cloud Service connectors for Adobe Target and Adobe Analytics have been updated with 

* new AEM UI implementations, replacing previous versions based on Classic UI

* simplified UI dialogs, leaving framework creation for variable mapping and other configurations to Adobe Launch 

* storage of configurations now in /conf rather than /etc/cloudsettings in the AEM repository
