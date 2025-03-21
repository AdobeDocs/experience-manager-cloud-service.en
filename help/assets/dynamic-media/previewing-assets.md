---
title: Preview assets
description: Learn how to preview assets in Dynamic Media so you can see how it is viewed by a customer in their own web browser.
contentOwner: Rick Brough
feature: Asset Management
role: User
exl-id: 3928798d-352a-42a8-a544-7104fc9b3cf1
---
# Preview assets{#previewing-assets}

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

You can use Preview to see how a digital asset that you have uploaded appears when it is viewed by a customer in their own web browser. The default embedded, cross-device viewer that is assigned to the asset is used for the Preview.

A viewer is a collection of various settings or "presets." For example, the viewer display size, zoom behavior, color schemes, borders, and fonts, that determine how users view rich-media assets on their computer screens and mobile devices.

Besides using the dedicated Preview feature for video, spin sets, and image sets, you can also preview an asset by using viewer presets that you have created. Or, use image presets to preview renditions of images.

* [Applying Image Presets](/help/assets/dynamic-media/image-presets.md)
* [Applying Viewer Presets](/help/assets/dynamic-media/viewer-presets.md)

>[!NOTE]
>
>When you are on a webpage (Sites) in Adobe Experience Manager, you cannot preview assets in **[!UICONTROL Edit]** mode. Instead, go to Preview mode by selecting **[!UICONTROL Preview]** in the upper right-hand corner of the page.

To enable or disable viewer presets in the user interface, see [Managing Viewer Presets](/help/assets/dynamic-media/managing-viewer-presets.md).

**To preview assets:**

