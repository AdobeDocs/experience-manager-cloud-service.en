---
title: Configuring Non-Production Pipelines
description: Learn how to configuring non-production pipelines to test the quality of your code before deploying to production environments.
index: yes
exl-id: eba608eb-a19e-4bff-82ff-05860ceabe6e
---
# Configuring Non-Production Pipelines {#configuring-non-production-pipelines}

Learn how to configuring non-production pipelines to test the quality of your code before deploying to production environments.

## Non-Production Pipelines {#non-production-pipelines}

In addition to [production pipelines](#configuring-production-pipelines.md) which deploys to stagings and production environments, you can also set up non-production pipelines to validate your code.

There are two types of non-production pipelines:

* **Code Quality Pipelines** - These run code quality scans on the code in a git branch and executes the build and code quality steps.
* **Deployment Pipelines** - In addition to executing the build and code quality steps like the code quality pipelines, these pipelines deploy the code to a non-production environment.

>[!NOTE]
>
>You can [edit pipeline settings](managing-pipelines.md) after the initial setup.

## Adding a New Non-Production Pipeline {#adding-non-production-pipeline}

Once you have set up your program and have at least one environment using the Cloud Manager UI, you are ready to add a non-production pipeline by following these steps.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Access the **Pipelines** card from the Cloud Manager home screen. Click on **+Add** and select **Add Non-Production Pipeline**. 

   ![Add non-production pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add1.png)

1. On the **Configuration** tab of the **Add Non-Production Pipeline** dialog, select the type of non-production pipeline you with to add, either **Code Quality Pipeline** or **Deployment Pipeline**.

   ![Add Non-Production pipeline dialog](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-config.png)

1. Provide a **Non-Production Pipeline Name** to identify your pipeline along with the following additional information.

   * **Deployment Trigger** - You have the following options when defining the deployment triggers to start the pipeline.
   
     * **Manual** - Use this option to manually start the pipeline.
     * **On Git Changes** - This options starts the CI/CD pipeline whenever commits are added to the configured git branch. With this option, you can still start the pipeline manually as required.  

1. Click **Continue**.

1. On the **Source Code** tab of the **Add Non-Production Pipeline** dialog, you must select which type of code the pipeline should process.

   * **[Front End Code](#front-end-code)**
   * **[Full Stack Code](#full-stack-code)**
   * **[Web Tier Config](#web-tier-config)**

The steps to complete the creation of your non-production pipeline vary depending on the option for **Source Code** you selected. Follow the links above to jump to the next section of this document to complete the configuration of your pipeline.

### Front End Code {#front-end-code}

A front-end code pipeline deploys front-end code builds containing one or more client-side UI applications. See the document [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#front-end) for more information about this type of pipeline.

To finish the configuration of the front-end code non-production pipeline, follow these steps.

1. On the **Source Code** tab, you must define the following options.

   * **Eligible Deployment Environments** - If your pipeline is a deployment pipeline, you must select to which environments it should deploy.
   * **Repository** - This option defines from which git repo the pipeline should retrieve the code.

   >[!TIP]
   > 
   >See the document [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/cloud-manager-repositories.md) to learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - This option defines from which branch in the selected the pipeline should retrieve the code.
     * Enter the first few characters of the branch name and the auto-complete feature of this field will find the matching branches to help you select.
   * **Code Location** - This option defines the path in the branch of the selected repo from which the pipeline should retrieve the code.
   
   ![Front-end pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-front-end.png)

1. Click **Save**.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

### Full Stack Code {#full-stack-code}

A full-stack code pipeline simultaneously deploys back-end and front-end code builds containing one or more AEM server applications along with HTTPD/Dispatcher configuration. See the document [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#full-stack-pipeline) for more information about this type of pipeline.

>[!NOTE]
>
>If a full-stack code pipeline already exists for the selected environment, this selection will be disabled.

To finish the configuration of the full-stack code non-production pipeline, follow these steps.

1. On the **Source Code** tab, you must define the following options.

   * **Eligible Deployment Environments** - If your pipeline is a deployment pipeline, you must select to which environments it should deploy.
   * **Repository** - This options defines from which git repo the pipeline should retrieve the code.

   >[!TIP]
   > 
   >See the document [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/cloud-manager-repositories.md) to learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - This option defines from which branch in the selected the pipeline should retrieve the code.
     * Enter the first few characters of the branch name and the auto-complete feature of this field will find the matching branches to help you select.
   * **Ignore Web Tier Configuration** - When checked, the pipeline will not deploy your web tier configuration.

   ![Full-stack pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-full-stack.png)

1. Click **Save**.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

### Web Tier Config {#web-tier-config}

A web tier config pipeline Deploys HTTPD/Dispatcher configurations. See the document [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipeline) for more information about this type of pipeline.

>[!NOTE]
>
>If a web-tier code pipeline already exists for the selected environment, this selection will be disabled.

To finish the configuration of the web-tier code non-production pipeline, follow these steps.
   
1. On the **Source Code** tab, you must define the following options.

   * **Eligible Deployment Environments** - If your pipeline is a deployment pipeline, you must select to which environments it should deploy.
   * **Repository** - This option defines from which git repo the pipeline should retrieve the code.

   >[!TIP]
   > 
   >See the document [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/cloud-manager-repositories.md) to learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - This option defines from which branch in the selected the pipeline should retrieve the code.
   * **Code Location** - This option defines the path in the branch of the selected repo from which the pipeline should retrieve the code. 
      * For web tier config pipelines this is usually the path containing `conf.d`, `conf.dispatcher.d`, and `opt-in` directories.
      * For example, if the project structure was generated from the [AEM Project Archetype,](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html?lang=en) the path would be `/dispatcher/src`.

   ![Web tier pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-web-tier.png)

1. Click **Save**.

>[!NOTE]
>
>If you have an existing full-stack pipeline deploying to an environment, creating a web tier config pipeline for the same environment will case the existing web tier configuration in the full-stack pipeline to be ignored.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

## Skip Dispatcher Packages {#skip-dispatcher-packages}

If you want dispatcher packages built as part of your pipeline, but do not want them published to build storage, you can disable publishing them, which may reduce pipeline run duration.

The following configuration to disable publishing dispatcher packages must be added via your project `pom.xml` file. It is based on an environment variable, which serves as a flag you can set in the Cloud Manager build container to define when dispatcher packages should be ignored.

```xml
<profile>
  <id>only-include-dispatcher-when-it-isnt-ignored</id>
  <activation>
    <property>
      <name>env.IGNORE_DISPATCHER_PACKAGES</name>
      <value>!true</value>
    </property>
  </activation>
  <modules>
    <module>dispatcher</module>
  </modules>
</profile>
```
