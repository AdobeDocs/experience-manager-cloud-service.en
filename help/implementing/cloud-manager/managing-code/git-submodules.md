---
title: Git Submodule Support
description: Learn how you can use Git submodules to merge the content of multiple branches across Git repositories at build time.
exl-id: fa5b0f49-4b87-4f39-ad50-7e62094d85f4
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Git submodule support for Adobe repositories {#git-submodule-support}

Git submodules can be used to merge the content of multiple branches across Git repositories at build time.

When Cloud Manager's build process runs, it clones the pipeline's repository and checks out the branch. If a `.gitmodules` file exists in the branch's root directory, the corresponding command is executed.

The following command checks out each submodule into the appropriate directory. 

```
$ git submodule update --init
```

This technique offers an alternative to the solution described in [Working with Multiple Source Git Repositories](/help/implementing/cloud-manager/managing-code/working-with-multiple-source-git-repositories.md). It is ideal for organizations comfortable with Git submodules and preferring not to manage an external merging process.

For example, suppose that there are three repositories. Each repository contains a single branch named `main`. In the primary repository, that is, the one configured in the pipelines, the `main` branch has a `pom.xml` file declaring the projects contained in the other two repositories:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="https://maven.apache.org/POM/4.0.0" xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="https://maven.apache.org/POM/4.0.0 https://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
   
    <groupId>customer.group.id</groupId>
    <artifactId>customer-reactor</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>pom</packaging>
   
    <modules>
        <module>project-a</module>
        <module>project-b</module>
    </modules>
   
</project>
```

You would then add submodules for the other two repositories:

```shell
$ git submodule add -b main https://git.cloudmanager.adobe.com/ProgramName/projectA/ project-a
$ git submodule add -b main https://git.cloudmanager.adobe.com/ProgramName/projectB/ project-b
```

The result is a `.gitmodules` file similar to the following:

```text
[submodule "project-a"]
    path = project-a
    url = https://git.cloudmanager.adobe.com/ProgramName/projectA/
    branch = main
[submodule "project-b"]
    path = project-b
    url = https://git.cloudmanager.adobe.com/ProgramName/projectB/
    branch = main
```

See also the [Git Reference Manual](https://git-scm.com/book/en/v2/Git-Tools-Submodules) for more information on Git submodules.

## Limitations and recommendations {#limitations-recommendations}

When using Git submodules with Adobe-managed repositories, be aware of the following limitations.

* The Git URL must be exactly in the syntax described in the previous section.
* Only submodules at the root of the branch are supported.
* For security reasons, do not embed credentials in Git URLs.
* Unless otherwise necessary, Adobe recommends that you use shallow submodules by running the following:
  `git config -f .gitmodules submodule.<submodule path>.shallow true` for each submodule.
* Git submodule references are stored to specific Git commits. As a result, when changes to the submodule repository are made, the commit referenced must be updated.
  For example, by using the following: 
  
  `git submodule update --remote`

## Git submodule support for private repositories {#private-repositories}

Support for Git submodules in [private repositories](private-repositories.md) is generally similar to their use with Adobe repositories.

However, after configuring your `pom.xml` file and executing the `git submodule` commands, you must add a `.gitmodules` file to the root directory of the aggregator repository for Cloud Manager to recognize the submodule configuration.

![.gitmodules file](assets/gitmodules.png)

![Aggregator](assets/aggregator.png)

### Limitations and recommendations {#limitations-recommendations-private-repos}

When using Git submodules with private repositories, keep the following limitations in mind:

* Submodule Git URLs can be in HTTPS or SSH format, but must point to a GitHub.com repository. Adding an Adobe repository submodule to a GitHub aggregator repository or the reverse is not supported.
* GitHub submodules must be accessible by the Adobe GitHub App.
* [The limitations of using Git submodules with Adobe-managed repositories](#limitations-recommendations) also apply.
