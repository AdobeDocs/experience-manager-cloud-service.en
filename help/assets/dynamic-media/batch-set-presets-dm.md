---
title: Batch Set Presets
description: Learn how to work with batch set presets for image sets and spin sets in Dynamic Media
contentOwner: Rick Brough
---

# About Batch Set Presets {#about-bsp}

Use **[!UICONTROL Batch Set Presets]** to automatically create image sets or spin sets while a job is running to upload assets to Dynamic Media.

You first define naming conventions for the assets that you want to group together in a set. You can then create a batch set preset to reference these images. Each preset is a uniquely named, self-contained set of instructions that defines how to construct the set using images that match the defined naming conventions in the preset recipe.

All active batch set presets for a company are listed on the Upload Job Option dialog box, so you can specify which preset you want applied during each upload session. Company administrators see all active and inactive batch set presets. When you upload files, Dynamic Media Classic automatically creates a set with all files that match the defined naming convention in the active presets.

## Creating a batch set preset for an image set or a spin set {#creating-bsp}

Dynamic Media uses batch set presets to organize assets that share some common information or content into sets of images for display in viewers. You can enable saved batch set presets to automatically run alongside the asset import jobs you schedule in Dynamic Media.

Use the **[!UICONTROL Batch Set Preset]** feature to create and edit or delete batch set presets and to apply or remove batch set presets to or from asset folders. You can create as many batch set presets as necessary to cover all asset ingest jobs you require. There are two forms of batch set preset definitions: one for a default naming convention that you might have set up, and one for custom naming conventions that you create on the fly.

You can use the either the form field method to define a batch set preset or the code method, which lets you use regular expressions. As in Default Naming, you can choose Code View at the same time you are defining in the Form View and use of regular expressions to build your definitions. Alternately, you can uncheck either view to use one or the other exclusively.

Two elements are available for definition, Match and Base Name. These fields let you define all elements of a naming convention and identify the part of the convention used to name the set in which they are contained. A company’s individual naming convention may make use of one or more lines of definition for each of these elements. You can use as many lines for your unique definition and group them into distinct elements, such as for Main Image, Color element, Alternate View element, and Swatch element.


