---
title: AEM Assets Activation report (Beta)
description: Definitions for AEM Assets Activation report (Beta) metrics, covering activations (downloads, shares) and distributions (Dynamic Media, Sites)."
role: Admin
hide: true
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
---

# AEM Asset Insights (Beta): Metrics explained {#aem-asset-insights-beta-metrics-explained}


## What is Asset Insights? {#what-is-asset-insights}

Asset Insights shows how your team uses assets and where those assets reach customers — from upload and approval to the moment an asset appears as a product image, shared link, or hero banner. It connects what happens inside your team to the reach your content earns outside it.

**Metrics are grouped around two questions:**

- How is your team working with assets? — finding and sharing, approving to publish, and acting on AI guidance.
- Where are those assets reaching customers? — where assets show up in live experiences, delivered through Dynamic Media and AEM Sites.

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
      <td rowspan="7"><strong>Team activity</strong></td>
      <td><strong>Downloads (Assets View)</strong></td>
      <td>Assets downloaded directly from core AEM Assets</td>
    </tr>
    <tr>
      <td><strong>Shares (Assets View)</strong></td>
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
      <td><strong>AEM Sites Distribution</strong> <em>(coming soon)</em></td>
      <td>Assets published to live AEM Sites pages</td>
    </tr>
  </tbody>
</table>

## How is your team working with assets? {#how-is-your-team-working-with-assets}


### Finding & sharing {#finding--sharing}

- **Downloads (Assets View)** — Times assets are downloaded directly from the core AEM Assets environment.
- **Shares (Assets View)** — Shareable links created in Assets View, giving external or unauthenticated users access without a login.
- **Downloads (Content Hub)** — Times assets are downloaded through Content Hub, the self-service space where broader teams grab approved, brand-ready assets.
- **Shares (Content Hub)** — Shareable links created in Content Hub, giving other users access to selected assets or collections.

Splitting downloads and shares by source shows whether activity comes from your core creative operations (Assets View) or from the wider organization using approved assets (Content Hub) — two different signals about how content spreads.

## Approving to publish {#approving-to-publish}

- **Approve to Content Hub** — Approving an asset from AEM Assets so it becomes available to end users in Content Hub. Only approved assets appear there.
- **Activate to Dynamic Media** — Publishing an asset into Dynamic Media so it can be processed into renditions and delivered in real time.

Both are publishing steps to different destinations. Approving to Content Hub makes an asset browsable and downloadable by people; activating to Dynamic Media puts it into the pipeline that serves live customer experiences.

### Getting AI guidance {#getting-ai-guidance}

- **Content Advisor** — The number of AI-generated recommendations your team acted on.

A low number is not a problem — it just means there is room to lean on these suggestions more as you go. It's a signal of opportunity, not a warning.

## Where are those assets reaching customers? {#where-are-those-assets-reaching-customers}

- **Dynamic Media Delivery Requests** — Total times any asset was requested and delivered across all channels through Dynamic Media. Your overall delivery volume.
- **Dynamic Media Unique Assets Served** — Distinct assets delivered at least once in the period, counted once each regardless of requests or renditions.
- **Dynamic Media Unique Transformations** — Distinct variations of your assets delivered in the period, showing how content adapts across devices, screens, and use cases.
- **AEM Sites Distribution** *(coming soon)* — Assets published from AEM Assets to live AEM Sites pages, reaching customers on your website.

These three answer different questions about the same activity. Delivery Requests is raw volume; Unique Assets Served is breadth (how much of your library is in use); Unique Transformations is adaptability. A high request count with few unique assets means a small set is doing heavy lifting.

### Asset Insights is still evolving {#asset-insights-is-still-evolving}

These metrics will keep growing alongside your use of AEM Assets. We would love your feedback as you put them to work.

**Questions or feedback?** Email [GRP-AEM-DAM-METRICS-BETA@ADOBE.COM](mailto:GRP-AEM-DAM-METRICS-BETA@ADOBE.COM) to reach Adobe Product and Engineering.

