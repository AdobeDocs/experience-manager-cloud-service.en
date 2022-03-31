---
title: Referrer Filter configuration with AEM Headless
description: Adobe Experience Manager's Referrer Filter enables access from third party hosts. An OSGi configuration for the Referrer Filter is needed to enable access to the GraphQL endpoint for headless applications.
feature: GraphQL API
exl-id: e2e3d2dc-b839-4811-b5d1-38ed8ec2cc87
---
# Referrer Filter {#referrer-filter}

 Adobe Experience Manager's Referrer Filter enables access from third party hosts. An OSGi configuration for the Referrer Filter is needed to enable access to the GraphQL endpoint for headless applications.

This is done by adding an appropriate OSGi configuration for the Referrer Filter that:

* specifies a trusted website host name; either `allow.hosts` or `allow.hosts.regexp`,
* grants access for this host name.

The name of the file must be `org.apache.sling.security.impl.ReferrerFilter.cfg.json`.

For example, to grant access for requests with the Referrer `my.domain` you can:

```xml
{
    "allow.empty":false,
    "allow.hosts":[
      "my.domain"
    ],
    "allow.hosts.regexp":[
      ""
    ],
    "filter.methods":[
      "POST",
      "PUT",
      "DELETE",
      "COPY",
      "MOVE"
    ],
    "exclude.agents.regexp":[
      ""
    ]
}
```

>[!CAUTION]
>
>It remains the customer's responsibility to:
>
>* only grant access to trusted domains 
>* make sure no sensitive information is exposed 
>* not use a wildcard [*] syntax; this will both disable authenticated access to the GraphQL endpoint and also expose it to the entire world.

>[!CAUTION]
>
>All the GraphQL [schemas](#schema-generation) (derived from Content Fragment Models that have been **Enabled**) are readable through the GraphQL endpoint.
>
>This means that you need to ensure that no sensitive data is available, as it could be leaked this way; for example, this includes information that could be present as field names in the model definition.
