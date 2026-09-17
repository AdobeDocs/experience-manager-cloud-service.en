---
title: Digital Rights Management in [!DNL Assets]
description: Learn how to manage asset expiration states and information for licensed assets in [!DNL Experience Manager] as a [!DNL Cloud Service].
contentOwner: AG
feature: Asset Management,DRM
role: User, Admin
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: fa5f94df-1c15-4593-afcb-1d24508da2bf
---
# Digital Rights Management for digital assets {#digital-rights-management-in-assets}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/drm.html?lang=en)                  |
| AEM as a [!DNL Cloud Service]     | This article         |

Digital assets carry a **license** that governs their permitted use, defining both the **license terms** and the **duration of use**. This licensing model is central to **Digital Rights Management (DRM)**, the practice of controlling how digital content may be accessed, distributed, and reused. Because licenses commonly restrict where, how, and for how long an asset may be published, tracking these conditions is essential to remaining compliant and avoiding the unauthorized use of expired or restricted content.

Using the [!DNL Experience Manager] platform, you manage **asset expiration information** and **licensing information** directly within the digital asset management workflow. This centralized control delivers several practical benefits:

- **Track license terms and duration** for each asset, so that usage rights are always visible alongside the content itself.
- **Manage asset expiration** to ensure that assets are no longer published or distributed once their licensed usage period ends.
- **Enforce compliance** with licensing agreements, reducing the risk of using assets beyond their authorized scope.

By keeping licensing and expiration details attached to the assets they govern, [!DNL Experience Manager] helps teams honor contractual obligations and prevent the accidental use of content whose rights have lapsed.

## Asset expiration {#asset-expiration}

Asset expiration enforces license requirements by automatically controlling when a published asset stays available. To enforce license requirements for assets, use asset expiration information. The expiry information ensures that the published asset is automatically unpublished when it expires. As a result, the asset can no longer be distributed after its license period ends, which prevents **license violation**. Once an asset expires, a user without administrator permissions cannot edit, copy, move, publish, or download the expired asset.

### Where to view asset expiration status

You can view the expiration status of an asset in the following places:

* **Card view**: For an expired asset, a flag on the card indicates that it has expired.
* **List view**: For an expired asset, the **[!UICONTROL Status]** column displays the **[!UICONTROL Expired]** banner.
* **Timeline**: You can view the expiration status of an asset in the timeline. Select the asset and choose Timeline.
* **References rail**: You can also view the expiration status of assets in the **[!UICONTROL References]** rail. The **[!UICONTROL References]** rail manages asset expiration statuses and relationships between compound assets and referenced subassets, collections, and projects.

To view referencing web pages and compound assets for an asset, follow these steps: 

1. Navigate to the asset, select the asset, and click ![left rail content references icon](assets/do-not-localize/content-rail-icon.png). The left rail opens.
1. Select **[!UICONTROL References]** from the left rail.
1. For expired assets, the [!UICONTROL References] displays the expiry status as **[!UICONTROL Asset is Expired]**. If the asset has expired subassets, the [!UICONTROL References] rail displays the status **[!UICONTROL Asset has Expired Sub-Assets]**.

### Search expired assets {#search-expired-assets}

To search for an expired asset, including expired subassets, follow these steps:

1. In the [!DNL Assets] console, click **[!UICONTROL Search]** in the toolbar and press `Enter`.

1. Click the GlobalNav icon and select the **[!UICONTROL Expiry Status]** option.

1. Select **[!UICONTROL Expired]**. The search results display the expired assets.

When you choose the **[!UICONTROL Expired]** option, the [!DNL Assets] console displays only the expired assets and subassets that are referenced by compound assets. Compound assets that reference expired subassets are not displayed immediately after those subassets expire. Instead, these compound assets appear as expired only after [!DNL Experience Manager] detects the referenced expired subassets. This detection occurs the next time the scheduler executes.

You can modify the expiration date of a published asset to a date earlier than the current scheduler cycle. The scheduler still detects such an asset as expired when it executes the next time, and [!DNL Experience Manager] reflects the status in its report. The expiration date of an asset is displayed differently for users in different time zones.

In addition, if an error prevents the scheduler from detecting expired assets during the current cycle, the scheduler re-examines those assets in the next cycle and, as a result, detects their expired status.

To enable the [!DNL Assets] console to display the referencing compound assets along with the expired subassets, configure the **[!UICONTROL Adobe CQ DAM Expiry Notification]** workflow in [!DNL Experience Manager]. The time-based scheduler schedules a job to check, at a specific time, whether an asset has expired subassets. After the job completes, assets that have expired subassets and their referenced assets are displayed as expired in search results.

#### Configure the expiry notification scheduler

1. Access the [!DNL Cloud Manager] Git repository associated with your environment.
1. Commit a file named `com.day.cq.dam.core.impl.ExpiryNotificationJobImpl.cfg.json` in the repository with the following contents.

   ```json
   {
      "send_email":"false", "asset_expired_limit":"100", "prior_notification_seconds":"86400", "cq.dam.expiry.notification.url.protocol":"http", "cq.dam.expiry.notification.scheduler.istimebased":"true", "cq.dam.expiry.notification.scheduler.period.rule":"10", "cq.dam.expiry.notification.scheduler.timebased.rule":"0 0 0 * * ?"
   }
   ```

