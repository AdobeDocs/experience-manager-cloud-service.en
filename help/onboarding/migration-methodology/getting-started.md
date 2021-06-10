---
title: Migration to Experience Manager as a Cloud Service
description: Migration to Experience Manager as a Cloud Service
exl-id: 4d1addcf-b22d-41a3-ba5c-e5c42244e5cd
---
# Migration to Adobe Experience Manager as a Cloud Service {#Overview}

>[!CONTEXTUALHELP]
>id="aemcloud_migration_overview"
>title="Migration to AEM as a cloud Service"
>abstract="Outlines the recommended phased approach to transition customers from various Experience Manager deployments to Experience Manager as a Cloud Service and help existing customers deliver connected, continuous experiences"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/overview/what-is-new-and-different.html?lang=en" text="What's new & different?"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/overview/introduction.html?lang=en" text="Introduction to AEM as a Cloud Service."

Adobe Experience Manager (AEM) as a Cloud Service offers a re-architected foundation for Experience Manager, built upon a container-based infrastructure, API-driven development, and guided DevOps process, allowing marketers and developers to always keep ahead of the curve in customer experience management innovations.

Cloud Service brings together rich out-of-the-box capabilities and extensibility of Adobe Experience Manager with agility of the modern cloud-native architecture enabling brands to meet the ever-evolving consumer demand.

This one-pager outlines the recommended phased approach to transition customers from various Experience Manager deployments to Experience Manager as a Cloud Service and help existing customers deliver connected, continuous experiences on this modern, purpose-built platform for experience management.

<!-- It primarily focuses on:
* Getting Started with Adobe Experience Manager as a Cloud Service
* Developer Journey in Adobe Experience Manager as a Cloud Service
* Moving to Adobe Experience Manager as a Cloud Service -->

<br>

## Getting Started with Adobe Experience Manager as a Cloud Service {#getting-started}

