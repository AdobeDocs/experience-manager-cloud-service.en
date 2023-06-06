---
title: Overview to Content Transformer
description: Overview to Content Transformer
---
# Overview {#overview-ct}

The Content Transformer (CT) is a tool developed by Adobe that can be used to automatically detect and fix content related issues reported by the [Best Practices Analyzer (BPA)](/help/journey-migration/best-practices-analyzer/overview-best-practices-analyzer.md) before migrating content from your current AEM implementation (On-premise or Managed Services) to AEM as a Cloud Service.

The Content Transformer can help resolve issues that fall under the following BPA pattern categories (shown in table below) by allowing users to take bulk actions such as move or delete. This can significantly reduce the time and reduce the complexity associated with a migration project.

## Pattern categories covered by Content Transformer and suggested solutions {#pattern-categories-and-benefits}

| Pattern Code  | Suspicion Type / Subtype                                                                                           | Description | Potential fix / Resolution before moving to AEMaaCS                                                                                |
|---------------|--------------------------------------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| URS           | clientlibs.location <br> file.location <br> node.location <br> workflow.location                                                 |             | Move to the right location                                                                                                         |
| URS           | node.size                                                                                                          |             | Move the node temporarily to "/etc/packages/content-transformation/paths" to avoid it being part of the migration                  |
| REP           | forward.replication reverse.replication standard.replication.agent.modification custom.replication.agent.detection |             | Remove the newly created replication agents OR Remove the modified/added properties                                                |
| PCX           | page.complexity.medium page.complexity.high                                                                        |             | delete/move the pages/children to different locations to reduce the complexity of migration                                        |
| OAUI          | non.migrated.oauth.users                                                                                           |             | Use the remove functionality to prevent these users from getting migrated to AEMaaCS                                               |
| DOPI          | deprecated.ordered.index                                                                                           |             | Remove the deprecated indexes                                                                                                      |
| CAV           | content.area.violation                                                                                             |             | Move the paths temporarily to "/etc/packages/content-transformation/paths" to avoid it being part of the migration                 |
| ACV           | missing.jcrcontent missing.original.rendition metadata.descendants.violation                                       |             | Move/Remove these assets to a different location to prevent  from getting migrated to prevent issues during the migration process. |

## Benefits provided by the Content Transformer {#benefits}
