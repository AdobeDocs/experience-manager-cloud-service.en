---
title: Quiet hours and Update Free Periods
description: Learn how to configure quiet hours and update free periods for your ongoing programs so that automatic updates do not occur.
feature: Deploying
role: Admin
---
# Quiet hours and Update free periods {#quiet-hours-update-free-periods}

>[!NOTE]
>Currently, the Quiet hours and Update free periods features are available only through the beta program. Please contact either Adobe support or your account manager for access to the beta program.

The AEM as a Cloud Service [automatic maintenance updates](/help/implementing/deploying/aem-version-updates.md) ensure that your instances stay secure and up to date with the latest maintenance releases. That said, in some cases (like go-live events) you might need to "protect' those critical working hours from any potential disruptions. As such, AEM as a Cloud Service offers you the option to set a time frame where automatic updates do not occur for your ongoing programs. You can configure these time frames by using two scheduling options:

* **Quiet hours** - You can define a time interval (up to 8 hours) within day where updates will not occur.
* **Update free periods** - You can define a 7 day time period where updates will not occur. You can have up to three update free periods within a 12-month time frame.

The update free periods and quiet hours features are configured on a "per program" basis.

## Quiet hours {#quiet-hours}

The quiet hours feature allows you to define a time window during the day without any automatic updates. All maintenance updates will shift to occur outside of the configured time window. If, for example, an update is scheduled during your specified quiet hours, it will automatically start after the specified quiet hour interval ends. The configured time interval cannot exceed 8 hours so that updates can still occur daily. You can define these quiet hours **per program**, using your local timezone.

### How to configure the quiet hours interval {#configure-quiet-hours}

The quiet hours feature can be configured by using the AEM Cloud Manager interface as follows:

Go to **Activities>Automatic Updates>Update Options**.

![Configuration](assets/main-config.png)

1. Make sure the **Quiet Hours** option is toggled.
2. Click **Edit**.
3. Set the quiet hours interval in the configuration window.

![Quiet Hours Configuration](assets/quiet-hours.png)

Once set, your specified start and end hours will apply to every calendar day moving forward. You can disable or re-configure the quiet hours time value as needed.

## Update free periods {#update-hours}

By using the update free periods feature you can define a 7 day time frame where updates will not occur. Once configured, all maintenance updates will automatically shift to occur outside the defined time frame. You can have up to three update free periods within a 12-month interval. Additionally, update free periods can be designated up to one year in advance. Keep in mind when configuring this option that (at least) a one-week time interval between periods is mandatory in order to facilitate automatic updates.

The update free periods feature can be configured on a "per program" basis.

### How to configure the update free periods {#configure-update-free-periods}

The update free periods feature can be configured by using the AEM Cloud Manager interface as follows:

Go to **Activities>Automatic Updates>Update Options**.

![Configuration](assets/main-config.png)

1. Go to the Update free periods section.
2. Click **Add Update free period**.
3. Select a one week update free period from the calendar.

![Update Free Periods Configuration](assets/update-free-periods.png)

An **Active** icon will be displayed near the currently active update free period and a **Complete** icon near the completed update free periods.
