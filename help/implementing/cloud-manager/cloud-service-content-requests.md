---
title: Cloud Service Content Requests
description: Learn about Content Requests that have variances with an organization's Analytics reporting tools.

---

# Variances of Cloud Service Content Requests{#content-requests-variances}

Content Requests have variances with an organization's Analytics reporting tools as summarized in the following table.

|Reason For Variance|Explanation|
|---|---|
|Tagging|All pages that are tracked as Adobe Experience Manager (AEM) content requests may or may not be tagged with Analytics tracking. All API calls that are tracked as AEM content requests are not tagged by an organization's Analytics tool.<br>Pages or API calls may be tagged to track actions or unique page views instead of all views.|
|Tag Management Rules|Tag management rule settings may result in various data collection configurations on a page, resulting in some combination of discrepancies with content request tracking.|
|Bots|Unknown bots that have not been pre-identified and removed by AEM may cause tracking discrepancies.|
|Report Suites|Pages that are part of the same AEM instance and domain may send data to different Analytics report suites.|
|Third-Party Monitoring and Security Tools|Monitoring and security scanning tools may generate content requests for AEM that are not tracked in Analytics reports.|
|Prefetch Requests|Using a prefetch service to pre-load pages to increase speed can cause significant content request traffic increases.|
|DDOS|While Adobe makes every effort to automatically detect and filter out traffic from DDOS attacks, there is no guarantee that all possible DDOS attacks are detected|
|Traffic Blockers|Using a tracker blocker in a browser may opt out some requests from being tracked.|
|Firewalls|Firewalls may block Analytics tracking. This scenario is more frequent with corporate firewalls.|

See also [Understanding Content Requests](/help/implementing/cloud-manager/content-requests.md) and [License Dashboard](/help/implementing/cloud-manager/license-dashboard.md).