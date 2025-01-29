---
title: Digital Rights Management in [!DNL Assets]
description: Learn how to manage asset expiration states and information for licensed assets in [!DNL Experience Manager] as a [!DNL Cloud Service].
contentOwner: AG
feature: Asset Management,DRM
role: User, Admin
exl-id: fa5f94df-1c15-4593-afcb-1d24508da2bf
---
# Digital Rights Management for digital assets {#digital-rights-management-in-assets}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/drm.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

Digital assets are often associated with a license that specifies the terms and the duration of use. Using the [!DNL Experience Manager] platform, you can efficiently manage asset expiration information and licensing information.

## Asset expiration {#asset-expiration}

To enforce license requirements for assets, use asset expiration information. The expiry information ensures that the published asset is unpublished when it expires, which prevents license violation. A user without administrator permissions cannot edit, copy, move, publish, and download an expired asset.

You can view the expiration status of an asset at the following places:

* **Card view**: For an expired asset, a flag on the card indicates that it has expired.
* **List view**: For an expired asset, the **[!UICONTROL Status]** column displays the **[!UICONTROL Expired]** banner.
* **Timeline**: You can view the expiration status of an asset in the timeline. Select the asset and choose Timeline.
* **References rail**: You can also view the expiration status of assets in the **[!UICONTROL References]** rail. It manages asset expiration statuses and relationships between compound assets and referenced subassets, collections, and projects.

To view referencing web pages and compound assets for an asset, follow these steps: 

1. Navigate to the asset, select the asset, and click ![left rail content references icon](assets/do-not-localize/content-rail-icon.png). The left rail opens.
1. Select **[!UICONTROL References]** from the left rail.
1. For expired assets, the [!UICONTROL References] displays the expiry status as **[!UICONTROL Asset is Expired]**. If the asset has expired subassets, the [!UICONTROL References] rail displays the status **[!UICONTROL Asset has Expired Sub-Assets]**.

### Search expired assets {#search-expired-assets}

To search for an expired asset, including expired subassets, follow these steps:

1. In the [!DNL Assets] console, click **[!UICONTROL Search]** in the toolbar and press `Enter`.

1. Click the GlobalNav icon and select the **[!UICONTROL Expiry Status]** option.

1. Select **[!UICONTROL Expired]**. The search results display the expired assets.

When you choose the **[!UICONTROL Expired]** option, the [!DNL Assets] console only displays the expired assets and subassets that are referenced by compound assets. The compound assets that reference expired subassets are not displayed immediately after the subassets expire. Instead, they are displayed after [!DNL Experience Manager] detects that they reference expired subassets the next time the scheduler executes.

It is possible to modify the expiration date of a published asset to a date earlier than the current scheduler cycle. However, the schedule still detects such an asset as an expired asset when it executes the next time and [!DNL Experience Manager] reflects the status in its report. The expiration date of an asset is displayed differently for users in different time zones.

In addition, if an error prevents the scheduler from detecting expired assets in the current cycle, the scheduler re-examines these assets in the next cycle and detects their expired status.

To enable the [!DNL Assets] console to display the referencing compound assets along with the expired subassets, configure **[!UICONTROL Adobe CQ DAM Expiry Notification]** workflow in [!DNL Experience Manager]. The time-based scheduler schedules a job to check at a specific time whether an asset has expired subassets. After the job completes, assets that have expired subassets and referenced assets are displayed as expired in search results.

1. Access the [!DNL Cloud Manager] Git repository associated with your environment. 
1. Commit a file named `com.day.cq.dam.core.impl.ExpiryNotificationJobImpl.cfg.json` in the repository with the following contents.

   ```json
   {
      "send_email":"false", "asset_expired_limit":"100", "prior_notification_seconds":"86400", "cq.dam.expiry.notification.url.protocol":"http", "cq.dam.expiry.notification.scheduler.istimebased":"true", "cq.dam.expiry.notification.scheduler.period.rule":"10", "cq.dam.expiry.notification.scheduler.timebased.rule":"0 0 0 * * ?"
   }
   ```

1. Follow the instructions of [how to do OSGi configuration in [!DNL Experience Manager] as a [!DNL Cloud Service]](/help/implementing/deploying/configuring-osgi.md).

You can configure the scheduler using the following properties:

* A `true` value of the property `cq.dam.expiry.notification.scheduler.istimebased` initiates the scheduler. * The value of the property `cq.dam.expiry.notification.scheduler.timebased.rule` is the regular expression to define the time. The example above initiates the scheduler job at 00 hours.
* If `send_email` is set to `true`, the asset creator (the person who uploads a particular asset to [!DNL Assets]) receives an email when the asset expires.
* The maximum number of assets expired in one iteration of the scheduler is the value of the property `asset_expired_limit`.
* To run the job periodically, set the value of the property `cq.dam.expiry.notification.scheduler.istimebased` as `false` and set the value of the property `cq.dam.expiry.notification.scheduler.period.rule` with time in seconds.

<!-- TBD: Web Console not available in CS.

1. Open [!DNL Experience Manager] Configuration Manager.
1. Choose **[!UICONTROL Adobe CQ DAM Expiry Notification]**. By default, **[!UICONTROL Time-based Scheduler]** is selected, which 

1. For example, the example expression '0 0 0 &ast; &ast; ?' triggers the job at 0000 hrs.

