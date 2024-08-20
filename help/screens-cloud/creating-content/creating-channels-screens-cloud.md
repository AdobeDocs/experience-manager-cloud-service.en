---
title: Creating and Managing Channels in Screens as a Cloud Service
description: This page describes how to create and manage channels in Screens as a Cloud Service.
exl-id: 3b0bae7a-4a45-485a-ab04-604510ff6578
feature: Authoring Screens
role: Admin, Developer, User
---
# Creating and Managing a Channel in Screens as a Cloud Service {#creating-channels-screens-cloud}

Once you have created an AEM Screens Project, you must create channels.
***Channels***, display a sequence of content (images and videos), a website, or a single-page application.

## Objective {#objective}

This document helps you understand creating and managing channels for your AEM Screens project in Screens Content Provider. After reading you should be to:

* understand how to create channels to Screens Content Provider
* manage and edit content in your channels
* manage assignment and activation schedule for your channels in [Screens Service Provider](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/screens-as-cloud-service/configure-screens-cloud/navigating-to-screens-services-provider.html?lang=en)

## Steps to Create a New Sequence Channel in Screens as a Cloud Service {#create-new-channel}

>[!NOTE]
>**Prerequisites**
>Before starting this section of the Guide, review [Creating and Managing Projects in Screens as a Cloud Service](/help/screens-cloud/creating-content/creating-projects-screens-cloud.md).

Follow the steps below to create a sequence channel in Screens as a Cloud Service:

1. Navigate to Screens Content Provider.

1. Navigate to your AEM Screens project, such as *FirstDigitalExperience*.

1. Select the **Channels** folder from your project, such as **FirstDigitalExperience** --> **Channels** and click **Create** from the action bar.

   ![channel-create1](/help/screens-cloud/assets/create-content/channel-create1.png)

