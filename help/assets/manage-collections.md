---
title: Manage digital assets collections
description: Understand the concept of collection in Adobe Experience Manager Assets. Learn how to collections, manage, edit, and collections with other users.
contentOwner: AG
mini-toc-levels: 1
feature: Collections, Asset Management
role: User
exl-id: b0798adc-56a4-4577-b4ee-8d1fca3bff09
---
# Manage collections {#manage-collections}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/manage-collections.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

A collection is a set of assets within Adobe Experience Manager Assets. Use collections to share assets between users. The set can be static collection or a dynamic collection that is based on search results.

Unlike folders, a collection can include assets from different locations. You can share collections with various users that are assigned different levels of privileges, including viewing, editing, and so on.

You can share multiple collections with a user. Each collection contains references to assets. The referential integrity of assets is maintained across collections.

Collections are of the following types, based on the way they collate assets:

* A collection that contains a static reference list of assets, folders, and other collections.

* A smart collection that dynamically includes assets based on a search criteria.

## Access the collections console {#navigate-the-collections-console}

To open the **[!UICONTROL Collections]** console:

To open the **[!UICONTROL Collections]**, select the Experience Manager logo. From the navigation page, go to **[!UICONTROL Assets]** > **[!UICONTROL Collections]**.

## Create a collection {#create-a-collection}

