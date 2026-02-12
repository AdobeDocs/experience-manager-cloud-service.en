---
title: New video Viewer
description: The New Video Viewer in Dynamic Media provides an enhanced video playback experience
  with improved performance, accessibility, and configurability.
role: User, Developer
exl-id:
---

# New Video Viewer in Dynamic Media {#new-video-viewer-dynamic-media}

The New Video Viewer for Dynamic Media introduces a modernized video playback experience in Adobe Experience Manager (AEM). It delivers a consistent and extensible viewing experience across authoring, preview, and Sites environments, while continuing to work with existing Dynamic Media workflows.

Existing video viewers in Dynamic Media support core playback requirements but offer limited extensibility and event-level integration for modern analytics and integration scenarios.

The New Video Viewer addresses these limitations by:

* Providing a more consistent playback experience  
* Allowing explicit viewer selection  
* Emitting structured playback events for programmatic consumption  
* Supporting integration with external analytics and external systems  

The viewer is available as an additional option and must be explicitly selected where supported. It does not automatically replace existing video viewers.

The New Video Viewer is intended for organizations that want an enhanced and extensible video experience without disrupting existing implementations.

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
| Dynamic Media sync | The asset folder must be synced with Dynamic Media |
| Video profile | A video profile must be applied to the folder |
| Video asset | A video must be ingested into the folder |

![Folder synced with Dynamic Media](assets/folder-syncing-with-dm.jpeg)

The New Video Viewer is available starting with **AEM as a Cloud Service version 2025.7.0**.

* To enable the New Video Viewer, contact your organization’s Adobe Customer Care representative.  
* To disable the New Video Viewer, contact Adobe Customer Care.  

>[!NOTE]
>This feature will be available as a **Limited Availability** feature. Email [aemcs-update-free@adobe.com](mailto:aemcs-update-free@adobe.com) to have the feature activated on your programs.

## Preview the New Video Viewer {#preview}

Execute the following steps to preview the New Video Viewer from the asset details page:

1. Open a video asset that meets the prerequisites.  
2. In the **Viewer rail**, select **Video (new)**.  
3. Click **Copy URL** to obtain the preview link.

![Viewer rail – Video (new)](assets/viewer-rail.jpeg)

## Use the New Video Viewer in Sites {#use-in-sites}

The New Video Viewer is available through the existing **Dynamic Media** component in AEM Sites.

### Add the Dynamic Media component

Execute the following steps to add the Dynamic Media component to a page:

1. Open the page in the **Sites editor**.  
2. Drag the **Dynamic Media** component onto the page.  
3. Click the asset placeholder in the component and select a video asset to add it.

![Drag Dynamic Media component](assets/drag-component.jpeg)

### Configure the viewer

1. Select the **Dynamic Media** component on your page.  
2. Click the **wrench icon** in the component toolbar to open the **Dynamic Media** settings dialog.  
   ![Open Dynamic Media settings](assets/open-settings.jpeg)

3. In the **Dynamic Media** settings dialog, open the **Viewer Preset** drop-down list and select **Video (new)**.  
   ![Select Video (new) viewer preset](assets/viewer-preset.jpeg)

4. Enter any required modifiers in the **Viewer Modifiers** field (e.g., `autoplay=true&muted=true`).  
   ![Viewer modifiers](assets/additional-modifiers.jpeg)

5. Click the **checkmark icon** to save the configuration.

The video will now load on the page using the New Video Viewer.

## Viewer modifiers {#viewer-modifiers}

Viewer modifiers allow you to control playback behavior.

| Modifier | Description |
|--------|-------------|
| `autoplay=true` | Automatically starts playback |
| `muted=true` | Starts playback in a muted state |

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

# Video Engagement Report for the New Video Viewer

The Video Engagement Report provides analytics metrics for videos played using the New Video Viewer in Dynamic Media. The report delivers aggregated performance data for selected date ranges and supports both daily and monthly reporting.

Reports are generated upon request. Customers must raise a Jira ticket to receive either a scheduled monthly report or an ad-hoc report.

The report provides per-video engagement metrics, including views, impressions, watch time, completion rate, and engagement score.

## Supported regions

Video engagement reporting is supported in the following regions:

* NA (North America)
* EMEA (Europe, Middle East, Africa)
* APAC (Asia Pacific)
* Polaris

## Report types

### Daily report

* Supports date range filtering.
* Date format: `YYYY-MM-DD`.
* Metrics are aggregated across the selected date range.

### Monthly report

* Supports month range filtering.
* Month format: `YYYY-MM-01`.
* Metrics are aggregated at the month level.

## Report format

* Reports are delivered in CSV format.
* Each row represents a single video.
* Metrics are aggregated for the selected reporting period.
* Deleted assets are excluded from the report.
* Supports filtering by `tenant_name`.

## Report fields

The Video Engagement Report includes the following fields:

| Field | Description |
|-------|------------|
| `video_id` | Unique video identifier. |
| `video_name` | Name of the video asset. |
| `video_created_date` | Date the video was created. |
| `duration_in_seconds` | Duration of the video in seconds. |
| `video_views` | Total number of video play events during the selected reporting period. |
| `video_impressions` | Total number of times the video was loaded. |
| `video_watched_seconds` | Total seconds watched across all play events. |
| `play_rate` | Percentage calculated as (video_views ÷ video_impressions) × 100. |
| `avg_time_watched_in_seconds` | Average seconds watched per view (video_watched_seconds ÷ video_views). |
| `avg_completion_rate` | Percentage of views that reached full video completion. |
| `engagement_score` | Average watch percentage across all play events. |
| `tenant_name` | Identifier of the company or tenant associated with the data. |

## Engagement metric calculations

The report includes the following calculated metrics:

* **Play rate**  
  (video_views ÷ video_impressions) × 100

* **Average time watched (seconds)**  
  video_watched_seconds ÷ video_views

* **Average completion rate**  
  Percentage of views that reached the full video duration

* **Engagement score**  
  Average watch percentage across all play events

Percentage-based values are represented as numeric percentages in the report.