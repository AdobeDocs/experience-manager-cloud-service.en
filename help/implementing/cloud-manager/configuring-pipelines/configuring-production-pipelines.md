---
title: Add a Production Pipeline
description: Learn how to add a production pipeline to build and deploy your code to production environments.
index: yes
exl-id: 67edca16-159e-469f-815e-d55cf9063aa4
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Add a production pipeline {#configure-production-pipeline}

Learn how to configuring production pipelines to build and deploy your code to production environments. A production pipeline deploys code first to stage environment, and upon approval deploys the same code to the production environment.

A user must have the **[Deployment Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions)** role to configure production pipelines.

>[!NOTE]
>
>A production pipeline cannot be set up until program creation is complete, a git repository has at least one branch, and a production and staging environment set is created.

Before you start to deploy your code, you must configure your pipeline settings from the [!UICONTROL Cloud Manager].

>[!NOTE]
>
>You can [edit pipeline settings](managing-pipelines.md) after the initial setup.

## Add a new production pipeline {#adding-production-pipeline}

Once you have set up your program and have at least one environment using the [!UICONTROL Cloud Manager] UI, you are ready to add a production pipeline by following these steps.

>[!TIP]
>
>Before you configure a front-end pipeline, see the [AEM Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) for an end-to-end guide though the easy-to-use AEM Quick Site Creation tool. This journey will help you streamline the front-end development of your AEM Site, allowing you to quickly customize your site with no AEM back-end knowledge.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. Navigate to the **Pipelines** card from the **Program Overview** page and click **Add** to select **Add Production Pipeline**. 

   ![The Pipelines card on the Program Manager overview](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-1.png)

1. The **Add Production Pipeline** dialog box displays. Provide a **Pipeline Name** to identify your pipeline along with the following options. Click **Continue**.

   **Deployment Trigger** - You have the following options when defining the deployment triggers to start the pipeline.
      
      * **Manual** - Use this option to manually start the pipeline.
      * **On Git Changes** - This options starts the CI/CD pipeline whenever commits are added to the configured git branch. With this option, you can still start the pipeline manually as required.  

    **Important Metric Failures Behavior** - During pipeline setup or edit, the **Deployment Manager** has the option of defining the behavior of the pipeline when an important failure is encountered in any of the quality gates. The available options are:

    * **Ask every time** - This is the default setting and requires manual intervention on any important failure.
    * **Fail Immediately** - If selected, the pipeline is cancelled whenever an important failure occurs. This is essentially emulating a user manually rejecting each failure.
    * **Continue Immediately** - If selected, the pipeline will proceed automatically whenever an important failure occurs. This is essentially emulating a user manually approving each failure.

    ![Production pipeline configuration](/help/implementing/cloud-manager/assets/configure-pipeline/production-pipeline-configuration.png)

1. On the **Source Code** tab you must select which type of code the pipeline should process.

   * **[Full Stack Code](#full-stack-code)**
   * **[Targeted deployment](#targeted-deployment)**

See [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) for more information about the types of pipelines.

The steps to complete the creation of your production pipeline vary depending on the type of source code you selected. Follow the links above to jump to the next section of this document so you can complete the configuration of your pipeline.

### Full Stack Code {#full-stack-code}

A full-stack code pipeline simultaneously deploys back-end and front-end code builds containing one or more AEM server applications along with HTTPD/Dispatcher configuration.

>[!NOTE]
>
>If a full-stack code pipeline already exists for the selected environment, this selection is disabled.

To finish the configuration of the full-stack code production pipeline, follow these steps.

1. On the **Source Code** tab, you must define the following options.

   * **Repository** - This option defines from which git repo the pipeline should retrieve the code.

   >[!TIP]
   > 
   >See the document [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md) to learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - This option defines from which branch in the selected the pipeline should retrieve the code.
     * Enter the first few characters of the branch name and the auto-complete feature of this field will find the matching branches to help you select.
   * **Ignore Web Tier Configuration** - When checked, the pipeline does not deploy your web tier configuration.
   * **Pause before deploying to Production** - This option pauses the pipeline before deploying to production.
   * **Scheduled** - This option allows the user to enable the scheduled production deployment.

   ![Full stack code](/help/implementing/cloud-manager/assets/configure-pipeline/production-pipeline-fullstack.png)

1. Tap or click **Continue** to advance to the **Experience Audit** tab where you can define the paths that should always be included in the Experience Audit.

   ![Add Experience Audit](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-audit.png)
  
1. Provide paths to be included in the Experience Audit.

   * See the document [Experience Audit Testing](/help/implementing/cloud-manager/experience-audit-dashboard.md#configuration) for details.

1. Click **Save** to save your pipeline.

Paths configured for the Experience Audit are submitted to the service and evaluated according to the performance, accessibility, SEO (Search Engine Optimization), best practice, and PWA (Progressive Web App) tests when the pipeline runs. See [Understanding Experience Audit Results](/help/implementing/cloud-manager/experience-audit-dashboard.md) for more details.

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
>Web tier and config pipelines are not supported with private repositories. See the document [Adding Private Repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/private-repositories.md) for details and the full list of limitations.

The steps to complete the creation of your production, targeted deployment pipeline are the same once you choose a deployment type.

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
   * **Scheduled** - This option allows the user to enable the scheduled production deployment. Only available for web tier targeted deployments.
   
   ![Config pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/prod-pipeline-config-deployment.png)

1. Click **Save**.

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
