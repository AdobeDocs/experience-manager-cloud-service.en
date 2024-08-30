---
title: Deploying to AEM as a Cloud Service
description: Learn about the fundamentals and best practices of deploying to AEM as a Cloud Service
feature: Deploying
exl-id: 7fafd417-a53f-4909-8fa4-07bdb421484e
role: Admin
---
# Deploying to AEM as a Cloud Service {#deploying-to-aem-as-a-cloud-service}

## Introduction {#introduction}

The fundamentals of code development are similar in AEM as a Cloud Service compared to the AEM On Premise and Managed Services solutions. Developers write code and test it locally, which is then pushed to remote environments on AEM as a Cloud Service. Cloud Manager, which was an optional content delivery tool for Managed Services, is required. This delivery tool is now the sole mechanism for deploying code to AEM as a Cloud Service dev, stage, and production environments. For quick feature validation and debugging before deploying those previously mentioned environments, code can be synced from a local environment to a [Rapid Development Environment](/help/implementing/developing/introduction/rapid-development-environments.md).

The update of the [AEM version](/help/implementing/deploying/aem-version-updates.md) is always a separate deployment event from pushing [custom code](#customer-releases). Viewed another way, custom code releases should be tested against the AEM version that is on production because that is what it is deployed on the top. AEM version updates that happen after that (which are frequent and are automatically applied), are intended to be backward compatible with the customer code already deployed.

The rest of this document describes how developers should adapt their practices so they work with both AEM as a Cloud Service's Version updates and customer updates. 

<!--
>[!NOTE]
>It is recommended for customers with existing code bases, to go through the repository restructuring exercise described in the [AEM documentation](https://docs.adobe.com/help/en/collaborative-doc-instructions/collaboration-guide/authoring/restructure.html).
-->

## Customer Releases {#customer-releases}

### Coding against the right AEM version {#coding-against-the-right-aem-version}

For previous AEM solutions, the most current AEM version changed infrequently (roughly annually with quarterly service packs) and customers would update the production instances to the latest quickstart on their own time, referencing the API Jar. However, applications on AEM as a Cloud Service are automatically updated to the latest version of AEM more often, so custom code for internal releases should be built against the latest AEM version.

Like for existing non-cloud AEM versions, a local, offline development based on a specific quickstart is supported and is expected to be the tool of choice for debugging usually.

>[!NOTE]
>There are subtle operational differences between how the application behaves on a local machine versus the Adobe Cloud. These architectural differences must be respected during local development and could lead to a different behavior when deploying on the cloud infrastructure. Because of these differences, it is important to perform the exhaustive tests on dev and stage environments before rolling out new custom code in production.

To develop custom code for an internal release, the relevant version of the [AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md) should be downloaded and installed. For additional information about using the AEM as a Cloud Service Dispatcher Tools, see [Dispatcher in the Cloud](/help/implementing/dispatcher/disp-overview.md).

The following video provides a high-level overview on how to deploy code to AEM as a Cloud Service:

>[!VIDEO](https://video.tv.adobe.com/v/30191?quality=9)

<!--
>[!NOTE]
>It is recommended for customers with existing code bases, to go through the repository restructuring exercise described in the [AEM documentation](https://docs.adobe.com/help/en/collaborative-doc-instructions/collaboration-guide/authoring/restructure.html). 
-->

## Deploying Content Packages by way of Cloud Manager and Package Manager {#deploying-content-packages-via-cloud-manager-and-package-manager}

### Deployments by way of Cloud Manager {#deployments-via-cloud-manager}

<!-- Alexandru: temporarily commenting this out, until I get some clarification from Brian 

![image](https://git.corp.adobe.com/storage/user/9001/files/e91b880e-226c-4d5a-93e0-ae5c3d6685c8) -->

Customers deploy custom code to cloud environments through Cloud Manager. Cloud Manager transforms locally assembled content packages into an artifact conforming to the Sling Feature Model, which is how an application on AEM as a Cloud Service is described when running in a cloud environment. As a result, when looking at the packages in [Package Manager](/help/implementing/developing/tools/package-manager.md) on Cloud environments, the name includes "cp2fm" and the transformed packages have all metadata removed. They cannot be interacted with, meaning they cannot be downloaded, replicated, or opened. For detailed documentation about the converter see [
sling-org-apache-sling-feature-cpconverter on GitHub](https://github.com/apache/sling-org-apache-sling-feature-cpconverter).

Content packages written for applications on AEM as a Cloud Service must have a clean separation between immutable and mutable content and Cloud Manager only installs the mutable content, also outputting a message like the following:

`Generated content-package <PACKAGE_ID> located in file <PATH> is of MIXED type`

The rest of this section describes the composition and implications of immutable and mutable packages.

### Immutable Content Packages {#immutabe-content-packages}

All content and code persisted in the immutable repository must be checked into git and deployed through Cloud Manager. In other words, unlike current AEM solutions, code is never deployed directly to a running AEM instance. This workflow ensures that the code running for a given release in any Cloud environment is identical, which eliminates the risk of unintentional code variation on production. As an example, OSGI configuration should be committed to source control rather than managed at runtime by way of the AEM web console's configuration manager.

As application changes due to the deployment pattern are enabled by a switch, they cannot depend on changes in the mutable repository except for service users, their ACLs, nodetypes, and index definition changes.

For customers with existing code bases, it is critical to go through the repository restructuring exercise described in AEM documentation to ensure that content formerly under the /etc is moved to the right location.

Some additional restrictions apply for these code packages, for example, [install hooks](https://jackrabbit.apache.org/filevault/installhooks.html) are not supported.

## OSGI Configuration {#osgi-configuration}

As mentioned above, OSGI configuration should be committed to source control rather than through the web console. Techniques to do so include:

* Making the necessary changes on the developer's local AEM environment with the AEM web console's configuration manager and then exporting the results to the AEM project on the local file system
* Creating the OSGI configuration manually in the AEM project on the local file system, the referencing the AEM console's configuration manager for the property names.

Read more about OSGI configuration at [Configuring OSGi for AEM as a Cloud Service](/help/implementing/deploying/configuring-osgi.md).

## Mutable Content {#mutable-content}

Sometimes, it might be useful to prepare content changes in source control so it can be deployed by Cloud Manager whenever an environment was updated. For example, it might be reasonable to seed certain root folder structures. Or, line up changes in editable templates to enable policies components that were updated by the application deployment.

There are two strategies to describe the content that is deployed by Cloud Manager to the mutable repository, mutable content packages and `repoinit` statements.

### Mutable Content Packages {#mutable-content-packages}

Content such as folder path hierarchies, service users, and access controls (ACLs) are typically committed into a maven archetype-based AEM project. Techniques include exporting from AEM or writing directly as XML. During the build and deployment process, Cloud Manager packages the resulting mutable content package. The mutable content is installed at three different times during the deploy phase in the pipeline: 

Ahead of startup of new version of application:

* index definitions (add, modify, remove)

During startup of new version of application but ahead of switchover:

* Service Users (add)
* Service User ACLs (add)
* node types (add)

After switchover to new version of application:

* All other content definable by way of Jackrabbit vault. For example:
  * Folders (add, modify, remove)
  * Editable templates (add, modify, remove)
  * Context Aware configuration (anything under `/conf`) (add, modify, remove)
  * Scripts (packages can trigger Install hooks at various stages of the install process of package installation. See [Jackrabbit filevault documentation](https://jackrabbit.apache.org/filevault/installhooks.html) about install hooks. AEM CS currently uses Filevault version 3.4.0, which limits install hooks to admin users, system users, and member of the administrators group)).

It is possible to limit mutable content installation to author or publish by embedding packages in an install.author or install.publish folder under `/apps`. Restructuring to reflect this separation was done in AEM 6.5 and details around recommended project restructuring can be found in the [AEM 6.5 documentation.](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/restructuring/repository-restructuring.html)

>[!NOTE]
>Content packages are deployed to all environment types (dev, stage, prod). It is not possible to limit deployment to a specific environment. This limitation is in place to ensure the option of a test run of automated execution. Content that is specific to an environment requires manual installation by way of [Package Manager](/help/implementing/developing/tools/package-manager.md).

Also, there is no mechanism to roll back the mutable content package changes after they've been applied. If customers detect a problem, they can choose to fix it in their next code release or as a last resort, restore the entire system to a point in time before the deployment.

Any included third-party packages must be validated as being AEM as a Cloud Service compatible, otherwise its inclusion results in a deployment failure.

As mentioned above, customers with existing code bases should conform to the repository restructuring exercise needed by the 6.5 repository changes described in the [AEM 6.5 documentation.](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/restructuring/repository-restructuring.html)

## Repoinit {#repoinit}

For the following cases, it is preferable to take the approach of hand coding explicit content creation `repoinit` statements in OSGI factory configurations:

* Create/delete/disable service users
* Create/delete groups
* Create/delete users
* Add ACLs

  >[!NOTE]
  >
  >Definition of ACLs requires the node structures to be already present. Thus, preceding create path statements might be necessary.

* Add path (for example, for root folder structures)
* Add CNDs (nodetype definitions)

Repoinit is preferable for these supported content modification use cases due to the following benefits:

* `Repoinit` creates resources at startup so logic can take the existence of those resources for granted. In the mutable content package approach, resources are created after startup, so application code relying on them may fail.
* `Repoinit` is a relatively safe instruction set as you explicitly control the action to be taken. Also, the only supported operations are additive except for a few security-related cases which allow removal of Users, Service Users, and Groups. In contrast, a removal of something in the mutable content package approach is explicit; as you define a filter, anything present covered by a filter is deleted. Still, caution should be taken since with any content there are scenarios where the presence of new content can alter the behavior of the application.
* `Repoinit` performs fast and atomic operations. Mutable content packages in contrast can highly depend performance wise on the structures covered by a filter. Even if you update a single node, a snapshot of a large tree might be created.
* It is possible to validate `repoinit` statements on a local dev environment at runtime because they are run when the OSGi configuration gets registered.
* `Repoinit` statements are atomic and explicit and are skipped if the state is already matching.

When Cloud Manager deploys the application, it executes these statements, independently from the installation of any content packages.

To create `repoinit` statements, follow the below procedure:

1. Add OSGi configuration for factory PID `org.apache.sling.jcr.repoinit.RepositoryInitializer` in a configuration folder of the project. Use a descriptive name for the configuration like **org.apache.sling.jcr.repoinit.RepositoryInitializer~initstructure**.
1. Add `repoinit` statements to the script property of the config. The syntax and options are documented in [Sling documentation](https://sling.apache.org/documentation/bundles/repository-initialization.html). There should be explicit creation of a parent folder before their child folders. For example, an explicit creation of `/content` before `/content/myfolder`, before `/content/myfolder/mysubfolder`. For ACLs being set on low-level structures, it is recommended to set them on a higher level and work with a `rep:glob` restriction. For example, `(allow jcr:read on /apps restriction(rep:glob,/msm/wcm/rolloutconfigs))`.
1. Validate on the local dev environment at runtime.

<!-- last statement in step 2 to be clarified with Brian -->

>[!WARNING]
>
>For ACLs defined for nodes underneath `/apps` or `/libs` the `repoinit`, execution starts on a blank repository. The packages are installed after `repoinit` so statements cannot rely on anything defined in the packages but must define the preconditions like the parent structures underneath.

>[!TIP]
>
>For ACLs, the creation of deep structures might be cumbersome. Therefore, it is more reasonable to define an ACL on a higher level and constrain where it is supposed to act by way of a `rep:glob` restriction.

More detail about `repoinit` can be found in the [Sling documentation](https://sling.apache.org/documentation/bundles/repository-initialization.html)

<!-- ### Packaging of Immutable and Mutable Packages {#packaging-of-immutable-and-mutable-packages}

above appears to be internal, to confirm with Brian -->

### Package Manager "one offs" for Mutable Content Packages {#package-manager-oneoffs-for-mutable-content-packages}

>[!CONTEXTUALHELP]
>id="aemcloud_packagemanager"
>title="Package Manager - Migrating Mutable Content Packages"
>abstract="Explore usage of Package Manager for use cases where a content package should be installed as 'one off'. The installation includes importing specific content from production on to staging to debug a production issue, transferring small content package from on-premise environment to AEM Cloud environments, and more."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html" text="Content Transfer Tool"

There are use cases where a content package should be installed as a "one off". For example, importing specific content from production on to staging to debug a production issue. For these scenarios, [Package Manager](/help/implementing/developing/tools/package-manager.md) can be used in environments on AEM as a Cloud Service.

Since Package Manager is a runtime concept, it is not possible to install content or code into the immutable repository, so these content packages should only consist of mutable content (mainly `/content` or `/conf`). If the content package includes content that is mixed (both mutable and immutable content), only the mutable content is installed.

>[!IMPORTANT]
>
>The Package Manager user interface might return an **undefined** error message if a package takes longer than ten minutes to install.
>
>This time is not due to an error with the installation, but to a timeout that Cloud Service has for all requests.
>
>Do not retry the installation if you see such an error. The installation is proceeding correctly in the background. If you do restart the installation, some conflicts could be introduced by multiple concurrent import processes.

Any content-packages installed by way of Cloud Manager (both mutable and immutable) appear in a frozen state in AEM Package Manager's user interface. These packages cannot be reinstalled, rebuilt, or even downloaded, and are listed with a **"cp2fm"** suffix, indicating their installation was managed by Cloud Manager.

### Including Third-Party Packages {#including-third-party}

It is common for customers to include pre-built packages from third-party sources such as software vendors like Adobe's translation partners. The recommendation is to host these packages in a remote repository and reference them in the `pom.xml`. This method is possible for public repositories and also for private repositories with password protection, as described in [password protected maven repositories](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/setting-up-project.md#password-protected-maven-repositories).

If storing the package in a remote repository is not possible, customers can place in a local, file system-based Maven repository, which is committed to SCM as part of the project. It is referenced by whatever depends on it. The repository is declared in the project pom as illustrated below:


```
<repository>
    <id>project.local</id>
    <name>project</name>
    <url>file:${maven.multiModuleProjectDirectory}/repository</url>
</repository>
```

<!-- formatting appears broken in the code sample above, check how it appears on AEM -->

Any included third-party packages must adhere to AEM as a Cloud Service coding and packaging guidelines described in this article, otherwise its inclusion results in a deployment failure.

The following Maven `POM.xml` snippet shows how third-party packages can be embedded in the project's "Container" package, typically named **'all'**, by way of the **filevault-package-maven-plugin** Maven plugin configuration.

```
...
<plugin>
  <groupId>org.apache.jackrabbit</groupId>
  <artifactId>filevault-package-maven-plugin</artifactId>
  <extensions>true</extensions>
  <configuration>
      ...
      <embeddeds>

          ...

          <!-- Include any other extra packages  -->
          <embedded>
              <groupId>com.vendor.x</groupId>
              <artifactId>vendor.plug-in.all</artifactId>
              <type>zip</type>
              <target>/apps/vendor-packages/container/install</target>
          </embedded>
      <embeddeds>
  </configuration>
</plugin>
...
```

## How Rolling Deployments Work {#how-rolling-deployments-work}

Like AEM updates, customer releases are deployed using a rolling deployment strategy to eliminate author cluster downtime under the right circumstances. The general sequence of events is described below, where nodes with both the old and new versions of customer code are running the same version of AEM code.

* Nodes with the old version are active and a release candidate for the new version is built and becomes available.
* If there are any new or updated index definitions, the corresponding indexes are processed. Nodes with the old version always use the old indexes, while nodes with the new version always use the new indexes.
* Nodes with the new version start-up, while old versions still serve traffic.
* Nodes with the old version are running and keep serving while nodes with the new version are checked for readiness by way of health checks.
* Nodes with the new version that are ready, accept traffic, and replace the nodes with the old version, which are brought down.
* Over time, the nodes with the old version are replaced by nodes with the new version until only nodes with new versions remain, thus completing the deployment.
* Any new or modified mutable content is then deployed.

## Indexes {#indexes}

New or modified indexes cause an extra indexing or reindexing step before the new version can take on traffic. Details about index management in AEM as a Cloud Service can be found under [Content Search and Indexing](/help/operations/indexing.md). You can check the indexing status of build pages on Cloud Manager, and receive a notification when the new version is ready to take traffic.

>[!NOTE]
>
>The time needed for a rolling deployment varies depending on the size of the index. The reason is because the new version cannot accept traffic until the new index is generated.

Currently, AEM as a Cloud Service does not work with index management tools such as ACS Commons Ensure Oak Index tool.

## Replication {#replication}

The publication mechanism is backwards compatible with the [AEM Replication Java&trade; APIs](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/previous-updates/aem-previous-versions.html).

To develop and test with replication with the cloud ready AEM quickstart, the classic replication capabilities must be used with an Author/Publish setup. If the user interface entry point on AEM Author is removed for the cloud, users go to `http://localhost:4502/etc/replication` for configuration.

## Backwards Compatible Code for Rolling Deployments {#backwards-compatible-code-for-rolling-deployments}

As detailed above, AEM as a Cloud Service's rolling deployment strategy implies that both the old and new versions may be operating at the same time. Therefore, be cautious of code changes that are not backwards compatible with the old AEM version that is still operation.

In addition, the old release should be tested for compatibility with any new mutable content structures applied by the new release if there is a rollback, because mutable content is not removed.

### Service Users and ACL Changes {#service-users-and-acl-changes}

Changing service users, or ACLs that access content or code, could lead to errors in the older AEM versions resulting in access to that content or code with outdated service users. To address this behavior, the recommendation is to make changes spread across at least two releases, with the first release acting as a link before cleaning up in the subsequent release.

### Index Changes {#index-changes}

If changes to indexes are made, it is important that the new version continues to use its indexes until it is terminated, while the old version uses its own modified set of indexes. The developer should follow the index management techniques described under [Content Search and Indexing](/help/operations/indexing.md).

### Conservative Coding for Rollbacks {#conservative-coding-for-rollbacks}

If a failure is reported or detected after the deployment, it is possible that a rollback to the old version is required. Ensure that the new code is compatible with any new structures created by that new version since the new structures (any mutable content) are not rolled back. If the old code is not compatible, fixes must be applied in subsequent customer releases.

## Rapid Development Environments (RDE) {#rde}

[Rapid Development Environments](/help/implementing/developing/introduction/rapid-development-environments.md) (or RDEs for short) allow developers to quickly deploy and review changes, minimizing the amount of time necessary to test features that are already proven to work on a local development environment.

Unlike regular dev environments, which deploy code by way of Cloud Manager pipeline, developers use command-line tools to sync code from a local development environment to the RDE. After the changes are successfully tested in an RDE, deploy them to a regular Cloud Development environment through the Cloud Manager pipeline, which puts the code through the appropriate quality gates. 

## Run Modes {#runmodes}

In existing AEM solutions, customers have the option of running instances with arbitrary run modes and apply OSGI configuration or install OSGI bundles to those specific instances. Run modes that are defined typically include the *service* (author and publish) and the environment (rde, dev, stage, prod).

AEM as a Cloud Service on the other hand is more opinionated about which run modes are available and how OSGI bundles and OSGI configuration can be mapped to them:

* OSGI configuration run modes must reference RDE, development, stage, production for the environment or author, publish for the service. A combination of `<service>.<environment_type>` is being supported, whereas these environments have to be used in this particular order (for example, `author.dev` or `publish.prod`). The OSGI tokens should be referenced directly from code rather than using the `getRunModes` method, which no longer includes the `environment_type` at runtime. For more information, see [Configuring OSGi for AEM as a Cloud Service](/help/implementing/deploying/configuring-osgi.md).
* OSGI bundles run modes are limited to the service (author, publish). Per-run mode OSGI bundles should be installed in the content package under either `install.author` or `install.publish`.

AEM as a Cloud Service does not allow using run modes to install content for specific environments or services. If a development environment must be seeded with data or HTML that is not in the staging or production environments, Package Manager can be used.

The supported run mode configurations are:

* **config** (*The default, applies to all AEM services*)
* **config.author** (*Applies to all AEM Author service*)
* **config.author.dev** (*Applies to AEM Dev Author service*)
* **config.author.rde** (*Applies to AEM RDE Author service*)
* **config.author.stage** (*Applies to AEM Staging Author service*)
* **config.author.prod** (*Applies to AEM Production Author service*)
* **config.publish** (*Applies to AEM Publish service*)
* **config.publish.dev** (*Applies to AEM Dev Publish service*)
* **config.publish.rde** (*Applies to AEM RDE Publish service*)
* **config.publish.stage** (*Applies to AEM Staging Publish service*)
* **config.publish.prod** (*Applies to AEM Production Publish service*) 
* **config.dev** (*Applies to AEM Dev services*)
* **config.rde** (*Applies to RDE services*)
* **config.stage** (*Applies to AEM Staging services*)
* **config.prod** (*Applies to AEM Production services*)

The OSGI configuration that has the most matching run modes is used.

When developing locally, a run mode startup parameter, `-r`, is used to specify the run mode OSGI configuration.

```shell
$ java -jar aem-sdk-quickstart-xxxx.x.xxx.xxxx-xxxx.jar -r publish,dev
```

<!-- ### Performance Monitoring {#performance-monitoring}

Developers want to ensure that their custom code is performing well. For Cloud environments, performance reports can be viewed on Cloud Manager. -->

## Maintenance Tasks Configuration in Source Control {#maintenance-tasks-configuration-in-source-control}

Maintenance Task configurations must be persisted in source control because the **Tools > Operations** screen is not available in Cloud environments. This benefit ensures that changes are intentionally persisted rather than reactively applied and forgotten. See [Maintenance Tasks in AEM as a Cloud Service](/help/operations/maintenance.md) for additional information.
