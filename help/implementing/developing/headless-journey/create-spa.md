---
title: How to Create Single Page Applications (SPAs) with AEM
description: In this part of the AEM Headless Developer Journey, you learn how you can create editable SPAs using AEM's SPA Editor framework as well as integrate external SPAs, enabling editing capabilities as required.
---

# How to Create Single Page Applications (SPAs) with AEM {#create-spa}

In this part of the [AEM Headless Developer Journey,](#overview.md) learn how you can create editable SPAs using AEM's SPA Editor framework as well as integrate external SPAs, enabling editing capabilities as required.

## Objective {#objective}

This document helps you understand how Single Page Applications are developed using the AEM SPA Editor framework. After reading this document you should:

* Understand the basic function of the SPA Editor
* Know the requirements for building a fully editable SPA for AEM
* Understand how external SPAs can be integrated into AEM
* Understand how server side rendering should or should not be implemented

## Requirements and Prerequisites {#requirements-prerequisites}

There are a number of requirements before you begin working with SPAs in AEM.

### Knowledge {#knowledge}

* Development experience creating SPAs with React or Angular frameworks
* Basic AEM skills creating [Content Fragments](/help/assets/content-fragments/content-fragments.md) and using the editor

### Tools {#tools}

* Sandbox access for testing deploying your project
* Local development instance for data modeling and testing
* Existing external SPA (optional, depending on what integration model is chosen)
* [AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html)

Be sure to review the document [Headful and Headless in AEM](/help/implementing/developing/headful-headless.md) in order to understand the various levels of SPA integration possible.

## What is a SPA? {#what-is-a-spa}

A single-page application (SPA) differs from a conventional page in that it is rendered client-side and is primarily Javascript-driven, relying on Ajax calls to load data and dynamically update the page. Most or all content is retrieved once in a single page load with additional resources loaded asynchronously as needed based on user interaction with the page.

This reduces the need for page refreshes and presents an experience to the user that is seamless, fast, and feels more like a native app experience.

The AEM SPA Editor allows front-end developers to create SPAs that can be integrated into an AEM site, allowing the content authors to edit the SPA content as easily as any other AEM content.

For a full description of SPAs, see the article [SPA Introduction and Walkthrough.](/help/implementing/developing/hybrid/introduction.md)

## Why a SPA? {#why-spa}

By being faster, fluid, and more like a native application, a SPA becomes a very attractive experience not only for the visitor of the webpage, but also for marketers and developers due to the nature of how SPAs work.

For a full description of SPAs, see the article [SPA Introduction and Walkthrough.](/help/implementing/developing/hybrid/introduction.md)

## How AEM Handles SPAs

Developing single page applications on AEM assumes that the front-end developer observes standard best practices when creating an SPA. If as a front end developer you follow these general best practices as well as few AEM-specific principles, your SPA will be functional with AEM and its content-authoring capabilities.

* **Portability** - As with any components, the SPA components should be built to be as portable as possible. The SPA should be built with portably and reusable components.
* **AEM Drives Site Structure** - The front end developer creates components and owns their internal structure, but relies on AEM to define the content structure of the site.
* **Dynamic Rendering** - All rendering should be dynamic.
* **Dynamic Routing** - The SPA is responsible for the routing and AEM listens to it and fetches based on it. Any routing should be dynamic as well.

See the document [Developing SPAs for AEM](/help/implementing/developing/hybrid/developing.md) for more guidelines on how to develop SPAs for AEM.

## The AEM SPA Editor {#aem-spa-editor}

Sites built using common SPA frameworks such as React and Angular load their content via dynamic JSON and do not provide the HTML structure that is necessary for the AEM Page Editor to be able to place edit controls.

To enable the editing of SPAs within AEM, a mapping between the JSON output of the SPA and the content model in the AEM repository is needed to save changes to the content.

SPA support in AEM introduces a thin JS layer that interacts with the SPA JS code when loaded in the Page Editor with which events can be sent and the location for the edit controls can be activated to allow in-context editing. This feature builds upon the Content Services API Endpoint concept since the content from the SPA needs to be loaded via Content Services.

See the document [SPA Editor Overview](/help/implementing/developing/hybrid/editor-overview.md) for details of how the SPA Editor works.

## Accommodating Existing SPAs {#existing-spas}

If you have an existing SPA, AEM supports embedding it into AEM so it is visible to your content authors in the AEM editor. This can be very useful to view the content they are creating via Content Fragments in context of the end application where it will be consumed.

Additionally, with only small changes, you can enable certain editing ability to the external SPA within the AEM editor.

The RemotePage component allows rendering of an external SPA in AEM.

To enable editing an external SPA in AEM, see the documents [Editing an External SPA within AEM](/help/implementing/developing/hybrid/editing-external-spa.md) and [The RemotePage Component.](/help/implementing/developing/hybrid/remote-page.md)

## What's Next {#what-is-next}

To gets started developing your own SPAs for AEM, be sure to review one of the following documents:

* [SPA WKND Tutorial](/help/implementing/developing/hybrid/wknd-tutorial.md)
* [Getting Started Using React](/help/implementing/developing/hybrid/getting-started-react.md)
* [Getting Started Using Angular](/help/implementing/developing/hybrid/getting-started-angular.md)

If you need to adapt an existing SPA to use it in AEM, review the following documents:

* [The RemotePage Component](/help/implementing/developing/hybrid/remote-page.md)
* [Editing an External SPA within AEM](/help/implementing/developing/hybrid/editing-external-spa.md)

Once you have done that, you can move on to the next step of your AEM headless journey and review [How to update your content via AEM assets APIs.](update-your-content.md)

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the headless development journey by reviewing the document [How to update your content via AEM assets APIs,](update-your-content.md) the following are some additional resources that do a deeper dive on some concepts mentioned in this document.

* [The RemotePage Component](/help/implementing/developing/hybrid/remote-page.md)
* [Editing an External SPA within AEM](/help/implementing/developing/hybrid/editing-external-spa.md)
* [Server Side Rendering](/help/implementing/developing/hybrid/ssr.md)
* [SPA Reference Documents](/help/implementing/developing/hybrid/reference-materials.md)
