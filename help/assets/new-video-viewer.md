---
title: New video Viewer
description: The New Video Viewer in Dynamic Media provides an enhanced video playback experience
  with improved performance, accessibility, and configurability.
role: User, Developer
exl-id:
---

# New Video Viewer in Dynamic Media {#new-video-viewer-dynamic-media}

The New Video Viewer for Dynamic Media provides a modernized video playback experience in Adobe Experience Manager (AEM). It delivers a consistent and extensible viewing experience across authoring, preview, and Sites environments, while continuing to work with existing Dynamic Media workflows.

Existing video viewers in Dynamic Media support core playback requirements but provide limited extensibility and event-level integration for modern analytics and integration scenarios.

The New Video Viewer addresses these limitations by:

* Providing a more consistent playback experience  
* Allowing explicit viewer selection  
* Emitting structured playback events for programmatic consumption  
* Supporting integration with external analytics and external systems  

The viewer is available as an additional option and requires explicit selection where supported. It does not automatically replace existing video viewers.

The New Video Viewer is intended for organizations that require an enhanced and extensible video experience without disrupting existing implementations.

> **Note:** The New Video Viewer is available only in selected environments. Availability depends on feature enablement and may vary by account.

## How the New Video Viewer works {#how-it-works}

The New Video Viewer works as follows:

1. A video asset is ingested into a folder that is synced with Dynamic Media.
2. The video can be previewed from the asset details page using **Video (new)**.
3. The New Video Viewer can be selected in the **Dynamic Media** component when authoring Sites pages.
4. During playback, the viewer emits structured events to the parent window.
5. Optional viewer modifiers can be used to control playback behavior.

## Key differences from the existing Video Viewer {#key-differences}

| Area | Description |
|------|-------------|
| Viewer availability | Appears as a new option named **Video (new)** |
| Viewer selection | Must be explicitly selected |
| Extensibility | Emits structured playback events |
| Integration | Continues to work with existing Dynamic Media workflows |

## Prerequisites {#prerequisites}

Before using the New Video Viewer, ensure the following prerequisites are met:

| Requirement | Description |
|------------|-------------|
| Dynamic Media sync | The asset folder must be synced with Dynamic Media. |
| Video profile | A video profile must be applied to the folder. |
| Video asset | A video must be ingested into the folder. |

The New Video Viewer is available starting with **AEM as a Cloud Service version 2025.7.0**

To enable or disable the New Video Viewer, contact Adobe Customer Care.