1. Select the template, such as, **Sequence Channel** from the **Create** wizard and click **Next**.

   ![channel-create2](/help/screens-cloud/assets/create-content/channel-create2.png)

   >[!NOTE]
   > The **Create** wizard provides different types of templates while creating a channel. See [Available Templates](#available-templates) in Create Wizard for more details.

1. Enter the name of your sequence channel, such as, **LoopingChannelOne** and click **Create**.

   ![channel-create3](/help/screens-cloud/assets/create-content/channel-create3.png)

   You will now see a **LoopingChannelOne** in your Channels folder in your AEM Screens project.

   Once you have created the channel, you can now add content to  your channel. See [Adding Content to a Channel](#add-content) to learn how  to add assets (images/videos) to  your channel.

## Managing a Channel {#managing-channels}

You can edit, view properties and dashboard, copy, preview, and delete a channel.

Navigate to the channel from your project and select the channel, as shown in the figure below. You can now select the options such as editing the channel, viewing properties, previewing content, managing publication, or deleting the channel from the action bar.

![channelprop1](/help/screens-cloud/assets/create-content/channelprop1.png)

### Adding Content to a Channel {#add-content}

To add or edit content in a channel, follow the steps below:

1. Select the channel you want to edit, as shown in the figure below. Click **Edit** from the top left corner of the action bar to open the editor.

   ![edit-channel1](/help/screens-cloud/assets/create-content/edit-channel1.png)

1. The editor lets you add assets/components to your channel that you want to publish.

1. Drag and drop the assets from the left hand side pane and add it to the editor.

    ![edit-channel2](/help/screens-cloud/assets/create-content/edit-channel2.png)

   >[!NOTE]
   >Click **Preview** to preview the contents of your channel.
   >![edit-channelpreview](/help/screens-cloud/assets/create-content/edit-channelpreview.png)

## Available Templates in Create Wizard {#available-templates}

The following templates are available while using the **Create** channel wizard:

|Available Templates|Description|
|--- |--- |
|Channels Folder|Lets you create a folder to store collection of channels.|
|Sequence Channel|Lets you create a channel that plays the components sequentially (one by one in a slide show).|
|Left or Right L-Bar Split Screen Channel|Allows content authors to view different types of assets in appropriately sized zones.|

## Use default assignment details for channels {#default-channels}

This capability lets you define a default activation schedule for a channel, and use it by default for every assignment for a display. This provides a method so that the cumbersome schedule definition does not need to be repeated.

1. Navigate to the [Screens Services Provider](https://experience.adobe.com/screens).

### Create default assignment details for a channel {#create-default}

1. Navigate to the details page for the channel you want to configure.
1. Locate the **Default assignment details** tile on the page.

   ![image](/help/screens-cloud/assets/display/Assignment1.png)

1. Click **Set default details**.
1. Configure the default assignment details, including priority, start & end dates, and recurrence patterns for the channel, and click **Assign**.

   ![image](/help/screens-cloud/assets/display/Assignments2.png)

1. Notice the details of the assignment are shown in the **Default assignment details** tile:

   ![image](/help/screens-cloud/assets/display/Assignments3.png)

This tile displays the following information:
* Default priority of the channel in the display.
* Activation start and end dates when the channel is scheduled to play.
* Synthetic view of the recurrence (Hourly/Daily/Weekly/Monthly/Yearly and name given to that recurrence).

### Use the default assignment details when assigning to a display {#default-display}

Channels having default assignment details can be assigned to displays the same way regular channels are, with the added option to use the default assignment details instead of manually defining custom ones each time.

1. Navigate to the display details page you want to assign the channel to and click the **Assign channel**.
alternatively, select the desired display in the [inventory](https://experience.adobe.com/screens/displays) view and click the **Assign channel**.
1. The channel assignment dialog opens.

   ![image](/help/screens-cloud/assets/display/Assignments4.png)

1. Select the desired channel that has the default assignment details from the channel picker.
1. Notice the channel assignment dialog changes to let you choose the default assignment details, or select custom ones:

   ![image](/help/screens-cloud/assets/display/Assignments5.png)

1. Click **Assign** to finalize the assignment, or click **Set custom assignment details** if you prefer overriding the defaults with some other values in the context of that particular display.

   ![image](/help/screens-cloud/assets/display/Assignments6.png)

1. Notice the **Assigned channels** tile is updated with the new assignment:

   ![image](/help/screens-cloud/assets/display/Assignments7.png)

1. Notice that the channels will have a different icon depending on if they are using custom schedules (Clock icon) or inheriting the default details (World clock icon), and clicking those will show the scheduling details.
1. Also notice that available actions for each type will differ.

   ![image](/help/screens-cloud/assets/display/Assignments8.png)

**Note:** A channel assignment that uses the default assignment details will not be editable in the context of the display.

* If you must change it to a custom assignment, first remove it and then add it again using the **Set custom assignment details** option.
* If you must change the properties of the default assignment details, do so directly from the channel details page.

### Remove default assignment details from a channel {#remove-display}

1. Navigate to the details page for the channel you want to remove the default assignment details.
1. Locate the **Default assignment details** tile in the page
1. Click the **Remove default**.

   ![image](/help/screens-cloud/assets/display/Assignments9.png)

1. A confirmation dialog is shown, and details match one of the following conditions:
**a.** Channel is not used in any display.

   ![image](/help/screens-cloud/assets/display/Assignments10.png)

**b.** Channel is used in a single display.

   ![image](/help/screens-cloud/assets/display/Assignment11.png)

**c.** Channel is used in several displays.

   ![image](/help/screens-cloud/assets/display/Assignments12.png)

1. Click the *Remove* to validate the change.

**Note:** Removing the default assignment details from a channel will remove the matching assignments on all displays that were using it.
As a consequence, this may lead to blank screens if there is no alternate content to be played on those displays.

## What's Next {#whats-next}

Now, that you have setup an AEM Screens channel in your project, you need to publish your channel. See [Publishing Channels in Screens as a Cloud Service](manage-publish.md) before managing your players from Screens Services Provider.
