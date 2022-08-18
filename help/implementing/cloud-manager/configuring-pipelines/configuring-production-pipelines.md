---
title: Configuring Production Pipelines
description: Learn how to configuring production pipelines to build and deploy your code to production environments.
index: yes
exl-id: 67edca16-159e-469f-815e-d55cf9063aa4
---
# Configuring a Production Pipeline {#configure-production-pipeline}

Learn how to configuring Production pipelines to build and deploy your code to Production environments. A Production pipeline deploys code first to Stage environment, and upon approval deploys the same code to the Production environment.

A user must have the **[Deployment Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions)** role to configure production pipelines.

>[!NOTE]
>
>A production pipeline can not be set up until program creation is complete, a git repository has at least one branch, and a production and staging environment set is created.

Before you start to deploy your code, you must configure your pipeline settings from the [!UICONTROL Cloud Manager].

>[!NOTE]
>
>You can [edit pipeline settings](managing-pipelines.md) after the initial setup.

## Adding a New Production Pipeline {#adding-production-pipeline}

Once you have set up your program and have at least one environment using the [!UICONTROL Cloud Manager] UI, you are ready to add a production pipeline by following these steps.

>[!TIP]
>
>Before you configure a front-end pipeline, see the [AEM Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) for an end-to-end guide though the easy-to-use AEM Quick Site Creation tool. This journey will help you streamline the front-end development of your AEM Site, allowing you to quickly customize your site with no AEM back-end knowledge.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page and click on **Add** to select **Add Production Pipeline**. 

   ![The Pipelines card on the Program Manager overview](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-1.png)

1. The **Add Production Pipeline** dialog box displays. Provide a **Pipeline Name** to identify your pipeline along with the following options. Click **Continue**.

   **Deployment Trigger** - You have the following options when defining the deployment triggers to start the pipeline.
      
      * **Manual** - Use this option to manually start the pipeline.
      * **On Git Changes** - This options starts the CI/CD pipeline whenever commits are added to the configured git branch. With this option, you can still start the pipeline manually as required.  

    **Important Metric Failures Behavior** - During pipeline setup or edit, the **Deployment Manager** has the option of defining the behavior of the pipeline when an important failure is encountered in any of the quality gates. The available options are:

    * **Ask every time** - This is the default setting and requires manual intervention on any important failure.
    * **Fail Immediately** - If selected, the pipeline will be cancelled whenever an important failure occurs. This is essentially emulating a user manually rejecting each failure.
    * **Continue Immediately** - If selected, the pipeline will proceed automatically whenever an important failure occurs. This is essentially emulating a user manually approving each failure.

    ![Production pipeline configuration](/help/implementing/cloud-manager/assets/configure-pipeline/production-pipeline-configuration.png)

