---
title: Installing and Configuring Players in Screens as a Cloud Service
description: This page describes how to install and configure players in Screens as a Cloud Service.
exl-id: a022738a-c543-4629-a244-f70fa294fe7f
feature: Developing Screens
role: Admin, Developer, User
---
# Installing and Configuring Players in Screens as a Cloud Service {#installing-players-screens-cloud}

This section describes how to install AEM Screens players that are registered to on-premise AEM instances. Also, you must do a factory reset of the existing player and then register the new player against AEM Screens as a Cloud Service.

## Objective {#objective}

This document helps you understand how to set up your player before registering the players. After reading, you should be able to understand the following:

* where to install the players from
* how to update the player to Cloud mode

## Steps to Set the Player to Cloud Mode {#cloud-mode-setup}

After you have downloaded the latest player from [AEM Screens Player Downloads](https://download.macromedia.com/screens/), you are now ready to update your player to Cloud mode.

Follow the steps below to update your player:

1. Open AEM Screens player.

   >[!NOTE]
   >You can choose to test with dedicated hardware devices or with a web extension on your own player.

1. Click the **Configuration** tab and click **To Factory** button under **Reset** option.

   ![To Factory button under Reset option](/help/screens-cloud/assets/player/installplayer-2.png)

1. Click **Confirm** to reset your player.

1. Again from the **Configuration** tab and click **Change to Cloud Mode** button under **Toggle Runmode** option.

   ![Change to Cloud Mode button under Toggle Runmode option](/help/screens-cloud/assets/player/installplayer-1.png)

1. Click **Confirm** that prompts when switching to cloud mode unregisters the player.

## Basic Playback Monitoring {#playback-monitoring}

The player reports various playback metrics with each `ping` that defaults to 30 seconds. Based on these metrics, Adobe can detect various edge cases such as stuck experience, blank screen, and scheduling issues. This detection lets us understand and troubleshoot issues on the device, and therefore expedites an investigation and corrective measures with you.

Basic Playback monitoring in an AEM Screens player allows us to:

* Remotely monitor, if a player is properly playing content.

* Improve reactivity to blank screens or broken experiences in the field.

* Decreases the risk of showing a broken experience to the user.

### Understanding Properties {#understand-properties}

The following properties are included in each `ping`:

|Property|Description|
|---|---|
|id {string}|the player identifier|
|activeChannel {string}|currently playing channel path, or null if nothing is scheduled|
|activeElements {string}|comma-separated string, currently visible elements in all playing sequence channels (multiple if there was a multi-zone layout)|
|isDefaultContent {boolean}|true if the playing channel is considered a default or fallback channel (that is, has priority 1 and no schedule)|
|hasContentChanged {boolean}|true if the content changed in the last 5 minutes, false otherwise|
|lastContentChange {string}|timestamp of the last content change|

>[!NOTE]
>
>Optionally, you can enable a more advanced property from the player preferences (Enable Playback Monitoring):
>
>|Property|Description|
>|---|---|
>|isContentRendering {boolean}|true if the GPU can confirm it is playing actual content (based on pixel analysis)|

### Limitations {#limitations}

Few limitations to basic playback monitoring are listed below:

* The player reports its own playback state to the server, so it requires an active connection.

* The `isContentRendering` property that checks the GPU is overly resource intensive to be enabled by default and requires explicit opt-in from the player preferences. It is recommended not to use it with videos in production.

* This feature is only supported for sequence channels and does not yet cover the interactive channels (SPA) use case.

* The metrics are not yet fully exposed to customers; Adobe is working on enabling dashboard-like reporting and alerting mechanism soon.

## What's Next {#whats-next}

Now that you have installed and configured the player to Cloud mode, continue your Screens as a Cloud Service journey. See [Registering Players in Screens as a Cloud Service](/help/screens-cloud/managing-players-registration/registering-players-screens-cloud.md) from Screens Services Provider.
