---
title: Metadata profiles
description: Know about metadata profiles for assets. Learn how to create a metadata profile and apply it to folder assets.
contentOwner: AG
feature: Metadata
role: User, Admin
exl-id: eef90c6a-b354-4342-8b97-21d067ae2979
---
# Metadata profiles {#metadata-profiles}

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
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/metadata-config.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

A Metadata Profile lets you apply default metadata to assets within a folder. Create a Metadata Profile and apply it to a folder. Any asset that you subsequently upload to the folder inherits the default metadata that you configured in the Metadata Profile.

An important concept regarding the use of profiles in Experience Manager Assets is that they are assigned to folders. Within a profile are settings in the form of metadata profiles, along with video profiles or image profiles. These settings process the contents of a folder along with any of its subfolders. Therefore, how you name files and folders, how you arrange subfolders, and how you handle the files within these folders has a significant impact on how those assets are processed by a profile.
By using consistent and appropriate file and folder naming strategies, and good metadata practice, you make the most of your digital asset collection, and ensure that the right files are processed by the right profile.

## Add a metadata profile {#adding-a-metadata-profile}

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Profiles]**, and then click **[!UICONTROL Create]**.
1. Enter a title for the Metadata Profile, for example, Sample Metadata, and select **[!UICONTROL Submit]**. The Edit Form for the Metadata Profile is displayed.
1. Click a component and configure its properties in the **[!UICONTROL Settings]** tab. For example, click the **[!UICONTROL Description]** component and edit its properties.
   Edit the following properties for the **[!UICONTROL Description]** component:

    * **[!UICONTROL Field Label]** &ndash; The display name of the metadata property. It is only for the user reference.
    * **[!UICONTROL Map to Property]** &ndash; The value of this property provides the relative path/name to the asset node where it is saved in the repository. The value should always start with `./` because it indicates that the path is under the asset's node.

       The value you specify for **[!UICONTROL Map to property]** is stored as a property under the asset's metadata node. For example, if you specify . `/jcr:content/metadata/dc:desc` as the name of **[!UICONTROL Map to property]**, [!DNL Adobe Experience Manager Assets] stores the value `dc:desc` at the asset's metadata node.

    * **[!UICONTROL Default Value]** &ndash; Use this property to add a default value for the metadata component. For example, if you specify "My description" then this value is assigned to the property `dc:desc` at the asset's metadata node.

      >[!NOTE]
      >
      >Adding a default value to a new metadata property (which does not exist at `/jcr:content/metadata` node) does not display the property and its value on the asset's Properties page by default. To view the new property on the [!UICONTROL Properties] page, modify the corresponding schema form.

1. (Optional) Add more components to the Edit Form from the **[!UICONTROL Build Form]** tab, and configure their properties in the **[!UICONTROL Settings]** tab. The following properties are available from the **[!UICONTROL Build Form]** tab:

| Component | Properties |
|------------------|----------------------------------------------------|
| Section Header | Field Label, Description |
| Single Line Text | Field Label, Map to property, Default Value |
| Multi Value Text | Field Label, Map to property, Default Value |
| Number | Field Label, Map to property, Default Value |
| Date | Field Label, Map to property, Default Value |
| Standard Tags | Field Label, Map to property, Default Value, Description |

1. Click **[!UICONTROL Done]**. The Metadata Profile is added to the list of profiles in the **[!UICONTROL Metadata Profiles]** page.

## Copy a metadata profile {#copying-a-metadata-profile}

1. From the **[!UICONTROL Metadata Profiles]** page, select a Metadata Profile to make a copy of it.
1. Click **[!UICONTROL Copy]** from the toolbar.
1. In the **[!UICONTROL Copy Metadata Profile]** dialog, enter a title for the new copy of the Metadata Profile.
1. Click **[!UICONTROL Copy]**. The copy of the Metadata Profile appears in the list of profiles in the **[!UICONTROL Metadata Profiles]** page.

## Delete a metadata profile {#deleting-a-metadata-profile}

1. From the **[!UICONTROL Metadata Profiles]** page, select a profile to delete.
1. Click **[!UICONTROL Delete Metadata Profiles]** in the toolbar.
1. In the dialog, click **[!UICONTROL Delete]** to confirm the delete operation. The metadata profile is deleted from the list.

## Apply a metadata profile to folders {#applying-a-metadata-profile-to-folders}

When you assign a metadata profile to a folder, any subfolders automatically inherit the profile from its parent folder. The inheritance stops when a different profile is applied to a subfolder. You can assign only one metadata profile to a folder. Hence, carefully consider the folder structure where you upload, store, use, and archive assets. 

