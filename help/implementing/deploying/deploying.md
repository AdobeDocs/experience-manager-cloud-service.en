---
title: Deploying to AEM as a Cloud Service
seo-title: Deploying to AEM as a Cloud Service
description: Deploying to AEM as a Cloud Service 
seo-description: Deploying to AEM as a Cloud Service
---

# Deploying to AEM as a Cloud Service {#deploying-to-aem-as-a-cloud-service}

<!-- ## Introduction {#introduction}

The fundamentals of code development are similar in AEM as a Cloud Service compared to the AEM On Premise and Managed Services solutions. Developers write code and test it locally, which is then pushed to remote AEM as a Cloud Service environments. Cloud Manager, which was an optional content delivery tool for Managed Services, is required. This is now the sole mechanism for deploying code to AEM as a Cloud Service environments.

The update of the AEM version is always a separate deployment event from pushing custom code. Viewed in another way, custom code releases should be tested against the AEM version that is on production since that is what it will be deployed on top of. AEM version updates that happen after that, which will be frequent when compared to Managed Services today, are automatically applied. They are intended to be backwards compatible with the customer code already deployed.

The rest of this document will describe how developers should adapt their practices so they work with both AEM as a Cloud Service's Version updates and customer updates. For customers with existing code bases, note that it's a pre-requisite to go through the repository restructuring exercise described in [AEM documentation](https://docs.adobe.com/content/help/en/collaborative-doc-instructions/collaboration-guide/markdown/syntax-style-guide.html).


## AEM version updates {#version-updates}

It is key to understand that AEM will be updated frequently, potentially as often as once a day, and will focus on bug fixes and performance enhancements. The update will happen transparently and without causing downtime. The update is intended to be backwards compatible meaning customers should not need to modify custom code. In fact, AEM updates are independent events from customer code deployments. The AEM update is deployed on top of the last successful customer code push, which implies that any changes committed since the last push to production will not be deployed.

On a regular frequency, a feature release will take place, focusing on feature additions and enhancements that will more substantially impact the user experience compared to the daily releases. A feature release is triggered not by the deployment of a large change set, but rather by the flip of a release toggle, activating code that had been accumulating (and rigorously tested) over the course of days or weeks through the daily updates.

Customers are encouraged to implement Apache Felix health checks to ensure that the application is ready before AEM starts accepting traffic. Health checks should return within 100ms and code should follow the guidelines in the [Felix health checks documentation](https://svn.apache.org/repos/asf/felix/trunk/healthcheck/README.md).

### Composite Node Store {#composite-node-store}

As mentioned above, updates in most cases will incur zero downtime, including for the author, which is a cluster of nodes. Rolling updates are possible due to the "composite node store" feature in Oak, which allows AEM to reference multiple repositories simultaneously. In a Blue-Green deployment, the new Green AEM version contains its own `/libs` (the TarMK based immutable repository), distinct from the older Blue AEM version, although both reference a shared DocumentMK based mutable repository that contains areas like `/content`, `/conf`, `/etc` and others. Because both the Blue and the Green have their own versions of `/libs`, they can both be active during the rolling update, both taking on traffic until the blue is fully replaced by the green.

## Customer Releases {#customer-releases}

### Coding against the right AEM version {#coding-against-the-right-aem-version}

For previous AEM solutions, the most current AEM version changed infrequently (roughly annually with quarterly service packs) and customers would update the production instances to the latest quickstart on their own time, referencing the Uberjar. However, AEM as a Cloud Service applications are auto-updated to the latest version of AEM more often (potentially daily maintenance releases and monthly feature releases), so custom code for internal releases should be built against those newer AEM interfaces.

Like for existing non-cloud AEM versions, a local, offline development based on a specific quickstart will be supported and is expected to be the tool of choice for debugging in the majority of cases.

> [!NOTE}
>There are subtle operational differences between how the application behaves on a local machine versus the Adobe Cloud. These architectural differences must be respected during local development and could lead to a different behavior when deploying on the cloud infrastructure.  Because of these differences it is important to perform the exhaustive tests on dev and stage environments before rolling out new custom code in production.

Below is the process for a developer to access the relevant version of the AEM artifacts (quickstart, uberjar, and javadocs), which we'll refer to as the SDK. needed for developing custom code for an internal release. The process will evolve between the current pilot phase and general availability. Information about the dispatcher can be found in its own dedicated section.

## Prerelease Phase (#prerelease-phase)

* Versions of the quickstart are placed on the prerelease site where they can be downloaded. You can check the AEM admin console's "About Adobe Experience Manager" icon to find out the version of AEM they're running on production.
* The maven poms should reference the following package, which is a placed in a discrete location until GA. This dependency should also be referenced in any subpackage poms. -->

<!-- Skyline UberJAR Dependency to be added to the project's Reactor pom.xml -->


<!-- ```

<dependency>
  <groupId>com.adobe.aem</groupId>
  <artifactId>uber-jar</artifactId> 
  <version>V16168</version> (enclosed comment: use the latest!)
  <scope>provided</scope>
  <classifier>future</classifier>
</dependency>

```

* The remote coordinate for the maven repository where the package is hosted should be included in the pom.

```

<repository>
    <id>adobe-future-releases</id>
    <name>Adobe Future Repository</name>
    <url>https://repo.adobe.com/nexus/content/repositories/ujscm/</url>
    <releases>
        <enabled>true</enabled>
        <updatePolicy>never</updatePolicy>
    </releases>
    <snapshots>
        <enabled>false</enabled>
    </snapshots>
</repository>

``` -->

## Deploying Content Packages via Cloud Manager and Package Manager {#deploying-content-packages-via-cloud-manager-and-package-manager}

### Deployments via Cloud Manager {#deployments-via-cloud-manager}

Customers deploy custom code to cloud environments through Cloud Manager. It should be noted that Cloud Manager transforms locally assembled content packages into an artifact conforming to the Sling Feature Model, which is how an AEM as a Cloud Service application is described when running in a cloud environment. Detailed documentation about the converter can be [found here](https://github.com/apache/sling-org-apache-sling-feature-cpconverter).

Content packages written for AEM as a Cloud Service applications must have a clean separation between immutable and mutable content and Cloud Manager will enforce it by failing the build, outputting a message like:

`Generated content-package <PACKAGE_ID> located in file <PATH> is of MIXED type`

The rest of this section will describe the composition and implications of immutable and mutable packages.

### Immutable Content Packages {#immutabe-content-packages}

All content and code persisted in the immutable repository must be checked into git and deployed through Cloud Manager. In other words, unlike current AEM solutions, code is never deployed directly to a running AEM instance. This ensures that the code running for a given release in any Cloud environment is identical, which eliminates the risk of unintentional code variation on production.

As application changes due to the Blue-Green deployment pattern are enabled by a switch, they cannot depend on changes in the mutable repository with the exception of service users, their ACLs, nodetypes and index definition changes.

For customers with existing code bases, it is critical to go through the repository restructuring exercise described in AEM documentation to ensure that content formerly under the /etc is moved to the right location.

### Mutable Content Packages {#mutable-content-packages}

In some cases it might be useful to prepare content changes in source control so it can be deployed by Cloud Manager whenever an environment was updated. For example, it might be reasonable to seed certain root folder structures or line up changes in editable templates to enable policies in those for components that were updated by the application deployment.

>[!NOTE] Content packages are deployed to all environment types (dev, stage, prod). It is not possible to limit deployment to a specific environment.  

Also, there is no mechanism to rollback the mutable content package changes after they've been applied. If customers detect a problem, they can choose to fix it in their next code release or as a last resort, restore the entire system to a point in time before the deployment.

Any included 3rd party packages must be validated as being AEM as a Cloud Service Service compatible, otherwise its inclusion will result in a deployment failure.

As mentioned above, customers with existing code bases should conform to the repository restructuring exercise described in [AEM documentation](https://helpx.adobe.com/experience-manager/6-5/sites/deploying/using/repository-restructuring.html).

### Package Manager "one offs" for Mutable Content Packages {#package-manager-oneoffs-for-mutable-content-packages}

There are use cases where a content package should be installed as a "one off". For example importing specific content from production on to staging in order to debug a production issue. For these scenarios, Package Manager can be used in AEM as a Cloud Service environments.

Since Package Manager is a runtime concept, it is not possible to install content or code into the immutable repository, so these content packages should only consist of mutable content (mainly `/content` or `/conf`). If the content package includes content that is mixed (both mutable and immutable content), only the mutable content will be installed.

Any content-packages installed via Cloud Manager (both mutable and immutable) will appear in a frozen state in AEM Package Manager's user interface. These packages cannot be reinstalled, rebuilt or even downloaded, and will listed with a **"cp2fm"** suffix, indicating their installation was managed by Cloud Manager.

### Including Third Party Packages {#including-third-party}

It is common for customers to include pre-built packages from third party sources such as software vendors like Adobe's translation partners. The recommendation is to host these packages in a remote repository and reference them in the `pom.xml`. This is only possible for public repositories.

If storing the package in a remote repository is not possible, customers can download the packages directly to their local maven repository and reference them as dependencies in the project `pom.xml`.

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
* If there are any new or updated index definitions, the corresponding indexes are processed.
* Green is starting up while Blue is still serving
* Blue is running and serving while Green is being checked for readiness via health checks
* Green nodes that are ready accept traffic and replace Blue nodes, which are brought down
* Over time, Blue nodes are replaced by Green nodes until only Green remain, thus completing the deployment
* Jobs for mutable content changes may be triggered

## Indexes {#indexes}

For more information on how Search and Indexing works, [see this article](/help/operations/indexing.md).

## Backwards Compatible Code for Rolling Deployments {#backwards-compatible-code-for-rolling-deployments}

As detailed above, AEM as a Cloud Service's rolling deployment strategy implies that both the old and new versions may be operating at the same time. Therefore, be cautious of code changes that are not backwards compatible with the old AEM version that is still operation.

### Service Users and ACL Changes {#service-users-and-acl-changes}

For example, changing service users or ACLs needed to access content or code could lead to errors in the older AEM versions resulting in access to that content or code with outdated service users. To address this behavior, a recommendation is to make changes spread across at least 2 releases, with the first release acting as a bridge before cleaning up in the subsequent release.

### Conservative Coding for Rollbacks {#conservative-coding-for-rollbacks}

If a failure is reported or detected after the deployment, it is possible that a rollback to the Blue version will be required. It would be wise to ensure that the Blue code is compatible with any new structures created by the Green version.

## Runmodes {#runmodes}

In existing AEM solutions, customers have the option of running instances with arbitrary run modes and apply OSGI configuration or install OSGI bundles to those specific instances. Run modes that are defined typically include the *service* (author and publish) and the environment (dev, stage, prod).

AEM as a Cloud Service on the other hand is more opinionated about which run modes are available and how OSGI bundles and OSGI configuration can be mapped to them:

* OSGI configuration run modes must reference dev, stage, prod for the environment or author, publish for the service. A combination of `<service>.<environment_type>` is being supported whereas these have to be used in this particular order (for example author.dev or publish.prod). The OSGI tokens should be referenced directly from code rather than using the `getRunModes` method, which will no longer include the `environment_type` at runtime.
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

The OSGI configuration that has the most matching runmodes is used.

When developing locally, a runmode startup parameter can be passed in to dictate which runmode OSGI configuration will be used.

<!-- ### Performance Monitoring {#performance-monitoring}

Developers want to ensure that their custom code is performing well. For Cloud environments, performance reports can be viewed on Cloud Manager. -->

## Maintenance Tasks Configuration in Source Control {#maintenance-tasks-configuration-in-source-control}

Maintenance Task configurations must be persisted in source control since the **Tools > Operations** screen will no longer be available in Cloud environments. This has the benefit of ensuring that changes are intentionally persisted rather than reactively applied and perhaps forgotten. Please reference the [Maintenance Task article](/help/operations/maintenance.md) for additional information.

<!-- ## Apache and Dispatcher Configuration and Testing {#apache-and-dispatcher-configuration-and-testing}

This section describes how to structure the AEM as a Cloud Service Apache and Dispatcher configuration, as well as how to validate it and run it locally before deploying to Cloud environments. It also describes debugging in Cloud environments. For a deep-dive into Dispatcher, see the AEM 6.5 dispatcher documentation.

>[!NOTE]
>Windows users will need Windows 10 Professional or other distribution that supports Docker, which is a pre-requisite for running and debugging Dispatcher on a local computer. The sections below include commands using the Mac or Linux versions of the SDK, but the Windows SDK can be used in a similar way.

## The Dispatcher SDK {#the-dispatcher-sdk}

The Dispatcher SDK provides:

* A vanilla file structure containing the configuration files to include in a maven project for dispatcher;
* Tooling for customers to validate a dispatcher configuration locally;
* A Docker image that brings up the dispatcher locally.

For prerelease, the dispatcher SDK will be distributed via the prerelease website.

## Extracting the SDK {#xtracting-the-sdk}

Download the shell script to a folder on your machine, make it executable and run it. It will extract the Dispatcher SDK files underneath the directory you stored it in.

## File Structure {#file-structure}

The structure of a project's dispatcher subfolder is as described below and should be copied into the maven project's dispatcher folder:

```
./
├── conf.d
│   ├── available_vhosts
│   │   └── default.vhost
│   ├── dispatcher_vhost.conf
│   ├── enabled_vhosts
│   │   ├── README
│   │   └── default.vhost -> ../available_vhosts/default.vhost
│   └── rewrites
│   │   ├── default_rewrite.rules
│   │   └── rewrite.rules
│   └── variables
|       ├── custom.vars
│       └── global.vars
└── conf.dispatcher.d
    ├── available_farms
    │   └── default.farm
    ├── cache
    │   ├── default_invalidate.any
    │   ├── default_rules.any
    │   └── rules.any
    ├── clientheaders
    │   ├── clientheaders.any
    │   └── default_clientheaders.any
    ├── dispatcher.any
    ├── enabled_farms
    │   ├── README
    │   └── default.farm -> ../available_farms/default.farm
    ├── filters
    │   ├── default_filters.any
    │   └── filters.any
    ├── renders
    │   └── default_renders.any
    └── virtualhosts
        ├── default_virtualhosts.any
        └── virtualhosts.any
```

Below is an explanation of the notable files that can be modified:

**Customizable Files**

The following files are customizable and will get transferred to your Cloud instance on deployment:

* `conf.d/available_vhosts/<CUSTOMER_CHOICE>.vhost`

You can have one or more of these files, and they contain `<VirtualHost>` entries to match host names and allow Apache to handle each domain traffic with different rules. Files are created in the `available_vhosts` directory and enabled with a symbolic link in the `enabled_vhosts` directory. From the `.vhost` files, other files like rewrites and variables will be included.

* `conf.d/rewrites/rewrite.rules`

This file is included from inside your `.vhost` files. It has a set of rewrite rules for `mod_rewrite`.

* `conf.d/variables/custom.vars`

This file is included from inside your `.vhost` files. You can put defines for Apache variables in this location.

* `conf.d/variables/global.vars`

This file is included from inside the `dispatcher_vhost.conf` file. You can change your dispatcher and rewrite log level in this file.

* `conf.dispatcher.d/available_farms/<CUSTOMER_CHOICE>.farm`

You can have one or more of these files, and they contain farms to match host names and allow the dispatcher module to handle each farm with different rules. Files are created in the `available_farms` directory and enabled with a symbolic link in the `enabled_farms` directory. From the `.farm` files, other files like filters, cache rules and others will be included.

* `conf.dispatcher.d/cache/rules.any`

This file is included from inside your `.farm` files. It specifies caching preferences.

* `conf.dispatcher.d/clientheaders/clientheaders.any`

This file is included from inside your `.farm` files. It specifies what request headers should be forwarded to the backend.

* `conf.dispatcher.d/filters/filters.any`

This file is included from inside your `.farm` files. It has a set of rules that change what traffic should be filtered out and not make it to the backend.

* `conf.dispatcher.d/virtualhosts/virtualhosts.any`

This file is included from inside your `.farm` files. It has a list of host names or URI paths to be matched by glob matching to determine what backend to use to serve a request.

The above files reference the unmodifiable files listed below. Changes to those files will not be processed by dispatchers in Cloud environments.

**Immutable Configuration Files**

These files are part of the base framework and enforce standards and best practices. They should be considered immutable, because modifying or deleting them locally will have no impact on your deployment, as they will not get transferred to your Cloud instance.

* `conf.d/available_vhosts/default.vhost`

Contains a sample virtual host. For your own virtual host, create a copy of this file, customize it, go to `conf.d/enabled_vhosts` and create a symbolic link to your customized copy.

* `conf.d/dispatcher_vhost.conf`

Part of the base framework, used to illustrate how your virtual hosts and global variables are included.

* `conf.d/rewrites/default_rewrite.rules`

Default rewrite rules suitable for a standard project. If you need customization, modify `rewrite.rules`. In your customization, you can still include the default rules first, if they suit your needs.

* `conf.dispatcher.d/available_farms/default.farm`

Contains a sample dispatcher farm. For your own farm, create a copy of this file, customize it, go to `conf.d/enabled_farms` and create a symbolic link to your customized copy.

* `conf.dispatcher.d/cache/default_invalidate.any`

Part of the base framework, gets generated on startup. You are **required** to include this file in every farm you define, in the `cache/allowedClients` section.

* `conf.dispatcher.d/cache/default_rules.any`

Default cache rules suitable for a standard project. If you need customization, modify `conf.dispatcher.d/cache/rules.any`. In your customization, you can still include the default rules first, if they suit your needs.

* `conf.dispatcher.d/clientheaders/default_clientheaders.any`

Default request headers to forward to backend, suitable for a standard project. If you need customization, modify `clientheaders.any`. In your customization, you can still include the default request headers first, if they suit your needs.

* `conf.dispatcher.d/dispatcher.any`

Part of base framework, used to illustrate how your dispatcher farms are included.

* `conf.dispatcher.d/filters/default_filters.any`

Default filters suitable for a standard project. If you need customization, modify `filters.any`. In your customization, you can still include the default filters first, if they suit your needs.

* `conf.dispatcher.d/renders/default_renders.any`

Part of base framework, this file gets generated on startup. You are **required** to include this file in every farm you define, in the `renders` section.

* `conf.dispatcher.d/virtualhosts/default_virtualhosts.any`

Default host globbing suitable for a standard project. If you need customization, modify `virtualhosts.any`. In your customization, you shouldn't include the default host globbing, as it matches **every** incoming request.

>[!NOTE]The AEM as a Cloud Service maven archetype will generate the same dispatcher configuration file structure.

The sections below describe how to validate the configuration locally so there is confidence that it will pass the associated quality gate in Cloud Manager when deploying an internal release.

## Local Validation of Dispatcher Configuration {#local-validation-of-dispatcher-configuration}

The validation tool is available in the SDK as a Mac OS, Linux, or Windows binary, allowing customers to run the same validation that Cloud Manager will perform while building and deploying a release.

It is invoked as: `validator full [-d folder] [-w whitelist] zip-file`

The tool validates the Apache and dispatcher configuration contained in the zip file. It scans all files with pattern `conf.d/enabled_vhosts/*.vhost` and checks that only whitelisted directives are used. The directives allowed in Apache configuration files can be listed by running the validator's whitelist command:

```

$ validator whitelist
Cloud manager validator 2.0.4
 
Whitelisted directives:
  <Directory>
  ...
  
  ```

The whitelist contains a list of Apache directives expected in the customer configuration. If a directive is not whitelisted, the tool logs an error and returns a non-zero exit code. If no whitelist is given on the command line, the tool uses a default whitelist. Run validator whitelist to print that list.

 It further scans all files with pattern `conf.dispatcher.d/enabled_farms/*.farm` and checks that:

* No filter rule exists that uses allows via `/glob` (see [CVE-2016-0957](https://nvd.nist.gov/vuln/detail/CVE-2016-0957) for more details)
* No admin feature is exposed. For example, access to paths such as `/crx/de or /system/console`. 

When run against your maven artifact or your `dispatcher/src` subdirectory, it will report validation failures:

 ```

$ validator full dispatcher/src
Cloud manager validator 1.0.4
2019/06/19 15:41:37 Apache configuration uses non-whitelisted directives:
  conf.d/enabled_vhosts/aem_publish.vhost:46: LogLevel
2019/06/19 15:41:37 Dispatcher configuration validation failed:
  conf.dispatcher.d/enabled_farms/999_ams_publish_farm.any: filter allows access to CRXDE

```

Note that the validation tool only reports prohibited use of Apache directives that have not been whitelisted. It does not report syntactical or semantical problems with your Apache configuration, as this information is only available to Apache modules in a running environment.

When no more validation failures are reported, your configuration is ready for deployment.

## Testing your Apache and Dispatcher Configuration Locally {#testing-your-apache-and-dispatcher-configuration-locally}

It is also possible to test drive your Apache and Dispatcher configuration locally, which requires Docker to be installed locally and your configuration passed validation as described above.

By using the "`-d`" parameter, the validator outputs a folder with all configuration files needed by the dispatcher.

Then, the `docker_run.sh` script can point to that folder, starting the container with your configuration.

```

$ validator full -d out src/dispatcher
2019/06/19 16:02:55 No issues found
$ docker_run.sh out docker.for.mac.localhost:4503 8080
Running script /docker_entrypoint.d/10-create-docroots.sh
Running script /docker_entrypoint.d/20-wait-for-backend.sh
Waiting until aemhost is available
aemhost resolves to xx.xx.xx.xx
Running script /docker_entrypoint.d/30-allowed-clients.sh
Starting httpd server
...

```

This will start the dispatcher in a container with its backend pointing to an AEM instance running on your local Mac OS machine at port 4503.

## Debugging your Apache and Dispatcher Configuration {#debugging-your-apache-and-dispatcher-configuration}

The following strategy can be used to increase the log output for the dispatcher module and see the result of `RewriteRule` evaluation in both local and cloud environments.

Log levels for those modules are defined by the variables `DISP_LOG_LEVEL` and `REWRITE_LOG_LEVEL`. They can be set in the file `conf.d/variables/global.vars`. Its relevant part follows:

```

# Log level for the dispatcher
#
# Possible values are: Error, Warn, Info, Debug and Trace1
# Default value: Warn
#
# Define DISP_LOG_LEVEL Warn
 
# Log level for mod_rewrite
#
# Possible values are: Error, Warn, Info, Debug and Trace1 - Trace8
# Default value: Warn
#
# To debug your RewriteRules, it is recommended to raise your log
# level to Trace2.
#
# More information can be found at:
# https://httpd.apache.org/docs/current/mod/mod_rewrite.html#logging
#
# Define REWRITE_LOG_LEVEL Warn

```

When running the Dispatcher locally, logs are also directly printed to the terminal output.

## Different Dispatcher Configurations Per Environment {#different-dispatcher-configurations-per-environment}

At this time, the same dispatcher configuration is applied to all AEM as a Cloud Service environments. The runtime will have an environment variable `ENVIRONMENT_TYPE` that contains the current run mode (dev, stage or prod) as well as a define. The define can be `ENVIRONMENT_DEV`, `ENVIRONMENT_STAGE` or `ENVIRONMENT_PROD`. In the Apache configuration othe variable can be used directly in an expression. Alternatively, the define can be used to build logic:

```

# Simple usage of the environment variable
ServerName ${ENVIRONMENT_TYPE}.company.com
 
# When more logic is required
<IfDefine ENVIRONMENT_STAGE>
  # These statements are for stage
  Define VIRTUALHOST stage.example.com
</IfDefine>
<IfDefine ENVIRONMENT_PROD>
  # These statements are for production
  Define VIRTUALHOST prod.example.com
</IfDefine>

```

In the Dispatcher configuration, the same environment variable is available. If more logic is required, define the variables as shown in the example above and then use them in the Dispatcher configuration section:

```

/virtualhosts {
  { "${VIRTUALHOST}" }
}

```

When testing your configuration locally, you can simulate different environment types by passing the variable `DISP_RUN_MODE` to the `docker_run.sh` script directly:

```

$ DISP_RUN_MODE=stage docker_run.sh out docker.for.mac.localhost:4503 8080

```

For a complete list of options and variables available, run the script `docker_run.sh` without arguments.

## Viewing the Dispatcher Configuration In Use by Your Docker Container {#viewing-the-dispatcher-configuration-in-use-by-your-docker-configuration}

With environment specific configurations, it can be difficult to determine what the actual Dispatcher configuration looks like. After having started your docker container with `docker_run.sh` it can be dumped as follows:

* Determine the docker container ID in use:

```

$ docker ps
CONTAINER ID       IMAGE
d75fbd23b29        adobe/aem-ethos/dispatcher-publish:...

```

*  Execute the following command line with that container ID:

```

$ docker exec d75fbd23b29 httpd-test
# Dispatcher configuration: (/etc/httpd/conf.dispatcher.d/dispatcher.any)
/farms {
  /publishfarm {
    /clientheaders {
...

```

## Main Differences Between AMS Dispatcher Configuration strategy and AEM as a Cloud Service {#main-differences-between-ams-dispatcher-configuration-and-aem-as-a-cloud-service}

As described on the reference page above, the Apache and Dispatcher configuration in AEM as a Cloud Service is quite similar to the AMS one. The main difference are:

* In AEM as a Cloud Service, some Apache directives may not be used (for example `Listen` or `LogLevel`)
* In AEM as a Cloud Service, only some pieces of the Dispatcher configuration can be put in include files and their naming is important. For instance, filter rules that you want to reuse across different hosts, must be put in a file called `filters/filters.any`. See the reference page for more information.
* In AEM as a Cloud Service there is extra validation to disallow filter rules written using `/glob` to prevent security issues. Since `deny *` will be used rather than `allow *` (which cannot be used), customers will benefit from running the Dispatcher locally and doing trial and error, looking at the logs to know exactly what paths the Dispatcher filters are blocking in order for those can be added.

--> 
