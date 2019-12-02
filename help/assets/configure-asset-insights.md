---
title: Configure Asset Insights
description: Learn how to configure Asset Insights in AEM Assets.
contentOwner: AG

---

# Configure Asset Insights{#configure-asset-insights}

Adobe Experience Manager (AEM) Assets fetches usage data around AEM assets used by third-party websites from Adobe Analytics. To enable Asset Insights to retrieve this data and generate insights, first configure the feature to integrate with Adobe Analytics.

>[!NOTE]
>
>Insights are only supported and provided for images.

1. In AEM, click **Tools** &gt; **Assets**.

   ![chlimage_1-72](assets/chlimage_1-72.png)

1. Click the **Insights Configuration** card.
1. In the wizard, select a data center and provide your credentials including the name of your organization, user name, and Shared Secret.

   ![Configure Adobe Analytics for Assets Insights in AEM](assets/insights_config2.png)

   Configure Adobe Analytics for Assets Insights in AEM

1. Click/tap **Authenticate**.
1. After AEM authenticates your credentials, from the **Report Suite** list, choose an Adobe Analytics report suite from where you want Asset Insights to fetch data. Click **Add**.
1. After AEM sets up your report suite, click/tap **Done.**

## Page Tracker {#page-tracker}

After you configure your Analytics account, the Page Tracker code is generated for you. To enable Assets Insights to track AEM assets used in third-party websites, include the page tracker code in the website code. Use the Page Tracker utility in AEM Assets to generate the page tracker code. For more information on how to include your Page Tracker code in third-party web pages, see [Using Page Tracker and Embed code in web pages](/help/assets/touch-ui-using-page-tracker.md).

1. In AEM, click **Tools** &gt; **Assets**.

   ![chlimage_1-73](assets/chlimage_1-73.png)

1. From the **Navigation** page, click the **Insights Page Tracker** card.
1. Click the **Download** icon to download the page tracker code.

