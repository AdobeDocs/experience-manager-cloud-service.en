---
title: Health Assessment for Production and Stage Environments
description: Learn how to use Cloud Manager's Health Assessment. You can scan AEM environments, run and review reports, view issue details, export PDFs, and manage past runs.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
exl-id: 5467a311-727d-4f67-ba43-4b6548431061
---
# Health Assessment {#about-health-assessment}

Health Assessment is an automated, non-intrusive scan for Production and Stage environments in Cloud Manager within AEM as a Cloud Service. It evaluates content, code, and configurations to find anti-patterns and departures from best practices, improving security and performance.

The health assessment service does the following:

* Scans environments and exposes performance bottlenecks, inefficiencies, and risks.
* Analyzes content structures, such as blueprints, live copies, and customer configurations.
* Detects outdated dependencies, including AEM SDK and third-party libraries.
* Flags code quality issues, such as incorrect annotations and inefficient patterns.
* Delivers actionable guidance in dashboards (for example, Action Center).
* Drives proactive remediation to improve system performance.

Each run lists issues by severity, links to guidance and recommended fixes, and supports a PDF export of the report. You can use the **Latest Report** view for the current state and **Past Reports** to compare runs.

See also [Health Assessment patterns](#ha-patterns) for rule definitions and remediation details.

## Access the Health Assessment page {#access-health-assessment}

1. Sign into Cloud Manager at [experiece.adobe.com](https://experience.adobe.com).
1. In the **Quick access** section, click **Experience Manager**.
1. In the left side panel, click **Cloud Manager**.
1. Select an organization that you want. The image below is for illustration. Select your own organization name.

    ![Selecting an organization in Cloud Manager](/help/implementing/cloud-manager/reports/assets/ha-org.png)

1. On the **My Programs** console, click the program for which you want to view its report. 

1. Do either one of the following:
    * In the **Environments** card, to the right of an environment name, click ![Ellipsis icon or More icon](https://spectrum.adobe.com/static/icons/ui_18/More.svg), then choose **Health Assessment** from the menu.

        ![Selecting Health Assessment from the ellipsis menu in the Environments card](/help/implementing/cloud-manager/reports/assets/ha-myprograms-environments-card.png) 

    * From the left side menu, under **Services**, click ![Data icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Data_18_N.svg) **Environments**. On the Environments page, to the right of an environment name, click ![Ellipsis icon or More icon](https://spectrum.adobe.com/static/icons/ui_18/More.svg), then choose **Health Assessment** from the menu.

        ![Selecting Health Assessment from the ellipsis menu on the Environments page](/help/implementing/cloud-manager/reports/assets/ha-environments-page.png) 

## Run a new report for a selected environment {#run-report}

1. [Access the Health Assessment page](#access-health-assessment).
1. In the upper-right corner of the **Health Assessment** page, confirm the target environment that you are about to assess.

    If the environment is incorrect, click ![Chevron down or drop-down menu to selected a different environment](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ChevronDown_18_N.svg) to choose the correct environment from the list.

1. Click **Run Report**.

    ![Click the Generate new report button on the Health Assessment page](/help/implementing/cloud-manager/reports/assets/ha-run-report.png)

    While a report runs for the selected environment, **Run Report** stays disabled until it finishes.

    ![Report in the middle of running](/help/implementing/cloud-manager/reports/assets/ha-running-report.png)

    When the report is complete, the report appears on the **Health Assessment** page, in the **Latest Report** section.

## View the latest report {#view-latest-report}

* On the **Health Assessment** page, review the **Latest report** section for the following information:

    * Results from the most recent run.
    * Run date and time.
    * Total issue count.
    * Highlights of top critical issues.
    * Actions: **[View details](#view-report-details)** or **[Download PDF](#download-pdf-report)** of all issues.

    ![The Latest Assessment page following the generation of a new report for a selected environment](/help/implementing/cloud-manager/reports/assets/ha-latest-report-page.png)

### View the latest report details {#view-report-details}

* On the **Health Assessment** page, to the right of the **Latest Report** title, click ![Ellipsis icon or More icon](https://spectrum.adobe.com/static/icons/ui_18/More.svg), then click **View details** or **Download**.

    The **View details** option shows you the following:
    
    * A comprehensive list of issues.
    * Ability to view findings and issue descriptions.
    * Ability to view documentation with potential fixes.

        ![Issue descriptions and finding](/help/implementing/cloud-manager/reports/assets/ha-issue-descriptions-and-findings.png)
    
    * The **Download** option gives you the ability to download individual issue reports in PDF.

        ![Download PDF of individual issue reports](/help/implementing/cloud-manager/reports/assets/ha-details-page-doc-links.png)


### Download PDF of entire report {#download-pdf-report}

* Near the upper-right corner of the report page, click **Download**.

    A ZIP file is generated that contains PDFs for all issues detected in that report.

    ![Download PDF of all issues found in a report](/help/implementing/cloud-manager/reports/assets/ha-download-pdf.png)


## Review past reports {#review-past-reports}

On the **Health Assessment** page, review the **Past Reports** section for the following information:

* View details of any prior report.
* View each run's date.
* Download a PDF for any report.
* Sort by date, issue count, or environment.

![Review past reports](/help/implementing/cloud-manager/reports/assets/ha-past-reports.png)

* To the right of the **Past Reports** heading, click ![Chevron down or drop-down menu to selected a different environment](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ChevronDown_18_N.svg) to sort past reports by date.
* To the far right of a report, click ![Ellipsis icon or More icon](https://spectrum.adobe.com/static/icons/ui_18/More.svg), then click **View details** or **Download**.


## Health Assessment patterns {#ha-patterns}

The following is the full list of anti-patterns and issues that Health Assessment detects in AEM as a Cloud Service. The table groups items into three types: Content Analysis, Code Analysis, and Cloud Service Optimizer anti-patterns, with an explanation for each.

| Pattern name | Category | Type | Description | Impact | Auto-fixed? |
| --- | --- | --- | --- | --- | --- |
| Custom AEM Groups with Direct User Additions | Security | Content Analysis | Users added directly to AEM groups instead of adding IMS groups as members. | Permission management and security governance can become complicated. [IMS Support](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/ims-support) | No |
| Missing JCR Content Node in Pages | Repository Structure| Content Analysis | Missing `jcr:content` node in page. | Functional limitations in Experience Manager as a Cloud Service. [Pattern detection - ACV](https://experienceleague.adobe.com/en/docs/experience-manager-pattern-detection/table-of-contents/acv) | No |
| Missing Sling Resource Type in Pages | Repository Structure | Content Analysis | Missing `sling:resourceType` in page.  | Functional limitations in Experience Manager as a Cloud Service. [Pattern detection - ACV](https://experienceleague.adobe.com/en/docs/experience-manager-pattern-detection/table-of-contents/acv) | No |
| Pages with Excessive Node Count | Performance | Content Analysis | Pages contain a large number of nodes in their structure. | Slow page load times and poor user experience. [Pattern detection - PCX](https://experienceleague.adobe.com/en/docs/experience-manager-pattern-detection/table-of-contents/pcx) | No |
| Excessive Running Workflow Instances | Performance | Content Analysis | Too many workflow instances are running. | Overall system performance degradation. [Maintenance tasks](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/maintenance) | No |
| Unpurged Completed Workflow Instances | Performance | Content Analysis | Older completed workflow instances are not being purged. | Decreased system efficiency and increased storage costs. [Maintenance tasks](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/maintenance) | No |
| Content Fragment Usage Statistics | Statistics | Content Analysis | Tracks the number of Content Fragments in use. | N/A | N/A |
| Content Fragment Model Usage Statistics | Statistics | Content Analysis | Tracks the number of Content Fragment Models in use. | N/A | N/A |
| MSM Large Number of Blueprints | Statistics | Content Analysis | Tracks the number of blueprints. | It can increase management complexity and make content governance more difficult. | N/A |
| MSM Pages per Blueprint | Statistics | Content Analysis | Tracks the number of pages per blueprint. | It can increase management complexity and make content governance more difficult. | N/A |
| MSM Excessive Live Copies | Statistics | Content Analysis | Tracks the number of live copies. | It can lead to performance issues during rollouts and complicate content synchronization. | N/A |
| MSM Excessive Live Copies per Blueprint | Statistics | Content Analysis | Tracks the number of live copies per blueprint. | It can lead to performance issues during rollouts and complicate content synchronization. | N/A |
| Number of Assets | Statistics | Content Analysis | Tracks the number of assets. | N/A | N/A |
| Number of Sites | Statistics | Content Analysis | Tracks the number of sites. | N/A | N/A |
| Number of Forms | Statistics | Content Analysis | Tracks the number of forms. | N/A  | N/A |
| Form Fragments | Statistics | Content Analysis | Tracks the number of form fragments. | N/A | N/A |
| Interaction Communications | Statistics | Content Analysis | Tracks the number of form communication interactions. | N/A | N/A |
| FDMs | Statistics | Content Analysis | Tracks the number of form data models. | N/A | N/A |
| Outdated Dependencies | Dependencies | Code Analysis | Highlights outdated dependencies in the customer repository. | Incompatibility with newer AEM versions; potential security vulnerabilities. | No |
| AEM SDK Version Mismatch | Dependencies | Code Analysis | Versions older than (n-2) compared to the Cloud Manager environment version. | It can cause build errors in Cloud Manager and issues in local development environments.  | No |
| Outdated Mockito Core Dependency | Dependencies | Code Analysis | Versions below 4.x.x are considered outdated for AEM as a Cloud Service. | It can cause build errors in Cloud Manager and issues in local development environments. | No |
| Unsupported Annotations | Dependencies | Code Analysis | Unsupported annotations in the customer's Cloud Manager repository. | Potential application failures and decreased performance. | No |
| @Inject Annotation in Sling Models | Dependencies | Code Analysis | Deprecated `@Inject` annotation. | Reduced application performance due to injection resolution overhead. | No |
| Outbound HTTP Requests | Performance | Cloud Service Optimizer anti-patterns | Problematic use in request context, high timeouts, or not closing connections. | Overall system performance degradation and possible outages. | Yes |
| Slow Queries | Performance | Cloud Service Optimizer anti-patterns | Slow queries in customer code. | Degraded system performance and potential timeouts. | Yes |

### Categories {#ha-patterns-categories}

| Category | Description |
| --- | --- |
| Security | Patterns related to security practices, user management, and access control. |
| Performance | Patterns that impact application and system performance. |
| Repository Structure | Patterns related to JCR repository organization and structure. |
| Dependencies | Patterns related to code dependencies and version management. |
| Statistics | Patterns that represent usage statistics and metrics. |
