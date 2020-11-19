---
title: Batch Set Presets
description: Learn how to work with batch set presets for image sets and spin sets in Dynamic Media
contentOwner: Rick Brough
---

# About Batch Set Presets {#about-bsp}

Use **[!UICONTROL Batch Set Presets]** to automatically create image sets or spin sets while a job is running to upload assets to Dynamic Media.

You first define naming conventions for the assets that you want to group together in a set. You can then create a batch set preset to reference these images. Each preset is a uniquely named, self-contained set of instructions that defines how to construct the set using images that match the defined naming conventions in the preset recipe.

All active batch set presets for a company are listed on the Upload Job Option dialog box, so you can specify which preset you want applied during each upload session. Company administrators see all active and inactive batch set presets. When you upload files, Dynamic Media Classic automatically creates a set with all files that match the defined naming convention in the active presets.

**Best Practice** &ndash; When working with batch set presets, image sets, and spin sets, Adobe recommends the following workflow:
1. Create a batch set preset.
1. Create a new asset folder.
1. Apply the batch set preset to the asset folder.
1. Upload images to the asset folder.
1. Create your image set or spin set.
1. Publish your image set or spin set. 

## Creating a batch set preset for an image set or a spin set {#creating-bsp}

Dynamic Media uses batch set presets to organize assets that share some common information or content into sets of images for display in viewers. You can enable saved batch set presets to automatically run alongside the asset import jobs you schedule in Dynamic Media.

Use the **[!UICONTROL Batch Set Preset]** feature to create and edit or delete batch set presets and to apply or remove batch set presets to or from asset folders. You can create as many batch set presets as necessary to cover all asset ingest jobs you require. There are two forms of batch set preset definitions: one for a default naming convention that you might have set up, and one for custom naming conventions that you create on the fly.

You can use the either the form field method to define a batch set preset or the code method, which lets you use regular expressions. As in Default Naming, you can choose Code View at the same time you are defining in the Form View and use of regular expressions to build your definitions. Alternately, you can uncheck either view to use one or the other exclusively.

Two elements are available for definition, Match and Base Name. These fields let you define all elements of a naming convention and identify the part of the convention used to name the set in which they are contained. A company’s individual naming convention may make use of one or more lines of definition for each of these elements. You can use as many lines for your unique definition and group them into distinct elements, such as for Main Image, Color element, Alternate View element, and Swatch element.

