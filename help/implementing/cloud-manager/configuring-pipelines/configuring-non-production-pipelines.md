---
title: Add a Non-Production Pipeline
description: Learn how to add a non-production pipeline to test the quality of your code before deploying to production environments.
index: true
exl-id: eba608eb-a19e-4bff-82ff-05860ceabe6e
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
---

# Add a non-production pipeline {#configuring-non-production-pipelines}

After setting up a program and creating at least one environment in the Cloud Manager UI, you can add non-production pipelines. These pipelines let you test code quality before deploying to production environments.

A user must have the **[Deployment Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions)** role to configure non-production pipelines.

>[!NOTE]
>
>You can [edit pipeline settings](managing-pipelines.md) after the initial setup.

## Add a new non-production pipeline {#adding-non-production-pipeline}

After you set up a program and create at least one environment in the Cloud Manager UI, you can add non-production pipelines. Use these pipelines to test code quality before you deploy to production environments.

**To add a new non-productoin pipeline:**

1. Sign into Cloud Manager at [experiece.adobe.com](https://experience.adobe.com).
1. In the **Quick access** section, click **Experience Manager**.
1. In the left side panel, click **Cloud Manager**.
1. Select an organization that you want.
1. On the **My Programs** console, click a program. 
1. In the left side panel, click **Pipelines**.
1. On the **Pipelines** page, near the upper-right corner, click **Add Pipeline** > **Add Non-Production Pipeline**. 

   ![Add non-production pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add1.png)

1. On the **Configuration** tab of the **Add Non-Production Pipeline** dialog box, select one of the following non-production pipelines you want to create:

   * **Code Quality Pipeline** - Creates a pipeline that builds the code on a GIT branch, runs unit tests, and evaluates code quality without deploying to an environment.
   * **Deployment Pipeline** - Creates a pipeline that builds the code, runs unit tests, evaluates code quality, and deploys to a non-production environment.
   
   ![Add Non-Production pipeline dialog](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-config.png)

1. Under the **Pipeline Configuration** section, in the **Non-Production Pipeline Name** field, type a description for your non-production pipeline.
1. Under the **Deployment Options** section, select one of the following deployment triggers that you want to use:

     * **Manual** - Lets you manually start the pipeline.
     * **On Git Changes** - Starts the pipeline when commits are added to the configured Git branch. With this option, you can still start the pipeline manually, as required.

1. Select the **Important Metric Failures Behavior** that you want to use.

   * **Ask every time** - This behavior is the default setting and requires manual intervention on any important failure.
   * **Fail Immediately** - If selected, the pipeline is canceled whenever an important failure occurs. It essentially emulates a user manually rejecting each failure.
   * **Continue Immediately** - If selected, the pipeline procedes automatically whenever an important failure occurs. It essentially emulates a user manually approving each failure.

1. Click **Continue**.

1. The remaining steps that you use to complete the configuration of your non-production pipeline depend on the type of source code you choose to use.
On the **Source Code** tab of the **Add Non-Production Pipeline** dialog box, select which type of code the non-production pipeline should process.

   * **[I am using Full Stack Code](#full-stack-code)**
   * **[I am using Targeted deployment](#targeted-deployment)**

    See [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) for more information about the types of pipelines.


### I am using Full Stack Code {#full-stack-code}

A full-stack code pipeline simultaneously deploys back-end and front-end code builds containing one or more AEM server applications along with HTTPD/Dispatcher configuration.

>[!NOTE]
>
>If a full-stack code pipeline exists for the selected environment, this selection is disabled.

To finish the configuration of the full-stack code non-production pipeline, do the following:

1. In the **Source Code** section, define the following options.

    * **Eligible Deployment Environments** - Available only when you edit a non-production pipeline. If your pipeline is a deployment pipeline, you must select to which environments it should deploy.
    * **Repository** - From the drop-down list, choose the Git repository that the pipeline uses as its source. Cloud Manager builds code from the repository that you choose here.

      >[!TIP]
      > 
      >See [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md) so you can learn how to add and manage repositories in Cloud Manager.

    * **Git Branch** - From the drop-down list, choose which branch in the selected repository the pipeline should build from. The default is `main`. The pipeline uses the chosen branch as the source for build and deployment. If necessary, click **Refresh** to update the list of available branches for the selected repository. Use this option if a recently created branch does not appear in the list.
    * **Build Strategy**
      * **Full Build** - Builds all modules in the repository every time
      * BETA **Smart Build** - Builds only modules that have changed since the last commit.<br>Learn more about [using Smart Build in a non-production pipeline](#about-smart-build-non-production-pipeline).

        >[!IMPORTANT]
        >
        >Smart Build is available only for Code Quality pipelines and Dev Full Stack Code deployment pipelines.

    * **Ignore Web Tier Configuration** check box - When checked, the pipeline does not deploy your web tier configuration.

1. In the **Pipeline** section, if your pipeline is a deployment pipeline, you can choose to run a testing phase. Check the options that you want to enable in this phase. If none of the options are selected, the testing phase is not displayed during the pipeline's run.

    * **Product Functional Testing** - Run [product functional tests](/help/implementing/cloud-manager/functional-testing.md#product-functional-testing) against the development environment.
    * **Custom Functional Testing** - Run [custom functional tests](/help/implementing/cloud-manager/functional-testing.md#custom-functional-testing) against the development environment.
    * **Custom UI Testing** - Run [custom UI tests](/help/implementing/cloud-manager/ui-testing.md) for custom applications.
    * **Experience Audit** - Run [Experience Audit](/help/implementing/cloud-manager/reports/report-experience-audit.md)

   ![Full-stack pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-full-stack.png)

1. Click **Save**.

The pipeline is saved and you can now [manage your pipelines](managing-pipe
lines.md) on the **Pipelines** card on the **Program Overview** page.

### I am using Targeted deployment {#targeted-deployment}

A targeted deployment deploys code only for selected parts of your AEM application. In such a deployment you can choose to **Include** one of the following types of code:

![Targeted deployment options](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-targeted-deployment1.png)

<!--
* **Config** - Configure settings for various features in your AEM environment.
  * See [Using Config Pipelines](/help/operations/config-pipeline.md) for a list of supported configurations, which include log forwarding, purge-related maintenance tasks, and various CDN configurations, and to manage them in your repository so they are deployed properly.
  * When running a targeted deployment pipeline, configurations are deployed, provided they are saved to the environment, repository, and branch you defined in the pipeline.
  * At any time, there can only be one config pipeline per environment.
* **Configure Edge Delivery Services config pipeline** - Edge Delivery Configuration Pipelines do not have separate development, staging, and production environments. In AEM as a Cloud Service, changes move through development, stage, and production tiers. In contrast, an Edge Delivery Configuration Pipeline applies its configuration directly to all Edge Delivery Sites domains registered in Cloud Manager. To learn more, see [Add an Edge Delivery Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-edge-delivery-pipeline.md).
-->


* **Front End Code** - Configure JavaScript and CSS for the front end of your AEM application.
  * With front-end pipelines, more independence is given to front-end developers and the development process can be accelerated.
  * See the document [Developing Sites with the Front-End Pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md) for how this process works along with some considerations to be aware of to get the full potential out of this process.
* **Web Tier Config** - Configure Dispatcher properties to store, process, and delivery web pages to the client.
  * See the document [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines) for more details.
  * If a web-tier code pipeline exists for the selected environment, this selection is disabled.
  * If a full-stack pipeline already deploys to an environment, you can still create a web-tier configuration pipeline for that same environment. When you do, Cloud Manager ignores the web-tier configuration in the full-stack pipeline.

    >[!NOTE]
    >
    >Web tier and config pipelines are not supported with private repositories. See [Adding Private Repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/private-repositories.md) for details and the full list of limitations.

<!--
The steps to complete the creation of your non-production, targeted deployment pipeline are the same once you choose a deployment type.

1. Choose which deployment type you require.

![Targeted deployment options](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-targeted-deployment.png)

1. Define the **Eligible Deployment Environments**.

   * If your pipeline is a deployment pipeline, you must select to which environments it should deploy.
-->

1. Under the **Source Code** section, define the following options:

   * **Repository** - This option defines from which GIT repository that the non-production pipeline should retrieve the code.

      >[!TIP]
      > 
      >See [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md) so you can learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - This option defines from which branch in the selected pipeline should retrieve the code. Enter the first few characters of the branch name and the auto-complete feature of this field. It finds the matching branches that you can select.
   * **Code Location** - This option defines the path in the branch of the selected repo from which the pipeline should retrieve the code.

<!--
   * **Pipeline** - For front-end non-production pipelines, you have the option to enable **[Experience Audit](/help/implementing/cloud-manager/reports/report-experience-audit.md)**.
   
   ![Config pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-config-deployment-experience-audit.png)
-->

1. If you enabled Experience Audit, click **Continue** to advance to the **Experience Audit** tab where you can define the paths that should always be included in the Experience Audit.

   * If you enabled **Experience Audit**, see the document [Experience Audit](/help/implementing/cloud-manager/reports/report-experience-audit.md) for details on how to configure.
   * If you did not, skip this step.

1. Click **Save** to save the pipeline.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.


## About using Smart Build in a non-production pipeline{#about-smart-build-non-production-pipeline}

**Smart Build** in Cloud Manager is an optimized build strategy for non-production pipelines. Smart Build reduces build times by caching modules and rebuilding only those modules that have changed since the last successful run. Unchanged modules are reused from cache, while only modified modules and their dependencies are rebuilt, improving efficiency for iterative development workflows.

Smart Build is currently available only for the following:

* Code Quality pipelines.
* Dev full-stack deployment pipelines.

>[!NOTE]
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
* You can switch back to **Full Build** at any time by editing the non-production pipeline.

If you encounter unexpected build behavior, consider disabling caching for specific modules or temporarily switching your build strategy to **Full Build**.

### Troubleshooting Smart Build issues{#smart-build-troubleshoot}

   | Issue | Suggested solutions |
   | --- | --- |
   | Build results are inconsistent | &bull; Disable caching for affected modules.<br>&bull; Verify plug-in behavior (especially `exec`/`antrun` plug-ins).   |
   | No performance improvement | &bull; Ensure that multiple runs have occurred (cache warm-up).<br>&bull; Check if most modules are changing frequently.  |
   | Unexpected artifacts or missing changes | &bull; Review whether changes are outside Maven dependency tracking.<br>&bull; Use **Full Build** for verification. |

See [Add a non-production pipeline](#adding-non-production-pipeline) to enable Smart Build.









   

<!--
## Add a non-production pipeline {#adding-non-production-pipeline}

Once you have set up your program and have at least one environment using the Cloud Manager UI, you are ready to add a non-production pipeline by following these steps.

1. Sign into Cloud Manager at [experiece.adobe.com](https://experience.adobe.com).
1. In the **Quick access** section, click **Experience Manager**.
1. In the left side panel, click **Cloud Manager**.
1. Select an organization that you want.
1. On the **My Programs** console, click a program. 

1. Access the **Pipelines** card from the Cloud Manager home screen. Click **+Add** and select **Add Non-Production Pipeline**. 

   ![Add non-production pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add1.png)

1. On the **Configuration** tab of the **Add Non-Production Pipeline** dialog, select the type of non-production pipeline you with to add.

   * **Code Quality Pipeline** - Create a pipeline that builds your code, runs unit tests, and evaluates code quality but does NOT deploy.
   * **Deployment Pipeline** - Create a pipeline that builds your code, runs unit tests, evaluates code quality, and deploys to an environment.

   ![Add Non-Production pipeline dialog](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-config.png)

1. Provide a **Non-Production Pipeline Name** to identify your pipeline along with the following additional information.

   * **Deployment Trigger** - You have the following options when defining the deployment triggers to start the pipeline.
   
     * **Manual** - Use this option to start the pipeline manually.
     * **On Git Changes** - This option starts the CI/CD pipeline whenever commits are added to the configured Git branch. With this option, you can still start the pipeline manually as required.

1. If you choose to create a **Deployment Pipeline**, you must also define the **Important Metric Failures Behavior**.

   * **Ask every time** - This behavior is the default setting and requires manual intervention on any important failure.
   * **Fail Immediately** - If selected, the pipeline is canceled whenever an important failure occurs. It is essentially emulating a user manually rejecting each failure.
   * **Continue Immediately** - If selected, the pipeline procedes automatically whenever an important failure occurs. It is essentially emulating a user manually approving each failure.

1. Click **Continue**.

1. On the **Source Code** tab of the **Add Non-Production Pipeline** dialog, you must select which type of code the pipeline should process.

   * **[Full Stack Code](#full-stack-code)**
   * **[Targeted deployment](#targeted-deployment)**

See [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) for more information about the types of pipelines.

The steps to complete the creation of your non-production pipeline vary depending on the type of source code you selected. Follow the links above to jump to the next section of this document so you can complete the configuration of your pipeline.

### Full Stack Code {#full-stack-code}

A full-stack code pipeline simultaneously deploys back-end and front-end code builds containing one or more AEM server applications along with HTTPD/Dispatcher configuration.

>[!NOTE]
>
>If a full-stack code pipeline exists for the selected environment, this selection is disabled.

To finish the configuration of the full-stack code non-production pipeline, follow these steps.

1. On the **Source Code** tab, you must define the following options.

   * **Eligible Deployment Environments** - If your pipeline is a deployment pipeline, you must select to which environments it should deploy.
   * **Repository** - This option defines from which git repo that the pipeline should retrieve the code.

   >[!TIP]
   > 
   >See [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md) so you can learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - This option defines from which branch in the selected pipeline should retrieve the code.
     * Enter the first few characters of the branch name and the auto-complete feature of this field. It helps you find the matching branches that you can select.
   * **Ignore Web Tier Configuration** - When checked, the pipeline does not deploy your web tier configuration.
   * **Pipeline** - If your pipeline is a deployment pipeline, you can choose to run a testing phase. Check the options that you want to enable in this phase. If none of the options are selected, the testing phase is not displayed during the pipeline's run.

     * **Product Functional Testing** - Execute [product functional tests](/help/implementing/cloud-manager/functional-testing.md#product-functional-testing) against the development environment.
     * **Custom Functional Testing** - Execute [custom functional tests](/help/implementing/cloud-manager/functional-testing.md#custom-functional-testing) against the development environment.
     * **Custom UI Testing** - Execute [custom UI tests](/help/implementing/cloud-manager/ui-testing.md) for custom applications.
     * **Experience Audit** - Execute [Experience Audit](/help/implementing/cloud-manager/reports/report-experience-audit.md)

   ![Full-stack pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-full-stack.png)

1. Click **Save**.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

-->



## Exclude Dispatcher packages {#exclude-dispatcher-packages}

If you want Dispatcher packages built in your pipeline but not uploaded to build storage, disable publishing. Doing so can shorten the pipeline's run time.

Add the following configuration to your project `pom.xml` file to disable publishing Dispatcher packages. Set an environment variable in the Cloud Manager build container to flag when to ignore Dispatcher packages. The pipeline reads this flag and ignores them accordingly.

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
