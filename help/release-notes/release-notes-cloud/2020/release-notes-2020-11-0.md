---
title: Release Notes for 2020.11.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: [!DNL Adobe Experience Manager] as a Cloud Service Release Notes for 2020.11.0.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2020.11.0 is December 2, 2020.
The following release (2020.12.0) will be on December 17, 2020

## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sites}

### What is new in [!DNL Sites] {#what-is-new-sites}

* **[Launches Hierarchy Management](/help/sites-cloud/authoring/launches/managing-pages.md) & [Future Timewarp](/help/sites-cloud/authoring/launches/preview.md)**: New UI to add/remove pages within a launch, and browsing site with Timewarp shows future state from Launches.

* **[Extended Content Fragment Models & Editor](/help/assets/content-fragments/content-fragments-models.md)**: New options for input validation on various data types, improved Enumeration data type with new form visualizations, and the Content Fragment model name is displayed and searchable in Assets UI.

* **Sort the Live Copy pages available for rollout**: New option to sort the Live Copy pages available for rollout using the [!UICONTROL Name], [!UICONTROL Last modified date], and [!UICONTROL Last rollout date] properties. The [!UICONTROL Last rollout date] for a page is a new property introduced.

## [!DNL Adobe Experience Manager Assets] as a Cloud Service {#assets}

### What is new in [!DNL Assets] and [!DNL Dynamic Media] {#what-is-new-assets}

