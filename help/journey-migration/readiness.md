---
title: Readiness Phase
description: Learn about the steps that you must take so you can make sure that your AEM installation is ready to be moved to the cloud.
exl-id: 3bc8c037-d82a-4455-bce6-3c80c359a4ae
feature: Migration
role: Admin
---
# Readiness Phase {#readiness-phase}

>[!CONTEXTUALHELP]
>id="aemcloud_cam_planning"
>title="Planning your Transition"
>abstract="Before beginning your transition journey to Cloud Service, familiarize yourself with AEM as a Cloud Service. Review the notable changes made to it and the features that were replaced or deprecated."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/best-practices-analyzer/overview-best-practices-analyzer.html" text="Best Practices Analyzer"

In this phase of the AEM as a Cloud Service Migration Journey, you familiarize yourself with AEM as a Cloud Service. You can review the notable changes introduced and understand what it takes to plan for a successful migration to the cloud.

## The Story So Far {#story-so-far}

The previous document, [Getting Started with Moving to AEM as a Cloud Service](/help/journey-migration/getting-started.md), outlines a list of phases you must undergo so you can migrate to AEM as a Cloud Service. It also outlines the benefits of doing the migration.

## Objective {#objective}

This document helps you understand what factors you must consider so you can make sure that your AEM installation is ready to be moved to the cloud:

* Learn about notable changes and deprecated features
* Understand how to plan for the migration to AEM as a Cloud Service

## Review the Notable Changes in the AEM as a Cloud Service Architecture {#notable-changes-in-aem-cloud-service-architecture}

AEM as a Cloud Service brings many new features and possibilities for managing your AEM Projects.

Along with these improvements, several differences have been introduced between on-premise installations of AEM and Adobe Managed Services, compared to AEM as a Cloud Service.

The list of items in the below table is the subset of the changes most relevant for a migration to AEM as a Cloud Service. You can consult the full list of [Notable Changes to Adobe Experience Manager as a Cloud Service](/help/release-notes/aem-cloud-changes.md).

