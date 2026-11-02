---
title: Assigning Channel to a Display in Screens as a Cloud Service
description: This page describes how to assign a channel to a display in Screens as a Cloud Service.
exl-id: ba001c18-7b05-4ae2-aa7f-9ebb320fedd0
feature: Authoring Screens
role: Admin, Developer, User
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
---
# Assigning Channel to a Display in Screens as a Cloud Service {#assign-channel-displays-screens-cloud}

After the project setup is complete, you must assign the channel to a display to view the content.

## Objective {#objective}

This document helps you understand how to assign a channel to a display, once your display  is ready and you have added content to your channel and published it. After reading, you should be able to understand how to assign a channel to a display from Screens Services Provider.

## Prerequisites {#prerequisites}

Before you perform the steps below to assign a channel to a display, you must have finished learning:

* Creating  and Managing Displays
* Creating and Managing Channels

## Steps to Assign a Channel to a Display {#assign-channel-to-display}

Follow the steps below to assign a channel to a display:

1. Navigate to Screens Services Provider and select **Displays** from the left navigation panel. 

1. Click **Assign Channel** to the display.

   ![image](/help/screens-cloud/assets/display/assignchannel-1.png)

1. Populate the following fields from **Assign a channel** dialog box.

   ![image](/help/screens-cloud/assets/display/assignchannel-2.png)

   1. Select the channel name from the drop-down.
   1. Choose the priority.

      >[!NOTE]
      >Priority is used to order the assignments in case multiple ones match the playing criteria. The one with the highest value always takes precedence over lower values. For example, if there are two channels A and B. A has a priority of 1 and B has a priority of 2, then channel B is displayed, as it has a higher priority than A.
   
   1. Select the start date and end date from **Activation**.

1. Click **+ Add recurrence** to add a recurrence schedule for your channel.

   ![image](/help/screens-cloud/assets/create-content/recurrence-1.png)

      >[!NOTE]
      >You can add multiple recurring schedules to your channel. Recurrence schedules introduce DayParting that lets you set a global schedule with multiple channels running at specific times of the day, and reuse that set up for all your displays at once.

   You can set the following options:

   * **Name**: Title of your recurrence schedule.
   * **Repeat**: Choose whether the schedule runs Daily, Weekly, Monthly, or Yearly.
   * **Start**: The start time for your schedule.
   * **End**: The ending time for your schedule. You can set it by time or duration.
   * **Time**: The schedule ends at a specified time.
   * **Duration**: The schedule runs for a particular duration of time in hours or minutes.
      
1. Click **Create**. You can see that a channel is assigned for that display, as shown in the figure below.

      ![image](/help/screens-cloud/assets/display/assignchannel-3.png)


## What's Next {#whats-next}

Now, that you have assigned the channel to a display, you should continue your Screens as a Cloud Service journey by next reviewing the document [Installing and Configuring Screens Player for AEM as a Cloud Service](/help/screens-cloud/managing-players-registration/installing-screens-cloud-player.md).
