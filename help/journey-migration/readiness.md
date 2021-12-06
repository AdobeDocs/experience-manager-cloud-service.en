---
title: Determining if your Deployment is Ready to be Moved to AEM as a Cloud Service 
description: Learn about the steps you need to take in order to make sure that your AEM installation is ready to be moved to the cloud
---
# Determining if your Deployment is Ready to be Moved to AEM as a Cloud Service  {#determining-if-your-deployment-is-ready}

In this part of the AEM as a Cloud Service Migration Journey you will familiarize yourself with AEM as a Cloud Service, review the notable changes that it has introduced and understand what it takes to plan for a successful migration to the cloud.

## The Story So Far {#story-so-far}

In the previous document of the journey, [Getting Started with Moving to AEM as a Cloud Service](/help/journey-migration/getting-started.md), you learned what are the benefits of moving to AEM as a Cloud Service, as well as an overview of the steps needed to do so.

<!-- Alexandru: to review if this is still needed

>[!CONTEXTUALHELP]
>id="aemcloud_cam_planning"
>title="Planning your Transition"
>abstract="Before beginning your transition journey to Cloud Service, you should familiarize yourself with AEM as a Cloud Service and review the notable changes that have been made to it and also review the features that have been replaced or deprecated."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/best-practices-analyzer/overview-best-practices-analyzer.html" text="Best Practices Analyzer" -->

## Objective {#objective}

This document helps you understand what factors you need to take into account in order to make sure your AEM installation is ready to be moved to the cloud:

* Learn about notable changes and deprecated features
* Understand the planning phase of the migration

## Notable Changes {#notable-changes}

AEM as a Cloud Service brings many new features and possibilities for managing your AEM projects.

Along with these improvements, a number of differences have been introduced between on-premise installations of AEM and Adobe Managed Services, compared to AEM as a Cloud Service.

We recommend you review these changes by consulting the [Notable Changes in AEM Cloud Service](/help/release-notes/aem-cloud-changes.md) documentation.

## Deprecated Features {#deprecated-features}

Adobe constantly evaluates product capabilities, to over time reinvent or replace older features with more modern alternatives to improve overall customer value, always under careful consideration of backward compatibility.

