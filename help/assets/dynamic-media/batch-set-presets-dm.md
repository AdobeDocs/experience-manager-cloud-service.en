---
title: Batch Set Presets
description: Learn how to automate image set and spin set creation using batch set presets in Dynamic Media.
contentOwner: Rick Brough
feature: Image Presets,Viewer Presets
role: User
exl-id: 022ee347-54ec-4cec-b808-9eb3a9e51424
---
# About Batch Set Presets {#about-bsp}

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

Use **[!UICONTROL Batch Set Presets]** to create and organize multiple assets in an image set or spin set at the time you upload asset files to a folder either individually or using bulk ingestion. You can have the preset run alongside the asset import jobs you schedule in [!DNL Dynamic Media]. Each preset is a uniquely named, self-contained set of instructions that defines how to construct the image set or spin set using images that match the defined naming conventions in the preset recipe.

>[!IMPORTANT]
>
>Are you using batch set presets in [!DNL Dynamic Media Classic], and migrating from [!DNL Dynamic Media Classic] to Adobe Experience Manager as a Cloud Service? If so, you must manually re-create your batch set presets definitions within [!DNL Adobe Experience Manager as a Cloud Service].

**Best Practice** - When working with batch set presets Adobe recommends the following workflow:

1. Create a batch set preset. See [Create a batch set preset for an image set or a spin set](#creating-bsp).
1. Create an asset folder or use an existing asset folder and ensure it is synced to [!DNL Dynamic Media]. See [Create folders](/help/assets/manage-digital-assets.md#creating-folders).
1. Apply the batch set preset to the asset folder. See [About applying batch set presets to folders](#apply-bsp).
1. Upload images to the asset folder. See [Upload assets for Image Sets](/help/assets/dynamic-media/image-sets.md#uploading-assets-in-image-sets), [Upload assets for Spin Sets](/help/assets/dynamic-media/spin-sets.md#uploading-assets-for-spin-sets), or [Add digital assets to Adobe Experience Manager](/help/assets/add-assets.md#add-assets-to-experience-manager).
1. Image set or spin set gets auto generated in the desired folder.
1. Publish your image set or spin set. See [Publish Dynamic Media Assets](/help/assets/dynamic-media/publishing-dynamicmedia-assets.md). 

## Create a batch set preset for an image set or a spin set {#creating-bsp}

To create Batch Set Presets, it is desirable that you have some familiarity and understanding of regular expressions.

Ideally, your company has already defined a naming convention for how assets are grouped in a set.
To help you understand the importance of using a naming convention, suppose your company's defined naming convention is `<style>-<color>-<view>`. And, the base name for the set must always be `<style>-<color>`, and the set name extension be `-SET`. If you upload an image named `0123-RED-01`, then a set would be created named `0123-RED-SET`. If you later upload images `0123-RED-03` and `0123-BLUE-01`, then the `RED-03` image would be added to the set in the second position because it is sorted lower than `01`. However, the `BLUE-01` image would be part of a new set named `0123-BLUE-SET`. For the next asset upload, you add files `0123-RED-02` and `0123-BLUE-02`. Each asset would be added to its respective set. The `RED-02` image would be automatically sorted between the existing `01` and `03` images, because of the sort order.

The **[!UICONTROL Batch Set Preset]** page in [!DNL Dynamic Media] lets you create, edit, or delete batch set presets, and apply or remove batch set presets to or from asset folders. You can use either the form field drop-down lists to define a batch set preset or use the **[!UICONTROL Raw Code]** field, which lets you type regular expression syntax.

You can create many batch set presets so you cover all asset ingest jobs you require.

### About Asset Naming Convention

The **[!UICONTROL Asset Naming Convention]** area on the **[!UICONTROL Batch Set Preset]** page has two elements that you can use to define your batch set preset: **[!UICONTROL Match]** and **[!UICONTROL Base Name]**. These elements let you define a naming convention and identify the part of the convention used to name the set in which they are contained. <!-- While **[!UICONTROL Match]** is required, **[!UICONTROL Base Name]** is mandatory only if the **[!UICONTROL Match]** field does not already specify a base name through the use of a bracket grouping. -->

A company's individual naming convention often uses one or more lines of definition from each of these two elements. You can use as many lines for your unique definition and group them into distinct elements, such as for Main Image, Color element, Alternate View element, and Swatch element.
 
For example, the syntax for a literal match regular expression could look like the following:

`(\w+)-\w+-\w+`

### About Sequence Ordering

You can optionally define the order in which images are displayed after the image set or spin set is grouped in [!DNL Dynamic Media]. By default, your assets are ordered alphanumerically. However, you can use a comma-separated list of regular expressions to define the order.

Regarding sequence ordering automation, you specify rules to force-sort assets in a certain way, if necessary. For example, suppose your first asset is always named `_main` and you want it followed with `_alt1`, `_alt2`, `_alt3`, and so on. In such cases, you can create a sequence ordering rule with the following syntax:

`.*_main,.*_alt[0-9]`

While a force-sort sequence is possible, it is best to rely on alphanumeric numbering for sequence ordering, as much as possible. Furthermore, you can use the image set or spin set editor tools in [!DNL Dynamic Media] to rearrange the sequence order of assets, or add and delete new assets in the set by using a drag-and-drop operation.

When you finish creating a batch set preset, you apply it to one or more folders that you have created. See [About applying batch set presets to folders](#apply-bsp).

<!-- See also [Creating a batch set preset for the auto generation of a 2D Spin Set](application-setup.md#creating_a_batch_set_preset_for_the_auto_generation_of_a_2d_spin_set). -->

**To create a batch set preset for an image set or a spin set:**

1. Select the Experience Manager logo and go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets]**.

   ![bsp-create1.png](/help/assets/assets-dm/bsp-create1.png)

1. On the **[!UICONTROL Batch Set Presets]** page, near the upper-right corner, select **[!UICONTROL Create]**.
1. In the **[!UICONTROL Create Batch Set Preset]** dialog box, in the **[!UICONTROL Preset Name]** text field, enter a descriptive name. The preset name is not editable if you later decide to change it.

1. In the **[!UICONTROL Preset Type]** drop-down list, select **[!UICONTROL ImageSet]** or **[!UICONTROL SpinSet]**. Be sure you choose the correct preset type; it is not editable later.
1. Select **[!UICONTROL Create]**.
1. On the right of the **[!UICONTROL Edit Batch Set Preset]** page, set the editable options you want under the **[!UICONTROL Preset Details]** and **[!UICONTROL Set Naming Convention]** headings.
   To learn more about the editable options that are available to you, see [Preset Details, Set Naming Convention, and Rule Results - RegX options](#features-options-bsp).

   ![bsp-create4.png](/help/assets/assets-dm/bsp-create4.png)

1. Create one or more regular expression groups. 

   * On the left of the **[!UICONTROL Edit Batch Set Preset]** page, under **[!UICONTROL Match]**, **[!UICONTROL Base Name]**, or **[!UICONTROL Sequence Ordering]**, select **[!UICONTROL Add Group]**.
   * The **[!UICONTROL Match]** field is required. **[!UICONTROL Base Name]** is mandatory only if the **[!UICONTROL Match]** field does not already specify a base name by using a bracket grouping. **[!UICONTROL Sequence Ordering]** is optional.
   * Using the drop-down lists and text boxes in the group's form, specify an expression group that you want to use to define the naming criteria for image set or spin set asset members.
      * As you select and specify expressions for a group, notice that the actual regular expression syntax is reflected near the lower right of the page, under the **[!UICONTROL Rule Results - RegX]** heading. To see the regular expression string updated in the lower right, select anywhere outside the form area. These regular expression strings represent the pattern that you want to match in a search of [!DNL Dynamic Media] assets to create your image set or spin set.
      * If you have added a group and want to remove it, select **[!UICONTROL X]**.
   * When you add two or more groups, in the **[!UICONTROL And]** drop-down list, select **[!UICONTROL And]** to conjoin a newly added group with any previous expression group you have added. Or, select **[!UICONTROL Or]** to add an alternation between the previous expression group and the new group you create. The **[!UICONTROL Or]** operand is defined by the use of a vertical line character `|` in the regular expression syntax itself.

1. Do one of the following:

   * To add another new group, under **[!UICONTROL Match]**, **[!UICONTROL Base Name]**, or **[!UICONTROL Sequencing Order]**, select **[!UICONTROL Add Group]**. Create another regular expression group as you did in the previous step.
   * Review the regular expression syntax in the **[!UICONTROL Rule Results - RegX]** area. If you must change the syntax, make your edits in the respective group on the left of the page.
   * If you have finished creating expression groups, continue to the next step.

1. In the upper-right corner of the page, select **[!UICONTROL Save]**.

You are now ready to apply the batch set preset to an asset folder. Then, you upload assets to that folder. This workflow results in the auto generation of your image set or spin set. See [About applying batch set presets to asset folders](#apply-bsp).

### Preset Details, Set Naming Convention, and Rule Results - RegX options {#features-options-bsp}

These options are available on the **[!UICONTROL Edit Batch Set Preset]** page when you create or edit a batch set preset.

See [Create a batch set preset for an image set or a spin set](#creating-bsp) or [Edit a batch set preset](#edit-bsp).

   | **[!UICONTROL Preset Details]**  | Description |
   | --- | --- |
   | Preset Name | Read-only. The name you specified when you first created the batch set. If you must rename the preset, you can copy the existing batch set preset and specify a new name. See [Copy an existing batch set preset](#copy-bsp). |
   | Type | Read-only. The type was specified when you first created the batch set. Copying an existing batch set preset does not let you change its [!UICONTROL Type]; you must create a preset instead. |
   | Include Derived Assets | Optional. To have [!DNL Dynamic Media]'s IPS (Image Production System) include generated or "derived" images with your Spin Set or Image Set, select **[!UICONTROL Yes]** (default). A derived asset is an image that was not directly uploaded by a user. Instead, the asset was produced by IPS when a master asset was uploaded. For example, an image asset that IPS generated from a page in a PDF, at the time the PDF was uploaded in [!DNL Dynamic Media], is considered a derived asset. |
   | Destination Folder | Optional. If you define large numbers of image sets or spin sets, Adobe recommends you keep these sets separate from the folders that contain the assets themselves. As such, consider creating an Image Sets or Spin Sets folder and redirect the application to place batch set generated sets here.<br>In such case, specify which folder within the Experience Manager Assets folder structure (`/content/dam`) has the batch set preset active. Be sure that the folder is enabled for [!DNL Dynamic Media] synchronization to allow it as a destination folder. See [Configure selective publishing at the folder level in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md#selective-publish-configure-folder).<br>More than one folder can have a given batch set preset assigned to it, if you apply the preset by way of the folder's **[!UICONTROL Properties]**. See [Apply batch set presets from an asset folder's Properties page](#apply-bsp-to-folders-via-properties).<br>If you do not specify a folder, the batch set preset generated image set or spin set is created in the same folder as the asset folder you uploaded to. |
   | **[!UICONTROL Set Naming Convention]** |  |
   | Prefix<br>or<br>Suffix | Optional. Enter either a prefix, suffix, or both in the respective fields.<br>The prefix and suffix fields let you create many batch set presets using an alternate, custom file naming convention for a particular set of content. This method is especially useful in cases where there is an exception to a company's defined default naming scheme.<br>The prefix or suffix is added to the **[!UICONTROL Base Name]** you define in the **[!UICONTROL Asset Naming Convention]** area. By adding a prefix or suffix, you ensure that your image set or spin set gets created exclusively and independently from other assets. It can also serve to further help others identify file types. For example, to determine a color mode used, you could add as a prefix or suffix `rgb` or `cmyk`.<br>While specifying a set naming convention is not required to use batch set preset functionality, best practice recommends that you use the set naming convention. This practice lets you define as many elements of your naming convention that you want grouped in a set to help streamline batch set creation. |
   | **[!UICONTROL Rule Results - RegX]** |  |
   | Asset Naming Convention - Match | Read-only. Displays the regular expression syntax based on the Match form options you chose or the raw code you entered. |
   | Asset Naming Convention - Base Name | Read-only. Displays the regular expression syntax based on the Base Name form options you chose or the raw code you entered. |
   | Sequence Ordering - Match | Read-only. Displays the regular expression syntax based on the form options you chose or the raw code you entered. |

## About applying batch set presets to asset folders {#apply-bsp}

When you assign batch set presets to one or more asset folders, any subfolders automatically inherit the presets from its parent folder.

You can apply multiple batch set presets to an asset folder.

Folders that have a batch preset assigned to it are indicated in the user interface with the name of the preset appearing in the folder, in the **[!UICONTROL Card]** view.

To apply batch set presets to asset folders, use either one of the following two methods:

* [Apply batch set presets to asset folders from the Batch Set Preset page](#apply-bsp-to-folders-via-bsp-page) - This method offers you the most flexibility. You can apply a single preset or multiple presets to a single folder or multiple folders.
* [Apply batch set presets from an asset folder's Properties page](#apply-bsp-to-folders-via-properties) - This method lets you apply one or more batch set presets to a single folder.

As a best practice, make sure that the asset folders are synced [!DNL Dynamic Media], then apply the presets you want.

Reprocess assets in a folder if you experience either of the following two scenarios:

* You want to run a batch set preset on an existing asset folder that already has assets uploaded to it.
* You later edit an existing batch set preset that was previously applied to a folder of assets.

<!-- See [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets). -->

### Apply batch set presets to asset folders from the Batch Set Preset page {#apply-bsp-to-folders-via-bsp-page}

1. Select the Experience Manager logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets]**.
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, select the check box of each batch set preset that you want to apply to folders.
1. In the toolbar, select **[!UICONTROL Apply Batch Preset to Folders]**.
1. On the **[!UICONTROL Select Folders]** page, select the check box of each folder that you want the batch set presets applied to.
1. In the upper-right corner of the **[!UICONTROL Select Folders]** page, select **[!UICONTROL Apply]**.

### Apply batch set presets from an asset folder's Properties page {#apply-bsp-to-folders-via-properties}

1. Select the Experience Manager logo and go to **[!UICONTROL Assets]** > **[!UICONTROL Files]**.
1. Navigate to a folder in which you want to apply one or more batch set presets.
1. On the page, to the left of the **[!UICONTROL Name]** column, select the check box of a folder.
1. In the toolbar, select **[!UICONTROL Properties]**.
1. On the folder's Properties page, select the **[!UICONTROL Dynamic Media Processing]** tab.

   ![bsp-apply-via-properties2.png](/help/assets/assets-dm/bsp-apply-via-properties2a.png)

1. Under **[!UICONTROL Batch Set Presets]**, from the **[!UICONTROL Preset Name]** drop-down list box, select the name of a batch set preset you want to apply. The screenshot above shows two selected batch set presets that are applied to the asset folder.

   If no batch set preset names exist in the **[!UICONTROL Preset Name]** drop-down list box, it means you have not yet created any batch set presets. See [Create a batch set preset for an image set or a spin set](#creating-bsp).

   To remove an applied batch set preset, select **[!UICONTROL X]** to the right of the preset type.

1. In the upper-right corner of the page, select **[!UICONTROL Save & Close]**.

## Edit a batch set preset {#edit-bsp}

You can edit an existing batch set preset that you have created. You can change any of the expression groups you created for the asset naming convention or sequence order. If needed, you can also update the destination folder and set naming conventions.

You cannot, however, change the preset's name or preset type (Image Set or Spin Set). If it becomes necessary to change a preset's name, copy the existing preset and specify a new name. See [Copy a batch set preset](#copy-bsp).

If you edit a batch set preset that was previously applied to a folder, the newly edited batch set preset gets applied only to new assets uploaded to that folder.

If you want the newly edited preset to be reapplied to the existing assets in the folder, you must reprocess the folder. <!-- See [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets). -->In this way, the existing assets would now qualify to be part of an image set or spin set and be added. Furthermore, the existing assets that were already included in the image set or spin set - based on the previous batch set preset that was used - do not get removed and show as-is. This scenario assumes they no longer qualify based on the newly edited preset.

**To edit a batch set preset:**

1. Select the Experience Manager logo and go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets]**.
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, check the batch set preset that you want to change.
1. In the toolbar, select **[!UICONTROL Edit Batch Set Preset]**.
1. Edit the preset as necessary.
1. In the upper-right corner of the **[!UICONTROL Batch Set Preset]** page, select **[!UICONTROL Save]**.

## Copy an existing batch set preset {#copy-bsp}

You can copy an existing batch set preset to avoid having to manually re-create a complex preset, or if you simply want to rename a preset. You cannot, however, change the preset type used (Image Set or Spin Set).

If you copy an existing preset that is reference by asset folders, those folders are not affected.

**Copy an existing batch set preset:**

1. Select the Experience Manager logo and go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets]**.
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, select the check box of the batch set preset that you want to copy.
1. In the toolbar, select **[!UICONTROL Copy]**.
1. In the **[!UICONTROL Copy Batch Set Preset]** dialog box, in the **[!UICONTROL Title]** text box, type a new name for the preset.

   ![bsp-copy2.png](/help/assets/assets-dm/bsp-copy2.png)

1. Select **[!UICONTROL Copy]**.

## About removing batch set presets from folders {#remove-bsp-from-folder}

When you remove batch set presets from folders, any new assets that you upload to these folders do not have the batch set preset applied to them. Existing assets in the folder that were already added to the image set or spint set&ndash;based on batch set preset that was applied to the folder&ndash;continue to show as-is.

If you want to *delete* presets from folders instead, see [Delete batch set presets](#delete-bsp).

There are two methods you can use to remove batch set presets from folders.

* [Remove batch set presets from folders by way of the Batch Set Preset page](#remove-bsp-from-folders-via-bsp-page) - This method offers you the most flexibility. You can remove a single preset or multiple presets from a single folder or multiple folders.
* [Remove batch set presets from a folder's Properties page](#remove-bsp-from-folders-via-properties) - This method lets you remove one or more batch set presets from a single folder only.

### Remove batch set presets from folders by way of the Batch Set Preset page {#remove-bsp-from-folders-via-bsp-page}

1. Select the Experience Manager logo and go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets]**.
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, select the check box of one or more batch set presets that you want to remove from one or more folders.
1. In the toolbar, select **[!UICONTROL Remove Batch Preset from Folders]**.

1. On the **[!UICONTROL Select Folders]** page, select one or more folders in which you want the batch set presets removed.
1. In the upper-right corner of the **[!UICONTROL Select Folders]** page, select **[!UICONTROL Remove]**.

   ![bsp-remove-from-folders3.png](/help/assets/assets-dm/bsp-remove-from-folders3.png)

1. In the **[!UICONTROL Remove profile]** dialog box, select **[!UICONTROL Remove]**.

### Remove batch set presets from a folder's Properties page {#remove-bsp-from-folders-via-properties}

1. Select the Experience Manager logo and navigate to **[!UICONTROL Assets]** > **[!UICONTROL Files]**.
1. Navigate to a folder to which you want to remove one or more batch set presets.
1. On the page, to the left of the **[!UICONTROL Name]** column, select the check box of a folder.
1. In the toolbar, select **[!UICONTROL Properties]**.
1. On the folder's Properties page, select **[!UICONTROL Dynamic Media Processing]**.

   ![bsp-apply-via-properties2.png](/help/assets/assets-dm/bsp-remove-via-properties2.png)

1. Under **[!UICONTROL Batch Set Presets]**, select **[!UICONTROL X]** to the right of the preset type.

1. In the upper-right corner of the page, select **[!UICONTROL Save & Close]**.

## Delete batch set presets {#delete-bsp}

You can delete batch set presets to remove them permanently from [!DNL Dynamic Media]. That is, they no longer show on the [!UICONTROL Batch Set Preset] page nor are they shown in the **[!UICONTROL Batch Set Presets]** drop-down list of the **[!UICONTROL Dynamic Media Processing]** tab on the folder's **[!UICONTROL Properties]** page. As such, the preset is not applied to existing assets on a folder reprocess or when new assets are uploaded in the folder.

If you delete a preset that was previously applied to one or more folders, any image sets or spin sets that were created from assets in those folders continue to show as-is.

If you want to *remove* presets from folders instead, see [Remove batch set presets from folders](#remove-bsp-from-folder).

**To delete batch set presets:**

1. Select the Experience Manager logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets]**.
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, select the check box of one or more batch set presets that you want to delete.
1. In the toolbar, select **[!UICONTROL Delete Batch Set Presets]**.

   ![bsp-delete2.png](/help/assets/assets-dm/bsp-delete2.png)

1. In the **[!UICONTROL Delete Batch Set Presets]** dialog box, select **[!UICONTROL Delete]**.

   If the preset you are deleting was referenced by an asset folder, select **[!UICONTROL Force Delete]** instead.

   ![bsp-delete3.png](/help/assets/assets-dm/bsp-delete3.png)

>[!MORELIKETHIS]
>
>* [Image Sets](/help/assets/dynamic-media/image-sets.md)
>* [Spin Sets](/help/assets/dynamic-media/spin-sets.md)
>* [Configure selective publishing at the folder level in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md#selective-publish-configure-folder) - See "Sync Mode" in the topic if you want to learn more about syncing a single folder to [!DNL Dynamic Media].
>* [Create a Dynamic Media Configuration in Cloud Services](/help/assets/dynamic-media/config-dm.md#configuring-dynamic-media-cloud-services) - See "Dynamic Media sync mode" in the topic if you want to learn more about syncing all folders to [!DNL Dynamic Media].