1. Select **[!UICONTROL send email]** to receive emails when an asset expires.

1. In the **[!UICONTROL Prior notification in seconds]** field, specify the time in seconds before the asset expiry when you want to receive a notification. If you are an administrator or the asset creator, you receive a message before the expiration of the asset. After the asset expiry, you receive another notification that confirms the expiration. In addition, the expired asset is deactivated.

1. Select **[!UICONTROL Save]**.
-->

## Asset states {#asset-states}

The [!DNL Assets] console can display various states for assets. Depending on the current state of a particular asset, its card view displays a label that describes its state, for example, Expired, Published, Approved, Rejected, and so on.

1. In the [!DNL Assets] user interface, select an asset.

1. Select **[!UICONTROL Publish]** from the toolbar. If you do not see [!UICONTROL Publish] option in the toolbar, click **[!UICONTROL More]** on the toolbar and locate **[!UICONTROL Publish]** option.

1. Choose **[!UICONTROL Publish]** from the menu, and then close the confirmation dialog.

1. Exit the selection mode. The publication status for the asset appears at the bottom of the asset thumbnail in the card view. In the list view, the Published column displays the time when the asset was published.

1. To display its asset details page, in the [!DNL Assets] interface, select an asset and click **[!UICONTROL Properties]**.

1. In the [!UICONTROL Advanced] tab, set an expiration date for the asset from the **[!UICONTROL Expires]** field.

1. Click **[!UICONTROL Save]** and then click **[!UICONTROL Close]** to display the Asset console.

1. The publication status for the asset indicates an expired status at the bottom of the asset thumbnail in the card view. In the list view, the status of the asset is displayed as **[!UICONTROL Expired]**.

1. In the [!DNL Assets] console, select a folder and create a review task on the folder.

1. Review and approve/reject the assets in the review task and click **[!UICONTROL Complete]**.

1. Navigate to the folder for which you created the review task. The status for the assets that you approved/reject is displayed at the bottom in the card view. In the list view, the approval and expiry statuses are displayed in appropriate columns.

1. To search for assets based on their status, click **[!UICONTROL Search]** to display the search bar.

1. Select `Return` and click [!DNL Experience Manager].

1. In the search panel, click **[!UICONTROL Publish Status]** and select **[!UICONTROL Published]** to search for published assets in [!DNL Assets].

1. To search for approved or rejected assets, select **[!UICONTROL Approval Status]** and select the appropriate option.

1. To search for assets based on their expiration status, select **[!UICONTROL Expiry Status]** in the search panel and select the appropriate option.

1. You can also search for assets based on a combination of statuses under various search facets. For example, you can search for published assets that are approved in a review task and are not expired. To search such assets, select the appropriate options in the search facets.

## Digital Rights Management in [!DNL Assets] {#digital-rights-management-in-assets-1}

DRM functionality enforces the acceptance of the license agreement before you can download a licensed asset from [!DNL Assets].

If you select a protected asset and click **[!UICONTROL Download]**, you are redirected to a license page to accept the license agreement. If you do not accept the license agreement, the **[!UICONTROL Download]** option is not available.

If the selection contains multiple protected assets, select one asset at a time, accept the license agreement, and proceed to download the asset.

An asset is considered protected if either of these conditions are fulfilled:

* The asset metadata property `xmpRights:WebStatement` points to the path of the page that contains the license agreement for the asset.
* The value of the asset metadata property `adobe_dam:restrictions` is a raw HTML that specifies the license agreement.

>[!NOTE]
>
>The location `/etc/dam/drm/licences` was used to store licenses in the earlier releases of [!DNL Experience Manager]. The location is deprecated now. If you create or modify license pages, or port the pages from previous [!DNL Experience Manager] releases, Adobe recommends that you store such assets at `/apps/settings/dam/drm/licenses` or `/conf/*/settings/dam/drm/licenses` locations.

### Download DRM-protected assets {#downloading-drm-assets}

1. In the card view, select the assets you want to download and select **[!UICONTROL Download]**.
1. In the **[!UICONTROL Copyright Management]** page, select the asset you want to download from the list.
1. In the [!UICONTROL License] pane, choose **[!UICONTROL Agree]**. A check mark appears next to the asset. Select the **[!UICONTROL Download]** option.

   >[!NOTE]
   >
   >The **[!UICONTROL Download]** option is enabled only when you choose to agree to the license agreement for a protected asset. However, if your selection comprises both protected and unprotected assets, only the protected assets are listed in the pane and the **[!UICONTROL Download]** option is available to download the unprotected assets. To simultaneously accept license agreements for multiple protected assets, select the assets from the list and then choose **[!UICONTROL Agree]**.

1. To download the asset or its renditions, select **[!UICONTROL Download]** in the dialog.

**See also**

* [Translate Assets](translate-assets.md)
* [Assets HTTP API](mac-api-assets.md)
* [Assets supported file formats](file-format-support.md)
* [Search assets](search-assets.md)
* [Connected assets](use-assets-across-connected-assets-instances.md)
* [Asset reports](asset-reports.md)
* [Metadata schemas](metadata-schemas.md)
* [Download assets](download-assets-from-aem.md)
* [Manage metadata](manage-metadata.md)
* [Search facets](search-facets.md)
* [Manage collections](manage-collections.md)
* [Bulk metadata import](metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
