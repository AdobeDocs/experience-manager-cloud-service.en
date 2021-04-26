---
title: Adobe Experience Manager as a Cloud Service Release Notes for 2020.4.0
description: Experience Manager Release Notes for 2020.4.0
exl-id: d98a3862-76fa-4b5b-b81a-333f5f532b67
---
# Release Notes for Adobe Experience Manager as a Cloud Service 2020.4.0 {#release-notes}

This page outlines the general release notes for [!DNL Experience Manager] as a Cloud Service 2020.4.0.

## Release Date {#release-date}

The release date for [!DNL Experience Manager] as a Cloud Service 2020.4.0 is April 9, 2020.

## What's New in Assets {#assets}

Know about new features, enhancements, and bug fixes for [!DNL Experience Manager Assets] and [!DNL Dynamic Media] in the current release.

* [Brand Portal](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/home.html) supports the asset distribution use cases for Experience Manager Assets. [!DNL Brand Portal] aids organizations to meet their marketing needs by securely distributing approved brand and product assets to external agencies, partners, internal teams, and resellers for download.
  * [!DNL Brand Portal] configuration is completed through [!DNL Adobe I/O] console. See [configure Brand Portal](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/publish/configure-aem-assets-with-brand-portal.html).
  * Asset sourcing in [!DNL Brand Portal] is not yet supported with [!DNL Experience Manager] as a Cloud Service.

* [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html) v2.0 works with [!DNL Experience Manager] as a Cloud Service. [!DNL Adobe Asset Link] streamlines collaboration between creatives and marketers in the content creation process by connecting [!DNL Experience Manager Assets] with [!DNL Creative Cloud] desktop apps [!DNL Adobe Photoshop], [!DNL Adobe Illustrator], and [!DNL Adobe InDesign] via in-app [!DNL Asset Link] panel.
  * [!DNL Experience Manager] is pre-configured for [!DNL Adobe Asset Link], which results in [easy configuration](https://helpx.adobe.com/enterprise/using/configure-aem-assets-for-asset-link.html) and faster roll-out to creative professionals.
  * [!DNL Asset Link] now supports an [Experience Manager environment switcher](https://helpx.adobe.com/enterprise/using/manage-assets-using-adobe-asset-link.html#UseAdobeAssetLink) that allows creative users to easily connect to a different [!DNL Experience Manager] environment. An example where this functionality is useful is, for agency designers who work with multiple clients using different [!DNL Experience Manager Assets] deployments.

* Users can configure [post-processing workflows](/help/assets/asset-microservices-configure-and-use.md#post-processing-workflows) to auto-start in the folder [!UICONTROL Properties] user interface for the specific folder hierarchies.
  * The folder [!UICONTROL Properties] user interface is simplified, with new [!UICONTROL Asset Processing] tab containing metadata profile, processing profile, and the new auto-start workflow configuration.

    ![Processing profiles can easily be applied to folders and all assets uploaded to folders are processing using these profiles](/help/assets/assets/asset-processing-folder-properties.png)

  * Asset reprocessing option allows to select a specific processing profile to reprocess user-selected assets in sub-folders.

    ![Reprocess selected assets using a specific processing profile](/help/assets/assets/fpo-existing-asset-reprocess.gif)

  * [!DNL Dynamic Media]: Added selective publish configuration so that assets are auto-published for secure preview only. Also, the assets can be explicitly published to Experience Manager without publishing to DMS7 for delivery in the public domain.

### Bug Fixes {#assets-bug-fixes}

* Fixes for asset processing issues.
* Fixes in [!DNL Dynamic Media] configuration and publishing assets to [!DNL Dynamic Media] delivery service.

>[!MORELIKETHIS]
>
>* [About Adobe Asset Link](https://www.adobe.com/creativecloud/business/enterprise/adobe-asset-link.html)
>* [Configure Brand Portal](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/publish/configure-aem-assets-with-brand-portal.html)
>* [Configure Experience Manager to work with Asset Link](https://helpx.adobe.com/enterprise/using/configure-aem-assets-for-asset-link.html)
>* [Create workflow in Experience Manager using assets microservices](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/assets/manage/asset-microservices-configure-and-use.html#post-processing-workflows)

## What's New in Cloud Manager {#whats-new-cloud-manager}

* Publisher URLs are now available from the Environment page in Cloud Manager UI.
* Changes to navigation to allow user to edit, switch or add a program from Cloud Manager overview page.
* Changes to allow user to Edit program from the program card on Cloud Manager landing page.
* New pipeline status **Pipeline Running** displayed against the environment it is associated with.
* Improvements to pipeline execution page comprehensibility. This includes display of Pipeline name (non-production pipeline only) and type, and a badge to indicate if the pipeline status is In Progress/Cancelled/Failed.
* Tool tips to improve user experience and comprehensibility around why Add Program/Environment button is disabled.
* Failed Environments can now be deleted through the UI and API.
* The process used to generate git passwords has been made more resilient to issues in the underlying service layer.

### Bug Fixes {#bug-fixes-cloud-manager}

* The links to the stage environment on the pipeline execution details page were not consistently navigating to the correct location.
* Individual steps within the environment creation process would timeout earlier than necessary causing the process to fail.
* The Maven configuration used in the build container was updated to avoid deadlocks when downloading artifact metadata.
* In some cases, the Build Image step would fail to download customer packages successfully.
* Certain infrequently occurring conditions would prevent environments from being deleted.
* Experience Cloud notifications were not consistently received.
