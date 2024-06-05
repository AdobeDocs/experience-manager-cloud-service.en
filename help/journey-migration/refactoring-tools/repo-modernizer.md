---
title: Repository Modernizer
description: Learn how to restructure existing project packages and make them compatible with the project structure defined for Adobe Experience Manager as a Cloud Service.
exl-id: cd9d212e-e720-4209-8b5a-659883cc1d95
feature: Migration
role: Admin
---
# Repository Modernizer {#repo-modernizer}

Repository Modernizer is a utility developed to restructure existing project packages by separating content and code into discrete packages to be compatible with the project structure defined for Adobe Experience Manager as a Cloud Service.

## Introduction {#introduction}

Adobe Experience Manager as a Cloud Service brings many new features and possibilities into your AEM Projects. However, there are some changes required to Adobe Experience Manager Maven projects to be compatible with AEM Cloud Service. At a high-level, AEM requires a separation of **content** and **code** into discrete subpackages to respect the split between mutable and immutable content. See [AEM Project Structure](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure.html) for more details about the new AEM project structure for Cloud Service. 

The Repository Modernizer creates a compatible AEM Cloud Service project structure by creating the following deployment structure:

* `ui.apps` package deploys to `/apps` and contains all the code

* `ui.content` package deploys to runtime-writable areas (for example, `/content`, `/conf`, `/home`, or anything  not `/apps`) and contains all the content and configuration.

* `all` package is a container package that contains the subpackages `ui.apps` and `ui.content`.

>[!NOTE]
>The Project structure is based on *Archetype 24* for packages and their `pom.xml/filter.xml files`. See [Archetype 24](https://github.com/adobe/aem-project-archetype) for more details.

## Using the Repository Modernizer {#using-repo-modernizer}

>[!VIDEO](https://video.tv.adobe.com/v/333057/?quality=12&learn=on)

* By way of Adobe I/O CLI : Adobe recommends using the Repository Modernizer via `aio-cli-plugin-aem-cloud-service-migration` (AEM as a Cloud Service code refactoring plugin for the Adobe I/O CLI).

  See **[Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration#introduction)** so you can learn how to install and use the plugin.

* As a standalone utility : The Repository Modernizer can also be executed as a standalone utility.

  See **[Git Resource: Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer)** so you can learn how to use this tool.

  >[!NOTE]
  >
  >The Repository Modernizer is developed using NodeJS. It is recommended to have NodeJS 10.0+ installed.
