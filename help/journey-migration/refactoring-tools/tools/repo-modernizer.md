---
title: Repository Modernizer
description: Learn how to restructure existing project packages and make them compatible with the project structure defined for Adobe Experience Manager as a Cloud Service.
feature: Migration
role: Admin
---

# Repository Modernizer {#repo-modernizer}

Repository Modernizer is a utility developed to restructure existing project packages by separating content and code into discrete packages to be compatible with the project structure defined for Adobe Experience Manager as a Cloud Service.

## Introduction {#introduction}

Adobe Experience Manager as a Cloud Service brings many new features and possibilities into your AEM Projects. However, there are some changes required to Adobe Experience Manager Maven projects to be compatible with AEM Cloud Service. At a high-level, AEM requires a separation of **content** and **code** into discrete subpackages to respect the split between mutable and immutable content. See [AEM Project Structure](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure.html) for more details about the new AEM project structure for Cloud Service.

The Repository Modernizer creates a compatible AEM Cloud Service project structure by creating the following deployment structure:

- `ui.apps` package deploys to `/apps` and contains all the code

- `ui.content` package deploys to runtime-writable areas (for example, `/content`, `/conf`, `/home`, or anything not `/apps`) and contains all the content and configuration.

- `all` package is a container package that contains the subpackages `ui.apps` and `ui.content`.

> [!NOTE]
>
> The Project structure is based on _Archetype 48_ for packages and their `pom.xml/filter.xml files`. See [Archetype 48](https://github.com/adobe/aem-project-archetype) for more details.

The Repository Modernizer now also supports the following project types:

- **MULTI_PROJECT**: Represents a multimodule project with no common parent POM, dispatcher, and all modules.
- **SINGLE_PROJECT**: Represents a single project.
- **NESTED_PROJECT**: Represents a multimodule project with a common parent POM, dispatcher, and all modules.
- **MONOLITHIC_PROJECT**: Represents a main project with one or more subprojects.

## Using the Repository Modernizer {#using-repo-modernizer}

> [!VIDEO](https://video.tv.adobe.com/v/333057/?quality=12&learn=on)

- The Repository Modernizer is now invoked automatically by the Refactoring Service under the Refactoring Job tab. Customers simply need to upload their project and trigger the refactoring job—no additional setup is required.

## Error Code Reference

If you encounter an error code while using the Repository Modernizer, refer to the table below for details and recommended actions.

| Error Code | Message                                                                                                                                                 | Description                                                                                                               | User Action Required? |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| RM-100     | Error while converting OSGi config file {0} to .cfg.json format. Please validate the existing config file before trying again.                          | This error occurs when there is an issue during the transformation of a OSGi config file to the .cfg.json format.         | Yes                   |
| RM-101     | Error while trying to copy content from: {0}                                                                                                            | This error occurs when there is a failure while attempting to copy content from the specified source.                     | No                    |
| RM-102     | Error while trying to move file {0} from {1} to {2}.                                                                                                    | This error occurs when there is a problem moving a file from one location to another.                                     | No                    |
| RM-103     | Given path could not be resolved to a valid file: {0}                                                                                                   | This error occurs when the file is not found at the given location.                                                       | No                    |
| RM-104     | Error occurred while iterating over the content of {0}.                                                                                                 | This error occurs during the traversal of files or directories, indicating an issue with accessing or processing content. | No                    |
| RM-105     | Error while trying to parse XML file: {0}. Please validate the XML file before trying again.                                                            | This error occurs when there is a failure in parsing the XML file.                                                        | Yes                   |
| RM-106     | Error while writing to XML file: {0}.                                                                                                                   | This error occurs when there is a problem writing to the XML file.                                                        | No                    |
| RM-107     | No content packages found in existing project: {0}. Please validate that the correct project has been uploaded.                                         | This error indicates that no content packages were found in the existing project.                                         | Yes                   |
| RM-108     | POM file not found at the expected path: {0}. The project or module's POM file is expected to be directly located within its directory as a child file. | This error occurs when the POM file is not found at the expected location.                                                | Yes                   |
| RM-109     | Error while trying to parse the pom.xml file: {0}. Please validate the pom file before trying again.                                                    | This error occurs when there is an issue parsing the pom.xml file.                                                        | Yes                   |
| RM-110     | Error while writing to pom.xml file: {0}.                                                                                                               | This error occurs when there is a problem writing to the pom file.                                                        | No                    |
| RM-111     | Error while writing to report file.                                                                                                                     | This error occurs when there is a failure during the process of writing to the report file.                               | No                    |
| RM-112     | Could not find {0} in repository structure pom file at ({1})                                                                                            | This error occurs when the expected configuration is not found in the AEM project archetype template.                     | No                    |
| RM-113     | Error while trying to copy the AEM Project Archetype templates to the destination.                                                                      | This error occurs when there is an issue copying the AEM Project Archetype templates to the destination.                  | No                    |
| RM-115     | Error while trying to connect to Azure Blob Storage.                                                                                                    | This error occurs when there is a problem connecting to Azure Blob Storage.                                               | No                    |
| RM-116     | Error while trying to upload file: {0} to Azure Blob Storage.                                                                                           | This error occurs when there is a problem uploading a file to Azure Blob Storage.                                         | No                    |
| RM-117     | Error while trying to download file: {0} from Azure Blob Storage.                                                                                       | This error occurs when there is a problem downloading a file from Azure Blob Storage.                                     | No                    |
| RM-118     | I/O error occurred while handling : {0}.                                                                                                                | This error occurs when there is an issue reading from or writing to a project file.                                       | No                    |
| RM-119     | I/O error while trying to archive the results for uploading to Azure.                                                                                   | This error occurs when there is an error while archiving the results generated by the process.                            | No                    |
| RM-120     | I/O error while trying to un-archive the provide project zip. Please check if the provided project zip is valid.                                        | This error occurs when there is an an error while un-archiving the given customer project.                                | Yes                   |
| RM-121     | Error while writing to configuration file.                                                                                                              | This error occurs when there is a failure during the process of writing to the configuration file.                        | No                    |
| RM-122     | Unsupported request type: {0}.                                                                                                                          | This error occurs when the request type is not supported by the system. Please check the request type and try again.      | No                    |

## Understanding Findings Report Priorities

When you download the findings report generated by the Repository Modernizer tool, each finding is assigned a **priority**. These priorities help you understand the urgency and impact of each issue:

| Priority | Description                                                                                     |
| -------- | ----------------------------------------------------------------------------------------------- |
| CRITICAL | Must be resolved to successfully build the project.                                             |
| HIGH     | Should be resolved to ensure that functionality is not broken in AEM.                           |
| NORMAL   | Should be resolved to ensure the overall sanity and completeness of modernization.              |
| LOW      | For manual verification; these findings are informational and may not require immediate action. |

>[!NOTE]
> 
>Addressing higher-priority findings first is recommended to ensure a smooth modernization and deployment process.
