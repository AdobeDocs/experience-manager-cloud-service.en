---
title: Work with 3D assets in Dynamic Media
description: Learn how to work with 3D assets in Dynamic Media.
contentOwner: Rick Brough
products: SG_EXPERIENCEMANAGER/6.5/ASSETS and Experience Manager as a Cloud Service
topic-tags: introduction
content-type: reference
feature: 3D Assets
role: User
exl-id: 82084ba7-1302-4cbd-8626-d77b3aaa4ed1
---
# Work with 3D assets in Dynamic Media {#working-with-three-d-assets-dm}

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

Dynamic Media lets you upload, manage, view, and deliver 3D assets as immersive experiences.

* One-click publishing (using **[!UICONTROL Quick Publish]** on the toolbar) of 3D assets to generate a URL.
* Optimized support for viewing 3D assets with the high-quality, interactive Dimensional viewer preset powered by Adobe Dimension.
* The 3D Media WCM component lets you easily add 3D assets to your [!DNL Adobe Experience Manager Sites] pages.

There is no additional installation required to use 3D assets in Dynamic Media.

![Shoe in 3d](/help/assets/dynamic-media/assets/3d-dimensional-viewer-quickpublish-url-embed2a.png)

<!-- See also [Dynamic Media 3D Release Notes](/help/release-notes/aem3d-release-notes.md). -->

## 3D formats supported in Dynamic Media {#supported-three-d-file-formats-in-dm}

Dynamic Media supports the following 3D file formats.