> **NOTE**
>
> The New Video Viewer is a limited availability feature. You can get it enabled by creating a [support ticket](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

## Preview the New Video Viewer {#preview}

Execute the following steps to preview the New Video Viewer from the asset details page:

1. Navigate to **Assets** > **Files**, and open the folder containing the video asset.
2. Click the video asset to open the asset details page.
3. In the left panel, click **Viewers**.
4. In the **Viewers** panel, select **Video (new)**.
5. Click **Copy URL** to copy the preview link.

## Use the New Video Viewer in Sites {#use-in-sites}

The New Video Viewer is available through the existing **Dynamic Media** component in AEM Sites.

### Add the Dynamic Media component

Execute the following steps to add a video using the Dynamic Media component:

1. Open the page in the **Sites editor**.
2. Drag the **Dynamic Media** component to the required location on the page.
3. Select the **Dynamic Media** component on the page.
4. Click the component to open the asset selector.
5. Select a video asset.

![Drag Dynamic Media component](assets/drag-component.jpeg)

### Configure the viewer

Execute the following steps to configure the viewer preset:

1. Select the **Dynamic Media** component on the page.
2. Click **Settings** in the component toolbar.
   ![Open Dynamic Media settings](assets/open-settings.jpeg)

3. In the **Dynamic Media settings dialog**, select **Video (new)** from the **Viewer Preset** drop-down list.
   ![Select Video (new) viewer preset](assets/viewer-preset.jpeg)

4. Enter any required modifiers in the **Viewer Modifiers** field (for example, `autoplay=true&muted=true`).
   ![Viewer modifiers](assets/additional-modifiers.jpeg)

5. Save the changes.

The video will now load on the page using the New Video Viewer.

## Viewer modifiers {#viewer-modifiers}

Viewer modifiers allow you to control asset loading, playback behavior, streaming format selection, and viewer presentation.

| Modifier | Description |
|--------|-------------|
| `asset` | Specifies the asset ID of the video or Adaptive Video Set. |
| `posterimage` | Specifies the image displayed before playback starts. |
| `serverurl` | Specifies the Image Serving root path. |
| `contenturl` | Specifies the content root path. |
| `videoserverurl` | Specifies the video server root path. |
| `sources.dash` | Specifies the DASH manifest URL for playback. |
| `sources.hls` | Specifies the HLS manifest URL for playback. |
| `autoplay=true` | Starts playback automatically when the video loads. |
| `controls=true/false` | Shows or hides the video playback controls. |
| `loop=true` | Restarts playback automatically after the video ends. |
| `muted=true` | Starts playback in a muted state. |
| `playbackrates` | Specifies the available playback speed options. |
| `playback` | Specifies the streaming format (auto, hls, dash, or progressive). |
| `progressivebitrate` | Specifies the bitrate for progressive playback. |
| `initialbitrate` | Specifies the initial bitrate for adaptive streaming. |
| `isletterboxed=true/false` | Controls whether the video is letterboxed or stretched. |
| `customcss` | Specifies a custom CSS file for viewer styling. |
| `transition` | Specifies the show or hide transition behavior for viewer controls. |

Modifiers are specified as query parameters in the **Viewer Modifiers** field.

## Supported events {#supported-events}

The New Video Viewer emits the following events during playback:

| Event type | Description |
|-----------|-------------|
| play | Video starts playing |
| pause | Video is paused |
| seek | User seeks within the video |
| load | Video is loaded |
| close | Player is closed |
| metadata | Metadata such as duration |
| milestone | Playback milestone reached |
| current_time | Periodic playback position |
| fullscreen | Enter fullscreen |
| un_fullscreen | Exit fullscreen |

## Handling events in the parent window {#handling-events}

The New Video Viewer sends playback-related messages to the parent page during video interactions. 

To handle these events, the parent application must listen for browser message events and validate the message origin before processing the data.

The event payload includes information such as the event type, playback state, current playback time, and additional metadata. These events can be used to support analytics tracking, custom interactions, or integration with external systems.

Adobe recommends validating the message origin to ensure that events are processed only from trusted Dynamic Media domains.

## Video Engagement Report for the New Video Viewer {#video-engagement-report}

The Video Engagement Report provides analytics metrics for videos played using the New Video Viewer in Dynamic Media. The report delivers aggregated performance data for selected date ranges and supports both daily and monthly reporting.

Reports are generated upon request. To request a report, create a [support ticket](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) and provide the following details:

* Required report type (ad-hoc or scheduled monthly)
* Reporting date range
* Delivery email address or contact details where the report should be sent

After the request is submitted, Adobe Customer Support reviews the request and forwards it to the engineering team for report generation. Once the report is generated, Adobe Customer Support delivers the report.

The report provides per-video engagement metrics, including views, impressions, watch time, completion rate, and engagement score.

### Supported regions

Video engagement reporting is supported in the following regions:

* NA (North America)
* EMEA (Europe, Middle East, Africa)
* APAC (Asia Pacific)
* Polaris

### Report type

The system provides the Monthly report to view aggregated video engagement metrics.

#### Monthly report

* Supports month range filtering.
* Month format: `YYYY-MM-01`.
* Metrics are aggregated at the month level.

### Report format

* Reports are delivered in CSV format.
* Each row represents a single video.
* Metrics are aggregated for the selected reporting period.
* Deleted assets are excluded from the report.
* Supports filtering by `tenant_name`.

### Report fields

The Video Engagement Report includes the following fields:

| Field | Description | Calculation |
|-------|------------|-------------|
| `video_id` | Unique video identifier. | NA |
| `video_name` | Name of the video asset. | NA |
| `video_created_date` | Date the video was created. | NA |
| `duration_in_seconds` | Duration of the video in seconds. | NA |
| `video_views` | Total number of video play events during the selected reporting period. | NA |
| `video_impressions` | Total number of times the video was loaded. | NA |
| `video_watched_seconds` | Total seconds watched across all play events. | Sum of seconds watched across all play events |
| `play_rate` | Percentage of video plays relative to video loads. | (`video_views` ÷ `video_impressions`) × 100 |
| `avg_time_watched_in_seconds` | Average seconds watched per view. | `video_watched_seconds` ÷ `video_views` |
| `avg_completion_rate` | Percentage of views that reached full video completion. | (Completed views ÷ `video_views`) × 100 |
| `engagement_score` | Average watch percentage across all play events. | Average watch percentage across all play events |
| `tenant_name` | Identifier of the company or tenant associated with the data. | NA |
