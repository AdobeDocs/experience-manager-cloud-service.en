---
title: Overview to User Mapping Tool
description: Overview to User Mapping Tool
exl-id: 17ed5721-093e-4491-b8c4-3dadcaa6598b
---
# Overview to User Mapping Tool {#overview-user-mapping-tool}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_usermapping"
>title="User Mapping Tool"
>abstract="The Content Transfer Tool helps you move users and groups from your existing AEM system to AEM as a Cloud Service. Existing users and groups need to be mapped to their IMS IDs to avoid duplicate users and groups on the Cloud Service author instance."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#important-considerations" text="Important Considerations for using User Mapping Tool"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#using-user-mapping-tool" text="Using User Mapping Tool"

## Introduction {#introduction}

As part of the transition journey to Adobe Experience Manager (AEM) as a Cloud Service, you need to move users and groups from your existing AEM system to AEM as a Cloud Service. This is done by the Content Transfer Tool. 

A major change to AEM as a Cloud Service is the fully integrated use of Adobe IDs for accessing the author tier.  This requires use of the [Adobe Admin Console](https://helpx.adobe.com/enterprise/using/admin-console.html) for managing users and user groups. The user-profile information is centralized in the Adobe Identity Management System (IMS) that provides single-sign-on across all Adobe cloud applications. For more details, refer to [Identity Management](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/overview/what-is-new-and-different.html?lang=en#identity-management). Because of this change, existing users and groups need to be mapped to their IMS IDs to avoid duplicate users and groups on the Cloud Service author instance.

## User Mapping Tool {#mapping-tool}

The Content Transfer Tool (without User Mapping) will migrate any users and groups associated with the content being migrated. The User Mapping Tool is a part of Content Transfer Tool, and its sole purpose is to modify the users and groups so that they can be recognized correctly by IMS, the single-sign-on functionality used by AEM as a Cloud Service. Once these modifications are done, the Content Transfer Tool migrates the specified content's users and groups as usual.

### What’s Next {#whats-next}

Once you have learned what a User Mapping tool is, you are now ready to review important considerations and exceptional cases before using the User Mapping Tool. See [Important Considerations for User Mapping Tool](/help/journey-migration/content-transfer-tool/user-mapping-tool/considerations-user-mapping-tool.md) for more details.
