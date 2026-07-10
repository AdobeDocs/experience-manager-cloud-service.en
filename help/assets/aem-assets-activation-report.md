---
title: AEM Assets Activation report (Beta)
description: Definitions for AEM Assets Activation report (Beta) metrics, covering activations (downloads, shares) and distributions (Dynamic Media, Sites)."
role: Admin
hide: true
hidefromtoc: yes
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
---

# AEM Assets Activation Report (Beta): Metrics definitions

## Understanding Your Asset Performance Metrics

Every asset in your AEM Assets system tells a story: from upload and approval to the moment it reaches a shopper as a product image, shared link, or hero banner. That journey drives billions of brand impressions, and understanding it is key to unlocking the value of your asset investment.

This article breaks down the metrics behind that journey, grouped the way your teams actually work with assets:

- **Activations (Employee & Partner initiated)**: downloads, shares, and activations across your AEM Assets (Assets View and Content Hub).
- **Distributions (External to end users)**: delivery to the world through channels like Dynamic Media and AEM Sites.

Together, these metrics connect internal asset activity to external reach and engagement, helping you see how your content operations translate into real business outcomes.

This is just the start of your journey with AEM Assets, and these metrics will keep evolving alongside it. We'd love your feedback as you put them to use, so we can keep making this reporting more useful for you.

**Note**: If you wish to review these with Adobe Product/Engineering or have feedback, send an email to `GRP-AEM-DAM-METRICS-BETA@ADOBE.COM`.

| | Metric | Definition |
|---|---|---|
| **Activations** | **Downloads (Assets View)** | The number of times assets are downloaded directly from the core AEM Assets environment, for example, by internal users browsing and downloading files through the Assets view interface. |
| | **Link Share (Assets View)** | The number of shares (via shareable links generated) from within AEM Assets View in order to give external or unauthenticated users direct access to specific assets, folders, or collections without requiring to login. |
| | **Downloads (Content Hub)** | The number of times assets are downloaded by users through Content Hub, the self-service UI that lets broader teams browse and download approved, brand-ready assets. |
| | **Shares (Content Hub)** | The number of shares (via shareable links generated) from within Content Hub in order to give other users direct access to selected assets or collections. |
| | **Activate to Content Hub** | The action of approving/publishing an asset from AEM Assets so it becomes available to end users in Content Hub. Only approved assets appear in Content Hub. |
| | **Activate to Dynamic Media** | The action of publishing an asset from AEM Assets into the Dynamic Media service, enabling it to be processed into renditions and delivered in real time via Dynamic Media's imaging/video pipeline and CDN. |
| **Distributions** | **Dynamic Media Delivery Requests** | The total number of times any asset was requested and delivered across all channels via Dynamic Media. |
| | **Dynamic Media Unique Assets Served** | The number of distinct assets that were delivered at least once via Dynamic Media in a given period, counted once per asset regardless of how many times it was requested or how many different renditions of it were served. |
| | **Dynamic Media Unique Transformations** | The number of distinct variations of your assets that were delivered via Dynamic Media in a given period. This shows how your content adapts across devices, screen sizes, and use cases. |
| | **Publish to Sites** | The action of publishing an asset from AEM Assets so it becomes available for use on live AEM Sites pages. |



