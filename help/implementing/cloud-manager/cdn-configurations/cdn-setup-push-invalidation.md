---
title: Setup Push Invalidation
description: Learn about how to configure push invalidation for building your own production CDN. 
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
hide: yes
hidefrom toc: yes

---
# Setup push invalidation 

Push invalidation ensures that content updates made by authors are automatically removed from the managed Content Delivery Network (CDN) when published, so only the latest content is served. 

The system clears the content based on specific URLs and cache tags or keys, ensuring that outdated versions are purged.

To enable push invalidation, specific properties must be added to the project's configuration file. For example, a Microsoft Excel workbook named `.helix/config.xlsx` in SharePoint, or a Google Sheet name `.helix/config` in Google Drive. 

The following configuration properties define the production host's name and the type of CDN management:

| key | value | comment |
| --- | --- | --- |
| `cdn.prod.host` | `<Production Host>`  | Host name of the production site. For example, `www.example.com`. |
| `cdn.prod.type` | managed |   |

Once changes are made to the configuration sheet, users must preview and activate them using the [Sidekick tool](/help/edge/docs/sidekick.md) to apply the updates.