* **Bulk asset ingestion**: Provide customers with a scalable, cloud-native ingestion service that leverages [!DNL Experience Manager] as a Cloud Service architecture including asset microservices. Key use cases include ingestion at scale with monitoring, reporting, and scheduling, while allowing for initial transfer of assets to cloud data stores using common cloud upload tooling. See [asset bulk ingestor tool](/help/assets/add-assets.md#asset-bulk-ingestor).

  This tool is for system administrator, consultant, or implementation partner personas. This feature allows for large scale ingestion and is ideally used during initial ingestion or occasional large ingestion. For smaller ingestion jobs, use the [[!DNL Experience Manager] desktop app](https://experienceleague.adobe.com/docs/experience-manager-desktop-app/using/introduction.html?lang=en) or [upload using Assets user interface](/help/assets/add-assets.md#upload-assets).

  ![Configuration of bulk importer](/help/assets/assets/bulk-import-config-low-res.png)

* Users can now sort the digital assets in Card and Column views.

  ![sort assets](/help/assets/assets/asset-sort-options.png)

* The following enhancements are done for accessibility in [!DNL Experience Manager Assets] in this release. For more information, see [accessibility features in [!DNL Assets]](/help/assets/accessibility.md).

  * When navigating timeline using a keyboard, the Esc key can collapse the Show All option without losing the focus.
  * When navigating using keyboard tab key, after removing the last tag from the added tags, the tag field retains the focus.
  * [!DNL Experience Manager] components now contain appropriate information for name, role, and value to be used by screen readers.
  * After you delete the Type/Size combo box, Link combo box, Language combo box, or Text edit box, the keyboard focus returns to the next or the previous user interface elements or to a more relevant user interface element.
  * When hovering pointer over options, tips such as Select and Download appear. Users who use a screen magnifier may not see the file thumbnails because of these tips. Now, it is possible to preserve the focus, after removing the option using `Escape` key.
  * Upon selecting a grid cell from the grid present in the page, the focus shifts to the action bar that appears on the screen.
  * Visual users can differentiate between normal text and a link, as visual clues (underline and chevron icon) are displayed for links to all solutions in [!DNL Experience Manager] home page.

* **Batch Set Presets in Dynamic Media**: Now you can automate the creation and organization of multiple assets in an image set or spin set at the time you upload asset files to a folder either individually or using bulk ingestion.

  See [About Batch Set Presets](/help/assets/dynamic-media/batch-set-presets-dm.md).

* The following accessibility enhancements are now available in [!DNL Dynamic Media]:

  * Screen readers (JAWS, Narrator) narrate the name, role, and state for the menu items in the Embed size menu option.
  * Users can navigate the Email link dialog using the `Tab` key.
  * The workflow to create video encoding profiles is more user-friendly given the screen reader enhancement.
  * When navigating using `Tab` key, the focus moves to the appropriate user interface elements in the workflow to create an interactive video.
  * The Publish page, Edit Asset page, Edit Smart Crops page, and Image Set Editor page are improved to comply with web standards. Assistive technology (AT) users can now navigate these pages easily and take actions such as cropping images.
  * Viewers are improved to let users navigate using a keyboard.
  * The keyboard and screen reader users can use the crop functionality.
  * The keyboard users can better manage the hotspots.

  See [Accessibility in [!DNL Dynamic Media]](/help/assets/dynamic-media/accessibility-dm.md).

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Released CIF Venia Reference Site - 2020.11.05 that includes the lastest CIF Core Components version v1.5.0. Refer to [CIF Venia Reference Site](https://github.com/adobe/aem-cif-guides-venia/releases/tag/venia-2020.10.27) for more details.

* Released CIF Core Components v1.5.0. Refer to [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.5.0) for more details.

### Bug Fixes {#bug-fixes-commerce}

* GraphQL client config was not read correctly when the config is not specified in the Sling CA config directly, but in one of the parent configs. This has been fixed.

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for Cloud Manager in AEM as a Cloud Service 2020.11.0 is November 12, 2020.

### What is new in [!DNL Cloud Manager] {#what-is-new-cm}

* A new menu option **Local Login** is now be available to users from the environment menu options on the **Environments** card and **Environments** summary pages. 
   Refer to [Managing Environments](/help/implementing/cloud-manager/manage-environments.md#login-locally) for more details.

* The **Learn** tab in Cloud Manager has been refreshed with new images in the UI.

### Bug Fixes {#bug-fixes-cloud-manager}

* The loading of dependencies done prior to build execution required downloading a Maven plugin.
* The link from the Cloud Manager footer to select a language will now navigate to the correct location.
* Sometimes during the code scanning, the SonarQube process would not start. This will now be auto-detected and a restart attempted.
* All existing production pipelines will be automatically enabled with the Experience Audit step. 

## Adobe Experience Manager as a Cloud Service Foundation {#cloud-service-foundation}

### Workflows {#workflows}

* Support was added for searching workflow instances based on Workflow Title, Workflow Model, Status, Initiator, Payload Path and Start Date. See [Search Workflow Instances](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/sites/administering/workflows-administering.html).

### Publish-tier User Data Synchronization {#user-sync}

* User data, including profile attributes and group memberships, can be persisted on the publish tier. Learn more about this feature in [Registration, Login, and User Profile documentation](/help/sites-cloud/authoring/personalization/user-and-group-sync-for-publish-tier.md). 

### SDK Build Analyzers {#analyzers}

The AEM as a Cloud Service SDK Build Analyzer Maven Plugin detects problems in a maven project, including missing dependencies. It gives developers an opportunity to discover issues during local development, well before deploying to Cloud environments with Cloud Manager. For more information, see the documentation [here](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html?lang=en#developing) and [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-as-a-cloud-service-sdk.html?lang=en#building-for-the-sdk).

### Others {#others-foundation}

New [“httpd -t” syntax](/help/implementing/dispatcher/disp-overview.md#local-validation) check for apache and dispatcher configuration executed during Cloud Manager build, which can also be run using AEM as a Cloud Service SDK’s Dispatcher Tools.

## Content Transfer Tool {#content-transfer-tool}

Follow this section to learn about what is new and the updates for [Content Transfer Tool](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html) Release v1.1.12.

### What is New {#what-is-new-ctt}

* User experience for logs improved. Timestamps added to Extraction and Ingestion logs. Message added to indicate if logs are empty.

### Bug Fixes {#ctt-bug-fixes}

* Content Transfer Tool was skipping content files if the migration set contained paths that had the partially similar file names. This has been fixed.

## Best Practices Analyzer {#best-practices-analyzer}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer is November 13, 2020.

### What is new in [!DNL Best Practices Analyzer] {#what-is-new-bpa}

* Cloud Readiness Analyzer is now Best Practices Analyzer (BPA). BPA provides a best practices assessment of your current AEM implementation and helps assess the readiness to move from an existing AEM instance to AEM as a Cloud Service.

* A new detector was added to detect the use of `java.io.InputStream`, which can cause issues if used in AEM as a Cloud Service.

### Bug Fixes {#bpa-bug-fixes}

* Bug causing the positives related to the *textfield foundation* component was fixed.
