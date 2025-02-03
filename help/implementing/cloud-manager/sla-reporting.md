---
title: SLA Reporting
description: Learn how to see the performance of your production AEM environment relative to the contracted Service Level Agreement (SLA).
exl-id: 03932415-a029-4703-b44a-f86a87edb328
---

# SLA Reporting {#sla-reporting} 

Learn how to see the performance of your production AEM environment relative to the contracted Service Level Agreement (SLA).

## Introduction {#introduction}

SLA reporting data is available for every production program via the **Reports** tab. Follow these steps to access.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. Using the side navigation panel, navigate to the **Reports** tab from the **Overview** page.

1. Click the year desired to see the SLA data graphed.

![SLA graph example](assets/sla-reporting-1.png)

Roll your cursor over a data point to show the specific values for that point.

![Showing detailed data](assets/sla-reporting-b.png)

## SLA Metrics {#sla-metrics}

The graph of the selected year includes several data sets.

* **Publish Tier Contract** - This is the SLA defined in your contract with Adobe for the publish tier.

* **Publish Tier Actual** - This is the measured uptime of the production publish tier factoring incidents caused by Adobe or Adobe's vendors.

* **Author Tier Contract** - This is the SLA defined in your contract with Adobe for the author tier.

* **Author Tier Actual** - This is the measured uptime of the production author tier factoring incidents caused by Adobe or Adobe's vendors.

## Event Analysis {#event-analysis}

The **Event Analysis** section under the graph shows the set of incidents which occurred for the program during the selected year. 

Each of the incidents has a time range, a cause, and a set of comments.

![Event Analysis example](assets/sla-reporting-c.png)

## Refresh Interval {#refresh}

SLA reporting gives you insight into the performance of your AEM production environment and is up-to-date, but not instantaneous. SLA report generation happens monthly and it is generated for new programs that are marked as Production previous month. It is not instant. Because of this delay, please keep the following in mind as you review your SLA report:

* The reported SLA will be the one which existed at the start of the month, even if SLA changed during that month.
* If there was no SLA at the start of the month because the program did not exist then, the SLA that existed at the date the program was created applies. 

## Preview Environments {#preview}

The preview environment is intended as a tool for content authors to verify the content's final experience before publishing. Because of this, preview environments are not designed with high-availability and do not have an associated SLA.
