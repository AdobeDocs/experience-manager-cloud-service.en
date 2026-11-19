---
title: Insights dashboard in AEM Assets
description: Learn about the unified Insights dashboard and its metrics for asset management, Content Hub sharing, and delivery through Dynamic Media and AEM Sites.
role: Admin
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---

# Insights dashboard in AEM Assets {#insights-dashboard-in-aem-assets}

## Overview {#overview}

Insights is a unified dashboard in Adobe Experience Manager (AEM) Assets that shows how your team uses assets and where those assets reach customers — from upload and approval to the moment an asset appears as a product image, shared link, or hero banner. It connects what happens inside your team to the reach your content earns outside it, bringing together metrics from AEM Assets, Content Hub, Dynamic Media, AEM Sites, and Content Advisor in one place.

The Insights dashboard displays four tabs:

1. **Activation Overview:** See how your team's work turns into customer reach, across DAM, Content Hub, Dynamic Media, Sites, and Content Advisor.
2. **Manage & Govern — Author:** Manage assets in the central repository, including uploading, organizing, editing metadata, versioning, and publishing. See [Manage digital assets](/help/assets/manage-digital-assets.md) for more information on Assets view.
3. **Discovery & Share — Content Hub:** Help teams find, access, and share approved brand assets through a self-service portal. See [Content Hub Overview](/help/assets/product-overview.md) for more information on Content Hub.
4. **Transform & Deliver — Dynamic Media:** Prepare and deliver rich media for channels such as web, mobile, and social, with assets adapted to different formats and experiences. See [Work with Dynamic Media](/help/assets/dynamic-media/dynamic-media.md) for more information on Dynamic Media.

## Access Insights {#access-insights}

To open the Insights dashboard:

1. Navigate to your AEM Assets environment in Assets View.
1. In the left rail, select **[!UICONTROL Insights]**.
3. Select a tab to view its metrics. Some tabs include additional tabs, for example, **[!UICONTROL Downloads]** and **[!UICONTROL Link sharing]** for **[!UICONTROL Discovery & Share]** tab.
1. (Optional) Use the time frame drop-down list to change the reporting period. The default is **[!UICONTROL Last 30 days]**.

## Activation Overview: Quick reference {#quick-reference}

The Activation Overview tab shows how your team's work turns into customer reach, across DAM, Content Hub, Dynamic Media, Sites, and Content Advisor. Its metrics are grouped around two questions.

### How is your team working with assets? {#how-is-your-team-working-with-assets}

These team activity metrics cover downloads and sharing, approving to publish, and acting on AI guidance.

| Category | Metric | What it counts |
| --- | --- | --- |
| **Downloads & sharing** | **Downloads (Author)** | Times assets are downloaded directly from the core AEM Assets environment. |
|  | **Shares (Author)** | Shareable links created in Assets View, giving external or unauthenticated users access without a login. |
|  | **Downloads (Content Hub)** | Times assets are downloaded through Content Hub, the self-service space where broader teams grab approved, brand-ready assets. |
|  | **Shares (Content Hub)** | Shareable links created in Content Hub, giving other users access to selected assets or collections. |
| **Approving to publish** | **Approve to Content Hub** | Approving an asset from AEM Assets so it becomes available to end users in Content Hub. Only **approved** assets appear there. |
|  | **Activate to Dynamic Media** | Publishing an asset into Dynamic Media so it can be processed into renditions and delivered in real time. |
|  | **Activate to Sites** | Publishing an asset into AEM Sites so it can be delivered in real time. |
| **Getting AI guidance** | **Content Advisor** | The number of AI-generated recommendations your team acted on. |

>[!NOTE]
>
>Author metrics include activity generated through both the Assets View and Admin View.

### Where are those assets reaching customers? {#where-are-those-assets-reaching-customers}

These customer reach metrics show where assets show up in live experiences, delivered through Dynamic Media and AEM Sites.

