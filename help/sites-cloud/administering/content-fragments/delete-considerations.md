---
title: Content Fragments - Delete Considerations
description: Review these important considerations before defining your Content Fragments deletion policies in AEM. Content Fragments are a powerful tool for delivering headless content, and the implications of deleting them must be carefully considered.
feature: Content Fragments
role: User, Developer, Architect
exl-id: d1726bff-3aa8-4758-bee7-0cacea1f660a
solution: Experience Manager Sites
---
# Delete Considerations for Content Fragments {#delete-considerations-content-fragments}

Review these important considerations before defining your deletion policies for Content Fragments in AEM. Content Fragments are a powerful tool for delivering headless content, and the implications of deleting them must be carefully considered.

## Permissions - Delete or Not Delete {#permissions-delete-or-not-delete}

The ability to delete content is powerful, but potentially sensitive, with many industries needing to restrict and control how these privileges are distributed.

In relation to delete permissions, Content Fragments must be considered at two levels:

1. **The Content Fragment as a single entity.**

    * **Use case**: A user who must edit/update a Content Fragment - **and delete an entire fragment**.
    * **Permissions**: The Delete permission can be assigned through User and/or Group Management.

2. **The multiple subentities that make up a Content Fragment; for example, variations, subnodes.**

   Basic operation of the Content Fragment editor requires that such transient subelements can be deleted. For example, when manipulating variations; also when editing metadata or managing associated content.

    * **Use case**: A user who must edit/update a Content Fragment - **without being allowed to delete an entire fragment**.
    * **Permissions**: See [Permissions Required for Editor Functionality Only](#permissions-required-for-editor-functionality-only).

>[!NOTE]
>
>See also How to Audit User Management Operations in AEM.

## Permissions Required for Editor Functionality Only {#permissions-required-for-editor-functionality-only}

For users that need to edit/update a Content Fragment, **without allowing them to delete an entire fragment**, specific permissions must be assigned, as basic operation of the Content Fragment editor requires that transient subelements can be deleted.

For example, when manipulating variations; also when editing metadata or managing associated content.

>[!NOTE]
>
>The delete permissions, required to edit/update a Content Fragment, are included in the Delete permission assigned through User and/or Group Management. 

The permissions needed to edit/update a fragment must be applied to either the node containing the Content Fragment, or an appropriate parent node (at any level under `/content/dam`). When assigned to such a parent node, the permissions are applied to all nodes within that branch.

For example, a folder to hold all Content Fragments, such as:

* `/content/dam/contentfragments`

>[!CAUTION]
>
>Setting the permissions on `/content/dam` is also possible, as all Content Fragments are stored here.
>
>However this action applies the same delete permissions to *all* other asset types as well.

The permissions prerequisite to allowing a specific user and/or group to edit/update a Content Fragment are:

>[!NOTE]
>
>This list shows all the privileges required, not just the delete privileges.

* For the Content Fragment nodes or folders:

  * `jcr:addChildNodes`, `jcr:modifyProperties`

* For the `jcr:content`node of all Content Fragments:

  * `jcr:addChildNodes`, `jcr:modifyProperties`, and `jcr:removeChildNodes`

* For all nodes below `jcr:content` of all Content Fragments:

  * `jcr:addChildNodes`, `jcr:modifyProperties`, and `jcr:removeChildNodes`, `jcr:removeNode`
