---
title: Assets Insights
description: Track user ratings and usage statistics of images that are used in third-party websites, marketing campaigns, and Adobe's creative solutions.
contentOwner: AG
feature: Asset Insights,Asset Reports
role: Business Practitioner,Leader
exl-id: e268453b-e7c0-4aa4-bd29-2686edb5f99a
---
# Assets Insights {#asset-insights}

Assets Insights functionality lets you track user ratings and usage statistics of images that are used in third-party websites, marketing campaigns, and Adobe's creative solutions. It helps provide insights about performance and popularity of the images.

Assets Insights captures user activity details, such as the number of times an image is rated, clicked, and impressions (number of times an image is loaded on the website). It assigns scores to images based on these statistics. You can use the scores and performance statistics to select popular images for inclusion in catalogs, marketing campaigns, and so on. You can even formulate archival and license renewal policies based on these statistics.

For Assets Insights to capture usage statistics for images from a website, you must include the embed code for the image in the website code.

To let Assets Insights display usage statistics for assets, first configure the feature to fetch reporting data from [!DNL Adobe Analytics]. For details, see [Configure Assets Insights](#configure-asset-insights). To use this feature, buy [!DNL Adobe Analytics] license separately.

>[!NOTE]
>
>Insights are supported and provided only for images.

## View statistics for an image {#viewing-statistics-for-an-image}

You can view the Assets Insights scores from the metadata page.

1. From the Assets user interface, select the image and then click **[!UICONTROL Properties]** from the toolbar.
1. From the Properties page, click **[!UICONTROL Insights]**.
1. Review the usage details for the asset in the **[!UICONTROL Insights]** tab. The **[!UICONTROL Score]** section describes the total asset usage and performance sores of an asset .

   Usage score describes the numbers of times asset is used in various solutions.

   The **[!UICONTROL Impressions]** score is the number of times the asset is loaded on the web site. The number displayed under **[!UICONTROL Clicks]** is the number of times the asset is clicked.

1. Review the **[!UICONTROL Usage Statistics]** section to know which entities the asset was part of and which creative solutions recently used it. The higher the usage, the greater the chances that the asset is popular among users. Usage data is displayed under the following heads:

    * **[!UICONTROL Asset]**: The number of times the asset was part of a collection or compound asset.
    * **[!UICONTROL Web & Mobile]**: The number of times the asset was part of websites and apps.
    * **[!UICONTROL Social]**: The number of times the asset was used in other solutions such as a [!DNL Adobe Campaign].
    * **[!UICONTROL Email]**: The number of times the asset was used in email campaigns.

   ![usage_statistics](assets/usage_statistics.png)

   >[!NOTE]
   >
   >Because the Assets Insights feature typically fetches the Solutions data from [!DNL Adobe Analytics] in a periodic manner, the Solutions section may not display the most recent data. The time period for which the data is displayed depends the schedule of the fetch operation that Assets Insights runs to retrieve Analytics data.

1. To view performance statistics for the asset graphically over a period of time, select period in the **[!UICONTROL Performance Statistics]** section. Details, including clicks and impressions are displayed as trend lines of a graph.

   ![chlimage_1-3](assets/chlimage_1-3.jpeg)

   >[!NOTE]
   >
   >Unlike the data in the Solutions section, the Performance Statistics section displays the most recent data.

1. To obtain the embed code for the asset that you include in websites to gets performance data, click **[!UICONTROL Get Embed Code]** below the asset thumbnail. <!-- For more information on how to include your Embed code in third-party web pages, see [Using Page Tracker and Embed code in web pages](/help/assets/use-page-tracker.md). -->

   ![chlimage_1-98](assets/chlimage_1-98.png)

## View aggregate statistics for images {#viewing-aggregate-statistics-for-images}

You can view scores of all assets within a folder simultaneously using **[!UICONTROL Insights View]**.

1. In the Assets UI, navigate to the folder containing the assets for which you want to view insights.
1. Click the Layout option from the toolbar, and then choose **[!UICONTROL Insights View]**.
1. The page displays usage scores for the assets. Compare the ratings of the various assets and draw insights.

<!-- TBD: Commenting as Web Console is not available. Document the appropriate OSGi config method if available in CS.

## Schedule background job {#scheduling-background-job}

Assets Insights fetches usage data for assets from Adobe Analytics report suites in a periodic manner. By default, Assets Insights runs a background job every 24 hours at 2 AM to the fetch data. However, you can modify both the frequency and the time by configuring the **[!UICONTROL Adobe CQ DAM Asset Performance Report Sync Job]** service from the web console.

1. Click the [!DNL Experience Manager] logo, and go to **[!UICONTROL Tools]** > **[!UICONTROL Operations]** > **[!UICONTROL Web Console]**.
1. Open the **[!UICONTROL Adobe CQ DAM Asset Performance Report Sync Job]** service configuration.

   ![chlimage_1-99](assets/chlimage_1-99.png)

1. Specify the desired scheduler frequency and the start time for the job in the property scheduler expression. Save the changes.
-->

## Configure Assets Insights {#configure-asset-insights}

[!DNL Experience Manager Assets] fetches usage data around digital assets used by third-party websites from [!DNL Adobe Analytics]. To enable Assets Insights to retrieve this data and generate insights, first configure the feature to integrate with [!DNL Adobe Analytics].

>[!NOTE]
>
>Insights are only supported and provided for images.

1. In [!DNL Experience Manager], click **[!UICONTROL Tools]** > **[!UICONTROL Assets]**.

   ![chlimage_1-72](assets/chlimage_1-72.png)

1. Click the **[!UICONTROL Insights Configuration]** card.
1. In the wizard, select a data center and provide your credentials including the name of your organization, user name, and Shared Secret.

   ![Configure Adobe Analytics for Assets Insights in [!DNL Experience Manager]](assets/insights_config2.png)

   *Figure: Configure Adobe Analytics for Assets Insights in [!DNL Experience Manager]*

1. Click **[!UICONTROL Authenticate]**. After [!DNL Experience Manager] authenticates your credentials, from the **[!UICONTROL Report Suite]** list, choose an Adobe Analytics report suite from where you want Assets Insights to fetch data. Click **[!UICONTROL Add]**.
1. After [!DNL Experience Manager] sets up your report suite, click **[!UICONTROL Done]**.

### Page Tracker {#page-tracker}

After you configure your Adobe Analytics account, the Page Tracker code is generated for you. To enable Assets Insights to track the [!DNL Experience Manager] assets used in third-party websites, include the page tracker code in the website code. Use the Page Tracker utility in Assets to generate the page tracker code. <!--  For more information on how to include your Page Tracker code in third-party web pages, see [Using Page Tracker and Embed code in web pages](/help/assets/use-page-tracker.md). -->

1. In [!DNL Experience Manager], click **[!UICONTROL Tools]** > **[!UICONTROL Assets]**.

   ![chlimage_1-73](assets/chlimage_1-73.png)

1. From the **[!UICONTROL Navigation]** page, click the **[!UICONTROL Insights Page Tracker]** card.
1. Click **[!UICONTROL Download]** to download the page tracker code.

<!--

## Using demo package for Assets Insights {#using-demo-package-for-asset-insights}

Using the demo package, you can enable Adobe Assets Insights to capture data from and generate insights for a sample web page.

1. Configure Assets Insights using the instructions in [Configure Assets Insights](#configure-asset-insights).
1. Download the sample [!DNL Experience Manager Assets] package from below and install the package from CRXDE package manager.

   [Get File](assets/insightsdemo.zip)

1. Download the ZIP file containing the sample web page from below and extract on your local file system.

   [Get File](assets/demosite.zip)

1. Click the web page to open it in the web browser.

   >[!CAUTION]
   >
   >Web Page is configured to load asset from the localhost server . In case your server is running somewhere else change server address from localhost to server address in the HTML content of the web page.

   >[!NOTE]
   >
   >The external web page can be in [!DNL Experience Manager] itself.

-->
