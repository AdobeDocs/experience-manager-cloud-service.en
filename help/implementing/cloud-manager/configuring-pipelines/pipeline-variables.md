---
title: Configuring Pipeline Variables
description: Learn how you can use pipeline variables in Cloud Manager to manage specific configuration variables for your build.
---

# Configuring Pipeline Variables {#configuring-pipeline-variables}

Your build process may depend upon specific configuration variables which would be inappropriate to place in the git repository or you may need to vary them between pipeline executions using the same branch. Cloud Manager allows you to manage these data as pipeline variables.

## Pipeline Variables {#pipeline-variables}

Using Cloud Manager you can configure pipeline variables in several different ways.

* [Via the Cloud Manager UI](#ui)
* [Using the Cloud Manager CLI](#cli)
* [Using the Cloud Manager API](https://developer.adobe.com/experience-cloud/cloud-manager/reference/api/#tag/Variables/operation/getPipelineVariables)


Variables may be stored as either plain text or encrypted at rest. In either case, variables are made available inside the build environment as an environment variable which can then be referenced from inside the `pom.xml` file or other build scripts.

## Via the Cloud Manager UI {#ui}

## Using the Cloud Manager CLI {#cli}

This CLI command sets a variable.

```shell
$ aio cloudmanager:set-pipeline-variables PIPELINEID --variable MY_CUSTOM_VARIABLE test
```

This command lists variables.

```shell
$ aio cloudmanager:list-pipeline-variables PIPELINEID
```

Variable names must observe the following conventions.

* Variables may only contain alphanumeric characters and the underscore (`_`).
* The names should be all upper-case.
* There is a limit of 200 variables per pipeline.
* Each name must be 100 characters or less.
* Each `string` variable value must be less than 2048 characters.
* Each `secretString` type variable value must be 500 characters or less.

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
