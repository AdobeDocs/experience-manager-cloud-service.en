---
title: Manage Collections in Content Hub
description: Learn how to manage collections in Content Hub
role: User
exl-id: ea74456c-f980-4a02-b26b-d7c46dac6aee
---

# Manage collections in [!DNL Content Hub] {#manage-collections}

<!-- ![Manage collections](assets/manage-collections.jpg) -->
![Manage collections](assets/manage-collection.png)

A collection refers to a set of assets that can be shared among users. A collection can include assets from different locations while maintaining their referential integrity.

[!DNL Content Hub] lets you create public collections. These collections are accessible to all the entitled users, creating a shared space where multiple users can efficiently access and utilize content. Collections promote collaborative use of resources for increased efficiency and convenience. Within the collection browse page, you can: 

* **Create**: Create one or more collections.
* **View**: View the assets and their properties.  
* **Share**: Share assets as a link with others. 
* **Download**: Download the assets.
* **Remove**: Remove specific assets from a collection. 
* **Delete**: Delete the entire collection. 
* **Pin/Unpin**: Pin or unpin collection.
* **Favorite**: Mark collection as favorite.

It helps users to easily access and manage the diverse assets available within [!DNL Content Hub].

## Prerequisites {#prerequisites}

[Content Hub users](deploy-content-hub.md#onboard-content-hub-users) can perform the actions mentioned in this article.

## Create collections{#create-collections}

You can choose to [create a new collection](#create-new-collection) or [add assets to an existing collection](#add-assets-to-existing-collection) while managing governance.

### Create a new collection{#create-new-collection}

Execute the steps below to control access while creating collections:

1. Go to **[!DNL Collections]** tab and click **[!UICONTROL Create Collection]**. A new Collection window appears.

1. Add **[!UICONTROL Title]** and **[!UICONTROL Description]** for the collection.

    ![collection permissions](assets/collection-permissions.png)

1. Under **[!UICONTROL Who can access]** dropdown > select the access control type. The following options are available:

    |Access method | Access type | Description |
    |---|---|---|
    | **Only you and administrators can edit**| Private | Only creator and the administrators can edit and access this collection. |
    | **Anyone can view**| Public | Everyone can access this collection, but only creator and Administrators can edit. |
    | **Anyone can view and edit**| Public | This collection is open to everyone, with full access and editing permissions granted without restrictions.|

    >[!NOTE]
    >
    > [!DNL Content Hub] administrator can view all the options available under **[!UICONTROL Who can access]** dropdown, whereas for regular users, you need to [specify and configure](configure-content-hub-ui-options.md) which options they can access.

1. Click **[!UICONTROL Create]**. Once done, you can [add assets to the collection](#add-assets-to-existing-collection).

>[!VIDEO](https://video.tv.adobe.com/v/3463336) 

<!--
>[!NOTE]
>
>Collections governance is a limited availability feature. You can get it enabled  by creating a support ticket. Once enabled, you need to [Configure Collections in Content Hub](configure-content-hub-ui-options.md#configure-collections-content-hub).-->

<!--To create a new collection, navigate to the **[!UICONTROL Collections]** tab and click **[!UICONTROL Create new collection]**. Enter the **[!UICONTROL Title]** and provide an optional **[!UICONTROL Description]** for the assets. Click **[!UICONTROL Create]**.
![Create collection](assets/add-assets-collection.jpg)          
-->

### Add assets to an existing collection{#add-assets-to-existing-collection}

To add assets to an existing collection, select the assets you need to add to the collection. Click **[!UICONTROL Add to collection]**. You are prompted to select the collection. 

 ![Create a new collection](assets/create-add-collection.jpg)

Choose the collection where you need to add the asset. You can also search the existing collection using the search bar. <br>Select the collection(s) to which you need to add the assets and click **[!UICONTROL Add to collection]**.

## View collections{#view-collections}

Navigate to the **[!UICONTROL Collections]** tab and search for the collection name. You can use filters to refine your search results by selecting specific criteria, helping you quickly find the most relevant collections. 

To view the list of assets available in a collection, click the collection name. You can also apply filters within a collection to narrow down the asset results. Click the asset that you need to view within a collection. [!DNL Content Hub] displays the detailed view for the asset. [See asset details](asset-properties-content-hub.md).

### Filter collections view {#filter-collections-view}

Content Hub allows you to filter collections view to easily find exactly what you are looking for by narrowing down options based on your preferences. Ensure the [configuration of Collections in Content Hub](configure-content-hub-ui-options.md#configure-collections-content-hub).

To filter the collections view, go to **[!DNL Collections]** tab and navigate to Collections drop down. Choose among the following options:
    
* **[!UICONTROL All Collections]:** Select this option to view and edit all collections, including those that are private or shared with you.
* **[!UICONTROL Only me]:** Select this option to view collections that are accessible to you.
* **[!UICONTROL Anyone can view]:** This option lets you filter collections that are accessible to everyone but editable only by the creator.
* **[!UICONTROL Anyone can edit]:** Select this option to filter collections that are both accessible and editable by everyone.

    ![filter collections view](assets/filter-collection-view.png)

Moreover, to filter the collections view based on access permissions, go to **[!DNL Collections]** tab and navigate to one of the following options:

* **[!UICONTROL Created by anyone]:** This filter restricts you to view collections created by any user.

* **[!UICONTROL Created by me]:** This filter restricts you to view collections created by you.

    ![filter collections view](assets/filter-collection-view1.png)

<!--
![Asset details](assets/view-collection.jpg)

* **A**: Details and metadata of the asset 
* **B**: Zoom In or Zoom Out the asset 
* **C**: Reset Zoom view 
* **D**: View the previous or next asset 
* **E**: Download the asset 
* **F**: Open the asset in Adobe Express 
* **G**: Hide the metadata of the asset 
* **H**: Share the asset as a link 
-->

## Download assets available within a collection{#download-assets-within-collection}

To download assets available within a collection, navigate to the **[!UICONTROL Collections]** tab.  
Click ![download icon](assets/download-icon.svg) icon on the collection card. 

![Collection tab](assets/download-collection.png)

All the assets in the collection are downloaded.

You can also open the collection to download the assets individually. Click the collection containing the assets that you need to download. Select the assets and click **[!UICONTROL Download]**. 

Learn how to [download an asset from the [!DNL Content Hub]](download-assets-content-hub.md). 

## Share assets available within a collection {#share-assets-available-within-collection}

You can also share the assets available within a collection. Ensure to [enable public link sharing in Content Hub](configure-content-hub-ui-options.md#enable-public-link-sharing). Navigate to the **[!UICONTROL Collections]** tab. Select the ![share icon](assets/share.svg) icon on the collection card. The share link is copied. You can share the copied link with the recipient. Learn more about [sharing assets in the [!DNL Content Hub]](share-assets-content-hub.md).

Content Hub Collections provides comprehensive governance tools for effective asset management, including customizable sharing permissions and collaboration features. From read-only access to full administrative control, these settings support fine governance over asset distribution. When sharing an asset either individually or as part of a collection, the scope of access is determined by the collection's current access level assigned to the user. Alternatively, you cannot share a private collection.

## Edit details of a collection {#edit-details-of-collection}

To edit **[!UICONTROL Title]** and **[!UICONTROL Description]** of a collection, click the collection name and then click the ![info icon](assets/info-icon.svg) icon. [!UICONTROL Collection Details] screen appears that allows you to edit the **[!UICONTROL Title]** and **[!UICONTROL Description]** of a collection. Click **[!UICONTROL Save Changes]** to confirm the modifications. Moreover, you can update the access to the collection through the Edit Collection dialog, depending on the configuration.

![collection details](assets/collection-details.png)

## Remove assets from a collection{#remove-assets-from-a-collection}

The following users can remove single or multiple assets from a collection:

* An administrator 
* An owner of collection
* A non-admin user with the edit rights

To remove assets from a collection, click the collection from which you need to remove assets, select the assets and click **[!UICONTROL Remove from collection]**. 

 ![Remove collection](assets/remove-collection-new.jpg)

You are prompted to confirm the asset removal. Click **[!UICONTROL Remove]**.  
The selected assets are successfully removed from the collection. 

## Delete a collection{#delete-collection}

Only administrators and creator can delete a collection. To delete a collection, navigate to the **[!UICONTROL Collections]** tab and click the collection that you need to delete. Click ![delete icon](assets/delete-icon.svg) icon to delete the collection.

## Pin or Unpin collection {#pin-unpin-collection}

Content Hub Administrators can pin collections in Content Hub for quick access. Pinned collections are displayed in a dedicated Pinned section on the Collections home page, making it easier to keep important collections within reach. For quick access, you can pin or unpin a collection by executing the steps below:

1. Browse the Collections which you want to pin or unpin.

1. Click **[!UICONTROL More actions]** ![More actions icon](assets/do-not-localize/more-actions.png) and select **[!UICONTROL Pin to quick access]**. A confirmation box appears.

    ![pin collection](assets/pin-collection.png)

1. Click **[!UICONTROL Pin]** to confirm. The warning message appears when you pin a private collection.

    ![Confirm pin collection](assets/confirm-pin-collection.png)

    The pinned Collections appear on the top for quick access. Alternatively, to unpin the collection, click **[!UICONTROL More actions]** ![More actions icon](assets/do-not-localize/more-actions.png) and select **[!UICONTROL Unpin]**.

    ![View pinned collections](assets/pinned-collections.png)
 
## Mark Collections as Favorite {#favorite-collection}

You can mark Collections as Favorite in Content Hub, making it easier to organize and retrieve them. Once added, your favorite collections are conveniently available from the Favorites tab on the Content Hub home page. Additionally, you can search assets within Favorite Collections. To mark collections as Favorites, follow these steps:

1. Browse the Collections you want to mark as Favorites.

1. Click **[!UICONTROL More actions]** ![More actions icon](assets/do-not-localize/more-actions.png) and select **[!UICONTROL Add to Favorites]** to mark collection as Favorite.

    ![Mark Collections as Favorite](assets/mark-favorite-collection.png)

    Collections marked as Favorites now display under **[!UICONTROL My Favorites]** tab. Alternatively, you can remove the Collections from **[!UICONTROL My Favorites]**. To do this, click **[!UICONTROL More actions]** ![More actions icon](assets/do-not-localize/more-actions.png) and select **[!UICONTROL Remove from Favorites]**.

    ![Remove Collection as Favorite](assets/remove-favorite-collection.png)
