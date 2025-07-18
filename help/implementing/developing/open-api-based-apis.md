---
title: OpenAPI-Based APIs
description: Learn about AEM as a Cloud Service support for OpenAPI-based APIs
feature: Developing
role: Admin, Architect, Developer
exl-id: 4aeafba9-8f9e-4ecb-9e37-8d048b0474cc
---
# OpenAPI-Based APIs {#openapi-based-apis}

Newer AEM as a Cloud Service APIs follow the OpenAPI specification, and thus offer a consistent and well-documented set of APIs.

>[!NOTE]
>
> An [end-to-end tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/invoke-openapi-based-aem-apis) is a recommended resource to learn how to configure and invoke the OpenAPI-based AEM APIs.

For endpoints that require authentication, the authentication approach differs based on the endpoint, but may use OAuth Server-to-Server, OAuth Web App, or OAuth Single Page App (SPA). Credentials are configured through projects in [Adobe Developer Console](https://developer.adobe.com/developer-console/).

 Common API use cases involve integrations with systems such as a CRM or PIM, where AEM APIs are invoked to retrieve or persist data. As part of the integration implementation, applications may subscribe to [AEM-emitted events](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-eventing/overview), which can trigger business logic in Adobe App Builder or other infrastructure.

This document serves as an overview, but more in-depth documentation is available in the following pages:

* The links from the OpenAPI-based API section of [reference documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/). Each API's reference documentation also includes an API playground, which makes it easy to try out an endpoint using a bearer token generated with the Adobe Developer Console.

* Informational [Guides](https://developer.adobe.com/experience-cloud/experience-manager-apis/guides/), including [API concepts and syntax](https://developer.adobe.com/experience-cloud/experience-manager-apis/guides/how-to/).

* A top-level tutorial describing [authentication approaches](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/openapis/overview#authentication-support) and other concepts.

* A tutorial with video focused on [how to configure the OpenAPI-based APIs](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/openapis/setup).

* [An end-to-end tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/invoke-openapi-based-aem-apis) about configuring and invoking OpenAPIs with the server-to-server authentication strategy. Similar tutorials can also be found for Web App and Single Page Application authentication approaches.

## Configuring API Access {#configuring-api-access}

Some OpenAPI-based AEM APIs need authentication, which requires credentials to be generated using [Adobe Developer Console](https://developer.adobe.com/developer-console/). Configuration involves the following steps:

1. Modernization of the AEM as a Cloud Service environment. For more information, see [Modernization of AEM as a Cloud Service environment](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/openapis/setup?#modernization-of-aem-as-a-cloud-service-environment) tutorial step.
1. Enable access to the AEM APIs using Product Profiles. Product Profiles are associated with the Services that represent AEM user groups with predefined Access Control Lists (ACLs). While some services are associated with specific product profiles by default, others need to be explicitly associated; for example, the AEM Assets API Users Service is not associated with any [Product Profile](/help/onboarding/aem-cs-team-product-profiles.md#aem-product-profiles), so you must enable it to use AEM Assets API. For more information, see [Enable AEM APIs access](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/openapis/setup#enable-aem-apis-access) tutorial step.
1. To add Server-to-Server authentication, the user setting up integration must be the organization's system administrator in the Adobe Admin Console or added as a Developer to the Product Profile where the Service is associated. For more information, see [Enable AEM APIs access](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/openapis/setup#enable-aem-apis-access) tutorial step.
1. Create an Adobe Developer Console (ADC) Project.
1. Configure the ADC Project. This generates credentials that will be used later to exchange for a bearer token when invoking the API.
1. Configure the AEM instance to enable ADC Project communication. This involves registering the client ID with the environment by configuring and deploying a YAML file, as described in the [Registering a Client ID](#registering-a-client-id) section below.

For detailed step-by-step instructions, see the [Set up OpenAPI-based APIs tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/aem-apis/openapis/setup).

### Registering a Client ID {#registering-a-client-id}

Client IDs scope the APIs in an Adobe Developer Console project to specific AEM environments. This is achieved as follows:

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
