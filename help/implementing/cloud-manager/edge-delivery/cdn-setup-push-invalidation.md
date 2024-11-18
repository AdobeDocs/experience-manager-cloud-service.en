---
title: Setup Push Invalidation for an Edge Delivery site
description: Discover how to configure push invalidation for an Edge Delivery site to ensure efficient content updates and caching control.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
exl-id: 7cded93c-325c-4a4b-8644-e6a2379d5179
---
# Setup push invalidation 

Push invalidation ensures that content updates made by authors are automatically removed from the managed Content Delivery Network (CDN) when published. Doing so ensures that only the latest content is served. 

The system clears the content based on specific URLs and cache tags or keys, ensuring that outdated versions are purged.

To enable push invalidation, specific properties must be added to the project's configuration file. For example, a Microsoft Excel workbook named `.helix/config.xlsx` in SharePoint, or a Google Sheet name `.helix/config` in Google Drive. 

The following configuration properties define the production host's name and the type of CDN management:

| key | value | comment |
| --- | --- | --- |
| `cdn.prod.host` | `<Production Host>`  | Host name of the production site. For example, `www.example.com`. |
| `cdn.prod.type` | managed |   |

Once changes are made to the configuration sheet, users must preview and activate them using the [Sidekick tool](/help/edge/docs/sidekick.md) to apply the updates.

See also [About the Edge Delivery to-do list in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/introduction-to-edge-delivery-services.md#ed-todo-list).
