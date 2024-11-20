---
title: OpenAPI-based APIs
description: Learn about AEM as a Cloud Service support for OpenAPI-based APIs
feature: Developing
role: Admin, Architect, Developer
---

# OpenAPI-based APIs {#openapi-based-apis}

>[!NOTE]
>
>OpenAPIs are available as part of an early access program. If you are interested in accessing them, we encourage you to email [aem-apis@adobe.com](mailto:aem-apis@adobe.com) with a description of your use case.

Newer AEM as a Cloud Service APIs follow the OpenAPI specification, and thus produce consistent, well-documented, and user-friendly APIs. In-depth information is available in the following pages:

* API setup and usage tutorial
* [Informational Guides](https://developer.adobe.com/experience-cloud/experience-manager-apis/guides/), including [API concepts and syntax](https://developer.adobe.com/experience-cloud/experience-manager-apis/guides/how-to/)
* API-endpoint [reference documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/), where some of the APIs are OpenAPI-based, such as [this Sites API](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/). Reference documentation also includes an API playground, which makes it simple to try out an endpoint using a bearer token generated with the Adobe Developer Console.

For the many OpenAPI-based AEM APIs that require authentication, credentials for APIs are generated using [Adobe Developer Console](https://developer.adobe.com/developer-console/docs/guides/). A common use case involves integrations with systems such as CRM or PIM, where AEM API calls are made to retrieve or persist data. Applications may subscribe to events emitted by AEM to trigger an API call to retrieve more data. Supported API authentication types differ based on the endpoint, but may be OAuth Server-to-Server, OAuth Web App, and OAuth Single Page App (SPA).

## Configuring API Access {#configuring-api-access}

Many OpenAPI-based AEM APIs require authentication, which requires credentials to be generated using Adobe Developer Console. The end-to-end tutorial should be consulted since it walks through this in detail, including the steps below:

1. Ensure your AEM program's [product profiles are updated](/help/onboarding/aem-cs-team-product-profiles.md#aem-product-profiles) and have an appropriate service enabled needed for access the desired API.
1. Create a new project in [Adobe Developer Console](https://developer.adobe.com/console) with the desired APIs added to the project, and the appropriate authentication approach selected.
1. Generate the credential, which should be used to generate a bearer token used in the API call.
1. Register the client id with the environment by configuring a YAML file and deploy it using the Config Pipeline (or via CLI if the environment is an RDE). See the Registering a Client ID section below.

## Registering a Client ID {#registering-a-client-id}

Client IDs scope an Adobe Developer Console project to specific AEM environments. This can be achieved with a YAML file, as described in the following steps:

1. Create a file named `api.yaml` or similar with a configuration like the snippet below, including the desired tiers (author, publish, preview). `Client_id` values should come from your Adobe Developer Console API projects.

   The kind, version, and metadata properties are described in the [Config Pipeline](/help/operations/config-pipeline.md#common-syntax) article. The kind property value should be API and the version property should be set to `1`.

   ```
   kind: "API"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     allowedClientIDs:
       author:
         - "<client_id>"
       publish:
         - "<client_id>"
       preview:
         - "<client_id>"

   ```

1. Place the file somewhere under a top level folder named `config` or similar, as described under [Config Pipeline](/help/operations/config-pipeline.md#folder-structure).
1. For environment types other than RDE (which uses command line tooling), create a targeted deployment config pipeline in Cloud Manager, as referenced by [this section](/help/operations/config-pipeline.md#creating-and-managing). Note that Full Stack pipelines and Web Tier pipelines do not deploy the configuration file
1. Deploy the configuration.