If you assigned a different metadata profile to a folder, the new profile overrides the previous profile. The previously existing folder assets remain unchanged. The new profile is applied on the assets that are added to the folder after the change. You can apply metadata profiles to specific folders or globally to all assets.

Folders that have a profile assigned to it are indicated in the user interface by the name of the profile appearing in the card name.

You can reprocess assets in a folder that already has an existing metadata profile that you later changed. <!-- See [Reprocessing assets in a folder after you have edited its processing profile](processing-profiles.md#reprocessing-assets-in-a-folder-after-you-have-edited-its-processing-profile). -->

### Apply metadata profiles to specific folders {#applying-metadata-profiles-to-specific-folders}

You can apply a metadata profile to a folder from within the **[!UICONTROL Tools]** menu or if you are in the folder, from **[!UICONTROL Properties]**. This section describes how to apply metadata profiles to folders both ways.

Folders that have a profile already assigned to it are indicated by the display of the profile's name directly below the folder name.

You can reprocess assets in a folder that already has an existing video profile that you later changed. <!--See [Reprocessing assets in a folder after you have edited its processing profile](processing-profiles.md#reprocessing-assets-in-a-folder-after-you-have-edited-its-processing-profile). -->

#### Apply metadata profiles to folders from Profiles user interface {#applying-metadata-profiles-to-folders-from-profiles-user-interface}

1. Navigate to **[!UICONTROL Tools > Assets > Metadata Profiles]**.
1. Select the metadata profile that you want to apply to a folder or multiple folders.
1. Click **[!UICONTROL Apply Metadata Profile to Folders]** and select the folder or multiple folders you want use to receive the newly uploaded assets and Click **[!UICONTROL Done]**. Folders that have a profile already assigned to it are indicated by the display of the profile's name directly below the folder name.

#### Apply metadata profiles to folders from Properties {#applying-metadata-profiles-to-folders-from-properties}

1. In the left rail, Click **[!UICONTROL Assets]** then navigate to the folder that you want to apply a metadata profile to.
1. On the folder, select the check mark to select it and then select **Properties**.  
1. Select the **[!UICONTROL Metadata Profiles]** tab and select the profile from the drop-down menu and Click **[!UICONTROL Save]**. Folders that have a profile already assigned to it are indicated by the display of the profile's name directly below the folder name.

### Apply a metadata profile globally {#applying-a-metadata-profile-globally}

In addition to applying a profile to a folder, you can also apply one globally so that any content uploaded into [!DNL Experience Manager Assets] in any folder has the selected profile applied.

You can reprocess assets in a folder that already has an existing metadata profile that you later changed. <!--See [Reprocessing assets in a folder after you have edited its processing profile](processing-profiles.md#reprocessing-assets-in-a-folder-after-you-have-edited-its-processing-profile). -->

**To apply a metadata profile globally, do one of the following**

* Navigate to `https://[aem_server]/mnt/overlay/dam/gui/content/assets/v2/foldersharewizard.html/content/dam` and apply the appropriate profile and click **[!UICONTROL Save]**.

* Navigate to CRXDE Lite to the following node: `/content/dam/jcr:content`. Add the property `metadataProfile:/etc/dam/metadata/dynamicmedia/<name of metadata profile>`. Click **Save All**.

## Removing a metadata profile from folders {#removing-a-metadata-profile-from-folders}

When you remove a metadata profile from a folder, any subfolders automatically inherit the removal of the profile from its parent folder. However, any processing of files that has occurred within the folders remains intact.

You can remove a metadata profile from a folder from within the **Tools** menu or if you are in the folder, from the **Properties**. This section describes how to remove metadata profiles from folders both ways.

### Removing metadata profiles from folders via Profiles user interface {#removing-metadata-profiles-from-folders-via-profiles-user-interface}

1. Click the Experience Manager logo and navigate to **[!UICONTROL Tools > Assets > Metadata Profiles]**.
1. Select the metadata profile that you want to remove from a folder or multiple folders.
1. Click **[!UICONTROL Remove Metadata Profile from Folders]** and select the folder or multiple folders you want use to remove a profile from and click **[!UICONTROL Done]**.

   You can confirm that the metadata profile is no longer applied to a folder because the name no longer appears below the folder name.

### Removing metadata profiles from folders via Properties {#removing-metadata-profiles-from-folders-via-properties}

1. Click the Experience Manager logo and navigate **[!UICONTROL Assets]** and then to the folder that you want to remove an metadata profile from.
1. On the folder, click the check mark to select it and then click **[!UICONTROL Properties]**.
1. Select the **[!UICONTROL Metadata Profiles]** tab and select **[!UICONTROL None]** from the drop-down menu and click **[!UICONTROL Save]**. Folders that have a profile already assigned to it are indicated by the display of the profile's name directly below the folder name.

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
