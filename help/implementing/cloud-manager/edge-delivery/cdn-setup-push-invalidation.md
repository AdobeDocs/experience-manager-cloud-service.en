---
title: Setup Push Invalidation for an Edge Delivery site
description: Discover how to configure push invalidation for an Edge Delivery site to ensure efficient content updates and caching control.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
exl-id: 7cded93c-325c-4a4b-8644-e6a2379d5179
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
# Setup push invalidation for an Edge Delivery site

Push invalidation ensures that content updates made by authors are automatically deleted from the managed Content Delivery Network (CDN) when published. Doing so ensures that only the latest content is served. 

The system clears the content based on specific URLs and cache tags or keys, ensuring that outdated versions are purged.

To enable push invalidation, specific properties must be added to the project's configuration file. For example, a Microsoft Excel workbook named `.helix/config.xlsx` in SharePoint, or a Google Sheet name `.helix/config` in Google Drive. 

The following configuration properties define the production host's name and the type of CDN management:

| key | value | comment |
| --- | --- | --- |
| `cdn.prod.host` | `<Production Host>`  | Host name of the production site. For example, `www.example.com`. |
| `cdn.prod.type` | managed |   |

Once changes are made to the configuration sheet, users must preview and activate them using the [Sidekick tool](https://www.aem.live/docs/sidekick) to apply the updates.

See also [About the Edge Delivery to-do list in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/introduction-to-edge-delivery-services.md#ed-todo-list).
