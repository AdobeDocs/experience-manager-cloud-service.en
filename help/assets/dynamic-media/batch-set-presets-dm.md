---
title: Batch Set Presets
description: Learn how to work with batch set presets for image sets and spin sets in Dynamic Media
contentOwner: Rick Brough
---

# About Batch Set Presets {#about-bsp}

Use **[!UICONTROL Batch Set Presets]** to help ease the creation and organization of multiple assets in an image set or spin set at the time you manually upload asset files to a folder either individually or using bulk ingestion, or have the preset run alongside the asset import jobs you schedule in Dynamic Media. Each preset is a uniquely named, self-contained set of instructions that defines how to construct the image set or spin sete using images that match the defined naming conventions in the preset recipe.

>[!IMPORTANT]
>
>If you used batch set presets in [!DNL Dynamic Media Classic], and you are migrating from [!DNL Dynamic Media Classic] to [!DNL Adobe Experience Manager as a Cloud Service], you will need to manually recreate your batch set presets definitions within [!DNL Adobe Experience Manager as a Cloud Service].

**Best Practice** &ndash; When working with batch set presets Adobe recommends the following workflow:

1. Create a batch set preset.
1. Create an asset folder and ensure it is synched to Dynamic Media.
1. Apply the batch set preset to the asset folder.
1. Upload images to the asset folder.
1. Create your image set or spin set.
1. Publish your image set or spin set. 

## Creating a batch set preset for an image set or a spin set {#creating-bsp}

To create Batch Set Presets, you should have some familiarity and understanding of regular expressions.

And, optimally, your company should also have a defined naming convention for how assets should be grouped together in a set.
To help you understand the importance of such a naming convention, suppose your company's defined naming convention is `<style>-<color>-<view>`, and the base name for the set must always be `<style>-<color>`, and the set name extension is `-SET`. If you upload an image named `0123-RED-01`, then a set would be created named `0123-RED-SET`. If you later upload images `0123-RED-03` and `0123-BLUE-01`, then the `RED-03` image would be added to the set in the second position because it is sorted lower than `01`. However, the `BLUE-01` image would be part of a new set named `0123-BLUE-SET`. For the next asset upload, you send files `0123-RED-02` and `0123-BLUE-02`. Each asset would be added to its respective set. The `RED-02` image would be automatically sorted between the existing `01` and `03` images, because of the sort order.

The **[!UICONTROL Batch Set Preset]** feature lets you create, edit, or delete batch set presets, and apply or remove batch set presets to or from asset folders. You can create as many batch set presets as necessary to cover all asset ingest jobs you require. There are two forms of batch set preset definitions: one for a default naming convention that your company may have defined, and one for custom naming conventions that you create on the fly.

You can use either the form field drop-down lists to define a batch set preset or use the raw code method, which lets you type out regular expression syntax.

**About Match and Base Name**

Two required elements are available for definition: **[!UICONTROL Match]** and **[!UICONTROL Base Name]**. These fields let you define all the elements of a naming convention and identify the part of the convention used to name the set in which they are contained. A company’s individual naming convention often makes use of one or more lines of definition for each of these elements. You can use as many lines for your unique definition and group them into distinct elements, such as for Main Image, Color element, Alternate View element, and Swatch element.
 
For example, the syntax for a literal match regular expression might look like the following:

`(\w+)-\w+-\w+`

**About Sequence Ordering**

You can optionally define the order in which images are displayed after the image set or spin set is grouped together in Dynamic Media. By default, your assets are ordered alphanumerically. However, you can use a comma-separated list of regular expressions to define the order.

With respect to sequence automation, you can specify rules to force-sort assets in a certain way, if necessary. For example, suppose your first asset is always named `_main` and you want it followed with `_alt1`, `_alt2`, `_alt2`. In such cases, then could create a sequence rule that looks like the following:

`.*_main,.*_alt[0-9]`

Nonetheless, it is best to rely on alphanumeric numbering for sorting as much as possible. Furthermore, you can use the image set or spin set editor tools in Dynamic Media to easily rearrange the sequence order of assets, or add and delete new assets in the set by using a drag-and-drop operation.

