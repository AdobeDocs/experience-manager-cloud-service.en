---
title: Add a Production Pipeline
description: Learn how to add a production pipeline to build and deploy your code to production environments.
index: true
exl-id: 67edca16-159e-469f-815e-d55cf9063aa4
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
---

# Add a production pipeline {#configure-production-pipeline}

Learn how to configure production pipelines to build and deploy your code to production environments. A production pipeline deploys code first to the stage environment. On approval, it deploys the same code to the production environment.

A user must have the **[Deployment Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions)** role to configure production pipelines.

>[!NOTE]
>
>A production pipeline cannot be set up until the following has happened: 
>
>* The program is created.
>* The Git repository has at least one branch.
>* The production and staging environments are created.

Before you start to deploy your code, configure your pipeline settings from the [!UICONTROL Cloud Manager].

>[!NOTE]
>
>You can [edit pipeline settings](managing-pipelines.md) after the initial setup.

## Add a new production pipeline {#adding-production-pipeline}

After you have set up your program and have at least one environment using the [!UICONTROL Cloud Manager] UI, you are ready to add a production pipeline by following these steps.

>[!TIP]
>
>Before you configure a front-end pipeline, see the [AEM Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) for an end-to-end guide through the easy-to-use AEM Quick Site Creation tool. This journey can help you streamline the front-end development of your AEM Site, letting you customize your site quickly with no AEM back-end knowledge.

