---
title: Experience Audit Testing
description: Learn how Experience Audit validates your deployment process and helps ensure that changes deployed meet baseline standards for performance, accessibility, best practices, and SEO.
exl-id: 8d31bc9c-d38d-4d5b-b2ae-b758e02b7073
---

# Experience Audit Testing {#experience-audit-testing}

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_expaudittesting"
>title="Experience Audit Testing"
>abstract="Learn how Experience Audit validates your deployment process and helps ensure that changes deployed meet baseline standards for performance, accessibility, best practices, and SEO."

Learn how Experience Audit validates your deployment process and helps ensure that changes deployed meet baseline standards for performance, accessibility, best practices, and SEO.

## Overview {#overview}

Experience Audit is a feature available in Cloud Manager Sites Production pipelines that validates the deployment process and helps ensure that changes deployed:

1. Meet baseline standards for performance, accessibility, best practices, SEO (Search Engine Optimization), and PWA (Progressive Web App).

1. Do not introduce regressions.

Experience Audit in Cloud Manager ensures that the end user's experience on the site are of the highest standards.

The audit results are informational and allow the deployment manager to see the scores and the change between the current and previous scores. This insight is valuable to determine if there is a regression that will be introduced with the current deployment.

Experience Audit is powered by Google Lighthouse, an open source tool from Google and is enabled in all Cloud Manager production pipelines.

## Understanding Experience Audit Results {#understanding-experience-audit-results}

Experience Audit provides aggregate and detailed page-level test results via the [production pipeline execution page.](/help/implementing/cloud-manager/deploy-code.md)

* Aggregate metrics measure the average scores across the pages that were audited for performance, accessibility, best practices, SEO (Search Engine Optimization). 
* Individual page level scores are also available via drill down.
* Details of the scores are available to view the results of the individual tests along with guidance on how to remediate any issues that were identified.
* A history of the test results is persisted within Cloud Manager to determine if changes that are being introduced in the pipeline include any regressions from the previous run.

### Aggregate Scores {#aggregate-scores}

The aggregate level score takes the average score of the pages that are included in the run. The change at the aggregate level represents the average score of the pages in the current run compared to the average of the scores from the previous run, even if the collection of pages configured to be included has been changed between runs.

There is an aggregate level score for each test types such as performance, accessibility, SEO, and best practices.

The change metric can have one of the following values.

* **Positive value** - The page(s) has improved on the selected test since the last production pipeline run.

* **Negative value** - the page(s) has regressed on the selected test since the last production pipeline run.

* **No Change** - The page(s) scored the same since the last production pipeline run.

* **N/A** - There was no previous score available to compare.

![Experience Audit results](/help/implementing/cloud-manager/assets/exp-audit-1.png)


### Page-Level Scores {#page-level-scores}

By drilling into any of the tests, more detailed page level scoring is available. You can see how the individual pages scored for the specific test along with the change from the previous test run.

Clicking into the details of any individual page provides information on the elements of the page that were evaluated as well as guidance to fix issues if opportunities for improvement are detected.

![Page-level scores](/help/implementing/cloud-manager/assets/exp-audit-2.png)
