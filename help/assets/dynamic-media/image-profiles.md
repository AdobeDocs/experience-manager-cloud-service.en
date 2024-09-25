---
title: Dynamic Media Image Profiles
description: Learn how to create Dynamic Media Image Profiles that contain settings for unsharp mask, and smart crop or smart swatch, or both. Then, apply the profile to a folder of image assets.
contentOwner: Rick Brough
feature: Asset Management,Image Profiles,Renditions,Best Practices
role: User
exl-id: 0856f8a1-e0a9-4994-b338-14016d2d67bd
---
# Dynamic Media Image Profiles {#image-profiles}

When uploading images, you can automatically crop the image upon upload by applying an Image Profile to the folder.

>[!IMPORTANT]
>
>Image Profiles are not applicable to PDF, animated GIF, or INDD (Adobe InDesign) files.

## Unsharp Mask option {#unsharp-mask}

When creating an Image Profile, you can use the **[!UICONTROL Unsharp mask]** option to fine-tune a sharpening filter effect on the final downsampled image. You can control the intensity of the effect, radius of the effect (measured in pixels), and a threshold of contrast that is ignored. This effect uses the same options as Adobe Photoshop's "Unsharp Mask" filter.

>[!NOTE]
>
>The unsharp mask is only applied to downscaled renditions within the PTIFF (pyramid tiff) that are downsampled more than 50%. The unsharp mask does not affect the largest-sized renditions within the ptiff. Whereas smaller-sized renditions, such as thumbnails, are altered (and show the unsharp mask).

In **[!UICONTROL Unsharp Mask]**, you have the following filtering options:

<table>
 <tbody>
  <tr>
   <td><strong>Option</strong></td>
   <td><strong>Description</strong></td>
  </tr>
  <tr>
   <td>Amount</td>
   <td>Controls the amount of contrast applied to edge pixels. The default is 1.75. For high-resolution images, you can increase it to as high as 5. Think of Amount as a measure of filter intensity. The range is 0-5.</td>
  </tr>
  <tr>
   <td>Radius</td>
   <td>Determines the number of pixels surrounding the edge pixels that affect the sharpening. For high-resolution images, enter from 1 through 2. A low value sharpens only the edge pixels; a high value sharpens a wider band of pixels. The correct value depends on the size of the image. The default value is 0.2. The range is 0-250.</td>
  </tr>
  <tr>
   <td>Threshold</td>
   <td><p>Determines the range of contrast to ignore when the unsharp mask filter is applied. This option controls how different sharpened pixels must be from their surroundings to be considered edge pixels. Only pixels that meet this threshold are sharpened. To avoid introducing noise, experiment with values between 0-255.</p> </td>
  </tr>
 </tbody>
</table>

Sharpening is described in [Sharpening Images](/help/assets/dynamic-media/assets/sharpening_images.pdf).

## Crop options {#crop-options}

When you implement smart crop on images, Adobe recommends the following best practice and enforces the following limit:

| Asset - Limit type | Best practice | Limit imposed |
| --- | --- | --- |
| **Image** - Number of Smart Crops per image | 5 | 100 |

See also [Dynamic Media limitations](/help/assets/dynamic-media/limitations.md).

<!-- CQDOC-16069 for the paragraph directly below -->

Smart crop coordinates are aspect ratio dependent. For the smart crop settings in an Image Profile, if the aspect ratio is the same for the added dimensions in the Image Profile, then the same aspect ratio is sent to Dynamic Media. Adobe recommends that you use the same crop area. Doing so ensures that there is no impact to different dimensions used in the Image Profile.

Each smart crop generation that you create requires extra processing. For example, adding more than five smart crop aspect ratios may result in a slow asset ingestion rate. It may also cause an increased load on systems. Since smart crop can be applied at the folder level, Adobe advises using it only for folders where it is necessary.

**Guidelines for defining Smart Crop in an Image Profile**
To keep Smart Crop usage under control, and to optimize for processing time and storage of crops, Adobe recommends the following guidelines and tips:

* Image assets that are going to have a smart crop applied to them must be a minimum of 50 x 50 pixels or larger.
* Ideally, have 10-15 smart crops per image to optimize for screen ratios and processing time.
* Name smart crops based on crop dimensions, not on end usage. Doing so helps to optimize for duplicates where a single dimension is used on multiple pages.
* Create page-wise/asset type-wise Image Profiles for specific folders and subfolders instead of a common smart crop profile that is applied to all folders or all assets.
* An Image Profile that you apply to subfolders overrides an Image Profile that is applied to the folder.
* An Image Profile that contains duplicate smart crop dimensions is not permitted.
* Duplicate named Image Profiles that have smart crop options set are not permitted.

You have two image crop options from which to choose: pixel crop and smart crop. You can also choose to automate the creation of color and image swatches or preserve crop content across target resolutions.

>[!IMPORTANT]
>
>Adobe recommends that you review any generated crops and swatches to ensure that they are appropriate and relevant to your brand and values.

| Option | When to use | Description |
| --- | --- | --- |
| **[!UICONTROL Pixel Crop]** | Bulk crop images based on dimensions only. | From the **[!UICONTROL Cropping Options]** drop-down list, select **[!UICONTROL Pixel Crop]**.<br>To crop from the sides of an image, you enter the number of pixels to crop from any side or each side of the image. How much of the image is cropped depends on the ppi (pixels per inch) setting in the image file.<br>An Image Profile pixel crop renders in the following manner:<br>&bull; Values are Top, Bottom, Left, and Right.<br>&bull; Upper left is considered `0,0` and the pixel crop is calculated from there.<br>&bull; Crop starting point: Left is X and Top is Y<br>&bull; Horizontal calculation: horizontal pixel size of original image minus Left and then minus Right.<br>&bull; Vertical calculation: vertical pixel height minus Top, and then minus Bottom.<br>For example, suppose you have a 4000 x 3000 pixel image. You use values: Top=250, Bottom=500, Left=300, Right=700.<br>From upper-left (300,250) crop using the fill space of (4000-300-700, 3000-250-500, or 3000,2250). |
| **[!UICONTROL Smart Crop]** | Bulk crop images based on their visual focal point. | Smart Crop uses the power of artificial intelligence in Adobe Sensei to automate the cropping of images quickly in bulk. Smart Crop automatically detects and crops to the focal point in any image to acquire the intended point of interest, regardless of screen size.<br>From the **[!UICONTROL Cropping Options]** drop-down list, select **[!UICONTROL Smart Crop]**, then to the right of **[!UICONTROL Responsive Image Crop]**, enable (turn on) the feature.<br>The default breakpoint sizes (**[!UICONTROL Large]**, **[!UICONTROL Medium]**, **[!UICONTROL Small]**) cover the full range of sizes that most images on mobile and tablet devices, desktops, and banners use. If desired, you can edit the default names of Large, Medium, and Small.<br>To add more breakpoints, select **[!UICONTROL Add Crop]**; to delete a crop, select the Garbage Can icon. |
| **[!UICONTROL Color and Image Swatch]** | Bulk generates an Image Swatch for each image. | **Note**: Smart Swatch is not supported in Dynamic Media Classic.<br>Automatically locate and generate high-quality swatches from product images that show color or texture.<br>From the **[!UICONTROL Cropping Options]** drop-down list, select **[!UICONTROL Smart Crop]**. Then to the right of **[!UICONTROL Color and Image Swatch]**, enable (turn on) the feature. Enter a pixel value in the **[!UICONTROL Width]** and **[!UICONTROL Height]** text boxes.<br>While all image crops are available from the Renditions rail, swatches are only used by way of the **[!UICONTROL Copy URL]** feature. Use your own viewing component to render the swatch on your site. The exception to this rule is carousel banners. Dynamic Media provides the viewing component for the swatch used in carousel banners.<br><br>**Using image swatches**<br>The URL for image swatches is straightforward:<br>`/is/image/company/&lt;asset_name&gt;:Swatch`<br>Where `:Swatch` is appended to the asset request.<br><br>**Using color swatches**<br>To use color swatches, you make a `req=userdata` request with the following:<br>`/is/image/&lt;company_name&gt;/&lt;swatch_asset_name&gt;:Swatch?req=userdata`<br><br>For example, the following is a swatch asset in Dynamic Media Classic:<br>`https://my.company.com:8080/is/image/DemoCo/Sleek:Swatch`<br>And here is the swatch asset's corresponding `req=userdata` URL:<br>`https://my.company.com:8080/is/image/DemoCo/Sleek:Swatch?req=userdata`<br>The `req=userdata` response is as follows:<br>`SmartCropDef=Swatch`<br>`SmartCropHeight=200.0`<br>`SmartCropRect=0.421671,0.389815,0.0848564,0.0592593,200,200`<br>`SmartCropType=Swatch`<br>`SmartCropWidth=200.0`<br>`SmartSwatchColor=0xA56DB2`<br>You can also request a `req=userdata` response in either XML or JSON format, as in the following respective URL examples:<br>&bull;`https://my.company.com</code>:8080/is/image/DemoCo/Sleek:Swatch?req=userdata,json`<br>&bull;`https://my.company.com:8080/is/image/DemoCo/Sleek:Swatch?req=userdata,xml`<br><br>**Note**: You must create your own WCM component to request a color swatch and parse the `SmartSwatchColor` attribute, represented by a 24-bit RGB hexadecimal value.<br>See also [`userdata`](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/req/r-userdata) in the Viewers Reference Guide. |
| **[!UICONTROL Preserve crop content across target resolutions]** | To maintain crop content across the same aspect ratio | Use when you create a smart crop profile.<br>To generate new crop content &ndash; while still maintaining the focal point &ndash; for a given aspect ratio across different resolutions, uncheck this option <br>If you decide to uncheck this box, make sure that the original image resolution is greater that the resolutions that you define for your smart crop profile.<br><br>As an example, suppose you have set the aspect ratios at 600 x 600 (Large), 400 x 400 (Medium), and 300 x 300 (Small).<br>When **[!UICONTROL Preserve crop content across target resolutions]** option is *checked*, you see the same crop across all three resolutions, similar to the following sample output of images (for illustrative purposes only):<br>![Option checked](/help/assets/dynamic-media/assets/preserve-checked.png)<br><br>When **[!UICONTROL Preserve crop content across target resolutions]** option is *unchecked*, the crop content is new for all three resolutions, similar to the following sample output of images (for illustrative purposes only):<br>![Option unchecked](/help/assets/dynamic-media/assets/preserve-unchecked.png) |

