---
title: Managing Principals after Migration
description: Learn how to set up users and groups in IMS and AEM
---
# Managing Principals after Migration {#managing-principals}

>[!CONTEXTUALHELP]
>id="managing-principals"
>title="Managing Principals after Migration"
>abstract="Learn how to set up users and groups in IMS and AEM"

This document describes high level steps customers should take to set up their users and groups in IMS and AEM to work with their AEM as a Cloud Service environment.

## After Migration {#after-migration}

Once the content is migrated to the AEM as a Cloud Service environment, users of the AEM authoring system must be created and given access to the content. This is done by following these steps.

* Create Users and Groups in IMS
* Assign Users to Groups in IMS
* Assign IMS groups to AEM groups

### Creating Users and Groups in IMS

The documents linked below provide detailed instructions on how to create users and groups in IMS, including three options for creating them: Manually through the Admin Console, via CSV upload through the Admin Console, and via a User Sync Tool.

### Assigning Users to Groups in IMS

Use the Admin Console, manually or via CSV upload, to add IMS users to IMS groups.  See the links below for further instructions.

Once a user uses IMS to log into AEM, an AEM version of the user will be created.  Furthermore, any IMS groups the user is in will have equivalent AEM groups created in AEM.  These AEM users and groups are still managed using the Admin Console.

### Assigning IMS Groups to AEM Groups in AEM

Use the AEM Security UI to assign IMS groups to AEM groups.  

AEM local groups are typically those that have been migrated along with the content.  AEM local groups are referred to in Access Control Lists of content to give their members access to that content; assigning an IMS group to an AEM local group passes on the access to its member IMS group and to that group's members (users and/or groups).  It is via this membership chaining that a specific user can have access to specific AEM content.  (link??)


See [Using Admin Console for AEM Principals](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/ims-support#how-to-set-up) to learn more about how Admin Console is used for managing users and groups.

See [Tutorial, AEM users, groups and permissions](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/accessing/aem-users-groups-and-permissions) to learn more about how AEM and IMS users and groups are integrated and administered.

