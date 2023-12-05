---
title: Troubleshoot Persisted GraphQL queries
description: Learn how to troubleshoot issues with persisted GraphQL queries in Adobe Experience Manager as a Cloud Service. 
feature: Content Fragments,GraphQL API
---

# Troubleshoot Persisted GraphQL Queries {#troubleshoot-persisted-graphql-queries}

The Actions Center includes the **GraphQL persisted query error** alert. This means that you are informed whenever one of your GraphQL persisted queries throws an error.

To help you troubleshoot and resolve such problems, we are providing documentation to explain the *most common* causes of failures, and steps on how to fix them.

## Changes to the Content Fragment model {#changes-to-content-fragment-model}

A GraphQL persisted query can fail when it is based on GraphQL types that are obsolete, often due a change in the underlying Content Fragment models.

This can happen for a variety of reasons. For example, when a content model author:

* removes or renames a field
* updates the allowed models defined for a fragment reference
* unpublishes a model that is referenced by other models
* other reasons

To address this, either:

* the persisted query that is failing should be updated to accommodate the change on the Content Fragment model 
* or the change on the model that introduced the problem should be reverted

To illustrate with an example scenario:

* Check error logs on the publisher and look for the persisted query error messages - splunk (update the env ID)
  * ` "Field 'abc' in type 'XYZModel' is undefined" `
* This means the Content Fragment model `XYZ` has been updated, and the field `abc` has been most likely removed
  * Can be confirmed by accessing the author environment - link (update the env ID + `/conf` path to the parent of the model)
* If the same persisted query works on the author environment, it likely that the model has not been published

## GraphQL endpoint not configured {#graphql-endpoint-not-configured}

When persisted queries return the `500` error code, together with the information `No suitable endpoint found`, this means that no GraphQL endpoint is configured on the AEM environment. 

To correct this, follow the steps for enabling and publishing your endpoint from [Manage GraphQL endpoints in AEM](/help/headless/graphql-api/graphql-endpoint.md).

## Missing path in the GraphQL persisted query URL {#missing-path-query-url}

If persisted queries return the `500` error code with the information `Suffix: '/' does not contain a path`

This means that the GraphQL servlet is being called without a path suffix. The pattern should be `/graphql/execute.json/thePath`.

## Blocked due to IP allow list {#blocked-due-to-ip-allow-list}

In such a case, the query returns the `405` error code.

This is not something specific to GraphQL. See the KB article [405 Error Not Allowed](https://experienceleague.adobe.com/docs/experience-cloud-kcs/kbarticles/KA-20824.html).

## Blocked by dispatcher {#blocked-dispatcher}

If the GraphQL endpoint returns the `404` error on publish for `POST` requests, it means the GraphQL queries are blocked at the dispatcher level and the endpoint needs to be manually enabled.

<!-- CHECK: might transform? -->

>[!NOTE]
>
>Keep in mind that direct `POST` GraphQL queries on the publish tier for production and stage environments are blocked by default at the dispatcher level generating a `404` response. 
>
>The CDN might transform the `404` coming from the dispatcher into a `301`.

This should not be the case by default, but a custom dispatcher configuration might cause this issue. See more under [Dispatcher - Endpoint configuration with AEM Headless](/help/headless/deployment/dispatcher.md).

cURL queries can be executed on the GraphQL endpoints with `newrelic` as `user-agent` to bybass the blocking:

```curl
# To send a standard GET GraphQL query on the publish instance
 curl 'https://publish-p${PROGRAM_ID}-e${ENVIRONMENT_ID}.adobeaemcloud.com/content/_cq_graphql/global/endpoint.json' \
      -H 'accept: application/json' \
      -H 'content-type: application/json' \
      -H 'user-agent: newrelic' \
      --data-binary '{"query":"{__schema{queryType{fields{name}}}}","variables":null}' \
      --compressed
 
# To send a POST GraphQL query on the publish instance bypassing the blocking using `newrelic` as `user-agent
curl 'https://publish-p${PROGRAM_ID}-e${ENVIRONMENT_ID}.adobeaemcloud.com/content/_cq_graphql/global/endpoint.json' \
      --request POST \
      -H 'accept: application/json' \
      -H 'content-type: application/json' \
      -H 'user-agent: newrelic' \
      --data-raw '{"query":"query IntrospectionQuery {\n  __schema {\n    types {\n      name\n    }\n  }\n}","variables":{}}' \
      --compressed
```

## GraphQL schema incorrectly constructed {#graphql-schema-incorrectly-contructed}

<!-- CHECK: Same error as what? -->

The GraphQL endpoint throws the same error when being called:

```curl
# To send an introspection query on the publish instance
curl 'https://<publish url>/content/_cq_graphql/global/endpoint.json' \
  -H 'accept: application/json' \
  -H 'content-type: application/json' \
  -H 'user-agent: newrelic' \
  --data-binary '{"query":"{__schema{queryType{fields{name}}}}","variables":null}' \
  --compressed
 
# To send a GET GraphQL query on the author instance. Basic authentication is required, credentials can be retrived following these [steps]({{ "howto/GetAdminPasswordForEnvironment" | relative_url }})
curl 'https://author-p${PROGRAM_ID}-e${ENVIRONMENT_ID}.adobeaemcloud.com/content/_cq_graphql/global/endpoint.json'   \
   -H 'accept: application/json' \
   -H 'content-type: application/json' \
   -u '<user>:<password>' \
   --data-binary '{"query":"{__schema{queryType{fields{name}}}}","variables":null}' \
   --compressed
```

<!-- CHECK: A lot of could/should/might -->

If the GraphQL schema is generated correctly, the response will be a JSON object. This object contains the names of the different GraphQL queries that can be executed on the instance, under `data__schema.queryType.fields`. For example, you should see a `adventureByPath` field when the instance contains an `Adventure` Content Fragment model.

When a schema generation issue exists the `Introspection` query will still return a `200` code. However the response payload will only contain the `basic/scalar` types instead of the full schema.

This case is rare and due to a glitch in the schema generation. Touching a Content Fragment model to retrigger the schema generation should solve the problem in such cases.

If the problem only affects a single pod, then recycling the faulty pod will address the problem.