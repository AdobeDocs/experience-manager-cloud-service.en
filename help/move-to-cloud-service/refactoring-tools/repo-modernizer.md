---
title: Repository Modernizer
description: Repository Modernizer
exl-id: b89156a8-3d7d-4d36-89a2-beeda35bbc01
---
# Repository Modernizer {#repo-modernizer}

Repository Modernizer is a utility developed to restructure existing project packages by separating content and code into discrete packages to be compatible with the project structure defined for Adobe Experience Manager as a Cloud Service.

## Introduction {#introduction}

Adobe Experience Manager as a Cloud Service brings many new features and possibilities into your AEM projects. However, there are some changes required to Adobe Experience Manager Maven projects to be compatible with AEM Cloud Service. At a high-level, AEM requires a separation of **content** and **code** into discrete sub-packages to respect the split between mutable and immutable content. Please refer to [AEM Project Structure](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/aem-project-content-package-structure.html) for more details about the new AEM project structure for Cloud Service. 

The Repository Modernizer creates a compatible AEM Cloud Service project structure by creating the following deployment structure:

* `ui.apps` package deploys to `/apps` and contains all the code

* `ui.content` package deployes to runtime-writable areas (e.g. `/content`, `/conf`, `/home`, or anything  not `/apps`) and contains all the content and configuration.

* `all` package is a container package that contains the sub-packages `ui.apps` and `ui.content`.

>[!NOTE]
>The Project structure is based on *Archetype 24* for packages and their `pom.xml/filter.xml files`. Refer to [Archetype 24](https://github.com/adobe/aem-project-archetype) for more details.

## Using the Repository Modernizer {#using-repo-modernizer}

* Via Adobe I/O CLI : It is recommended to use the Repository Modernizer via `aio-cli-plugin-aem-cloud-service-migration` (AEM as a Cloud Service code refactoring plugin for the Adobe I/O CLI).

  Refer to **[Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration#introduction)** to learn how to install and use the plugin.

* As a standalone utility : The Repository Modernizer can also be executed as a standalone utility.

  Refer to **[Git Resource: Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer)** to learn how to use this tool.

  >[!NOTE]
  >
  >The Repository Modernizer is developed using NodeJS. It is recommended to have NodeJS 10.0+ installed.
