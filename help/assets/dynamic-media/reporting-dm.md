---
title: Reporting in Dynamic Media
description: Learn how to request an error report for Dynamic Media deliver URLs that fail.
contentOwner: Rick Brough
feature: Asset Management
role: User
hide: yes
hidefromtoc: yes
exl-id: 2488f813-df15-4dbb-8747-f827ee5925e1
---
# Request an error report for Dynamic Media delivery URLs that fail

You can request an error report that identifies Dynamic Media URLs that failed at delivery time. The report is an aggregation of data up to five days and is available in a CSV format. The error report includes the following information:

* Failed Dynamic Media delivery URL &ndash; A failing URL is a Dynamic Media-generated URL that is not able to produce any content at the time of delivery.
* Referrer URL &ndash; The referrer URL from which the failed delivery URL is called.
* Failure count &ndash; The number of times the delivery URL was loaded that resulted in a failure.

When you request the error report, the Adobe Dynamic Media team emails the report to you, in CSV format. It covers a five-day period from the day that your request was made.

You can request an error report once a month, for a given company.

**To request an error report for Dynamic Media delivery URLs that fail:**

1. [Send an email to reports-dynamic-media@adobe.com](mailto:reports-dynamic-media@adobe.com) with the company name that is associated with your Dynamic Media account.

    If you do not know the company name, see the [Dynamic Media Configuration](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/dynamicmedia/config-dm.html?lang=en#configuring-dynamic-media-cloud-services) page in **[!UICONTROL Adobe Experience Manager]** > **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** > **[!UICONTROL Dynamic Media Configuation]**. On the Dynamic Media Configuration Browser page, click **[!UICONTROL global]**, select the *[Dynamic_Media_folder_icon]* checkbox, then select **[!UICONTROL Edit]**. You must have Administrator rights in AEM to access the Dynamic Media Configuration page.

    ![Accessing the Dynamic Media Configuration page.](/help/assets/dynamic-media/assets/reporting-accessdmconfig.png)