### Supported image file formats for Smart Crop and Color Swatches

The maximum supported input file size resolution is 16K.

>[!NOTE]
>
>16K resolution is a display resolution with approximately 16,000 pixels horizontally. The most commonly discussed 16K resolution is 15360 × 8640, which doubles the pixel count of 8K UHD in each dimension, for a total of four times as many pixels. This resolution has 132.7 megapixels, 16 times as many pixels as 4K resolution and 64 times as many pixels as 1080p resolution.

| Image format | Case-insensitive file extension | MIME type | Supported input color space | Maximum supported input file size | Supported image format? |
| --- | --- | --- | --- | --- | --- |
| BMP | `.bmp` | image/bmp | sRGB | 4 GB | Yes |
| CMYK | | | | | Yes |
| EPS | | | | | No |
| GIF | `.gif` | image/gif | sRGB | 15 GB | Yes; the first frame of the animated GIF is used for the rendition. You cannot configure or change the first frame. |
| JPEG | `.jpg` and `.jpeg` | image/jpeg | sRGB | 15 GB | Yes |
| PNG | `.png` | image/png | sRGB | 15 GB | Yes |
| PSD | `.psd` | image/vnd.adobe.photoshop | sRGB<br>CMYK | 2 GB | Yes |
| SVG | | | | | No |
| TIFF | `.tif` and `.tiff` | image/tiff | sRGB<br>CMYK | 4 GB | Yes |
| WebP/Animated WebP | | | | | No |

## Create Dynamic Media Image Profiles {#creating-image-profiles}

