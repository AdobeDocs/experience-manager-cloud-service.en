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

With this setting disabled, groups will not be migrated, and there will be no Principal Migration report or User Report (see below).

## Principal Migration Report and User Report {#principal-migration-report}

When groups are included during migration (the default), a Principal Migration Report is saved which outlines what happens to each group during the migration.  To download this report after a successful ingestion:
* In CAM, go to Content Transfer and select Ingestion Jobs.
* Click the ellipsis (...) on the line of the Ingestion in question, and choose "View principal summary".
* On the dialog that appears, select select "Principal Migration Report" from the dropdown list under "Download a file..." and click the Download button.
* Save the resulting CSV file.

Some of the information recorded per group is:
* If migrated, the path to the first ACL or CUG that caused the group to be migrated.
* Whether the group was previously migrated; if the current ingestion was a non-wipe ingestion, some groups may have been migrated during a previous ingestion.
* Whether the group is a built-in group; these groups are not migrated because they are always on the target AEMaaCS environment.
* If the group was not part of an ACL or a CUG on the migrated content, it would not have been migrated.
* If the group was a local group, such as a group created by an Assets Collection, it may have been migrated, and in this case the word "local" is added to the report for that group.

During migration users are not migrated, but the user-group relationships on the source system would be lost unless they were somehow captured. The Ingestion process captures some of this information in text format in a User Report, which is at the end of the Principal Migration Report. 

### User Report {#user-report} ###

In the User Report section users are reported (one per line) along with their email address and a list of IMS-enabled groups that were migrated during this ingestion.  Groups that were not migrated, were migrated during a previous ingestion, or are local groups, are not included in the list.   If a user is not in any migrated IMS-enabled group, and it has no extra notes indicating it is a special case (see **Notes** below), that user does _not_ appear in the report. The groups reported along with each user are those the user is a member of, directly or indirectly, in the source system; since groups in the source system may be nested while in the target system they are not, this list of groups supports the new flattened group structure in IMS.

In the case of a wipe and then a non-wipe ingestion, the groups in a user's list from the non-wipe ingestion will only be those groups migrated during the non-wipe phase.

#### Notes {#user-report-notes} ####

In addition to the groups for each user, there is a field in the User Report where notes about the user may be provided (and a detailed description of the note's meaning is also in the report) for information purposes.  Possible notes are:

* **Note-A** Users which are referenced directly in an ACL will have *Note-A* in their notes section, as this is not a recommended use case or best practice.
* **Note-B** Users which are direct members of a built-in group will have *Note-B* in their notes section, as this is also not a recommended use case or best practice.
* **Note-C** Users which are direct of indirect members of a migrated local group (such as a group created by an Assets Collection) will have *Note-C* in their notes section, as local groups are not configured to be managed by IMS.

These cases can occur simultaneously, and also at the same time as the earlier cases.  _For additional information about which groups each Note refers to for each user, check the Ingestion log; it reports this information for each user._

The User Report is added onto the end of (and is therefore part of) the Principal Migration Report (see [Final Summary and Report](#final-summary-and-report) below) to give customers a more complete understanding of the groups and users, and their relationships.

## Bulk Upload Files {#bulk-upload-files}

Since groups are migrated only to AEM as a Cloud Service, they still must also be added to IMS so they can work properly with AEM in the cloud. Additionally, users are not migrated, so they also need to be added to IMS. The CTT/CAM migration tooling does not perform this step, but the Ingestion process creates two bulk upload files, one for groups and one for users. These files can be edited and then used, along with the Admin Console's bulk upload functionality, to create IMS groups and users based on your AEM groups and users.

See [Bulk Group and User Uploading to IMS](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/bulk-principal-uploading.md) for details about how to use bulk upload files to create users and groups using the Admin Console.

Also see [Manage users](https://helpx.adobe.com/ca/enterprise/using/users.html) for additional details about managing AEM as a Cloud Service users.

## Additional Considerations {#additional-considerations}

* If the setting **Wipe existing content on Cloud instance before ingestion** is set, groups previously transferred to the Cloud Service instance are deleted along with the entire existing repository; a new repository is created into which content is ingested. This process also resets all settings including permissions on the target Cloud Service instance and is true for any user added to the **administrators** group. The admin user must be re-added to the **administrators** group to retrieve the access token for CTT/CAM Ingestion.
* When non-wipe ingestions are performed (**Wipe existing content** is unset), if content is not transferred because it has not changed since the previous transfer, groups associated with that content are not transferred either. This rule is true even if the groups have changed on the source system. This is because groups are only migrated along with the content they are associated with. Because of this, in this case any groups which are members of a group on the source system will not be migrated unless they are part of a different group that is being migrated, or in the ACL of different content being migrated. To migrate these groups afterwards, consider using packages, deleting groups from the target and re-migrating the relevant content, or re-migrating using a wipe ingestion.
* During a non-wipe ingestion, if a group exists with any of the same uniqueness-constrained data (rep:principalName, rep:authorizableId, jcr:uuid or rep:externalId) on both the source AEM instance and the target AEM Cloud Service instance, the group in question is _not_ migrated and the previously existing group on the cloud system remains unchanged. This is logged in the Principal Migration Report.
* See [Migrating Closed User Groups](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/closed-user-groups-migration.md) for extra considerations for groups used in a Closed User Group (CUG) policy.

## Final Summary and Report

Once the extraction and ingestion have completed successfully, a report is generated showing the group migration details. See [How to Validate the Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/validating-content-transfers.md#how-to-validate-group-migration) for the details.
