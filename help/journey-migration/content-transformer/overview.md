---
title: Overview to Content Transformer
description: Learn how to detect and fix content related issues reported by the BPA using Content Transformer.
exl-id: aa3397ff-3dd6-4c67-9064-cb9b19bf1c73
feature: Migration
role: Admin
---
# Overview {#overview-ct}

The Content Transformer (CT) is a tool developed by Adobe that can be used to automatically detect and fix content related issues reported by the [Best Practices Analyzer (BPA)](/help/journey-migration/best-practices-analyzer/overview-best-practices-analyzer.md) before migrating content from your current AEM implementation (On-premise or Managed Services) to AEM as a Cloud Service.

The Content Transformer can help resolve issues that fall under the following [BPA pattern categories](https://experienceleague.adobe.com/docs/experience-manager-pattern-detection/table-of-contents/aso.html) (shown in table below) by allowing users to take bulk actions such as move or delete. This can significantly reduce the time and reduce the complexity associated with a migration project.

## Pattern categories covered by Content Transformer and suggested solutions {#pattern-categories-and-benefits}

| Pattern Code | Suspicion Type / Subtype                                                                                           | Potential fix before migrating content to AEM as a Cloud Service                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| ACV          | missing.jcrcontent <br> missing.original.rendition <br> metadata.descendants.violation                                       | Move these assets to a different location or delete them to ensure they are not migrated to AEM as a Cloud Service. |
| CAV          | content.area.violation                                                                                             | Move the paths temporarily to `/etc/packages/content-transformation/paths` to ensure they are not migrated to AEM as a Cloud Service.                  |
| DOPI         | deprecated.ordered.index                                                                                           | Remove the deprecated indexes.                                                                                                      |
| OAUI         | non.migrated.oauth.users                                                                                           | Remove these users to ensure they are not migrated to AEM as a Cloud Service.                                              |
| PCX          | page.complexity.medium <br> page.complexity.high                                                                        | Delete the pages/children or move them to a different location to ensure they are not migrated to AEM as a Cloud Service.                                       |
| REP          | forward.replication <br> reverse.replication <br> standard.replication.agent.modification <br> custom.replication.agent.detection | Remove the created replication agents. <br> OR <br> Remove the modified/added properties.                                                |
| URS          | clientlibs.location <br> file.location <br> node.location <br> workflow.location                                                 | Move to the correct location to avoid issues during migration.                                                                                                       |
| URS          | node.size                                                                                                          | Move the nodes temporarily to`/etc/packages/content-transformation/paths` to ensure they are not migrated to AEM as a Cloud Service.               |

## Benefits provided by the Content Transformer {#benefits}

The Content Transformer provides the following benefits:

* Fail-safe: a package is created by the Content Transformer every time it makes any modification to the repository to fix issues. If needed, you can revert back to the previous state by installing the package.
* Easy-to-use: the Content Transformer has been integrated with the Content Transfer Tool and comes with a simple user interface that is intuitive. 
* Saves time: when you have a high number of content issues that fall under one pattern category, you can resolve them all with several clicks using the Content Transformer.
