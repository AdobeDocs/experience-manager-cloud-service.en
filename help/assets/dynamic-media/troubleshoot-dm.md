---
title: Troubleshoot Dynamic Media
description: Learn about troubleshooting tips you can try when you work with images, sets, and viewers in Dynamic Media.
contentOwner: Rick Brough
feature: Troubleshooting,Image Sets,Viewers
role: Admin,User
exl-id: 3e8a085f-57eb-4009-a5e8-1080b4835ae2
---
# Troubleshoot Dynamic Media {#troubleshooting-dynamic-media-scene-mode}

The following topic describes troubleshooting for Dynamic Media.

## New Dynamic Media configuration {#new-dm-config}

See [Troubleshoot a new Dynamic Media configuration](/help/assets/dynamic-media/config-dm.md#troubleshoot-dm-config).

## General (All Assets) {#general-all-assets}

The following are some general tips and tricks for all assets.

### Asset synchronization status properties {#asset-synchronization-status-properties}

The following asset properties can be reviewed in CRXDE Lite to confirm the successful synchronization of the asset from Adobe Experience Manager to Dynamic Media:

| **Property** |**Example** |**Description** |
|---|---|---|
| `<object_node>/jcr:content/metadata/dam:scene7ID` |**`a|364266`** |General indicator that node is linked to Dynamic Media. |
| `<object_node>/jcr:content/metadata/dam:scene7FileStatus` |**PublishComplete** or error text |Status of upload of asset to Dynamic Media. |
| `<object_node>/jcr:content/metadata/dam:scene7File`  |**myCompany/myAssetID** |Must be populated to generate URLs to remote asset of Dynamic Media. |
| `<object_node>/jcr:content/dam:lastSyncStatus` |**success** or **failed: `<error text>`** |Synchronization status of sets (spin sets, image sets, and so on), image presets, viewer presets, image map updates for an asset, or images that were edited. |

### Synchronization logging {#synchronization-logging}

Synchronization errors and issues are logged in `error.log` (Experience Manager server directory `/crx-quickstart/logs/`). Sufficient logging is available to determine the root cause of most issues, however you can increase the logging to DEBUG on the `com.adobe.cq.dam.ips` package through the Sling Console ([https://localhost:4502/system/console/slinglog](https://localhost:4502/system/console/slinglog)) to gather more information.

### Version Control {#version-control}

When replacing an existing Dynamic Media asset (same name and location), you can keep both assets or replace/create a version:

* Keeping both creates an asset with a unique name for the published asset URL. For example, `image.jpg` is the original asset and `image1.jpg` is the newly uploaded asset.

* Creating a version is not supported in Dynamic Media. The new version replaces the existing asset in delivery.

## Images and Sets {#images-and-sets}

If you are having issues with images and sets, see the following troubleshooting guidance.

<table>
 <tbody>
  <tr>
   <td><strong>Issue</strong></td>
   <td><strong>How to debug</strong></td>
   <td><strong>Solution</strong></td>
  </tr>
  <tr>
   <td>Cannot access copy URL/Embed button in asset detail view</td>
   <td>
    <ol>
     <li><p>Go to CRX/DE:</p>
      <ul>
       <li>Check whether the preset in the JCR <code>/etc/dam/presets/viewer/&lt;preset&gt; has lastReplicationAction</code> defined. This location applies if you upgraded from Experience Manager 6.x to 6.4 and opted out of migration. Otherwise, the location is <code>/conf/global/settings/dam/dm/presets/viewer</code>.</li>
       <li>Check to make sure that the asset in the JCR has <code>dam:scene7FileStatus</code><strong> </strong>under Metadata shows as <code>PublishComplete</code>.</li>
      </ul> </li>
    </ol> </td>
   <td><p>Refresh page/navigate to another page and come back (side rail JSP must be recompiled)</p> <p>If that does not work:</p>
    <ul>
     <li>Publish asset.</li>
     <li>Reupload asset and publish it.</li>
    </ul> </td>
  </tr>
  <tr>
   <td>Carousel hotspot moves around after switching between slides</td>
   <td><p>Check that all slides are the same size.</p> </td>
   <td><p>Use only images with the same size for the carousel.</p> </td>
  </tr>
  <tr>
   <td>Image does not preview with the Dynamic Media viewer</td>
   <td><p>Check that the asset contains <code>dam:scene7File</code> in the Metadata properties (CRXDE Lite)</p> </td>
   <td><p>Check that all assets have finished processing.</p> </td>
  </tr>
  <tr>
   <td>Uploaded asset does not show in asset selector</td>
   <td><p>Check asset has property <code>jcr:content</code> &gt; <strong><code>dam:assetState</code></strong> = <code>processed</code> (CRXDE Lite)</p> </td>
   <td><p>Check that all assets have finished processing.</p> </td>
  </tr>
  <tr>
   <td>Banner on card view shows <strong>New</strong> when asset has not started processing</td>
   <td>Check asset <code>jcr:content</code> &gt; <code>dam:assetState</code> = if <code>unprocessed</code> it was not picked up by the workflow.</td>
   <td>Wait until asset is picked up by workflow.</td>
  </tr>
  <tr>
   <td>Images or sets do not display the viewer URL or embed code</td>
   <td>Check if the viewer preset has been published.</td>
   <td><p>Go to <strong>Tools</strong> &gt; <strong>Assets</strong> &gt; <strong>Viewer Presets</strong> and publish the viewer preset.</p> </td>
  </tr>
 </tbody>
</table>

## Video {#video}

If you are having issues with video, see the following troubleshooting guidance.

<table>
 <tbody>
  <tr>
   <td><strong>Issue</strong></td>
   <td><strong>How to debug</strong></td>
   <td><strong>Solution</strong></td>
  </tr>
  <tr>
   <td>Video cannot be previewed</td>
   <td>
    <ul>
     <li>Check that the folder has a video profile assigned to it (if non-supported file format). If non-supported, only an image displays.</li>
     <li>Video profile must contain more than one encoding preset to generate an AVS set (single encodings are treated as video content for MP4 files; for non-supported files, treated the same as non-processed).</li>
     <li>Check that the video has finished processing by confirming <code>dam:scene7FileAvs</code> of <code>dam:scene7File</code> in metadata.</li>
    </ul> </td>
   <td>
    <ol>
     <li>Assign a video profile to the folder.</li>
     <li>Edit video profile to include more than one encoding preset.</li>
     <li>Wait for video to finish processing.</li>
     <li>Before you reload the video, make sure that the Dynamic Media Encode Video workflow is not running.<br/> </li>
     <li>Reupload the video.</li>
    </ol> </td>
  </tr>
  <tr>
   <td>Video is not encoded</td>
   <td>
    <ul>
     <li>Check whether Dynamic Media Cloud Service is configured.</li>
     <li>Check whether a video profile is associated with the upload folder.</li>
    </ul> </td>
   <td>
    <ol>
     <li>Check that the Dynamic Media Configuration under Cloud Services is properly set up.</li>
     <li>Check that the folder has a video profile. Also, check the video profile.</li>
    </ol> </td>
  </tr>
  <tr>
   <td>Video processing takes too long</td>
   <td><p>To determine if video encoding is still in progress or if it has entered a failure state:</p>
    <ul>
     <li>Check the video status <code>https://localhost:4502/crx/de/index.jsp#/content/dam/folder/videomp4/jcr%3Acontent</code> &gt; <code>dam:assetState</code></li>
    </ul> </td>
   <td> </td>
  </tr>
  <tr>
   <td>Video rendition missing</td>
   <td><p>When video is uploaded, but there are no encoded renditions:</p>
    <ul>
     <li>Check that the folder has a video profile assigned to it.</li>
     <li>Check that the video has finished processing by confirming <code>dam:scene7FileAvs</code> in metadata.</li>
    </ul> </td>
   <td>
    <ol>
     <li>Assign a video profile to the folder.</li>
     <li>Wait for video to finish processing.<br /> </li>
    </ol> </td>
  </tr>
 </tbody>
</table>

## Viewers {#viewers}

If you are having issues with viewers, see the following troubleshooting guidance.

### Issue: Viewer presets are not published {#viewers-not-published}

**How to debug**

1. Proceed to sample manager diagnostic page: `https://localhost:4502/libs/dam/gui/content/s7dam/samplemanager/samplemanager.html`.
1. Observe computed values. When operating correctly, you see the following: `_DMSAMPLE status: 0 unsyced assets - activation not necessary _OOTB status: 0 unsyced assets - 0 unactivated assets`.

   >[!NOTE]
   >
   >It can take about 10 minutes after configuration of Dynamic Media cloud settings for the viewer assets to sync.
   
1. If unactivated assets remain, select either of the **List all Unactivated Assets** buttons to see details.

**Solution**

1. Navigate to viewer preset list in admin tools: `https://localhost:4502/libs/dam/gui/content/s7dam/samplemanager/samplemanager.html`
1. Select all viewer presets, then select **Publish**.
1. Navigate back to sample manager and observe that unactivated asset count is now zero.

### Issue: Viewer preset artwork returns 404 from Preview in asset details or Copy URL/Embed code {#viewer-preset-404}

**How to debug**

In CRXDE Lite do the following:

1. Navigate to `<sync-folder>/_CSS/_OOTB` folder within your Dynamic Media sync folder (for example, `/content/dam/_CSS/_OOTB`).
1. Find the metadata node of the problematic asset (for example, `<sync-folder>/_CSS/_OOTB/CarouselDotsLeftButton_dark_sprite.png/jcr:content/metadata/`).
1. Check for the presence of `dam:scene7*` properties. If the asset was successfully synced and published, you see the `dam:scene7FileStatus` set is to **PublishComplete**.
1. Attempt to request the artwork directly from Dynasmic Media by concatenating the values of the following properties and string literals:

   * `dam:scene7Domain`
   * `"is/content"`
   * `dam:scene7Folder` 
   * `<asset-name>` 
    Example: `https://<server>/is/content/myfolder/_CSS/_OOTB/CarouselDotsLeftButton_dark_sprite.png`

**Solution**

If the sample assets or viewer preset artwork has not synced or published, restart the entire copy/sync process:

1. Navigate to CRXDE Lite. 
1. Delete `<sync-folder>/_CSS/_OOTB`. 
1. Navigate to the CRX Package Manager: `https://localhost:4502/crx/packmgr/`.
1. Search for viewer package in the list; it starts with `cq-dam-scene7-viewers-content`.
1. Select **Reinstall**.
1. Under Cloud Services, navigate to the Dynamic Media Configuration page, then open the configuration dialog box for your Dynamic Media - S7 configuration.
1. Make no changes, select **Save**.
   This save action triggers the logic again to create and sync the sample assets, viewer preset CSS, and artwork.

### Issue: Image Preview is not loading in Viewer presets authoring {#image-preview-not-loading}

**Solution**

1. In Experience Manager, select the Experience Manager logo to access the global navigation console, then navigate to **[!UICONTROL Tools]** > **[!UICONTROL General]** > **[!UICONTROL CRXDE Lite]**.
1. In the left rail, navigate to the sample content folder at the following location:

   `/content/dam/_DMSAMPLE`

1. Delete the `_DMSAMPLE` folder. 
1. In the left rail, navigate to the presets folder at the following location:

   `/conf/global/settings/dam/dm/presets/viewer`

1. Delete the `viewer` folder.
1. Near the upper-left corner of the CRXDE Lite page, select **[!UICONTROL Save All]**.
1. In the upper-left corner of the CRXDE Lite page, select the **Back Home** icon.
1. Re-create a [Dynamic Media Configuration in Cloud Services](/help/assets/dynamic-media/config-dm.md#configuring-dynamic-media-cloud-services).
