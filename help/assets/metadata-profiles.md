---
title: Metadata profiles
description: Know about metadata profiles for assets. Learn how to create a metadata profile and apply it to folder assets.
contentOwner: AG

---

# Metadata profiles {#metadata-profiles}

A Metadata Profile lets you apply default metadata to assets within a folder. Create a Metadata Profile and apply it to a folder. Any asset that you subsequently upload to the folder inherits the default metadata that you configured in the Metadata Profile.

<!-- See [Profiles for Processing Metadata, Images, and Videos](processing-profiles.md).

See also [Best Practices for Organizing your Digital Assets for using Processing Profiles](/help/assets/best-practices-for-file-management.md).

-->

## Add a metadata profile {#adding-a-metadata-profile}

1. Tap the AEM logo and navigate to **[!UICONTROL Tools > Assets > Metadata Profiles]**, and then tap  **[!UICONTROL Create]**.
1. Enter a title for the Metadata Profile, for example Sample Metadata, and tap **[!UICONTROL Submit]**. The Edit Form for the Metadata Profile is displayed.
1. Click a component and configure its properties in the **[!UICONTROL Settings]** tab. For example, click the **[!UICONTROL Description]** component and edit its properties.
   Edit the following properties for the **[!UICONTROL Description]** component:

    * **[!UICONTROL Field Label]** &ndash; The display name of the metadata property. It is only for the user reference.
    * **[!UICONTROL Map to Property]** &ndash; The value of this property provides the relative path/name to the asset node where it is saved in the repository. The value should always start with `./` because it indicates that the path is under the asset's node.

       The value you specify for **[!UICONTROL Map to property]** is stored as a property under the asset's metadata node. For example, if you specify . `/jcr:content/metadata/dc:desc` as the name of **[!UICONTROL Map to property]**, AEM Assets stores the value `dc:desc` at the asset's metadata node.

    * **[!UICONTROL Default Value]** &ndash; Use this property to add a default value for the metadata component. For example, if you specify "My description" then this value is assigned to the property `dc:desc` at the asset's metadata node.

      >[!NOTE]
      >
      >Adding a default value to a new metadata property (which doesn't exist already at the . `/jcr:content/metadata` node) does not display the property and its value on the asset's Properties page by default. To view the new property on the assets's Properties page, modify the corresponding schema form.

1. (Optional) Add more components to the Edit Form from the **[!UICONTROL Build Form]** tab, and configure their properties in the **[!UICONTROL Settings]** tab. The following properties are available from the **[!UICONTROL Build Form]** tab:

| Component | Properties |
|------------------|----------------------------------------------------|
| Section Header | Field Label, Description |
| Single Line Text | Field Label, Map to property, Default Value |
| Multi Value Text | Field Label, Map to property, Default Value |
| Number | Field Label, Map to property, Default Value |
| Date | Field Label, Map to property, Default Value |
| Standard Tags | Field Label, Map to property, Default Value, Description |

1. Tap **[!UICONTROL Done]**. The Metadata Profile is added to the list of profiles in the **[!UICONTROL Metadata Profiles]** page.

## Copy a metadata profile {#copying-a-metadata-profile}

1. From the **[!UICONTROL Metadata Profiles]** page, select a Metadata Profile to make a copy of it.
1. Tap **[!UICONTROL Copy]** from the toolbar.
1. In the **[!UICONTROL Copy Metadata Profile]** dialog, enter a title for the new copy of the Metadata Profile.
1. Tap **[!UICONTROL Copy]**. The copy of the Metadata Profile appears in the list of profiles in the **[!UICONTROL Metadata Profiles]** page.

## Delete a metadata profile {#deleting-a-metadata-profile}

1. From the **[!UICONTROL Metadata Profiles]** page, select a profile to delete.
1. Tap **[!UICONTROL Delete Metadata Profiles]** in the toolbar.
1. In the dialog, click **[!UICONTROL Delete]** to confirm the delete operation. The metadata profile is deleted from the list.

## Apply a metadata profile to folders {#applying-a-metadata-profile-to-folders}

When you assign a metadata profile to a folder, any subfolders automatically inherit the profile from its parent folder. This means that you can assign only one metadata profile to a folder. As such, consider carefully the folder structure of where you upload, store, use, and archive assets.

If you assigned a different metadata profile to a folder, the new profile overrides the previous profile. The previously existing folder assets remain unchanged. The new profile is applied on the assets that are added to the folder later.

Folders that have a profile assigned to it are indicated in the user interface by the name of the profile appearing in the card name.

You can apply metadata profiles to specific folders or globally to all assets.

You can reprocess assets in a folder that already has an existing metadata profile that you later changed. <!-- See [Reprocessing assets in a folder after you have edited its processing profile](processing-profiles.md#reprocessing-assets-in-a-folder-after-you-have-edited-its-processing-profile). -->

### Apply metadata profiles to specific folders {#applying-metadata-profiles-to-specific-folders}

You can apply a metadata profile to a folder from within the **[!UICONTROL Tools]** menu or if you are in the folder, from **[!UICONTROL Properties]**. This section describes how to apply metadata profiles to folders both ways.

Folders that have a profile already assigned to it are indicated by the display of the profile's name directly below the folder name.

You can reprocess assets in a folder that already has an existing video profile that you later changed. <!--See [Reprocessing assets in a folder after you have edited its processing profile](processing-profiles.md#reprocessing-assets-in-a-folder-after-you-have-edited-its-processing-profile). -->

#### Apply metadata profiles to folders from Profiles user interface {#applying-metadata-profiles-to-folders-from-profiles-user-interface}

1. Tap the AEM logo and navigate to **[!UICONTROL Tools > Assets > Metadata Profiles]**.
1. Select the metadata profile that you want to apply to a folder or multiple folders.
1. Tap **[!UICONTROL Apply Metadata Profile to Folder(s)]** and select the folder or multiple folders you want use to receive the newly uploaded assets and tap **[!UICONTROL Done]**. Folders that have a profile already assigned to it are indicated by the display of the profile's name directly below the folder name.

#### Apply metadata profiles to folders from Properties {#applying-metadata-profiles-to-folders-from-properties}

1. In the left rail, tap **[!UICONTROL Assets]** then navigate to the folder that you want to apply a metadata profile to.
1. On the folder, tap or click the check mark to select it and then tap or click **Properties**.  
1. Select the **[!UICONTROL Metadata Profiles]** tab and select the profile from the drop-down menu and tap **Save]**. Folders that have a profile already assigned to it are indicated by the display of the profile's name directly below the folder name.

### Apply a metadata profile globally {#applying-a-metadata-profile-globally}

In addition to applying a profile to a folder, you can also apply one globally so that any content uploaded into AEM assets in any folder has the selected profile applied.

You can reprocess assets in a folder that already has an existing metadata profile that you later changed. <!--See [Reprocessing assets in a folder after you have edited its processing profile](processing-profiles.md#reprocessing-assets-in-a-folder-after-you-have-edited-its-processing-profile). -->

**To apply a metadata profile globally, do one of the following**

* Navigate to `https://<AEM server>/mnt/overlay/dam/gui/content/assets/foldersharewizard.html/content/dam` and apply the appropriate profile and tap **Save**.

* Navigate to CRXDE Lite to the following node: `/content/dam/jcr:content`. Add the property `metadataProfile:/etc/dam/metadata/dynamicmedia/<name of metadata profile>` and tap **Save All**.

## Removing a metadata profile from folders {#removing-a-metadata-profile-from-folders}

When you remove a metadata profile from a folder, any subfolders automatically inherit the removal of the profile from its parent folder. However, any processing of files that has occurred within the folders remains intact.

You can remove a metadata profile from a folder from within the **Tools** menu or if you are in the folder, from the **Properties**. This section describes how to remove metadata profiles from folders both ways.

### Removing metadata profiles from folders via Profiles user interface {#removing-metadata-profiles-from-folders-via-profiles-user-interface}

1. Tap or click the AEM logo and navigate to **[!UICONTROL Tools > Assets > Metadata Profiles]**.
1. Select the metadata profile that you want to remove from a folder or multiple folders.
1. Tap **[!UICONTROL Remove Metadata Profile from Folder(s)]** and select the folder or multiple folders you want use to remove a profile from and tap **[!UICONTROL Done]**.

   You can confirm that the metadata profile is no longer applied to a folder because the name no longer appears below the folder name.

### Removing metadata profiles from folders via Properties {#removing-metadata-profiles-from-folders-via-properties}

1. Tap the AEM logo and navigate **[!UICONTROL Assets]** and then to the folder that you want to remove an metadata profile from.
1. On the folder, tap the check mark to select it and then tap **[!UICONTROL Properties]**.
1. Select the **[!UICONTROL Metadata Profiles]** tab and select **[!UICONTROL None]** from the drop-down menu and click **[!UICONTROL Save]**. Folders that have a profile already assigned to it are indicated by the display of the profile's name directly below the folder name.
