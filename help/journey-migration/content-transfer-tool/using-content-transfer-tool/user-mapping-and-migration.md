---
title: User Mapping and Principal Migration
description: Overview of User Mapping and Principal Migration in AEM as a Cloud Service.
exl-id: 4a35fc46-f641-46a4-b3ff-080d090c593b
---
# User Mapping and Principal Migration {#user-mapping-and-principal-migration}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_usermapping"
>title="User Mapping"
>abstract="The Content Transfer Tool helps you move users and groups from your existing Adobe Experience Manager (AEM) system to AEM as a Cloud Service. Existing users must be mapped to their IMS IDs to avoid having them duplicated on the Cloud Service author instance."

>[!NOTE]
>For previous versions of the User Mapping Tool, see the [legacy documentation](/help/journey-migration/content-transfer-tool/user-mapping-tool-legacy/considerations-user-mapping-tool-legacy.md).

## Introduction {#introduction}

As part of the transition journey to Adobe Experience Manager (AEM) as a Cloud Service, users and groups (or 'principals') must be migrated from existing AEM systems to AEM as a Cloud Service. This task is done by the Content Transfer Tool.

A major change to AEM as a Cloud Service is the fully integrated use of Adobe IDs for accessing the author tier. This process requires use of the [Adobe Admin Console](https://helpx.adobe.com/enterprise/using/admin-console.html) for managing users and user groups. The user-profile information is centralized in the Adobe Identity Management System (IMS) that provides single sign-on across all Adobe cloud applications. For more details, see [Identity Management](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/overview/what-is-new-and-different.html#identity-management). Because of this change, existing users must be mapped to their IMS IDs to avoid the creation of duplicate users on the Cloud Service author instance. Since groups in traditional AEM are fundamentally different from groups in IMS, groups are not mapped, but the two sets of groups must be reconciled after the migration is complete.

## Principal Migration Details {#principal-migration-detail}

The Content Transfer Tool and Cloud Acceleration Manager will migrate to the cloud system any principals associated with the content being migrated.  The Content Transfer Tool does this by copying all principals from the source AEM system during the extraction process.  CAM Ingestion then selects and migrates only those principals associated with the content being ingested.

* What principals are migrated? If a principal is on an ACL or CUG policy of migrated content, that principal and all groups it is in and their ancestor (parent) groups will all be migrated. Further, if a principal on the content is a group, all its descendent (child) groups and users will also be migrated.

## User Mapping Details {#user-mapping-detail}

AEM users can be mapped to corresponding Adobe IMS users with the same email address.  This mapping can be done automatically in CTT (during the extraction step), and whether it is done or not can be controlled by a toggle before extraction is started. The toggle's default setting can be overridden by the user when starting extraction.

* If the source system is an author instance, by default the choice to do the mapping is _on_, because it is the recommended process.
* If the source system is a publish instance, by default the choice to do the mapping is _off_, because users are not normally migrated or used on publish instances; or if they are used, a different authentication system (i.e., not IMS) is typically used for them.

Whether or not users are mapped during extraction, they, along with the groups, are migrated to the cloud system during ingestion if they are associated with content being migrated.

## Important Considerations when Mapping and Migrating Users {#important-considerations}

### Exceptional cases {#exceptional-cases}

The following specific cases are logged:

1. If a user has no email address in the `profile/email` field of their *jcr* node, the user or group in question may be migrated but is not mapped. This scenario is the case even if the email address is used as a user name for logging in.
2. If the user is disabled, it is treated the same as other users; it is mapped and migrated as normal, and remains disabled on the cloud instance.
3. If a principal exists with the same name (rep:principalName) on both the source AEM instance and the target AEM Cloud Service instance, the principal in question is not migrated and the previously existing principal on the cloud system remains unchanged.
4. If a user is migrated without being mapped by way of User Mapping, on the target cloud system the user will not able to login using their IMS ID. Or, if their email address does not match the email address used to log into IMS, on the target cloud system they will also not able to login using their IMS ID. They might be able to log on using the traditional AEM method (local login), but this method is not normally what is wanted or expected.

## Additional Considerations {#additional-considerations}

* If the setting **Wipe existing content on Cloud instance before ingestion** is set, already transferred users on the Cloud Service instance are deleted along with the entire existing repository; a new repository is created into which content is ingested. This process also resets all settings including permissions on the target Cloud Service instance and is true for an admin user added to the **administrators** group. The admin user must be re-added to the **administrators** group to retrieve the access token for CTT/CAM Ingestion.
* When content top-ups are performed, if content is not transferred because it has not changed since the previous transfer, users and groups associated with that content are not transferred either. This rule is true even if the users and groups have changed on the source system. The reason is because users and groups are only migrated along with the content they are associated with.
* If the target AEM Cloud Service instance has a user with a different user name but same email address as one of the users on the source AEM instance, and User Mapping is enabled, the logs record an error message. Also, the source AEM user is not transferred, as only one user with a given email address is allowed on the target system.
* See [Migrating Closed User Groups](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/closed-user-groups-migration.md) for extra considerations for principals used in a Closed User Group (CUG) policy.

## Final Summary and Report {#final-report}

Once the extraction and ingestion have completed successfully, a report is generated showing the principal migration details. See [How to Validate the Principal Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/validating-content-transfers.md#how-to-validate-principal-migration) for the details.