1. Sign into Cloud Manager at [experience.adobe.com](https://experience.adobe.com).
1. In the **Quick access** section, click **Experience Manager**.
1. In the left side panel, click **Cloud Manager**.
1. Select an organization that you want.
1. On the **My Programs** console, click a program. 

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. Navigate to the **Pipelines** card from the **Program Overview** page and click **Add** to select **Add Production Pipeline**. 

   ![The Pipelines card on the Program Manager overview](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-1.png)

1. The **Add Production Pipeline** dialog box displays. Provide a **Pipeline Name** to identify your pipeline along with the following options. Click **Continue**.

   **Deployment Trigger** - You have the following options when defining the deployment triggers to start the pipeline.
      
      * **Manual** - Start the pipeline manually.
      * **On Git Changes** - Starts the CI/CD pipeline whenever commits are added to the configured Git branch. With this option, you can still start the pipeline manually as required.  

    **Important Metric Failures Behavior** - During pipeline setup or edit, the **Deployment Manager** has the option of defining the behavior of the pipeline when an important failure is encountered in any of the quality gates. The available options are:

    * **Ask every time** - Default setting. It requires manual intervention in any important failure.
    * **Fail Immediately** - If selected, the pipeline is canceled whenever an important failure occurs. This process is essentially emulating a user manually rejecting each failure.
    * **Continue Immediately** - If selected, the pipeline proceeds automatically whenever an important failure occurs. This process is essentially emulating a user manually approving each failure.

    ![Production pipeline configuration](/help/implementing/cloud-manager/assets/configure-pipeline/production-pipeline-configuration.png)

1. On the **Source Code** tab, select which type of code the pipeline should process.

   * **[I am using Full Stack Code](#full-stack-code)**
   * **[Configure a targeted deployment pipeline](#targeted-deployment)**

See [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) for more information about the types of pipelines.

The steps to complete the creation of your production pipeline vary depending on the type of source code you selected. Follow the links above to jump to the next section of this document so you can complete the configuration of your pipeline.

### I am using a Full Stack Code {#full-stack-code}

A full-stack code pipeline simultaneously deploys back-end and front-end code builds containing one or more AEM server applications along with HTTPD/Dispatcher configuration.

>[!NOTE]
>
>If a full-stack code pipeline already exists for the selected environment, this selection is disabled.

**To configure a full stack code pipeline:**

1. On the **Source Code** tab, define the following options.

   * **Repository** - Defines from which Git repository that the pipeline should retrieve the code.

   >[!TIP]
   > 
   >See [Add and Manage Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md) to learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - From the drop-down list, choose which branch in the selected repository the pipeline should build from. The default is `main`. The pipeline uses the chosen branch as the source for build and deployment. If necessary, click **Refresh** to update the list of available branches for the selected repository. Use this option if a recently created branch does not appear in the list.
   * **Build Strategy**
        * **Full Build** - Builds all modules in the repository every time
        * BETA **Smart Build** - Builds only modules that have changed since the last commit.<br>Learn more about [using Smart Build in a non-production pipeline](#about-smart-build-non-production-pipeline).
  
          >[!IMPORTANT]
          >
          >Smart Build is available only for Code Quality pipelines and Dev Full Stack Code deployment pipelines.
   * **Ignore Web Tier Configuration** - When checked, the pipeline does not deploy your web tier configuration.
   * **Pause before deploying to Production** - Pauses the pipeline before deploying to production.
   * **Scheduled** - Lets the user enable the scheduled production deployment.

   ![Full stack code](/help/implementing/cloud-manager/assets/configure-pipeline/production-pipeline-fullstack.png)

1. Click **Continue** to advance to the **Experience Audit** tab where you can define the paths that should always be included in the Experience Audit.

   ![Add Experience Audit](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-audit.png)
  
1. Provide paths to be included in the Experience Audit.

   * See [Experience Audit Testing](/help/implementing/cloud-manager/reports/report-experience-audit.md#configuration) for details.

1. Click **Save** to save your pipeline.

When the pipeline runs, paths configured for the Experience Audit are submitted and evaluated based on performance, accessibility, SEO, best practices, and PWA tests. For more details, see [Understanding Experience Audit Results](/help/implementing/cloud-manager/reports/report-experience-audit.md).

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

### I am using Targeted deployment {#targeted-deployment}

A targeted deployment deploys code only for selected parts of your AEM application. In such a deployment, you can choose to **Include** one of the following types of code:

* **Config** - Configure settings for various features in your AEM environment.
  * See [Using Config Pipelines](/help/operations/config-pipeline.md) for a list of supported configurations, which include log forwarding, purge-related maintenance tasks, and various CDN configurations, and to manage them in your repository so they are deployed properly.
  * When running a targeted deployment pipeline, configurations are deployed, provided they are saved to the environment, repository, and branch defined in the pipeline.
  * At any time, there can only be one config pipeline per environment.
* **Configure Edge Delivery Services config pipeline** - Edge Delivery Configuration Pipelines do not have separate development, staging, and production environments. In AEM as a Cloud Service, changes move through development, stage, and production tiers. In contrast, an Edge Delivery Configuration Pipeline applies its configuration directly to all Edge Delivery Sites domains registered in Cloud Manager. To learn more, see [Add an Edge Delivery Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-edge-delivery-pipeline.md). 
* **Front End Code** - Configure JavaScript and CSS for the front end of your AEM application.
  * With front-end pipelines, more independence is given to front-end developers and the development process can be accelerated.
  * See the document [Developing Sites with the Front-End Pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md) for how this process works along with some considerations to be aware of to get the full potential out of this process.
* **Web Tier Config** - Configure Dispatcher properties to store, process, and delivery web pages to the client.
  * See the document [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines) for more details.
  * If a web-tier code pipeline exists for the selected environment, this selection is disabled.
  * If you create a web tier config pipeline for an environment with an existing full-stack pipeline, the web tier configuration in the full-stack pipeline is ignored. This change affects only the web tier configuration in that environment.

>[!NOTE]
>
>Web tier and config pipelines are not supported with private repositories. See [Adding Private Repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/private-repositories.md) for details and the full list of limitations.

**To configure a targeted deployment pipeline:**

1. Choose which deployment type you require.

![Targeted deployment options](/help/implementing/cloud-manager/assets/configure-pipeline/prod-pipeline-targeted-deployment.png)

1. Define the **Eligible Deployment Environments**.

   * If your pipeline is a deployment pipeline, you must select to which environments it should deploy.

1. Under **Source Code**, define the following options:

   * **Repository** - This option defines from which git repo that the pipeline should retrieve the code.

   >[!TIP]
   > 
   >See [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md) so you can learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - This option defines from which branch in the selected pipeline should retrieve the code.
     * Enter the first few characters of the branch name and the auto-complete feature of this field. It finds the matching branches that you can select.
   * **Code Location** - This option defines the path in the branch of the selected repo from which the pipeline should retrieve the code.
   * **Pause before deploying to Production** - This option pauses the pipeline before deploying to production.
   * **Scheduled** - Lets the user enable the scheduled production deployment. Only available for web tier targeted deployments.
   
   ![Config pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/prod-pipeline-config-deployment.png)

1. Click **Save**.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

## BETA: About using Smart Build in a production pipeline{#about-smart-build-production-pipeline}

**Smart Build** in Cloud Manager is an optimized build strategy for production pipelines. Smart Build reduces build times by caching modules and rebuilding only those modules that have changed since the last successful run. Unchanged modules are reused from cache, while only modified modules and their dependencies are rebuilt, improving efficiency for iterative development workflows.

>[!NOTE]
>
>Interested in this beta? Email [beta_quickbuild_cmpipelines@adobe.com](mailto:beta_quickbuild_cmpipelines@adobe.com) with your Adobe OrgID and Program ID.

>[!IMPORTANT]
>
>The first run after enabling Smart Build behaves like a Full Build because the cache is empty.

Smart Build is recommended when you have the following:

* You are actively developing and committing frequent incremental changes.
* Your project contains multiple Maven modules.
* Full builds are taking significant time.

Smart Build is not always ideal when you have the following:

* Your build relies heavily on plugins that perform operations outside Maven's dependency graph.
* You require full rebuild validation on every execution.

### Understand build performance{#smart-build-performance}

The performance gain from using Smart Build depends on several factors including the following:

* The number of modules in the project.
* The frequency and scope of code changes.
* The distribution of dependencies across modules.

Generally, projects with many independent modules can see the greatest improvement.

### Per-module cache opt-out{#smart-build-cache-optout}

Smart Build provides fine-grained control that lets you disable caching for specific modules. This ability is useful when certain modules:

* Use plug-ins, such as `exec-maven-plugin` or `maven-antrun-plugin`.
* Perform file operations not tracked by Maven dependencies.
* Cached content produces inconsistent results.

### Disable caching for a module{#smart-build-disable-caching}

You can add the following property to the affected module's `pom.xml`:

```xml
<properties>
  <maven.build.cache.enabled>false</maven.build.cache.enabled>
</properties>
```

This syntax forces the module to rebuild on every pipeline execution while other modules continue to benefit from caching.

### Limitations and considerations when using Smart Build{#smart-build-limitations}

Keep the following in mind when you use Smart Build:

* Smart Build relies on Maven dependency analysis.
* Changes outside the dependency graph may not trigger rebuilds.
* Some plug-ins may not be fully compatible with caching.
* You can switch back to **Full Build** at any time by editing the production pipeline.

If you encounter unexpected build behavior, consider disabling caching for specific modules or temporarily switching your build strategy to **Full Build**.

### Troubleshooting Smart Build issues{#smart-build-troubleshoot}

   | Issue | Suggested solutions |
   | --- | --- |
   | Build results are inconsistent | &bull; Disable caching for affected modules.<br>&bull; Verify plug-in behavior (especially `exec`/`antrun` plug-ins).   |
   | No performance improvement | &bull; Ensure that multiple runs have occurred (cache warm-up).<br>&bull; Check if most modules are changing frequently.  |
   | Unexpected artifacts or missing changes | &bull; Review whether changes are outside Maven dependency tracking.<br>&bull; Use **Full Build** for verification. |

See [Add a production pipeline](#adding-production-pipeline) to enable Smart Build.

## Skip Dispatcher packages {#skip-dispatcher-packages}

To build Dispatcher packages in your pipeline without publishing them to build storage, you can disable the publishing option. Doing so may help reduce the pipeline's run time.

The following configuration to disable publishing Dispatcher packages must be added via your project `pom.xml` file. An environment variable serves as a flag that you set in the Cloud Manager build container to determine when to ignore Dispatcher packages.

```xml
<profile>
  <id>only-include-dispatcher-when-it-isnt-ignored</id>
  <activation>
    <property>
      <name>env.IGNORE_DISPATCHER_PACKAGES</name>
      <value>[!NOTE]rue</value>
    </property>
  </activation>
  <modules>
    <module>dispatcher</module>
  </modules>
</profile>
```
