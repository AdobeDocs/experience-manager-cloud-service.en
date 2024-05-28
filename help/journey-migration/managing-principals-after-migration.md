---
title: Managing Principals after Migration
description: Learn how to set up users and groups in IMS and AEM
---
# Managing Principals after Migration {#managing-principals-after-migration}

>[!CONTEXTUALHELP]
>id="managing-principals"
>title="Managing Principals after Migration"
>abstract="Learn how to set up users and groups in IMS and AEM"

This document describes high level steps customers should take to set up their users and groups in IMS and AEM to work with their AEM as a Cloud Service environment.

## Managing Principals {#managing-principals}

For AEM as a Cloud Service, users and groups must primarily be managed using the Admin Console.  When considering a migration, some of these tasks can be carried out before the content migration happens.  Essentially, of these main task groups

* Create Users and Groups in IMS
* Assign Users to Groups in IMS
* Assign IMS groups to AEM groups

the first two may be carrried out before the content migration.  They are steps which affect users and groups in IMS only, possibly including integration with an external IDP such as Active Directory or LDAP.  These steps are described in [Managing Principals in IMS with the Admin Console](/help/journey-migration/managing-principals.md)

Once the content is migrated to the AEM as a Cloud Service environment, the third step can be carried out.

### Assigning IMS Groups to AEM Groups in AEM

Local (non-IMS) AEM groups are typically those that have been migrated along with the content.  AEM local groups are referred to in Access Control Lists of content to give their members access to that content; assigning an IMS group to an AEM local group passes on the access to its member IMS group and to that group's members (users and/or groups).  It is via this membership chaining that a specific user can have access to specific AEM content.

Use the AEM Security UI to assign IMS groups to local AEM groups.  See [Creating and Configuring Groups](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/forms/administrator-help/setup-organize-users/creating-configuring-groups#edit-a-group).  Although this document is for AEM 6.5, it also applies to adding groups to other groups in AEM as a Cloud Service.