| What's different? | Architecture Overview |
|--------------------------|--------------------------|
| <ul><li>[Modern Architecture](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/core-concepts/architecture.html)</li><li>[Automatic Updates](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/aem-version-updates.html?lang=en#aem-version-updates)</li><li>[Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/introduction-to-cloud-manager.html)</li><li>[Asset Microservices](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/assets/asset-microservices-overview.html)</li><li>[Direct-Access Binaries](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/assets/asset-microservices-overview.html?lang=en#asset-upload-with-direct-binary-access)</li><li>[Separation of code and content](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-project-content-package-structure.html?lang=en#developing)</li><li>[Replication as a Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/replication.html?lang=en)</li><li>[Admin console, Group/User Membership and ACLs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/security/ims-support.html)</li></ul>| <ul><li>[Introduction to AEM Architecture](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/underlying-technology/introduction-architecture.html?lang=en#underlying-technology)</li><li>[Environment Stack](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/core-concepts/architecture.html)</li><li>[Author Tier](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/underlying-technology/introduction-author-publish.html?lang=en#underlying-technology)</li><li>[Publish Tier](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/underlying-technology/introduction-author-publish.html?lang=en#underlying-technology)</li><li>[Dispatcher](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/content-delivery/disp-overview.html?lang=en#content-delivery)</li><li>[CDN](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/content-delivery/cdn.html?lang=en#content-delivery) </li><li>[Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/introduction-to-cloud-manager.html) (CI/CD)</li><li>[Identity Management](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/security/ims-support.html?lang=en#onboarding-users-in-admin-console) via [Admin console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/security/ims-support.html)</li><li>[Asset Compute Service](https://experienceleague.adobe.com/docs/asset-compute/using/home.html)</li></ul> |

![AEM as a Cloud Service - Runtime Architecture](/help/core-concepts/assets/concepts-03.png "AEM as a Cloud Service - Runtime Architecture")

<br>

## Developer Journey in Adobe Experience Manager as a Cloud Service {#developer-journey}

### Developing 

The fundamentals of code development are similar in Adobe Experience Manager as a Cloud Service compared to the Adobe Experience Manager On Premise and Managed Services solutions. 

Developers write code and test it locally, which is then pushed to remote Adobe Experience Manager as a Cloud Service environments. 

See self-help resources about implementation for Experience Manager as a Cloud Service to learn how to customize your Experience Manager as a Cloud Service deployment.

|Local Development Setup|Things to know before you start|
|-----------|------------|
|<ol><li>Review [Adobe Experience Manager SDK](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-as-a-cloud-service-sdk.html?lang=en#developing) documentation to learn more.</li><li>Watch [Install Dispatcher SDK](https://video.tv.adobe.com/v/30601) to understand how to install Dispatcher SDK</li><li>Watch [Configure Dispatcher SDK](https://video.tv.adobe.com/v/30602) to understand on how to configure Dispatcher SDK</li><li>Review [Local Development Setup](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview.html?lang=en#local-development-environment-set-up) documentation to learn more</li><li>Configuring access to Experience Manager [walk-through](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/walk-through.html?lang=en#accessing)</li></ol> | <ol><li>[Development Essentials](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-as-a-cloud-service-sdk.html?lang=en#developing)</li><li>[Development Guidelines](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html?lang=en#developing)</li><li>[Understanding Experience Manager Project Structure](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-project-content-package-structure.html?lang=en#developing)</li><li>[Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html)</li><li>[Digital Foundation Blueprint](https://solutionpartners.adobe.com/content/dam/spp_assets/restricted/community/community_31/digital_foundation_best_practices_and_documentation.zip)</li><li>[Style System](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/sites/authoring/features/style-system.html?lang=en#authoring)</li><li>[Overlays](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/overlays.html?lang=en#developing)</li><li>[Experience Manager as a Cloud Service API reference](https://docs.adobe.com/content/help/en/experience-manager-cloud-service-javadoc/)</li></ol>|

>[!TIP]
> See tutorial on how to [Develop and Deploy WKND on local Experience Manager SDK](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/overview.html?lang=en)

### Deploying

 Developers write code and test it locally, which is then pushed to remote AEM as a Cloud Service environments. 
  
  Cloud Manager, which was an optional content delivery tool for Managed Services, is required. This is now the sole mechanism for deploying code to AEM as a Cloud Service environments.

  See self-help resources about how to configure and deploy to AEM as a Cloud Service environments.

1. [Configure CM Pipelines](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/configure-pipeline.html?lang=en#using-cloud-manager)
      * Production Pipeline
      * Non-Production & Code Quality Only Pipelines 
  2. [Deploy Code](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/deploy-code.html?lang=en#using-cloud-manager)
  3. [Understanding Your Test Results](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/test-results/overview-test-results.html?lang=en#using-cloud-manager)
  4. **Accessing Logs**
      * [via CM UI](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-logs.html?lang=en#using-cloud-manager)
      * [via Adobe i/o cli](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/logs.html?lang=en#debugging)
  5. [Operations and Maintenance](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/home.html?lang=en)
     * [Configuring OSGI configuration](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/configuring-osgi.html?lang=en#deploying)
      * [Backup and Restore](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/backup.html?lang=en)

>[!TIP]
> See tutorial on how to [Deploy WKND to Experience Manager Cloud  Service](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/develop-wknd-tutorial.html?lang=en)  

### Help and Resources

1. [Debugging tips and tricks](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/overview.html?lang=en#debugging-aem-as-a-cloud-service)
  2. [Developer Console](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console.html?lang=en#debugging)
  3. [CRXDE Lite](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/crxde-lite.html?lang=en#debugging) (Only available on local SDK and Experience Manager Cloud Dev environments)
  4. [Logs and logging](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/logs.html?lang=en#debugging)
      * [CM Logs](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/build-and-deployment.html?lang=en#debugging) (build-unit-testing, code-scanning, build-image, deploy)
      * [Experience Manager Cloud Service Logs](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/logs.html?lang=en#debugging) (aemerror, aemaccess, aemrequest, aemdispatcher, httpderror, httpaccess)
      * Local SDK Logs (under host:port/crx-quickstart/logs)

>[!NOTE]
> For additional help, you may want to :
>1. [Contact the Experience Manager Support Team](https://experienceleague.adobe.com/docs/customer-one/using/home.html?lang=en)
>2. Explore [Experience Manager Communities & Forums](https://experienceleaguecommunities.adobe.com/t5/adobe-experience-manager/ct-p/adobe-experience-manager-community)

<br>

## Moving to Adobe Experience Manager as a Cloud Service {#move-to-cloud}

>[!CONTEXTUALHELP]
>id="aemcloud_move_to_cloud"
>title="Moving to Adobe Experience Manager as a Cloud Service"
>abstract="This one-pager outlines the recommended phased approach to transition customers from various Experience Manager deployments to Experience Manager as a Cloud Service and help existing customers deliver connected, continuous experiences on this modern, purpose-built platform for experience management."

**Experience Manager as a Cloud Service provides a scalable, secure, and agile technology foundation for Experience Manager Sites and Assets, enabling marketers and IT to focus on delivering impactful experiences at scale.**
 
With Experience Manager as a Cloud Service, your teams can focus on innovating instead of planning for product upgrades. New product features are thoroughly tested and delivered to your teams without any interruption so that they always have access to the state-of-the art application.

The transition journey to Cloud Service involves three phases - Planning, Execution, and Post Go-live.
For a successful and smooth transition, you should ensure proper planning and adhere to best practices outlined in this Guide.

The figure below shows a pictorial representation of the recommended transition journey to Cloud Service.

![image](/help/move-to-cloud-service/assets/home-img1.png)

<br>

### Planning

Before beginning your transition journey to Cloud Service, you should familiarize yourself with Experience Manager as a Cloud Service and review the notable changes that have been made to it and also review the features that have been replaced or deprecated.

<table>
<tr>
<td>Project discovery and assessment</td>
<td><ul><li>Refer to <a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/aem-cloud-changes.html?lang=en">Notable Changes to Experience Manager as a Cloud Service</a> to understand the important differences between Adobe Experience Manager as a Cloud Service and Experience Manager 6.x.</li><li>Refer to <a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/deprecated-removed-features.html?lang=en#deprecated-features">Deprecated Features</a> to learn more about features and capabilities that have been marked as deprecated.</li><li>[For Cloud Service Migrations only] Assessing Cloud Service Readiness : Run the <a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/best-practices-analyzer/overview-best-practices-analyzer.html?lang=en#cloud-migration">Best Practices Analyzer(BPA)</a> on source environment </li><li>Complete an assessment against notable changes and deprecated features in Experience Manager CS</li></ul></td>
</tr>
<tr>
<td>Review</td>
<td><ul><li>Based on discovery, perform effort estimation and resourcing exercises</li></ul></td>
</tr>
<tr>
<td>Measure</td>
<td><ul><li><a href="https://experienceleague.adobe.com/welcome/aem/part6.html">Establish Project KPIs</a>, success criteria and project timelines</li></ul></td>
</tr>
</table>

>[!NOTE]
>The Best Practices Analyzer Report speeds up the process of estimating the time and cost that is required to transition to AEM as a Cloud Service by providing information that would otherwise have to be manually gathered and evaluated.
 

<br>

### Execution

Before you start the Execution phase of a project, you should be on-boarded to Cloud Service. You also need to familiarize yourself with Cloud Manager. This is the mechanism for deploying project code to an Experience Manager Cloud Service instance.

Cloud Manager enables organizations to self-manage Experience Manager in the Cloud. It includes a continuous integration and continuous delivery ([CI/CD](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/overview/ci-cd-pipeline.html?lang=en#overview)) framework that lets IT teams and implementation partners expedite the delivery of customizations or updates without compromising performance or security.

#### Content Migration

1. [Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/migration/content-transfer-tool.html?lang=en#migration) : used to move existing content over from a source AEM instance (on-premise or AMS) to the target AEM Cloud Service instance.
2. [Package Manager](https://experienceleague.adobe.com/docs/experience-manager-65/administering/contentmanagement/package-manager.html?lang=en#package-manager) : used for importing and exporting of mutable content of the repository.


#### Refactor/Optimize

|Getting Started|Review & Refactor Code|Dispatcher Review|
|---|---|---|
|<ul><li>[Local Dev setup](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview.html?lang=en#local-development-environment-set-up)</li><li>[Local Dispatcher Setup](https://video.tv.adobe.com/v/30602/)</li><li>[Compile your code using SDK API jar](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-as-a-cloud-service-sdk.html?lang=en#developing)</li><li>[Review AEM Dev Guidelines](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html?lang=en#developing)<ul><li>Background Tasks and Long Running Jobs</li><li>Sling schedulers</li><li>Input stream usage & more</li></ul></li></ul>|<ul><li>Run the [Best Practices Analyzer(BPA)](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/best-practices-analyzer/overview-best-practices-analyzer.html?lang=en#cloud-migration) on source environment.[**Migration only**]<ul><li>Project Structuring considerations (based on [Cloud Archetype](https://github.com/adobe/aem-project-archetype))<ul><li>Separation of code and content (Mutable vs Immutable)</li><li>[Custom index definitions](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/operations/indexing.html?lang=en#indexing)</li><li>[Custom runmodes](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/overview.html?lang=en#runmodes)</li></ul></li></ul></li><li>Review and execute on necessary changes</li><li>[Deploy](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/overview.html?lang=en) it on local SDK</li><li>Perform smoke testing via AEM SDK</li></ul>|<ul><li>Review [Dispatcher configurations](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/content-delivery/disp-overview.html?lang=en#local-validation-of-dispatcher-configuration) for refactoring</li><li>Leverage [Dispatcher Converter](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/refactoring-tools/dispatcher-transformation-utility-tools.html?lang=en#introduction-dispatcher) tool where appropriate. [**Migration only**]</li><li>Testing can be conducted using [Dispatcher SDK](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/dispatcher-tools.html?lang=en#prerequisites)</li></ul>|

>[!TIP]
> Assets Customers : Review & Refactor Assets Workflows using [Asset Cloud Migration](https://github.com/adobe/aem-cloud-migration) tooling 


#### Deployment/Go-Live

  1. [Deploy to Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/managing-code/setup-cloud-manager-git-integration.html?lang=en#managing-code) git
  2. Run customer code through the [Cloud Manager Quality Pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/understand-your-test-results.html?lang=en#how-to-use)
  3. [Deploy to Development Environment](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/build-and-deployment.html?lang=en#debugging)
  4. [**Migration only**] Content transfer using packages or [Content Transfer Tool](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md)(CTT)
  5. Perform recommended testing cycles (smoke, QA and more)
  6. Promote to the Cloud Manager Production Pipeline 
  7. Smoke test validation
  8. Go-Live 

<br>

### Post Go-Live

In the Post Go-live phase, you should ensure clean-up of temporary files, review best practices for continuous development and manage logs.

>[!TIP]
> Tools are available to troubleshoot AEM as a Cloud Service environments
>1. [Developer Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html?lang=en#aem-as-a-cloud-service-development-tools)
>2. [CRX/DE Lite](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/crxde-lite.html?lang=en#debugging)
>3. [Managing Logs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-logs.html?lang=en#using-cloud-manager)

<br>

### Tools & Resources
  
| Assessment | Refactoring | Experience Manager Modernization| Content Migration | 
|------------|-------------|---------------------------------|-------------------|
|<ul><li>[Best Practices Analyzer](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/best-practices-analyzer/overview-best-practices-analyzer.html?lang=en#cloud-migration)</li></li>| <ul><li>[Unified Experience Plugin](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/refactoring-tools/unified-experience.html?lang=en#refactoring-tools)</li></ul>      |     <ul><li>[Static templates to editable templates](https://opensource.adobe.com/aem-modernize-tools/pages/tools/page-structure.html)</li><li>[Design configurations to policies](https://opensource.adobe.com/aem-modernize-tools/pages/tools/policy-importer.html) <li>[Foundation Components to Core Components](https://opensource.adobe.com/aem-modernize-tools/pages/tools/component.html)</li><li>[Classic UI to Touch-Enabled UI](https://opensource.adobe.com/aem-modernize-tools/pages/tools/dialog.html)</li></ul>       | <ul><li>[Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#cloud-migration)</li><li>[Package Manager](https://experienceleague.adobe.com/docs/experience-manager-65/administering/contentmanagement/package-manager.html?lang=en#contentmanagement)</li></ul> |     

>[!NOTE]
> For additional help, you may want to :
>1. [Contact the Experience Manager Support Team](https://experienceleague.adobe.com/docs/customer-one/using/home.html?lang=en)
>2. Explore [Experience Manager Communities & Forums](https://experienceleaguecommunities.adobe.com/t5/adobe-experience-manager/ct-p/adobe-experience-manager-community)
