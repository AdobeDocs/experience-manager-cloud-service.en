---
title: Universal Editor Developer Overview
description: If you are developer interested in how the Universal Editor works and how to use it in your project, this document give you an end-to-end introduction.
---

# Universal Editor Developer Overview {#developer-overview}

If you are developer interested in how the Universal Editor works and how to use it in your project, this document give you an end-to-end introduction.

## Purpose {#purpose}

This document serves as a developer's introduction to both how the Universal Editor functions and how to instrument your application to work with it.

It does this by taking a standard example that most AEM developer's a familiar with, the Core Components and the WKND site, and instruments a few example components to be editable using the Universal editor.

## Prerequisites {#prerequisites}

You will need the following available to you.

* [Local development instance of AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-cloud/software-distribution/home.html)
* [WKND demo site installed](https://github.com/adobe/aem-guides-wknd)
* [Access to the Universal Editor](/help/implementing/universal-editor/getting-started.md#onboarding)

Beyond general familiarity with web development, this document assumes basic familiarity with AEM development. If you are not experienced with AEM development, consider reviewing the WKND tutorial before continuing.

## First set SAMEORIGIN OSGi setting

## Then add script to header

http://localhost:4502/system/console/configMgr

lax cookie
uBlock origin