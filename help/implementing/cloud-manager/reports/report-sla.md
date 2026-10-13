---
title: SLA Reports
description: Learn how to see the performance of your production AEM environment relative to the contracted Service Level Agreement.
exl-id: 03932415-a029-4703-b44a-f86a87edb328
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: a01bfd36-4ab8-4bf8-9dc0-5b45b890552e
    internal-label: APIs
subfeature_v2:
  - id: d9eb3b3e-9447-4ed4-bf4a-96c7b245cb27
    internal-label: Cloud Manager APIs
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# SLA reports {#sla-reporting} 

Learn how to see the performance of your production AEM environment relative to the contracted SLA (Service Level Agreement).

## View an SLA report {#introduction}

SLA report data tracks performance metrics for two production tiers: Author Tier and Publish Tier. 

The line graph of a selected year includes data points for each month from January to December. The following metrics are tracked.

| Metric tracked | Line color | Description |
| --- | --- | --- |
| Author Tier Actual | Light green | The measured uptime of the production Author Tier factoring incidents caused by Adobe or Adobe's vendors. |
| Author Tier Contract  | Dark blue | The SLA defined in your contract with Adobe for the Author Tier. |
| Publish Tier Actual | Orange | The measured uptime of the production Publishing Tier, factoring incidents caused by Adobe or Adobe's vendors. |
| Publish Tier Contract | Red | The SLA defined in your contract with Adobe for the Publishing Tier. |

**To view an SLA report:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. From the **Program Overview** page, in the left side menu, click **Reports**.

1. Click **SLA Reports**. 

    ![SLA report line graph](/help/implementing/cloud-manager/reports/assets/cm-sla-report2.png)

1. Click the year desired to see a line graph of SLA data.

1. (Optional) Do any of the following:

    * To show the specific values for a data point, move your cursor over it in the line graph.
    * Below the line graph's year, click the icon **Download** to save a PNG image file of the line graph.
    * Click a metric name to see that metric's data. Alternatively, press and hold `Shift` on the keyboard while selecting or deselecting one or more metric names.  

## Event analysis {#event-analysis}

The **Event Analysis** section under the graph shows the set of incidents that occurred for the program during the selected year. 

Each of the incidents has a time range, a cause, and a set of comments.

![Event Analysis example](/help/implementing/cloud-manager/reports/assets/sla-reporting-c.png)

## Refresh interval of SLA reports {#refresh}

SLA reporting provides information about the performance of your AEM production environment and is current, but not instantaneous. SLA report generation happens monthly and it is generated for new programs that are marked as `Production previous month`. It is not instantaneous. Because of this delay, keep the following in mind as you review your SLA report:

* The reported SLA is the one that existed at the start of the month, even if SLA changed during that month.
* If there was no SLA at the start of the month because the program did not exist, the SLA that existed at the date the program was created applies.

## Preview environments {#preview}

The preview environment is intended as a tool for content authors to review the content before publishing. Because of this functionality, preview environments are not designed with high availability and do not have an associated SLA.


