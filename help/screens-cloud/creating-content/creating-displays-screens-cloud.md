---
title: Creating and Managing Displays in Screens as a Cloud Service
description: This page describes how to create and manage displays in Screens as a Cloud Service.
exl-id: 0f9faa4b-b50e-40f8-a8ed-280f8bd0a9b8
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
# Creating and Managing Displays in Screens as a Cloud Service {#create-displays-screens-cloud}

Once you have published your channel, it is now time to create your display in the Screens Services Provider.

A Display is a virtual grouping of screens that are usually positioned next to each other. The display is usually permanent in respect to an installation. This object content is what authors work with and always reference to as logical display rather than their physical counter parts.

## Objective {#objective}

This document helps you understand how to create and manage displays in the Screens Services Provider. After reading you should:

* Understand how to create and delete displays
* Understand how to organize your displays into folders

## Steps to Create a Display {#create-display}

Follow the steps below to create the display from the Screens Services Provider:

1. Navigate to Screens Services Provider from your AEM Cloud Service instance.
1. Select **Displays** from the left navigation panel and click **Create** from the upper-right corner of the screen.

   ![image](/help/screens-cloud/assets/display/disp-1.png)

1. Select **Display** from the action bar.

   ![image](/help/screens-cloud/assets/display/disp-2.png)

1. Enter the title as **LoopingChannelDisplay** in **Display Name** and click **Create**.

   ![image](/help/screens-cloud/assets/display/disp3.png)

1. The display titled as **LoopingChannelDisplay** will now be visible in the display list.

   ![image](/help/screens-cloud/assets/display/disp-4.png)

### Deleting a Display {#deleting-display}

You can delete a display from Screens Services Provider.

Select the display and click **Delete** from the bottom of the panel, as shown in the figure below.

   ![image](/help/screens-cloud/assets/display/disp-5.png)

## Steps to Organize displays into folders {#organize-display}

## How to toggle the folder rail {#toggle-rail}

You can switch the folder rail from displaying all the folders to specific folders:

1. Navigate to the displays inventory view by clicking the button highlighted below:

   ![image](/help/screens-cloud/assets/display/display-inventory.png)

1. The folder side-rail is displayed.

   ![image](/help/screens-cloud/assets/display/toggle-rail.png)

1. Select **Hide Folders** to close it again.

## How to create a folder {#create-folder}

You can create folders to better organize your displays.

1. Navigate to the displays inventory view.
1. Ensure you are not currently in a folder, your should see the following:

   ![image](/help/screens-cloud/assets/display/verify-view.png)

   Note: **All Displays** should be selected in the folder side rail and the breadcrumb navigation should only show **Displays**.

1. Click the "Create" button on the top right and select the **Folder** option.

   ![image](/help/screens-cloud/assets/display/Createfolder.png)

1. Fill in the title for the new folder and click **Create**.

   ![image](/help/screens-cloud/assets/display/Createfolder2.png)

## How to create a nested folder {#nested-folder}

1. Navigate to the displays inventory view.

1. Select the desired parent folder from the folder side rail or by browsing in the inventory view.
1. Verify the desired parent folder is selected.

   ![image](/help/screens-cloud/assets/display/Nestedview.png)

   * The folder should be selected in the folder side rail.
   * The breadcrumb navigation should show the current folder name next to **Displays**.

1. Click  **Create**  on the top right and select the **Folder** option.

   ![image](/help/screens-cloud/assets/display/Createfolder.png)

1. Fill in the title for the new folder and click **Create**.

   ![image](/help/screens-cloud/assets/display/Createfolder2.png)

## How to move content to a new folder {#move-folder}

You can move content to your new folders to better organize your displays.

1. Navigate to the displays inventory view.

1. Select the desired parent folder from the folder side rail or by selecting from the inventory view.

1. Verify you selected the desired parent folder.

 ![image](/help/screens-cloud/assets/display/movetofolder.png)

**Note**: The folder should be selected in the folder side rail. Also, the breadcrumb navigation should show the current folder name next to **Displays**.

## How to delete content from a folder {#delete-folder}

All folder operations are accessible via the selection action bar in inventory view.

1. Navigate to the parent folder or select it from the side rail.

1. In the inventory view, select the desired child folder you want to delete and ensure it is empty.

1. Click **Delete** action in the selection action bar. The action is disabled if the folder is not empty.


## What's Next {#whats-next}

Now, that you have learnt how to create and manage displays for your project, you should continue your Screens as a Cloud Service journey by next reviewing the document [Assigning Channel to a Display in Screens as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/screens-as-cloud-service/create-content/assigning-channels-to-display.html).