When you finish creating a batch set preset, you apply it to one or more folders that you have created. At that point, you are ready to create your image set or spin set, depending on the preset type you chose. See [Applying batch set presets to one or more folders](#apply-bsp).

<!-- See also [Creating a batch set preset for the auto generation of a 2D Spin Set](application-setup.md#creating_a_batch_set_preset_for_the_auto_generation_of_a_2d_spin_set). -->

**To create a batch set preset for an image set or a spin set:**

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Assets]** &gt; **[!UICONTROL Batch Set Presets.]**

   ![bsp-create1.png](/help/assets/assets-dm/bsp-create1.png)

1. On the **[!UICONTROL Batch Set Preset]** page, tap **[!UICONTROL Create.]**

   ![bsp-create2.png](/help/assets/assets-dm/bsp-create2.png)

1. In the **[!UICONTROL Create Batch Set Preset]** dialog box, in the **[!UICONTROL Preset Name]** text field, enter a descriptive name. The preset name is not editable unless you copy the preset later and specify a new name.

   ![bsp-create3.png](/help/assets/assets-dm/bsp-create3.png)

1. In the **[!UICONTROL Preset Type]** drop-down list, select **[!UICONTROL ImageSet]** or **[!UICONTROL SpinSet]**. Choose the preset type carefully; it is not editable later.
1. Tap **[!UICONTROL Create]**.
1. On the right side of the **[!UICONTROL Edit Batch Set Preset]** page, set the editable options you want under the **[!UICONTROL Preset Details]** and **[!UICONTROL Set Naming Convention]** headings.
   See [Preset Details, Set Naming Convention, and Rule Results - RegX options](#features-options-bsp) to learn more about the editable options that are available.

   ![bsp-create4.png](/help/assets/assets-dm/bsp-create4.png)

1. Create one or more regular expression groups. 

   * On the left side of the **[!UICONTROL Edit Batch Set Preset]** page, under **[!UICONTROL Match]**, **[!UICONTROL Base Name]**, or **[!UICONTROL Sequence Ordering]**, tap **[!UICONTROL Add Group]**.
   * The **[!UICONTROL Match]** and **[!UICONTROL Base Name]** forms are required; **[!UICONTROL Sequence Ordering]** is optional.
   * Using the drop-down lists and text boxes in the form, specify an expression string that you want to use to define the naming criteria for image set or spin set asset members. See [Regular expression options](#regx-options-bsp) to view the list of expressions that are available in each form.
      * As you select and specify expressions for a group, notice that the resulting regular expression syntax is reflected near the lower right side of the page, under the **[!UICONTROL Rule Results - RegX]** heading. These regular expression strings represent the pattern that you want to match in a search of Dynamic Media assets to create your image set or spin set.

   * When you add two or more groups, in the **[!UICONTROL And]** drop-down, select **[!UICONTROL And]** to conjoin a newly added group with any previous expression group you have added. Or, select **[!UICONTROL OR]** to add an alternation between the previous expression group and the new group you create. The **[!UICONTROL OR]** operand is defined by the use of a vertical line character `|` in the regular expression syntax itself.

      >[!IMPORTANT]
      >
      >Dynamic Media does not validate the regular expressions you create. However, the methods you use to create regular expressions on the [!UICONTROL Edit Batch Set Preset] page (except for the [!UICONTROL Raw Code] field) are designed to prevent most syntax errors.

1. Do one of the following:

   * To add another new group, under **[!UICONTROL Match]**, **[!UICONTROL Base Name]**, or **[!UICONTROL Sequencing Order]**, tap **[!UICONTROL Add Group]**. Create another regular expression group as you did in the previous step.
   * Review the regular expression syntax in the **[!UICONTROL Rule Results - RegX]** area. If you need to make changes to the syntax, make your edits in the respective group on the left side of the page.
   * If you are finished creating groups, continue to the next step.

1. In the upper-right corner of the page, tap **[!UICONTROL Save]**.

When you finish creating a batch set preset, you apply it to one or more empty asset folders, upload assets to the folder, then create your image set or spin set, depending on the preset type you chose. See [Applying batch set presets to one or more folders](#apply-bsp).

### Preset Details, Set Naming Convention, and Rule Results - RegX options {#features-options-bsp}

These options are available on the **[!UICONTROL Edit Batch Set Preset]** page when you create or edit a batch set preset.

See [Creating a batch set preset for an image set or a spin set](#creating-bsp) or [Editing a batch set preset](#edit-bsp).

   | **[!UICONTROL Preset Details]**  | Description | 
   | --- | --- |
   | Preset Name | Read-only. The name you specified when you first created the batch set. If you need to re-name the preset, you can copy the existing batch set preset and specify a new name. See [Copying an existing batch set preset](#copy-bsp). |
   | Type | Read-only. The type was specified when you first created the batch set. Copying an existing batch set preset does not let you change its [!UICONTROL Type]; you must create a new preset instead. |
   | Included Derived Assets | Optional. Select **[!UICONTROL Yes]** (default) to have Dynamic Media’s IPS (Image Production System) include generated or “derived” images with your Spin Set or Image Set. A derived asset is an image that was not directly uploaded by a user. Instead, the asset was produced by IPS when a master asset was uploaded. For example, an image asset that IPS generated from a page in a PDF, at the time the PDF was uploaded in Dynamic Media, is considered a derived asset. |
   | Destination Folder | Optional.  If you define large numbers of image sets or spin sets, you may prefer to keep these sets separate from the folders that contain the assets themselves. As such, you may want to consider creating an Image Sets or Spin Sets folder and redirect the application to place batch set generated sets here.<br>In such case, specify which folder within the AEM Assets folder structure (`/content/dam`) should have the batch set preset active. Be sure the folder is enabled for Dynamic Media synchronization to allow it as a destination folder. See [Configuring selective publishing at the folder level in Dynamic Media](/help/assets/dynamic-media/selective-publishing.md#selective-publish-configure-folder).<br>Be aware that more than one folder can have a given batch set preset assigned to it, if you apply the preset by way of the folder’s **[!UICONTROL Properties]**. See [Applying batch set presets from a folder's Properties page](#apply-bsp-to-folders-via-properties).<br>If you do not specify a folder, the batch set preset is created in the same folder as the asset upload folder. |
   | **[!UICONTROL Set Naming Convention]** |  |
   | Prefix<br>or<br>Suffix | Optional. Enter either a prefix, suffix, or both in the respective fields.<br>The prefix and suffix fields let you create as many batch set presets using an alternate, custom file naming convention that may be needed for a particular set of content. This method is especially useful in cases where there is an exception to a company's defined default naming scheme.<br>The prefix or suffix is added to the **[!UICONTROL Base Name]** you define in the **[!UICONTROL Asset Naming Convention]** area. By adding a prefix or suffix you ensure that your set gets created exclusively and independently from other assets. It can also serve to further help others identify file types. For example, to determine a color mode used, you could add as a prefix or suffix `rgb` or `cmyk`.<br>While specifying a set naming convention is not required to use batch set preset functionality, best practice recommends that you use the set naming convention to define as many elements of your naming convention that you want grouped in a set to help streamline batch set creation. |
   | **[!UICONTROL Rule Results - RegX]** |  |
   | Asset Naming Convention - Match | Read-only. Displays the regular expression syntax based on the Match form options you chose or the raw code you entered. |
   | Asset Naming Convention - Base Name | Read-only. Displays the regular expression syntax based on the Base Name form options you chose or the raw code you entered. |
   | Sequence Ordering - Match | Read-only. Displays the regular expression syntax based on the form options you chose or the raw code you entered. |

### Regular expression options {#regx-options-bsp}

These options are available on the **[!UICONTROL Edit Batch Set Preset]** page when you create or edit a batch set preset.

See [Creating a batch set preset for an image set or a spin set](#creating-bsp) or [Editing a batch set preset](#edit-bsp).

   | Match type | Context | Value you can specify | character(s), which are | and |
   | --- | --- | --- | --- | --- |
   | Literal Match | Exact phrase | `<one or more alpha or numeric characters>` |
   | | Match any | `<one or more alpha or numeric characters>` |
   | | Exclude any of these characters | `<one or more alpha or numeric characters>` |
   | Sequence Match | any number of | | Alphanumeric | Case Insensitive |
   | | | | | Uppercase |
   | | | | | Lowercase |
   | | | | Numeric | |
   | | | | Alpha | Case Insensitive |
   | | | | | Uppercase |
   | | | | | Lowercase |
   | | a series of | `<numeral (1-20)>`  | Alphanumeric | Case Insensitive |
   | | | | | Uppercase |
   | | | | | Lowercase |
   | | | | Numeric | |
   | | | | Alpha | Case Insensitive |
   | | | | | Uppercase |
   | | | | | Lowercase |
   | | one | | Alphanumeric | Case Insensitive |
   | | | | | Uppercase |
   | | | | | Lowercase |
   | | | | Numeric | |
   | | | | Alpha | Case Insensitive |
   | | | | | Uppercase |
   | | | | | Lowercase |
   | Raw Code | | `<regular expression pattern>`| | |

## About applying batch set presets to one or more folders {#apply-bsp}

When you assign batch set presets to one or more folders, any subfolders automatically inherit the presets from its parent folder.

If you assigned a different preset to a folder, the new preset overrides the previous preset. The previously existing folder assets remain unchanged. The new preset is applied on the assets that are added to the folder later.

Folders that have a preset assigned to it are indicated in the user interface by the name of the preset appearing in the card name.

![chlimage_1-517](assets/chlimage_1-517.png)

You can apply presets to specific folders or globally to all assets.

You can reprocess assets in a folder that already has an existing batch set preset that you later changed. See [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

Choose either one of the following:

* [Applying batch set presets to folders from the Batch Set Preset page](#apply-bsp-to-folders-via-bsp-page)
* [Applying batch set presets from a folder's Properties page](#apply-bsp-to-folders-via-properties)
* [Applying batch set presets to a folder with previously uploaded assets](#apply-bsp-to-uploaded-assets)

### Applying batch set presets to folders from the Batch Set Preset page {#apply-bsp-to-folders-via-bsp-page}

When you apply one or more batch set preseets to one or more folders, you FINSH

**To apply batch set presets to folders from the Batch Set Preset page:**

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets]**.
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, check one or more batch set presets that you want to apply one or more folders.
1. On the toolbar, tap **[!UICONTROL Apply Batch Preset to Folder(s)]**.

   ![bsp-apply-to-folders1.png](/help/assets/assets-dm/bsp-apply-to-folders1.png)

1. On the **[!UICONTROL Select Folder(s)]** page, select one or more folder you want the batch set presets applied to.

   ![bsp-apply-to-folders2.png](/help/assets/assets-dm/bsp-apply-to-folders2.png)

1. In the upper-right corner of the **[!UICONTROL Select Folder(s)]** page, tap **[!UICONTROL Apply]**.

### Applying batch set presets from a folder's Properties page {#apply-bsp-to-folders-via-properties}

When you apply one or more batch set preseets to one or more folders, you FINSH

**To apply batch set presets from a folder's Properties page:**

1. Tap the AEM logo and navigate to **[!UICONTROL Assets]** > **[!UICONTROL Files]**.
1. Navigate to a folder to which you want to apply one or more batch set presets.
1. On the page, to the left of the **[!UICONTROL Name]** column, select the check box.

   ![bsp-apply-via-properties1.png](/help/assets/assets-dm/bsp-apply-via-properties1.png)

1. On the toolbar, tap **[!UICONTROL Properties]**.
1. On the folder's Properties page, tap **[!UICONTROL Dynamic Media Processing]**.

   ![bsp-apply-via-properties2.png](/help/assets/assets-dm/bsp-apply-via-properties2a.png)

1. Under **[!UICONTROL Batch Set Preset(s)]**, from the **[!UICONTROL Preset Name]** drop-down list box, select the name of a batch set preset you want to apply. The screenshot above shows two batch set presets were applied to the folder.

   If no batch set preset names exist in the **[!UICONTROL Preset Name]** drop-down list box, it means you have not yet created any batch set presets. See [Creating a batch set preset](#creating-bsp).

   To remove an applied batch set preset, tap **[!UICONTROL X]** to the right of the preset type.

1. In the upper-right corner of the page, tap **[!UICONTROL Save & Close]**.

### Applying batch set presets to a folder with previously uploaded assets {#apply-bsp-to-uploaded-assets}

If you have a folder that already contains assets that you uploaded previously, you can still apply the batch set preset to the folder as usual. However, you will need to *reprocess* the assets to apply the preset across the existing assets in the folder or all assets across multiple folders.

See [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

## Editing a batch set preset {#edit-bsp}

You can edit an existing batch set preset that you have created. You can change any of the string groups you created for the asset naming convention or sequence order. If needed, you can also update the destination folder and set naming conventions.

You cannot, however, change the preset's name or preset type (Image Set or Spin Set). If it becomes necessary to change a preset's name, you can simply copy the existing preset and specify a new name. See [Copying a batch set preset.](#copy-bsp)

If the batch set preset was already applied to one or more folders before you edited it, the updated preset is re-applied when you *reprocess* assets in the folder. See [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

**To edit a batch set preset:**

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets.]**
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, check the batch set preset that you want to change.
1. On the toolbar, tap **[!UICONTROL Edit Batch Set Preset.]**

   ![bsp-edit1.png](/help/assets/assets-dm/bsp-edit1.png)

1. Edit the preset as necessary. 
1. In the upper-right corner of the **[!UICONTROL Batch Set Preset]** page, tap **[!UICONTROL Save.]**

## Copying an existing batch set preset {#copy-bsp}

You can copy an existing batch set preset to avoid having to manually recreate a complex preset, or if you simply want to rename a preset. You cannot, however, change the preset type used (Image Set or Spin Set).

If you copy an existing preset that is reference by asset folders, those folders are not affected.

**To copy an existing batch set preset:**

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets.]**
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, select the check box of the batch set preset that you want to copy.

   ![bsp-copy1.png](/help/assets/assets-dm/bsp-copy1.png)

1. On the toolbar, tap **[!UICONTROL Copy]**.
1. In the **[!UICONTROL Copy Batch Set Preset]** dialog box, in the **[!UICONTROL Title]** text box, type a new name for the preset.

   ![bsp-copy2.png](/help/assets/assets-dm/bsp-copy2.png)

1. Tap **[!UICONTROL Copy]**.

## Deleting batch set presets {#delete-bsp}

You can delete batch set presets to remove them permanently from Dynamic Media. If you delete a preset that was previously applied to one or more asset folders, 

CHECK! the folder's assets remain unchanged until you reprocess the folder (see [Reprocessing assets]()CHECK! In such cases, you will need to "force delete" the preset. 

If you want to remove presets from folders instead, see [Removing batch set presets from folders](#remove-bsp-from-folder).

**To delete batch set presets:**

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets]**.
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, select the check box of one or more batch set presets that you want to delete.

   ![bsp-delete1.png](/help/assets/assets-dm/bsp-delete1.png)

1. On the toolbar, tap **[!UICONTROL Delete Batch Set Preset(s)]**.

   ![bsp-delete2.png](/help/assets/assets-dm/bsp-delete2.png)

1. In the **[!UICONTROL Delete Batch Set Presets]** dialog box, tap **[!UICONTROL Delete]**. 

   If the preset you are deleting was referenced by an asset folder, you may need to tap **[!UICONTROL Force Delete]** instead.

   ![bsp-delete3.png](/help/assets/assets-dm/bsp-delete3.png)



## About removing batch set presets from folders {#remove-bsp-from-folder}

When you remove batch set presets from one or more folders, FINISH

If no batch set presets were applied to a selected folder, 

Choose from the following:

* [Removing batch set presets from folders by way of the Batch Set Preset page](#remove-bsp-from-folders-via-bsp-page)
* [Removing batch set presets from a folder's Properties page](#remove-bsp-from-folders-via-properties)

### Removing batch set presets from folders by way of the Batch Set Preset page {#remove-bsp-from-folders-via-bsp-page}

When you remove one or more batch set preseets from one or more folders, you FINSH

See also [Removing batch set presets from a folder's Properties page](#remove-bsp-from-folders-via-properties).

**To remove batch set presets from folders by way of the Batch Set Preset page:**

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets]**.
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, select the check box of one or more batch set presets that you want to remove from one or more folders.

   ![bsp-remove-from-folders1.png](/help/assets/assets-dm/bsp-remove-from-folders1.png)

1. On the toolbar, tap **[!UICONTROL Remove Batch Preset from Folder(s)]**.

   ![bsp-remove-from-folders2.png](/help/assets/assets-dm/bsp-remove-from-folders2.png)

1. On the **[!UICONTROL Select Folder(s)]** page, select one or more folders in which you want the batch set presets removed. The screenshot above shows a selected folder with the names of two batch set presets already applied to it that will be removed.
1. In the upper-right corner of the **[!UICONTROL Select Folder(s)]** page, tap **[!UICONTROL Remove]**.

   ![bsp-remove-from-folders3.png](/help/assets/assets-dm/bsp-remove-from-folders3.png)

1. In the **[!UICONTROL Remove profile]** dialog box, tap **[!UICONTROL Remove]**.

### Removing batch set presets from a folder's Properties page {#remove-bsp-from-folders-via-properties}

When you remove one or more batch set presets from a folders, you FINSH

See [Removing batch set presets from folders by way of the Batch Set Preset page](#remove-bsp-from-folders-via-bsp-page).

**To remove batch set presets from a folder's Properties page:**

1. Tap the AEM logo and navigate to **[!UICONTROL Assets]** > **[!UICONTROL Files]**.
1. Navigate to a folder to which you want to remove one or more batch set presets.
1. On the page, to the left of the **[!UICONTROL Name]** column, select the check box.

   ![bsp-apply-via-properties1.png](/help/assets/assets-dm/bsp-apply-via-properties1.png)

1. On the toolbar, tap **[!UICONTROL Properties]**.
1. On the folder's Properties page, tap **[!UICONTROL Dynamic Media Processing]**.

   ![bsp-apply-via-properties2.png](/help/assets/assets-dm/bsp-remove-via-properties2.png)

1. Under **[!UICONTROL Batch Set Preset(s)]**, tap **[!UICONTROL X]** to the right of the preset type.

1. In the upper-right corner of the page, tap **[!UICONTROL Save & Close]**.

>[!MORELIKETHIS]
>
>* [Image Sets](/help/assets/dynamic-media/image-sets.md)
>* [Spin Sets](/help/assets/dynamic-media/spin-sets.md)
>* [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets)