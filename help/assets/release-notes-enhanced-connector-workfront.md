---
title: Release Notes for [!DNL Workfront for Experience Manager enhanced connector]
description: Release Notes for [!DNL Workfront for Experience Manager enhanced connector]
exl-id: 12de589d-fe5d-4bd6-b96b-48ec8f1ebcb6
---
# Release Notes for [!DNL Workfront for Experience Manager enhanced connector] {#release-notes-enhanced-connector-workfront}

The following section outlines the general Release Notes for [!DNL Workfront for Experience Manager enhanced connector].

## Release Date {#release-date}

The release date for the latest version 1.9.0 of [!DNL Workfront for Experience Manager enhanced connector] is June 16, 2022.

## Release highlights {#release-highlights}

The latest version of the [!DNL Workfront for Experience Manager enhanced connector] includes the following bug fix:

* When you use `Upload Linked Folder` or `Send To` options available in Workfront to upload assets to Experience Manager as a Cloud Service, the assets get corrupted when you download them from Experience Manager.

>[!IMPORTANT]
>
>Adobe recommends you to [upgrade to the latest 1.9.0 version](../assets/update-workfront-enhanced-connector.md) of the [!DNL Workfront for Experience Manager enhanced connector].

## Known Issues {#known-issues}

* While configuring project linked folders with AEM 6.4, Experience Manager do not save the values for **[!UICONTROL sub-folders]** and **[!UICONTROL Create linked folder in projects with portfolio]** fields. The value for the **[!UICONTROL sub-folders]** field updates to **[!UICONTROL undefined]** and the value for the **[!UICONTROL Create linked folder in projects with portfolio]** field updates to **[!UICONTROL Default Portfolio]** automatically after saving the configuration.

* When you are using the classic Workfront experience, the **[!UICONTROL Send to]** option available in the **[!UICONTROL More]** dropdown list does not allow you to select the target destination within Experience Manager. The **[!UICONTROL Send to]** option works correctly using the **[!UICONTROL Document Actions]** dropdown list. The **[!UICONTROL Send to]** option works correctly for **[!UICONTROL More]** dropdown list as well as the **[!UICONTROL Document Actions]** dropdown list available in the new Workfront experience.

## Previous releases {#previous-releases}

### March 2022 release {#march-2022-release}

[!DNL Workfront for Experience Manager enhanced connector] now includes the following updates:

* You can now create linked folders between Adobe Workfront and AEM Assets as a Cloud Service even if there are multiple project linked folder configurations.

* Added support for event subscription pagination.

* Added support for AEM 6.4.x.

* Added support for proxy environments.

* Several bug fixes based on partner and customer feedback.

>[!MORELIKETHIS]
>
>* [Integrate [!DNL Workfront for Experience Manager enhanced connector] with Experience Manager 6.5](https://experienceleague.adobe.com/docs/experience-manager-65/assets/integrations/workfront-integrations.html?lang=en)
>* [Integrate [!DNL Workfront for Experience Manager enhanced connector] with Experience Manager 6.4](https://experienceleague.adobe.com/docs/experience-manager-64/assets/integrations/workfront-integrations.html?lang=en)
