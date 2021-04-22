---
title: Adobe Experience Manager as a Cloud Service Release Notes for 2020.6.0
description: Experience Manager Release Notes for 2020.6.0
exl-id: fd6ebe2b-6d98-498c-a45d-b9a9c34e6be7
---
# Release Notes for AEM as a Cloud Service 2020.6.0 {#release-notes}

This page outlines the general Release Notes for Experience Manager as a Cloud Service 2020.6.0.

## Release Date {#release-date}

The release date for [!DNL Experience Manager] as a Cloud Service 2020.6.0 is June 04, 2020.

## What's New in AEM Sites {#aem-sites}

Follow this section to learn about what is new and the updates for AEM Sites in AEM as a Cloud Service Release 2020.6.0.

### What's New {#whats-new-2020.6.0}

Release 2.9.0 of the [Core Components](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/introduction.html) is now available as part of AEM Sites including:

* Integration between [Adobe Client Data Layer](https://github.com/adobe/adobe-client-data-layer) and the Core Components
* Configurable HTML ID attributes for all components
* A new Progress Bar component
* Many bug fixes

### Bug Fixes {#sites-bug-fixes}

* Components inside layout container not visible when Layout container is copied and pasted again on a page.

* Fixed Issue with resizing of layout component.

* Added ability to manage routing Angular only pages and AEM/Angular pages.

### Accessibility {#accessibility}

* Narrating role and state are now possible for the Masonry items in the **Create Page** dialog while navigating in the browsing mode using the down arrow.

* Added a link in navigation to allow users to skip to the main content.

* Screen reader improvements.

## What's New in Foundations in AEM as a Cloud Service {#foundations}

AEM project build times will improve by removing all references in the AEM project’s pom.xml to the remote repository `https://downloads.experiencecloud.adobe.com/content/maven/public`.

The AEM as a Cloud Service SDK API Jar, which was previously hosted in that location, is now located in Maven Central, which is Maven’s default artifact repository.

## What's New in Cloud Manager {#cloud-manager}

Follow this section to learn about what is new and the updates for Cloud Manager in AEM as a Cloud Service Release 2020.6.0.

### What's New {#what-is-new-cloud-manager}

* A user in the *Business Owner* role in Cloud Manager is now able to delete a Sandbox Program from the landing page (via quick action button on Program card) or from within the program.

  Refer to [Deleting a Sandbox Program](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/onboarding/getting-access/cloud-service-programs/creating-a-program.html) for more details.

* A Sandbox Program user in *Business Owner* or *Deployment Manager* role in Cloud Manager is now able to delete their Production and Stage environment set via the Cloud Manager UI. The delete option is now available from both the Environment card on the **Programs Overview** page as well as the **Environments** page. Selecting the delete option on either Production or Stage also deletes the other in the set.

  Refer to [Deleting a Sandbox Program](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/onboarding/getting-access/cloud-service-programs/creating-a-program.html) for more details.

* Coach marks on the landing page to inform and instruct the user about basic navigation.

* Coach marks on the **Program Overview** page to inform and instruct the user about basic navigation inside Cloud Manager to get them started.

* A **LEARN** page is now available in Cloud Manager, accessible via the top navigation. This page includes resources to help users learn about the most frequently used work-flows as relevant to their roles assigned in Cloud Manager.

* Sandbox Programs are now identified by means of a **Sandbox** badge that will be displayed on the program card on the landing page as well as next to the program name in the **Program Overview** page.

* A user in the SysAdmin role now has one-click access to the location in Admin Console from where user roles or permissions to Cloud Manager can be managed. A **Manage Access** button is now available on the landing page next to the **Add Program** button.
  
  Refer to [SysAdmin Tasks](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/onboarding/getting-access/navigation.html#sysadmin-tasks) for more details.

* A user in the SysAdmin role now has one-click access to author instance directly from Cloud Manager. 

  Refer to [Managing Access to Author Instance](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/onboarding/getting-access/navigation.html#manage-access-aem) for more details.

* The Build log now includes the list of discovered artifacts, including skipped content packages.

* The Build step now validates that all of the generated content packages include all mandatory properties – name, group and version.

* The Build step now validates that the build produced at least one content package.

### Bug Fixes {#bug-fixes-cm}

* In certain situations, the icons in the **Create Program** dialog were misaligned.

* The AEM release identifier was not consistently displayed on the **Programs Overview** page.

* When configuring the production pipeline, the **Scheduled Deployment** option was not visible for some customers.

### Known Issues {#known-issues-cm}

* Environments within a Sandbox program will be hibernated when no activity is detected for a certain duration. This status will not be observed in Cloud Manager. The status can however be observed via Developer Console. This will be addressed in an upcoming release.

* The link to the Developer Console directly from Cloud Manager will not display the option to de-hibernate/hibernate a Sandbox Program's environment. To address this, once at the Developer Console, add the pattern `#release-cm-p1234-e5678` to the end of the url, where *1234* is the Program ID and *5678* is the Environment ID. This will be addressed in an upcoming release.

## What's New in [!DNL Adobe Experience Manager Assets] {#aem-assets}

**Guided User Experience for Enhanced Smart Tags, powered by Adobe Sensei**

Enhanced Smart Tags allow organizations to train smart tagging models to recognize images based on customer-specific business tags in addition to generic smart tags.

With this release, there is a new, guided user experience that helps set up smart tags training for sets of customer-specific tags and train them with assets, that should be recognized and tagged with them in the future. The experience is a more intuitive now.
Train Enhanced Smart Tags for more an intuitive training for Smart Tags. See [how to add smart tags to assets](/help/assets/smart-tags.md) and [configure smart tagging](/help/assets/smart-tags-configuration.md).

**Support for ingestion, preview, and delivery of 3D content**

Organizations can now store and use 3D files within AEM Assets. User can upload, preview, and use various core 3D files, including OBJ, STL, GLTF, and GLB files. With the addition of [!DNL Dynamic Media], you can configure and deliver 3D experiences using agnostic URLs or viewers. This includes a [!DNL Dynamic Media] 3D Experience Viewer, Sites 3D Viewer component, and the ability to deliver 3D files via [!DNL Dynamic Media] (AR/VR). See [Working with 3D assets in Dynamic Media](/help/assets/dynamic-media/assets-3d.md).

**Adobe Asset Link support for Adobe XD**

With the latest release, [!DNL Experience Manager Assets] supports a new [!DNL Adobe Asset Link] plug-in that is released with [!DNL Adobe XD] v29.3. The integration allows designers to access and use assets from [!DNL Experience Manager] in their designs, without the need to leave [!DNL Adobe XD] application. See [Adobe Asset Link for Adobe XD documentation](https://helpx.adobe.com/enterprise/using/adobe-asset-link-for-xd.html).

With this release, creative users and designers can now work with assets managed in [!DNL AEM Assets] using [!DNL Adobe Asset Link] in a range of Creative Cloud desktop apps, including [!DNL Adobe XD], [!DNL Photoshop], [!DNL Illustrator], and [!DNL InDesign].

**Accessibility enhancements**

[!DNL Adobe Experience Manager Assets] is now more accessible in compliance with Web Content Accessibility Guidelines (WCAG) v2.1 guidelines. The accessibility has improved for the following use cases or interfaces:

The user interface elements are screen reader friendly, are accessible using a keyboard, and have better contrast. The following is a detailed list of enhancements:

* The [!UICONTROL Options], [!UICONTROL Scope], and [!UICONTROL Workflows] progress bars on [!UICONTROL Manage Publication] page are not read out by the screen-reader as progress bar. Instead, screen reader users perceive these status indicators as a tab list. (CQ-4273015)

* When adding tags in [!UICONTROL Properties] page of an asset, users navigate a tree structure of tags. The tree structure is not accessible as screen reader users do not hear anything when navigating it. (CQ-4272964)

* In the link sharing dialog, when navigating in browse mode, the screen reader,

  * Narrates the table information immediately when the dialog is loaded.
  * Is unable to navigate to all the listed auto-suggestions.
  * Does not narrate the displayed auto-suggestions for the [!UICONTROL Add Email Address/Search] combo box. (CQ-4294232)

* The [!UICONTROL Metadata Schema Editor] page and its elements are now accessible using a keyboard and are screen reader friendly. (CQ-4272953) Users can drag the components using the keyboard in NVDA browse mode. (CQ-4296326)

* On Assets user interface, the view settings are not accessible by keyboard. (CQ-4289038)

* The luminosity ratio is less than 3:1 for the Yellow-colored rating icons. It is not useful to users with limited vision and without perception of color. The rating stars are displayed in the  tab in asset  or in card view  

* Color and contrast of some user interface elements are updated so that users with limited vision or users without perception of color can distinguish these user interface elements. For example, the color of star rating icons in the [!UICONTROL Rating] section of [!UICONTROL Advanced] tab in the [!UICONTROL Properties] of an asset and in card view is changed for appropriate contrast. (CQ-4295106)

* The screen readers can now read the entries of the list box pop-up menu of combo box (in various fields on different pages) as a list of options. (CQ-4294017)

* To apply a workflow to an asset, the chevron arrow in the [!UICONTROL Timeline] can be accessed using a keyboard. (CQ-4289268)

* Users can remove selected tags in the [!UICONTROL Tags] field in [!UICONTROL Basic] tab of an asset's [!UICONTROL Properties] page using `x` symbol. The screen readers now announce the purpose and the number of selected tags (CQ-4273033).

* The read-only form fields can be focused upon using a keyboard. For example, the disabled fields on [!UICONTROL Basic] tab on an asset's [!UICONTROL Properties] page. (CQ-4273031)

* Access the options to filter assets in the left sidebar using a keyboard now. (CQ-4273018)

* The screen reader announces the purpose of various combo box elements such as Path field and the option to open Selection dialog in [!UICONTROL Basic] tab of an asset's [!UICONTROL Properties] page. (CQ-4273016)

* The volume controls for videos are accessible using a keyboard. (CQ-4272696)

* Many actionable options on the Assets user interface do not indicate focus when using keyboard. (CQ-4272694)

* Screen reader users now get to know when the rows in list view are selectable using a keyboard. The information is announced when pointer is hovered on the rows. (CQ-4271824)

* Some form fields, such as the user name and password fields on the login page, rely on placeholder values to give an accessible label. (CQ-4271716)

* Interactive user interface elements, such as links and options such as on header and zoom options of assets page or folder navigation can now be accessed using a keyboard. (CQ-4271412)

* Titles of all the browsed pages on [!DNL Adobe Experience Manager] Assets are now unique. (CQ-4271409)

**Other enhancements**

The release provides the following other enhancements:

* Ability to reprocess assets with asset processing profiles, giving users full control of the process (run full asset processing, just apply specific processing profile, and decide if post-processing workflow should be run).
* Search queries return results faster now when the underlying cluster instance has been restarted behind the scenes (the initial search run could last longer in such a case before).
* Sort by 'Name' when viewing assets in list view in Assets interface and in the search results. See [search assets](/help/assets/search-assets.md#sort).
* Sort on ‘Created’ (Date) when viewing assets in list view in Assets interface and in the search results. See [search assets](/help/assets/search-assets.md#sort).
* Support to convert EPS files to images using asset microservices.

### Bug Fixes {#assets-bug-fixes}

In addition to the above new features, the current release provides the following bug fixes based on customer feedback for [!DNL Assets].

* For MP3 music files, the play button displayed on thumbnail in the DAM preview does not work. (CQ-4294731)
* Hovering pointer on card view, makes the screen scroll as a result of (automatic) focus on the quick actions available in the card. (GRANITE-26895)
* Displaying too many images after scrolling many search results leads to browser crash. (GRANITE-26432)
* When downloading an asset, if email option is selected and even if a valid email ID is provided, the download option is not available. (CQ-4296535)
* Custom filters saved as smart collections are not applied properly to assets. (CQ-4294942)
* Multiple search and indexing enhancements and bug fixes to improve performance. (CQ-4286373)
* The folder properties tab cannot be accessed in Assets and returns a 500 error. (CQ-4295701)
