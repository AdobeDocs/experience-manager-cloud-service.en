---
title: Release Notes for Cloud Manager 2025.5.0
description: Learn about the release of Cloud Manager 2025.5.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2025.5.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- https://wiki.corp.adobe.com/display/DMSArchitecture/Cloud+Manager+2025.03.0+Release -->

Learn about the release of Cloud Manager 2025.5.0 in AEM (Adobe Experience Manager) as a Cloud Service.

See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2025.5.0 in AEM as a Cloud Service is Thursday, May 8, 2025. 

The next planned release is Thursday, June 5, 2025.
 
## What's new {#what-is-new}

* **AI-powered build summaries now available for internal use**

    Internal users can now use AI-powered build summaries to simplify build log analysis. The feature provides actionable recommendations and helps identify the root causes of build failures.

    ![Build Summary dialog box](/help/implementing/cloud-manager/release-notes/assets/build-summary.png)


## Early adopter program {#early-adoption}

Participate in Cloud Manager's Early Adopter Program to get exclusive access to upcoming features before their general release.

The following early adopter opportunities are currently available:

### Add Edge Delivery Pipeline

**Pipelines** are now supported for sites built with Edge Delivery Services, expanding this capability beyond just Cloud Service environments. You can use **Pipelines** to manage settings such as traffic filtering rules and Web Application Firewall (WAF) configurations, where applicable. See [Supported Configurations](/help/operations/config-pipeline.md#configurations).

![Add Edge Delivery pipeline in Add Pipeline drop-down list](/help/implementing/cloud-manager/release-notes/assets/add-edge-delivery-pipeline.png)

If you are interested in testing this new feature and sharing your feedback, send an email to [grp-aemeds-config-pipeline-adopter@adobe.com](mailto:grp-aemeds-config-pipeline-adopter@adobe.com) from your email address associated with your Adobe ID.

### Bring Your Own Git - now with support for Azure DevOps {#gitlab-bitbucket-azure-vsts}

<!-- BOTH CS & AMS -->

Customers can now onboard their Azure DevOps Git repositories into Cloud Manager, with support for both modern Azure DevOps and legacy VSTS (Visual Studio Team Services) repositories.

* For Edge Delivery Services users, the onboarded repository can be used to sync and deploy site code.
* For AEM as a Cloud Service and Adobe Managed Services (AMS) users, the repository can be linked to both full-stack and frontend pipelines.

Support for additional pipeline types and pull request validation through code quality pipelines is coming soon.

See [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md).

![Add Repository dialog box](/help/implementing/cloud-manager/release-notes/assets/azure-repo.png)

If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:grp-cloudmanager_byog@adobe.com) from your email address associated with your Adobe ID. Be sure to include which Git platform you want to use and whether you are on a private/public or enterprise repository structure.

## Bug fixes

* Issue

* Issue

* Issue


<!-- ## Known issues {#known-issues} -->

