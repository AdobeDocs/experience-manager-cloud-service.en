---
title: Git Submodule Support
description: Learn how you can use Git submodules to merge the content of multiple branches across git repositories at build time.
exl-id: fa5b0f49-4b87-4f39-ad50-7e62094d85f4
feature: "Cloud Manager, Developing"
role: "Admin, Architect, Developer"
---
# Git Submodule Support for Adobe Repositories {#git-submodule-support}

Git submodules can be used to merge the content of multiple branches across git repositories at build time.

When Cloud Manager's build process executes, after the repository configured for the pipeline is cloned and the configured branch is checked out, if the branch contains a `.gitmodules` file in the root directory, the command is executed.

The following command will check out each submodule into the appropriate directory. 

```
$ git submodule update --init
```

This technique is a potential alternative to the solution described in the document [Working with Multiple Source Git Repositories](/help/implementing/cloud-manager/managing-code/working-with-multiple-source-git-repositories.md) for organizations which are comfortable with using git submodules and do not want to manage an external merging process.

For example, let's say there are three repositories, each containing a single branch named `main`. In the primary repository, that is, the one configured in the pipelines, the `main` branch has a `pom.xml` file declaring the projects contained in the other two repositories.

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

You would then add submodules for the other two repositories.

```shell
$ git submodule add -b main https://git.cloudmanager.adobe.com/ProgramName/projectA/ project-a
$ git submodule add -b main https://git.cloudmanager.adobe.com/ProgramName/projectB/ project-b
```

This results in a `.gitmodules` file similar to the following.

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

More information on git submodules can be found in the [Git Reference Manual.](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

### Limitations and Recommendations {#limitations-recommendations}

When using git submodules with Adobe-managed repositories, be aware of the following limitations.

* The git URL must be exactly in the syntax described in the previous section.
* Only submodules at the root of the branch are supported.
* For security reasons, do not embed credentials in git URLs.
* Unless otherwise necessary, it is highly recommended to use shallow submodules.
  * To do this, run `git config -f .gitmodules submodule.<submodule path>.shallow true` for each submodule.
* Git submodule references are stored to specific git commits. As a result, when changes to the submodule repository are made, the commit referenced must be updated.
  * For example, by using `git submodule update --remote`

## Git Submodule Support for Private Repositories {#private-repositories}

Support for git submodules when using [private repositories](private-repositories.md) is largely the same as when using Adobe repositories.

However, after setting up your `pom.xml` file and running the `git submodule` commands, you must add a `.gitmodules` file to the root directory of the aggregator repository for Cloud Manager to detect the submodule setup.

![.gitmodules file](assets/gitmodules.png)

![Aggregator](assets/aggregator.png)

### Limitations and Recommendations {#limitations-recommendations-private-repos}

When using git submodules with private repositories, be aware of the following limitations.

* The git URLs for the submodules can either be in the HTTPS or SSH format, but they must link to a github.com repository
   * Adding an Adobe repository submodule to a GitHub aggregator repository or vice-versa won't work.
* The GitHub submodules must be accessible to the Adobe GitHub App.
* [The limitations of using git submodules with Adobe-managed repositories](#limitations-recommendations) also apply.
