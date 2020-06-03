---
title: Adobe Experience Manager as a Cloud Service Release Notes for 2020.6.0
description: Experience Manager Release Notes for 2020.6.0
---

# Release Notes for AEM as a Cloud Service 2020.6.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.6.0.

## Release Date {#release-date}

The release date for [!DNL Experience Manager] as a Cloud Service 2020.6.0 is June ??, 2020.

## What's New in AEM Sites {#aem-sites}

Follow this section to learn about what is new and the updates for AEM Sites in AEM as a Cloud Service Release 2020.5.0.

* Detailed job information now available after processing bulk page moves and roll outs as asynchronous jobs.
* When copying/pasting a page tree, now offering to choose between pasting only the root page or also the sub-pages of the tree.
* AEM Experience Fragments exported to Adobe Target workspaces now appear as unique offer types and offer sources in Target.
* MSM - using *publish* trigger now successfully rolls out delete events for components in live copy source, that is, deleting components in a live copy that were deleted in live copy source.
* MSM - live copy components are now being renamed to *_msm_moved* after same component rollout from live copy source.

## What's New in Cloud Manager {#cloud-manager}

Follow this section to learn about what is new and the updates for Cloud Manager in AEM as a Cloud Service Release 2020.5.0.

### What's New {#what-is-new}

* Six additional code quality rules have been added to help customers identify potential issues when planning a migration to Cloud Service.
* A new metric *Cloud Service Compatibility* has been added to summarize the number of compatibility-related issues.
* Environments which failed to be created will now be automatically deleted approximately 24 hours after creation failed unless they have already been deleted.
* The performance of the Activity page and the Pipeline Executions List API has been improved.
* The code quality log now contains complete stack traces for exceptions.

### Bug Fixes  {#bug-fixes}

* A misleading card was displayed on the overview page while the production pipeline was running.
* The *DontImplementOrExtendProviderTypesPomCheck* code quality rule could sometimes produce a Null Pointer Exception.
* Some documentation links from the overview page did not work correctly.
* The Create Environment dialog did not render correctly in Safari.
* Certain cards on the overview page did not display entity names correctly.
* In some cases, the Build Image would fail to download customer packages successfully.

## What's New in [!DNL Adobe Experience Manager Assets] {#aem-assets}

<!-- 
Assets RNs are being authored and are a work in progress.
PM/EM review required before publishing. 
-->

**Guided User Experience for Enhanced Smart Tags, powered by Adobe Sensei**

Enhanced Smart Tags allow organizations to train smart tagging models to recognize images based on customer-specific business tags in addition to generic smart tags.

With this release, there is a new, guided user experience that helps set up smart tags training for sets of customer-specific tags and train them with assets, that should be recognized and tagged with them in the future. This is a more intuitive experience.
Train Enhanced Smart Tags for more a intuitive training for Smart Tags. See [how to smart tag](/help/assets/smart-tags.md) and [configure smart tagging]().

**Support for ingestion, preview and delivery of 3D content**

Organizations can now store and use 3D files within AEM Assets. User can upload, preview, and leverage a variety of core 3D files, including .obj, .stl, .gltf, and .glb files. With the addition of [!DNL Dynamic Media], 3D experiences can be configured and delivered via agnostic URLs or viewers. This includes a [!DNL Dynamic Media] 3D Experience Viewer, Sites 3D Viewer component, and the ability to deliver 3D files via [!DNL Dynamic Media] (AR/VR).

**Adobe Asset Link support for Adobe XD**

With the latest release, [!DNL Experience Manager Assets] provides support for a new [!DNL Adobe Asset Link] plug-in that is released with [!DNL Adobe XD] v29. The integration allows designers to access and use assets from [!DNL Experience Manager] in their designs, without the need to leave [!DNL Adobe XD] application.

**Accessibility enhancements**

[!DNL Adobe Experience Manager Assets] is now more accessible in compliance with Web Content Accessibility Guidelines (WCAG) v2.1 guidelines. The accessibility has improved for the following use cases or interfaces:

* User interface elements, controls, pages and dialogs are screen reader friendly.
* User interface elements, controls, and input form fields are accessible using keyboard.
* Change in color or contrast of some interface elements to make these more distinguishable by users with limited vision and without perception of color. For example, Assets now has appropriate contrast in the star rating icons in [!UICONTROL Properties] page and in the card view.

**Enhancements based on customer feedback**

The release provides the following additional enhancements based on the feedback from our customers and users:

* Accessibility improvements for the Assets user interface.
* Ability to reprocess assets with asset processing profiles, giving users full control of the process (run full asset processing, just apply specific processing profile, and decide if post-processing workflow should be run).
* Search queries return results faster now when the underlying cluster instance has been restarted behind the scenes (the initial search run could last longer in such a case before).

### Bug Fixes {#assets-bug-fixes}

In addition to the above new features, the current release provides the following enhancements and bug fixes based on customer feedback for [!DNL Assets].

* For MP3 music files, the play button displayed on thumbnail in the DAM preview does not work. (CQ-4294731)
* Search results page automatically scrolls up when the user is browsing the assets at the bottom of the search results. (GRANITE-26895)
* Scrolling a large number of assets search results crashes [!DNL Google Chrome] browser. (GRANITE-26432)
* The options, scope, and workflows progress indicators on [!UICONTROL Manage Publication] page are not read out by the screen-reader as progress indicators. Instead, these items appear to as tabs instead. (CQ-4273015)
* While navigating between elements of tree structure, nothing is read out to screen reader users due to inappropriate implementation of accessibility concerns in tree view. (CQ-4272964)
* In the link sharing dialog, when navigating in browse mode, the screen reader narrates the table information as soon as the dialog is loaded. (CQ-4294232)
* In the link sharing dialog, when navigating in browse mode, the screen reader is unable to navigate to all the listed auto-suggestions. (CQ-4294232)
* In the link sharing dialog, when navigating in browse mode, the screen reader does not narrate the displayed auto-suggestions for the [!UICONTROL Add Email Address/Search] combo box (CQ-4294232).
