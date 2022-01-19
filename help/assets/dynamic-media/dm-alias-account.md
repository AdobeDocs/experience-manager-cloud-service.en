---
title: Configure a Dynamic Media Alias Account
description: Learn how to
contentOwner: Rick Brough
topic-tags: administering
content-type: reference
feature: Image Profiles
role: User,Admin
mini-toc-levels: 4
hide: yes
hidefromtoc: yes
exl-id: 886063d4-71dd-48c8-a342-884ad2c111ca
---
# About configuring a Dynamic Media Alias Account {#about-dm-alias-acct}

>[!NOTE]
>
>The feature to create a Dynamic Media alias account is in the Prerelease Channel for January 2022. The feature will be generally available in the February 2022 release.

Dynamic Media URLs and viewer embed code contain your company account name. This account name was created at the time of provisioning Dynamic Media. There may be scenarios where your business has undergone an acquisition or a rebranding. In such scenarios, it is not easy to manually update your company account name in all URLs and viewer embed code that comes out of the box. There is the possibility that you will impact your existing Dynamic Media repository or impact live content. To solve this issue, you can configure a Dynamic Media Company Alias account.

A Dynamic Media Company Alias account ensures that all out-of-the-box Dynamic Media URLs and viewer embed code in the user interface reflect any updates made to your business context, such as rebranding. An alias account also has a positive impact on your SEO (Search Engine Optimization) because the Dynamic Media URLs and viewer embed code reflects the new company account name.

When you configure a Dynamic Media alias account, be aware of the following:

* Any existing Dynamic Media URLs or viewer embed code on your *live* digital properties must be updated manually to reflect the alias name. However, any URLs or viewers embed code with your original Dynamic Media company name continue to work for existing or new assets.
* The Dynamic Media Company Alias capability is limited to Experience Manager Assets authoring and delivery. The Company Alias name does not work with Experience Manager Sites. WCM (Web Content Management) components are not updated for this change. Those components continue to work with the original Dynamic Media company name for fetching Dynamic Media assets.
* You can set up only one alias account from the **[!UICONTROL Edit Dynamic Media Configuration]** page. However, you can create as many company alias accounts by way of a support case, and manually reflect the necessary alias name in the Dynamic Media URLs or viewer embed code.
* The out-of-the-box [Cache Invalidation](/help/assets/dynamic-media/invalidate-cdn-cache-dynamic-media.md) capability of Dynamic Media invalidates the URLs with both Company and Company Alias accounts configured in Dynamic Media Configuration in Cloud Services.

See also [Create a Dynamic Media Configuration in Cloud Services](/help/assets/dynamic-media/config-dm.md#configuring-dynamic-media-cloud-services)

## Configure a Dynamic Media Company Alias Account {#configure-dm-alias-account}

You begin configuring a Dynamic Media Company Alias account by first submitting a Support case. This step is required.

1. [Use the Admin Console to create a support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).
1. Provide the following information in your support case:

    * The Dynamic Media Company Alias name you want to use.
    * Your region.
    * Whether any [rulesets](/help/assets/dynamic-media/using-rulesets-to-transform-urls.md) are being used previously to achieve serving of Dynamic Media content through an alternate Dynamic Media company account name.

1. After the Dynamic Media alias account is created by Support, in Experience Manager as a Cloud Service Author instance, select the Experience Manager as a Cloud Service logo to access the global navigation console.
1. On the left of the console, select the Tools icon, then go to **[!UICONTROL Cloud Services > Dynamic Media Configuration]**.
1. On the Dynamic Media Configuration Browser page, in the left pane, select **[!UICONTROL global]** (do not select the folder icon to the left of **[!UICONTROL global]**). Then select **[!UICONTROL Edit]**.

SCREEN SHOT HERE

1. On the **[!UICONTROL Edit Dynamic Media Configuration]** page, in the **[!UICONTROL Company Alias]** text field, type the Dynamic Media alias account name.
1. In the upper right of the page, select **[!UICONTROL Save]**.
The Dynamic Media Company Alias account is now saved and enabled; all URLs and viewer embed code for existing and new assets now reflect the Company Alias name.