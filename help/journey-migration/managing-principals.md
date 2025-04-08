---
title: Managing Principals
description: Managing Principals for Migration, using Admin Console
exl-id: a75598d0-8f59-466b-984e-dfe527388c2a
---
# Managing Principals {#managing-principals}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_managingprincipals"
>title="Managing Principals"
>abstract="Learn what needs to be done to manage users during or after a content migration"

Before content is transferred to the AEM as a Cloud Service cloud environment, there are a few tasks that can be carried out on the Admin Console.  They are: create users, create groups, and assign users to groups; these users and groups will exist in in IMS, Adobe's Identity Management Service, which is used to manage users and groups for all Adobe cloud-based services.

### Creating Groups and their Users in Admin Console

[Using Admin Console for AEM Principals](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/ims-support#how-to-set-up) provides detailed instructions on how to create users and groups in IMS, and how to add the users to the groups at the same time or later.  The document includes three options for creating them: Manually through the Admin Console, via CSV upload through the Admin Console, and via a User Sync Tool.  

The manual option lets you create one group or user at a time; the CSV upload allows you do create and link several user and groups at once; and the User Sync Tool lets you use an existing IDP to create and manage the IMS users and groups.

Once a user uses IMS to log into AEM, an AEM representation of the user will be created.  Furthermore, any IMS groups the user is in will have equivalent AEM groups created in AEM.  These IMS-created AEM users and groups are still mainly managed using the Admin Console.

After the content migration is complete, IMS groups will typically need to have some additional configuration on them so that users can access the migrated content.  See [Migrating Principals After Migration](/help/journey-migration/managing-principals-after-migration.md)

See also [Tutorial, AEM users, groups and permissions](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/accessing/aem-users-groups-and-permissions) to learn more about how AEM and IMS users and groups are integrated and administered.
