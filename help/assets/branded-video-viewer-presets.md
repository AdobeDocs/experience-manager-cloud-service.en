---
title: Configure branded video viewer presets
description: Learn how to create, customize, and apply branded video viewer presets to configure the appearance and playback behavior of videos in Dynamic Media.
role: User
---

# Configure branded video viewer presets {#configure-branded-video-viewer-presets}

Branded video viewer presets let you define and reuse a consistent playback experience for videos in Dynamic Media. A preset is a named collection of appearance and playback settings that you can apply to video assets without configuring the same options individually for each video.

Use branded video viewer presets to customize the player's appearance, control playback behavior, and provide a consistent viewing experience across videos.

## Create a branded video viewer preset {#create-branded-video-viewer-preset}

Execute the following steps to create a branded video viewer preset:

1. In Experience Manager, navigate to **Tools** > **Assets** > **Viewer Presets**.
2. Click **Create**.
3. Enter a name for the preset.
4. For the Rich Media Type, select **Branded Videos**.

   ![Create a branded video viewer preset](assets/create-branded-video-viewer-preset.png)

5. Configure the appearance and playback settings for the video viewer.
6. Save the preset.

The available settings depend on the selected viewer and the Dynamic Media environment.

## Customize the player appearance {#customize-player-appearance}

Use the **[!UICONTROL Appearance]** tab to customize the video player's colors, control bar scale, and main play button.

![Appearance settings for the branded video viewer](assets/branded-video-viewer-appearance.png)

In the **[!UICONTROL Component Appearance]** panel, configure the following settings:

* **Colors:** Set the colors for the control bar, accent and progress, icons and text, big play button, and border.
* **Sizes:** Adjust the control bar scale using the slider or select **[!UICONTROL S]**, **[!UICONTROL M]**, **[!UICONTROL L]**, or **[!UICONTROL XL]**.
* **Borders:** Choose a shape for the main play button, such as a rectangle, rounded rectangle, oval, or circle. Adjust the button scale using the slider.

Select **[!UICONTROL Show CSS]** to edit the viewer CSS and customize its appearance. Changes are applied to the preview and saved with the preset.

![CSS Viewer editor](assets/css-viewer.png)

Use the **[!UICONTROL Desktop]**, **[!UICONTROL Tablet]**, and **[!UICONTROL Phone]** previews to review the player appearance at different display sizes.

## Configure playback behavior {#configure-playback-behavior}

Use the Behavior settings to control how the video plays and how playback controls appear.

![Playback behavior settings for the branded video viewer](assets/branded-video-viewer-behavior.png)

### Configure player controls {#configure-player-controls}

Configure whether the player controls are displayed. Depending on the supported options, you can also show or hide individual controls, including:

* Volume control
* Time display
* Captions control
* Playback rate control

Choose the controls that viewers need for the intended playback experience.

### Configure playback options {#configure-playback-options}

Configure the supported playback options for the preset.

| Option | Description |
| --- | --- |
| Autoplay | Starts video playback automatically when the viewer loads. |
| Loop | Restarts the video automatically after playback ends. |
| Start muted | Starts playback with audio muted. |
| Playback rates | Specifies the playback speeds available to viewers. You can also configure whether the playback rate control is displayed, where supported. |
| Transition | Configures the transition used when viewer controls appear or disappear, such as a fade or slide-down transition. |

The availability and behavior of individual options depend on the selected viewer.

### Configure video presentation and quality {#configure-video-presentation-quality}

Configure the supported options for how the video is displayed and loaded.

| Option | Description |
| --- | --- |
| Letterboxing | Controls whether the video is displayed with letterboxing or stretched to fill the available area. |
| Initial bitrate | Specifies the initial bitrate used when adaptive streaming starts playback. |
| Progressive bitrate | Specifies the bitrate used for progressive video playback. |
| Smart Crop | Enables the supported smart-cropped video presentation for the asset. |

Preview the video after changing these settings to verify the resulting playback.

## Save and make the preset available {#save-and-publish-preset}

After configuring the preset, save your changes.

The steps required to make a preset available depend on your Dynamic Media environment:

* **Dynamic Media Scene7:** Publish the preset when required so it can be used for delivery.
* **Dynamic Media with OpenAPI:** Complete the required preset approval workflow before using the preset.

Confirm that the preset is available in the relevant environment before applying it to a video.

## Apply a branded video viewer preset to a video {#apply-preset-to-video}

After the preset is available, you can select it when previewing or delivering a video, where supported.

### Apply the preset from the asset details page {#apply-preset-from-asset-details}

Execute the following steps to preview a video using an available viewer or preset:

1. Navigate to **Assets** > **Files**, and open the folder containing the video.
2. Click the video asset to open the asset details page.
3. In the left panel, click **Viewers**.
4. Select the appropriate viewer or preset, where available, to preview the video.

   ![Apply the branded video viewer preset from the asset details page](assets/apply-branded-video-viewer-preset.png)

5. Copy the available delivery URL or embed code if you need to use the video elsewhere.

The available viewer options depend on the Dynamic Media environment and the preset's availability.

### Apply the preset in AEM Sites {#apply-preset-in-sites}

To use a video with a branded viewer preset on a Sites page:

1. Open the page in the **Sites editor**.
2. Add or select the **Dynamic Media** component.
3. Configure the component and select the video asset.
4. Select the appropriate viewer or preset from the available viewer settings.

   ![Select the branded video viewer preset in the Dynamic Media component](assets/select-branded-video-viewer-preset-sites.png)

5. Save the page and preview the video.

The selected preset controls the playback experience according to its configured settings and the capabilities of the selected viewer.

## Apply a preset using a playback URL {#apply-preset-using-playback-url}

Some Dynamic Media delivery environments support selecting a viewer preset through a playback URL parameter.

Use the parameter supported by your environment and confirm the required syntax with the corresponding delivery documentation before using it in production. Parameter names and supported workflows can differ between Dynamic Media environments.

Do not assume that a parameter supported by one delivery environment is supported by another.

## Important considerations {#important-considerations}

* A branded video viewer preset is reusable. You can apply it to multiple videos instead of configuring the same appearance and playback options for each asset.
* Changes to a preset can affect the playback experience wherever that preset is used. Review the impact before updating a preset used by published content.
* Available settings and application workflows can differ between Dynamic Media delivery environments.
* Ensure that the preset is published or approved, as required by your environment, before using it for video delivery.
* Preview the video after applying a preset to verify its appearance, playback behavior, and available controls.
* Test custom CSS and other advanced settings with the supported viewer to confirm the expected behavior.