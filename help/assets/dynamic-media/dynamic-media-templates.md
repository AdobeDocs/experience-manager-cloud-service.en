---
title: How to manage Dynamic Media templates?
description: Learn how to create Dynamic Media templates using a WYSIWYG template editor and include multiple images and text layers to quickly create banners and flyers and use them in downstream applications.
role: User
---
# Dynamic Media templates{#dynamic-media-templates}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|-----|

Create Dynamic Media templates using a WYSIWYG template editor and include multiple images and text layers to quickly create banners and flyers and use them in downstream applications. You can also add parameters to the images and text layers included in the template and use [Dynamic Media URLs](https://experienceleague.adobe.com/en/docs/commerce-admin/content-design/wysiwyg/storage/catalog-urls-dynamic-media) to update the values for those layers in real-time.

Some of the key features include:

* **Dynamic Media WYSIWYG Template Editor:** Create customizable banners with image and text layers. 
* **Layer Parameterization:** Define dynamic key-value pairs for layers to enable real-time updates.
* **Dynamic Media URL Support:** Use Dynamic Media URLs for templates, integrating personalized values from 1st or third party applications.
* **Layer Visibility Control:** Dynamically hide or show layers as needed.
* **Smart Text Resizing:** Automatically adjust text size to fit designated areas.

Some of the key benefits of Dynamic Media templates include:

* **Optimize 1:1 Personalization:** Tailor content to real-time customer signals.
* **Reduce Manual Effort:** Automate and accelerate content creation and management.
* **Ensure Consistent Omnichannel Experiences:** Maintain brand consistency across channels.
* **Reuse Content Effectively:** Avoid single-use content and scale with dynamic, parameterized templates.
* **Mitigate Risks:** Update pricing, discounts, and links in real-time.
* **Enhance Customer Engagement:** Drive interactive, contextually relevant experiences..

>[!NOTE]
>
>Customers with subscriptions to the Enhanced Security SKU cannot use any Dynamic Media capabilities, including Dynamic Media Templates, on that Cloud Services program.

## Before you begin{#prerequisites-for-dynamic-media-wysiwyg-template}

To create a Dynamic Media template, you must have:

1. Access to Dynamic Media.
1. [Synced the images available in your AEM Assets instance with Dynamic Media to use them for creating the template](/help/assets/dynamic-media/config-dm.md).

## Create Dynamic Media WYSIWYG template{#how-to-create-dynamic-media-wysiwyg-template}

To create a DM template, follow these steps:

1. [Create a blank canvas](#create-a-canvas)
1. [Add images to the canvas](#add-images-to-the-canvas)
1. [Add text layers to the canvas](#add-text-to-the-canvas)
1. [Edit or delete a layer](#edit-or-delete-a-layer)
1. [Parameterise layers](#parameterise-a-layer)


### Create a blank canvas{#create-a-canvas}

Execute these steps to create a blank canvas:

1. Navigate to Assets View and click **Dynamic Media Assets** available in the left panel.

   ![](/help/assets/assets/dm-templates/DM-Assets1.png)

1.  Click **Create Template** to save the template under Dynamic Media Assets or navigate to a folder and click **Create Template** to save the template within that folder. The **New Template** dialog box displays.
![](/help/assets/assets/dm-templates/new-template.png)
To [create a folder](/help/assets/add-delete-assets-view.md) under **Dynamic Media Assets**, create a folder under **Assets**. The folder tree under **Assets** replicates under **Dynamic Media Assets**. 
1. Specify a template name, define the canvas width and height, and click **Create**. A blank canvas displays with menu options on both sides to use for creating the template. Hover over the menu options to see their tooltip. 
![](/help/assets/assets/dm-templates/blank-canvas-page.png)

>[!NOTE]
>
> The allowed width and height range is from 50 to 5000.

**Menu options on the right pane:** Use these options to add the necessary images and text layers to the canvas.

* ![](/help/assets/assets/dm-templates/add-image.svg): Click to add images to the canvas.
* ![](/help/assets/assets/dm-templates/add-text.svg): Click to add texts to the canvas.
* ![](/help/assets/assets/dm-templates/show-layers-list.svg): Click to see the list of all layers (image and text) on the canvas. Every image and text added to the canvas is represented as a separate layer.

**Menu options on the left pane:** Use these options for common editor actions as mentioned below.

* ![](/help/assets/assets/dm-templates/layer-selector.svg): Select a layer.
* ![](/help/assets/assets/dm-templates/bring-forward.svg): Click to bring a selected layer forward or press **Ctrl** + **]** (Windows) or **Cmd** + **]** (Mac).
* ![](/help/assets/assets/dm-templates/send-backward.svg): Click to send a selected layer backward or press **Ctrl** + **[** (Windows) or **Cmd** + **[** (Mac).
* ![](/help/assets/assets/dm-templates/undo.svg): Click to undo the last action or press **Ctrl** + **Z** (Windows) or **Cmd** + **Z** (Mac).
* ![](/help/assets/assets/dm-templates/redo.svg): Click to redo the last action or press **Ctrl** + **Y** (Windows) or **Cmd** + **Y** (Mac).
* ![](/help/assets/assets/dm-templates/zoomin.svg): Click to zoom in the canvas or press **Ctrl** + **+** (Windows) or Cmd + **+** (Mac).
* ![](/help/assets/assets/dm-templates/zoomout.svg): Click to zoom out the canvas or press **Ctrl** + **-** (Windows) or **Cmd** + **-** (Mac).
* Press **Backspace** or **delete** to delete the selected layer if no text or property is being edited.

Click ![](/help/assets/assets/dm-templates/show-layers-list.svg) and more options (![](/help/assets/assets/dm-templates/three-dots.svg)) on the Canvas layer to edit the canvas dimensions anytime while creating the template.
![](/help/assets/assets/dm-templates/edit-canvas1.png)

   >[!NOTE]
   >
   > Templates allow a maximum of 20 layers, including the Canvas.

### Add images to the canvas{#add-images-to-the-canvas}

Execute these steps to add images to the canvas:

1. Click ![](/help/assets/assets/dm-templates/add-image.svg) to display the [Asset Selector](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/asset-selector/overview-asset-selector) panel. The panel displays the images in your AEM Assets instance that are synced to Dynamic Media. 
1. Browse the panel or use keywords in the search bar to find a specific image.
1. Drag and drop an image on the canvas to use it. See the [Properties panel](#4) for resizing or repositioning a layer on the canvas.
![](/help/assets/assets/dm-templates/add-image-to-canvas.png)

### Add text layers to the canvas{#add-text-to-the-canvas}

Execute these steps to add text layers to the canvas:

1. Click ![](/help/assets/assets/dm-templates/add-text.svg) to add a text layer to the canvas and open the Properties panel. 
1. Select the layer and click the text to update it. 
1. Enable **Smart Text Resize** in the Properties panel to  adjust the text length and font size automatically to fit in the designated area optimally. 
![](/help/assets/assets/dm-templates/add-text-layer.png)

See the [Properties panel](#4) to reposition, resize, rotate or delete the layer. Format your text to your desired font, size, color, style, alignment (in the layer) by changing their values in the respective fields under the **Text** section of the panel.

   >[!NOTE]
   >
   > To use a font other than the default Arial font family, you need to upload and publish the font file to AEM Assets and Dynamic Media. If you have some old fonts in your instance, ensure to [reprocess](/help/assets/reprocessing-assets-view.md) to view them in the Template editor.

### Edit or delete a layer {#edit-or-delete-a-layer}

Execute these steps to edit or delete a canvas layer:

1. Click ![](/help/assets/assets/dm-templates/show-layers-list.svg) and select the layer either on the canvas or from the Layers list.
1. Click **more options** (![](/help/assets/assets/dm-templates/three-dots.svg)) to edit or delete the layer. 
1. Click **Delete** to delete the layer. 
1. Click **Edit** to edit the layer using the [Properties panel](#4).
![](/help/assets/assets/dm-templates/edit-delete-layer.png)

### Properties Panel{#properties-panel}

To navigate to a layer's properties panel:

1. Click ![](/help/assets/assets/dm-templates/show-layers-list.svg).
1. Select the layer from the list. 

This panel displays the position of the layer's center point on the canvas plane (X and Y values) and layer's dimensions (width and height) along with text formatting options.

![](/help/assets/assets/dm-templates/properties-panel.png)

From the properties panel of a layer, select another layer on the canvas to navigate to its properties panel.
<a id="4"></a> 

#### Reposition, resize, rotate or delete a layer{#reposition-resize-delete-a-layer}

See these common layer editing actions to edit a text or an image layer:

* **Reposition the layer:** Drag the layer to move it anywhere on the canvas. This action updates the X and Y values in the properties panel.
* **Resize the layer:** Select the layer and drag its edge handles to resize it. This action updates the W (width) and H (height) values in the properties panel.
* **Rotate the layer:** Drag the square handle placed vertically above the layer to rotate it around its center. This action updates the angle values in the properties panel. 
* **Delete the layer:** Press **Backspace** or **delete** and then click **Confirm** to delete a selected layer.

#### Text formatting options{#text-formatting-options-on-properties-panel}

Format your text to your desired font, size, color, style, alignment (in the layer) by changing their values in the respective fields under the **Text** section of the panel.

**Smart Text Resize:** Ensure to include **Smart Text Resize** ([Copyfitting](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/text-formatting/r-copy-fitting)) to fit any text in the designated area optimally by adjusting its font size and length smartly. This capability prevents text overflow or minimizes extra spaces at the bottom of the text.
![](/help/assets/assets/dm-templates/smart-text-resize.png)

### Parameterise layers {#parameterise-a-layer}

After creating a template with multiple layers of images and texts, parameterise the selected layers. When a layer or its property is parameterised, it gets a key-value pair (also called as parameter). This parameter can be included in the template URL to update the layer's position, size or content in real time resulting in template customisation in no time.

To parameterise a layer: <a id="1"></a> 

1. click ![](/help/assets/assets/dm-templates/show-layers-list.svg), select a layer and click **Parameters**. The **Parameters** panel displays.
1. Toggle **Include Parameter** to parameterise a property. See [this](#parameterisation-options-or-allowed-parameters) to know the property's behaviour after parameterisation.
1. **Optional:** Rename the parameter name. A parameter name has layer name followed by a suffix. For a selected layer all its parameterized properties share the same layer name followed by a varying suffix. Rename the layer name by following the semantic naming convention so that when you include the parameter in the URL, the parameter name self explains about the layer's content or its purpose.
1. Click **Save**.
![](/help/assets/assets/dm-templates/parameterise-a-layer.png)
To switch between the Parameter panel of an image and text layer,  select the layer on the canvas and click **Parameters**.

#### Parameters panel option {#parameterisation-options-or-allowed-parameters} 

The parameterised properties can be included as URL parameters in the template URL to edit the template in real time using the URL. 

**Image parameters:**

**X:** Include to move the layer horizontally along its centreline, parallel to the X-axis of the template plane, by changing the parameter's value in the URL.
**Y:** Include to move the layer vertically along its centre line, parallel to the Y-axis of the template plane, by changing the parameter's value in the URL. 
**Width:** Include to adjust the layer's width by changing the parameter's value in the URL.
**Height:** Include to adjust the layer's height by changing the parameter's value in the URL.
**Hide:** Include to hide or show the layer in the template using 0 (show) and 1 (hide).
**Source:** Include to replace the layer's image with new image by changing the image path in the parameter's value in the URL.

**Text formatting parameters:**

Include the below parameters to edit the text, its font, colour and size from the URL by updating the parameter values in the URL.

**Text:** Include to update text from the URL.
**Font Family:** Include to update the text's font from the URL.
**Font Size:** Include to update the text's font size from the URL.
**Text color:** Include to update the text's font color from the URL.

### Group layers to control their visibility simultaneously{#group-layers}

Another way to keep your templates flexible, is by utilising a single parameter name to control multiple layers. This strategy is helpful for the visibility (hide or show layers) parameter, to update the design or graphics from a single template.

Follow these steps to assign the same name to the hide parameters (![](/help/assets/assets/dm-templates/Visibility-icon.svg)) of multiple layers, allowing you to hide or show them simultaneously.

1. Navigate to the [Parameters panel](#1) of a layer.
1. Toggle the **Hide** Parameter if not parameterised earlier.
1. **Optional:** Rename the Hide Parameter.
1. Copy the Hide Parameter name. 
1. Go to the Parameter panel of other layers by selecting them from the canvas and toggle their **Hide** Parameter if not parameterised.
1. Replace their **Hide Parameter** name with the copied name.
1. Click **Save** to group the layers. 
1. Execute step 3 and then 4 in [Preview and Publish](#2) section to see your changes. 

## Preview and publish the template to copy the delivery URL{#preview-and-publish-template-and-copy-template-deliver-url}

Execute these steps to preview and publish the template and copy the delivery URL:

1. On the canvas page, click **Preview**. You can also navigate to **Assets View > Dynamic Media Assets >** find and select your template **>** click **Edit Template >** click **Preview**. The preview page displays the template, its parameters (parameterized layers and properties), publish status, and the **Publish** option. <a id="3"></a> 
1. Select parameters from **Template Parameters** panel to edit their values and instantly update the content, size, position, or text formatting of the corresponding template layer in the preview. For example: 
   1. Select a text layer and edit its text or 
   1. Select an image layer, click ![](/help/assets/assets/dm-templates/add-image.svg), select an image from the asset selector, and click **Refresh**. 

   The template updates immediately, displaying the edited text and replacing the previous image with the new one. Additionally, the image parameter value reflects the new image path. Similarly, you can resize a layer by adjusting its values, and the changes are applied to the template in real time. <a id="2"></a>  
1. Select only one **Hide Parameter** from the duplicates when multiple layers are grouped under the same Hide Parameter. 
1. **Optional:** Change the **Hide Parameter** value between 0 and 1 and click **Refresh** to see the changes. Layers with the same hide parameter hides or displays together. Similarly, you can control the layers' visibility from the URL.

   ![](/help/assets/assets/dm-templates/preview-publish-copy-delivery-url.png)
   You can also toggle **Include all parameters** to edit all of the displayed parameter values and see the updates in the template preview.
   <br>
1. To publish the template on the preview page, click **Publish** and confirm to publish. Publish Complete message displays and the publish status updates to Published.

 >[!NOTE]
 >
 >Publishing the template requires the template images to be published first.

### Copy the delivery URL

The selected parameters on the **Preview** page become the URL parameters in the template URL.

To copy the URL of the published template displayed in preview:

1. Click **Copy URL**. The **Copy URL** dialog box displays. Select and copy the displayed URL. Observe that the first parameter in the URL starts after a question mark **(?)** and a key-value pair starts with **$** and ends with **&**. The key and value are separated by an equals sign **(=)**, with the key on the left and the value on the right. 
1. Paste this URL in your browser tab and see your live template. Customize the template in real time by updating the required parameter's value (Key's value) in the URL directly as demonstrated in [step 2](#3) of **Preview and Publish** section.  
1. Use this URL for rapid merchandising of your products or services. You can share this URL with your customers or integrate it into your website or any downstream third-party application to display the banner and make real-time updates to it to reflect the ongoing offers.

## Make real-time updates to the template from the URL{#update-the-template-from-the-url}

Editing parameters directly in the URL can be tedious. To simplify: 

1. Copy the URL and paste it into a notepad. 
1. Use Cmd+F (Mac) or Ctrl+F (Windows) to find and edit the parameter values. Such as:
   * Replace image paths for image layers.
   * Adjust layer dimensions and positions (if [parameterized](#parameterise-a-layer)). 
   * Edit text, font, color, size, or alignment for text layers. 
   * Change visibility values between 0 and 1. 

Paste this updated URL in your browser to view the changes. 

## Edit the template{#edit-the-template}

Edit the template by following these steps:

1. On the Assets view, click **Dynamic Media Assets**.
2. Navigate to the template location.
3. Select the template.
4. Click **Edit Template**. The template canvas displays the template and the list of all its layers in the Layers panel. Start to edit your template as per the requirements.

## Important points to note {#important-points-to-note}

* After creating a template with parameterized image layers for dynamic updates, ensure that the images intended for future updates share the same dimensions as the parameterized images. This ensures the images fit perfectly within the layers without overflowing or leaving empty spaces. Currently, the template does not support automatic dimension adjustments to fit images into the layers.
* References for all image assets used in the template are added to the template. This results in:
   * Display of a warning message while deleting an associated asset.
   * Publishing all associated assets while publishing the template.
* There is no substring support in a text layer. User cannot apply different font properties on substring of a text layer.
* Support of multiple Dynamic Media companies is not currently available with Dynamic Media Templates.
* In case of copy or move, Destination Selector shows all the folders (including non-Dynamic Media synced folders). Also, currently, it does not display the Dynamic Media Template assets (both of these are limitations of destination selector).
* Any update operation on a folder (for example, Publish or Delete) from Assets section impacts the Dynamic Media Templates available within that folder. 
* Trash does not work for Dynamic Media Templates. If an asset is moved to trash and then restored, the asset is restored in AEM but not on Dynamic Media. The same is valid for Dynamic Media Templates.

## See also

1. Explore [Dynamic Media and its capabilities](/help/assets/dynamic-media/dynamic-media.md)
1. Explore [Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)