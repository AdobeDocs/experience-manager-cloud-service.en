---
title: Cloud Manager Repositories
description: Learn how to create, view, and delete your git repositories in Cloud Manager.
exl-id: 6e1cf636-78f5-4270-9a21-38b4d5e5a0b0
---

# Cloud Manager Repositories {#cloud-manager-repos} 

Learn how to create, view, and delete your git repositories in Cloud Manager.

>[!NOTE]
>
>There is a limit of 300 repositories across all programs in any given company or IMS organization.

## Adding and and Managing Repositories {#add-manage-repos}

Follow these steps view and manage repositories in Cloud Manager.

1. From the **Program Overview** page, click on **Repositories** tab and navigate to the **Repositories** page.

1. Click on **Add Repository** to start the wizard.

   ![Add repository button](/help/implementing/cloud-manager/assets/repos/create-repo2.png)
  
1. Enter the name and description as requested and click **Save**.

   ![Add Repository dialog](/help/implementing/cloud-manager/assets/repos/repo-1.png)

When the wizard closes, your new repository will be displayed in the table.

You can select the repository in the table and click on the ellipsis button and select **Copy Repository URL**, **View &amp; Update**, or **Delete**.

![Repository options](/help/implementing/cloud-manager/assets/repos/create-repo3.png)

Repositories created in Cloud Manager will also be available for you to select when adding or editing pipelines. Please refer to the document [CI-CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) to learn more.

There is a single primary repository or a branch for any given pipeline. With [git submodule support](#git-submodule-support), many secondary branches can be included at build time.

>[!NOTE]
>
>A user must have the role **Deployment Manager** or **Business Owner** to be able to add a repository.

## Deleting a Repository {#delete-repo}

Deleting a repository will:

* Make the deleted repository name unusable for new repositories that may be created in the future.
   * The error message `Repository name should be unique within organization.` will be shown in such cases.
* Make the deleted repository unavailable in Cloud Manager and unavailable for linking to a pipeline.

Follow these to delete a repository in Cloud Manager.

1. From the **Program Overview** page, click on **Repositories** tab and navigate to the **Repositories** page.

1. Select the repository and click on the ellipsis button and select **Delete** to delete the repository.

   ![Delete repository](/help/implementing/cloud-manager/assets/repos/delete-repo.png)

## Git Submodule Support {#git-submodule-support}

Git submodules can be used to merge the content of multiple branches across git repositories at build time.

When Cloud Manager's build process executes, after the repository configured for the pipeline is cloned and the configured branch is checked out, if the branch contains a `.gitmodules` file in the root directory, the command is executed.

The following command will check out each submodule into the appropriate directory. 

```
$ git submodule update --init
```

This technique is a potential alternative to the solution described in the document [Working with Multiple Source Git Repositories](/help/implementing/cloud-manager/managing-code/working-with-multiple-source-git-repositories.md) for organizations which are comfortable with using git submodules and do not want to manage an external merging process.

For example, let's say there are three repositories, each containing a single branch named `main`. In the primary repository, i.e. the one configured in the pipelines, the `main` branch has a `pom.xml` file declaring the projects contained in the other two repositories.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
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

When using git submodules, please be aware of the following limitations.

* The git URL must be exactly in the syntax described in the previous section.
* Only submodules at the root of the branch are supported.
* For security reasons, do not embed credentials in git URLs.
* Unless otherwise necessary, it is highly recommended to use shallow submodules.
  * To do this, run `git config -f .gitmodules submodule.<submodule path>.shallow true` for each submodule.
* Git submodule references are stored to specific git commits. As a result, when changes to the submodule repository are made, the commit referenced needs to be updated.
  * For example, by using `git submodule update --remote`