1. Follow the instructions of [how to do OSGi (Open Service Gateway initiative) configuration in [!DNL Experience Manager] as a [!DNL Cloud Service]](/help/implementing/deploying/configuring-osgi.md).

Configure the scheduler using the following properties:

* A `true` value of the property **`cq.dam.expiry.notification.scheduler.istimebased`** initiates the scheduler.
* The value of the property **`cq.dam.expiry.notification.scheduler.timebased.rule`** is the regular expression that defines the time. The example above initiates the scheduler job at 00 hours, ensuring the expiry check runs at midnight.
* If **`send_email`** is set to `true`, the asset creator (the person who uploads a particular asset to [!DNL Assets]) receives an email when the asset expires.
* The maximum number of assets expired in one iteration of the scheduler is the value of the property **`asset_expired_limit`**.
* To run the job periodically, set the value of the property **`cq.dam.expiry.notification.scheduler.istimebased`** to `false` and set the value of the property **`cq.dam.expiry.notification.scheduler.period.rule`** with the time in seconds.

<!--
 TBD: Web Console not available in CS.

1. Open [!DNL Experience Manager] Configuration Manager.
1. Choose **[!UICONTROL Adobe CQ DAM Expiry Notification]**. By default, **[!UICONTROL Time-based Scheduler]** is selected, which 

1. For example, the example expression '0 0 0 &ast; &ast; ?' triggers the job at 0000 hrs.

1. Select **[!UICONTROL send email]** to receive emails when an asset expires.

1. In the **[!UICONTROL Prior notification in seconds]** field, specify the time in seconds before the asset expiry when you want to receive a notification. If you are an administrator or the asset creator, you receive a message before the expiration of the asset. After the asset expiry, you receive another notification that confirms the expiration. In addition, the expired asset is deactivated.

1. Select **[!UICONTROL Save]**.
-->

## Asset states {#asset-states}

The [!DNL Assets] console displays various states for assets to indicate where each asset is in its lifecycle. Depending on the current state of a particular asset, its card view shows a label that describes that state — for example, **Expired**, **Published**, **Approved**, or **Rejected**.

These asset states represent distinct stages:

- **Published** — the asset has been made live and is available for delivery.
- **Approved** — the asset was accepted during a review task.
- **Rejected** — the asset was declined during a review task.
- **Expired** — the asset has passed its configured expiration date and is no longer valid for use.

### Publish an asset

1. In the [!DNL Assets] user interface, select an asset.
1. Select **[!UICONTROL Publish]** from the toolbar. If you do not see the [!UICONTROL Publish] option in the toolbar, click **[!UICONTROL More]** on the toolbar and locate the **[!UICONTROL Publish]** option.
1. Choose **[!UICONTROL Publish]** from the menu, and then close the confirmation dialog.
1. Exit the selection mode. The publication status for the asset appears at the bottom of the asset thumbnail in the card view. This confirms the asset is live and available. In the list view, the Published column displays the time when the asset was published.

### Set an expiration date for an asset

1. To display its asset details page, in the [!DNL Assets] interface, select an asset and click **[!UICONTROL Properties]**.
1. In the [!UICONTROL Advanced] tab, set an expiration date for the asset from the **[!UICONTROL Expires]** field. This ensures the asset is automatically flagged once it is no longer valid for use.
1. Click **[!UICONTROL Save]** and then click **[!UICONTROL Close]** to display the Asset console.
1. The publication status for the asset indicates an expired status at the bottom of the asset thumbnail in the card view. In the list view, the status of the asset is displayed as **[!UICONTROL Expired]**.

### Review and approve or reject assets

1. In the [!DNL Assets] console, select a folder and create a review task on the folder.
1. Review and approve or reject the assets in the review task, and then click **[!UICONTROL Complete]**.
1. Navigate to the folder for which you created the review task. The status for the assets that you approved or rejected is displayed at the bottom in the card view. In the list view, the approval and expiry statuses are displayed in the appropriate columns.

### Search for assets by status

Because assets move through distinct states, you can locate them by searching on those states. This makes it easy to filter large asset libraries by lifecycle stage.

1. To search for assets based on their status, click **[!UICONTROL Search]** to display the search bar.
1. Select `Return` and click [!DNL Experience Manager] (Adobe [!DNL Experience Manager]).
1. In the search panel, click **[!UICONTROL Publish Status]** and select **[!UICONTROL Published]** to search for published assets in [!DNL Assets].
1. To search for approved or rejected assets, select **[!UICONTROL Approval Status]** and select the appropriate option.
1. To search for assets based on their expiration status, select **[!UICONTROL Expiry Status]** in the search panel and select the appropriate option.
1. You can also search for assets based on a combination of statuses under various search facets. For example, you can search for published assets that are approved in a review task and are not expired. To search for such assets, select the appropriate options in the search facets.