<table>
<thead>
  <tr>
    <th>What's Changed?</th>
    <th>Reference</th>
    <th>Key Takeaways</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Separate Mutable and Immutable Filters into corresponding packages</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/aem-cloud-changes.html">AEM as a Cloud Service Notable Changes</a><br><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure.html#mutable-vs-immutable">AEM Project Structure for AEM as a Cloud Service</a></td>
    <td>A single package that can be deployed into AEM as a Cloud Service can have sub packages, primarily to contain mutable and immutable content separated into their own packages.</td>
  </tr>
  <tr>
    <td>Repo Init</td>
    <td><a href="https://sling.apache.org/documentation/bundles/repository-initialization.html#the-repoinit-repository-initialization-language">Apache Sling RepoInit Documentation</a></td>
    <td>Repoinit scripts are the best practice to create any initial node structures, users, groups, or service users. As these scripts can be targeted by run mode and manageable via code package deployment, they provide much flexibility to achieve repository initialization tasks.</td>
  </tr>
  <tr>
    <td>Custom Run modes are not allowed</td>
    <td></td>
    <td>Only run modes provided out of the box with AEM as a Cloud Service are supported.<br>When additional Development environments are added, all of them tie to the "dev" run mode.</td>
  </tr>
  <tr>
    <td>Cloud Manager Pipeline Execution is the only way to deploy</td>
    <td></td>
    <td>In AEM as a Cloud Service, access to /system/console is not permitted, hence all OSGi configurations must be part of code, and should be deployed as code.<br>The OSGi configurations are available in read-only mode for viewing through Developer Console through Cloud Manager</td>
  </tr>
  <tr>
    <td>Replication Agents are replaced by Sling Content Distribution</td>
    <td></td>
    <td>The concept of the replication agent is replaced by Sing Content Distribution. If there are customizations that use replication agents, they must be redesigned.<br>Reverse replication is not supported</td>
  </tr>
  <tr>
    <td>CRX/DE and Package Manager</td>
    <td></td>
    <td>CRX/DE is allowed only on the Development environment.<br>Package Manager is accessible on all author instances but the packages that are going to be deployed must contain only mutable content ( for example: /content or /conf)</td>
  </tr>
  <tr>
    <td>Built in CDN and Get your own CDN</td>
    <td></td>
    <td>AEM as a Cloud Service includes the CDN for all environments which is optimized for most use cases.<br>If you want to set up your own CDN, you must submit a request to Adobe Support for it to be approved.<br>If it is approved, the CDN points to Fastly and not to AEM instances in any environments.</td>
  </tr>
  <tr>
    <td>Long Running Jobs</td>
    <td></td>
    <td>Avoid long running Jobs such as Sling Schedulers or Cron jobs, as the AEM instances running in the containers can come and go at any point.<br>Rethink these functionalities so you can offload them to Adobe Developer.</td>
  </tr>
  <tr>
    <td>Switch to Asynchronous Operations</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/operations/asynchronous-jobs.html#configuring-asynchronous-msm-operations">Configuring Asynchronous Operations</a></td>
    <td>To improve the overall performance of your environments, certain operations are run in async mode. The async jobs are queued and run when system resources are available.</td>
  </tr>
  <tr>
    <td>Token-based authentication and integration strategies</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/generating-access-tokens-for-server-side-apis.html#the-server-to-server-flow">Generating Access Tokens for Server-side APIs</a><br><a href="https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/overview.html#authentication">Token-based Authentication Tutorial</a></td>
    <td>It is common that systems external to AEM are trying to perform HTTP operations within AEM.<br>The recommended approach is to implement the strategies outlined here rather than relying on creating local usernames with passwords in AEM.</td>
  </tr>
  <tr>
    <td>File IO / Disk Usage</td>
    <td></td>
    <td>There is no guarantee of how much disk space is allocated, and the instances in containers come and go. Therefore, it is not advisable to use File I/O operations to write or read from the disk attached to the AEM instance.</td>
  </tr>
  <tr>
    <td>DAM Update Asset Workflow</td>
    <td><a href="https://experienceleague.adobe.com/docs/asset-compute/using/introduction.html">Asset Compute Service</a></td>
    <td>The media processing steps that are part of DAM Update Asset workflow are now replaced by the Asset Compute Service</td>
  </tr>
  <tr>
    <td>Asset upload methods and supported workflow process steps in AEM as a Cloud Service</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/admin/developer-reference-material-apis.html#post-processing-workflows-steps">Upload API Comparisons and Supported WF Process Steps</a></td>
    <td>In AEM as a Cloud Service, either during upload or download of an asset the asset streams directly in or out of binary storage. <br>Not all workflow process steps are supported in AEMaaCS.</td>
  </tr>
  <tr>
    <td>Workflow Launchers</td>
    <td></td>
    <td>Remove any Workflow Launchers that are triggering either out-of-the-box or custom DAM Update Asset Workflow from your code. <br>All the assets uploaded into AEM as a Cloud Service are going to be processed by the Asset Processing Service. For custom steps, see <a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/manage/asset-microservices-configure-and-use.html#post-processing-workflows"> Post Processing Workflows</a> on how to setup and configure post-processing workflows.</td>
  </tr>
  <tr>
    <td>Custom Rendition Steps</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/manage/asset-microservices-configure-and-use.html">Processing Profiles</a></td>
    <td>Any custom rendition generation, image conversions, or video encodings must be offloaded to the Asset Processing Service by creating corresponding processing profiles.</td>
  </tr>
  <tr>
    <td>Content Search and Indexing</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/operations/indexing.html">Content Search and Indexing Changes</a></td>
    <td>There are considerable changes to the underlying processing of indexes and when it is kicking in.<br>Completely understand and refactor the Oak Indexes before managing them in the code that you deploy.</td>
  </tr>
  <tr>
    <td>Not all maintenance tasks are configurable</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/operations/maintenance.html">AEM as a Cloud Service Maintenance Tasks</a></td>
    <td>You can configure only certain maintenance tasks with AEM as a Cloud Service.</td>
  </tr>
  <tr>
    <td>Changes to Publish repository</td>
    <td></td>
    <td>Direct changes to the Publish repository are not allowed, except those changes under /home. It is always recommended that any changes made on author get distributed. All code and configuration changes must be deployed through the corresponding Cloud Manager pipeline.</td>
  </tr>
  <tr>
    <td>Dispatcher Configurations and Caching</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/content-delivery/disp-overview.html">Dispatcher in the Cloud</a><br><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/content-delivery/caching.html#other-content">Cache Management<br></td>
    <td>The Dispatcher configurations must follow a specific structure.<br>The configurations must be managed as part of code and deployed through the Cloud Manager pipeline.</td>
  </tr>
  <tr>
    <td>Back up and Restore</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/operations/backup.html">AEM as a Cloud Service Backup and Restore</a></td>
    <td></td>
  </tr>
  <tr>
    <td>Changes to Authentication</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/security/ims-support.html">IMS Support for AEM as a Cloud Service</td>
    <td>If you were previously using SAML 2.0 integration on both author and publish before moving to Cloud Service, the main change is that AEM as a Cloud Service Author only integrates with Adobe IMS. However, AEM as a Cloud Service Publish tier can still use SAML or other authentication integrations. AEM as a Cloud Service offers IMS authentication support only for Author, Admin, and Dev users. The IMS authentication does not offer support for external end users of customer sites like site visitors.</td>
  </tr>
