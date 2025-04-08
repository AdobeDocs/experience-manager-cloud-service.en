---
title: Add a Non-Production Pipeline
description: Learn how to add a non-production pipeline to test the quality of your code before deploying to production environments.
index: yes
exl-id: eba608eb-a19e-4bff-82ff-05860ceabe6e
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Add a non-production pipeline {#configuring-non-production-pipelines}

Learn how to configure non-production pipelines to test the quality of your code before deploying to production environments.

A user must have the **[Deployment Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions)** role to configure non-production pipelines.

## Non-production pipelines {#non-production-pipelines}

In addition to [production pipelines](#configuring-production-pipelines.md) which deploys to stagings and production environments, you can also set up non-production pipelines to validate your code.

There are two types of non-production pipelines:

* **Code Quality Pipelines** - These run code quality scans on the code in a git branch and executes the build and code quality steps.
* **Deployment Pipelines** - In addition to executing the build and code quality steps like the code quality pipelines, these pipelines deploy the code to a non-production environment.

>[!NOTE]
>
>You can [edit pipeline settings](managing-pipelines.md) after the initial setup.

## Add a new non-production pipeline {#adding-non-production-pipeline}

Once you have set up your program and have at least one environment using the Cloud Manager UI, you are ready to add a non-production pipeline by following these steps.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. Access the **Pipelines** card from the Cloud Manager home screen. Click **+Add** and select **Add Non-Production Pipeline**. 

   ![Add non-production pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add1.png)

1. On the **Configuration** tab of the **Add Non-Production Pipeline** dialog, select the type of non-production pipeline you with to add.

   * **Code Quality Pipeline** - Create a pipeline that builds your code, runs unit tests, and evaluates code quality but does NOT deploy.
   * **Deployment Pipeline** - Create a pipeline that builds your code, runs unit tests, evaluates code quality, and deploys to an environment.

   ![Add Non-Production pipeline dialog](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-config.png)

1. Provide a **Non-Production Pipeline Name** to identify your pipeline along with the following additional information.

   * **Deployment Trigger** - You have the following options when defining the deployment triggers to start the pipeline.
   
     * **Manual** - Use this option to manually start the pipeline.
     * **On Git Changes** - This option starts the CI/CD pipeline whenever commits are added to the configured git branch. With this option, you can still start the pipeline manually as required.

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
     * **Experience Audit** - Execute [Experience Audit](/help/implementing/cloud-manager/experience-audit-dashboard.md)

   ![Full-stack pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-full-stack.png)

1. Click **Save**.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

### Targeted deployment {#targeted-deployment}

A targeted deployment deploys code only for selected parts of your AEM application. In such a deployment you can choose to **Include** one of the following types of code:

* **Config** - Configure settings for various features on your AEM environment.
  * See [Using Config Pipelines](/help/operations/config-pipeline.md) for a list of supported configurations, which includes log forwarding, purge-related maintenance tasks, and various CDN configurations, and to manage them in your repository so they are deployed properly.
  * When running a targeted deployment pipeline, configurations will be deployed, provided they are saved to environment, repository, and branch you defined in the pipeline.
  * At any time, there can only be one config pipeline per environment. 
* **Front End Code** - Configure JavaScript and CSS for the front end of your AEM application.
  * With front-end pipelines, more independence is given to front-end developers and the development process can be accelerated.
  * See the document [Developing Sites with the Front-End Pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md) for how this process works along with some considerations to be aware of to get the full potential out of this process.
* **Web Tier Config** - Configure dispatcher properties to store, process, and delivery web pages to the client.
  * See the document [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines) for more details.
  * If a web-tier code pipeline exists for the selected environment, this selection is disabled.
  * If you have an existing full-stack pipeline deploying to an environment, creating a web tier config pipeline for the same environment will case the existing web tier configuration in the full-stack pipeline to be ignored.

>[!NOTE]
>
>Web tier and config pipelines are not supported with private repositories. See [Adding Private Repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/private-repositories.md) for details and the full list of limitations.

The steps to complete the creation of your non-production, targeted deployment pipeline are the same once you choose a deployment type.

1. Choose which deployment type you require.

![Targeted deployment options](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-targeted-deployment.png)

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
   * **Pipeline** - For front-end non-production pipelines, you have the option to enable **[Experience Audit](/help/implementing/cloud-manager/experience-audit-dashboard.md)**.
   
   ![Config pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-config-deployment-experience-audit.png)

1. If you enabled Experience Audit, click **Continue** to advance to the **Experience Audit** tab where you can define the paths that should always be included in the Experience Audit.

   * If you enabled **Experience Audit**, see the document [Experience Audit](/help/implementing/cloud-manager/experience-audit-dashboard.md) for details on how to configure.
   * If you did not, skip this step.

1. Click **Save** to save the pipeline.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

## Skip Dispatcher packages {#skip-dispatcher-packages}

If you want Dispatcher packages built as part of your pipeline, but do not want them published to build storage, you can disable publishing them, which may reduce pipeline run duration.

The following configuration to disable publishing Dispatcher packages must be added via your project `pom.xml` file. It is based on an environment variable, which serves as a flag you can set in the Cloud Manager build container to define when Dispatcher packages should be ignored.

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