To define advanced processing parameters for other asset types, see [Configuring Asset Processing](config-dm.md#configuring-asset-processing).

See [About Dynamic Media Image Profiles and Video Profiles](/help/assets/dynamic-media/about-image-video-profiles.md).

See also [Best Practices for Organizing your Digital Assets for using Processing Profiles](/help/assets/organize-assets.md).

**To create Dynamic Media Image Profiles:**

1. Select the Adobe Experience Manager logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Image Profiles]**.
1. To add an Image Profile, select **[!UICONTROL Create]**.
1. Enter a profile name, and values for unsharp mask, crop, or swatch, or both.

   >[!TIP]
   >
   >Use a profile name that is specific to its intended purpose. For example, suppose you want to create a profile that generates swatches only. That is, smart crop is disabled (turned off) and Color and Image Swatch is enabled (turned on). In such cases, you can use the profile name "Smart Swatch."

   See also [Smart Crop and Smart Swatch Options](#crop-options) and [Unsharp Mask](#unsharp-mask).

   ![crop](assets/crop.png)

1. Select **[!UICONTROL Save]**. The created profile appears in the list of available profiles.

## Edit or delete Dynamic Media Image Profiles {#editing-or-deleting-image-profiles}

1. Select the Experience Manager logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Image Profiles]**.
1. Select the Image Profile that you want to edit or remove. To edit it, select **[!UICONTROL Edit Image Processing Profile]**. To remove it, select **[!UICONTROL Delete Image Processing Profile]**.

   ![chlimage_1-254](assets/chlimage_1-254.png)

1. If editing, save the changes. If deleting, confirm that you want to remove the profile.

## Apply a Dynamic Media Image Profile to folders {#applying-an-image-profile-to-folders}

When you assign an Image Profile to a folder, any subfolders automatically inherit the profile from its parent folder. As such, you can assign only one Image Profile to a folder. As such, consider carefully the folder structure of where you upload, store, use, and archive assets.

If you assigned a different Image Profile to a folder, the new profile overrides the previous profile. The previously existing folder assets remain unchanged. The new profile is applied on the assets that are added to the folder later.

Folders with an assigned profile display the profile's name in the card.

<!-- When you add smart crop to an existing Image Profile, you need to re-trigger the [DAM Update Asset workflow](assets-workflow.md) if you want to generate crops for existing assets in your asset repository. -->

You can apply Image Profiles to specific folders or globally to all assets.

