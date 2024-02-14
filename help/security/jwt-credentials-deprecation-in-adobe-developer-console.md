---
title: JWT Credentials Deprecation in Adobe Developer Console
description: Learn about the impact of JWT credentials deprecation in Adobe Developer Console
---

# JWT Credentials Deprecation in Adobe Developer Console {#jwt-credentials-deprecation-in-adobe-developer-console}

Adobe Developer Console is the place to generate credentials enabling access to various APIs. One of those credential types, Service Account (JWT) credentials, has been deprecated in favor of the OAuth Server-to-Server credentials. New JWT credentials cannot be created on or after May 1, 2024, and existing JWT credentials will not work on or after Jan 1, 2025. Learn more about the deprecation [here](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/).

This article provides some additional context for AEM as a Cloud Service and AEM 6.5 customers, regarding Adobe's expectations.

AEM features do not currently support OAuth Server-to-Server credentials. Support will come by early April 2024 through an AEM release for AEM as a Cloud Service, and a small, dedicated Service Pack for AEM 6.5. You may have received an email instructing you to migrate your credentials, but rest assured that you can and should hold off on the migration until AEM supports the new credential type.

The sections below list of the scenarios where customers must (or must not) replace their Service Account (JWT) credentials with OAuth Server-to-Server credentials, **once AEM supports them**. [Read how](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/#migration-overview) to replace the credentials.

>[!NOTE]
>
>The [AEM Developer Console](/help/implementing/developing/introduction/development-guidelines.md#crxde-lite-and-developer-console) provides a utility to generate [JWT tokens](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md) used for server-to-server APIs. These credentials are not deprecated and can keep being used.


## Integrating AEM with Other Adobe Solutions {#integrating-aem-with-other-adobe-solutions}

Action: Wait to migrate until after mid-April 2024, when AEM supports it.

AEM customers use the AEM Author UI to configure integrations with other Adobe solutions, including Adobe Target. 

![Integrating AEM with other solutions](/help/security/assets/jwt-deprecation.png)

As an example, here are [the instructions](https://docs.mktossl.com/docs/experience-manager-cloud-service/content/sites/integrations/integration-adobe-target-ims.html?lang=en#prerequisites) for configuring the integration with Adobe Target. The API key in the "Completing the IMS Configuration in AEM" section should be migrated to the OAuth Server-to-Server credential type, once AEM supports those credentials.

## Cloud Manager APIs {#cloud-manager-apis}

Action: Wait to migrate until after mid-April 2024, when AEM supports it.

Customers create Adobe Developer Console projects so they can invoke [Cloud Manager APIs](https://developer.adobe.com/experience-cloud/cloud-manager/guides/getting-started/create-api-integration/). The credentials in the Adobe Developer project should be migrated to the OAuth Server-to-Server credential type, once AEM and Cloud Manager support it. 

## Auto-generated projects {#autogen-projects}

Action: No need to migrate.

When Cloud Manager provisions AEM as a Cloud Service environments, it auto-generates an Adobe Developer Console project with JWT credentials. This project is marked as read-only, as illustrated in the screenshot below. Customers cannot and should not attempt to migrate these projects to OAuth Server-to-Server credentials; instead, Adobe will migrate these projects on its own, before the credentials are not usable.

![Auto-generated projects](/help/security/assets/jwt-deprecation-autogen-projects.png)