You can create a collection either with [static references](#create-a-collection-with-static-references) or based on a [search criteria-based filter](#create-a-smart-collection). You can also create a collection from a lightbox.

### Create a collection with static references {#create-a-collection-with-static-references}

You can create a collection with static references, for example, a collection with references to assets, folders, collections, spin sets, and image sets.

1. Navigate to the **[!UICONTROL Collections]** console.
1. From the toolbar, select **[!UICONTROL Create]**.
1. In the **[!UICONTROL Create Collection]** page, enter a title and an optional description for the collection.
1. Add members to the collection and assign appropriate permissions. Alternatively, select **[!UICONTROL Public Collection]** to allow all users to access the collection.

   >[!NOTE]
   >
   >To enable the members to share collections with other users, provide the `dam-users` group read permissions at the path `home/users`. Give permission to the users at `/content/dam/collections` location to allow the users to view the Collections in pop up lists. Alternatively, make the user a part of `dam-users` group.

1. (Optional) Add a thumbnail image for the collection.
1. Select **[!UICONTROL Create]**, and then select **[!UICONTROL OK]** to close the dialog. A collection with the specified title and properties is opened in the Collections console.

   >[!NOTE]
   >
   >Experience Manager Assets lets you create review tasks for a collection similar to the way you create review tasks for an assets folder.

   To add assets to the collection, navigate to the Assets user interface. For details, see [Add assets to a collection](#add-assets-to-a-collection).

### Create collections using dropzone {#create-collections-using-dropzone}

You can drag assets from the Assets UI to a collection. You can also create a copy of a collection and drag the assets there.

1. From the Assets user interface, select the assets you want to add to a collection.
1. Drag the assets to the **[!UICONTROL Drop in Collection]** zone. Alternatively, select the **[!UICONTROL To Collection]** icon from the toolbar.
1. In the **[!UICONTROL Add To Collection]** page, select the **[!UICONTROL Create Collection]** icon from the toolbar. If you want to add the assets to an existing collection, select it from the page, and select **[!UICONTROL Add]**. By default, the most recently updated collection is selected.
1. In the **[!UICONTROL Create New Collection]** dialog, specify a name for the collection. If you want the collection to be accessible to all users, select **[!UICONTROL Public Collection]**.
1. Select **[!UICONTROL Continue]** to create the collection.

### Create a smart collection {#create-a-smart-collection}

A Smart Collection uses a search criteria to dynamically populate assets. You can create a Smart Collection using only files and not folders or files and folders.

1. Navigate to the Assets UI, and select the **[!UICONTROL Search]** icon.
1. Enter search keyword in the Omni Search box and select `Enter`. Select the GlobalNav icon to display the Filters panel and apply a search filter from the Search panel.
1. From the **[!UICONTROL Files & Folders]** list, select **[!UICONTROL Files]**.
1. Select **[!UICONTROL Save Smart Collection]**.
1. Specify a name for the collection. Select **[!UICONTROL Public]** to add the DAM Users group with the Viewer role to the smart collection.

   >[!NOTE]
   >
   >If you select **[!UICONTROL Public]**, the smart collection becomes available to everyone with the Owner role after you create it. If you cancel the **[!UICONTROL Public]** option, the DAM user group is no longer associated with the smart collection.

1. Select **[!UICONTROL Save]** to create the smart collection, and then close the message box to complete the process. The new smart collection is also added to the **[!UICONTROL Saved Searches]** list.
   The label of the **[!UICONTROL Create Smart Selection]** button changes to **[!UICONTROL Edit Smart Selection]**. To edit the settings of the smart collection, select **[!UICONTROL Files]** from the **[!UICONTROL Files & Folders]** list. Then, select the **[!UICONTROL Edit Smart Selection]** button.

## Add assets to a collection {#add-assets-to-a-collection}

You can add assets to a collection that contains a list of referenced assets or folders.

>[!NOTE]
>
>Smart collections use a search query to populate assets. Therefore, static references to assets and folders are not applicable to them.

1. In the Assets UI, navigate to the location of the asset that you want to add to a collection.
1. Select the asset and select the **[!UICONTROL To Collection]** icon from the toolbar. Alternatively, you can drag the asset to the **[!UICONTROL Drop in Collection]** zone. Release the mouse button when the drop zone becomes active and its label changes to **[!UICONTROL Drop to Add]**.
1. In the **[!UICONTROL Add To Collection]** page, select the collection to which you want to add the asset.
1. Select **[!UICONTROL Add]**, and then close the confirmation message. The asset is added to the collection.

## Edit a smart collection {#edit-a-smart-collection}

Smart collections are built by saving a search so you can alter their content by modifying the search parameters of the [saved search](#saved-searches).

1. In the Assets user interface, select the **[!UICONTROL Search]** icon from the toolbar.
1. With the cursor in the Omnisearch box, select the `Enter` key.
1. Select the GlobalNav icon to display the Filters panel.
1. From the **[!UICONTROL Saved Searches]** list, select the smart collection you want to modify. The Search panel displays the filters configured for the saved search.
1. From the **[!UICONTROL Files & Folders]** list, select **[!UICONTROL Files]**.
1. Modify one or more filters, as necessary. Select **[!UICONTROL Edit Smart Collection]**. You can also edit the name of the smart collection.
1. Select **[!UICONTROL Save]**. The **[!UICONTROL Edit Smart Collection]** dialog appears.
1. Select **[!UICONTROL Overwrite]** to replace the original smart collection with the edited collection. Alternatively, select **[!UICONTROL Save As]** to save the edited collection separately.
1. In the confirmation dialog, select **[!UICONTROL Save]** to complete the process.

## View and edit collection metadata {#view-and-edit-collection-metadata}

Collection metadata comprises data about the collection, including any tags that are added.

1. From the Collections console, select a collection and select the **[!UICONTROL Properties]** icon from the toolbar.
1. In the **[!UICONTROL Collection Metadata]** page, view the collection metadata from the **[!UICONTROL Basic]** and **Advanced** tabs.
1. Modify the metadata, as necessary, and then select **[!UICONTROL Save & Close]** from the toolbar to save the changes.

### Edit collection metadata in bulk {#edit-collection-metadata-in-bulk}

You can edit the metadata of multiple collections simultaneously. This functionality helps you quickly replicate common metadata in multiple collections.

1. In the Collections console, select two or more collections for which you want to edit metadata.
1. From the toolbar, select the **[!UICONTROL Properties]** icon.
1. In the **[!UICONTROL Collection Metadata]** page, edit the metadata under the **[!UICONTROL Basic]** and **[!UICONTROL Advanced]** tabs, as necessary.
1. Select **[!UICONTROL Save & Close]** from the toolbar, and then close the confirmation dialog to complete the process.
1. To append the new metadata with the existing metadata, select **[!UICONTROL Apend mode]**. If you do not select this option, the new metadata replaces the existing metadata in the fields. Select **[!UICONTROL Submit]**.

   >[!NOTE]
   >
   >The Append mode works only for fields that can contain multiple values. For fields that can contain only a single value, the new metadata is not appended to the existing value in the field even if you select **[!UICONTROL Append mode]**.

## Search {#searching}

The Search feature within Collections supports both [Search for collections](#search-collections) and [Search for assets within a Collection](#search-within-collections).

### Search collections {#search-collections}

You can search collections from the Collections console. When you search with keywords in the Omnisearch box, [!DNL Experience Manager Assets] searches for collection names, metadata, and the tags added to the collections.

If you search for collections from the top level, only individual collections are returned in search results. Assets or folders within the collections are excluded. In all other cases (for example, within an individual collection or in a folder hierarchy), all relevant assets, folders, and collections are returned.

### Search within Collections {#search-within-collections}

In the Collections console, select a collection to open it.

Within a collection, [!DNL Experience Manager] search is restricted to assets (and their tags and metadata) within the collection that you are viewing. When you search within a folder, all matching assets and child folders within the current folder are returned. When you search within a collection, only matching assets, folders, and other collections that are direct members of the collection are returned.

## Edit collection settings {#edit-collection-settings}

You can edit collection settings, such as title and description, or to add members to a collection.

1. Select a collection, and select the **[!UICONTROL Settings]** icon in the toolbar. Alternatively, use the **[!UICONTROL Settings]** quick action from the collection thumbnail.
1. Modify the collection settings in the **[!UICONTROL Collection Settings]** page. For example, modify the collection title, descriptions, members, and permissions as discussed in [Add collections](#create-a-collection).
1. Select **[!UICONTROL Save]** to save the changes.

## Delete a collection {#delete-a-collection}

1. From the Collections console, select one or more collections and select the delete icon in the toolbar.
1. In the dialog, select **[!UICONTROL Delete]** to confirm the delete action.

   >[!NOTE]
   >
   >You can also delete Smart collections by [delete saved searches](#saved-searches).

## Download a collection {#download-a-collection}

When you download a collection, the entire hierarchy of assets within the collection is downloaded, including folders and child collections.

1. From the Collections console, select one or more collections to download.
1. From the toolbar, select the download icon.
1. In the **[!UICONTROL Download]** dialog, select **[!UICONTROL Download]**. If you want to download the renditions of the assets within the collection, select **[!UICONTROL Renditions]**. <!-- Select the **[!UICONTROL Email]** option to send an email notification to the owner of the collection. -->

   When you select a collection to download, the complete folder hierarchy under the collection is downloaded. To include each collection you download (including assets in child collections nested under the parent collection) in an individual folder, select **[!UICONTROL Create separate folder for each asset]**.

## Edit metadata properties of multiple collections {#editing-metadata-properties-of-multiple-collections}

Adobe Enterprise Manager Assets lets you edit the metadata of many collections in bulk. Use the [!UICONTROL Properties] page to perform metadata changes on multiple collections, for example, change metadata properties to a common value or add or modify tags.

To customize the metadata [!UICONTROL Properties] page, including adding, modifying, deleting metadata properties, use the Schema editor.

>[!NOTE]
>
>The bulk editing methods work for assets available in a collection. For the assets that are available across folders or match a common criteria, it is possible to [bulk update the metadata after searching](/help/assets/search-assets.md#metadata-updates).

1. From the collections console, select the collections you want to edit.
1. From the toolbar, select **[!UICONTROL Properties]** to open the [!UICONTROL Properties] page for the selected collections.
1. Modify the metadata properties for selected collections under the various tabs.

   >[!NOTE]
   >
   >The metadata you add for the selected collections overwrites the previous metadata for these collections, except for tags. Any tags you add in the **[!UICONTROL Tags]** field, are appended to the existing list of tags in the metadata.

1. To view the metadata properties for a specific collection, cancel the selection of the remaining collections in the collections list. The metadata editor fields are populated with the metadata for the particular collection.

   >[!NOTE]
   >
   >* In the collection properties page, you can remove collections from the list of collections by canceling the selection. The collections list has all the collections selected by default. The metadata for collections that you remove is not updated.
   >* At the top of the list, select the check box near **[!UICONTROL Title]** to toggle between selecting the collections and clearing the list.

1. Save the changes.

## Create nested collections {#create-nested-collections}

You can add a collection to another collection, thereby creating a nested collection.

1. From the Collections console, select the desired collection or group of collections, and select **[!UICONTROL To Collection]** in the toolbar.
1. From the **[!UICONTROL Add To Collection]** page, select the collection in which to add the collection.

   >[!NOTE]
   >
   >The most recently updated collection is selected by default in the **[!UICONTROL Add To Collection]** page.

1. Select **[!UICONTROL Add]**. A message confirms that the collection is added to the target collection in the **[!UICONTROL Select Destination]** page. Close the message to complete the process.

>[!NOTE]
>
>Smart collections cannot be nested. In other words, Smart collections cannot contain any other collection.

## Saved searches {#saved-searches}

In the Assets user interface, you can search or filter assets based on certain rules, search criteria, or custom search facets. If you save these as **[!UICONTROL Saved Searches]**, you can access them later from the **[!UICONTROL Saved Searches]** list in the Filter panel. Creating a saved search also creates a smart collection.

Saved searches are created when you create a smart collection. Smart collections are automatically added to the **[!UICONTROL Saved Searches]** list. The Saved Searches query for the collection is saved in the `dam:query` property in CRXDE at the relative location `/content/dam/collections/`. There are no limits to the searches that you can save and on the saved searches displayed in the list.

>[!NOTE]
>
>You can share smart collections in the same way as you share static collections.

Editing saved searches is the same as editing smart collections. For details, see [Edit a smart collection](#edit-a-smart-collection).

To delete saved searches, follow these steps:

1. In the Assets user interface, select the search icon from the toolbar.

1. With the cursor in the Omnisearch field, select the `Enter` key.
1. Select the GlobalNav icon to display the Filters panel.
1. From the **[!UICONTROL Saved Searches]** list, select **[!UICONTROL Delete]** next to the smart collection you want to delete.
1. In the dialog, select **[!UICONTROL Delete]** to delete the saved search.

## Execute a workflow on a collection {#run-a-workflow-on-a-collection}

You can run a workflow for the assets within a collection. If the collection contains nested collections, the workflow also runs on the assets within the nested collections. However, if the collection and the nested collection contain duplicate assets, the workflow only runs once for such assets.

1. From the Collections console, select a collection on which you want to run a workflow.
1. Select the GlobalNav icon, and choose **[!UICONTROL Timeline]** from the list.
1. From the timeline, select the Caret icon at the bottom, and then select **[!UICONTROL Start Workflow]**.
1. In the **[!UICONTROL Start Workflow]** section, select a workflow model from the list. For example, select the **[!UICONTROL DAM Update Asset]** model.
1. Enter a title for the workflow, and select **[!UICONTROL Start]**.
1. In the dialog, select **[!UICONTROL Proceed]**. The workflow runs on all the assets in the collection.

**See also**

* [Translate Assets](translate-assets.md)
* [Assets HTTP API](mac-api-assets.md)
* [Assets supported file formats](file-format-support.md)
* [Search assets](search-assets.md)
* [Connected assets](use-assets-across-connected-assets-instances.md)
* [Asset reports](asset-reports.md)
* [Metadata schemas](metadata-schemas.md)
* [Download assets](download-assets-from-aem.md)
* [Manage metadata](manage-metadata.md)
* [Search facets](search-facets.md)
* [Bulk metadata import](metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

>[!MORELIKETHIS]
>
>* [Create a review task for Collections](/help/assets/bulk-approval.md)