1. From **[!UICONTROL Experience Manager]**, on the **[!UICONTROL Navigation]** page, select **[!UICONTROL Assets]**, then **[!UICONTROL Files]** to access assets.
1. Near the upper-right corner of the page, from the **[!UICONTROL View]** drop-down list, select **[!UICONTROL List View]**.
1. (Optional) Use the **[!UICONTROL Type]** column to sort the assets by the type you want to preview.
1. Under the **[!UICONTROL Title]** column, select the title name (not the thumbnail image) of the asset you want to preview.
1. Depending on the asset type you selected, do any one of the following:

    <table>
    <tbody>
      <tr>
      <td><strong>Asset type you selected</strong><br /> </td>
      <td><strong>Able to preview asset in a particular rendition?</strong></td>
      <td><strong>Able to preview asset in a particular viewer?</strong></td>
      </tr>
      <tr>
      <td><p>3D</p> </td>
      <td>No</td>
      <td>Yes</td>
      <td><p><strong>To preview a 3D asset in the Dimensional viewer</strong></p>
      <ul>
      <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Viewers</strong> from the list, then select the Dimensional viewer.</li>
      <li>To return the image to the original zoomap, select <strong>Reset</strong>.</li>
      <li>To maximize the viewer on the display device, select <strong>Fullscreen</strong>.</li>
      </ul>
      <p><strong>Navigating the 3D scene</strong></p>
      <ul>
      <li><p><strong>Turn your 3D camera</strong> - Orbit your view around the 3D scene and objects.</p> Mouse: Left click + Drag.</p> Touch-screen: Press + Drag.</p></li>
      <li><p><strong>Pan your camera</strong> - Pan your view left, right, up, and down.</p> Mouse: Right-click + Drag.</p> Touch-screen: Two-finger press + Drag.</p></li>
      <li><p><strong>Zoom your camera</strong> - Zoom your camera if you want to move in and out of areas in the 3D scene.</p> Mouse: Scroll wheel.</p> Touch-screen: Finger pinch.</p></li>
      <li><p><strong>Recenter your camera</strong> - Orbit your view around the 3D scene and objects.</p> Mouse: Double-click.</p> Touch-screen: Double-select.</li></ul></td>
      </tr>
      <tr>
      <td><p>Image</p> </td>
      <td>Yes</td>
      <td>Yes</td>
      <td><p><strong>To preview asset in a particular rendition</strong></p>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Renditions</strong> from the list, then select a particular rendition that you want to preview.</li>
        </ul> <p><strong>To preview asset in a particular viewer</strong></p>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Viewers</strong> from the list, then select a viewer that you want to apply to the asset.</li>
        </ul><p>Use the <strong>+</strong> and <strong>-</strong>icons to increase or decrease the zoom of the selected image, respectively. To return the image to the original zoom, select <strong>Reset</strong>.<br>If you are on a touch-screen, double-select the image to zoom in by steps. When you reach maximum zoom, double-select the image again to reset the zoom state. Drag across the image to pan.</p> </td>
      </tr>
      <tr>
      <td>Multimedia</td>
      <td>Yes</td>
      <td>Yes</td>
      <td><p><strong>To preview asset in a particular rendition</strong></p>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Renditions</strong> from the list, then select a particular rendition that you want to preview.</li>
        </ul><p>Selecting a higher-resolution video rendition to preview can cause the video to appear truncated. The reason is because the rendition preview shows you the exact resolution that your customers see it, all in the context of the embedded viewer that is used for the preview.</p><p>When you preview an adaptive video set at the Asset level, the renditions are grouped into one playback experience. That is, the adaptive video is sized properly for viewing and played back using the best resolution in the context of your viewing device and connection speed.<br /></p><p><strong>To preview an asset in a particular viewer</strong></p>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Viewers</strong> from the list, then select a viewer that you want to apply to the asset.</li>
        </ul> </td>
      </tr>
      <tr>
      <td>Image set</td>
      <td>No</td>
      <td>Yes</td>
      <td><p><strong>To preview an asset in a particular viewer</strong></p>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Viewers</strong> from the list, then select a viewer that you want to apply to the asset.</li>
        </ul> <p>Use the <strong>+</strong> and <strong>- </strong>icons to increase or decrease the zoom of the selected image, respectively. To return the image to the original zoom, select <strong>Reset</strong>.<br /> If you are on a touch-screen, double-select the image to zoom in by steps. When you reach maximum zoom, double-select the image again to reset the zoom state. Drag across the image to pan.</p></td>
      </tr>
      <tr>
      <td>Spin set</td>
      <td>No</td>
      <td>Yes</td>
      <td><p><strong>To preview an asset in a particular viewer</strong></p>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Viewers</strong> from the list, then select a viewer that you want to apply to the asset.</li>
        </ul><p>Use the <strong>+</strong> and <strong>- </strong>icons to increase or decrease the zoom of the selected image, respectively. To return the image to the original zoom, select <strong>Reset</strong>.<br /> If you are on a touch-screen, double-select the image to zoom in by steps. When you reach maximum zoom, double-select the image again to reset the zoom state. Drag across the image to pan.</p> </td>
      </tr>
      <tr>
      <td>Mixed Media set</td>
      <td>No</td>
      <td>Yes</td>
      <td><p><strong>To preview an asset in a particular viewer</strong></p>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Viewers</strong> from the list, then select a viewer that you want to apply to the asset.</li>
        </ul> <p>Use the <strong>+</strong> and <strong>- </strong>icons to increase or decrease the zoom of the selected image, respectively. To return the image to the original zoom, select <strong>Reset</strong>.<br /> If you are on a touch-screen, double-select the image to zoom in by steps. When you reach maximum zoom, double-select the image again to reset the zoom state. Drag across the image to pan.</p> </td>
      </tr>
      <tr>
      <td>Carousel set</td>
      <td>No</td>
      <td>Yes</td>
      <td><strong>To preview an asset in a particular viewer</strong>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select a viewer that you want to apply to the asset.</li>
        </ul> </td>
      </tr>
      <tr>
      <td>360 Video<br /> </td>
      <td>Yes</td>
      <td>Yes</td>
      <td><p><strong>To preview asset in a particular rendition</strong></p>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Renditions</strong>, then select the rendition that you want to preview.</li>
        </ul> <p><strong>To preview asset in a particular viewer</strong></p>
        <ul>
        <li>Near the upper-left corner of the page, select the icon so the drop-down list appears. Select <strong>Viewers</strong>, then select a viewer that you want to apply to the asset.</li>
        </ul> <p>Use the <strong>+</strong> and <strong>- </strong>icons to increase or decrease the zoom of the selected image, respectively. To return the image to the original zoom, select <strong>Reset</strong>.<br /> If you are on a touch-screen, double-select the image to zoom in by steps. When you reach maximum zoom, double-select the image again to reset the zoom state. Drag across the image to pan.</p> </td>
      </tr>
    </tbody>
    </table>
