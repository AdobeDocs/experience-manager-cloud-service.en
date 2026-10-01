---
title: Manage digital assets collections
description: Understand the concept of collection in Adobe Experience Manager Assets. Learn how to collections, manage, edit, and collections with other users.
contentOwner: AG
mini-toc-levels: 1
feature: Collections, Asset Management
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: b0798adc-56a4-4577-b4ee-8d1fca3bff09
---
# Manage collections {#manage-collections}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/manage-collections.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

A **collection** is a set of assets within Adobe [!DNL Experience Manager] (AEM) Assets. Collections enable users to group, organize, and share assets between team members, making them a core tool for collaborative asset management. Use collections to distribute assets between users, streamline creative workflows, and provide controlled access to curated sets of content. A collection can be a **static collection** or a **dynamic collection** that is based on search results.

Unlike folders, a collection can include assets from different locations across the digital asset management repository. This flexibility allows teams to assemble related content regardless of where individual assets are stored. You can share collections with multiple users, each assigned specific privilege levels such as viewing, editing, and full administrative control, ensuring that access rights match each user's role.

You can share multiple collections with a single user. Each collection contains references to assets rather than duplicate copies of the files. As a result, the **referential integrity** of assets is maintained across collections. This means that when an asset is referenced in several collections, updates and changes to that asset remain consistent everywhere it appears, preventing duplication and reducing storage overhead.

## Collection Types in AEM Assets

Collections are of the following types, based on the way they collate assets:

* **Static collection** — Contains a static reference list of assets, folders, and other collections. The contents remain fixed until a user manually adds or removes items, giving teams precise control over exactly which assets belong to the set.

* **Smart collection** — Dynamically includes assets based on defined search criteria. Because a smart collection is driven by search results, its contents update automatically as new assets matching the criteria are added to the repository, ensuring the collection always reflects the most current qualifying assets without manual maintenance.

## Access the collections console {#navigate-the-collections-console}

The **[!UICONTROL Collections]** console is the central workspace in [!DNL Experience Manager] for organizing, grouping, and managing related digital assets in a single location.

To open the **[!UICONTROL Collections]** console, follow these steps:

1. Select the **[!DNL Experience Manager]** logo to return to the main navigation page.
2. From the navigation page, go to **[!UICONTROL Assets]** > **[!UICONTROL Collections]**.

The **[!UICONTROL Collections]** console opens, displaying the available collections. From here, you can browse existing collections and manage the assets grouped within them.

## Create a collection {#create-a-collection}

A **collection** groups related assets together so they can be organized, retrieved, and shared as a single set. Collections make it easier to keep frequently used or thematically related content in one place, whether that content is selected manually or gathered automatically based on defined criteria.

A collection can be created using three methods:

