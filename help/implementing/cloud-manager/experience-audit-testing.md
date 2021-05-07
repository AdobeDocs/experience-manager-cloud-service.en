---
title: Experience Audit Testing - Cloud Services
description: Experience Audit Testing - Cloud Services
---

# Experience Audit Testing {#experience-audit-testing}

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_expaudittesting"
>title="Experience Audit Testing"
>abstract="Experience Audit is a feature available in Cloud Manager Sites Production pipelines, powered by Google Lighthouse, an open source tool from Google. This feature is enabled in all Cloud Manager Production pipelines."

Experience Audit is a feature available in Cloud Manager Sites Production pipelines, powered by Google Lighthouse, an open source tool from Google. This feature is enabled in all Cloud Manager Production pipelines.

It validates the deployment process and helps ensure that changes deployed:

1. Meet baseline standards for performance, accessibility, best practices, SEO (Search Engine Optimization), and PWA (Progressive Web App).

1. Do not include regressions in these dimensions.

Experience Audit in Cloud Manager ensures that the end users digital experience on the site may be maintained at the highest standards. The results are informational and allow the user to see the scores and the change between the current and previous scores. This insight is valuable to determine if there is a regression that will be introduced with the current deployment.

## Understanding Experience Audit Results {#understanding-experience-audit-results}

Experience Audit provides aggregate and detailed page-level test results via the Production Pipeline execution page.

* Aggregate level metrics measure the average score across the pages that were audited for performance, accessibility, best practices, SEO (Search Engine Optimization). 
   >[!NOTE]
   >Progressive Web App (PWA) score is not included in the summary score and will only be shown in the page-level report details screen.
* Individual page level scores are also available via drill down.
* Details of the scores are available to see what are the results of the individual tests, along with guidance on how to remediate any issues that were identified during the experience audit.
* A history of the test results are persisted within Cloud Manager so customers can see whether changes that are being introduced in the pipeline run include any regressions from the previous run.

### Aggregate Scores {#aggregate-scores}

There is an aggregate level score for each test types such as performance, accessibility, SEO, and best practices.
>[!NOTE]
>Progressive Web App (PWA) score is not included in the summary score and will only be shown in the page-level report details screen.

The aggregate level score takes the average score of the pages that are included in the run. The change at the aggregate level represents the average score of the pages in the current run compared to the average of the scores from the previous run, even if the collection of pages configured to be included has been changed between runs. 

Value of Change metric may be one of the following:

* **Positive value** - the page(s) have improved on the selected test since the last production pipeline run

* **Negative value** - the page(s) have regressed on the selected test since the last production pipeline run

* **No Change** - the page(s) have scored the same since the last production pipeline run

* **N/A** - there was no previous score available to compare to

   ![](/help/implementing/cloud-manager/assets/exp-audit-1.png)


### Page-level Scores {#page-level-scores}

By drilling into any of the tests, more detailed page level scoring can be seen. The user will be able to see how the individual pages scored for the specific test along with the change from the previous time the test was run.

Clicking into the details of any individual page will provide information on the elements of the page that were evaluated and guidance to fix issues if opportunities for improvement are detected. The details of the tests and associated guidance are provided by Google Lighthouse. 

   ![](/help/implementing/cloud-manager/assets/exp-audit-2.png)

