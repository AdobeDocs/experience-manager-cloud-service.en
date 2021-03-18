---
title: Deploying to AEM as a Cloud Service
description: Deploying to AEM as a Cloud Service 
---

# Deploying to AEM as a Cloud Service {#deploying-to-aem-as-a-cloud-service}

## Introduction {#introduction}

The fundamentals of code development are similar in AEM as a Cloud Service compared to the AEM On Premise and Managed Services solutions. Developers write code and test it locally, which is then pushed to remote AEM as a Cloud Service environments. Cloud Manager, which was an optional content delivery tool for Managed Services, is required. This is now the sole mechanism for deploying code to AEM as a Cloud Service environments.

The update of the [AEM version](/help/implementing/deploying/aem-version-updates.md) is always a separate deployment event from pushing [custom code](#customer-releases). Viewed in another way, custom code releases should be tested against the AEM version that is on production since that is what it will be deployed on the top. AEM version updates that happen after that, which will be frequent and are automatically applied. They are intended to be backward compatible with the customer code already deployed.

The rest of this document will describe how developers should adapt their practices so they work with both AEM as a Cloud Service's Version updates and customer updates. 

>[!NOTE]
>It is recommended for customers with existing code bases, to go through the repository restructuring exercise described in the [AEM documentation](https://docs.adobe.com/help/en/collaborative-doc-instructions/collaboration-guide/authoring/restructure.html).

## Customer Releases {#customer-releases}

### Coding against the right AEM version {#coding-against-the-right-aem-version}

For previous AEM solutions, the most current AEM version changed infrequently (roughly annually with quarterly service packs) and customers would update the production instances to the latest quickstart on their own time, referencing the API Jar. However, AEM as a Cloud Service applications are automatically updated to the latest version of AEM more often, so custom code for internal releases should be built against the latest AEM version.

Like for existing non-cloud AEM versions, a local, offline development based on a specific quickstart will be supported and is expected to be the tool of choice for debugging in the majority of cases.

>[!NOTE]
>There are subtle operational differences between how the application behaves on a local machine versus the Adobe Cloud. These architectural differences must be respected during local development and could lead to a different behavior when deploying on the cloud infrastructure. Because of these differences it is important to perform the exhaustive tests on dev and stage environments before rolling out new custom code in production.

In order to develop custom code for an internal release, the relevant version of the [AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md) should be downloaded and installed. For additional information about using the AEM as a Cloud Service Dispatcher Tools, see [this page](/help/implementing/dispatcher/disp-overview.md).

The following video provides a high level overview on how to deploy code to AEM as a Cloud Service:

>[!VIDEO](https://video.tv.adobe.com/v/30191?quality=9)

>[!NOTE]
>It is recommended for customers with existing code bases, to go through the repository restructuring exercise described in the [AEM documentation](https://docs.adobe.com/help/en/collaborative-doc-instructions/collaboration-guide/authoring/restructure.html). 

## Deploying Content Packages via Cloud Manager and Package Manager {#deploying-content-packages-via-cloud-manager-and-package-manager}

### Deployments via Cloud Manager {#deployments-via-cloud-manager}

Customers deploy custom code to cloud environments through Cloud Manager. It should be noted that Cloud Manager transforms locally assembled content packages into an artifact conforming to the Sling Feature Model, which is how an AEM as a Cloud Service application is described when running in a cloud environment. As a result, when looking at the packages in Package Manager on Cloud environments, the name will include "cp2fm" and the transformed packages have all metadata removed. They cannot be interacted with, meaning they cannot be downloaded, replicated, or opened. Detailed documentation about the converter can be [found here](https://github.com/apache/sling-org-apache-sling-feature-cpconverter).

Content packages written for AEM as a Cloud Service applications must have a clean separation between immutable and mutable content and Cloud Manager will enforce it by failing the build, outputting a message like:

`Generated content-package <PACKAGE_ID> located in file <PATH> is of MIXED type`

The rest of this section will describe the composition and implications of immutable and mutable packages.

### Immutable Content Packages {#immutabe-content-packages}

All content and code persisted in the immutable repository must be checked into git and deployed through Cloud Manager. In other words, unlike current AEM solutions, code is never deployed directly to a running AEM instance. This ensures that the code running for a given release in any Cloud environment is identical, which eliminates the risk of unintentional code variation on production. As an example, OSGI configuration should be committed to source control rather than managed at runtime via the AEM web console's configuration manager.

As application changes due to the Blue-Green deployment pattern are enabled by a switch, they cannot depend on changes in the mutable repository with the exception of service users, their ACLs, nodetypes and index definition changes.

For customers with existing code bases, it is critical to go through the repository restructuring exercise described in AEM documentation to ensure that content formerly under the /etc is moved to the right location.

Some additional restrictions apply for these code packages, for example [install hooks](http://jackrabbit.apache.org/filevault/installhooks.html) are not supported.

## OSGI Configuration {#osgi-configuration}

As mentioned above, OSGI configuration should be committed to source control rather than through the web console. Techniques to do so include:

* Making the necessary changes on the developer's local AEM environment with the AEM web console's configuration manager and then exporting the results to the AEM project on the local file system
* Creating the OSGI configuration manually in the AEM project on the local file system, the referencing the AEM console's configuration manager for the property names.

Read more about OSGI configuration at [Configuring OSGi for AEM as a Cloud Service](/help/implementing/deploying/configuring-osgi.md).

## Mutable Content {#mutable-content}

In some cases it might be useful to prepare content changes in source control so it can be deployed by Cloud Manager whenever an environment was updated. For example, it might be reasonable to seed certain root folder structures or line up changes in editable templates to enable policies in those for components that were updated by the application deployment.

There are two strategies to describe the content that will be deployed by Cloud Manager to the mutable repository, mutable content packages and repoinit statements.

### Mutable Content Packages {#mutable-content-packages}

Content such as folder path hierarchies, service users, and access controls (ACLs) are typically committed into a maven archetype-based AEM project. Techniques include exporting from AEM or writing directly as XML. During the build and deployment process, Cloud Manager packages the resulting mutable content package. The mutable content is installed at 3 different times during the deploy phase in the pipeline: 

Ahead of startup of new version of application:

* index definitions (add, modify, remove)

During startup of new version of application but ahead of switchover:

* Service Users (add)
* Service User ACLs (add)
* node types (add)

After switchover to new version of application:

* All other content definable via jackrabbit vault. For example:
  * Folders (add, modify, remove)
  * Editable templates (add, modify, remove)
  * Context Aware configuration (anything under `/conf`) (add, modify, remove)
  * Scripts (packages can trigger Install hooks at various stages of the install process of package installation

It is possible to limit mutable content installation to author or publish by embedding packages in an install.author or install.publish folder under `/apps`. Details to be found in [AEM documentation](https://docs.adobe.com/content/help/en/experience-manager-65/deploying/restructuring/repository-restructuring.html) around recommended project restructuring.

>[!NOTE]
>Content packages are deployed to all environment types (dev, stage, prod). It is not possible to limit deployment to a specific environment. This limitation is in place to ensure the option of a test run of automated execution. Content that is specific to an environment requires manual installation via Package Manager.

Also, there is no mechanism to rollback the mutable content package changes after they've been applied. If customers detect a problem, they can choose to fix it in their next code release or as a last resort, restore the entire system to a point in time before the deployment.

Any included 3rd party packages must be validated as being AEM as a Cloud Service Service compatible, otherwise its inclusion will result in a deployment failure.

As mentioned above, customers with existing code bases should conform to the repository restructuring exercise necessitated by the 6.5 repository changes described in the [AEM 6.5 documentation.](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/restructuring/repository-restructuring.html)

## Repoinit {#repoinit}

For the following cases, it is preferable to take the approach of hand coding explicit content creation `repoinit` statements in OSGI factory configurations:

* Create/delete/disable service users
* Create/delete groups
* Create/delete users
* Add ACLs

  >[!NOTE]
  >
  >Definition of ACLs requires the node structures to be already present. Thus, preceding create path statements might be necessary.

* Add path (for example for root folder structures)
* Add CNDs (nodetype definitions)

Repoinit is preferable for these supported content modification use cases due to the following benefits:

* Repoinit creates resources at startup so logic can take the existence of those resources for granted. In the mutable content package approach, resources are created after startup, so application code relying on them may fail.
* Repoinit is a relatively safe instruction set as you explicitly control the action to be taken. Also, the only supported operations are additive with the exception of a few security related cases which allow removal of Users, Service Users, and Groups. In contrast, a removal of something in the mutable content package approach is explicit;  as you define a filter anything present covered by a filter will be deleted. Still, caution should be taken since with any content there are scenarios where the presence of new content can alter the behavior of the application.
* Repoinit performs fast and atomic operations. Mutable content packages in contrast can highly depend performance wise on the structures covered by a filter. Even if you update a single node, a snapshot of a large tree might be created.
* It is possible to validate repoinit statements on a local dev environment at runtime since they will be executed when the OSGi configuration gets registered.
* Repoinit statements are atomic and explicit and will skip if the state is already matching.

When Cloud Manager deploys the application, it executes these statements, independently from the installation of any content packages.

To create repoinit statements, follow the below procedure:

1. Add OSGi configuration for factory PID `org.apache.sling.jcr.repoinit.RepositoryInitializer` in a configuration folder of the project. Use a descriptive name for the configuration like **org.apache.sling.jcr.repoinit.RepositoryInitializer~initstructure**.
1. Add repoinit statements to the script property of the config. The syntax and options are documented in [Sling documentation](https://sling.apache.org/documentation/bundles/repository-initialization.html). Note that there should be explicit creation of a parent folder before their child folders. For example, an explicit creation of `/content` before `/content/myfolder`, before `/content/myfolder/mysubfolder`. For ACLs being set on low level structures it is recommended to set those on a higher level and work with a `rep:glob` restriction.  For example `(allow jcr:read on /apps restriction(rep:glob,/msm/wcm/rolloutconfigs))`.
1. Validate on the local dev environment at runtime.

<!-- last statement in step 2 to be clarified with Brian -->

>[!WARNING]
>
>For ACLs defined for nodes underneath `/apps` or `/libs` the repoinit execution will start on a blank repository. The packages are installed after repoinit so statements cannot rely on anything defined in the packages but must define the preconditions like the parent structures underneath.

>[!TIP]
>
>For ACLs the creation of deep structures might be cumbersome, therefore is more reasonable to define an ACL on a higher level and constrain where it is supposed to act via a rep:glob restriction.

More detail about about repoinit can be found in the [Sling documentation](https://sling.apache.org/documentation/bundles/repository-initialization.html)

<!-- ### Packaging of Immutable and Mutable Packages {#packaging-of-immutable-and-mutable-packages}

above appears to be internal, to confirm with Brian -->

### Package Manager "one offs" for Mutable Content Packages {#package-manager-oneoffs-for-mutable-content-packages}

There are use cases where a content package should be installed as a "one off". For example importing specific content from production on to staging in order to debug a production issue. For these scenarios, Package Manager can be used in AEM as a Cloud Service environments.

Since Package Manager is a runtime concept, it is not possible to install content or code into the immutable repository, so these content packages should only consist of mutable content (mainly `/content` or `/conf`). If the content package includes content that is mixed (both mutable and immutable content), only the mutable content will be installed.

Any content-packages installed via Cloud Manager (both mutable and immutable) will appear in a frozen state in AEM Package Manager's user interface. These packages cannot be reinstalled, rebuilt or even downloaded, and will listed with a **"cp2fm"** suffix, indicating their installation was managed by Cloud Manager.

### Including Third Party Packages {#including-third-party}

It is common for customers to include pre-built packages from third party sources such as software vendors like Adobe's translation partners. The recommendation is to host these packages in a remote repository and reference them in the `pom.xml`. This is possible for public repositories and also for private repositories with password protection, as described in [password protected maven repositories](/help/onboarding/getting-access-to-aem-in-cloud/setting-up-project.md#password-protected-maven-repositories).

If storing the package in a remote repository is not possible, customers can place in a local, file system based Maven repository, which is committed to SCM as part of the project, and referenced by whatever depends on it. The repository would be declared in the project pomas illustrated below:


```
<repository>
    <id>project.local</id>
    <name>project</name>
    <url>file:${maven.multiModuleProjectDirectory}/repository</url>
</repository>
```

<!-- formatting appears broken in the code sample above, check how it appears on AEM -->

Any included third party packages must be adhere to the AEM as a Cloud Service Service coding and packaging guidelines described in this article, otherwise its inclusion will result in a deployment failure.

The following Maven POM XML snippet shows how 3rd party packages can be embedded in the project's "Container" package, typically named **'all'**, via the **filevault-package-maven-plugin** Maven plugin configuration.

```
...
<plugin>
  <groupId>org.apache.jackrabbit</groupId>
  <artifactId>filevault-package-maven-plugin</artifactId>
  <extensions>true</extensions>
  <configuration>
      ...
      <subPackages>
           
          <!-- Include the application's ui.apps and ui.content packages -->
          ...
 
          <!-- Include any other extra packages such as AEM WCM Core Components -->
          <!-- Set the version for all dependencies, including 3rd party packages, in the project's Reactor POM -->
          <subPackage>
              <groupId>com.adobe.cq</groupId>
              <artifactId>core.wcm.components.all</artifactId>
              <filter>true</filter>
          </subPackage>
 
 
          <subPackage>
              <groupId>com.3rdparty.groupId</groupId>
              <artifactId>core.3rdparty.artifactId</artifactId>
              <filter>true</filter>
          </subPackage>
      <subPackages>
  </configuration>
</plugin>
...
```

## How Rolling Deployments Work {#how-rolling-deployments-work}

Like AEM updates, customer releases are deployed using a rolling deployment strategy in order to eliminate author cluster downtime under the right circumstances. The general sequence of events is as described below, where **Blue** is the old version of customer code and **Green** is the new version. Both Blue and Green are running the same version of AEM code.

* Blue version is active and a release candidate for Green is built and available
* If there are any new or updated index definitions, the corresponding indexes are processed. Note that the blue deployment will always use the old indexes, while the green will always use the new indexes.
* Green is starting up while Blue is still serving
* Blue is running and serving while Green is being checked for readiness via health checks
* Green nodes that are ready accept traffic and replace Blue nodes, which are brought down
* Over time, Blue nodes are replaced by Green nodes until only Green remain, thus completing the deployment
* Any new or modified mutable content is deployed

## Indexes {#indexes}

New or modified indexes will cause an additional indexing or re-indexing step before the new (Green) version can take on traffic. Details about index management in AEM as a Cloud Service can be found in [this article](/help/operations/indexing.md). You can check the status of the indexing job on the Cloud Manager build page and will receive a notification when the new version is ready to take traffic.

>[!NOTE]
>
>The time needed for a rolling deployment will vary depending on the size of the index, since the Green version cannot accept traffic until the new index has been generated.

At this time, AEM as a Cloud Service does not work with index management tools such as ACS Commons Ensure Oak Index tool.

## Replication {#replication}

The publication mechanism is backwards compatible with the [AEM Replication Java APIs](https://helpx.adobe.com/experience-manager/6-3/sites/developing/using/reference-materials/diff-previous/changes/com.day.cq.replication.Replicator.html).

In order to develop and test with replication with the cloud ready AEM quickstart, the classic replication capabilities needs to be used with an Author/Publish setup. In the case of the UI entry point on AEM Author has been removed for the cloud, users would go to `http://localhost:4502/etc/replication` for configuration.

## Backwards Compatible Code for Rolling Deployments {#backwards-compatible-code-for-rolling-deployments}

As detailed above, AEM as a Cloud Service's rolling deployment strategy implies that both the old and new versions may be operating at the same time. Therefore, be cautious of code changes that are not backwards compatible with the old AEM version that is still operation.

In addition, the old release should be tested for compatibility with any new mutable content structures applied by the new release in the event of roll back, since mutable content is not removed.

### Service Users and ACL Changes {#service-users-and-acl-changes}

Changing service users or ACLs needed to access content or code could lead to errors in the older AEM versions resulting in access to that content or code with outdated service users. To address this behavior, a recommendation is to make changes spread across at least 2 releases, with the first release acting as a bridge before cleaning up in the subsequent release.

### Index Changes {#index-changes}

If changes to indexes are made, it is important that the Blue version continues to use its indexes until it is terminated, while the Green version uses its own modified set of indexes. The developer should follow the index management techniques described [in this article](/help/operations/indexing.md).

### Conservative Coding for Rollbacks {#conservative-coding-for-rollbacks}

If a failure is reported or detected after the deployment, it is possible that a rollback to the Blue version will be required. It would be wise to ensure that the Blue code is compatible with any new structures created by the Green version since the new structures (any mutable content content) will not be rolled back. If the old code is not compatible, fixes will need to be applied in subsequent customer releases.

## Runmodes {#runmodes}

In existing AEM solutions, customers have the option of running instances with arbitrary run modes and apply OSGI configuration or install OSGI bundles to those specific instances. Run modes that are defined typically include the *service* (author and publish) and the environment (dev, stage, prod).

AEM as a Cloud Service on the other hand is more opinionated about which run modes are available and how OSGI bundles and OSGI configuration can be mapped to them:

* OSGI configuration run modes must reference dev, stage, prod for the environment or author, publish for the service. A combination of `<service>.<environment_type>` is being supported whereas these have to be used in this particular order (for example `author.dev` or `publish.prod`). The OSGI tokens should be referenced directly from code rather than using the `getRunModes` method, which will no longer include the `environment_type` at runtime. For more information, see [Configuring OSGi for AEM as a Cloud Service](/help/implementing/deploying/configuring-osgi.md).
* OSGI bundles run modes are limited to the service (author, publish). Per-run mode OSGI bundles should be installed in the content package under either `install/author` or `install/publish`.

Like the existing AEM solutions, there is no way to use run modes to install just content for specific environments or services. If it was desired to seed a dev environment with data or HTML that isn't on stage or production, package manager could be used.

The supported runmode configurations are:

* **config** (*The default, applies to all AEM Services*)
* **config.author** (*Applies to all AEM Author service*)
* **config.author.dev** (*Applies to AEM Dev Author service*)
* **config.author.stage** (*Applies to AEM Staging Author service*)
* **config.author.prod** (*Applies to AEM Production Author service*)
* **config.publish** (*Applies to AEM Publish service*)
* **config.publish.dev** (*Applies to AEM Dev Publish service*)
* **config.publish.stage** (*Applies to AEM Staging Publish service*)
* **config.publish.prod** (*Applies to AEM Production Publish service*) 
* **config.dev** (*Applies to AEM Dev services)
* **config.stage** (*Applies to AEM Staging services)
* **config.prod** (*Applies to AEM Production services)

The OSGI configuration that has the most matching runmodes is used.

When developing locally, a runmode startup parameter can be passed in to dictate which runmode OSGI configuration will be used.

<!-- ### Performance Monitoring {#performance-monitoring}

Developers want to ensure that their custom code is performing well. For Cloud environments, performance reports can be viewed on Cloud Manager. -->

## Maintenance Tasks Configuration in Source Control {#maintenance-tasks-configuration-in-source-control}

Maintenance Task configurations must be persisted in source control since the **Tools > Operations** screen will no longer be available in Cloud environments. This has the benefit of ensuring that changes are intentionally persisted rather than reactively applied and perhaps forgotten. Please reference the [Maintenance Task article](/help/operations/maintenance.md) for additional information.
