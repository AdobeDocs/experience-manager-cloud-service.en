---
title: Release Notes for 2020.8.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: [!DNL Adobe Experience Manager] as a Cloud Service Release Notes for 2020.8.0.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service 2020.8.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.8.0.

## [!DNL Adobe Experience Manager Assets] as a Cloud Service {#assets}

* The new [!DNL Experience Manager Assets] deployments are integrated with [!DNL Adobe Developer Console] by default. It helps configure the smart tags functionality faster. On the existing deployments, administrators [configure smart tags integration](/help/assets/smart-tags-configuration.md#aio-integration) as before.

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What's New {#what-is-new-commerce}

* Product Console feature is now available. This allows marketers/authors in AEM to view and navigate categories and products that are stored in the commerce backend. Support for properties for catogories and products in the Product Console also provided.

* Product and Category Pickers improved to allow marketers to select product via SKU or select category via category ID.

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for [!UICONTROL Cloud Manager] Version 2020.8.0 is August 06, 2020.

### What's New {#what-is-new-cloud-manager}

* Content Audit is a feature enabled on Cloud Manager Sites Production Pipelines. The Production Pipeline configuration for programs with Sites now includes a third tab named **Content Audit**. Whenever a production pipeline is run, a new Content Audit step will be included in the pipeline after custom functional testing which will evaluate the site against a number of dimensions including performance, SEO (Search Engine Optimization), accessibility, best practices and PWA (Progressive Web App).

   Refer to [Content Audit Testing](/help/implementing/developing/introduction/understand-test-results.md#content-audit-testing) for more details.

* Newly created environments in Assets programs will now be automatically configured with Smart Content Services.

* Hibernated environments can be de-hibernated from the Cloud Manager's **Overview** page.

* Authentication-bound Private Maven Repositories are now supported.

* The Cloud Manager build container now supports both Java 8 and Java 11.
  Refer to [Using Java 11 Support](/help/onboarding/getting-access-to-aem-in-cloud/creating-aem-application-project.md#using-java-support) for more details.

### Bug Fixes {#bug-fixes-cm}

* Some unnecessary and undesired SonarQube plugins were being executed as part of the Code Quality scanning.

* On the pipeline execution page, the branch name was incorrectly formatted.

* In some cases, completed pipeline executions were not successfully recorded as having been completed thereby preventing new executions of the pipeline.

* Pipeline executions would occasionally get *stuck* due to internal communication issues.

* Upon provisioning a new organization, some users with administrative roles other than system administrators were erroneously given access to Cloud Manager.

* Under certain conditions, the update indexes job was started multiple times in parallel resulting in a deployment failure.

* The tooltip on the program cards were not consistently correct.

* The user interface erroneously allowed for operations to be attempted on an environment while it was being deleted.

* There was a color mismatch on the Cloud Manager's **Overview** page.

### Known Issues {#known-issues-cm}

* Invalid pages are included bringing the Content Audit Average Score below what they should be.

* The Content Audit tab incorrectly displays the base URL using the author domain instead of the publish domain.

* In order to activate the Content Audit step, users must edit the pipeline and, optionally, add pages. If no pages are added, the homepage will be audited.

## Content Transfer Tool {#content-transfer-tool}

Follow this section to learn about what is new and the updates for Content Transfer Tool Release v1.0.4.

### What's New {#what-is-new-ctt}

* Content Transfer Tool now supports Shared S3 DataStore.

### Bug Fixes {#ctt-bug-fixes}

* Additional timeouts added for the tool to complete actions.

* Earlier version UI sometimes displayed successful extraction even though log showed errors.

