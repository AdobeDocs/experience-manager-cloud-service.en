---
title: JWT Credentials Deprecation in Adobe Developer Console
description: Learn about the impact of JWT credentials deprecation in Adobe Developer Console on AEM
exl-id: 7c811081-484c-41f7-a289-4e9a10a837b3
---
# JWT Credentials Deprecation in Adobe Developer Console {#jwt-credentials-deprecation-in-adobe-developer-console}

>[!NOTE]
>
>AEM 6.5 customers should reference [this article](https://experienceleague.adobe.com/docs/experience-manager-65/content/security/jwt-credentials-deprecation-in-adobe-developer-console.html) for more information.

Adobe customers use [Adobe Developer Console](https://developer.adobe.com/console) to generate credentials that enable access to various APIs. Customers select from various credential types ranging from OAuth Server-to-Server to Single-Page App. One of those credential types, Service Account (JWT) credentials, has been deprecated in favor of the OAuth Server-to-Server credentials. New Service Account (JWT) credentials cannot be created on or after June 3, 2024, and existing JWT credentials will not work on or after Jan 27, 2025. You can [read about the deprecation](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/).

This article provides some additional context about how AEM as a Cloud Service should handle the deprecation.

The main takeaway at this time is that AEM features do not yet support the new OAuth Server-to-Server credentials. Support will come soon -- by late April 2024 through an AEM release for AEM as a Cloud Service. You may have received an email with instructions to migrate your JWT credentials, but rest assured that you can and should hold off on the credentials migration until AEM supports the new OAuth Server-to-Server credential type.

The sections below list the scenarios where customers must (or in some cases must not) replace their Service Account (JWT) credentials with OAuth Server-to-Server credentials, once AEM supports them in late April. [Read how](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/#migration-overview) to replace the credentials in the future.

>[!NOTE]
>
>The [**AEM** Developer Console](/help/implementing/developing/introduction/development-guidelines.md#crxde-lite-and-developer-console) (note the **AEM** in the name, which distinguishes it from the **Adobe** Developer Console) provides a utility to generate [JWT tokens](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md) used for server-to-server APIs. These credentials are not deprecated and can continue to be used.


## Integrating AEM with Other Adobe Solutions {#integrating-aem-with-other-adobe-solutions}

**Action**: Wait to migrate until after late April 2024, when AEM supports it (this article will be updated at that time)

**Relevant AEM versions**: AEM as a Cloud Service

AEM customers use the AEM Author UI to configure integrations with all other Adobe solutions. For example, Adobe Target, Adobe Analytics, Adobe Launch, AFCS, and many more.

![Integrating AEM with other solutions](/help/security/assets/jwt-deprecation.png)

As an example, here are [the instructions](https://docs.mktossl.com/docs/experience-manager-cloud-service/content/sites/integrations/integration-adobe-target-ims.html?lang=en) for configuring the integration with Adobe Target. The API key in the [Completing the IMS Configuration in AEM](https://docs.mktossl.com/docs/experience-manager-cloud-service/content/sites/integrations/integration-adobe-target-ims.html#completing-the-ims-configuration-in-aem) section should be migrated to the OAuth Server-to-Server credential type, once AEM supports those credentials in late April. Those instructions will be updated will revised in late April to help you apply the new OAuth Server-to-Server credentials.

## Cloud Manager APIs {#cloud-manager-apis}

**Action**: Wait to migrate until after late April 2024, when AEM supports it (this article will be updated at that time).

**Relevant AEM versions**: AEM as a Cloud Service

Customers create Adobe Developer Console projects so they can invoke [Cloud Manager APIs](https://developer.adobe.com/experience-cloud/cloud-manager/guides/getting-started/create-api-integration/). The credentials in the Adobe Developer project should be migrated to the OAuth Server-to-Server credential type, once AEM and Cloud Manager support it. 

## Auto-generated projects {#autogen-projects}

**Action**: Do not migrate since Adobe will migrate on your behalf.

**Relevant AEM versions**: AEM as a Cloud Service.

When Cloud Manager provisions AEM as a Cloud Service environments, it auto-generates an Adobe Developer Console project with JWT credentials. This project is marked as read-only, as illustrated in the screenshot below. Customers cannot and should not attempt to migrate these projects to OAuth Server-to-Server credentials; instead, Adobe will migrate these projects on its own, before the credentials are no longer usable.

![Auto-generated projects](/help/security/assets/jwt-deprecation-autogen-projects.png)
