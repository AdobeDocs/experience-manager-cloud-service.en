---
title: Migrating Closed User Groups
description: Learn about the required special considerations to enable Closed User Groups after migrating content to Adobe Experience Manager as a Cloud Service.
hide: yes
hidefromtoc: yes
exl-id: f62ed751-d5e2-4a01-8910-c844afab5733
---
# Migrating Closed User Groups {#migrating-closed-user-groups}

>[!CONTEXTUALHELP]
>id="aemcloud_cug_migration"
>title="Migration of Close User Groups"
>abstract="Migration of Closed User Groups (CUG) currently requires a few checks and steps to make it operational after a migration."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/closed-user-groups.html" text="Closed User Groups in AEM"

Currently, Closed User Groups (CUG) need some additional steps to be functional in the destination environment of a migration. This document explains the scenario, and the steps required to have them protect nodes in the intended way.

## Migration of Groups

Principals (including groups) are automatically included in a migration to Adobe Experience Manager as a Cloud Service if they are associated to the migrated content through that content's ACL. 

## Closed User Groups in Migration

Currently, groups associated *only* with a Closed User Group (CUG) policy are *not* automatically included in the ingestion. As said above, they are migrated if they are associated with any content through an ACL. Verifying the group and its members exist should be done before going live. The Principal Report, downloaded through the Ingestions Job view, can be used to see if the group in question was included, or was not because it was not in an ACL. If the group does not exist, it should be created in the Author instance including adding appropriate members, and activated to have it exist on the Publish instance. This can be done using packages created on the source.

Finally, processes have to be triggered and properties must be set to enable CUGs. To do this, republish all pages that are associated with a CUG policy. This calibrates the Publish instance to track the policies.

This enables CUG policies on Publish, and the content is only accessible to those authenticated users that are members of the group associated with the policies.

## Active Development

The migration team is working to make CUG policies migrate and function automatically, without any additional steps after ingesting the content.
Include CUG functionality in any testing processes before attempting to go live.

## Summary

In summary, these are the steps to enable CUG after a migration:

1. Ensure each group used in CUG policies exists on Publish after the migration.
   - A group may exist if included in a migrated content's ACL.
   - If it does not, use Packages to install it on the destination instance (or create it manually there) and activate it and its members. Then verify it exists on Publish.
1. Republish all pages associated with a CUG policy, ensuring it is published by, for example, editing the page first. It is important to republish all of them.
    - After all the pages are republished, verify the functionality for each CUG protected page.
