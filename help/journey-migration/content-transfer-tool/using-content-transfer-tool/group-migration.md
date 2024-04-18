---
title: Group Migration
description: Overview of Group Migration in AEM as a Cloud Service.
exl-id: 4a35fc46-f641-46a4-b3ff-080d090c593b
---
# Group Migration {#group-migration}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_groupmigration"
>title="Group Migration"
>abstract="The Content Transfer Tool helps you copy groups from your existing Adobe Experience Manager (AEM) system to AEM as a Cloud Service."

>[!NOTE]
>For previous versions of the User Mapping Tool, see the [legacy documentation](/help/journey-migration/content-transfer-tool/user-mapping-tool-legacy/considerations-user-mapping-tool-legacy.md).

## Introduction {#introduction}

As part of the transition journey to Adobe Experience Manager (AEM) as a Cloud Service, groups must be migrated from existing AEM systems to AEM as a Cloud Service. This task is done by the Content Transfer Tool.

A major change to AEM as a Cloud Service is the fully integrated use of Adobe IDs for accessing the author tier. This process requires use of the [Adobe Admin Console](https://helpx.adobe.com/enterprise/using/admin-console.html) for managing users and user groups. The user profile information is centralized in the Adobe Identity Management System (IMS) that provides single sign-on across all Adobe cloud applications. For more details, see [Identity Management](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/overview/what-is-new-and-different.html#identity-management). Because of this change, users on are automatically created on AEM when they first log into it via IMS.  Thus, CTT does not migrate the users to the cloud system.  IMS users must be placed in IMS groups, which in turn must be placed in the AEM groups that have been given permission to access the AEM content being migrated.  In this way, users on the cloud system will have the same access they had on their source AEM system.

## Group Migration Details {#group-migration-detail}

The Content Transfer Tool and Cloud Acceleration Manager will migrate any groups associated with the content being migrated to the cloud system. The Content Transfer Tool does this by copying all groups from the source AEM system during the extraction process. CAM Ingestion then selects and migrates only those groups associated with the content being ingested. If a group is on an ACL or CUG policy of migrated content, that group, all groups it is in, and their ancestor (parent) groups will all be migrated. Further, all its descendent (child) groups will also be migrated.

## Additional Considerations {#additional-considerations}
* If the setting **Wipe existing content on Cloud instance before ingestion** is set, groups previously transferred to the Cloud Service instance are deleted along with the entire existing repository; a new repository is created into which content is ingested. This process also resets all settings including permissions on the target Cloud Service instance and is true for an admin user added to the **administrators** group. The admin user must be re-added to the **administrators** group to retrieve the access token for CTT/CAM Ingestion.
* When non-wipe ingestions are performed (**Wipe existing content** is unset), if content is not transferred because it has not changed since the previous transfer, groups associated with that content are not transferred either. This rule is true even if the groups have changed on the source system. This is because groups are only migrated along with the content they are associated with. Because of this, in this case any groups which are members of a group on the source system will not be migrated unless they are part of a different group that is being migrated, or in the ACL of different content being migrated. To migrate these groups afterwards, consider using packages, deleting groups from the target and re-migrating the relevant content. or re-migrating using a wipe ingestion.
* During a non-wipe ingestion, if a group exists with any of the same uniqueness-constrained data (rep:principalName, rep:authorizableId, jcr:uuid or rep:externalId) on both the source AEM instance and the target AEM Cloud Service instance, the group in question is _not_ migrated and the previously existing group on the cloud system remains unchanged. This is logged in the Principal Migration Report.
* See [Migrating Closed User Groups](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/closed-user-groups-migration.md) for extra considerations for groups used in a Closed User Group (CUG) policy.

## Final Summary and Report {#final-report}

Once the extraction and ingestion have completed successfully, a report is generated showing the group migration details. See [How to Validate the Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/validating-content-transfers.md#how-to-validate-group-migration) for the details.
