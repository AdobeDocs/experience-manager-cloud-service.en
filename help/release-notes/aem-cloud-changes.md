---
title: Notable Changes to Adobe Experience Manager (AEM) as a Cloud Service
description: Notable Changes to Adobe Experience Manager (AEM) as a Cloud Service
exl-id: fe11d779-66cd-45aa-aa6b-c819b88d2405
---
# Notable Changes to Adobe Experience Manager (AEM) as a Cloud Service {#notable-changes-aem-cloud}

AEM Cloud Service brings many new features and possibilities for managing your AEM projects. However there are a number of differences between AEM Sites on premise or in Adobe Managed Service as compared to AEM Cloud Service. This document highlights the important differences.

[!CONTEXTUALHELP] id="aem_cloud_notable_changes" title="Notable Changes in AEM as a Cloud Service" abstract="In this tab, you can view content that will help you to understand the differences between AEM on premise, or in Adobe Managed Services, as compared to AEM as a Cloud Service." additional-url="https://video.tv.adobe.com/v/330543" text="Evolution of AEM as a Cloud Service"


>[!NOTE]
>This document highlights the notable changes to AEM as a whole. For further information and solution-specific changes see:
>
>* [An Introduction to Adobe Experience Manager as a Cloud Service](/help/overview/introduction.md)
>* [What is New and What is Different](/help/overview/what-is-new-and-different.md) between Adobe Experience Manager as a Cloud Service and previous versions
>* The [Architecture](/help/core-concepts/architecture.md) of Adobe Experience Manager as a Cloud Service
>* [Notable changes to AEM Sites as a Cloud Service](/help/sites-cloud/sites-cloud-changes.md)
>* [Notable changes to AEM Assets as a Cloud Service](/help/assets/assets-cloud-changes.md)

The main differences are found in the following areas:

* [/apps and /libs are immutable at runtime](#apps-libs-immutable)

* [OSGi bundles and settings must be repository-based](#osgi)

* [Changes to publish repository are not allowed](#changes-to-publish-repo)

* [Custom runmodes are not allowed](#custom-runmodes)

* [Removal of Replication Agents](#replication-agents)

* [Removal of Classic UI](#classic-ui)

* [Publish-Side Delivery](#publish-side-delivery)

* [Asset Handling and Delivery](#asset-handling)

## /apps and /libs are immutable at runtime {#apps-libs-immutable}

 Any content and sub-folders in `/apps` and `/libs` is read-only. Any feature or custom code that expects to make changes there will fail to do so. An error will be returned that such content is read-only and the write operation wasn't able to complete. This has an impact in a number of areas of AEM:

* No changes in `/libs` are allowed at all.
  * This is not new rule, however this was not enforced in previous on-premise versions of AEM.
* Overlays for areas in `/libs` that are allowed to be overlaid are are still permitted within `/apps`.
  * Such overlays must come from Git via the CI/CD pipeline.
* Static Template design information that is stored in `/apps` can't be edited via UI.
  * It is recommended that you leverage Editable Templates instead.
  * If Static Templates are still required, configuration information must come from Git via the CI/CD pipeline.
* MSM Blueprint and custom MSM roll-out configurations must be installed from Git via the CI/CD pipeline.
* I18n translation changes need to come from Git via the CI/CD pipeline.

## OSGi bundles and settings must be repository-based {#osgi}

The Web Console, used in previous versions of AEM to change OSGi settings, is not available in AEM Cloud Service. Therefore changes to OSGi must be introduced via the CI/CD pipeline.

* Changes to OSGi settings can only come via Git persistence as JCR-based OSGi settings.
* New or updated OSGi bundles must be introduced via Git as part of the CI/CD pipeline build process.

## Changes to publish repository are not allowed {#changes-to-publish-repo}

Aside from changes under the `/home` folder on the publish tier, direct changes to the publish repository are not allowed on AEM Cloud Service. In prior versions of on-premise AEM or AEM on AMS, code changes could be made directly to the publish repository. Some limitations can be mitigated in the following ways:

* For content and content based configuration: make the changes on the author instance and publish them.
* For code and configuration: make the changes in the GIT repository and run the CI/CD pipeline to roll them out.

## Custom runmodes are not allowed {#custom-runmodes}

The following runmodes are provided out-of-the-box for AEM Cloud Service:

* `author`
* `publish`
* `prod`
* `author.prod`
* `publish.prod`
* `stage`
* `author.stage`
* `publish.stage`
* `dev`
* `author.dev`
* `publish.dev`

Additional or custom run modes are not possible in AEM Cloud Service.

## Removal of Replication Agents {#replication-agents}

In AEM Cloud Service, content is published using [Sling Content Distribution](https://sling.apache.org/documentation/bundles/content-distribution.html). The replication agents used in previous versions of AEM are no longer used or provided, which might impact the following areas of existing AEM projects:

* Custom workflows that push content to replication agents of preview servers for example.
* Customization to replication agents to transform content
* Using Reverse Replication to bring content from publish back to author

## Removal of Classic UI {#classic-ui}

The Classic UI is no longer available in AEM Cloud Service.

## Publish-Side Delivery {#publish-side-delivery}

HTTP acceleration including CDN and traffic management for author and publish services are provided by default in AEM Cloud Service.

For project transitioning from AMS or an on-premises installation Adobe strongly recommends leveraging the built-in CDN, because features within AEM Cloud Service are optimized for the CDN provided.

## Asset Handling and Delivery {#asset-handling}

Asset upload, treatment, and download have been optimized in Assets as a Cloud Service to be more efficient enabling better scaling and faster uploads and downloads. However this may impact some existing custom code.

* The default workflow **DAM Asset Update** in previous versions of AEM is no longer available.
* Web site components that deliver a binary **without transformation** should use direct download.
  * The Sling GET servlet has been changed to do this by default.
* Web site components that deliver a binary **with transformation** (for example, resize via servlet) can continue to operate as they have.
* Assets that come in via Package Manager require manual re-processing using the **Reprocess Asset** action in the Assets interface.
