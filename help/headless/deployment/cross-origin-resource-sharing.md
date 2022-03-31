---
title: Cross-Origin Resource Sharing (CORS) configuration with AEM Headless
description: Adobe Experience Manager's Cross-Origin Resource Sharing (CORS) allows headless web applications to make client-side calls to AEM. A CORS configuration is needed to enable access to the GraphQL endpoint.
feature: GraphQL API
exl-id: 426be9f9-f44a-4744-ac08-e64bb97308a0
---
# Cross-Origin Resource Sharing (CORS) configuration

>[!NOTE]
>
>For a detailed overview of the CORS resource sharing policy in AEM see [Understand Cross-Origin Resource Sharing (CORS)](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/security/understand-cross-origin-resource-sharing.html#understand-cross-origin-resource-sharing-(cors)).

To access the GraphQL endpoint, a CORS policy must be configured and added to an AEM Project that is [deployed to AEM via Cloud Manager](/help/implementing/cloud-manager/deploy-code.md). This is done by adding an appropriate OSGi CORS configuration file for the desired endpoint(s). Multiple CORS configurations can be created and deployed to different environments. Examples can be found in the [WKND Reference Site](https://github.com/adobe/aem-guides-wknd/tree/master/ui.config/src/main/content/jcr_root/apps/wknd/osgiconfig)

The CORS configuration must specify a trusted website origin `alloworigin` or `alloworiginregexp` for which access must be granted.

The configuration file must be named like: `com.adobe.granite.cors.impl.CORSPolicyImpl~appname-graphql.cfg.json` where `appname` reflects the name of your application.

For example, to grant access to the GraphQL endpoint `/content/cq:graphql/wknd/endpoint` and persisted queries endpoint for `https://my.domain` you can use:

```json
{
  "supportscredentials":false,
  "supportedmethods":[
    "GET",
    "HEAD",
    "POST"
  ],
  "exposedheaders":[
    ""
  ],
  "alloworigin":[
    "https://my.domain"
  ],
  "maxage:Integer":1800,
  "alloworiginregexp":[
    ""
  ],
  "supportedheaders":[
    "Origin",
    "Accept",
    "X-Requested-With",
    "Content-Type",
    "Access-Control-Request-Method",
    "Access-Control-Request-Headers"
  ],
  "allowedpaths":[
    "/content/cq:graphql/wknd/endpoint.json",
    "/graphql/execute.json/.*"
  ]
}
```

If you have configured a vanity path for the endpoint, you can also use it in `allowedpaths`.