## Digital Rights Management in [!DNL Assets] {#digital-rights-management-in-assets-1}

**Digital Rights Management (DRM)** functionality in Adobe [!DNL Experience Manager] [!DNL Assets] enforces mandatory acceptance of the license agreement before a licensed asset can be downloaded. This mechanism ensures that every download of a protected asset is bound to explicit acceptance of its licensing terms, protecting the rights of asset owners and maintaining compliance across the asset library.

If you select a protected asset and click **[!UICONTROL Download]**, [!DNL Assets] redirects you to a license page to accept the license agreement. Because acceptance is mandatory, the **[!UICONTROL Download]** option remains unavailable until you accept the license agreement.

If the selection contains multiple protected assets, select one asset at a time, accept the license agreement for each, and then proceed to download that asset.

An asset is considered **protected** when either of these conditions is fulfilled, because each condition tells [!DNL Experience Manager] where to locate the license terms that must be accepted:

* The asset metadata property **`xmpRights:WebStatement`** points to the path of the page that contains the license agreement for the asset.
* The value of the asset metadata property **`adobe_dam:restrictions`** is a raw HTML value that specifies the license agreement.

>[!NOTE]
>
>The location `/etc/dam/drm/licences` was used to store licenses in earlier releases of [!DNL Experience Manager]. This location is now deprecated. If you create or modify license pages, or port the pages from previous [!DNL Experience Manager] releases, Adobe recommends that you store such assets at the `/apps/settings/dam/drm/licenses` or `/conf/*/settings/dam/drm/licenses` locations.

### Download DRM-protected assets {#downloading-drm-assets}

Digital Rights Management (DRM)-protected assets require you to accept a license agreement before they can be downloaded. To download DRM-protected assets, follow these steps:

1. In the card view, select the assets you want to download and select **[!UICONTROL Download]**.
1. In the **[!UICONTROL Copyright Management]** page, select the asset you want to download from the list.
1. In the [!UICONTROL License] pane, choose **[!UICONTROL Agree]** to accept the license terms. Accepting the agreement is what unlocks the protected asset for download. A check mark appears next to the asset. Select the **[!UICONTROL Download]** option.

   >[!NOTE]
   >
   >The **[!UICONTROL Download]** option is enabled only when you agree to the license agreement for a protected asset, because the license acceptance is what authorizes the download. However, if your selection comprises both protected and unprotected assets, only the protected assets are listed in the pane, and the **[!UICONTROL Download]** option is available to download the unprotected assets. To simultaneously accept license agreements for multiple protected assets, select the assets from the list and then choose **[!UICONTROL Agree]**.

1. To download the asset or its renditions, select **[!UICONTROL Download]** in the dialog.

### Expiring asset notification and unpublication {#expiring-asset-notification-unpublication}

A background job named **`com.day.cq.dam.core.impl.ExpiryNotificationJobImpl`** removes expired assets from Publish and Dynamic Media Scene7. This job runs **every day at midnight by default**. You can configure the job's frequency or timing through the **`com.day.cq.dam.core.impl.ExpiryNotificationJobImpl`** OSGi (Open Services Gateway initiative) configuration.

This job performs the following tasks:

* **Unpublishes assets that have passed their expiration date**, which is stored in the `/jcr:content/metadata/prism:expirationDate` property beneath the Asset node in the JCR (Java Content Repository). This ensures expired content is no longer served to end users on published or delivery environments.

* **When email notification is enabled**, the job additionally generates notifications so uploaders are kept aware of impending and completed expirations:
   * Identifies soon-to-expire assets and notifies the user who uploaded them. The notification lead time is controlled by the **`prior_notification_seconds`** configuration property, which is set to **86400 seconds, or 24 hours by default**.
   * Notifies the uploading user of any assets that have expired since the previous execution of the job.

The email templates used for these notification emails are stored at `/libs/settings/dam/notification/email/default`. You can customise these templates by overlaying them beneath `/conf/global/settings/dam/notification/email/default` or `/apps/settings/dam/notification/email/default`.

### Asset on-time and off-time {#asset-on-time-off-time}

**Asset on-time and off-time** is a time-based access control that is separate and distinct from **Asset expiration**. It governs a delivery window during which an asset becomes accessible and after which it ceases to be delivered.

You enable the on-time and off-time behaviour by providing the **`com.day.cq.dam.core.impl.servlet.OnOffTimeAssetAccessFilter`** Open Services Gateway initiative (OSGi) configuration. Enforcement occurs at the point an asset is requested by path. This ensures the time window is evaluated on every delivery request rather than at a single scheduled event, so access reflects the current time and date whenever the asset is called.

When the configuration is present, the filter delivers the asset to the requester **only** when both of the following conditions are met:

* The current time and date is **after** the configured **on-time** (if an on-time is set).
* The current time and date is **before** the configured **off-time** (if an off-time is set).

Because delivery is gated on both boundaries, an asset requested before its on-time or after its off-time is not served, giving administrators precise control over when content becomes available and when it is withdrawn.


**See also**

* [Translate [!DNL Assets]](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in [!DNL Assets] view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish [!DNL Assets] to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
