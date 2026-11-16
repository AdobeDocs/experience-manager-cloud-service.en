---
title: Assets Insights
description: Learn about the unified Assets Insights dashboard and its metrics for asset management, Content Hub sharing, and delivery through Dynamic Media and AEM Sites.
role: Admin
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---

# Assets Insights {#aem-asset-insights-beta-metrics-explained}

Assets Insights provides a unified dashboard for asset activity and delivery in Adobe Experience Manager (AEM) Assets as a Cloud Service.

## What is Assets Insights? {#what-is-asset-insights}

Assets Insights shows how your team uses assets and where those assets reach customers, from upload and approval to delivery in live experiences. Use it to connect internal asset activity with the reach of your content.

The dashboard brings together metrics for Author, Content Hub, and Dynamic Media. This article explains the dashboard tabs, the Activation Overview metrics, and the data-availability considerations.

>[!IMPORTANT]
>
>The Assets Insights tab in Assets View is being deprecated. The metrics previously available there, including download reports, are now accessible in the new Insights dashboard. Breakdowns of assets by asset type and asset count by size will be available in the dashboard in a future update.

## Insights dashboard tabs {#insights-dashboard-tabs}

The **[!UICONTROL Insights]** menu provides four tabs. Use **[!UICONTROL Activation Overview]** for a cross-channel summary, and the other tabs to focus on specific areas of the asset lifecycle.

| Tab | Focus | When to use it |
| --- | --- | --- |
| **[!UICONTROL Activation Overview]** | Team activity and customer reach across channels. | Review downloads, shares, approvals, publishing, AI recommendations acted on, and asset delivery together. The quick-reference table below explains these metrics. |
| **[!UICONTROL Manage & Govern]** | Author activity in the central asset repository. | Review activity related to uploading, organizing, editing metadata, versioning, and publishing assets. See [Manage digital assets](/help/assets/manage-digital-assets.md). |
| **[!UICONTROL Discover & Share]** | Content Hub activity. | Understand how teams find, access, and share approved brand assets through the self-service portal. See [Content Hub overview](/help/assets/product-overview.md). |
| **[!UICONTROL Transform & Deliver]** | Dynamic Media activity. | Review how rich media is prepared and delivered for web, mobile, and social channels, with assets adapted to different formats and experiences. See [Work with Dynamic Media](/help/assets/dynamic-media/dynamic-media.md). |

**Activation Overview: Quick reference**

Activation Overview metrics are grouped around two questions:

- How is your team working with assets? This includes finding and sharing, approving to publish, and acting on AI guidance.
- Where are those assets reaching customers? This includes delivery through Dynamic Media and AEM Sites.

<a id="quick-reference"></a>

<table>
  <thead>
    <tr>
      <th>Section</th>
      <th>Metric</th>
      <th>What it counts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8"><strong>Team activity</strong></td>
      <td><strong>Downloads (Author)</strong></td>
      <td>Assets downloaded directly from core AEM Assets</td>
    </tr>
    <tr>
      <td><strong>Shares (Author)</strong></td>
      <td>Shareable links created in Assets View</td>
    </tr>
    <tr>
      <td><strong>Downloads (Content Hub)</strong></td>
      <td>Assets downloaded through Content Hub</td>
    </tr>
    <tr>
      <td><strong>Shares (Content Hub)</strong></td>
      <td>Shareable links created in Content Hub</td>
    </tr>
    <tr>
      <td><strong>Approve to Content Hub</strong></td>
      <td>Assets approved and published to Content Hub</td>
    </tr>
    <tr>
      <td><strong>Activate to Dynamic Media</strong></td>
      <td>Assets published into Dynamic Media</td>
    </tr>
    <tr>
      <td><strong>Activate to Sites</strong></td>
      <td>Assets published into AEM Sites</td>
    </tr>
    <tr>
      <td><strong>Content Advisor</strong></td>
      <td>AI recommendations acted on</td>
    </tr>
    <tr>
      <td rowspan="4"><strong>Customer reach</strong></td>
      <td><strong>Dynamic Media Delivery Requests</strong></td>
      <td>Total asset deliveries across all channels</td>
    </tr>
    <tr>
      <td><strong>Dynamic Media Unique Assets Served</strong></td>
      <td>Distinct assets delivered at least once</td>
    </tr>
    <tr>
      <td><strong>Dynamic Media Unique Transformations</strong></td>
      <td>Distinct asset variations delivered</td>
    </tr>
    <tr>
      <td><strong>AEM Sites Distribution</strong></td>
      <td>Asset deliveries to live AEM Sites pages</td>
    </tr>
  </tbody>
</table>

>[!NOTE]
>
>Author metrics include activity generated through both the **Author UI** and the **Admin UI**.

## How is your team working with assets? {#how-is-your-team-working-with-assets}

These metrics describe how teams find, share, approve, and publish assets, and act on AI recommendations.

### Finding & sharing {#finding--sharing}

Download and share metrics distinguish activity in Author from activity in Content Hub:

- **Downloads (Author)**: Times assets are downloaded directly from the core AEM Assets environment.
- **Shares (Author)**: Shareable links created in Assets View, giving external or unauthenticated users access without a login.
- **Downloads (Content Hub)**: Times assets are downloaded through Content Hub, the self-service space where broader teams access approved, brand-ready assets.
- **Shares (Content Hub)**: Shareable links created in Content Hub, giving other users access to selected assets or collections.

### Approving to publish {#approving-to-publish}

These metrics track approval and publishing to different destinations:

- **Approve to Content Hub**: Approving an asset from AEM Assets so it becomes available to end users in Content Hub. Only approved assets appear there.
- **Activate to Dynamic Media**: Publishing an asset into Dynamic Media so it can be processed into renditions and delivered in real time.
- **Activate to Sites**: Publishing an asset into AEM Sites so it can be delivered in real time.

### Getting AI guidance {#getting-ai-guidance}

**Content Advisor** counts the AI-generated recommendations your team acted on.

## Where are those assets reaching customers? {#where-are-those-assets-reaching-customers}

These metrics describe asset delivery through Dynamic Media and AEM Sites:

- **Dynamic Media Delivery Requests**: Total times any asset was requested and delivered across all channels through Dynamic Media. This measures overall delivery volume.
- **Dynamic Media Unique Assets Served**: Distinct assets delivered at least once in the period, counted once each regardless of requests or renditions.
- **Dynamic Media Unique Transformations**: Distinct variations of your assets delivered in the period, showing how content adapts across devices, screens, and use cases.
- **AEM Sites Distribution**: Asset deliveries to live AEM Sites pages, reaching customers on your website.

The three Dynamic Media metrics measure volume, breadth of asset use, and variations delivered, respectively. A high request count with few unique assets means a small set of assets accounts for much of the delivery volume.

## Important points to note {#important-points-to-note}

Consider the following when interpreting the dashboard:

- **Content Hub metrics displayed as `-`**: Content Hub is not enabled for your organization, or no Content Hub activity was observed during the selected period.
- **Dynamic Media metrics displayed as `-`**: Your organization does not have a Dynamic Media entitlement, or no Dynamic Media activity was observed during the selected period.
- **All dashboard metrics displayed as `-`**: For an AEM Sites-only customer, these metrics are not applicable.
- **Link shares on Author**: Folder-level asset counts are available and included from August 20, 2026.
- **Content Hub downloads**: Download data is available only from November 19, 2025.
