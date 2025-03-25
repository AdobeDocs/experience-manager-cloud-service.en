---
title: Preview 3D assets
description: Learn how to preview 3D assets in Experience Manager.
contentOwner: Rick Brough
feature: 3D Assets
role: User
exl-id: e873bd25-f841-4063-824f-7e48f40bb678
---
# Preview 3D assets in Adobe Experience Manager{#previewing-3d-assets}

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
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/using/previewing-3d-assets.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

Experience Manager Assets supports the ingestion, management, preview, and delivery of 3D assets. 

You can preview 3D assets with the automatically generated thumbnail renditions or the interactive 3D viewer. The interactive 3D viewer is available from the asset details page in Experience Manager. The viewer includes, among other things, a collection of interactive camera controls that let you rotate, zoom, and pan around the 3D scene.

<!-- See also [Working with 3D assets in Dynamic Media](/help/assets/dynamic-media/assets-3d.md). -->

## Supported formats for thumbnail preview in Experience Manager{#supported-thumbnail-previewing-assets} 

Experience Manager generates thumbnails for the following file formats by default: 

|3D file extension |File format | MIME type |Notes |
|---|---|---|---|
| GLB |Binary GL Transmission|model/gltf-binary ||
| FBX |Autodesk FBX|application/octet-stream ||
| OBJ |WaveFront 3D Object File|application/x-tgif ||
| 3DS |3D Studio Model|application/x-3ds ||
| USDz |Universal Scene Description|model/vnd.usdz+zip ||

## Supported formats for interactive 3D preview in Experience Manager{#supported-3d-previewing-assets} 

Experience Manager supports Interactive 3D preview for the following file formats natively: 

|3D file extension |File format | MIME type |Notes |
|---|---|---|---|
| GLB |Binary GL Transmission|model/gltf-binary ||
| GLTF |GL Transmission Format|model/gltf+json |See the **Note** below. |
| OBJ |WaveFront 3D Object File|application/x-tgif ||
| STL |Stereolithography|application/vnd.ms-pki.stl ||


>[!NOTE]
>
>If materials do not render in preview of a gLTF model, make sure they are named properly and in a `textures` folder in the same root folder as the model, similar to the following:

    Asset (folder)
        model.gltf
        model.bin
        textures (folder)
            material_0_baseColor.jpeg
            material_0_normal.jpeg

## Performance considerations when you preview 3D assets in Experience Manager{#performance-3d-previewing-assets}

The time it takes to open a 3D asset in the asset details view page depends on several factors such things as bandwidth, image complexity, and latencies to the server.

In addition, the capabilities of the client computer &ndash; such as a workstation, notebook, or mobile touch device &ndash; are also important to consider when you manipulate the camera interactively. A reasonably powerful system with good graphics capabilities can make the interactive 3D viewing experience smoother and more favorable.

**To preview 3D assets in Experience Manager:**

1. Make sure you have uploaded 3D assets into Experience Manager.
    See [Supported formats for 3D preview](#supported-3d-previewing-assets) and [Upload assets](/help/assets/manage-digital-assets.md#uploading-assets).
1. From Experience Manager, on the **[!UICONTROL Navigation]** page, go to **[!UICONTROL Assets]** > **[!UICONTROL Files]**.

    ![Navigation page](/help/assets/dynamic-media/assets/navigation-assets.png
    )

1. Near the upper-right corner of the page, from the View drop-down list, select **[!UICONTROL Card View]**, then navigate to a 3D asset that you want to preview.

    ![Selection of the 3D card](/help/assets/dynamic-media/assets/3d-card-select.png)
    _In Card View, select the card of the 3D asset you want to preview._

1. Select the card of the 3D asset.

    ![Interactive 3D preview](/help/assets/dynamic-media/assets/3d-preview.png)
    _Interactive preview of a 3D asset in the asset details view page._ 
1. On the asset details view page for the 3D asset, do any of the following:

    | View | Description | Mouse action | Touch screen action |
    | --- | --- | --- | --- |
    | **Turn your camera** | Orbit your view around the 3D scene and objects. | Left click + drag. | Single-finger press + drag. |
    | **Pan your camera**  | Pan your view left, right, up, or down. | Right click + drag. | Two-finger press + drag. |
    | **Zoom your camera**  | Move in and out of areas of the 3D scene. | Scroll wheel. | Two-finger pinch. |
    | **Recenter your camera**  | Recenter your camera to a point on an object in the 3D scene. | Double-click. | Double-select. |
    | **Reset**  | Near the lower-right corner of the page, select the Reset icon to restore the view target point to the center of the 3D asset. Reset also moves the camera closer or further away to show the asset in its entirety and at a reasonable viewing size.  |   |   |
    | **Full screen mode**  | To enter full screen mode, in the lower-right corner of the page, select the Fullscreen icon.  |   |   |

1. When you are finished, near the upper-right corner of the page, select **[!UICONTROL Close]**.
