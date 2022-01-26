---
title: Enable AEM Screens for Your Demo Site
description: Learn the extra steps to enable the full AEM Screens as a Cloud Service experience on your demo site.
---

# Enable AEM Screens for Your Demo Site {#enable-screens}

Learn the extra steps to enable the full AEM Screens as a Cloud Service experience on your demo site.

## The Story So Far {#story-so-far}

In the previous document of the AEM Quick Site Creation journey, [Manage Your Demo Sites,](manage.md) you learned how you can manage the demo sites you created. You should now:

* Understand how to access the Self-Service Demo Utilities.
* Know what utilities are available to you.
* How to delete an existing demo site or template.

Now that you have your own demo site to explore and understand the tools available to help you manage your demo sites, you can now enable the full AEM Screens as a Cloud Service experience for your demo sites.

## Objective {#objective}

The AEM Reference Demos Add-On contains AEM Screens content for We.Cafe, a coffee shop-type business vertical. This document helps you understand how to execute the We.Cafe demo setup in the context of AEM Screens. After reading you should:

* Know how to setup prerequisites.
* Understand the demo setup.

Before testing the features, the We.Cafe Site requires additional prerequisites.

## Understand Screens {#understand-screens}

AEM Screens as a Cloud Service is a digital signage solution that allows marketers to create and manage dynamic digital experiences at scale. With AEM Screens as a Cloud Service, you can create engaging and dynamic digital signage experiences intended to be consumed in public spaces.


[!TIP]
>
>For the full details of AEM Screens as a Cloud Service, see the [Additional Resources](#additional-resources) section at the end of this document.

By installing the AEM Reference Demos Add-On, you automatically have We.Cafe content for AEM Screens available to you in your demo authoring environment. The steps describe here allow you to enable the full AEM Screens experience by publishing that content and deploying to media players etc.

## Configure ContextHub {#configure-contexthub}

Just like AEM, AEM Screens can change content dynamically based on context. The We.Cafe demo has channels configured to show different content depending on the current temperature and it uses AEM's ContextHub to do this.

[!TIP]
>
>For the full details of ContextHub, see the [Additional Resources](#additional-resources) section at the end of this document.

Since it is very difficult to change the weather during a demo, temperature changes must be simulated. This is done using Google Sheets to provide the values as an external "weather service".

During the demo, the values in the sheet can be changed. ContextHub will recognize this and the content will adjust in the channel according to the updated temperature.

1. Create a new Google spreadsheet. Refer to the Google documentation **Using API Keys** as referenced under [AdditionalResources](#additional-resources) to configure the spreadsheet correctly.
1. Set the temperature in cell A2.
1. On the AEMaaCS author instance, go to  **Tools -&gt; Sites -&gt; ContextHub**.
1. Select the configuration container that has the same name as how you named the project when you imported the template.
1. Select  **Configuration -&gt; ContextHub Configuration -&gt; Google Sheets** then click **Next** at the top right.
1. The configuration should already have pre-configured JSON data. There are two values that need to be changed:
   1. Replace `<your Google Sheets id>` with ID of the sheet you created.
   1. Replace `<your Google API Key>` with your API key.
1. Click **Save**.

>[!ATTENTION]
>
>Only use the described Google Sheets solution for demo purposes. Adobe does not support using Google Sheets for production environments.

## Connect Screens as a Cloud Service {#connect-screens}

If you like to setup a real digital signage experience, including a player that runs on a digital signage device or on your computer, you can follow the next, optional steps.

Alternatively you can preview the demo simply in the Channel Editor on AEMaaCS.

>[!TIP]
>
>For the full details of the Channel Editor, see the [Additional Resources](#additional-resources) section at the end of this document.

1. Navigate to Screens as a Cloud Service.
1. Link the URLs of AEMaaCS author and publish instances in the settings
1. Create  a Display  and open it afterwards
1. Click  Assign channel  in the top right and select a channel that has been synced from your AEMaaCS instance
1. Download, register and assign a Player
   1. Download
   1. Register
   1. Assign Display to Player

## Understand the Demo Content {#demo-content}

The We.Cafe coffee shop is comprised of three shops in three locations in the US. All three shops have three similar experiences:

* A menu board above the counter with two or three vertical panels
* An entrance display facing the street with one horizontal or vertical panel inviting customers into the shop
* A quick self-order kiosk booth to bypass the queue with one vertical tablet

>[!NOTE]
>
>Only the entrance display can be tested in the current version of the demo. Other displays will follow in a future version.

The New-York location is assumed to be in a smaller shop that does not have a lot of space, and as such:

* The menu board only has two vertical panels instead of three for San Francisco and San Jose
* The entrance display is positioned vertically instead of horizontally as in the other locations
## Additional Resources {#additional-resources}

* [ContextHub documentation](/help/sites-cloud/authoring/personalization/contexthub.md)
* [Using API Keys - Google Documentation](https://developers.google.com/maps/documentation/javascript/get-api-key)