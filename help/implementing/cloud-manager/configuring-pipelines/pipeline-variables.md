---
title: Configuring Pipeline Variables
description: Learn how you can use pipeline variables in Cloud Manager to manage specific configuration variables for your build.
exl-id: cfcef2e2-0590-457d-a0f9-6092a6d9e0e8
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Configuring Pipeline Variables {#configuring-pipeline-variables}

Your build process may depend upon specific configuration variables which would be inappropriate to place in the git repository or you may need to vary them between pipeline executions using the same branch. Cloud Manager allows you to manage these data as pipeline variables.

## Pipeline Variables {#pipeline-variables}

Using Cloud Manager you can configure pipeline variables in several different ways.

* [Via the Cloud Manager UI](#ui)
* [Using the Cloud Manager CLI](#cli)
* [Using the Cloud Manager API](https://developer.adobe.com/experience-cloud/cloud-manager/reference/api/#tag/Variables/operation/getPipelineVariables)

Variables may be stored as either plain text or encrypted at rest. In either case, variables are made available inside the build environment as an environment variable which can then be referenced from inside the `pom.xml` file or other build scripts.

### Pipeline Variable Naming Conventions {#naming-conventions}

Variable names must observe the following conventions.

* Variables may only contain alphanumeric characters and the underscore (`_`).
* The names should be all upper-case.
* There is a limit of 200 variables per pipeline.
* Each name must be 100 characters or less.
* Each `string` variable value must be less than 2048 characters.
* Each `secretString` type variable value must be 500 characters or less.

## Via the Cloud Manager UI {#ui}

Pipeline variables can be configured and managed via the Cloud Manager UI. You must have permissions to edit the pipeline in order to add, edit, and delete pipeline variables.

If a pipeline is running, variable management is blocked.

### Adding Pipeline Variables {#add-ui}

1. When [managing your pipelines,](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md) tap or click the ellipsis button of the pipeline for which you want to create pipeline variables and select **View/edit variables** from the context menu.

   ![View/edit pipeline variables](/help/implementing/cloud-manager/assets/pipeline-variables-view-edit.png)

1. The **Variables Configuration** window opens. Enter the variable details in the first row of the table and tap or click **Add**.

   * **Configuration Name** is a unique identifier for your variable, which must head [pipeline variable naming conventions](#naming-conventions).
   * **Value** is the value that the variable holds.
   * **Step Applied** is the step in the pipeline to which the variable applies. It is required.
     * **Build**
     * **Functional testing**
     * **UI testing**
   * **Type** defines if the variable is plain text or encrypted as a secret.

   ![Add variable](/help/implementing/cloud-manager/assets/pipeline-variables-add-variable.png) 

1. The is added to the table. Add additional variables as required and then tap or click **Save** to save the variables you added to the pipeline.

### Editing Pipeline Variables {#edit-ui}

1. When [managing your pipelines,](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md) tap or click the ellipsis button of the pipeline for which you want to create pipeline variables and select **View/edit variables** from the context menu.

   ![View/edit pipeline variables](/help/implementing/cloud-manager/assets/pipeline-variables-view-edit.png)

1. The **Variables Configuration** window opens. Tap or click the ellipsis button of the variable you want to edit and select **Edit**.

   ![Edit variable](/help/implementing/cloud-manager/assets/pipeline-variables-edit.png)

1. Update the value of the variable as required and tap or click **Apply** (the checkmark at the end of the row) to apply the change or **Discard** (the back arrow) to revert the change.

   * Only the value of the variable can edited.

   ![Editing a variable](/help/implementing/cloud-manager/assets/pipeline-variables-edit-save.png)

1. Tap or click **Save** to save the changes you made to the variables to the pipeline.

If you want to delete a variable, select **Delete** instead of **Edit** from the ellipsis menu of the pipeline variable in the **Variables Configuration** window.

## Using the Cloud Manager CLI {#cli}

This CLI command sets a variable.

```shell
$ aio cloudmanager:set-pipeline-variables PIPELINEID --variable MY_CUSTOM_VARIABLE test
```

This command lists variables.

```shell
$ aio cloudmanager:list-pipeline-variables PIPELINEID
```

When used inside a Maven `pom.xml` file, it is typically helpful to map these variables to Maven properties using a syntax similar to this.

```xml
        <profile>
            <id>cmBuild</id>
            <activation>
                <property>
                    <name>env.CM_BUILD</name>
                </property>
            </activation>
            <properties>
                <my.custom.property>${env.MY_CUSTOM_VARIABLE}</my.custom.property> 
            </properties>
        </profile>
```