1. On the **Source Code** tab you must define where the pipeline should retrieve its code and what type of code it is.

   * **[Front End Code](#front-end-code)**
   * **[Full Stack Code](#full-stack-code)**
   * **[Web Tier Config](#web-tier-config)**

The steps to complete the creation of your production pipeline vary depending on the option for **Source Code** you selected. Follow the links above to jump to the next section of this document to complete the configuration of your pipeline.

### Front End Code {#front-end-code}

A front-end code pipeline deploys front-end code builds containing one or more client-side UI applications. See the document [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#front-end) for more information about this type of pipeline.

To finish the configuration of the front end code production pipeline, follow these steps.

1. On the **Source Code** tab, you must define the following options.

   * **Repository** - This option defines from which git repo the pipeline should retrieve the code.
   
   >[!TIP]
   > 
   >See the document [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/cloud-manager-repositories.md) to learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - This option defines from which branch in the selected the pipeline should retrieve the code.
     * Enter the first few characters of the branch name and the auto-complete feature of this field will find the matching branches to help you select.
   * **Code Location** - This option defines the path in the branch of the selected repo from which the pipeline should retrieve the code.
   * **Pause before deploying to Production** - This option pauses the pipeline before deploying to production.

   ![Front end code](/help/implementing/cloud-manager/assets/configure-pipeline/production-pipeline-frontend.png)

1. Click **Save** to save your pipeline.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

### Full Stack Code {#full-stack-code}

A full-stack code pipeline simultaneously deploys back-end and front-end code builds containing one or more AEM server applications along with HTTPD/Dispatcher configuration. See the document [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#full-stack-pipeline) for more information about this type of pipeline.

>[!NOTE]
>
>If a full-stack code pipeline already exists for the selected environment, this selection will be disabled.

To finish the configuration of the full-stack code production pipeline, follow these steps.

1. On the **Source Code** tab, you must define the following options.

   * **Repository** - This option defines from which git repo the pipeline should retrieve the code.

   >[!TIP]
   > 
   >See the document [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/cloud-manager-repositories.md) to learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - This option defines from which branch in the selected the pipeline should retrieve the code.
     * Enter the first few characters of the branch name and the auto-complete feature of this field will find the matching branches to help you select.
   * **Code Location** - This option defines the path in the branch of the selected repo from which the pipeline should retrieve the code.
   * **Pause before deploying to Production** - This option pauses the pipeline before deploying to production.
   * **Scheduled** - This option allows the user to enable the scheduled production deployment.

   ![Full stack code](/help/implementing/cloud-manager/assets/configure-pipeline/production-pipeline-fullstack.png)

1. Click **Continue** to advance to the **Experience Audit** tab where you can define the paths that should always be included in the Experience Audit.

   ![Add Experience Audit](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-audit.png)
  
1. Provide a path to be included in the Experience Audit.

   * Page paths must start with `/`.
   * For example, if you would like to include `https://wknd.site/us/en/about-us.html` in the Experience Audit, enter the path `/us/en/about-us.html`.

   ![Defining a path for the Experience Audit](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-audit3.png)

1. Click **Add Page** and the path will be auto-completed with the address of your environment and added to the table of paths.

   ![Saving path to the table](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-audit4.png)

1. Continue to add paths as necessary by repeating the previous two steps.

   * You can add a maximum of 25 paths.
   * If you don't define any paths, the homepage of the site will be included in the Experience Audit by default.

1. Click on **Save** to save your pipeline.

Paths configured for the Experience Audit will be submitted to the service and evaluated according to the performance, accessibility, SEO (Search Engine Optimization), best practice, and PWA (Progressive Web App) tests when the pipeline runs. Refer to [Understanding Experience Audit Results](/help/implementing/cloud-manager/experience-audit-testing.md) for more details.

The pipeline is saved and you can now [manage your pipelines](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page.

### Web Tier Config {#web-tier-config}

A web tier config pipeline Deploys HTTPD/Dispatcher configurations. See the document [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipeline) for more information about this type of pipeline.

To finish the configuration of the full-stack code production pipeline, follow these steps.
   
1. On the **Source Code** tab, you must define the following options.

   * **Repository** - This option defines from which git repo the pipeline should retrieve the code.
   
   >[!TIP]
   > 
   >See the document [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/cloud-manager-repositories.md) to learn how to add and manage repositories in Cloud Manager.
   
   * **Git Branch** - This option defines from which branch in the selected the pipeline should retrieve the code.
     * Enter the first few characters of the branch name and the auto-complete feature of this field will find the matching branches to help you select.
   * **Code Location** - This option defines the path in the branch of the selected repo from which the pipeline should retrieve the code.
     * For web tier config pipelines this is usually the path containing `conf.d`, `conf.dispatcher.d`, and `opt-in` directories.
     * For example, if the project structure was generated from the [AEM Project Archetype,](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html?lang=en) the path would be `/dispatcher/src`.
   * **Pause before deploying to Production** - This option pauses the pipeline before deploying to production.
   * **Scheduled** - This option allows the user to enable the scheduled production deployment.

   ![Web tier code](/help/implementing/cloud-manager/assets/configure-pipeline/production-pipeline-webtier.png)

1. Click **Save** to save your pipeline.

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
