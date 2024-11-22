---
title: OpenAPI-Based APIs
description: Learn about AEM as a Cloud Service support for OpenAPI-based APIs
feature: Developing
role: Admin, Architect, Developer
exl-id: 4aeafba9-8f9e-4ecb-9e37-8d048b0474cc
---
# OpenAPI-Based APIs {#openapi-based-apis}

>[!NOTE]
>
>OpenAPIs are available as part of an early access program. If you are interested in accessing them, we encourage you to email [aem-apis@adobe.com](mailto:aem-apis@adobe.com) with a description of your use case.

Newer AEM as a Cloud Service APIs follow the OpenAPI specification, and thus produce consistent, well-documented, and user-friendly APIs. In-depth information is available in the following pages:

* An [end-to-end tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/invoke-openapi-based-aem-apis) about how to configure and invoke OpenAPI-based AEM APIs.
* Informational [Guides](https://developer.adobe.com/experience-cloud/experience-manager-apis/guides/), including [API concepts and syntax](https://developer.adobe.com/experience-cloud/experience-manager-apis/guides/how-to/).
* API-endpoint [reference documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/), where some of the APIs are OpenAPI-based, such as [this Sites API](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/). Reference documentation also includes an API playground, which makes it simple to try out an endpoint using a bearer token generated with the Adobe Developer Console.

A common API use case involves integrations with systems such as a CRM or PIM, where AEM APIs are invoked to retrieve or persist data. As part of the integration implementation, applications may subscribe to [AEM-emitted events](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-eventing/overview), which can trigger business logic in Adobe App Builder or other infrastructure.

Supported API authentication types differ based on the endpoint, but may be OAuth Server-to-Server, OAuth Web App, and OAuth Single Page App (SPA).

>[!NOTE]
>
> The [end-to-end tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/invoke-openapi-based-aem-apis) is a recommended resource to learn how to configure and invoke the OpenAPI-based AEM APIs.


## Configuring API Access {#configuring-api-access}

Many OpenAPI-based AEM APIs require authentication, which requires credentials to be generated using [Adobe Developer Console](https://developer.adobe.com/developer-console/docs/guides/). Configuration involves the following steps, which are illustrated in the tutorial:

1. Ensure your AEM program's [product profiles are updated](/help/onboarding/aem-cs-team-product-profiles.md#aem-product-profiles) and have an appropriate service enabled to access the desired API.
1. Create a new project in Adobe Developer Console and add the desired API(s) to the project, also selecting the appropriate authentication type.
1. Generate the credential, which will later be used to exchange fora bearer token when invoking the API.
1. Register the client ID with the environment by configuring a YAML file, which is deployed using the Config Pipeline (or commandline for RDEs). 

## Registering a Client ID {#registering-a-client-id}

Client IDs scope the APis in an Adobe Developer Console project to specific AEM environments. This is achieved as follows:

1. Create a file named `api.yaml` or similar with a configuration like the snippet below, including the desired tiers (author, publish, preview). `Client_id` values should come from your Adobe Developer Console API project(s).

   The `kind`, `version`, and `metadata` properties are described in the [Config Pipeline](/help/operations/config-pipeline.md#common-syntax) article. The `kind` property value should be set to *API* and the `version` property should be set to *1*.

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
1. For environment types other than RDE (which uses command line tooling), create a targeted deployment config pipeline in Cloud Manager, as referenced by [this section](/help/operations/config-pipeline.md#creating-and-managing) in the Config Pipeline article. Note that Full Stack pipelines and Web Tier pipelines do not deploy the configuration file.
1. Deploy the configuration.