You can reprocess assets in a folder that already has an existing Image Profile that you later changed. See [Reprocess assets in a folder after you have edited its processing profile](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

### Apply Dynamic Media Image Profiles to specific folders {#applying-image-profiles-to-specific-folders}

You can apply an Image Profile to a folder from within the **[!UICONTROL Tools]** menu or if you are in the folder, from **[!UICONTROL Properties]**.

Folders with an assigned profile display the profile's name directly below the folder name.

You can reprocess assets in a folder that already has an existing video profile that you later changed. See [Reprocess assets in a folder after you have edited its processing profile](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

#### Apply Dynamic Media Image Profiles to folders from Profiles user interface {#applying-image-profiles-to-folders-from-profiles-user-interface}

1. Select the Experience Manager logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Image Profiles]**.
1. Select the Image Profile that you want to apply to a folder or multiple folders.

   ![chlimage_1-255](assets/chlimage_1-255.png)

1. Select **[!UICONTROL Apply Processing Profile to Folders]** and select the folder or multiple folders you want to use to receive the newly uploaded assets and select **[!UICONTROL Apply]**. Folders with an assigned profile display the profile's name directly below the folder name.

#### Apply Dynamic Media Image Profiles to folders from Properties {#applying-image-profiles-to-folders-from-properties}

1. Select the Experience Manager logo and navigate to **[!UICONTROL Assets]**.
1. Navigate to a *folder* (not an asset) to which you want to apply an Image Profile.
1. Depending on the view you are in, do one of the following:
   * In Card View, hover the pointer on the folder, then select the check mark to select it.
   * In Column View or List View, select the check box to the left of the folder name.
1. On the toolbar, select **[!UICONTROL Properties]**.
1. Select the **[!UICONTROL Dynamic Media Processing]** tab.
1. Under **[!UICONTROL Image Profile]**, from the **[!UICONTROL Profile Name]** drop-down list, select the profile to apply.
1. Near the upper-right corner of the page, select **[!UICONTROL Save & Close]**. Folders with an assigned profile display the profile's name directly below the folder name.

   ![chlimage_1-256](assets/chlimage_1-256.png)

### Apply a Dynamic Media Image Profile globally {#applying-an-image-profile-globally}

In addition to applying a profile to a folder, you can also apply one globally. Any content uploaded into Experience Manager Assets in any folder has the selected profile applied.

You can reprocess assets in a folder that already has an existing video profile that you later changed. See [Reprocess assets in a folder after you have edited its processing profile](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

**To apply a Dynamic Media Image Profile globally:**

1. Do one of the following:

    * Navigate to `https://&lt;AEM server&gt;/mnt/overlay/dam/gui/content/assets/foldersharewizard.html/content/dam` and apply the appropriate profile and select **[!UICONTROL Save]**.

      ![chlimage_1-257](assets/chlimage_1-257.png)

    * Navigate to CRXDE Lite to the following node: `/content/dam/jcr:content`.

      Add the property `imageProfile:/conf/global/settings/dam/adminui-extension/imageprofile/<name of image profile>` and select **[!UICONTROL Save All]**.

      ![configure_image_profiles](assets/configure_image_profiles.png)

## Edit the smart crop or smart swatch of a single image {#editing-the-smart-crop-or-smart-swatch-of-a-single-image}

>[!IMPORTANT]
>
>Adobe recommends that you review any generated smart crops and smart swatches to ensure that they are appropriate and relevant to your brand and values.

To refine the focal point of an image, you can manually adjust the alignment or resize the smart crop window.

After you edit a smart crop and save, the change is propagated everywhere you use the crop for the specific images.

>[!IMPORTANT]
>
>When you manually adjust the smart crop window of an asset, your changes are saved. These edits remain intact even if you reprocess the asset later. However, if you edit the width, height, or both in the **[!UICONTROL Responsive Image Crop]** area of the Image Profile, then that asset is subject to reprocessing.
>See [Reprocess Dynamic Media assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

Rerun smart crop to generate the additional crops again, if necessary.

See also [Edit the smart crop or smart swatch of multiple images](#editing-the-smart-crop-or-smart-swatch-of-multiple-images).

**To edit the smart crop or smart swatch of a single image:**

1. Select the Experience Manager logo and navigate to **[!UICONTROL Assets]**, then to the folder that has a smart crop or smart swatch Image Profile applied to it.
1. To open its contents, select the folder.
1. Select the image whose smart crop or smart swatch that you want to adjust.
1. In the toolbar, select **[!UICONTROL Smart Crop]**.

   >[!TIP]
   >
   >Use the hot key `s` to edit the smart crops or smart swatches.

1. Do any of the following:

    * Near the upper-right corner of the page, drag the slider bar left or right to increase or decrease the image display, respectively.
    * On the image, drag a corner handle to adjust the size of the viewable area of the crop or swatch.
    * On the image, drag the box/swatch to a new location. You can only edit image swatches; color swatches are static.
    * Near the upper-right corner of the image, select **[!UICONTROL Revert]** to undo all your edits and restore the original crop or swatch.
    * Use the keyboard arrow keys to crop the frame size, or reposition the image, or both. 

1. Near the upper-right corner of the page, select **[!UICONTROL Save]**, then select **[!UICONTROL Close]** to return to the folder of assets.

## Edit the smart crop or smart swatch of multiple images {#editing-the-smart-crop-or-smart-swatch-of-multiple-images}

>[!IMPORTANT]
>
>Adobe recommends that you review any generated smart crops and smart swatches to ensure that they are appropriate and relevant to your brand and values.

After you apply an Image Profile &ndash; containing smart crop &ndash; to a folder, all images in that folder have a crop applied to them. If needed, you can manually adjust the alignment or resize the smart crop window on multiple images to fine-tune their focal points further.

After you edit a smart crop and save, the change is propagated everywhere you use the crop for the specific images.

>[!IMPORTANT]
>
>When you manually adjust the smart crop window of multiple assets, your changes are saved. These edits remain intact even if you reprocess the assets later. However, if you edit the width, height, or both in the **[!UICONTROL Responsive Image Crop]** area of the Image Profile, then those assets are subject to reprocessing.
>See [Reprocess Dynamic Media assets in a folder](/help/assets/dynamic-media/about-image-video-profiles.md#reprocessing-assets).

Rerun smart crop to generate the additional crops again, if necessary.

**To edit the smart crop or smart swatch of multiple images:**

1. Select the Experience Manager logo and navigate to **[!UICONTROL Assets]**, then to a folder that has a smart crop or smart swatch Image Profile applied to it.
1. On the folder, select the **[!UICONTROL More Actions]** (...) icon, then select **[!UICONTROL Smart Crop]**.

1. On the **[!UICONTROL Edit Smart Crops]** page, do any of the following:

    * Adjust the viewing size of images on the page.

      To the right of the breakpoint name drop-down list, drag the slider bar left or right to change the size of the viewable image display.

       ![edit_smart_crops-sliderbar](assets/edit_smart_crops-sliderbar.png)

    * Filter the list of viewable images based on breakpoint names. In the example below, the images are filtered on the breakpoint name "Medium."

      Near the upper-right corner of the page, from the drop-down list, select a breakpoint name to filter on what images you see. (See the image above.)

       ![edit_smart_crops-dropdownlist](assets/edit_smart_crops-dropdownlist.png)

    * Resize the smart crop box. Do any one of the following:

        * If the image has a smart crop or a smart swatch only, on the image, drag the corner handle of the crop box. Adjust the size of the viewable area of the crop.
        * If the image has both a smart crop and a smart swatch, on the image, drag the corner handle of the crop box. Adjust the size of the viewable area of the crop. Or, select the smart swatch below the image (color swatches are static), then drag the corner handle of the crop box. Adjust the size of the viewable area of the swatch.

       ![Resizing the smart crop of an image](assets/edit_smart_crops-resize.png).

    * Move the smart crop box. Do any one of the following:

        * If the image has a smart crop or a smart swatch only, on the image, drag the crop box to a new location.
        * If the image has both a smart crop and a smart swatch, on the image, drag the smart crop box to a new location. Or, select the smart swatch below the image (color swatches are static), then drag the smart swatch crop box to a new location.

       ![edit_smart_crops-move](assets/edit_smart_crops-move.png)

    * Undo all your edits and restore the original smart crop or smart swatch (applies to the current editing session only).

      Select **[!UICONTROL Revert]** above the image.

       ![edit_smart_crops-revert](assets/edit_smart_crops-revert.png)

1. Near the upper-right corner of the page, select **[!UICONTROL Save]**, then select **[!UICONTROL Close]** to return to the folder of assets.

## Remove an Image Profile from folders {#removing-an-image-profile-from-folders}

When you remove an Image Profile from a folder, any subfolders automatically inherit the removal of the profile from its parent folder. However, any processing of files that has occurred within the folders remains intact.

You can remove an Image Profile from a folder from within the **[!UICONTROL Tools]** menu or if you are in the folder, from **[!UICONTROL Properties]**.

### Remove Dynamic Media Image Profiles from folders by way of Profiles user interface {#removing-image-profiles-from-folders-via-profiles-user-interface}

1. Select the Experience Manager logo and navigate to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Image Profiles]**.
1. Select the Image Profile that you want to remove from a folder or multiple folders.
1. Select **[!UICONTROL Remove Processing Profile from Folders]** and select the folder or multiple folders you want to use to remove the profile from and select **[!UICONTROL Remove]**.

    You can confirm that the Image Profile is no longer applied to a folder because the name no longer appears below the folder name.

### Remove Dynamic Media Image Profiles from folders by way of Properties {#removing-image-profiles-from-folders-via-properties}

1. Select the Experience Manager logo and navigate **[!UICONTROL Assets]** and then to the folder that you want to remove an Image Profile from.
1. On the folder, select the check mark to select it, then select **[!UICONTROL Properties]**.
1. Select the **[!UICONTROL Image Profiles]** tab.
1. From the **[!UICONTROL Profile Name]** drop-down list, select **[!UICONTROL None]**, then select **[!UICONTROL Save & Close]**.

    Folders with an assigned profile display the profile's name directly below the folder name.
