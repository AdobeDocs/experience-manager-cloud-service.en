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

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_usermigration"
>title="Users are not Migrated"
>abstract="The Content Transfer Tool no longer migrates users. Users should be managed in the Admin Console."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/admin-console" text="AEM Admin Console documentation"
>additional-url="https://adminconsole.adobe.com/" text="AEM Admin Console"

As part of the transition journey to Adobe Experience Manager (AEM) as a Cloud Service, groups must be migrated from existing AEM systems to AEM as a Cloud Service. This task is done by the Content Transfer Tool.

A major change to AEM as a Cloud Service is the fully integrated use of Adobe IDs for accessing the author tier. This process requires use of the [Adobe Admin Console](https://helpx.adobe.com/enterprise/using/admin-console.html) for managing users and user groups. The user profile information is centralized in the Adobe Identity Management System (IMS) that provides single sign-on across all Adobe cloud applications. For more details, see [Identity Management](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/overview/what-is-new-and-different.html#identity-management). Because of this change, users are automatically created on AEM when they first log into it via IMS.  Thus, CTT does not migrate the users to the cloud system.  IMS users must be placed into IMS groups, which can be migrated groups or new groups placed in the AEM groups that have been given permission to access the AEM content being migrated.  In this way, users on the cloud system will have the same access they had on their source AEM system.

## Group Migration Details {#group-migration-detail}

The Content Transfer Tool and Cloud Acceleration Manager will migrate any groups associated with the content being migrated to the cloud system. The Content Transfer Tool does this by copying all groups from the source AEM system during the extraction process. CAM Ingestion then selects and migrates only certain groups:

* If a group is on an ACL or CUG policy of migrated content, that group will be migrated, with a few exceptions listed below.
* There are a number of groups that are built-in, and already present on the target cloud system; these are never migrated.
    * Some built-in groups may include member groups that are _not_ built-in; any such member groups (direct members or members of members, etc.) referenced in an ACL or CUG policy of migrated content will be migrated, to ensure users who are members of these groups (either directly or indirectly) maintain their access to the migrated content.
* Other groups, such as those not found on an ACL or CUG policy, those already on the destination system, and those with any uniqueness-constrained data already on the target system, will not be migrated. 

Note that the path logged/reported for a group is only the first path that triggered that group to be migrated, and that group could also be on other content paths.

Most groups migrated are configured to be managed by IMS.  This means that a group in IMS with the same name will be linked to the group in AEM, and any IMS users in the IMS group will become AEM users and members of the group in AEM.  This allows those users to have access to the content according to ACLs or CUGs policies for the group.

Note that migrated groups are no longer considered AEM "local groups"; they are IMS-ready groups in AEM though they may not yet exist in IMS.  They must be separately re-created in IMS so that they can be synchronized between AEM and IMS.  Groups can be created in IMS via Admin Console, among other methods, individually or in bulk.  See [Manage user groups](https://helpx.adobe.com/ca/enterprise/using/user-groups.html) for details about creating groups individually or in bulk on the Admin Console.

The exception to this IMS configuration is with groups created by Assets Collections. When a collection is created on AEM, groups are created for access to that collection; such groups are migrated to the cloud system, but they are not configured to be managed by IMS.  In order to add IMS users to these groups, they must be added in the Group Properties page in the Assets UI, either individually or collectively as part of another IMS group.


## Opt Out of Group Migration {#group-migration-option}

CTT version 3.0.20 and later includes an option to disable the migration of groups.  This is configured in the OSGI console as follows: 

* Open the OSGI Configuration `(http://<server>/system/console/configMgr)`
* Click on the configuration called **Content Transfer Tool Extraction Service Configuration**
* Uncheck **Include Groups in migration** to disable group migrations
* Click **Save** to ensure the configuration is saved and active on the server

With this setting disabled, groups will not be migrated, and there will be no Principal Migration report or User Report.

## User Report {#user-report}

During migration users are not migrated, but the user-group relationships on the source system are lost unless they are somehow captured.  The User Report captures some of this information in text format in a User Report. In it, each user is reported (one per line) along with a list of groups it is a member of (but groups not migrated are not put in this list), unless its list of groups is empty, in which case the user does not appear. The groups reported along with each user are those the user is a member of directly or indirectly in the source system; since groups in the source system may be nested while in the target system they are not, this list of groups supports the new flattened group structure in IMS.

In the case of a wipe and then a non-wipe ingestion, the groups in a user's list will include those groups migrated in either phase.

In addition to the groups for each user, there is a field in the report where notes may be added for the user (and a detailed description of the note's meaning is also in the report).  Possilble notes are:

* Users which are referenced directly in an ACL will have *Note-A* in their notes section, as this is not a recommended use case or best practice.
* Users which are direct members of a built-in group will have *Note-B* in their notes section, as this is also not a recommended use case or best practice.

These cases can occur simultaneously, and also at the same time as the earlier cases.

The User Report is added onto the end of (and is therefore part of) the Principal Migration Report (see [Final Summary and Report](#final-summary-and-report) below).  The information in this report, including the groups reported for each user, can be used to create a bulk user upload file which can be used in Admin Console to create many users in IMS in bulk.  Existing IMS users can also be edited in bulk.

See [Manage multiple users | Bulk CSV upload](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html) for details about creating or editing users in bulk via the Admin Console.

## Additional Considerations {#additional-considerations}

* If the setting **Wipe existing content on Cloud instance before ingestion** is set, groups previously transferred to the Cloud Service instance are deleted along with the entire existing repository; a new repository is created into which content is ingested. This process also resets all settings including permissions on the target Cloud Service instance and is true for any user added to the **administrators** group. The admin user must be re-added to the **administrators** group to retrieve the access token for CTT/CAM Ingestion.
* When non-wipe ingestions are performed (**Wipe existing content** is unset), if content is not transferred because it has not changed since the previous transfer, groups associated with that content are not transferred either. This rule is true even if the groups have changed on the source system. This is because groups are only migrated along with the content they are associated with. Because of this, in this case any groups which are members of a group on the source system will not be migrated unless they are part of a different group that is being migrated, or in the ACL of different content being migrated. To migrate these groups afterwards, consider using packages, deleting groups from the target and re-migrating the relevant content, or re-migrating using a wipe ingestion.
* During a non-wipe ingestion, if a group exists with any of the same uniqueness-constrained data (rep:principalName, rep:authorizableId, jcr:uuid or rep:externalId) on both the source AEM instance and the target AEM Cloud Service instance, the group in question is _not_ migrated and the previously existing group on the cloud system remains unchanged. This is logged in the Principal Migration Report.
* See [Migrating Closed User Groups](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/closed-user-groups-migration.md) for extra considerations for groups used in a Closed User Group (CUG) policy.

## Final Summary and Report

Once the extraction and ingestion have completed successfully, a report is generated showing the group migration details. See [How to Validate the Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/validating-content-transfers.md#how-to-validate-group-migration) for the details.
