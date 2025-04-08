---
title: Overview to User Mapping Tool (Legacy)
description: Overview to User Mapping Tool (Legacy)
exl-id: 17ed5721-093e-4491-b8c4-3dadcaa6598b
hide: yes
hidefromtoc: yes
feature: Migration
role: Admin
---

# Overview to User Mapping Tool (Legacy) {#overview-user-mapping-tool}

>[!INFO]
>
>This documentation refers to a deprecated version of the tool. For more information on the latest version, see [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md).

<!-- Alexandru: drafting this for now

NOTE: "LEGACY" for user mapping includes everything before (that is, not including) 2.0.16 of CTT.

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_usermapping"
>title="User Mapping Tool"
>abstract="The Content Transfer Tool helps you move users and groups from your existing AEM system to AEM as a Cloud Service. Existing users and groups need to be mapped to their IMS IDs to avoid duplicate users and groups on the Cloud Service author instance."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html#important-considerations" text="Important Considerations for using User Mapping Tool"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html#using-user-mapping-tool" text="Using User Mapping Tool"

-->

## Introduction {#introduction}

As part of the transition journey to Adobe Experience Manager (AEM) as a Cloud Service, you must move users and groups from your existing AEM system to AEM as a Cloud Service. This migration is done by the Content Transfer Tool. 

A major change to AEM as a Cloud Service is the fully integrated use of Adobe IDs for accessing the author tier. This integration requires use of the [Adobe Admin Console](https://helpx.adobe.com/enterprise/using/admin-console.html) for managing users and user groups. The user-profile information is centralized in the Adobe Identity Management System (IMS) that provides single sign-on across all Adobe cloud applications. For more details, see [Identity Management](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/overview/what-is-new-and-different.html#identity-management). Because of this change, existing users and groups must be mapped to their IMS IDs to avoid duplicate users and groups on the Cloud Service author instance.

## User Mapping Tool {#mapping-tool}

The Content Transfer Tool (without User Mapping) migrates any users and groups associated with the content being migrated. The User Mapping Tool is a part of Content Transfer Tool. Its sole purpose is to edit the users so that they are recognized correctly by IMS, the single sign-on functionality used by AEM as a Cloud Service. After these modifications are done, the Content Transfer Tool migrates the specified content's users and groups as usual.

### What's Next {#whats-next}

Once you have learned what a User Mapping tool is, you are now ready to review important considerations and exceptional cases before using the User Mapping Tool. See [Important Considerations for User Mapping Tool](/help/journey-migration/content-transfer-tool/user-mapping-tool-legacy/considerations-user-mapping-tool-legacy.md) for more details.
