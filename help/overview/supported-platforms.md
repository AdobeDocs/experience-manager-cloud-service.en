---
title: Supported Client Platforms
description: Learn which browsers are supported for authoring content with Adobe Experience Manager as a Cloud Service and accessing sites published with AEM.
topic-tags: platform
solution: Experience Manager, Experience Manager Sites
feature: Deploying
role: Admin
---

# Supported Client Platforms {#supported-platforms}

Adobe Experience Manager as a Cloud Service and accessing sites published with AEM.

## Support Levels {#support-levels}

Adobe defines the following levels of support for AEM's client platforms.

|Support Level|Description|
|---|---|
|A: Supported|Adobe provides full support and maintenance for this configuration. This configuration is covered by Adobe's quality assurance process.|
|R: Restricted Support|Support requires a formal request to Adobe to use the configuration in a project. Once confirmed by Adobe, Adobe provides full support within the restricted support program. For more information, contact Adobe Customer Care.|
|Z: Unsupported|The configuration is not supported. Adobe does not make statements about whether the configuration works, and does not support it.|

## Supported Browsers for Authoring Content {#authoring}

The AEM user interface is optimized for larger screens found in notebooks, desktop computers, and tablet devices (such as Apple iPad or Microsoft Surface). The phone form factor is not supported for any authoring use case.

The Adobe Experience Manager user interface works with the following client platforms depending on [authoring method.](/help/edge/authoring-methods.md)

* [Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md)
* [Page Editor](/help/sites-cloud/authoring/page-editor/introduction.md)
* [Document-based authoring](/help/edge/docs/authoring.md) using the [Sidekick](/help/edge/docs/sidekick.md)

All browsers are tested with the default set of plug-ins and add-ons.

|Browser|Universal Editor Support Level|Page Editor Support Level|Sidekick Support Level|
|---|---|---|---|
|Google Chrome (evergreen)|A: Supported|A: Supported|A: Supported|
|Microsoft Edge (evergreen)|A: Supported|A: Supported|Z: Unsupported|
|Mozilla Firefox (evergreen)|A: Supported|A: Supported|Z: Unsupported|
|Mozilla Firefox latest ESR [1]|A: Supported|A: Supported|Z: Unsupported|
|Safari on macOS (evergreen)|A: Supported|A: Supported|Z: Unsupported|
|Safari on iOS (evergreen) [2]|Z: Unsupported|A: Supported|Z: Unsupported|

1. Extended Support Release of Firefox ([learn more on mozilla.org](https://www.mozilla.org/en-US/firefox/enterprise/))
1. Support for Apple iPad only

>[!NOTE]
>
>**Support for browsers with rapid release cycles:**
>
>Firefox, Chrome, and Edge release updates regularly. Adobe is committed to maintaining the support level as listed above for upcoming versions of these browsers.

## Supported Browsers for Websites {#websites}

Browser support for websites rendered by AEM depends on the implementation of AEM page templates, blocks, design, and component output. Therefore your developers who implement your project are ultimately in control of your site's compatibility.

The AEM [project boilerplate,](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md#create-github-project) [Core Components,](/help/implementing/developing/components/overview.md#aem-core-components) and [WKND sample site](/help/implementing/developing/introduction/develop-wknd-tutorial.md) are all compatible with all modern browsers.