See also [Creating a batch set preset for the auto generation of a 2D Spin Set](application-setup.md#creating_a_batch_set_preset_for_the_auto_generation_of_a_2d_spin_set).

**To create a batch set preset for an image set or a spin set** 

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Assets]** &gt; **[!UICONTROL Batch Set Presets.]**
1. In the **[!UICONTROL Preset Name]** text field, enter a descriptive name. The preset name is not editable later.
1. In the **[!UICONTROL Preset Type]** drop-down list, select **[!UICONTROL ImageSet]** or **[!UICONTROL SpinSet]**. The preset type is not editable later.
1. Tap **[!UICONTROL Create.]**
1. On the right side of the **[!UICONTROL Edit Batch Set Preset]** page, set the editable options you want.
    Use the [Table of features and options for Preset Details, Set Naming Convention, and Rule Results - RegX fields](#features-options-bsp) to learn more about the editable options that are available for your batch set preset.

1. Create one or more regular expression groups. On the left side of the Edit Batch Set Preset page, under **[!UICONTROL Match]**, **[!UICONTROL Base Name]**, or **[!UICONTROL Sequence Ordering]**, tap **[!UICONTROL Add Group]**, then specify a expression string that you want to use to define the image set's or spin set's members naming criteria.
Use the [Table of expressions for Asset Naming Convention and Sequence Ordering](#regx-options-bsp) to see the list of expressions that are available to create your regular expression.<br>As you select and specify expressions for this first group, notice that the resulting regular expression syntax is reflected near the lower right side of the page, under the **[!UICONTROL Rule Results - RegX]** heading. These regular expression strings represent the pattern that you want to match in a search of Dynamic Media assets to create your image set or spin set.

    >[!IMPORTANT]
    >
    >There is no validation of regular expressions you create, by Dynamic Media. However, the method of creating regular expressions for a batch set preset is designed to prevent most syntax errors.

   | **[!UICONTROL Asset Naming Convention]**  | Description | 
   | --- | --- | --- |
   | Match | Optional. To delete a group, tap **[!UICONTROL X]**.|
   | Base Name | Optional. To delete a group, tap **[!UICONTROL X]**. |
   | And/Or | Optional. These variables are only available if you add two or more groups within the same Match, Base Name, or Sequence Order. In the **[!UICONTROL And]** drop-down, select **[!UICONTROL And]** to conjoin a newly added group with any previous expression group you have added. Or, select **[!UICONTROL OR]** to add an alternation between the previous expression group and the new group you are about to create. The **[!UICONTROL OR]** operand is defined by the use of a vertical line character `|` in the regular expression syntax itself.|
   | **[!UICONTROL Sequence Ordering]** |  |
   | Match | Optional. If you are finished creating groups, continue to the next step. |
   | And/Or | Optional. These variables are only available if you add two or more groups within the same Match, Base Name, or Sequence Order. In the **[!UICONTROL And]** drop-down, select **[!UICONTROL And]** to conjoin a newly added group with any previous expression group you have added. Or, select **[!UICONTROL OR]** to add an alternation between the previous expression group and the new group you are about to create. The **[!UICONTROL OR]** operand is defined by the use of a vertical line character `|` in the regular expression syntax itself.

   SCREENSHOT HERE

1. Do one of the following:

   * To add another new group, under **[!UICONTROL Match]**, **[!UICONTROL Base Name]**, or **[!UICONTROL Sequencing Order]**, tap **[!UICONTROL Add Group]**. Create another group as you did in the previous step.
   * Review the regular expressions syntax in the [!UICONTROL Rule Results - RegX] area. If you need to make changes to the syntax, make your edits in the respect group on the left side of the page.
   * If you are finished creating groups, continue to the next step.

1. In the upper-right corner of the page, tap **[!UICONTROL Save]**.
You are now ready to apply the batch set preset to one or more folders.
ADD LINKS TO TOPICS HERE.

### Table of features and options for Preset Details, Set Naming Convention, and Rule Results - RegX fields {#features-options-bsp}

These features and options are available on the right side of the Edit Batch Set Preset page.

   | **[!UICONTROL Preset Details]**  | Description | 
   | --- | --- | --- |
   | Preset Name | Not editable. The name you specified when you first created the batch set. If you need to re-name the preset, you can copy the existing batch set preset and specify a new name. See [Copying an existing batch set preset](#copy-bsp). |
   | Type | Not editable. The type was specified when you first created the batch set. Copying an existing batch set preset does not let you change its [!UICONTROL Type]; you must create a new preset instead. |
   | Included Derived Assets | Optional. Select **[!UICONTROL Yes]** (default) to include derived assets in your batch set. For example, when you upload assets, Dynamic Media creates one additional asset per uploaded asset, letting you see all of the assets in AEM ??? |
   | Destination Folder | Optional. Specify the folder where you want the the image set or spin set created within the AEM Assets folder structure. If you define large numbers of image sets or spin sets, you may prefer to keep these sets separate from the folders that contain the assets themselves. As such, you may want to consider creating an Image Sets or Spin Sets folder and redirect the application to place batch set generated sets here. |
   | **[!UICONTROL Set Naming Convention]** |  |
   | Prefix<br>or<br>Suffix | Optional. Enter either a prefix, suffix, or both in the respective fields.<br>The prefix and suffix fields let you create as many batch set presets using an alternate, custom file naming convention that may be needed for a particular set of content. This method is especially useful in cases where there is an exception to a company's defined default naming scheme.<br>The prefix or suffix is added to the **[!UICONTROL Base Name]** you define in the **[!UICONTROL Asset Naming Convention]** area. By adding a prefix or suffix you ensure that your set gets created exclusively and independently from other assets. It can also serve to further help others identify file types. For example, to determine a color mode used, you could add as a prefix or suffix `rgb` or `cmyk`.<br>While specifying a set naming convention is not required to use batch set preset functionality, best practice recommends that you use the set naming convention to define as many elements of your naming convention that you want grouped in a set to help streamline batch set creation. |
   | **[!UICONTROL Rule Results - RegX]** |  |
   | Asset Naming Convention - Match | Not editable. Displays the regular expression syntax based on the Match expressions you chose or the raw code you enter. To edit the syntax, make changes to the expressions you selected for a Match group. |
   | Asset Naming Convention - Base Name | Not editable. Displays the regular expression syntax based on the Base Name expressions you chose or the raw code you enter. To edit the syntax, make changes to the expressions you selected for a Base Name group. |
   | Sequence Ordering - Match | Not editable. Displays the regular expression syntax based on the expressions you chose or the raw code you enter. To edit the syntax, make changes to the expressions you selected for a Sequence Ordering group. |


https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet

### Table of expressions for Asset Naming Convention and Sequence Ordering {#regx-options-bsp}

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

You can edit an existing batch set preset that you have created. You can change the asset naming convention or sequence order. You can also update the destination folder and set naming conventions. You cannot, however, change the preset's name or type. If it becomes necessary to change a preset's name, you can simply copy the existing preset and specify a new name.

See [Copying a batch set preset.](#copy-bsp)

If the batch set preset was already applied to one or more folders before you edited it, the updated preset is re-applied when you *reprocess* assets in the folder.

kSee [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets.]**
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, check the batch set preset that you want to change.
1. On the toolbar, tap **[!UICONTROL Edit Batch Set Preset.]**

   SCREENSHOT

1. Edit the preset as necessary. 
1. In the upper-right corner of the **[!UICONTROL Batch Set Preset]** page, tap **[!UICONTROL Save.]**

## Copying an existing batch set preset {#copy-bsp}

If you copy an existing preset that was previously applied to folders, those folders are not affected when you copy the preset.

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets.]**
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, check the batch set preset that you want to copy.
1. On the toolbar, tap **[!UICONTROL Copy]**.
1. In the **[!UICONTROL Copy Batch Set Preset]** dialog box, in the **[!UICONTROL Title]** field, type a new name for the preset.
1. In the upper-right corner of the **[!UICONTROL Batch Set Preset]** page, tap **[!UICONTROL Save.]**

## Deleting batch set presets {#delete-bsp}

If you delete one or more batch set presets that were previously applied to one or more asset folders, the folder's assets remain unchanged.

1. Tap the AEM logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Batch Set Presets.]**
1. On the **[!UICONTROL Batch Set Presets]** page, to the left of the **[!UICONTROL Preset Name]** column, check one or more batch set presets that you want to remove.
1. On the toolbar, tap **[!UICONTROL Delete Batch Set Presets]**.
1. In the **[!UICONTROL Delete Batch Set Presets]** dialog box, tap **[!UICONTROL Delete]**.
If the presets were previously applied to one or more asset folders, you may need to tap **[!UICONTROL Force Delete]** instead.

## Applying a batch set preset to one or more folders {#apply-bsp-to-folder}

When you assign a batch set preset to a folder, any subfolders automatically inherit the preset from its parent folder. This means that you can assign only one preset to a folder. As such, consider carefully the folder structure of where you upload, store, use, and archive assets.

If you assigned a different preset to a folder, the new preset overrides the previous preset. The previously existing folder assets remain unchanged. The new preset is applied on the assets that are added to the folder later.

Folders that have a preset assigned to it are indicated in the user interface by the name of the preset appearing in the card name.

![chlimage_1-517](assets/chlimage_1-517.png)

You can apply presets to specific folders or globally to all assets.

You can reprocess assets in a folder that already has an existing batch set preset that you later changed. See [Reprocessing assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

## Removing a batch set preset from one or more folders {#remove-bsp-from-folder}



>[!MORELIKETHIS]
>
>* [Previewing an asset](previewing-asset.md#previewing_an_asset) FIX
>* [Setting up Image Presets](setting-image-presets.md#setting_up_image_presets) FIX
>* [Viewing, adding, and exporting metadata](viewing-adding-exporting-metadata.md#viewing_adding_and_exporting_metadata) FIX
>* [Checking job files](checking-job-files.md#checking_job_files) FIX