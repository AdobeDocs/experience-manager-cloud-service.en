---
title: Managing Principals after Migration
description: Learn how to set up users and groups in IMS and AEM
exl-id: 46c4abfb-7e28-4f18-a6d4-f729dd42ea7b
---
# Managing Principals after Migration {#managing-principals-after-migration}

>[!CONTEXTUALHELP]
>id="managing-principals"
>title="Managing Principals after Migration"
>abstract="Learn how to set up users and groups in IMS and AEM"

This document describes high level steps customers should take to set up their users and groups in IMS and AEM to work with their AEM as a Cloud Service environment.  

For information on group migration and the Principal Migration Report available with each ingestion, see [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md).

For a guide on using bulk group and user files in Admin Console, see [Bulk Upload of Principals to IMS after using CTT](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/bulk-principal-uploading.md).

## Managing Principals {#managing-principals}

For AEM as a Cloud Service, users and groups must be managed primarily using the Admin Console.  When considering a migration, some of these tasks can be carried out before the content migration happens.  Essentially, of these main task groups

* Create Users and Groups in IMS
* Assign Users to Groups in IMS
* Assign IMS groups to AEM groups (if necessary)

The first two may be carried out before or after the content migration.  They are steps which affect users and groups in IMS only, possibly including integration with an external IDP such as Active Directory or LDAP.  These steps are described in [Managing Principals in IMS with the Admin Console](/help/journey-migration/managing-principals.md).

Once the content is migrated to the AEM as a Cloud Service environment, the third step can be carried out.

### Migrating Groups

During the ingestion phase of the migration, groups are migrated if they are required to satisfy the ACLs or CUG policies on the migrated content.  See [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md) for more details.

Migrated groups (those not created by Assets Collection creation &mdash; see Collections below) are configured as IMS groups.  What this means is that any group of the same name created in IMS (via the Admin Console, for instance) will be linked to the group in AEM, and users which are members of the IMS group will become members of the group in AEM as well.  In order for this linking to happen, the group must also be created in IMS first.  Use the Admin Console to create groups, individually or in bulk, in your AEM instance, as described in [Managing Principals in IMS with the Admin Console](/help/journey-migration/managing-principals.md).

Use the AEM Security UI to assign IMS groups to local AEM groups. To do this, go to the Tools page in AEM, click on Security, and choose Groups.

### IMS Users

Since users are not migrated, they must be created in IMS so that they can be used in AEM.  There are several ways to achieve this, but it is important that the users created be assigned to the correct IMS groups in order for the users to have the same access to the content they had in the previous AEM system.  One of the tools that can be used for this is the bulk upload functionality in the Admin Console; use the bulk uploader to upload users along with groups they must be members of.  Before doing this the groups must first be created in IMS, as described above.

To know which groups each user should belong to, you can make use of the User Report (see [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md)).  This report lists the groups each user should be a member of, and this list will normally be included in the Bulk User input file for use with the Admin Console bulk upload functionality.

### Collections

Creation of an Assets Collection also automatically creates some groups to manage access to that collection.  These groups are migrated if they are mentioned on migrated collections, but they are not configured to link to IMS groups directly; in AEM they remain "local groups", and they cannot be managed via IMS.

Since these groups are not in IMS, the bulk upload tool cannot be used to create users as their direct members.  IMS users which are also in AEM can be added to these groups individually, but doing this in bulk requires an extra step.  Here is one way this can be done:
* Create a new group or groups in Admin Console/IMS for access to collections and configure them for AEM.
* Log in as a member of the group(s) so the group(s) are created in AEM.
* For the migrated collections, use the Assets Collections UI to add the new group as editor/owner/viewer.
* Add (or bulk upload) users to the new group(s) in Admin Console.
* When the user logs in for the first time, their IMS user will be created in AEM and they should have access to the new group(s) and thereby the original collection groups.

Note: For bulk assigning of users, the above steps must be used to create the users in IMS; users that already exist in IMS cannot be created again via bulk upload, though the bulk editor can be used to make those kinds of changes (See [Admin Console Bulk User upload](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html) under **Edit user details**).
