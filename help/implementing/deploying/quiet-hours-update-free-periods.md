---
title: Automatic update quiet hours and update free periods
description: Learn how to configure quiet hours and update free periods for your ongoing programs.
feature: Deploying
role: Admin
---
# Quiet hours and Update free periods {#quiet-hours-update-free-periods}

BETA NOTE

The AEM as a Cloud Service [automatic maintenance updates](/help/implementing/deploying/aem-version-updates.md) ensure that your instances stay secure and up to date with the latest maintenance releases. That said, in some cases (like go-live events) you might need to "protect' those critical buisness operations from any potential disruptions. As such, AEM as a Cloud Service offers the option to set a window of time where automatic updates do not occur, . You can configure these time frames by using two scheduling options:

* **Quiet hours** - You can define a time interval within a 24 hour day where updates will not occur.
* **Update free periods** - You can define a 7 day time period where updates will not occur. You can define up to three update free periods within a 12-month timeframe.

The update free periods and quiet hours features can be configured on a "per program" basis.

## Quiet hours {#quiet-hours}

By using the quiet hours feature you can define a time window during the day and all maintenance updates will automatically shift to occur outside this window. If, for example, an update is scheduled during your specified quiet hours, it will automatically start after the specified quiet hour interval ends. The configured time interval cannot exceed 8 hours ensuring updates can still occur daily.

You can define the time interval by using the AEM Cloud Manager interface. As mentioned earlier you can set up to 8 hours of quiet time **per environment**, using your local timezone. 

### How to configure the quiet hours interval {#configure-quiet-hours}

The quiet hours feature can be configured by using the AEM Cloud Manager interface as follows:

Go to **Activities >Automatic Updates>Update Options**.

SCREENSHOT

1. Make sure the Use Quiet Hours option is toggled.
2. Click Edit.
3. Set quiet hours interval in the configuration window.

SCREENSHOT

Once set, your specified start and end hours apply automatically to every calendar day moving forward. You can disable or re-configure the quiet hours time value as needed.

## Update free periods {#update-hours}

By using the update free periods feature you can define a 7 day time frame where updates will not occur. Once configured, all maintenance updates will automatically shift to occur outside this window. You can have up to 3 update free periods within a 12-month timeframe. Additionally, update free periods can be designated up to one year in advance. Keep in mind when configuring this option that (at least) a one-week interval between time periods is mandatory in order to facilitate automatic updates.

### How to configure the update free periods {#configure-update-free-periods}

The update free periods feature can be configured by using the AEM Cloud Manager interface as follows:

Go to **Activities >Automatic Updates>Update Options**.

SCREENSHOT

Go to the update free periods section.
Click Add Update Free Period .
Select the one week update free period from the calendar.

SCREENSHOT

An **Active** icon will be displayed new the currently active update free period.
