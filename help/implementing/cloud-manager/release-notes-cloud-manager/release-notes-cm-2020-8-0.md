---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.8.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.8.0
feature: Release Information
exl-id: 70674e16-f9ba-4777-98fe-34161e90a481
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2020.8.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2020.8.0.

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2020.8.0 is August 06, 2020.

## What's New {#whats-new-cloud-manager}

* Content Audit is a feature enabled on Cloud Manager Sites Production Pipelines. The Production Pipeline configuration for programs with Sites now includes a third tab named **Content Audit**. Whenever a production pipeline is run, a new Content Audit step will be included in the pipeline after custom functional testing which will evaluate the site against a number of dimensions including performance, SEO (Search Engine Optimization), accessibility, best practices and PWA (Progressive Web App).


  >[!NOTE]
  >Content Audit has since been renamed to Experience Audit.

   Refer to [Experience Audit Testing](/help/implementing/cloud-manager/experience-audit-testing.md) for more details.

* Newly created environments in Assets programs will now be automatically configured with Smart Content Services.

* Hibernated environments can be de-hibernated from the Cloud Manager's **Overview** page.

* Ability to perform Experience Checks on pages, powered by Google Lighthouse. As part of Cloud Manager pipeline, up to 25 pages can be checked and validated against experience KPIs, and scores are displayed in Cloud Manager UI.

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
