---
title: Pipeline Variables in Cloud Manager
description: Learn how you can use pipeline variables in Cloud Manager to manage specific configuration variables for your build.
exl-id: cfcef2e2-0590-457d-a0f9-6092a6d9e0e8
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Pipeline variables in Cloud Manager {#configuring-pipeline-variables}

Your build process might rely on specific configuration variables that should not be stored in the Git repository. Or, you may need to adjust them between pipeline runs on the same branch. Cloud Manager lets you manage these settings as pipeline variables.

## About pipeline variables {#pipeline-variables}

Using Cloud Manager you can configure pipeline variables in several different ways.

* [Using the Cloud Manager user interface](#ui)
* [Using the Cloud Manager CLI](#cli)
* [Using the Cloud Manager API](https://developer.adobe.com/experience-cloud/cloud-manager/reference/api/#tag/Variables/operation/getPipelineVariables)

Variables may be stored as either plain text or encrypted at rest. In either case, variables are made available inside the build environment as an environment variable, which can then be referenced from inside the `pom.xml` file or other build scripts.

## Add a pipeline variable through Cloud Manager {#ui}

Pipeline variables can be configured and managed through the Cloud Manager user interface. They help streamline pipeline management, especially when varying configurations are required across different steps.

You must have permissions to edit the pipeline to add, edit, and delete pipeline variables.

If a pipeline is running, variable management is blocked.

**To add a pipeline variable through Cloud Manager:**

1. When [managing your pipelines](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md), click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) of the pipeline for which you want to create pipeline variables.

1. From the drop-down menu, click **View/Edit variables**.

   ![View/Edit pipeline variables](/help/implementing/cloud-manager/assets/pipeline-variables-view-edit.png)

1. In the **Variables Configuration** dialog box, enter the details in the first row of the table.

   | Field | Description |
   | --- | --- |
   | Name | A unique name of the configuration variable. It identifies the specific variable that is used in the pipeline. It must adhere to the following naming conventions:<ul><li>Variables can only contain alphanumeric characters and the underscore (`_`).</li><li>The names should be all upper-case.</li><li>There is a limit of 200 variables per pipeline.</li><li>Each name must be 100 characters or less.</li><li>Each `string` variable value must be less than 2048 characters.</li><li>Each `secretString` type variable value must be 500 characters or less.</li></ul> |
   | Value | The value that the variable holds. |
   | Step Applied | Required. The step in the pipeline to which the variable applies:<ul><li>**Build** - The variable is applied during the build process.</li><li>**Functional testing** - The variable is used during the functional testing step.</li><li>**UI testing** - The variable is used during the UI testing phase.</li></ul> |
   | Type | Select if the variable is plain text or encrypted as a secret.  |

   ![Add variable](/help/implementing/cloud-manager/assets/pipeline-variables-add-variable.png) 

1. Click **Add**.

   Add additional variables as needed.

1. Click **Save**.

## Edit a pipeline variable {#edit-ui}

1. When [managing your pipelines](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md), click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) of the pipeline for which you want to edit pipeline variables.

1. In the drop-down menu, click **View/Edit variables**.

   ![View/Edit pipeline variables](/help/implementing/cloud-manager/assets/pipeline-variables-view-edit.png)

1. In the **Variables Configuration** dialog box, click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) of the variable that you want to change.

1. In the drop-down menu, click **Edit**.

   ![Edit variable](/help/implementing/cloud-manager/assets/pipeline-variables-edit.png)

1. Update the value of the variable as required.

   Only the variable's value can be changed.

1. Do one of the following:

   * Click ![Apply - Checkmark icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Checkmark_18_N.svg) to apply the change.
   * Click ![Undo icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Undo_18_N.svg) to revert the change.

1. Click **Save**.


## Delete a pipeline variable {#delete-ui}

1. When [managing your pipelines](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md), click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) of the pipeline for which you want to delete pipeline variables.

1. In the drop-down menu, click **View/Edit variables**.

   ![View/Edit pipeline variables](/help/implementing/cloud-manager/assets/pipeline-variables-view-edit.png)

1. In the **Variables Configuration** dialog box, click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) of the variable you want to remove, then click **Delete**.

## Set pipeline variables using the Cloud Manager CLI {#cli}

This command in the CLI (Command Line Interface) sets a variable.

```shell
$ aio cloudmanager:set-pipeline-variables PIPELINEID --variable MY_CUSTOM_VARIABLE test
```

This command lists variables.

```shell
$ aio cloudmanager:list-pipeline-variables PIPELINEID
```

When used in a Maven `pom.xml` file, it is often useful to link these variables to Maven properties using a syntax similar to the following example:

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
