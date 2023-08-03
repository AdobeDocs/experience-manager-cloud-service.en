---
title: Migrating Closed User Groups
description: This page provides the required, special considerations to enable Closed User Groups after migrating content to Adobe Experience Manager as a Cloud Service.
---
# Migrating Closed User Groups {#migrating-closed-user-groups}

>[!CONTEXTUALHELP]
>id="aemcloud_cug_migration"
>title="Migration of Close User Groups"
>abstract="Migration of Closed User Groups (CUG) currently requires a few checks and steps to make operational after a migration."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/closed-user-groups.html" text="Closed User Groups in AEM"

Currently, Closed User Groups (CUG) need some additional steps to be functional in the destination environment of a migration.  This document
explains the scenario, and the steps required to have them protect nodes in the intended way.

## Migration of Groups

Principals (including groups) are automatically included in a migration to Adobe Experience Manager as a Cloud Service if they are
associated to the migrated content through that content's ACL. 

## Closed User Groups in Migration

Currently, groups associated *only* with a Closed User Group (CUG) policy are *not* automatically included in the ingestion. If they are
associated with any content through an ACL, as said above, then they will be migrated. Verification that the group exists should be done before
going live. The Principal Report, downloaded through the Ingestions Job view, can be used to see if the group in question was included, or was not
because it was not in an ACL. If the group does not exist, it should be created in the Author instance including adding appropriate members, and
activated in order to have it exist on the Publish instance.

It is most likely that configurations exist in the `/conf` path related to CUG operation. The app related information in `/conf` should be included
as a path during the extraction.

Finally, processes have to be triggered to enable CUG. To do this re-publish any of the content that contains the CUG policy. So, in your normal
testing processes, if it is found that the CUG does not work, re-publish that content (ensuring it is published even if not modified).

This should enable CUG policies on Publish, and the content will only be accessible to those authenticated users that are members of the group
associated with the policies.

## Active Development

The migration team is working to make CUG policies migrate and function automatically, without any addition steps after ingesting the content.
It is advisable to include CUG functionality in any testing processes before attempting to go live.

## Summary

In summary, these are the steps to enable CUG after a migration:

1. Include the app-related configurations in the source `/conf` path in the extraction.
2. Ensure each group used in CUG policies exists on Publish after the migration.
   - A group may already exist if included in a migrated content's ACL.
   - If it does not, use packages to install it on the destination Author instance (or create it manually there) and activate it and its members. Then verify it exists on Publish.
3. If the CUG policy does not yet protect the node, re-publish the page again (ensuring it publishes even if no changes were made to that page).
   - Verify for each CUG protected node.
