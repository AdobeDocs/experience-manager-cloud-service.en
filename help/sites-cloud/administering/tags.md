---
title: Administering Tags
description: Learn how to administer tags in AEM to organize your content.
---

# Administering Tags {#administering-tags}

Tags are a quick and easy method of classifying your content. They can be thought of as keywords or labels (metadata) that allow content to be more quickly found.

It is best practices to minimize the number of tags that relate to the same ideas. For example, if you are managing content for an outdoor supply store, you probably don't need a tag for both *footwear* and *shoes*.

In Adobe Experience Manager (AEM), a tag can be a property of:

* A content node for a page
  * See the document [Using Tags](/help/sites-cloud/authoring/features/tags.md) for more information.
* A metadata node for an asset 
  * See the document [Managing Metadata for Digital Assets](/help/assets/manage-metadata.md) for more information.

## Tag Features {#tag-features}

Tags offer robust features for organizing and managing content.

* Tags can be grouped into various namespaces.
  * These can be thought of as hierarchies that allow taxonomies to be built. 
  * These taxonomies are global throughout AEM.
* Tags can be applied by authors and site visitors.
* Irrespective of their creator, all forms of tags are made available for selection, both when assigning to a page, or when searching.
* Tags are used by the [List Component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/wcm-components/list.html) to generate dynamic lists based on the tags selected.


If tagging is an important aspect of your content, make sure to:

