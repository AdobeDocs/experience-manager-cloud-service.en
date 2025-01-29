---
title: Migrating Closed User Groups
description: Learn about the required special considerations to enable Closed User Groups after migrating content to Adobe Experience Manager as a Cloud Service.
hide: yes
hidefromtoc: yes
exl-id: f62ed751-d5e2-4a01-8910-c844afab5733
feature: Migration
role: Admin
---

# Migrating Closed User Groups {#migrating-closed-user-groups}

>[!CONTEXTUALHELP]
>id="aemcloud_cug_migration"
>title="Migration of Closed User Groups"
>abstract="Migration of Closed User Groups (CUG) currently requires a few checks and steps to make it operational after a migration."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/closed-user-groups.html" text="Closed User Groups in AEM"

Currently, Closed User Groups (CUG) need some additional steps to be functional in the destination environment of a migration. This document explains the scenario, and the steps required to have them protect nodes in the intended way.

## Migration of Closed User Groups (CUGs)

Groups are automatically included in a CTT/CAM migration to Adobe Experience Manager as a Cloud Service if they are associated to the migrated content via that content's ACL or its CUG policy node. Verifying that the group and its members exist should be done before going live. Groups referenced on a CUG policy are referred to here as "CUGs groups."

To use CUGs in AEM as a Cloud Service, users must be present on the Author instance and be members of the relevant CUGs groups.  This can be accomplished using packages, or if the CUGs users are IMS users, they may already be present.  CUGs users must then be made members of the AEM CUGs groups.

To enable CUGs behavior on the Publish instance,
1. The CUGs groups must be activated (which replicates them and their members to the Publish instance),
1. *All* pages protected with CUGs policies must be unpublished (to clear the global CUGs count), and
1. The pages protected with CUGs policies must then be published (which enables the Publish instance and to track the policies).
1. After all the pages are published, verify the functionality for each CUG protected page.

For additional information, see [Closed User Groups](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/closed-user-groups.html).