When you finish creating a batch set preset, you apply it to one or more folders, then create your image set or spin set, depending on the preset type you chose. See [Applying batch set presets to one or more folders](#apply-bsp).

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
   See [Asset Naming Convention and Sequence Ordering fields](#regx-main-fields-bsp) to learn more about the group types that are available.
   * Specify an expression string that you want to use to define the naming criteria for image set or spin set asset members.
   See [Regular expression options](#regx-options-bsp) to view the list of expressions that are available in each field.
      * As you select and specify expressions for a group, notice that the resulting regular expression syntax is reflected near the lower right side of the page, under the **[!UICONTROL Rule Results - RegX]** heading. These regular expression strings represent the pattern that you want to match in a search of Dynamic Media assets to create your image set or spin set.

      >[!IMPORTANT]
      >
      >Dynamic Media does not validate the regular expressions you create. However, the methods you use to create regular expressions on the [!UICONTROL Edit Batch Set Preset] page (except for the [!UICONTROL Raw Code] field) are designed to prevent most syntax errors.

1. Do one of the following:

   * To add another new group, under **[!UICONTROL Match]**, **[!UICONTROL Base Name]**, or **[!UICONTROL Sequencing Order]**, tap **[!UICONTROL Add Group]**. Create another regular expression group as you did in the previous step.
   * Review the regular expressions syntax in the **[!UICONTROL Rule Results - RegX]** area. If you need to make changes to the syntax, make your edits in the respective group on the left side of the page.
   * If you are finished creating groups, continue to the next step.

1. In the upper-right corner of the page, tap **[!UICONTROL Save]**.

When you finish creating a batch set preset, you apply it to one or more folders, upload assets to the folder, then create your image set or spin set, depending on the preset type you chose. See [Applying batch set presets to one or more folders](#apply-bsp).

### Preset Details, Set Naming Convention, and Rule Results - RegX options {#features-options-bsp}

These options are available on the **[!UICONTROL Edit Batch Set Preset]** page when you create or edit a batch set preset.

See [Creating a batch set preset for an image set or a spin set](#creating-bsp) or [Editing a batch set preset](#edit-bsp).

   | **[!UICONTROL Preset Details]**  | Description | 
   | --- | --- |
   | Preset Name | Not editable. The name you specified when you first created the batch set. If you need to re-name the preset, you can copy the existing batch set preset and specify a new name. See [Copying an existing batch set preset](#copy-bsp). |
   | Type | Not editable. The type was specified when you first created the batch set. Copying an existing batch set preset does not let you change its [!UICONTROL Type]; you must create a new preset instead. |
   | Included Derived Assets | Optional. Select **[!UICONTROL Yes]** (default) to include derived assets in your batch set. For example, when you upload assets, Dynamic Media creates one additional asset per uploaded asset, letting you see all of the assets in AEM ??? |
   | Destination Folder | Optional. Specify the folder where you want the the image set or spin set created within the AEM Assets folder structure. If you define large numbers of image sets or spin sets, you may prefer to keep these sets separate from the folders that contain the assets themselves. As such, you may want to consider creating an Image Sets or Spin Sets folder and redirect the application to place batch set generated sets here. |
   | **[!UICONTROL Set Naming Convention]** |  |
   | Prefix<br>or<br>Suffix | Optional. Enter either a prefix, suffix, or both in the respective fields.<br>The prefix and suffix fields let you create as many batch set presets using an alternate, custom file naming convention that may be needed for a particular set of content. This method is especially useful in cases where there is an exception to a company's defined default naming scheme.<br>The prefix or suffix is added to the **[!UICONTROL Base Name]** you define in the **[!UICONTROL Asset Naming Convention]** area. By adding a prefix or suffix you ensure that your set gets created exclusively and independently from other assets. It can also serve to further help others identify file types. For example, to determine a color mode used, you could add as a prefix or suffix `rgb` or `cmyk`.<br>While specifying a set naming convention is not required to use batch set preset functionality, best practice recommends that you use the set naming convention to define as many elements of your naming convention that you want grouped in a set to help streamline batch set creation. |
   | **[!UICONTROL Rule Results - RegX]** |  |
   | Asset Naming Convention - Match | Not editable. Displays the regular expression syntax based on the Match expressions you chose or the raw code you enter. To edit the syntax, you make changes to the expressions you selected for a Match group. |
   | Asset Naming Convention - Base Name | Not editable. Displays the regular expression syntax based on the Base Name expressions you chose or the raw code you enter. To edit the syntax, you make changes to the expressions you selected for a Base Name group. |
   | Sequence Ordering - Match | Not editable. Displays the regular expression syntax based on the expressions you chose or the raw code you enter. To edit the syntax, you make changes to the expressions you selected for a Sequence Ordering group. |

### Asset Naming Convention and Sequence Ordering fields {#regx-main-fields-bsp}

These options are available on the **[!UICONTROL Edit Batch Set Preset]** page when you create or edit a batch set preset.

See [Creating a batch set preset for an image set or a spin set](#creating-bsp) or [Editing a batch set preset](#edit-bsp).

   | **[!UICONTROL Asset Naming Convention]** | Description |
   | --- | --- |
   | Match | Required. To delete a group, tap **[!UICONTROL X]**. |
   | Base Name | Required. To delete a group, tap **[!UICONTROL X]**. |
   | And/Or | Optional. These variables are only available if you add two or more groups within the same Match, Base Name, or Sequence Order. In the **[!UICONTROL And]** drop-down, select **[!UICONTROL And]** to conjoin a newly added group with any previous expression group you have added. Or, select **[!UICONTROL OR]** to add an alternation between the previous expression group and the new group you are about to create. The **[!UICONTROL OR]** operand is defined by the use of a vertical line character `|` in the regular expression syntax itself.|
   | **[!UICONTROL Sequence Ordering]** |  |
   | Match | Optional. If you are finished creating groups, continue to the next step. |
   | And/Or | Optional. These variables are only available if you add two or more groups within the same Match, Base Name, or Sequence Order. In the **[!UICONTROL And]** drop-down, select **[!UICONTROL And]** to conjoin a newly added group with any previous expression group you have added. Or, select **[!UICONTROL OR]** to add an alternation between the previous expression group and the new group you are about to create. The **[!UICONTROL OR]** operand is defined by the use of a vertical line character `|` in the regular expression syntax itself.

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


   **Sequence Ordering**

| | a series of | 

   To autogenerate a 2D Spin Set, select **Multi-Axis Spin Set** from the Batch Set Type drop-down list.

1. Do one of the following:

    * If you are using a default naming convention that you previously set up under Application Setup &gt; Batch Set Presets &gt; Default Naming, expand **Asset Naming Conventions**, and then in the File Naming drop-down list, click **Default**.
    * To define a naming convention as you set up the preset, expand **Asset Naming Conventions**, and then in the File Naming drop-down list, click **Custom**.

1. For Sequence order, define the order for the images after the set is grouped together in Dynamic Media Classic. By default, your assets are ordered alphanumerically. However, you can use a comma-separated list of regular expressions to define the order. 
1. For Set Naming and Creation Convention, specify the suffix or prefix to the base name you defined in the Asset Naming Convention. Also define where the image set will be created within the Dynamic Media Classic folder structure.

   If you define large numbers of image sets, you may prefer to keep these separate from the folders that contain the assets themselves. Many customers create an Image Sets folder and redirect the application to place batch set generated sets here.

1. Click **Save** in the Details Panel.











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

## Applying batch set presets to one or more folders {#apply-bsp}

When you assign batch set presets to one or more folders, any subfolders automatically inherit the presets from its parent folder.

If you assigned a different preset to a folder, the new preset overrides the previous preset. The previously existing folder assets remain unchanged. The new preset is applied on the assets that are added to the folder later.

Folders that have a preset assigned to it are indicated in the user interface by the name of the preset appearing in the card name.

![chlimage_1-517](assets/chlimage_1-517.png)

You can apply presets to specific folders or globally to all assets.

You can reprocess assets in a folder that already has an existing batch set preset that you later changed. See [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

Choose either one of the following:

* [Applying batch set presets to folders from the Batch Set Preset page](#apply-bsp-to-folders-via-bsp-page)
* [Applying batch set presets from a folder's Properties page](#apply-bsp-to-folders-via-properties)

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





## Removing batch set presets from folders {#remove-bsp-from-folder}

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
>* [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).