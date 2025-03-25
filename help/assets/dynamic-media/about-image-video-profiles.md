---
title: About Dynamic Media Image Profiles and Video Profiles
description: An Image Profile or a Video Profile is a recipe for what options to apply to assets that you upload to a folder. For example, you can specify what video encoding to apply to Dynamic Media video assets that you upload. Or, what Image Profile to apply to Dynamic Media image assets to have them properly cropped.
contentOwner: Rick Brough
feature: Asset Management,Image Profiles,Video Profiles
role: Admin,User
exl-id: 8c8f0a57-13f5-4903-8d76-bfb6ee83323c
---
# About Dynamic Media Image Profiles and Video Profiles{#about-dm-image-video-profiles}

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

An Image Profile or Video Profile is a recipe for what options to apply to assets that you upload to a folder. For example, you can specify what video encoding to apply to Dynamic Media video assets that you upload. Or, what Image Profile to apply to Dynamic Media image assets to have them properly cropped.

In Dynamic Media, you can create two types of profiles, which are covered in detail at the following links:

* [Dynamic Media Image profiles](/help/assets/dynamic-media/image-profiles.md)
* [Dynamic Media Video profiles](/help/assets/dynamic-media/video-profiles.md)

See also [Metadata profiles](/help/assets/metadata-profiles.md).

You must have Administrator rights to create, edit, and delete Dynamic Media Image Profiles or Dynamic Media Video Profiles.

After you create your Image Profile or Video Profile, you assign it to one or more folders that you use for newly uploaded Dynamic Media assets.

See also [Best Practices for Organizing your Digital Assets for using Processing Profiles](/help/assets/organize-assets.md).


>[!NOTE]
>
>Assets that you move from one folder to another do not get reprocessed. For example, suppose you have Folder 1 that has profile A assigned to it and Folder 2 that has profile B assigned to it. If you move assets from Folder 1 to Folder 2, the moved assets retain their original processing from Folder 1.
>
>The same is true even when you move assets between two folders that have the same profile assigned to it.

## Reprocess Dynamic Media assets in a folder {#reprocessing-assets}

You can reprocess assets in a folder that already has an existing Dynamic Media Image Profile or a Dynamic Media Video Profile that you later changed.

For example, suppose you created a Dynamic Media Image Profile and assigned it to a folder. Any image assets you uploaded to the folder automatically had the Image Profile applied to the assets. However, later you decide to add a new smart crop ratio to the Image Profile. Now, instead of having to select and reupload the assets to the folder all over again, you simply run the *Dynamic Media Reprocess* workflow.

You can run the reprocess workflow on an asset for which processing failed the first time. Even if you have not edited an Image Profile or Video profile, or you have already applied an Image Profile or Video Profile, you can still run the reprocess workflow on a folder of assets anytime.

You can optionally adjust the batch size of the reprocess workflow from a default of 50 assets up to 1000 assets. When you run the _Dynamic Media Reprocess_ workflow on a folder, assets are grouped in batches, then sent to the Dynamic Media server for processing. Following processing, the metadata of each asset in the entire batch set is updated on [!DNL Adobe Experience Manager]. If the batch size is large, you can experience a delay in processing. Or, if the batch size is too small, it can cause too many roundtrips to the Dynamic Media server.

