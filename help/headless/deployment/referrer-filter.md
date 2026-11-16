---
title: Referrer Filter configuration with AEM Headless
description: Adobe Experience Manager's Referrer Filter enables access from third-party hosts. An OSGi configuration for the Referrer Filter is needed to enable access to the GraphQL endpoint for headless applications.
feature: Headless, GraphQL API
exl-id: e2e3d2dc-b839-4811-b5d1-38ed8ec2cc87
solution: Experience Manager
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: bfd4bc52-c397-5127-8f86-8953ba9fc0a3
    internal-label: Headless
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Referrer Filter {#referrer-filter}

 Adobe Experience Manager's Referrer Filter enables access from third-party hosts. 
 
An OSGi configuration for the Referrer Filter is needed to enable access to the GraphQL endpoint for headless applications over HTTP POST. When using AEM Headless Persisted Queries which access AEM over HTTP GET, a Referrer Filter configuration is not needed.
 
>[!WARNING]
> AEM's Referrer Filter is not an OSGi configuration factory, meaning only one configuration is active on an AEM service at a time. When possible, avoid adding custom Referrer Filter configurations, as this will overwrite AEM's native configurations, and may break the product functionality. 

This is done by adding an appropriate OSGi configuration for the Referrer Filter that:

* specifies a trusted website host name; either `allow.hosts` or `allow.hosts.regexp`,
* grants access for this host name.

The name of the file must be `org.apache.sling.security.impl.ReferrerFilter.cfg.json`.

## Example Configuration {#example-configuration}

For example, to grant access for requests with the Referrer `my.domain` you can:

>[!CAUTION]
>
>This is a basic example that may overwrite the standard configuration. You need to ensure that product updates are always applied to any customizations. 

```xml
{
    "allow.empty": false,
    "allow.hosts": [
      "my.domain"
    ],
    "allow.hosts.regexp": [
      ""
    ],
    "filter.methods": [
      "POST",
      "PUT",
      "DELETE",
      "COPY",
      "MOVE"
    ],
    "exclude.agents.regexp": [
      ""
    ]
}
```

## Data Security {#data-security}

>[!CAUTION]
>
>It remains your responsibility to fully address the following points.

To ensure that your data remains secure you must ensure that:

* access is **only** granted to trusted domains 

* wildcard [`*`] syntax in **not** used; this both disables authenticated access to the GraphQL endpoint, and also exposes it to the entire world

* sensitive information is **never** exposed; neither directly, nor indirectly:

  * For example, all the [GraphQL schemas](/help/headless/graphql-api/content-fragments.md#schema-generation) are:

    * derived from Content Fragment Models that have been **Enabled**

    **and**

    * are readable through the GraphQL endpoint 

    This means that information present as field names in the model definition can become available.

You must ensure that no sensitive data is available by any means, so such details must be carefully considered. 
