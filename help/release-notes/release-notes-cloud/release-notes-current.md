---
title: Adobe Experience Manager as a Cloud Service Release Notes for 2020.6.0
description: Experience Manager Release Notes for 2020.6.0
---

# Release Notes for AEM as a Cloud Service 2020.6.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.6.0.

## Release Date {#release-date}

The release date for [!DNL Experience Manager] as a Cloud Service 2020.6.0 is June 04, 2020.

## What's New in Foundations in AEM as a Cloud Service {#foundations}

AEM project build times will improve by removing all references in the AEM project’s pom.xml to the remote repository `https://downloads.experiencecloud.adobe.com/content/maven/public`.

The AEM as a Cloud Service SDK API Jar, which was previously hosted in that location, is now located in Maven Central, which is Maven’s default artifact repository.

## What's New in Cloud Manager {#cloud-manager}

Follow this section to learn about what is new and the updates for Cloud Manager in AEM as a Cloud Service Release 2020.6.0.

### What's New {#what-is-new-cloud-manager}

* A user in the *Business Owner* role in Cloud Manager is now able to delete a Sandbox Program from the landing page (via quick action button on Program card) or from within the program.

* A Sandbox Program user in *Business Owner* or *Deployment Manager* role in Cloud Manager is now able to delete their Production and Stage environment set via the Cloud Manager UI. The delete option is now available from both the Environment card on the overview page as well as the Environments page. Selecting the delete option on either Production or Stage also deletes the other in the set.

* Coach marks on the landing page to inform and instruct the user about basic navigation.

* Coach marks on the *Overview* page to inform and instruct the user about basic navigation inside Cloud Manager to get them started.

* A **LEARN** page is now available in Cloud Manager, accessible via the top navigation. This page includes resources to help users learn about the most frequently used work-flows as relevant to their roles assigned in Cloud Manager.

* Sandbox Programs are now identified by means of a **Sandbox** badge that will be displayed on the program card on the landing page as well as next to the program name in the *Overview* page.

* A user in the *SysAdmin* role now has one-click access to the location in Admin Console from where user roles or permissions to Cloud Manager can be managed. A **Manage Roles** button will be available on the landing page next to the **Add Program** button.

* A user in the SysAdmin role now has one-click access to Author instance directly from CM.

* The Build log now includes the list of discovered artifacts, including skipped content packages.

* The Build step now validates that all of the generated content packages include all mandatory properties – name, group and version.

* The Build step now validates that the build produced at least one content package.

### Bug Fixes {#bug-fixes-cm}

* In certain situations, the icons in the **Create Program** dialog were misaligned.

* The AEM release identifier was not consistently displayed on the *Overview* page.

* When configuring the production pipeline, the **Scheduled Deployment** option was not visible for some customers.

### Known Issues {#known-issues-cm}

* Environments within a Sandbox program will be hibernated when no activity is detected for a certain duration. This status will not be observed in Cloud Manager. The status can however be observed via Developer Console. This will be addressed in an upcoming release.

* The link to the Developer Console directly from Cloud Manager will not display the option to de-hibernate/hibernate a Sandbox Program's environment. To address this, once at the Developer Console, add the pattern `#release-cm-p1234-e5678` to the end of the url, where *1234* is the Program ID and *5678* is the Environment ID. This will be addressed in an upcoming release.

## What's New in [!DNL Adobe Experience Manager Assets] {#aem-assets}

<!-- 
Assets RNs are being authored and are a work in progress.
PM/EM review required before publishing.
-->

**Guided User Experience for Enhanced Smart Tags, powered by Adobe Sensei**

Enhanced Smart Tags allow organizations to train smart tagging models to recognize images based on customer-specific business tags in addition to generic smart tags.

With this release, there is a new, guided user experience that helps set up smart tags training for sets of customer-specific tags and train them with assets, that should be recognized and tagged with them in the future. This is a more intuitive experience.
Train Enhanced Smart Tags for more a intuitive training for Smart Tags. See [how to smart tag](/help/assets/smart-tags.md) and [configure smart tagging](/help/assets/smart-tags-configuration.md).

**Support for ingestion, preview and delivery of 3D content**

Organizations can now store and use 3D files within AEM Assets. User can upload, preview, and leverage a variety of core 3D files, including .obj, .stl, .gltf, and .glb files. With the addition of [!DNL Dynamic Media], 3D experiences can be configured and delivered via agnostic URLs or viewers. This includes a [!DNL Dynamic Media] 3D Experience Viewer, Sites 3D Viewer component, and the ability to deliver 3D files via [!DNL Dynamic Media] (AR/VR).

<!-- TBD: Add link to the DM help article, if any. -->

<!-- Hiding this as the GA is at a later date. 
TBD: Add link to the AAL help article. 

**Adobe Asset Link support for Adobe XD**

With the latest release, [!DNL Experience Manager Assets] provides support for a new [!DNL Adobe Asset Link] plug-in that is released with [!DNL Adobe XD] v29. The integration allows designers to access and use assets from [!DNL Experience Manager] in their designs, without the need to leave [!DNL Adobe XD] application.

-->

**Accessibility enhancements**

[!DNL Adobe Experience Manager Assets] is now more accessible in compliance with Web Content Accessibility Guidelines (WCAG) v2.1 guidelines. The accessibility has improved for the following use cases or interfaces:

* User interface elements, controls, pages and dialogs are screen reader friendly.
* User interface elements, controls, and input form fields are accessible using keyboard.
* Change in color or contrast of some interface elements to make these more distinguishable by users with limited vision and without perception of color. For example, Assets now has appropriate contrast in the star rating icons in [!UICONTROL Properties] page and in the card view.

<!-- TBD: Add link to the a11y help article if created. Else add it post-GA. -->

**Other enhancements**

The release provides the following additional enhancements:

* Accessibility improvements for the Assets user interface.
* Ability to reprocess assets with asset processing profiles, giving users full control of the process (run full asset processing, just apply specific processing profile, and decide if post-processing workflow should be run).
* Search queries return results faster now when the underlying cluster instance has been restarted behind the scenes (the initial search run could last longer in such a case before).
* Sort by 'Name' when viewing assets in list view in Assets interface and in the search results.
* Sort on ‘Created’ (Date) when viewing assets in list view in Assets interface and in the search results.
* Support to convert EPS files to images.

### Bug Fixes {#assets-bug-fixes}

<!-- TBD: Add enhancements above and bug fixes below.
Seek DM bug fixes if any.
Add Nui update as shared on Slack: https://git.corp.adobe.com/nui/app/releases/tag/22
-->

In addition to the above new features, the current release provides the following enhancements and bug fixes based on customer feedback for [!DNL Assets].

* For MP3 music files, the play button displayed on thumbnail in the DAM preview does not work. (CQ-4294731)
* Hovering pointer on card view, makes the screen scroll as a result of (automatic) focus on the quick actions available in the card. (GRANITE-26895)
* Displaying too many images after scrolling a large number of search results leads to browser crash. (GRANITE-26432)
* The [!UICONTROL Options], [!UICONTROL Scope], and [!UICONTROL Workflows] progress indicators on [!UICONTROL Manage Publication] page are not read out by the screen-reader as progress indicators. Instead, screen reader users perceive these status indicators as a tab list. (CQ-4273015)
* When downloading an asset, if email option is selected and even if a valid email ID is provided, the download option is not available. (CQ-4296535)

* When adding tags in [!UICONTROL Properties] page of an asset, users navigate a tree structure of tags. The tree structure is not accessible as screen reader users do not hear anything when navigating it. (CQ-4272964)
* In the link sharing dialog, when navigating in browse mode, the screen reader,

  * narrates the table information as soon as the dialog is loaded.
  * is unable to navigate to all the listed auto-suggestions.
  * does not narrate the displayed auto-suggestions for the [!UICONTROL Add Email Address/Search] combo box. (CQ-4294232)

* Dragging options is not working using keyboard in NVDA browse mode in metadata schema editor. (CQ-4296326)
* On Assets user interface, the view settings are not accessible by keyboard. (CQ-4289038)
* Custom filters saved as smart collections are not applied properly to assets. (CQ-4294942)
* Multiple search and indexing enhancements and bug fixes to improve performance. (CQ-4286373)
* The luminosity ratio is less than 3:1 for the Yellow-colored rating icons. It is not useful to users with limited vision and without perception of color. The rating stars are displayed in the [!UICONTROL Rating] section of [!UICONTROL Advanced] tab in asset [!UICONTROL Properties] or in card view  (CQ-4295106)
* The list box drop-down of combo box (in various fields on different pages) now shows entries as a list of options that can be announced by screen readers. (CQ-4294017)
* The chevron up arrow in the [!UICONTROL Timeline] cannot be accessed using a keyboard, to apply a workflow to an asset. (CQ-4289268)
* Options (having [!UICONTROL x]) to remove each of the selected tags below the [!UICONTROL Tags] field in [!UICONTROL Basic] tab of [!UICONTROL Properties] are now accessible to screen readers. (CQ-4273033)
* Read-only form fields (for example disabled fields on [!UICONTROL Basic tab] of asset [!UICONTROL Properties]) are now focusable using keyboard. (CQ-4273031)
* The option to open filter sidebar can now be accessed using keyboard. (CQ-4273018)
* The purpose of various combo box elements (such as Path field and option to open Selection dialog in Basic tab of asset Properties) are now correctly announced by screen readers. (CQ-4273016)
* [!UICONTROL Metadata Schema Editor] page and its elements are not accessible using keyboard and are not screen reader friendly. (CQ-4272953)
* Video volume controls are not accessible using a keyboard. (CQ-4272696)
* Many actionable options on the Assets user interface do not indicate focus when using keyboard. (CQ-4272694)
* Screen reader users do not know that the rows in list view are selectable when using a keyboard. The information is only announced when mouse is hovered on the rows. (CQ-4271824)
* Some form fields, such as the username and password fields on the login page, rely only on placeholder values to give an accessible label. (CQ-4271716)
* Interactive user interface elements, such as links and options (on header and zoom options of assets page, folder navigation) can now be accessed using a keyboard. (CQ-4271412)
* Titles of all the browsed pages on [!DNL Adobe Experience Manager] Assets are now unique. (CQ-4271409)