See also [3D formats supported in Experience Manager Assets](/help/assets/file-format-support.md#support-3d-formats)

|3D file extension |File format | MIME type |Notes |
|---|---|---|---|
| GLB | Binary GL Transmission | model/gltf-binary | Includes the materials and textures as a single asset.|
| OBJ | WaveFront 3D Object File | application/x-tgif |  |
| STL | Stereolithography | application/vnd.ms-pki.stl |  |
| USDZ | Universal Scene Description Zip archive|model/vnd.usdz+zip | *Support for ingestion only; no viewing or interaction is available.* USDZ is a proprietary 3D format that can be viewed natively by Safari or iOS.|

The 3D Media WCM component and 3D preview on an asset's Details page is not compatible with the latest version of Chrome (97.x). Instead, to work with 3D assets, use Firefox or Safari, or use an earlier version of Chrome (96.x).

## Quick Start: 3D assets in Dynamic Media {#quick-start-three-d}

The following step-by-step workflow description is designed to help you get up and running quickly with 3D assets in Dynamic Media. 

Before you work with 3D assets in Dynamic Media, make sure that your [!DNL Experience Manager] administrator has already enabled and configured Dynamic Media Cloud Services.

See [Configure Dynamic Media Cloud Services](/help/assets/dynamic-media/config-dm.md#configuring-dynamic-media-cloud-services).

1. **Upload 3D assets**

    * [Upload your 3D assets for use in Dynamic Media](/help/assets/add-assets.md#upload-assets)
    * [Supported 3D file formats for upload in Dynamic Media](#supported-three-d-file-formats-in-dm)

1. **Manage 3D assets**

    * Organize and search 3D assets

        * [Organizing digital assets](/help/assets/organize-assets.md)
        * [Search 3D assets](/help/assets/search-assets.md)

    * View 3D assets

        * [View and interact with 3D assets](#viewing-three-d-assets)
        * [Manage the Dimensional viewer preset](/help/assets/dynamic-media/managing-viewer-presets.md)

    * Work with 3D asset metadata

        * [Manage metadata for digital assets](/help/assets/manage-digital-assets.md#editing-properties)
        * [Metadata schemas](/help/assets/metadata-schemas.md)

1. **Publish 3D assets**

    * [Publish static Dynamic Media 3D assets](#publishing-three-d-assets)
    * [Alternate methods for publishing Dynamic Media 3D assets using the Dimensional viewer](#alternate-publish-methods)

## About viewing and interacting with 3D assets {#viewing-three-d-assets}

This section describes how to view and interact with 3D assets two different ways: from within the asset details page and from within the 3D Media component in Sites.

The interactive 3D viewer includes, among other things, a collection of interactive camera controls that let you orbit, zoom, and pan the 3D asset.

The time it takes to open a 3D asset in the Asset Details page view depends on several factors. These factors include such things as the following:

* Bandwidth to the server.
* Latencies to the server
* Complexity of the image.

In addition, the capabilities of the client computer-such as a workstation, notebook, or mobile touch device-are also important to consider when you manipulate the camera interactively. A reasonably powerful system with good graphics capabilities can make the interactive 3D viewing experience smoother and more favorable.

>[!TIP]
>
>You can open the Dimensional viewer preset in the Viewer Preset Editor to practice navigating a 3D asset without the need to first upload any 3D files. The Dimensional viewer preset has a built-in 3D asset for you to interact with.
>
>See [Manage viewer presets](/help/assets/dynamic-media/managing-viewer-presets.md).

## View and interact with a 3D asset from the asset details page {#viewing-three-d-assets-from-asset-details-page}

See also [Preview assets using the software interface](/help/assets/dynamic-media/previewing-assets.md).

**To view and interact with a 3D asset from the asset details page:**

1. Make sure you have uploaded 3D assets into [!DNL Experience Manager].

    See [Upload your 3D assets for use in Dynamic Media](/help/assets/add-assets.md#upload-assets).

1. From [!DNL Experience Manager], on the **[!UICONTROL Navigation]** page, select **[!UICONTROL Assets > Files]**.
1. Near the upper-right corner of the page, from the **[!UICONTROL View]** drop-down list, select **[!UICONTROL Card View]**.
1. Navigate to a 3D asset that you want to view.
1. To open the asset in the Details page, select the card of the 3D asset.  
1. On the Details page for the 3D asset, do any of the following:

    | View | Description | Mouse action | Touch screen action |
    | --- | --- | --- | --- |
    | **Turn your camera** | Orbit your view around the 3D scene and objects. | Left click + drag. | Single-finger press + drag. |
    | **Pan your camera**  | Pan your view left, right, up, or down. | Right click + drag. | Two-finger press + drag. |
    | **Zoom your camera**  | Move in and out of areas in the 3D scene. | Scroll wheel. | Two-finger pinch. |
    | **Recenter your camera**  | Recenter your camera to a point on an object in the 3D scene. | Double-click. | Double-select. |
    | **Reset**  | Near the lower-right corner of the page, select the Reset icon to restore the view target point to the center of the 3D asset. Reset also moves the camera closer or further away to show the asset in its entirety and at a reasonable viewing size.  |   |   |
    | **Full screen mode**  | To enter full screen mode, in the lower-right corner of the page, select the Fullscreen icon.  |   |   |

1. In the upper-right corner of the page, select **[!UICONTROL Close]** to return to the Assets page.

## View and interact with a 3D asset inside a 3D Media component {#interacting-with-asset-inside-three-d-media-component}

When a web page is in **[!UICONTROL Edit]** mode, no interaction is possible with a 3D asset. To make the asset interactive, you can use the **[!UICONTROL Preview]** feature to view the web page in the page editor with full access to the functionality of the 3D Media component.

>[!IMPORTANT]
>
>You can accomplish this task only after you have added a 3D Media component to a web page and assigned a 3D asset to the component. See [Add the 3D Media component to a web page](#adding-the-three-d-media-component-to-a-web-page) and [Assign a 3D asset to a 3D Media component](#assigning-a-three-d-asset-to-the-component).

See also [Preview assets using the software interface](/help/assets/dynamic-media/previewing-assets.md).

**To view and interact with a 3D asset inside a 3D Media component:**

1. While a web page is in **[!UICONTROL Edit]** mode, do either one of the following:

    * Near the upper right of the page, click **[!UICONTROL Preview]** to enter **[!UICONTROL Preview]** mode.
    * Delete `/editor.html` from the page URL in the browser.

    ![3D asset showing inside the 3D Media component](/help/assets/dynamic-media/assets/3d-asset-in-3d-mediaa.png)
    A fully interactive 3D asset as displayed in **[!UICONTROL Preview]** mode.

1. While in **[!UICONTROL Preview]** mode, do any of the following:

    | View | Description | Mouse action | Touch screen action |
    | --- | --- | --- | --- |
    | **Turn your camera** | Orbit your view around the 3D scene and objects. | Left click + drag. | Single-finger press + drag. |
    | **Pan your camera**  | Pan your view left, right, up, or down. | Right click + drag. | Two-finger press + drag. |
    | **Zoom your camera**  | Move in and out of areas in the 3D scene. | Scroll wheel. | Two-finger pinch. |
    | **Recenter your camera**  | Recenter your camera to a point on an object in the 3D scene. | Double-click. | Double-select. |
    | **Reset**  | Near the lower-right corner of the page, select the Reset icon to restore the view target point to the center of the 3D asset. Reset also moves the camera closer or further away to show the asset in its entirety and at a reasonable viewing size.  |   |   |
    | **Full screen mode**  | To enter full screen mode, in the lower-right corner of the page, select the Fullscreen icon.  |   |   |

## About working with the 3D Media component {#working-with-three-d-media-component}

Dynamic Media includes a Dynamic Media 3D Media component that you can use in [!DNL Experience Manager Sites] to enable interactive viewing of 3D models on your web pages.

* [Add the 3D Media component to the page template](#adding-three-d-media-component-to-page-template)
* [Add the 3D Media component to a web page](#adding-the-three-d-media-component-to-a-web-page)
  * [Optional - Configuring the 3D Media component](#configuring-the-three-d-component)
* [Assign a 3D asset to the 3D Media component](#assigning-a-three-d-asset-to-the-component)

## Add the 3D Media component to the page template {#adding-three-d-media-component-to-page-template}

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL General]** > **[!UICONTROL Templates]**.  
1. Navigate to the page template that you want to enable the 3D component in and select the template.  
1. To open the template, select **[!UICONTROL Edit]**.
1. Near the upper right of the page, in the drop-down menu, select **[!UICONTROL Structure]** mode, if it is not already active.

   ![3d-media-component-structure](/help/assets/dynamic-media/assets/3d-media-component-structurea.png)

1. To select an empty area and open its associated toolbar, select the empty area in the **[!UICONTROL Layout Container]** region.  
1. On the toolbar, select the **[!UICONTROL Policy]** icon to open the **[!UICONTROL Policy Editor]**.
1. In the **[!UICONTROL Properties]** section, under the **[!UICONTROL Allowed Components]** tab, scroll to **[!UICONTROL Dynamic Media]**, then expand the list and check **[!UICONTROL 3D Media]**.
1. Select **[!UICONTROL Done]** to save the changes and close the **[!UICONTROL Policy Editor]**.

   You can now place the Dynamic Media 3D Media component on all pages that use this template.

## Add the 3D Media component to a web page {#adding-the-three-d-media-component-to-a-web-page}

If you are using [!DNL Experience Manager] as your web content management system, you can add 3D assets to your web pages by way of the 3D Media component.

See also [Add Dynamic Media assets to pages](/help/assets/dynamic-media/adding-dynamic-media-assets-to-pages.md).

1. Open [!DNL Experience Manager Sites] and select the web page to which you want to add the Dynamic Media 3D Media component.  
1. To open the page into the page editor, select the **[!UICONTROL Edit]** (pencil) icon. Make sure that **[!UICONTROL Edit]** mode is selected near the upper right of page.

   ![3d-media-component-add](/help/assets/dynamic-media/assets/3d-media-component-edita.png)

1. On the toolbar, select the Side Panel icon to toggle or "turn on" the display of the panel.  

1. In the side panel, select the plus sign icon to open the **[!UICONTROL Components]** list.

    ![3d-media-component-drag-drop](/help/assets/dynamic-media/assets/3d-assets-filtera.png)

1. Drag the **[!UICONTROL 3D Media]** component from the **[!UICONTROL Components]** list to the location on the page where you want the 3D viewer to appear.

You are now ready to assign a 3D asset to the component.

See [Assign a 3D asset to the 3D Media component](#assigning-a-three-d-asset-to-the-component)

### Optional - Configuring the 3D Media component {#configuring-the-three-d-component}

1. In the [!DNL Experience Manager Sites] page editor, select the **[!UICONTROL 3D Media Viewer]** component that you previously added to the page.  
1. To open the component configuration dialog box, select the **[!UICONTROL Configuration]** icon (wrench).

    ![3d-media-component-config](/help/assets/dynamic-media/assets/3d-media-component-configa.png)

1. In the 3D Media dialog box, from the Viewer Preset drop-down list, select **[!UICONTROL Dimensional]** to assign the Dimensional viewer preset to the component.

    ![3d-media-component-edit-config](/help/assets/dynamic-media/assets/3d-media-component-edit-configa.png)

1. In the upper-right corner, select the check mark to save your changes.

## Assign a 3D asset to the 3D Media component {#assigning-a-three-d-asset-to-the-component}

After you have added a 3D Media component to a web page, you can assign a 3D asset to it.

See [Add the 3D Media component to a web page](#adding-the-three-d-media-component-to-a-web-page).

1. In the [!DNL Experience Manager Sites] page editor, click the **[!UICONTROL Assets]** icon to open **[!UICONTROL Assets]** in the side panel.  
1. In the drop-down list, select **[!UICONTROL 3D]** to show only 3D asset file types.
1. In the side panel, search for or scroll to the 3D asset that you want to view on the page being edited.
1. Drag the 3D asset from the Assets side panel and drop it onto the **[!UICONTROL 3D Media]** component that you previously added to the page.

    ![Assign 3d asset to 3d Media component](/help/assets/dynamic-media/assets/3d-asset-adda.png)

>[!NOTE]
>
>While a web page is in the [!DNL Experience Manager Sites] **[!UICONTROL Edit]** mode, the 3D Media component displays the 3D asset but no interaction with the asset is possible. To make the asset interactive, you can use the **[!UICONTROL Preview]** feature to view the web page in the page editor with full access to the functionality of the 3D Media component.

## Publish static Dynamic Media 3D assets {#publishing-three-d-assets}

Dynamic Media accepts various 3D file formats that are supported as *static content* in Dynamic Media. Static content means that you can upload and published 3D assets, but there is no support for *dynamic* imaging or image refitting that is associated with the 3D asset. The reason is because Dynamic Media Imaging Server does not recognize 3D formats. As such, after you publish a 3D asset in Dynamic Media, you have an instant URL that you can copy. The URL for the 3D asset follows the usual Dynamic Media URL structure. However, you cannot edit any parameters in the asset's URL, unlike traditional image assets in Dynamic Media.

See also [Obtain a URL for a static asset](/help/assets/dynamic-media/linking-urls-to-yourwebapplication.md#obtaining-a-url-for-a-static-asset).

In the **[!UICONTROL Card View]**, a small globe icon appears directly below an asset's name and to the left of its date and time to indicate that it is published. In the **[!UICONTROL List View]**, a **[!UICONTROL Published]** column indicates which assets are published or which are not.

If you are using [!DNL Experience Manager] as your WCM, use this publishing method to add the Dynamic Media 3D assets directly on your web page.

See also [Publish Dynamic Media assets](/help/assets/dynamic-media/publishing-dynamicmedia-assets.md).

See also [Publish pages](/help/sites-cloud/authoring/sites-console/publishing-pages.md).

**To publish static Dynamic Media 3D assets:**

1. Open a 3D asset (GLB, OBJ, or STL file format).
1. On the Details page, on the toolbar, select **[!UICONTROL Quick Publish]**.

    ![3d-asset-quick-publish](/help/assets/dynamic-media/assets/3d-asset-quick-publisha.png)

1. Select **[!UICONTROL Close]** to exit the dialog box and return to the asset details page.
1. From the drop-down list to the left of the 3D asset's file name, select **[!UICONTROL Renditions]**.

    ![3d-asset-renditions](/help/assets/dynamic-media/assets/3d-asset-renditionsa.png)

1. Select **[!UICONTROL original]**. When a 3D asset is published (or "activated"), the **[!UICONTROL URL]** button appears near the bottom-left corner of the page if all the following 3D asset conditions are met:
    * The 3D asset is a supported format (GLB, OBJ, STL, and USDZ).
    * The 3D asset was ingested into the Dynamic Media Image Production System (IPS).
    * The 3D asset is published.

    ![3d-asset-url](/help/assets/dynamic-media/assets/3d-asset-urla.png)

1. To display the 3D asset's direct production URL which you can copy and use on web pages, select **[!UICONTROL URL]**.

### Alternate methods for publishing Dynamic Media 3D assets using the Dimensional viewer {#alternate-publish-methods}

Use the following two methods for publishing Dynamic Media 3D assets if you are *not* using [!DNL Experience Manager] as your WCM.

* **[!UICONTROL URL]** - Use **[!UICONTROL URL]** if you are using a third-party web content management system and you want to link Dynamic Media 3D assets to your web pages using the Dimensional viewer.

  See [Link URLs to your web application](/help/assets/dynamic-media/linking-urls-to-yourwebapplication.md#obtaining-a-url-for-an-asset).

* **[!UICONTROL Embed]** - Use **[!UICONTROL Embed]** when you want to view a Dynamic Media 3D asset embedded on a web page using the Dimensional viewer. You copy the embed code to the clipboard so you can paste it in your web pages. Editing of the code is not permitted in the **[!UICONTROL Embed]** dialog box.

  See [Embed the Dynamic Media Video, Image viewer, or Dimensional viewer on a web page](/help/assets/dynamic-media/embed-code.md#embedding-the-video-or-image-viewer-on-a-web-page).
