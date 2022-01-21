---
title: Creating and Managing Channels in Screens as a Cloud Service
description: This page describes how to create and manage channels in Screens as a Cloud Service.
exl-id: 3b0bae7a-4a45-485a-ab04-604510ff6578
---
# Creating and Managing a Channel in Screens as a Cloud Service {#creating-channels-screens-cloud}

Once you have created an AEM Screens Project, you must create channels.
***Channels***, display a sequence of content (images and videos), a website, or a single-page application.

## Objective {#objective}

This document helps you understand creating and managing channels for your AEM Screens project in Screens Content Provider. After reading you should be to:

* understand how to create channels to Screens Content Provider
* manage and edit content in your channels

## Steps to Create a New Sequence Channel in Screens as a Cloud Service {#create-new-channel}

>[!NOTE]
>**Prerequisites**
>Before starting this section of the Guide, please review [Creating and Managing Projects in Screens as a Cloud Service](/help/screens-cloud/creating-content/creating-projects-screens-cloud.md).

Follow the steps below to create a new sequence channel in Screens as a Cloud Service:

1. Navigate to Screens Content Provider.

1. Navigate to your AEM Screens project, such as *FirstDigitalExperience*.

1. Select the **Channels** folder from your project, such as **FirstDigitalExperience** --> **Channels** and click on **Create** from the action bar.

   ![](/help/screens-cloud/assets/create-content/channel-create1.png)

1. Select the template, such as, **Sequence Channel** from the **Create** wizard and click on **Next**.

   ![](/help/screens-cloud/assets/create-content/channel-create2.png)
   >[!NOTE]
   > The **Create** wizard provides different types of templates while creating a channel. Refer to the section [Available Templates](#available-templates) in Create Wizard for more details.

1. Enter the name of your sequence channel, such as, **LoopingChannelOne** and click on **Create**.

   ![](/help/screens-cloud/assets/create-content/channel-create3.png)

   You will now see a **LoopingChannelOne** in your Channels folder in your AEM Screens project.

   Once you have created the channel, you can now add content to  your channel. Refer to [Adding Content to a Channel](#add-content) to learn how  to add assets (images/videos) to  your channel.

## Managing a Channel {#managing-channels}

You can edit, view properties and dashboard, copy, preview, and delete a channel.

Navigate to the channel from your project and select the channel, as shown in the figure below. You can now select the options such as editing the channel, viewing properties, previewing content, managing publication, or deleting the channel from the action bar.

![](/help/screens-cloud/assets/create-content/channelprop1.png)

### Adding Content to a Channel {#add-content}

To add or edit content in a channel, follow the steps below:

1. Select the channel you want to edit, as shown in the figure below. Click on **Edit** from the top left corner of the action bar to open the editor.

   ![](/help/screens-cloud/assets/create-content/edit-channel1.png)

1. The editor allows you to add assets/components to your channel that you want to publish.

1. Drag and drop the assets from the left hand side pane and add it to the editor.

    ![](/help/screens-cloud/assets/create-content/edit-channel2.png)

   >[!NOTE]
   >Click on **Preview** to preview the contents of your channel.
   >![](/help/screens-cloud/assets/create-content/edit-channelpreview.png)

## Available Templates in Create Wizard {#available-templates}

The following templates are available while using the **Create** channel wizard:

|Available Templates|Description|
|--- |--- |
|Channels Folder|Allows to create a folder to store collection of channels.|
|Sequence Channel|Allows to create a channel that plays the components sequentially (one by one in a slide show).|
|Left or Right L-Bar Split Screen Channel|Allows content authors to view different types of assets in appropriately sized zones.|


## What's Next {#whats-next}

Now, that you have setup an AEM Screens channel in your project, you need to publish your channel. Refer to [Publishing Channels in Screens as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/screens-as-cloud-service/create-content/manage-publish.html?lang=en) before managing your players from Screens Services Provider.