We recommend you consult the [Deprecated Features](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/deprecated-removed-features.html#deprecated-features) to familiarize yourself with the features and capabilities that have been marked as deprecated in Experience Manager as a Cloud Service and see what the impact is for your AEM deployment.

## Cloud Manager {#cloud-manager}

A notable new feature of AEM as a Cloud Service is Cloud Manager, the mechanism for deploying code to Cloud Service environments.

To get up to speed on how to use Cloud Manager to manage and deploy your code, follow the resources below: 

* [Managing Environments](/help/implementing/cloud-manager/manage-environments.md)

* [Configuring your CI-CD Pipeline](/help/implementing/cloud-manager/configure-pipeline.md)

* [Deploying your Code](/help/implementing/cloud-manager/deploy-code.md)

## Plan for a Review of your AEM Installation {#review-planning}

Once you have accustomed yourself with the changes introduced with AEM as a Cloud Service, it is time to start planning for a review of your existing installation, in order to gauge the level of changes required in order to move it to the cloud.

The following figure showcases key steps involved during the review phase:

![image](/help/move-to-cloud-service/assets/planning-phaseimg1.png)

Next, we will explore what each of these steps means in detail.

### Assessing Cloud Service Readiness {#assess-cloud-readiness}

The first step is to assess your readiness to move from your existing AEM version to Cloud Service and determine areas that will require refactoring in order to be compatible with AEM as a Cloud Service.

You will need to undertake a comprehensive assessment of your current AEM source code against the notable changes and deprecated features to determine the level of effort expected in the transition journey.

The number of findings will directly influence the timelines and overall project success. Hence it is recommended to uncover as much as possible to plan the delivery or to initiate the conversations needed to redesign any customizations required to be in line with AEM as a Cloud Service best practices.

You can accelerate the assessment by running the Best Practices Analyzer on your current AEM version. You can read up on how it works by consulting the [Best Practices Analyzer](/help/move-to-cloud-service/best-practices-analyzer/overview-best-practices-analyzer.md) documentation.

If you already have access to a Cloud Service environment, it is recommended to run your current code in a Cloud Manager [code quality pipeline](/help/implementing/cloud-manager/code-quality-testing.md) to assess the required code changes to be compatible with Cloud Service.

### Be Aware of Considerable Changes in the AEM as a Cloud Service Architecture {#be-aware-of-considerable-changes-in-aem-cloud-service}

The list of items in the following table are only subset of the changes and are worth highlighting.

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
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/aem-cloud-changes.html?lang=en">AEM as a Cloud Service Notable Changes</a><br><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-project-content-package-structure.html#mutable-vs-immutable">AEM Project Structure for AEM as a Cloud Service</a></td>
    <td>A single package that can be deployed into AEM as a Cloud Service can have sub packages, primarily to contain mutable and immutable content separated into their own packages.</td>
  </tr>
  <tr>
    <td>Repo Init</td>
    <td><a href="https://sling.apache.org/documentation/bundles/repository-initialization.html#the-repoinit-repository-initialization-language">Apache Sling RepoInit Documentation</a></td>
    <td>Repoinit scripts are the best practice to create any initial node structures, users, groups or service users. As these scripts can be targeted by run mode and manageable via code package deployment, they provide much flexibility to achieve repository initialization tasks.</td>
  </tr>
  <tr>
    <td>Custom Run modes are not allowed</td>
    <td></td>
    <td>Only run modes provided out of the box with AEM as a Cloud Service are supported.<br>When additional Development environments are added all of them tie to the “dev” run mode.</td>
  </tr>
  <tr>
    <td>Cloud Manager Pipeline Execution is the only way to deploy</td>
    <td></td>
    <td>In AEM as a Cloud Service, there is no access to /system/console, hence all OSGi configurations must be part of code and should be deployed as code.<br>The OSGi configurations are available in read only mode for viewing through Developer Console through Cloud Manager</td>
  </tr>
  <tr>
    <td>Replication Agents are replaced by Sling Content Distribution</td>
    <td></td>
    <td>The concept of replication agent is replaced by Sing Content Distribution. Therefore, if there are customizations leveraging replication agents, they must be redesigned.<br>Reverse replication is not supported</td>
  </tr>
  <tr>
    <td>CRX/DE and Package Manager</td>
    <td></td>
    <td>CRX/DE is allowed only on the Development environment.<br>Package Manger is accessible on all author instances but the packages that are going to be deployed must contain only mutable content ( for example: /content or /conf)</td>
  </tr>
  <tr>
    <td>Built in CDN and Get your own CDN</td>
    <td></td>
    <td>AEM as a Cloud Service includes the CDN for all environments which is optimized for most use cases.<br>If you wish to set up your own CDN you must submit a request to Adobe for it to be approved.<br>If it is approved, the CDN will point to Fastly and not to AEM instances in any environments.</td>
  </tr>
  <tr>
    <td>Long Running Jobs</td>
    <td></td>
    <td>Avoid executing long running Jobs such as Sling Schedulers or Cron jobs, as the AEM instances executing in the containers can come and go at any point of time.<br>Rethink these functionalities to offload them to Adobe IO.</td>
  </tr>
  <tr>
    <td>Switch to Asynchronous Operations</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/asynchronous-jobs.html?lang=en#configuring-asynchronous-msm-operations">Configuring Asynchronous Operations</a></td>
    <td>To improve the overall performance of your environments, certain operations are executed in async mode. The async jobs will be queued and executed when system resources are available.</td>
  </tr>
  <tr>
    <td>Token based authentication and integration strategies</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/generating-access-tokens-for-server-side-apis.html?lang=en#the-server-to-server-flow">Generating Access Tokens for Server side APIs</a><br><a href="https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/overview.html?lang=en#authentication">Token based Authentication Tutorial</a></td>
    <td>It is quite common that systems external to AEM are trying to perform HTTP operations within AEM.<br>The recommended approach is to implement the strategies outlined here rather than relying on creating local usernames with passwords in AEM.</td>
  </tr>
  <tr>
    <td>File IO / Disk Usage</td>
    <td></td>
    <td>As there is no guarantee of how much disk space is allocated and the instances in containers come and go, it is not advisable to use File I/O operations to write or read from the disk attached to the AEM instance.</td>
  </tr>
  <tr>
    <td>DAM Update Asset Workflow</td>
    <td><a href="https://experienceleague.adobe.com/docs/asset-compute/using/introduction.html?lang=en">Asset Compute Service</a></td>
    <td>The media processing steps that are part of DAM Update Asset workflow are now replaced by the Asset Compute Service</td>
  </tr>
  <tr>
    <td>Asset upload methods and supported workflow process steps in AEM as a Cloud Service</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/assets/admin/developer-reference-material-apis.html?lang=en#post-processing-workflows-steps">Upload API Comparions and Supported WF Process Steps</a></td>
    <td>In AEM as a Cloud Service, either during upload or download of an asset the asset streams directly in or out of binary storage.</br>Not all workflow process steps are supported in AEMaaCS.</td>
  </tr>
  <tr>
    <td>Workflow Launchers</td>
    <td></td>
    <td>Remove any Workflow Launchers that are triggering either OOTB or custom DAM Update Asset Workflow from your code.</br>All the assets uploaded into AEM as a Cloud Service are going to be processed by the Asset Processing Service.There is a Workflow post processing OSGi configuration which can be used to trigger additional custom processing steps.</td>
  </tr>
  <tr>
    <td>Custom Rendition Steps</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/assets/manage/asset-microservices-configure-and-use.html?lang=en#manage">Processing Profiles</a></td>
    <td>Any custom rendition generation, image conversions or video encodings must be offloaded to the Asset Processing Service by creating corresponding processing profiles.</td>
  </tr>
  <tr>
    <td>Content Search and Indexing</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/indexing.html?lang=en">Content Search and Indexing Changes</a></td>
    <td>There are considerable changes to the underlying processing of indexes and when it is kicking in.<br>Completely understand and refactor the Oak Indexes before managing them in the code that you will deploy.</td>
  </tr>
  <tr>
    <td>Not all maintenance tasks are configurable</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/maintenance.html?lang=en">AEM as a Cloud Service Maintenance Tasks</a></td>
    <td>You can configure only certain maintenance tasks with AEM as a Cloud Service.</td>
  </tr>
  <tr>
    <td>Changes to Publish repository</td>
    <td></td>
    <td>Direct changes to the Publish repository are not allowed, except those under /home. It is always recommended to make the changes on author and distribute them. All code and configuration changes must be deployed through the corresponding Cloud Manager pipeline.</td>
  </tr>
  <tr>
    <td>Dispatcher Configurations and Caching</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/content-delivery/disp-overview.html?lang=en#content-delivery">Dispatcher in the Cloud</a><br><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/content-delivery/caching.html?lang=en#other-content">Cache Management<br></td>
    <td>The dispatcher configurations must follow a specific structure.<br>The configurations must be managed as part of code and deployed through the Cloud Manager pipeline.</td>
  </tr>
  <tr>
    <td>Backup and Restore</td>
    <td><a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/backup.html?lang=en">AEM as a Cloud Service Backup and Restore</a></td>
    <td></td>
  </tr>
</tbody>
</table>

### Understand Best Practice Analyzer Codes and Resolutions {#understand-bpa-codes-and-resolutions}

One of the useful resources that aides the assessment is the report generated by the Best Practice Analyzer. The important column in each line items in that report is a CODE (e.g.: CAV, LUI, NBCC etc.).

Having a good understanding of what each code means and the corresponding path to resolution comes very handy while creating the Assessment Report.
Please refer to the BPA Codes available as part of public documentation.

### Reviewing Resource Planning {#review-resource-planning}

Once you have estimated the level of effort that will be required to move to Cloud Service, you should identify resources, create a team, and map out roles and responsibilities for the transition process.

### Establishing KPIs {#establish-kpis}

If you have not established Key Performance Indicators (KPIs) previously, it is recommended to establish KPIs for your AEM implementation to help your team focus on what matters the most.

See [Developing KPIs](https://guided.adobe.com/welcome/aem/part6.html) to learn how to choose the right KPIs for your business objectives.

## What's Next {#what-is-next}

Once you understand the scope of the changes required to move to AEM as a Cloud Service, it's time to [Make your code and content cloud ready](/help/journey-migration/making-your-code-and-content-cloud-ready.md) before actually performing the migration.

## Additional Resources {#additional-resources}

This is where additional resources should be.
