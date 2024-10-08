---
title: Private folders to share assets
description: Learn how to create a private folder in the [!DNL Adobe Experience Manager Assets] and share it with other users and the assign various privileges to them.
contentOwner: Vishabh Gupta
role: User
feature: Collaboration
exl-id: d48f6daf-af81-4024-bff2-e8bf6d683b0c
---
# Private folder in [!DNL Adobe Experience Manager Assets] {#private-folder}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/private-folder.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

You can create a private folder in the [!DNL Adobe Experience Manager Assets] user interface that is available exclusively to you. You can share this private folder to other users and assign various privileges to them. Based on the privilege level you assign, users can perform various tasks on the folder, for example, view assets within the folder or edit the assets.

>[!NOTE]
>
>Private folder has at least one member with Owner role.
>
>To create a private folder, you require `Read` and `Modify` permissions on the parent folder under which you create a private folder. If you are not an administrator, these permissions are not enabled by default on `/content/dam`. In this case, first obtain these permissions for your user ID/group before attempting to create private folders.

## Create and share private folder  {#create-share-private-folder}

To create and share a private folder:

1. In the [!DNL Assets] console, click the **[!UICONTROL Create]** button from the toolbar and then select **[!UICONTROL Folder]** from the menu.

   ![Create assets folder](assets/create-folder.png)

1. In the **[!UICONTROL Create Folder]** dialog, enter a `Title` and `Name` (optional) for the folder. 

   Select the **[!UICONTROL Private]** check box and click **[!UICONTROL Create]**. 

   ![chlimage_1-413](assets/create-private-folder.png)

   A private folder is created. You can now [add assets](add-assets.md#upload-assets) to the folder and share the folder with other users or groups. The folder is not visible to any other user until you share it and assign privileges to them. 

1. To share the folder, select the folder, and click **[!UICONTROL Properties]** from the toolbar.

1. In the **[!UICONTROL Folder Properties]** page, select a user or group from the **[!UICONTROL Add User]** list, assign a role (`Viewer`, `Editor`, or `Owner`) on your private folder, and click **[!UICONTROL Add]**. 

   ![assign-user-group](assets/assign-permissions-private-folder.png)

   You can assign various roles, such as `Editor`, `Owner`, or `Viewer` to the user with whom you share the folder. If you assign an `Owner` role to the user, the user has `Editor` privileges on the folder. In addition, the user can share the folder with others. If you assign an `Editor` role, the user can edit the assets in your private folder. If you assign a viewer role, the user can only view the assets in your private folder.

   >[!NOTE]
   >
   >Private folder has at least one member with `Owner` role. Therefore, the administrator cannot remove all the owner members from a private folder. However, to remove the existing owners (and administrator itself) from the private folder the administrator must add another user as owner.

1. Click **[!UICONTROL Save & Close]**. Depending on the role you assign, the user is assigned a set of privileges on your private folder when the user logs in to [!DNL Assets].
1. Click **[!UICONTROL Ok]** to close the confirmation message.
1. The user with whom you share the folder receives a sharing notification in their user interface. 

1. Click [!UICONTROL Notifications] to open a list of notifications.

   ![notification](assets/notification-icon.png)

1. Click the entry for the private folder shared by the administrator to open the folder.

## Private folder deletion {#delete-private-folder}

You can delete a folder by selecting the folder and selecting [!UICONTROL Delete] option from the top menu, or by using Backspace key on your keyboard.

![delete option in top menu](assets/delete-option.png)

>[!CAUTION]
>
>If you delete a private folder from CRXDE Lite, then redundant user groups are left in the repository.

>[!NOTE]
>
>If you delete a folder using the above method from the user interface, then the associated user groups are also deleted.
>
>However, the existing redundant, unused, and auto-generated user groups can be removed from the repository using `clean` method in JMX in the author instance (`http://[server]:[port]/system/console/jmx/com.day.cq.dam.core.impl.team%3Atype%3DClean+redundant+groups+for+Assets`).

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
* [Manage collections](manage-collections.md)
* [Bulk metadata import](metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
