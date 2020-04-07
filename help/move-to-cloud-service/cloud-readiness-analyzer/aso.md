---
title: AEM System Overview
description: AEM System Overview
---

# AEM System Overview {#aem-system}

This page describes Adobe Experience Manager (AEM) System Overview.

## Background {#background}

This pattern is used to identify general information that provides an overview of the AEM system. Information can include items such as:

AEM version
AEM products used (Sites, Assets, Forms, and so on)
Node counts (pages, assets, and so on)

## Pattern Data {#pattern-data}

The following objects are included in the JSON representation of the pattern:

* **item.message**: refers to the message of the pattern.
* **item.context**: refers to additional information about the overview information:
   * *type*: The type of context data, either "aem.version", "aem.product", or "node.count".
   * *data*: A JSON object containing the data corresponding to the type: "version" (string), "product" (string), or "count" (integer).

### Possible implications and risks {#possible-implications}

Not applicable.

### Possible solutions  {#possible-solutions} 

Not applicable.
