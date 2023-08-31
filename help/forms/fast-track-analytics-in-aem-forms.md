---
title: Using Fast Track Analytics in AEM Forms
description: Fast Track Analytics is a robust web analytics tool, It aids in tracking and analyzing user interaction with AEM Forms, offering insights into visitor interactions and engagement.
---

# Using Fast Track Analytics in AEM Forms

Fast Track Analytics is a robust web analytics tool, It aids in tracking and analyzing user interaction with AEM Forms, offering insights into visitor interactions and engagement. Fast Track Analytics also helps monitoring form performance involves assessing metrics like conversion rates, completion times, and drop-off points. This analysis helps optimize forms for better user experience and increased conversions.

Fast Track Analytics distinguishes user behavior based on login status. For logged-in users, it tracks specific actions tied to individual accounts. For anonymous users, it aggregates data to identify general trends and patterns, respecting privacy.

## Benefits of using FastTrack Analytics in AEM Forms

* **Importance of gathering form usage information**: Insights into end user behavior, FastTrack Analytics reveals user actions, drop-offs, and completion rates, enabling a deeper understanding of how individuals engage with forms, leading to better optimizations.
* **Insights into end user behavior**: FastTrack Analytics reveals user actions, drop-offs, and completion rates, enabling a deeper understanding of user engagement.
* **Enabling business users to gain insights**: FastTrack Analytics empowers even non-technical users to access and interpret form usage data, fostering data-driven decisions for enhancing forms and user satisfaction.
* **Optimizing data capture experience based on usage**: Organizations can identify pain points in data capture, leading to targeted improvements that enhance form usability and increase successful submissions.

## Prerequisites to connect Adobe Analytics

Setting up Fast Track Analytics in Adobe Experience Manager Forms requires an Adobe Analytics license, Data Collection (formerly Adobe Launch) to manage tracking scripts, and integration with the Experience Platform Launch API for streamlined data aggregation and insights generation.

When you have access to above applications, you can visit developer console and search your project with the program id and author id of your AEM instance, and ensure to have Experience Cloud Setup Automation, Adobe Analytics, and Experience Platform Launch API are included in the corresponding AEM developer console as given in the image below.

![Prerequiste Forms Analytics Integration](assets/analytics-aem.png)

## Configure Fast Track Analytics {configure-fast-track-analytics}:

Fast Track Analytics are scalable, comprehensive, and easy to integrate to use in AEM Adaptive Forms, based on your AEM Forms version, you configure and integrate:

* [FastTrack Analytics for Foundation Components](#fast-track-analytics-foundation)
* [FastTrack Analytics for Core Components](#fast-track-analytics-core)

### Integrate FastTrack Analytics for Foundation Component(#fast-track-analytics-foundation)

1. On your AEM instance, Go to **[Forms]** >> **[Forms and Document]** and select you Form. 
1. Create a configuration container for cloud services:
    1. Go to **[!UICONTROL Tools > General > Configuration Browser]**.
    1. Select a folder or create a folder, and enable the folder for **[!UICONTROL Cloud Configurations]**.
    1. Tap **[!UICONTROL Save & Close]** to save the configuration and exit the dialog.
1. Select Task Panel on the Left Rail and click **Setup Analytics** and **Activate Adobe Analytics**.
1. Provide the name you prefer for the report suite, Click **[!UICONTROL Next]** and **[!UICONTROL Save]**.
1. Once you save the project, the setup will run for sometime till installation and integration of Fast Track Analytics with your AEM Forms, you can also check the **integration status**.

    >[!NOTE] 
    >
    >If your installation does not setup in sometime, retry. If the issue still persists, you can connect to Analytics Support team.

* Navigate to your forms, and you see Adobe Analytics is integrated to your form as shown in the image.

![Integrated AEM Analytics](assets/analytics-aem-integrated.png)

### Integrate FastTrack Analytics for Core Component (#fast-track-analytics-core)

1. On your AEM instance, Go to **[Forms]** >> **[Forms and Document]** and select you Form. 
1. Select Task Panel on the Left and click **Setup Analytics** and **Activate Adobe Analytics**.
1. Provide the name you prefer for the report suite, Click **[!UICONTROL Next]** and **[!UICONTROL Save]**.
1. Once you save the project, the setup will run for sometime till installation and integration of Fast Track Analytics with your AEM Forms, you can also check the integration status.

    >[!NOTE] 
    >
    >If your installation does not setup in sometime, retry. If the issue still persists, you can connect to Analytics Support team.

1. Navigate to your forms, and you see Adobe Analytics is integrated to your form.