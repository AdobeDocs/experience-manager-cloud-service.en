---
title: Overview to Content Transformer
description: Overview to Content Transformer
---
# Overview {#overview-ct}

The Content Transformer (CT) is a tool developed by Adobe that can be used to automatically detect and fix content related issues reported by the [Best Practices Analyzer (BPA)](/help/journey-migration/best-practices-analyzer/overview-best-practices-analyzer.md) before migrating content from your current AEM implementation (On-premise or Managed Services) to AEM as a Cloud Service.

The Content Transformer can help resolve issues that fall under the following [BPA pattern categories](https://experienceleague.adobe.com/docs/experience-manager-pattern-detection/table-of-contents/aso.html) (shown in table below) by allowing users to take bulk actions such as move or delete. This can significantly reduce the time and reduce the complexity associated with a migration project.

## Pattern categories covered by Content Transformer and suggested solutions {#pattern-categories-and-benefits}

| Pattern Code | Suspicion Type / Subtype                                                                                           | Description  | Potential fix / Resolution before moving to AEMaaCS                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------|
| ACV          | missing.jcrcontent <br> missing.original.rendition <br> metadata.descendants.violation                                       |              | Move/Remove these assets to a different location to prevent  from getting migrated to prevent issues during the migration process. |
| CAV          | content.area.violation                                                                                             |              | Move the paths temporarily to `/etc/packages/content-transformation/paths` to avoid it being part of the migration                 |
| DOPI         | deprecated.ordered.index                                                                                           |              | Remove the deprecated indexes                                                                                                      |
| OAUI         | non.migrated.oauth.users                                                                                           |              | Use the remove functionality to prevent these users from getting migrated to AEMaaCS                                               |
| PCX          | page.complexity.medium <br> page.complexity.high                                                                        |              | delete/move the pages/children to different locations to reduce the complexity of migration                                        |
| REP          | forward.replication <br> reverse.replication <br> standard.replication.agent.modification <br> custom.replication.agent.detection |              | Remove the newly created replication agents OR Remove the modified/added properties                                                |
| URS          | clientlibs.location <br> file.location <br> node.location <br> workflow.location                                                 |              | Move to the right location                                                                                                         |
| URS          | node.size                                                                                                          |              | Move the node temporarily to`/etc/packages/content-transformation/paths` to avoid it being part of the migration                  |

## Benefits provided by the Content Transformer {#benefits}

The Content Transformer provides the following benefits:

* Fail-safe: a package is created by the Content Transformer every time it makes any modification to the repository to fix issues. If needed, you can revert back to the previous state by installing the package.
* Easy-to-use: the Content Transformer has been integrated with the Content Transfer Tool and comes with a simple user interface that is intuitive. 
* Saves time: when you have a high number of content issues that fall under one pattern category, you can resolve all of them with just a couple of clicks using the Content Transformer.