</tbody>
</table>

## Deprecated Features {#deprecated-features}

Adobe constantly evaluates product capabilities, to over time reinvent or replace older features with more modern alternatives to improve overall customer value, always under careful consideration of backward compatibility.

Adobe recommends that you consult [Deprecated Features](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/deprecated-removed-features.html#deprecated-features) to familiarize yourself with the features and capabilities that are marked as deprecated in Experience Manager as a Cloud Service. See what the impact is for your AEM deployment.

## Plan for a Review of your AEM Installation {#review-planning}

After you have accustomed yourself with the changes introduced with AEM as a Cloud Service, it is time to start planning for a review of your existing installation. Doing so helps you gauge the level of changes required to move it to the cloud.

The following figure showcases key steps involved during the review phase:

![Key steps involved during the review phase](/help/journey-migration/assets/planning-phaseimg1.png)

Next, you explore what each of these steps means in detail.

### Assessing Cloud Service Readiness {#assess-cloud-readiness}

The first step is to assess your readiness to move from your existing AEM version to Cloud Service and determine areas that require refactoring to be compatible with AEM as a Cloud Service.

Undertake a comprehensive assessment of your current AEM source code against the notable changes and deprecated features to determine the level of effort expected in the transition journey.

The number of findings can directly influence the timelines and overall project success. Therefore, Adobe recommends that you uncover as much as possible so you can plan the delivery. Or, initiate the conversations so you can redesign any customizations required to be in line with AEM as a Cloud Service best practice.

**Best Practice Analyzer**

You can accelerate the assessment by running the Best Practices Analyzer against your current AEM version. Having a good understanding of how it works is key to speeding up your assessment planning.

You can read up on how it works by consulting the [Best Practices Analyzer](/help/journey-migration/best-practices-analyzer/overview-best-practices-analyzer.md) documentation.

**Create a Cloud Readiness Assessment Report**

The next step is creating a report based on all the knowledge gained so far. You create the report by generating Best Practices Analyzer reports from the Stage and Production instances, [then upload them into Cloud Acceleration Manager](/help/journey-migration/cloud-acceleration-manager/using-cam/cam-readiness-phase.md#readiness-phase-cam) for a digestible report of actionable items.

A typical report should contain these inputs:

* Documentation detailing the feature set of your particular AEM installation
* Details on your AEM custom configurations and code
* Production Dispatcher configurations
* Domain mappings (CDN configurations) (if there are any)

**Socialize the Report**

After the Best Practices Analyzer reports are complete, share them with the relevant teams so you can confirm your findings and plan for your next steps. Depending on preference, you can also distribute a printed version of the report by using [Print Preview](/help/journey-migration/cloud-acceleration-manager/using-cam/cam-readiness-phase.md#print-preview-cam).

### Reviewing Resource Planning {#review-resource-planning}

Once you have estimated the level of effort that is required to move to Cloud Service, you should identify resources, create a team, and map out roles and responsibilities for the transition process.

### Establishing KPIs {#establish-kpis}

If you have not established Key Performance Indicators (KPIs) previously, it is recommended to establish KPIs for your AEM implementation to help your team focus on what matters the most.

See [Developing KPIs](https://experienceleague.adobe.com/welcome/aem/part6.html) so you can learn how to choose the right KPIs for your business objectives.

## What's Next {#what-is-next}

Once you understand the scope of the changes required to move to AEM as a Cloud Service, it's time to [Make your code and content cloud ready](/help/journey-migration/implementation.md) before actually performing the migration.

## Additional Resources {#additional-resources}

* [Getting Started with Cloud Acceleration Manager](/help/journey-migration/cloud-acceleration-manager/using-cam/getting-started-cam.md) - A comprehensive guide on how to use Cloud Acceleration Manager to speed up your move to the cloud.
* [AEM as a Cloud Service: Introduction, Architecture, and Thinking Differently](https://experienceleague.adobe.com/?launch=ExperienceManager-D-1-2021.1.migration&recommended=ExperienceManager-D-1-2021.1.migration&lang=en#dashboard/learning)
* [AEM a Cloud Service Home](/help/overview/introduction.md) - For an overview of the Experience Manager as a Cloud Service documentation, start here.
* [AEM as a Cloud Service Overview](/help/overview/introduction.md) - This guide provides an overview of Experience Manager as a Cloud service, including an introduction, terminology, and architecture.
* [Onboarding Journey](/help/journey-onboarding/overview.md)- This guide provides a summary of how to get started with Experience Manager as a Cloud Service, including how to get access and set up your team.