| Metric | What it counts |
| --- | --- |
| **Dynamic Media Delivery Requests** | Total times any asset was requested and delivered across all channels through Dynamic Media. Your overall delivery volume. |
| **Dynamic Media Unique Assets Served** | Distinct assets delivered at least once in the period, counted once each regardless of requests or renditions. |
| **Dynamic Media Unique Transformations** | Distinct variations of your assets delivered in the period, showing how content adapts across devices, screens, and use cases. |
| **AEM Sites Distribution** | Asset deliveries to live AEM Sites pages, reaching customers on your website. |

## Manage & Govern: Quick reference {#manage-and-govern-quick-reference}

Find insights for the Author environment, including both Assets View and Admin view, that show how your DAM is being used and what it contains. The overview insights describe the profile of your assets: how many you have, by type and size, and what people search for most. The download and link share insights show activity both cumulatively and over time, along with your top performing assets and your most active users.

Together, these insights help you:

* **Know what your DAM holds.** Asset counts by type and size help you plan storage and spot where content is concentrated.
* **Understand what content is in demand.** Top searches, most downloaded assets, and most shared assets show which content people want and which sits unused, so you can invest in what works.
* **See how content moves beyond the DAM.** Download and link share trends show when and how assets are distributed, which supports governance and helps you spot unusual activity.
* **Identify your most engaged users.** Top 10 users by downloads and by link shares show who relies on the DAM most, so you can target training, support, and permissions.

| Section | Metric |
| --- | --- |
| **Overview** | Upload |
|  | Asset count by asset Type |
|  | Asset Count by Size |
|  | Top Searches |
| **Downloads** | Total assets downloads |
|  | Assets downloaded YTD |
|  | Assets downloads over time |
|  | Top performing: Most downloaded assets |
|  | Top 10 users by downloads |
| **Shares** | Total assets in link shares |
|  | Total assets in link shares YTD |
|  | Link shares over time |
|  | Top performing assets (most shared) |
|  | Top 10 users by link shares |

## Discovery & Share: Quick reference {#discover-and-share-quick-reference}

In this section, you will find insights for Content Hub. The section includes two tabs:

* **Downloads**: What's being downloaded from Content Hub, by whom, and how download activity is trending over time.
* **Link sharing**: What's being shared from Content Hub, by whom, and how sharing activity is trending over time.

| Section | Metric | What it counts |
| --- | --- | --- |
| **Downloads** | **Total downloads** | Number of assets downloaded from Content Hub during the selected period. |
|  | **Unique downloaders** | Number of distinct users who downloaded assets from Content Hub during the selected period. |
|  | **Downloads over time** | Number of assets downloaded from Content Hub during the selected period. |
|  | **Top performing assets** | Assets ranked by their number of downloads from Content Hub during the selected period. |
|  | **Downloads log** | Displays the details for the last 100 assets. Download the CSV to see all. |
| **Link sharing** | **Links created** | Number of private and public sharing links created in Content Hub during the selected period. |
|  | **Links viewed** | Number of views of private and public Content Hub sharing links during the selected period. |
|  | **Links created over time** | Private and public links created over time, grouped by day, week, or month for the selected period. |
|  | **Link views over time** | Daily views of private and public Content Hub sharing links during the selected period. |

>[!NOTE]
>
>Data for Links created and Links viewed starts on October 22, 2026. If your selected date range begins earlier, results will only reflect data from this date forward.

## Transform & Deliver: Quick reference {#transform-and-deliver-quick-reference}

Find insights for Dynamic Media that show how your assets are transformed and delivered to customers across channels. The performance insights describe your delivery volume, the distinct assets and variations served, the bandwidth saved through optimization, and how requests break down by asset type, device, browser, format, and referring domain. The error insights show failed delivery requests, both as totals and over time, along with the error rate, response classes, top error URLs, and error reasons.

Together, these insights help you:

* **Understand your delivery reach.** Delivery requests, unique assets served, and unique transformations show how much content Dynamic Media delivers and how it adapts across devices, screens, and use cases.
* **Measure the value of optimization.** Bandwidth saved and the distribution of delivered image and video formats show how Dynamic Media optimization reduces delivery size compared with the original renditions.
* **See how your assets perform.** Requests by asset type, delivery by channel, traffic by browser, and top referral domains show where and how customers access your assets, including your top performing and low performing assets.
* **Find and fix delivery issues.** Error rate, errors by response class, top error URLs, and error reasons help you identify failing requests and prioritize fixes.

| Section | Metric | What it counts |
| --- | --- | --- |
| **Performance** | **Bandwidth saved through optimization** | Bytes saved through Dynamic Media optimisation (format, quality and responsive delivery) versus delivering the original renditions |
|  | **Delivery requests** | Total asset requests delivered via Dynamic Media |
|  | **Unique assets served** | Number of distinct assets delivered via Dynamic Media across the selected time period |
|  | **Unique transformations** | Distinct asset variations delivered via Dynamic Media across the selected time period |
|  | **Unique transformations per asset** | Average number of distinct variants delivered per asset |
|  | **Top referral domains** | Top domains that requested your assets |
|  | **Delivery requests trend** | Total asset requests delivered via Dynamic Media across the selected time period |
|  | **Requests by asset type** | Delivery requests by asset type |
|  | **Delivery by channel** | Delivery requests by device type |
|  | **Top delivered image formats** | Distribution of delivered image formats (For example, WebP, AVIF, JPEG, PNG) |
|  | **Top delivered video formats** | Distribution of delivered video formats (For example, MP4, HLS) |
|  | **Traffic by browser** | Delivery requests by browser type |
| **Errors** | **Total Delivery requests** | Total asset requests delivered via Dynamic Media |
|  | **Total errors** | Total failed delivery requests in the selected period, across all error types |
|  | **Error Rate** | Percentage of delivery requests that failed in the selected period |
|  | **Error by response class** | Number of errors in each HTTP response class (4xx, 5xx) |
|  | **Error rate trend** | Percentage of delivery requests that failed, over a period of time |
|  | **Top error URLs** | Delivery URLs with the most failed requests |
|  | **Error reasons** | Error causes grouped by category, with a hit count for each |
| **Sites distribution** | **Delivery requests** | Total requests served for assets delivered through AEM Sites pages. |
|  | **Top performing assets** | Assets with the most delivery requests from AEM Sites pages |
|  | **Top referral domains** | Pages sending the most delivery requests for your Sites assets. |
|  | **Delivery requests trends** | Delivery requests for Sites assets over the selected time range. |
|  | **Requests by asset type** | Share of Sites delivery requests by the type of asset served. |
|  | **Delivery by channel** | Share of Sites delivery requests by the device that requested them. |
|  | **Traffic by location** | Sites delivery requests by the region they were served to. |
|  | **Traffic by browser** | Sites delivery requests by the browser that requested them. |

>[!NOTE]
>
>In Top referral domains, N/A indicates referral source is unknown.


## Important points to note {#important-points-to-note}

The following will need to be taken into account if:

1. Content Hub metrics are displayed as '-', then one of the following applies:
    1. Content Hub metrics are not applicable because Content Hub is not enabled for the customer.
    2. No Content Hub activity was observed during the selected period.
2. Dynamic Media metrics are displayed as '-', then one of the following applies:
    1. Dynamic Media metrics are not applicable because the customer does not have a Dynamic Media entitlement.
    2. No Dynamic Media activity was observed during the selected period.
3. All metrics in your dashboard are displayed as '-':
    1. This is an AEM Sites-only customer. Metric is not applicable.
4. **Note**: Link share on Author:
    1. Folder-level asset counts are available and included from August 20, 2026.
5. **Note**: Content Hub downloads:
    1. Content Hub downloads is available starting November 19, 2025.