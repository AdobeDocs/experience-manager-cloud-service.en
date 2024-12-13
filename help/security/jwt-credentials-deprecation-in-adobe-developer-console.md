---
title: JWT Credentials Deprecation in Adobe Developer Console
description: Learn about the impact of JWT credentials deprecation in Adobe Developer Console on AEM.
exl-id: 7c811081-484c-41f7-a289-4e9a10a837b3
feature: Security
role: Admin
---
# JWT Credentials Deprecation in Adobe Developer Console {#jwt-credentials-deprecation-in-adobe-developer-console}

>[!NOTE]
>
>AEM 6.5 customers should reference [the comparable documentation for AEM 6.5](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/security/jwt-credentials-deprecation-in-adobe-developer-console) for more information.

Adobe customers use [Adobe Developer Console](https://developer.adobe.com/console) to generate credentials that enable access to various APIs. Customers select from various credential types ranging from OAuth Server-to-Server to Single-Page App. One of those credential types, Service Account (JWT) credentials, has been deprecated in favor of the OAuth Server-to-Server credentials. New Service Account (JWT) credentials cannot be created on or after June 3, 2024, and existing JWT credentials will not work on or after Jan 27, 2025. You can [read about the deprecation](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/).

This article provides some additional context about how AEM as a Cloud Service should handle the deprecation.

The main takeaway is that AEM now supports the new OAuth Server-to-Server credentials for AEM as a Cloud Service. You may have received an email with instructions to migrate your JWT credentials, and this migration can now be done.

The sections below list the scenarios where customers must (or in some cases must not) replace their Service Account (JWT) credentials with OAuth Server-to-Server credentials, now that AEM supports them. [Read how](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/#migration-overview) to migrate the credentials.

>[!NOTE]
>
>The [**AEM** Developer Console](/help/implementing/developing/introduction/development-guidelines.md#crxde-lite-and-developer-console) (note the **AEM** in the name, which distinguishes it from the **Adobe** Developer Console) provides a utility to generate [JWT tokens](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md) used for server-to-server APIs. These credentials are not deprecated and can continue to be used.

## Integrating AEM with Other Adobe Solutions {#integrating-aem-with-other-adobe-solutions}

**Action**: Migrate your configuration as AEM now supports OAuth credentials.

**Relevant AEM versions**: AEM as a Cloud Service

AEM customers use AEM to configure integrations with many other Adobe solutions. For example, Adobe Target, Adobe Analytics, and others.

See [Setting Up IMS Integrations for AEM as a Cloud Service](/help/security/setting-up-ims-integrations-for-aem-as-a-cloud-service.md) for details of how to:

* create configurations with OAuth credentials 
* migrate configurations, that were created with JWT credentials, to use OAuth credentials

## Cloud Manager APIs {#cloud-manager-apis}

**Action**: Migrate your JWT credentials to OAuth credentials, which Cloud Manager now supports.

**Relevant AEM versions**: AEM as a Cloud Service

Customers create Adobe Developer Console projects so they can invoke [Cloud Manager APIs](https://developer.adobe.com/experience-cloud/cloud-manager/guides/getting-started/create-api-integration/). The credentials in the Adobe Developer project should be migrated to the OAuth Server-to-Server credential type before the deprecated JWT credentials expire in January 2025.

## Auto-generated projects {#autogen-projects}

**Action**: Do not migrate because Adobe is going to migrate on your behalf.

**Relevant AEM versions**: AEM as a Cloud Service.

When Cloud Manager provisions AEM as a Cloud Service environments, it auto-generates an Adobe Developer Console project with JWT credentials. This project is marked as read-only, as illustrated in the screenshot below. Customers cannot and should not attempt to migrate these projects to OAuth Server-to-Server credentials. Instead, Adobe will migrate these projects on its own, before the credentials are no longer usable.

![Auto-generated projects](/help/security/assets/jwt-deprecation-autogen-projects.png)

## Auto-generated projects FAQs {#autogen-projects-faqs}

This section provides answers to the most frequently asked questions about JWT credentials deprecation for auto-generated projects in AEM as a Cloud Service.

**How do I do which projects are auto-generated?**
Navigate to the Adobe Developer Console | Projects section.  AEM as a Cloud Service auto-generated projects will have a lock icon with ‘Auto-generated’ identifier.  Auto-generated projects follow format AEM-p#####-e###### and are created by Technical account user.  

<img width="439" alt="image" src="https://git.corp.adobe.com/storage/user/16149/files/6b20a8a3-3711-4741-8f2c-ec5e36fe97cc">


**What if we encounter issues with our auto-generated projects?**  

Contact [Adobe Customer Care](https://helpx.adobe.com/ca/enterprise/using/support-for-experience-cloud.html).  

**Should I go ahead and migrate our auto-generated projects?**

No action is required as Adobe will migrate auto-generated on your behalf for environments with AEM Release 17258 (Aug '24) and higher.  

**What are the timelines for migration of auto-generated projects?**

Adobe will initiate a phased migration approach in Q1 of 2025, beginning with development environments.   

**How will our AEM as a Cloud Service instance be impacted if we have an AEM release that is older than AEM Release 17258 (Aug '24)?**

Auto-generated project integrations will stop working if they are not migrated to OAuth by June 2025.   

To ensure a smooth transition customers should contact [Adobe Customer Care](https://helpx.adobe.com/ca/enterprise/using/support-for-experience-cloud.html) promptly and begin the process of updating to the [latest AEM Release](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/release-notes/maintenance/latest). This will provide ample time for regression testing and allow Adobe to efficiently manage the migration of projects. 

**Can I upgrade to a supported OAuth version without upgrading my AEM as a Cloud Service AEM Release?**

No. To ensure a smooth transition customers should contact [Adobe Customer Care](https://helpx.adobe.com/ca/enterprise/using/support-for-experience-cloud.html) promptly and begin the process of updating to the [latest AEM Release](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/release-notes/maintenance/latest). This will provide ample time for regression testing and allow Adobe to efficiently manage the migration of projects. 
