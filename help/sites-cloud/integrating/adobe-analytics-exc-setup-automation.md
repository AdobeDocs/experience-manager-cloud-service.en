---
title: Integrate Adobe Analytics with Experience Cloud Setup Automation
description: Experience Cloud Setup Automation provides a simple and automated way to integrate and instrument Experience Manager Sites with Experience Platform Launch and Adobe Analytics with a simple UI wizard interface. Learn how to use the automated setup with your own site.
feature: Administering
role: Admin
exl-id: 351ead2c-7b0d-4bd9-a020-47516948d467
---
# Integrate Adobe Analytics with Experience Cloud Setup Automation {#integrate-adobe-analytics-automation-setup}

>[!CAUTION]
>
> This functionality is currently in internal beta. Target release is in Q1 2022.

Experience Cloud Setup Automation provides a simple and automated way to integrate and instrument Experience Manager Sites with Experience Platform Launch and Adobe Analytics with a simple UI wizard interface.

It has never been simpler to integrate Adobe Analytics with AEM Sites. With Experience Cloud Setup Automation, setting up, integrating, and instrumenting your site to capture performance analytics to understand how well your customers are engaging and converting is all taken care of with just a few clicks.

This video explores how an AEM site is integrated with Experience Platform Launch and Analytics using Experience Cloud Setup Automation:

>[!VIDEO](https://video.tv.adobe.com/v/339605/?quality=12)

## Requirements

The automation setup is designed to work out of the box with an AEM Site built using [AEM Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html) with the [Adobe Client Data Layer](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/data-layer/overview.html) enabled. You can generate a new site that has these features enabled automatically using the [AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html) or by creating a site using a [Site template](/help/journey-sites/quick-site/create-site.md).

## How to Setup

1. Navigate to **Sites** and select the root of the site to integrate with Adobe Analytics.
1. Expand the side rail menu and tap **Setup Analytics**.

    This is a new option in the side rail that will open a panel that will provide controls and status for Experience Cloud Setup Automation. 
1. Tap the **Integrate Analytics** button.
1. In the resulting dialog, provide a name for the **Report Suite ID**.

    This string will be used to create a new [Report Suite ID](https://experienceleague.adobe.com/docs/analytics/admin/manage-report-suites/new-report-suite/t-create-a-report-suite.html?lang=en) in Adobe Analytics as the data store for the analytics data for the selected AEM site. The string provided will be appended with environment and tier identifiers to ensure uniqueness.

1. Refresh the page and panel and tap **Check Integration Status** to check the status of the automation.

    The automation setup occurs asynchronously. The **Check Integration Status** will show the current status of the integration.

    * **In progress** - indicates that the job is running.
    * **Integration Complete** - indicates that the job has completed integrating Analytics and Launch, setting up Launch extensions and Launch rules, and creating the new Report Suite in Adobe Analytics.
    * **Failure** - indicates that the automated job was unable to complete successfully. Check the log files for this job by clicking on the Logs link.

## Validate AEM setup

Once the automation is complete, validate that your site is now firing the Analytics events.

1. Open up a page in your site using the **Sites Editor**.
1. Use the **View as Published** option to load a published version of the page.
1. Use the browser's developer tools to inspect the network traffic and that **Launch** and `AppMeasurement.js` files are now being loaded.
1. Inspect the browser's console to see that page and component level events are fired and collected by the Adobe Client Data Layer.

## Validate Analytics setup

Next, navigate to Adobe Analytics to view the data flowing in from events on the AEM site.

1. Navigate to Adobe Analytics in the same IMS Org as your AEM site.
1. Create a new overview report for AEM Sites navigating to **Reports** > **Engagement** > **Adobe Experience Manager** > **Site Performance Overview**.
1. Tap **Open Report**.
1. Select the **Report Suite ID** that matches the Report Suite name used in the previous exercise.
1. View analytics data flow into the new template over time.

    >[!NOTE]
    >
    > With a new integration, it may take a few hours before the report is populated with data.
