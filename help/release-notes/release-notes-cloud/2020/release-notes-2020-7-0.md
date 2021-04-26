---
title: Release Notes for 2020.7.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: [!DNL Adobe Experience Manager] as a Cloud Service Release Notes for 2020.7.0.
exl-id: 75d354a3-6987-4de0-aec8-24043461c516
---
# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service 2020.7.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.7.0.

## Release Date {#release-date}

The release date for [!DNL Experience Manager] as a Cloud Service 2020.7.0 is July 30, 2020.

## Adobe Experience Manager Sites as a Cloud Service {#cloud-services-sites}

### What's New {#what-is-new-sites}

[!DNL Experience Manager] as a Cloud Service connectors for [!DNL Adobe Target] and [!DNL Adobe Analytics] are enhanced in the following ways:

* A new user interface implementation replaces the implementation based on the Classic UI.

* Simplified user interface dialogs, leaving framework creation for variable mapping and other configurations to [!DNL Adobe Launch]. See [Integrating Adobe Analytics](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/sites/integrations/integrating-adobe-analytics.html) and [Integrating Adobe Target](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/sites/integrations/integrating-adobe-target.html).

* Configurations are now stored in `/conf` rather than `/etc/cloudsettings` in the Experience Manager repository.

## [!DNL Adobe Experience Manager Assets] as a Cloud Service {#assets}

### What is new in [!DNL Assets] {#what-is-new-assets}

* [!DNL Asset Compute Service] is a scalable and extensible service to process assets. Administrators can configure [!DNL Experience Manager] to invoke custom applications created using the [!DNL Asset Compute Service]. Developers can use the service to create specialized custom applications that cater to complex use cases. This web service can generate thumbnails for different file types, high-quality image renderings from Adobe file formats, encode videos (future), extract metadata, extract full text as precursor for indexing, and run an asset through all available [!DNL Sensei] services. see [use asset microservices and processing profiles](/help/assets/asset-microservices-configure-and-use.md).

* The initial configuration of [!DNL Dynamic Media] in [!DNL Experience Manager] as a Cloud Service is improved to be more robust. It now provides progress of the processes to the administrators.

* Publishing of assets to [!DNL Dynamic Media] is simplified and made more robust by making it an integral part of overall asset processing pipeline using asset microservices and improving the batch publishing backend.

* Workflow steps that are not compatible with a Cloud Service deployment are now marked with a warning in the [!UICONTROL workflow model] editor. Additionally, when executing the existing workflows on Cloud Service environment, the incompatible workflow steps are skipped.

* Workflow models created by customers that are deployed to `/conf/global` in the Git project associated with the environment in [!DNL Cloud Manager] are automatically deployed to `/var` and thus available in [!DNL Experience Manager]. The product workflow models under `/libs` that were changed by customer are not automatically deployed to `/var`.

### Bugs fixed {#assets-bugs-fixed}

* The Move Asset wizard does not load as expected for the assets that are included in Collections. (CQ-4296756)
* The values of `dam:size` and `dam:sha1` are excluded from XMP writeback. (CQ-4237355)
* When unpublishing assets in bulk, [!DNL Brand Portal] generates an error suggesting that the request URI is too long. (CQ-4299474)

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What's New {#what-is-new-commerce}

AEM Commerce is now available on Cloud Service.

  Refer to [Getting started with AEM Commerce as a Cloud Service](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/commerce/getting-started.html) for more details.

## Core Components {#core-components}

### What's New {#what-is-new-core-components}

Release 2.11.0 of the [AEM Core Components](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/introduction.html) is now available as part of AEM Sites including:

* Introduction of a new [PDF Viewer Component](https://aemcomponents.dev/content/core-components-examples/library/page-authoring/pdf-viewer.html).

* Accelerated Mobile Pages (AMP) support of Core Components is now available. It helps to produce faster customer experiences by making the page transition instantaneously when entering the site from a Google mobile search result, which improves user engagement and SEO.
   Refer to [AMP Support for the Core Components](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/developing/amp.html) for more details.

* Compatibility with version 1.0.2 of the [Adobe Client Data Layer](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/developing/data-layer/overview.html).

* Bug fixes and code quality improvements.

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for [!UICONTROL Cloud Manager] Version 2020.7.0 is July 09, 2020.

### What's New {#what-is-new-cloud-manager}

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

## Adobe Experience Manager as a Cloud Service Foundation {#cloud-foundation}

### What's New {#what-is-new-foundations}

* [Logs can be forwarded to Splunk accounts](/help/implementing/developing/introduction/logging.md#splunk-logs), which allows organizations to leverage their Splunk investment.

* [A static, dedicated egress IP address](/help/implementing/developing/introduction/development-guidelines.md#dedicated-egress-ip-address) can be assigned for outbound traffic programmed in Java code, which may be useful for some integrations.

* Ported AEM Analytics cloud service UI from Classic UI to new AEM UI. Also moved location of Analytics cloud service in AEM repository from `/etc` to `/conf`, to align with other AEM cloud services.

* Ported AEM Target cloud service UI from Classic UI to new AEM UI. Also moved location of Target cloud service in AEM repository from `/etc` to `/conf`, to align with other AEM cloud services.

## Cloud Readiness Analyzer {#cloud-readiness-analyzer}

Follow this section to learn about what is new and the updates for Cloud Readiness Analyzer Release v1.0.2.

### Bug Fixes {#cra-bug-fixes}

* Earlier version of the CRA could not be run on Adobe Experience Manager (AEM) 6.1. Explicit support to allow users in the administrators group was added.

   Refer to [Installing CRA on AEM 6.1](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/moving/cloud-migration/cloud-readiness-analyzer/using-cloud-readiness-analyzer.html#installing-on-aem61) for more details.

* The expiration timestamp displayed on the summary report was incorrect.

* CRA was detecting duplicate custom components.

* On AEM 6.1, the content inspection was exiting before completing the full inspection. Exception handling was added to allow the inspector to skip and continue until the full inspection is completed.
