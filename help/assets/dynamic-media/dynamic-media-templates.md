---
title: How to manage [!DNL Dynamic Media] templates?
description: Learn how to create [!DNL Dynamic Media] templates using a WYSIWYG template editor and include multiple images and text layers to quickly create banners and flyers and use them in downstream applications.
hide: yes
role: User
exl-id: 07de648e-4ae2-4524-8e05-3cf10bb6006d
---
# [!DNL Dynamic Media] templates{#dynamic-media-templates}

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

Create real time customizable templates for your banners and flyers using [!DNL Dynamic Media] templates, a WYSIWYG template editor. Use your [!DNL Dynamic Media] template in downstream applications. A [!DNL Dynamic Media] template includes image and text layers. Add parameters to the image and text layers of the template and use [[!DNL Dynamic Media] URLs](https://experienceleague.adobe.com/en/docs/commerce-admin/content-design/wysiwyg/storage/catalog-urls-dynamic-media) to reposition and resize the layer and update its content in real-time. 

Some of the key features include:

* **[!DNL Dynamic Media] WYSIWYG Template Editor:** Create customizable banners with image and text layers. 
* **Layer Parameterization:** Define dynamic key-value pairs for layers to enable real-time updates.
* **[!DNL Dynamic Media] URL Support:** Use [!DNL Dynamic Media] URLs for templates, integrating personalized values from 1st or third party applications.
* **Layer Visibility Control:** Dynamically hide or show layers as needed.
* **Smart Text Resizing:** Automatically adjust text size to fit designated areas.

Some of the key benefits of [!DNL Dynamic Media] templates include:

* **Optimize 1:1 Personalization:** Tailor content to real-time customer signals.
* **Reduce Manual Effort:** Automate and accelerate content creation and management.
* **Ensure Consistent Omnichannel Experiences:** Maintain brand consistency across channels.
* **Reuse Content Effectively:** Avoid single-use content and scale with dynamic, parameterized templates.
* **Mitigate Risks:** Update pricing, discounts, and links in real-time.
* **Enhance Customer Engagement:** Drive interactive, contextually relevant experiences.

>[!NOTE]
>
>Customers with subscriptions to the Enhanced Security SKU cannot use any [!DNL Dynamic Media] capabilities, including [!DNL Dynamic Media] Templates, on that Cloud Services program.

## Before you begin{#prerequisites-for-dynamic-media-wysiwyg-template}

To create a [!DNL Dynamic Media] template, you must have:

1. Access to [!DNL Dynamic Media].
1. [Synced the images available in your [!DNL AEM Assets] instance with [!DNL Dynamic Media] to use them for creating the template](/help/assets/dynamic-media/config-dm.md).
1. verified the following in the Touch UI:
   * On the **[!UICONTROL Edit [!DNL Dynamic Media] Configuration page]**, **[!UICONTROL [!DNL Dynamic Media] sync mode]** that is set to **[!UICONTROL Disabled by default]**, is not applied to all AEM folders (**[!UICONTROL Sync all content]** is unchecked). See [configuring Dynamic Media Cloud Service](/help/assets/dynamic-media/config-dm.md) for more information.
   * **[!UICONTROL [!DNL Dynamic Media] sync mode]** is set to **[!UICONTROL Enable for subfolders]** for the destination folder or subfolder where you will save the template after creation. See [configuring [!DNL Dynamic Media] Cloud Service](/help/assets/dynamic-media/config-dm.md) for more information.

## Create [!DNL Dynamic Media] WYSIWYG template{#how-to-create-dynamic-media-wysiwyg-template}

Execute the following steps to create a [!DNL Dynamic Media] template:

1. Navigate to your [!DNL Assets View] and [create a folder](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/assets-view/add-delete-assets-view) in ![Assets](/help/assets/assets/Asset-icon.svg)**[!UICONTROL Assets]**. The folder tree in ![Assets](/help/assets/assets/Asset-icon.svg)**[!UICONTROL Assets]** replicates in **[!UICONTROL Dynamic Media Assets]**. Save your [!DNL Dynamic Media] template in this [!UICONTROL Dynamic Media Assets] folder.
1. Select ![Assets](/help/assets/assets/Asset-icon.svg)**[!UICONTROL Assets]** and [upload and publish your images to [!DNL AEM] and [!DNL Dynamic Media] simultaneously](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/assets-view/publish-assets-to-aem-and-dm#dynamic-media-publish-mode-set-to-upon-activation) to use them for creating the template. 
1. [Create a blank canvas](#create-a-canvas)
1. [Add images to the canvas](#add-images-to-the-canvas)
1. [Add text layers to the canvas](#add-text-to-the-canvas)
1. [Edit or delete a layer](#edit-or-delete-a-layer)
1. [Parameterise layers](#parameterise-a-layer)

### Create a blank canvas{#create-a-canvas}

Execute these steps to create a blank canvas: 

1. Navigate to [!DNL Assets View], select **[!UICONTROL Dynamic Media Assets]** available in the left panel and navigate to your folder to save your template in that folder.

   ![Dynamic Media templates](/help/assets/assets/DM-Assets1.png)

1. Select **[!UICONTROL Create Template]**. The **[!UICONTROL New Template]** dialog box displays.
![how to create dynamic templates that can be customised in real time](/help/assets/assets/new-template.png)
   >[!NOTE]
   >
   >  The template is saved in the location where you create it. On [!DNL Assets View] home page, select **[!UICONTROL Dynamic Media Assets]** and click **[!UICONTROL Create Template]** to save the template in **[!UICONTROL Dynamic Media Assets]** root folder.
1. Specify a template name, define the canvas width and height, and click **[!UICONTROL Create]**. A blank canvas displays with menu options on both sides to use for creating the template. Hover over the menu options to see their tooltip. 
![real-time customizable template](/help/assets/assets/blank-canvas-page.png)

   >[!NOTE]
   >
   > The allowed width and height range is from 50 to 5000.

**Menu options on the right pane:** Use these options to add the necessary images and text layers to the canvas.

* ![DM Templates](/help/assets/assets/add-image.svg): Click to add images to the canvas.
* ![customizable templates](/help/assets/assets/add-text.svg): Click to add texts to the canvas.
* ![customizable templates](/help/assets/assets/show-layers-list.svg): Click to see the list of all layers (image and text) on the canvas. Every image and text added to the canvas is represented as a separate layer.

**Menu options on the left pane:** Use these options for common editor actions as mentioned below.

* ![DM Templates](/help/assets/assets/layer-selector.svg): Select a layer.
* ![templates that support customization](/help/assets/assets/bring-forward.svg): Click to bring a selected layer forward or press **Ctrl** + **]** (Windows) or **Cmd** + **]** (Mac).
* ![how to create a template that can be customized easily](/help/assets/assets/send-backward.svg): Click to send a selected layer backward or press **Ctrl** + **[** (Windows) or **Cmd** + **[** (Mac).
* ![create a template that can be customized instantly](/help/assets/assets/undo.svg): Click to undo the last action or press **Ctrl** + **Z** (Windows) or **Cmd** + **Z** (Mac).
* ![template to create banners rapidly](/help/assets/assets/redo.svg): Click to redo the last action or press **Ctrl** + **Y** (Windows) or **Cmd** + **Y** (Mac).
* ![template to create flyers rapidly](/help/assets/assets/zoom-in.svg): Click to zoom in the canvas or press **Ctrl** + **+** (Windows) or Cmd + **+** (Mac).
* ![template to create banners rapidly](/help/assets/assets/Zoom-out.svg): Click to zoom out the canvas or press **Ctrl** + **-** (Windows) or **Cmd** + **-** (Mac).
* Press **Backspace** or **delete** to delete the selected layer if no text or property is being edited.

Click ![template to create flyers rapidly](/help/assets/assets/show-layers-list.svg) **>** more options (![](/help/assets/assets/three-dots.svg)) on the Canvas layer to edit the canvas dimensions anytime while creating the template.
![](/help/assets/assets/edit-canvas1.png)

   >[!NOTE]
   >
   > Templates allow a maximum of 20 layers, including the Canvas.

### Add images to the canvas{#add-images-to-the-canvas}

Execute these steps to add images to the canvas:

1. Click ![create a banner in no time](/help/assets/assets/add-image.svg) to display the [Asset Selector](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/asset-selector/overview-asset-selector) panel. The panel displays the images in your AEM Assets instance that are synced to [!DNL Dynamic Media]. 
1. Browse the panel or use keywords in the search bar to find a specific image.
1. Drag and drop an image on the canvas to use it. See the [**[!UICONTROL Properties Panel]**](#reposition-resize-delete-a-layer) for resizing or repositioning a layer on the canvas.
![create a banner within seconds](/help/assets/assets/add-image-to-canvas.png)

### Add text layers to the canvas{#add-text-to-the-canvas}

Execute these steps to add text layers to the canvas:

1. Click ![creating new banners fastly](/help/assets/assets/add-text.svg) to add a text layer to the canvas and open the Properties panel. 
1. Select the layer and click the text to update it. 
1. Select **[!UICONTROL Smart Text Resize]** in the Properties panel to  automatically adjust the text length and font size to optimally fit in the designated area. 
![best customizable banners](/help/assets/assets/add-text-layer.png)

See the [**[!UICONTROL Properties Panel]**](#reposition-resize-delete-a-layer) to reposition, resize, rotate or delete the layer. Format your text to the required font, size, color, style, alignment (in the layer) by changing their values in the respective fields under the **[!UICONTROL Text]** section of the panel.

   >[!NOTE]
   >
   > To use a font other than the default Adobe Sans F2 font family, you need to upload and publish the font file to [!AEM Assets] and [!DNL Dynamic Media]. If you have some old fonts in your instance, ensure to [reprocess](/help/assets/reprocessing-assets-view.md) to view them in the Template editor.

### Edit or delete a layer {#edit-or-delete-a-layer}

Execute these steps to edit or delete a canvas layer:

1. Click ![templates with support to dynamic updates](/help/assets/assets/show-layers-list.svg) and select the layer either on the canvas or from the Layers list.
1. Click **[!UICONTROL more options]** (![templates with support to real-time updates](/help/assets/assets/three-dots.svg)) to edit or delete the layer. 
1. Click **[!UICONTROL Delete]** to delete the layer. 
1. Click **[!UICONTROL Edit]** to edit the layer using the [**[!UICONTROL Properties Panel]**](#reposition-resize-delete-a-layer).
![rapid banner creation](/help/assets/assets/dm-templates/edit-delete-layer.png)

### Properties Panel{#properties-panel}

To navigate to a layer's properties panel:

1. Click ![rapid content creation](/help/assets/assets/show-layers-list.svg).
1. Select the layer from the list. 

This panel displays the position of the layer's center point on the canvas plane (X and Y values) and the layer's dimensions (width and height) along with text formatting options.

![rapid content creation](/help/assets/assets/properties-panel.png)

From the properties panel of a layer, select another layer on the canvas to navigate to its properties panel.
 

#### Reposition, resize, rotate or delete a layer{#reposition-resize-delete-a-layer}

See these common layer editing actions to edit a text or an image layer:

* **Reposition the layer:** Drag the layer to move it anywhere on the canvas. This action updates the X and Y values in the properties panel.
* **Resize the layer:** Select the layer and drag its edge handles to resize it. This action updates the W (width) and H (height) values in the properties panel.
* **Rotate the layer:** Drag the square handle placed vertically above the layer to rotate it around its center. This action updates the angle values in the properties panel. 
* **Delete the layer:** Press **Backspace** or **delete** and then click **[!UICONTROL Confirm]** to delete a selected layer.

#### Text formatting options{#text-formatting-options-on-properties-panel}

Format your text to required font, size, color, style, alignment (within the layer) by changing their values in the respective fields under the **[!UICONTROL Text]** section on the panel.
Ensure to include **[!UICONTROL Smart Text Resize]**. [!UICONTROL Smart Text Resize] works on [Copyfitting](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/text-formatting/r-copy-fitting) algorithum to optimally fill text in the text area and prevents text overflow and minimizes extra space at the bottom of the text.

![content creation in no time](/help/assets/assets/smart-text-resize.png)

### Parameterise layers {#parameterise-a-layer}

After creating a template with multiple layers of images and texts, parameterise the selected layers. When a layer or its property is parameterised, it gets a key-value pair (also called as parameter). This parameter can be included in the template URL to update the layer's position, size or content in real time resulting in template customisation in no time.

To parameterise a layer:

1. click ![instant content creation](/help/assets/assets/show-layers-list.svg), select a layer and click **[!UICONTROL Parameters]**. The **[!UICONTROL Parameters]** panel displays.
1. Toggle **[!UICONTROL Include Parameter]** to parameterise a property. See [Parameters panel option](#parameterisation-options-or-allowed-parameters) to know the property's behaviour after parameterisation.
1. **Optional:** Rename the parameter name. A parameter name has layer name followed by a suffix. For a selected layer all its parameterized properties share the same layer name followed by a varying suffix. Rename the layer name by following the semantic naming convention so that when you include the parameter in the URL, the parameter name self explains about the layer's content or its purpose.
1. Click **[!UICONTROL Save]**.
![instant content creation](/help/assets/assets/parameterise-a-layer.png)
To switch between the Parameter panel of an image and text layer, select the layer on the canvas and click **[!UICONTROL Parameters]**.

#### Parameters panel option {#parameterisation-options-or-allowed-parameters} 

The parameterised properties can be included as URL parameters in the template URL to edit the template in real time using the URL. 

**Image parameters:**

**[!UICONTROL X]:** Include to move the layer horizontally along its centreline, parallel to the X-axis of the template plane, by changing the parameter's value in the URL.
**[!UICONTROL Y]:** Include to move the layer vertically along its centre line, parallel to the Y-axis of the template plane, by changing the parameter's value in the URL. 
**[!UICONTROL Width]:** Include to adjust the layer's width by changing the parameter's value in the URL.
**[!UICONTROL Height]:** Include to adjust the layer's height by changing the parameter's value in the URL.
**[!UICONTROL Hide]:** Include to hide or show the layer in the template using 0 (show) and 1 (hide).
**[!UICONTROL Source]:** Include to replace the layer's image with new image by changing the image path in the parameter's value in the URL.

**Text formatting parameters:**

Include the below parameters to edit the text, its font, colour and size from the URL by updating the parameter values in the URL.

**[!UICONTROL Text]:** Include to update text from the URL.
**[!UICONTROL Font Family]:** Include to update the text's font from the URL.
**[!UICONTROL Font Size]:** Include to update the text's font size from the URL.
**[!UICONTROL Text color]:** Include to update the text's font color from the URL.

### Group layers to control their visibility simultaneously{#group-layers}

Another way to keep your templates flexible, is by utilising a single parameter name to control multiple layers. This strategy is helpful for the visibility (hide or show layers) parameter, to update the design or graphics from a single template.

Follow these steps to assign the same name to the hide parameters (![fast content creation](/help/assets/assets/Visibility-icon.svg)) of multiple layers, allowing you to hide or show them simultaneously.

1. Navigate to the [**[!UICONTROL Properties Panel]**](#parameterise-a-layer) of a layer.
1. Toggle the **[!UICONTROL Hide]** Parameter if not parameterised earlier.
1. **Optional:** Rename the **[!UICONTROL Hide]** Parameter.
1. Copy the **[!UICONTROL Hide]** Parameter name. 
1. Go to the Parameter panel of other layers by selecting them from the canvas and toggle their **[!UICONTROL Hide]** Parameter if not parameterised.
1. Replace their **[!UICONTROL Hide parameter]** name with the copied name.
1. Click **[!UICONTROL Save]** to group the layers. 
1. Execute step 3 and then 4 in [**[!UICONTROL Preview and Publish]**](#preview-and-publish-template-and-copy-template-deliver-url) section to see your changes. 

## Preview and publish the template to copy the delivery URL{#preview-and-publish-template-and-copy-template-deliver-url}

Execute these steps to preview and publish the template and copy the delivery URL:

1. On the canvas page, click **[!UICONTROL Preview]**. You can also navigate to **[!UICONTROL Assets View]** **>** **[!UICONTROL Dynamic Media Assets]** **>** find and select your template **>** click **[!UICONTROL Edit Template]** **>** click **[!UICONTROL Preview]**. The preview page displays the template, its parameters (parameterized layers and properties), publish status, and the **[!UICONTROL Publish]** option.
1. Select parameters from **[!UICONTROL Template Parameters]** panel to edit their values and instantly update the content, size, position, or text formatting of the corresponding template layer in the preview. For example: 
   1. Select a text layer and edit its text or 
   1. Select an image layer, click ![creating content on the fly](/help/assets/assets/add-image.svg), select an image from the asset selector, and click **[!UICONTROL Refresh]**. 

   The template updates immediately, displaying the edited text and replacing the previous image with the new one. Additionally, the image parameter value reflects the new image path. Similarly, you can resize a layer by adjusting its values, and the changes are applied to the template in real time. 
1. Select the **[!UICONTROL Hide]** parameter for [grouped layers](#group-layers) from the list to show or hide them together in the template. 
1. **Optional:** Change the **[!UICONTROL Hide]** parameter value between 0 and 1 and click **[!UICONTROL Refresh]** to see the changes. Layers with the same **[!UICONTROL Hide]** parameter hides or displays together. Similarly, you can control the layers' visibility from the URL.

   ![creating content on the fly](/help/assets/assets/dm-templates-publish-status.png)
   You can also toggle **[!UICONTROL Include all parameters]** to edit all of the displayed parameter values and see the updates in the template preview.
   <br>
1. To publish the template on the preview page, click **[!UICONTROL Publish]**  and confirm to publish. **[!UICONTROL Publish Complete]** message displays and the publish status updates to **[!UICONTROL Published]**.

 >[!NOTE]
 >
 >Publishing the template requires the template images to be published first.

### Copy the delivery URL

The selected parameters on the **[!UICONTROL Preview]** page become the URL parameters in the template URL.

To copy the URL of the published template displayed in preview:

1. Click **[!UICONTROL Copy URL]**. The **[!UICONTROL Copy URL]** dialog box displays. Select and copy the displayed URL. The first parameter in the URL starts after a question mark **([!UICONTROL ?])** and a key-value pair starts with **[!UICONTROL $]** and ends with **[!UICONTROL &]**. The key and value are separated by an equals sign **([!UICONTROL =])**, with the key on the left and the value on the right. 
1. Paste this URL in your browser tab and see your live template. Customize the template in real time by updating the required parameter's value (Key's value) in the URL directly as demonstrated in [step 2](#preview-and-publish-template-and-copy-template-deliver-url) of **Preview and Publish** section.  
1. Use this URL for rapid merchandising of your products or services. You can share this URL with your customers or integrate it into your website or any downstream third-party application to display the banner and make real-time updates to it to reflect the ongoing offers.

Learn to create a [!DNL Dynamic Media] template step by step in this video.
>[!VIDEO](https://video.tv.adobe.com/v/3443281)

## Make real-time updates to the template from the URL{#update-the-template-from-the-url}

Editing parameters directly in the URL can be tedious. To simplify: 

1. Copy the URL and paste it into a notepad. 
1. Use Cmd+F (Mac) or Ctrl+F (Windows) to find and edit the parameter values. Such as:
   * Find and replace image paths for image layers.
   * Find layer's [parameterized](#parameterise-a-layer) coordinates, width and height, to adjust their values. 
   * Edit text, font, color, size, or alignment for text layers. 
   * Change visibility values between 0 and 1. 

Paste this updated URL in your browser to view the changes. 

## Edit the template{#edit-the-template}

Edit the template by following these steps:

1. On the [!DNL Assets view], click **[!UICONTROL Dynamic Media Assets]**.
2. Navigate to the template location.
3. Select the template.
4. Click **[!UICONTROL Edit Template]**. The template canvas displays the template and the list of all its layers in the Layers panel. Start editing your template as per your requirements.

## Add Call to Action (CTA) link to your template layer{#add-CTA-in-dynamic-media-templates}

Turn any image or text layer of your [!DNL Dynamic Media] template into a hyperlink by adding a CTA link to it that directs users to a target page. Execute these steps to add a CTA link to a layer:

1. Navigate to your template location, select the template and click ![edit](/help/assets/assets/edit-pen-icon.svg) **[!UICONTROL Edit Template]**. The template displays on the canvas.
1. Select the template layer and [navigate to its properties panel](#edit-or-delete-a-layer) to add a CTA link to it.
1. On the properties panel, select **[!UICONTROL Add CTA]**, specify the destination URL in the **[!UICONTROL URL]** field and click **[!UICONTROL Save]**. 

   ![add CTA](/help/assets/assets/add-cta.png)

1. Click **[!UICONTROL Preview]** to preview your template and see its defined parameters. 
1. Click **[!UICONTROL Publish]** and select **[!UICONTROL Yes]** to publish your template, if not published earlier. 
1. Navigate to the folder where this template is saved, select this template and click ![details page](/help/assets/assets/details-page-icon.svg) **[!UICONTROL Details]**.
1. Click **[!UICONTROL Copy Options]** and select **[!UICONTROL Copy Embed Code]**. 
    
   ![copy embed code](/help/assets/assets/copy-options1.png)

   The following is an example of the Embed Code:

      ``` json
       <div class="adobe-dynamicmedia-template-embed-container">
       <img id="<Image ID>>" src="<Image Source>>" alt="adobe dynamicmedia template" usemap="#adobe-dynamicmedia-template-map" width="800" height="300">
       <map name="adobe-dynamicmedia-template-map">
       <area shape="rect" coords="417,-60,817,340" href="https://business.adobe.com/products.html" alt="Layer with CTA" title="https://business.adobe.com/products.html" target="_blank">
       <area shape="rect" coords="6,206.57,129,231.43" href="https://business.adobe.com/products.html" alt="Layer with CTA" title="https://business.adobe.com/products.html" target="_blank">
       </map>
       </div>
    ```

1. Add the copied embed code to your site's HTML file and run it in your browser to display the template.

Click the CTA element on the template to navigate to the destination page.

Watch this step by step video to learn how to add a CTA link to a template layer.

>[!VIDEO](https://video.tv.adobe.com/v/3457616)

## Important points to note {#important-points-to-note}

* After creating a template with parameterized image layers for dynamic updates, ensure that the images intended for future updates share the same dimensions as the parameterized images. This ensures the images fit perfectly within the layers without overflowing or leaving empty spaces. Currently, the template does not support automatic dimension adjustments to fit images into the layers.
* There is no substring support in a text layer. User cannot apply different font properties on substring of a text layer.
* Support of multiple [!DNL Dynamic Media] companies is not currently available with [!DNL Dynamic Media] Templates.
* In case of copy or move, Destination Selector shows all the folders (including non-[!DNL Dynamic Media] synced folders). Also, currently, it does not display the [!DNL Dynamic Media] Template assets (both of these are limitations of destination selector).
* Any update operation on a folder (for example, Publish or Delete) from Assets section impacts the [!DNL Dynamic Media] Templates available within that folder. 
* Trash does not work for [!DNL Dynamic Media] Templates. If an asset is moved to trash and then restored, the asset is restored in AEM but not on [!DNL Dynamic Media]. The same is valid for [!DNL Dynamic Media] Templates.

## See also

1. Explore [[!DNL Dynamic Media] and its capabilities](/help/assets/dynamic-media/dynamic-media.md)
1. Explore [[!DNL Dynamic Media] with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)