- **Static references** — Build a collection by manually adding specific assets, giving you full control over exactly which items are included. See [static references](#create-a-collection-with-static-references). This method is best when the desired assets are already known and the collection contents are not expected to change automatically.
- **Search criteria-based filter (smart collection)** — Build a collection that populates dynamically based on a defined search filter, so matching assets are included automatically. See [smart collection](#create-a-smart-collection). This method is best when the collection should update as new assets meet the specified criteria.
- **From a lightbox** — Convert an existing lightbox of gathered assets directly into a collection, reusing a working selection without starting over.

Choosing between these methods depends on whether the collection should remain fixed to a chosen set of assets or update automatically as content changes.

### Create a collection with static references {#create-a-collection-with-static-references}

A collection with static references is a **collection that holds fixed links to specific content items** in Adobe [!DNL Experience Manager] (AEM) Assets. You can create a collection with static references to **assets**, **folders**, **collections**, **spin sets**, and **image sets**, grouping related content together for streamlined access, review, and sharing.

1. Navigate to the **[!UICONTROL Collections]** console.
1. From the toolbar, select **[!UICONTROL Create]**.
1. In the **[!UICONTROL Create Collection]** page, enter a title and an optional description for the collection.
1. Add members to the collection and assign appropriate permissions. Alternatively, select **[!UICONTROL Public Collection]** to allow all users to access the collection.

   >[!NOTE]
   >
   >To enable the members to share collections with other users, provide the `dam-users` group read permissions at the path `home/users`. This ensures members have the access required to distribute collections beyond their own account. Give permission to the users at `/content/dam/collections` location so that those users can view the Collections in pop-up lists. Alternatively, make the user a part of the `dam-users` group.

1. (Optional) Add a thumbnail image for the collection.
1. Select **[!UICONTROL Create]**, and then select **[!UICONTROL OK]** to close the dialog. A collection with the specified title and properties opens in the Collections console.

   >[!NOTE]
   >
   >Adobe [!DNL Experience Manager] (AEM) Assets lets you create review tasks for a collection in the same way you create review tasks for an assets folder.

   To add assets to the collection, navigate to the Assets user interface. For details, see [Add assets to a collection](#add-assets-to-a-collection).

### Create collections using dropzone {#create-collections-using-dropzone}

Drag assets directly from the Assets user interface into a collection using the dropzone. You can also duplicate an existing collection and drag assets into the copy, which lets you reuse a collection's structure without rebuilding it.

Follow these steps to create a collection using the dropzone:

1. From the Assets user interface, select the assets you want to add to a collection.
1. Drag the selected assets to the **[!UICONTROL Drop in Collection]** zone. Alternatively, select the **[!UICONTROL To Collection]** icon from the toolbar. Both methods open the same workflow for adding assets to a collection.
1. In the **[!UICONTROL Add To Collection]** page, select the **[!UICONTROL Create Collection]** icon from the toolbar. To add the assets to an existing collection instead, select the collection from the page and select **[!UICONTROL Add]**. **By default, the most recently updated collection is selected**, which speeds up adding assets to the collection you worked with most recently.
1. In the **[!UICONTROL Create New Collection]** dialog, specify a name for the collection. To make the collection accessible to all users rather than only yourself, select **[!UICONTROL Public Collection]**, because this setting grants shared visibility across users.
1. Select **[!UICONTROL Continue]** to create the collection. The new collection is created and the selected assets are added to it.

### Create a smart collection {#create-a-smart-collection}

A **Smart Collection** uses **search criteria** to **dynamically populate assets**, automatically including any file that matches the defined query. Unlike a static collection, a Smart Collection updates itself as new matching assets are added, ensuring the collection always reflects the current search results. You can create a Smart Collection using only files, or using both folders and files — organizing assets consistently as your library grows.

1. Navigate to the Assets UI, and select the **[!UICONTROL Search]** icon.
1. Enter a search keyword in the Omni Search box and select `Enter`. Select the GlobalNav icon to display the Filters panel and apply a search filter from the Search panel. These filters define the criteria that determine which assets the Smart Collection includes.
1. From the **[!UICONTROL Files & Folders]** list, select **[!UICONTROL Files]**.
1. Select **[!UICONTROL Save Smart Collection]**.
1. Specify a name for the collection. Select **[!UICONTROL Public]** to add the Digital Asset Management (DAM) Users group with the Viewer role to the smart collection. This grants shared visibility so that members of the DAM Users group can view the collection.

   >[!NOTE]
   >
   >If you select **[!UICONTROL Public]**, the smart collection becomes available to everyone with the Owner role after you create it. If you cancel the **[!UICONTROL Public]** option, the DAM user group is no longer associated with the smart collection, and access remains restricted.

1. Select **[!UICONTROL Save]** to create the smart collection, and then close the message box to complete the process. The new smart collection is also added to the **[!UICONTROL Saved Searches]** list, allowing you to reuse the underlying search at any time.
   The label of the **[!UICONTROL Create Smart Selection]** button changes to **[!UICONTROL Edit Smart Selection]**. To edit the settings of the smart collection, select **[!UICONTROL Files]** from the **[!UICONTROL Files & Folders]** list. Then, select the **[!UICONTROL Edit Smart Selection]** button.

## Add assets to a collection {#add-assets-to-a-collection}

Adding assets to a collection lets you group a curated list of referenced assets or folders under a single collection. This provides a stable, manually managed set of assets that remains consistent regardless of search criteria, making it ideal for organizing and sharing specific groups of content.

>[!NOTE]
>
>Smart collections populate their contents automatically using a search query rather than fixed references. Because a smart collection is defined by dynamic search results, static references to individual assets and folders do not apply to it. As a result, you cannot manually add assets or folders to a smart collection—its membership is determined solely by the query that matches assets in real time.

1. In the Assets UI, navigate to the location of the asset that you want to add to a collection. This ensures you are working from the exact source asset before initiating the add action.
1. Select the asset, then select the **[!UICONTROL To Collection]** icon from the toolbar. Alternatively, drag the asset to the **[!UICONTROL Drop in Collection]** zone. Release the mouse button when the drop zone becomes active and its label changes to **[!UICONTROL Drop to Add]**, which confirms the target is ready to receive the asset.
1. In the **[!UICONTROL Add To Collection]** page, select the collection to which you want to add the asset.
1. Select **[!UICONTROL Add]**, then close the confirmation message. The asset is now added to the selected collection, where it appears as a referenced item within that collection.

## Edit a smart collection {#edit-a-smart-collection}

**Smart collections** are dynamic collections built by saving a search. Because a smart collection stores search parameters rather than a fixed list of assets, you edit its content by modifying the filters of the underlying [saved search](#saved-searches). This lets the collection update automatically whenever matching assets change.

1. In the Assets user interface, select the **[!UICONTROL Search]** icon from the toolbar.
1. With the cursor in the Omnisearch box, select the `Enter` key.
1. Select the GlobalNav icon to display the Filters panel.
1. From the **[!UICONTROL Saved Searches]** list, select the smart collection you want to modify. The Search panel displays the filters configured for the saved search, so you can review the current criteria before making changes.
1. From the **[!UICONTROL Files & Folders]** list, select **[!UICONTROL Files]**.
1. Modify one or more filters as necessary. Select **[!UICONTROL Edit Smart Collection]**. You can also edit the name of the smart collection to keep it descriptive and easy to locate later.
1. Select **[!UICONTROL Save]**. The **[!UICONTROL Edit Smart Collection]** dialog appears.
1. Choose how to save the edited collection: Select **[!UICONTROL Overwrite]** to replace the original smart collection with the edited version, keeping a single collection. Alternatively, select **[!UICONTROL Save As]** to preserve the original and save the edited collection separately as a new smart collection.
1. In the confirmation dialog, select **[!UICONTROL Save]** to complete the process.

## View and edit collection metadata {#view-and-edit-collection-metadata}

**Collection metadata** is the descriptive data about a collection, including any **tags** that are added. This metadata identifies, describes, and organizes the collection, making it easier to search, filter, and manage assets. Reviewing and keeping this metadata accurate ensures collections remain discoverable and properly categorized.

### Steps to view and edit collection metadata

Follow these steps to view and edit collection metadata:

1. From the Collections console, select a collection and select the **[!UICONTROL Properties]** icon from the toolbar.
1. In the **[!UICONTROL Collection Metadata]** page, view the collection metadata from the **[!UICONTROL Basic]** and **Advanced** tabs. The **[!UICONTROL Basic]** tab displays core descriptive metadata, while the **Advanced** tab exposes additional, more detailed metadata fields, giving you complete control over how the collection is described.
1. Modify the metadata, as necessary, and then select **[!UICONTROL Save & Close]** from the toolbar to save the updated metadata.

### Edit collection metadata in bulk {#edit-collection-metadata-in-bulk}

Bulk metadata editing lets you edit the metadata of multiple collections simultaneously in a single operation. This functionality replicates common metadata across multiple collections quickly, eliminating the need to update each collection individually and saving considerable time when standardizing shared metadata values.

1. In the Collections console, select two or more collections for which you want to edit metadata.
1. From the toolbar, select the **[!UICONTROL Properties]** icon.
1. In the **[!UICONTROL Collection Metadata]** page, edit the metadata under the **[!UICONTROL Basic]** and **[!UICONTROL Advanced]** tabs, as necessary.
1. Select **[!UICONTROL Save & Close]** from the toolbar, and then close the confirmation dialog to complete the process.
1. To append the new metadata to the existing metadata, select **[!UICONTROL Append mode]**. This ensures the existing values are preserved and the new metadata is added alongside them. If you do not select this option, the new metadata replaces the existing metadata in the fields, because replacement is the default behavior. Select **[!UICONTROL Submit]**.

   >[!NOTE]
   >
   >The Append mode works only for fields that can contain multiple values. For fields that can contain only a single value, the new metadata is not appended to the existing value in the field even if you select **[!UICONTROL Append mode]**. This is because a single-value field cannot hold more than one entry, so the new value simply overwrites the current one.

## Search {#searching}

The **Search feature within Collections** supports two distinct search modes: **[Search for collections](#search-collections)** and **[Search for assets within a Collection](#search-within-collections)**. Together, these two capabilities allow you to locate content at both the collection level and the individual asset level from a single, unified search experience.

The two supported search modes are:

- **[Search for collections](#search-collections)** — Locates entire collections by name or attributes. This mode is useful when you know the collection you are looking for but need to navigate to it quickly among a large number of collections.
- **[Search for assets within a Collection](#search-within-collections)** — Locates specific assets contained inside a collection. This mode narrows the search scope to a single collection, allowing you to pinpoint individual items without browsing the full collection manually.

Because the Search feature covers both the collection level and the asset level, you can move efficiently from finding the right collection to finding the exact asset within it. This layered approach reduces the time spent browsing and helps you retrieve the specific content you need, whether you are searching broadly across collections or drilling down into the contents of one.

### Search collections {#search-collections}

Search collections directly from the Collections console in [!DNL Experience Manager Assets]. When you enter keywords in the **Omnisearch box**, [!DNL Experience Manager Assets] matches those keywords against the searchable attributes of each collection, returning results that align with the terms you provide.

#### What Omnisearch matches

[!DNL Experience Manager Assets] searches the following attributes when you look for collections:

- **Collection names** — the title assigned to each collection.
- **Metadata** — descriptive properties associated with the collection.
- **Tags** — the tags added to the collections to categorize and label them.

Because Omnisearch evaluates all three of these attributes, a keyword that appears in a collection's name, its metadata, or one of its assigned tags will surface that collection in the results.

#### Search results by starting location

The location from which you initiate the search determines which items appear in the results:

- **Searching from the top level:** Only individual collections are returned in search results. Assets and folders contained within those collections are excluded. This scoping keeps top-level results focused on collections themselves rather than the items nested inside them.
- **Searching within a collection or folder hierarchy:** In all other cases—for example, from inside an individual collection or within a folder hierarchy—all relevant assets, folders, and collections are returned. As a result, the deeper you search, the broader the range of item types that appear in the results.

### Search within Collections {#search-within-collections}

In the Collections console, select a collection to open it. Once a collection is open, **Adobe [!DNL Experience Manager] search is scoped exclusively to the contents of that collection** — searching from within a collection never returns results from outside it. This scoping keeps results relevant to the context you are working in, rather than surfacing matches from across the entire asset repository.

Within a collection, [!DNL Experience Manager] search is restricted to **assets**, along with their associated **tags** and **metadata**, that belong to the currently open collection. Understanding how this scope differs from folder-based search is essential for retrieving the correct results.

#### Searching within a folder

- Search returns **all matching assets** within the current folder.
- Search also returns **matching child folders** contained within the current folder.
- Folder search therefore traverses the folder hierarchy to surface nested matches.

#### Searching within a collection

In contrast to folder search, searching within a collection returns only items that are **direct members of that collection**. Specifically, search returns:

- **Matching assets** that are direct members of the collection.
- **Matching folders** that are direct members of the collection.
- **Other collections** that are direct members of the collection.

Because collection search is limited to direct members, items that are not explicitly added to the collection do not appear in the results. This ensures that search results remain precisely scoped to the collection you are viewing, giving you predictable, focused results when working within organized collections.

## Edit collection settings {#edit-collection-settings}

Collection owners and editors can modify collection settings at any time, including the title, description, member list, and permissions. Editing these settings keeps a collection's metadata accurate and up to date, refines who can access or contribute to the collection, and ensures the collection remains organized as its purpose or membership evolves.

### Steps to edit collection settings

To edit collection settings, follow these steps:

1. Select a collection, and select the **[!UICONTROL Settings]** icon in the toolbar. Alternatively, use the **[!UICONTROL Settings]** quick action from the collection thumbnail.
1. Modify the collection settings in the **[!UICONTROL Collection Settings]** page to keep the collection's metadata current and to manage who can view or contribute. For example, modify the collection title, descriptions, members, and permissions as discussed in [Add collections](#create-a-collection). Updating the title and description clarifies the collection's purpose, while adjusting members and permissions controls access and contribution rights.
1. Select **[!UICONTROL Save]** to apply and save the changes.

## Delete a collection {#delete-a-collection}

1. From the Collections console, select one or more collections, then click the delete (trash) icon in the toolbar. Selecting multiple collections lets you remove several items in a single batch operation.
1. In the confirmation dialog that appears, select **[!UICONTROL Delete]** to confirm the delete action. This confirmation step prevents accidental removal, because deleting a collection is permanent and cannot be undone.

   >[!NOTE]
   >
   >You can also delete Smart collections. Because Smart collections are generated from saved searches, you remove them by [deleting the corresponding saved searches](#saved-searches) rather than deleting the collection directly.

## Download a collection {#download-a-collection}

<!-- Select the **[!UICONTROL Email]** option to send an email notification to the owner of the collection. -->

Downloading a collection downloads the **entire hierarchy of assets** within that collection, including all **folders** and **child collections** nested beneath it. This ensures the complete structure of your collection is preserved in the downloaded output, rather than only the top-level assets.

1. From the **Collections console**, select one or more collections to download.
1. From the toolbar, select the **download icon**.
1. In the **[!UICONTROL Download]** dialog, select **[!UICONTROL Download]** to begin the download. To also include the generated renditions of the assets within the collection, select **[!UICONTROL Renditions]** before confirming.

   When you select a collection to download, the **complete folder hierarchy** under the collection is downloaded, preserving the original organization of parent and child collections. To place each collection you download—including the assets in **child collections nested under the parent collection**—into its own individual folder, select **[!UICONTROL Create separate folder for each asset]**. This option keeps assets clearly organized and prevents files from different collections from being merged into a single flat folder.

## Edit metadata properties of multiple collections {#editing-metadata-properties-of-multiple-collections}

Adobe [!DNL Experience Manager] (AEM) Assets lets you edit the metadata of many collections in bulk, saving significant time compared to updating each collection individually. Use the [!UICONTROL Properties] page to perform metadata changes on multiple collections, for example, change metadata properties to a common value or add or modify tags.

To customize the metadata [!UICONTROL Properties] page, including adding, modifying, deleting metadata properties, use the Schema editor.

>[!NOTE]
>
>The bulk editing methods work for assets available in a collection. For the assets that are available across folders or match a common criteria, you can [bulk update the metadata after searching](/help/assets/search-assets.md#metadata-updates).

1. From the collections console, select the collections you want to edit.
1. From the toolbar, select **[!UICONTROL Properties]** to open the [!UICONTROL Properties] page for the selected collections.
1. Modify the metadata properties for selected collections under the various tabs.

   >[!NOTE]
   >
   >The metadata you add for the selected collections overwrites the previous metadata for these collections, except for tags. Any tags you add in the **[!UICONTROL Tags]** field are appended to the existing list of tags rather than replacing them, ensuring that established taxonomy is preserved.

1. To view the metadata properties for a specific collection, cancel the selection of the remaining collections in the collections list. The metadata editor fields are populated with the metadata for the particular collection.

   >[!NOTE]
   >
   >* In the collection properties page, you can remove collections from the list of collections by clearing the selection of the remaining collections. The collections list has all the collections selected by default. The metadata for collections that you remove is not updated.
   >* At the top of the list, select the check box near **[!UICONTROL Title]** to toggle between selecting the collections and clearing the list.

1. Save the changes.

## Create nested collections {#create-nested-collections}

You can add one collection inside another collection to create a **nested collection**—a hierarchical structure in which a parent collection contains one or more child collections. Nesting organizes related assets under a single grouping, making large asset libraries easier to browse, manage, and navigate.

1. From the Collections console, select the desired collection or group of collections, then select **[!UICONTROL To Collection]** in the toolbar.
1. From the **[!UICONTROL Add To Collection]** page, select the target collection in which to place the selected collection.

   >[!NOTE]
   >
   >The most recently updated collection is selected by default in the **[!UICONTROL Add To Collection]** page.

1. Select **[!UICONTROL Add]**. A confirmation message appears in the **[!UICONTROL Select Destination]** page, verifying that the collection has been added to the target collection. Close the message to complete the process.

>[!NOTE]
>
>Smart collections cannot be nested. Because Smart collections are generated dynamically from search criteria rather than from manually assigned members, a Smart collection cannot contain any other collection.

## Saved searches {#saved-searches}

**Saved searches** in the Assets user interface let you store search criteria for reuse and, at the same time, generate a corresponding smart collection. In the Assets user interface, you can search or filter assets based on defined rules, specific search criteria, or **custom search facets**—the filterable attributes such as file type, metadata, or tags that narrow results. When you save these as **[!UICONTROL Saved Searches]**, you can access them later from the **[!UICONTROL Saved Searches]** list in the Filter panel. Because a saved search and a smart collection are directly linked, creating a saved search automatically creates a smart collection.

Every saved search corresponds to a smart collection. As a result, smart collections are added automatically to the **[!UICONTROL Saved Searches]** list. The Saved Searches query for each collection is stored in the **`dam:query`** property in CRXDE at the relative location **`/content/dam/collections/`**. There are no limits to the number of searches that you can save or on the saved searches displayed in the list, so you can maintain as many reusable queries as your workflow requires without needing to reconstruct complex filters each time.

>[!NOTE]
>
>You can share smart collections in the same way that you share static collections.

Editing saved searches works the same way as editing smart collections. For details, see [Edit a smart collection](#edit-a-smart-collection).

To delete saved searches, follow these steps:

1. In the Assets user interface, select the search icon from the toolbar.

1. With the cursor in the Omnisearch field, select the `Enter` key.
1. Select the GlobalNav icon to display the Filters panel.
1. From the **[!UICONTROL Saved Searches]** list, select **[!UICONTROL Delete]** next to the smart collection you want to delete.
1. In the dialog, select **[!UICONTROL Delete]** to delete the saved search.

## Execute a workflow on a collection {#run-a-workflow-on-a-collection}

Adobe [!DNL Experience Manager] (AEM) can run a workflow across every asset within a collection, and users can trigger a workflow directly from the Collections console. When a collection contains nested collections, the workflow also processes the assets within those nested collections, ensuring complete coverage of the entire collection hierarchy. However, **if the collection and a nested collection contain duplicate assets, the workflow runs only once for such assets**. This deduplication prevents redundant processing of the same asset and ensures consistent, efficient workflow execution.

1. From the Collections console, select a collection on which you want to run a workflow.
1. Select the GlobalNav icon, and choose **[!UICONTROL Timeline]** from the list.
1. From the timeline, select the Caret icon at the bottom, and then select **[!UICONTROL Start Workflow]**.
1. In the **[!UICONTROL Start Workflow]** section, select a workflow model from the list. For example, select the **[!UICONTROL DAM Update Asset]** model.
1. Enter a title for the workflow, and select **[!UICONTROL Start]**.
1. In the dialog, select **[!UICONTROL Proceed]**. The workflow then runs on all the assets in the collection, confirming that processing has begun across the entire asset set.

**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in Assets view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)


>[!MORELIKETHIS]
>
>* [Create a review task for Collections](/help/assets/bulk-approval.md)
