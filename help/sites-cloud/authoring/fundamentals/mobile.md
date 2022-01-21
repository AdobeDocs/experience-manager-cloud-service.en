---
title: Authoring a Page for Mobile Devices
description: When authoring for mobile, you can switch between several emulators to see what the end-user sees
exl-id: fabd4468-3304-402f-9522-342da3bbae94
---
# Authoring a Page for Mobile Devices {#authoring-a-page-for-mobile-devices}

Adobe Experience Manager pages are based on a responsive layout. [Responsive layout](/help/sites-cloud/authoring/features/responsive-layout.md) adapts your content to fit the target device automatically, eliminating the need to author content for specific devices.

When authoring a mobile page, the page is displayed in a way that emulates the mobile device. When authoring the page, you can switch between several emulators to see what the end-user sees when accessing the page.

Devices are grouped into the categories feature, smart, and touch according to the capabilities of the devices to render a page. When the end-user accesses a mobile page, AEM detects the device and sends the representation that corresponds to its device group.

>[!NOTE]
>
>To create a mobile site based on an existing standard site, create a live copy of the standard site. See [Creating Live Copies.](/help/sites-cloud/administering/msm/creating-live-copies.md)
>
>AEM developers can create new device groups. See Creating Device Group Filters.

<!--
>AEM developers can create new device groups. (See [Creating Device Group Filters](/help/sites-developing/groupfilters.md).)
-->

Use the following procedure to author a mobile page:

1. From global navigation open the **Sites** console.
1. Edit a content page.
1. Switch to the desired emulator by clicking the **Emulator** icon at the top of the page.

   ![Emulator icon](/help/sites-cloud/authoring/assets/emulator.png)

1. Drag and drop components from the component browser or asset browser on to the page.
1. [Modify the responsive layout](/help/sites-cloud/authoring/features/responsive-layout.md) of the page and its components based on the selected device.

The page will look similar to the following:

![Mobile example](/help/sites-cloud/authoring/assets/mobile.png)

>[!NOTE]
>
>The emulators are disabled when a page on the author instance is requested from a mobile device.