* Package tags with the pages that use them
* Configure [tag permissions](#setting-tag-permissions)

## Tag Requirements {#requirements}

There are a few technical details to keep in mind when creating and managing tags.

* Tags must be unique within a specific namespace.
* A tag's name may not include tag delimiters:
  * Colon (`:`) - Delimits the namespace tag
  * Slash (`/`) - Delimits sub-tags
* If a tag's title includes tag delimiters, they will be suppressed in the UI.
* Tags can be created and their taxonomy can be modified by members of the `tag-administrators` group and members who have modification rights to `/content/cq:tags`.
  * A tag that contains child tags is referred to as a container tag.
  * A tag that is not a container tag is referred to as a leaf tag.
  * A tag namespace can be either a leaf tag or container tag.

## Tagging Console {#tagging-console}

The tagging console is used to create and manage tags and their taxonomies. You can use the tagging console to manage your tags by:

* Grouping them into namespaces.
* Reviewing the usage of exiting tags before creating new ones.
* Reorganizing your tags without disconnecting the tag from currently referenced content.

To access the tagging console:

1. Sign in to an authoring environment with with administrative privileges.
1. In the global navigation menu select **`Tools`** -&gt; **`General`** -&gt;
**`Tagging`**.

![The tagging console in AEM](/help/sites-cloud/administering/assets/tagging-console.png)

You can use the tagging console to [create new namespaces](#creating-a-namespace) and tags as well as manage existing tags.

## Creating a Namespace {#creating-a-namespace}

A namespace is itself a tag, and need not contain any sub-tags. However, to continue creating a taxonomy, [create sub-tags](#creating-tags), which in turn may be either leaf tags or container tags.

1. To create a new namespace, open the [tagging console](#tagging-console) and tap or click the **Create** button in the toolbar and then **Create Namespace**.

   ![Add Namespace dialog](/help/sites-cloud/administering/assets/add-namespace.png)

1. Provide the necessary information.

   * **Title** - A title for the namespace displayed to the user in the UI (optional)
   * **Name** - If a name is not specified, a valid node name is created from the **Title**. See the document [AEM Tagging Framework](/help/implementing/developing/introduction/tagging-framework.md#tagid) for more information.
   * **Description** - A description of the namespace (optional)

1. Once the required information is entered tap or click **Create**.

You can now create new tags in this namespace or manage existing tags.

### Operations on Tags {#operations-on-tags}

Selecting a namespace or other tag makes available the following operations:

* [View Properties](#viewing-tag-properties)
* [References](#showing-tag-references)
* [Create Tag](#creating-tags)
* [Edit](#editing-tags)
* [Move](#moving-tags)
* [Merge](#merging-tags)
* [Publish](#publishing-tags)
* [Unpublish](#unpublishing-tags)
* [Delete](#deleting-tags)

![chlimage_1-184](assets/chlimage_1-184.png)

When the browser window is not wide enough to display all icons, then the right-most icons are grouped together under a **`... More`** icon, which will display a drop-down list of the hidden operation icons when selected.

![chlimage_1-185](assets/chlimage_1-185.png)

### Selecting a Namespace Tag {#selecting-a-namespace-tag}

When first selected, if the namespace does not contain any tags, then the properties are displayed to the right, else the child tags are displayed. Each tag selected will display either the tags it contains or its properties if it does not have child tags.

To select the tag for operations, and to multi-select, only select the icon next to the title. Selecting the title will only display properties or open the tag to display its contents.

![chlimage_1-186](assets/chlimage_1-186.png) ![chlimage_1-187](assets/chlimage_1-187.png)

### Viewing Tag Properties {#viewing-tag-properties}

![chlimage_1-188](assets/chlimage_1-188.png)

When a namespace or other tag is selected, selecting the **`View Properties`** icon results in the display of information as to the `name`, time of last edit, and number of references. If published, the time it was last published and the id of the publisher are shown. This information will appear in a column to the left of the tag columns.

![chlimage_1-189](assets/chlimage_1-189.png)

### Showing Tag References {#showing-tag-references}

![chlimage_1-190](assets/chlimage_1-190.png)

When a namespace or other tag is selected, selecting the **References** icon will identify the content to which the tag has been applied.

The initial display is a count of tags applied.

![chlimage_1-191](assets/chlimage_1-191.png)

By selecting the arrow to the right of the count, the reference names are listed.

The path to the reference is displayed as a tool tip when hovering over a reference.

![chlimage_1-192](assets/chlimage_1-192.png)

### Creating Tags {#creating-tags}

![chlimage_1-193](assets/chlimage_1-193.png)

When a namespace or other tag is selected (by selecting the icon next to the title), a child tag may be created for the current tag by selecting the **`Create Tag`** icon.

![chlimage_1-194](assets/chlimage_1-194.png)

* **Title**
  *(required) *A display title for the tag.

* **Name**
  *(optional) *A name for the tag. If not specified, a valid node name is created from the Title. See [TagID](/help/sites-developing/framework.md#tagid).

* **Description**
  *(optional) *A description of the tag.

Once the required information is entered

* select **Create**

### Editing Tags {#editing-tags}

![chlimage_1-195](assets/chlimage_1-195.png)

When a namespace or other tag is selected, it is possible to alter the Title, Description, and provide localizations of the Title by selecting the **`Edit`**icon.

After edits are made, select **Save**.

For details about adding language translations, see the section on [Managing Tags in Different Languages](#managing-tags-in-different-languages).

![chlimage_1-196](assets/chlimage_1-196.png)

### Moving Tags {#moving-tags}

![chlimage_1-197](assets/chlimage_1-197.png)

When a namespace or other tag is selected, selecting the **`Move`** icon will allow Tags Administrators and Developers to clean up the taxonomy by moving the tag to a new location or renaming it. When the selected tag is a container tag, moving the tag will move all child tags as well.

>[!NOTE]
>
>It is recommended that Authors only be allowed to [edit](#editing-tags) the tag's `title`, not to move or rename tags.

![chlimage_1-198](assets/chlimage_1-198.png)

* **Path**
  *(readonly)* The current path to the selected tag.

* **Move to**
  Browse to the new path under which to move the tag.

* **Rename to**
  Initially displays the current `name`of the tag. A new `name`may be entered.

* select **Save**

### Merging Tags {#merging-tags}

![chlimage_1-199](assets/chlimage_1-199.png)

Merging tags can be used when a taxonomy has duplicates. When tag A is merged into tag B, all the pages tagged with tag A will be tagged with tag B and tag A is no longer available to authors.

When a namespace or other tag is selected, selecting the **Merge** icon will open a panel where the path to merge into may be selected.

![chlimage_1-200](assets/chlimage_1-200.png)

* **Path**
  *(readonly)* The path of the tag selected to be merged into another tag.

* **Merge into**
  Browse to select the path of the tag to merge into.

>[!NOTE]
>
>After the merge, the **Path** originally selected will (virtually) no longer exist.
>
>When a referenced tag is moved or merged, the tag is not physically deleted such that it is possible to maintain references.

### Publishing Tags {#publishing-tags}

![chlimage_1-201](assets/chlimage_1-201.png)

When a namespace or other tag is selected, selecting the **Publish** icon to activate the tag in the publish environment. Similar to page content, only the selected tag is published, regardless of whether it is a container tag or not.

To publish a taxonomy (a namespace and sub-tags), the best practice is to create a [package](/help/sites-administering/package-manager.md) of the namespace (see [Taxonomy Root Node](/help/sites-developing/framework.md#taxonomy-root-node)). Be sure to [apply permissions](#setting-tag-permissions) to the namespace before creating the package.

### Unpublishing Tags {#unpublishing-tags}

![chlimage_1-202](assets/chlimage_1-202.png)

When a namespace or other tag is selected, selecting the **Unpublish** icon will deactivate the tag in the author environment and remove it from the publish environment. Similar to the `Delete`operation, if the selected tag is a container tag, all of its child tags will be deactivated in the author environment and removed from the publish environment.

### Deleting Tags {#deleting-tags}

![chlimage_1-203](assets/chlimage_1-203.png)

When a namespace or other tag is selected, selecting the **Delete** icon will permanently remove the tag from the author environment. If the tag was published, it is also removed from the publish environment. If the selected tag is a container tag, all of its child tags will be removed as well.

## Setting Tag Permissions {#setting-tag-permissions}

Tag permissions are ['secure (by default)'](/help/sites-administering/production-ready.md); a best practice for the publish environment that requires read permission to be explicitly allowed for tags. Bascially, this is done by creating a package of the Tag Namespace after permissions have been set on author, and installing the package on all publish instances.

* on author instance

    * sign in with administrative privileges
    * access the [Security Console](/help/sites-administering/security.md#accessing-user-administration-with-the-security-console),

        * for example, browse to http://localhost:4502/useradmin

    * in the left pane, select the group (or user) for which [read permission](/help/sites-administering/security.md#permissions) is to be granted
    * in the right pane, locate the **Path **to the Tag Namespace

        * for example, `/content/cq:tags/mycommunity`

    * select the `checkbox`in the **Read** column
    * select **Save**

![chlimage_1-204](assets/chlimage_1-204.png)

* ensure all publish instances have same permissions

    * one approach is to [create a package](/help/sites-administering/package-manager.md#package-manager) of the namespace on author

        * on `Advanced` tab, for `AC Handling` select `Overwrite`

    * replicate the package

        * choose `Replicate` from package manager

## Managing Tags in Different Languages {#managing-tags-in-different-languages}

The `title`property of a tag may be translated into multiple languages. Once translated, the appropriate tag `title`may be displayed according to the user language or to the page language.

### Defining Tag Titles in Multiple Languages {#defining-tag-titles-in-multiple-languages}

The following describes how to translate the `title`of the tag **Animals** from English into German and French.

Start by selecting the tag under the **Stock Photography** namespace and selecting the **`Edit`**icon (see [Editing Tags](#editing-tags) section).

The Edit Tag panel presents the ability to choose languages into which the tag title is to be localized.

As each language is selected, a text entry box appears into which the translated title may be entered.

Once all translations are entered, select **Save** to exit edit mode.

![chlimage_1-205](assets/chlimage_1-205.png)

In general, the language chosen for the tag is taken from the page language, when available. When the [ `tag` widget](/help/sites-developing/building.md#tagging-on-the-client-side) is used in other cases (for example in forms or in dialogs), the tag language depends on the context.

Instead of using the page language setting, the Tagging console uses the user language setting. In the Tagging console, for the 'Animals' tag, 'Animaux' would be displayed for a user who sets the language to French in their user properties.

To add a new language to the dialog, see [Adding a New Language to the Edit Tag Dialog](/help/sites-developing/building.md#adding-a-new-language-to-the-edit-tag-dialog).

>[!NOTE]
>
>The tag cloud and the meta keywords in the standard page component use the localized tag `titles`based on the page language, if available.

## Resources {#resources}

* [Tagging for Developers](/help/sites-developing/tags.md)

  Information about the tagging framework as well as extending and including tags in custom applications.

* [Classic UI Tagging Console](/help/sites-administering/classic-console.md)