See [Adjust the batch size of the reprocess workflow](#adjusting-load).

>[!NOTE]
>
>If you are performing a bulk migration of assets from Dynamic Media Classic to [!DNL Experience Manager], enable the Migration replication agent on the Dynamic Media server. When the migration is complete, make sure you disable the agent.
>
>The Migration publish agent must be disabled on the Dynamic Media server so the Reprocess workflow works as expected.

<!-- LEAVE IN PLACE, MAY BE USED IN THE FUTURE

Batch size is the number of assets that are amalgamated into a single IPS (Dynamic Media's Image Production System) job. When you run the Dynamic Media Reprocess workflow, the job is triggered on IPS. The number of IPS jobs that are triggered is based on the total number of assets in the folder, divided by the batch size. For example, suppose you had a folder with 150 assets and a batch size of 50. In this case, three IPS jobs are triggered. The assets are updated when the entire batch size (50 in our example) is processed in IPS. The job then moves onto the next IPS job and so on until complete. If you increase the batch size, you may notice a longer delay with assets getting updated. 

-->

**To reprocess Dynamic Media assets in a folder:**

1. In [!DNL Experience Manager], from the Assets page, navigate to an assets folder that has an Image Profile or a Video Profile assigned to it and for which you want to apply the **Dynamic Media Reprocess** workflow.

    Folders that have an Image Profile or Video Profile assigned to it have the profile's name appear directly below the folder name in Card View. 

1. Select a folder.

    * The workflow considers all files in the selected folder, recursively.
    * If there are one or more subfolders with assets in the main selected folder, the workflow reprocesses every asset in the folder hierarchy.
    * As a best practice, avoid running this workflow on a folder hierarchy that has more than 1000 assets.

1. Near the upper-left corner of the page, from the drop-down list, select **[!UICONTROL Timeline]**.
1. Near the lower-left corner of the page, to the right of the [!UICONTROL Comment] field, select the carat icon  ( **^** ) .

    ![Screenshot of Assets in Experience Manager showing a selected folder of assets, the Timeline drop-down list highlighted, the Start Workflow button highlighted, and the carat icon to the right of the Comment field also highlighted](/help/assets/dynamic-media/assets/reprocess-assets1.png).

1. Select **[!UICONTROL Start Workflow]**.
1. From the **[!UICONTROL Start Workflow]** drop-down list, choose **[!UICONTROL Dynamic Media Reprocess]**.
1. (Optional) In the **Enter title of workflow** text field, enter a name for the workflow. You can use the name to reference the workflow instance, if necessary.

    ![Screenshot of the Timeline user interface with "Dynamic Media Reprocess" selected from the Start Workflow drop-down list, and the Start button highlighted](/help/assets/dynamic-media/assets/reprocess-assets2.png).

1. Select **[!UICONTROL Start]**, then select **[!UICONTROL Confirm]**.

    To monitor the workflow or check its progress, from the [!DNL Experience Manager] main console page, select **[!UICONTROL Tools > Workflow]**. On the Workflow Instances page, select a workflow. On the menu bar, select **[!UICONTROL Open History]**. You can also terminate, suspend, or rename a selected workflow from the same Workflow Instances page.

### Adjust the batch size of the reprocess workflow (optional) {#adjusting-load}

(Optional) The default batch size in the reprocessing workflow is 50 assets per job. This optimal batch size is governed by the average asset size and the MIME types of assets on which the reprocess is run. A higher value means you have many files in a single reprocessing job. So, the processing banner stays on [!DNL Experience Manager] assets for a longer time. However, if the average file size is small&ndash;1 MB or less&ndash;Adobe recommends that you increase the value to several 100, but never more than a 1000. If the average file size is hundreds of megabytes, Adobe recommends that you lower the batch size up to 10.

**To optionally adjust the batch size of the reprocess workflow:**

1. In [!DNL Experience Manager], select **[!UICONTROL Adobe Experience Manager]** to access the global navigation console, then select the **[!UICONTROL Tools]** (hammer) icon > **[!UICONTROL Workflow > Models]**.
1. On the Workflow Models page, in Card View or List View, select **[!UICONTROL Dynamic Media Reprocess]**.

    ![Screenshot of the Workflow Models page with "Dynamic Media Reprocess" workflow selected in the Card view of Experience Manager](/help/assets/dynamic-media/assets/reprocess-assets7.png).

1. In the toolbar, select **[!UICONTROL Edit]**. A new browser tab opens the Dynamic Media Reprocess workflow model page.
1. On the Dynamic Media Reprocess workflow page, near the upper-right corner, select **[!UICONTROL Edit]** to "unlock" the workflow.
1. In the workflow, select the Scene7 Batch Upload component to open the toolbar, then select **[!UICONTROL Configure]** in the toolbar.

    ![Screenshot of the "Scene7 Batch Upload" component on the "Dynamic Media Reprocess" page with the mouse pointer hovering over the "Configure" icon](/help/assets/dynamic-media/assets/reprocess-assets8.png).

1. On the **[!UICONTROL Batch Upload to Scene7&mdash;Step Properties]** dialog box, set the following:
    * In the **[!UICONTROL Title]** and **[!UICONTROL Description]** text fields, enter a new title and description for the job, if desired.
    * Select **[!UICONTROL Handler Advance]** if your handler will advance to the next step.
    * In the **[!UICONTROL Timeout]** field, enter the external process timeout (seconds).
    * In the **[!UICONTROL Period]** field, enter a polling interval (seconds) to test for the completion of the external process. 
    * In the **[!UICONTROL Batch field]**, enter the maximum number of assets (50-1000) to process in a Dynamic Media server batch processing upload job.
    * Select **[!UICONTROL Advance on timeout]** if you want to advance when the timeout is reached. Deselect if you want to proceed to the inbox when the timeout is reached. 

    ![Screenshot of the "Batch Upload to Scene7 - Step Properties" page](/help/assets/dynamic-media/assets/reprocess-assets3.png).

1. In the upper-right corner of the **[!UICONTROL Batch Upload to Scene7 &ndash; Step Properties]** dialog box, select **[!UICONTROL Done]**. 

1. In the upper-right corner of the Dynamic Media Reprocess workflow model page, select **[!UICONTROL Sync]**. When you see **[!UICONTROL Synced]**, the workflow runtime model is successfully synchronized and ready to reprocess assets in a folder.

    ![Screenshot of Assets in Experience Manager showing a selected folder of assets, the Timeline drop-down list highlighted, the Start Workflow button highlighted, and the carat icon to the right of the Comment field also highlighted](/help/assets/dynamic-media/assets/reprocess-assets1.png).

1. Close the browser tab that shows the Dynamic Media Reprocess workflow model.
 
<!-- MAY BE NEEDED IN THE FUTURE

1. Return to the browser tab that has the open Workflow Models page, then press **Esc** to exit the selection.
1. In the upper-left corner of the page, select **[!UICONTROL Adobe Experience Manager]** to access the global navigation console, then select the **[!UICONTROL Tools]** (hammer) icon > **[!UICONTROL General > CRXDE Lite]**.
1. In the folder tree on the left side of the CRXDE Lite page, navigate to the following location:

   `/conf/global/settings/workflow/models/scene7_reprocess_assets/jcr:content/flow/reprocess/metaData`

   ![CRXDE Lite](/help/security/assets/workflow-models9.png)

1. On the right side of the CRXDE Lite page, in the lower portion, enter the following name, type, and value in its respective field:
    * **[!UICONTROL Name]**: `reprocess-batch-size`
    * **[!UICONTROL Type]**: `Long`
    * **[!UICONTROL Value]**: enter a default value (50-1000) for the batch size
1. In the lower-right corner, select **[!UICONTROL Add]**. The new property appears as the following:

    ![Saving the new property](/help/security/assets/workflow-models10.png)

1. On the menu bar of the CRXDE Lite page, select **[!UICONTROL Save All]**.
1. In the upper-left corner of the page, select **[!UICONTROL CRXDE Lite]** to return to the main Experience Manager console
1. Repeat steps 1-7 to re-synchronize the new batch size to the Dynamic Media Reprocess workflow model.

-->
