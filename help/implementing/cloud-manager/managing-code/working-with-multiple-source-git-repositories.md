---
title: Use Multiple Repositories
description: Learn how to manage multiple Git repositories when working with Cloud Manager.
exl-id: 1b9cca36-c2d7-4f9e-9733-3f1f4f8b2c7a
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Use multiple repositories {#working-with-multiple-source-git-repos} 

Learn how to manage multiple Git repositories when working with Cloud Manager.

## Sync private Git repositories {#syncing-customer-managed-git-repositories}

Instead of directly working with Cloud Manager's Git repository, [customers can work with their own private Git repository](integrating-with-git.md) or multiple own Git repositories. In these cases, set up an automated synchronization process to ensure that the Git repository in Cloud Manager is always kept up-to-date.

Depending on where the customer's Git repository is hosted, a GitHub action or a continuous integration solution like Jenkins could be used to set up the automation. With an automation in place, every push to a customer-owned Git repository can be automatically forwarded to Cloud Manager's Git repository.

While such an automation for a single customer-owned Git repository is straight forward, configuring it for multiple repositories requires an initial setup. The contents from multiple Git repositories must be mapped to different directories within the single Cloud Manager Git repository. Cloud Manager's Git repository must be provisioned with a root Maven `pom.xml`, listing the different subprojects in the modules section.

The following is a sample `pom.xml` file for two customer-owned Git repositories.

* The first project is put into the directory named `project-a`.
* The second project is put into the directory named `project-b`.

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

Such a root `pom.xml` is pushed to a branch in Cloud Manager's Git repository. Then, the two projects must be set up to forward changes automatically to Cloud Manager's Git repository. 

A possible solution would be the following.

1. Trigger a GitHub action by pushing to a branch in project A.
1. The action checks out project A and the Cloud Manager Git repository. Then it copies all contents of project A to the `project-a` directory in Cloud Manager's Git repository.
1. Then the action commits-pushes the change.

For example, a change on the main branch in project A is automatically pushed to the main branch in Cloud Manager's Git repository. There could be a mapping between branches like a push to a branch named `dev` in project A is pushed to a branch named `development` in Cloud Manager's Git repository. Similar steps are required for project B.

Depending on the branching strategy and workflows, the syncing can be configured for different branches. If the used Git repository does not provide a concept similar to GitHub actions, an integration by way of Jenkins (or similar) is possible as well. In this case, a webhook triggers a Jenkins job, which does the work.

Follow these steps so you can add a new, third source or repository.

1. Add a GitHub action to the new repository, which pushes changes from that repository to Cloud Manager's Git repository.
1. Perform that action at least once to ensure that project code is in Cloud Manager's Git repository.
1. In the Cloud Manager Git repository, add a reference to the new directory in the root Maven `pom.xml`.



## Sample GitHub action {#sample-github-action}

The following is a sample GitHub action triggered by a push to the main branch. Then pushing into a subdirectory of Cloud Manager's Git repository. The GitHub actions must be provided with two secrets, `MAIN_USER` and `MAIN_PASSWORD`, to be able to connect and push to Cloud Manager's Git repository.

```java
name: SYNC
env:
  # Username/email used to commit to Cloud Manager's Git repository
  USER_NAME: <NAME>
  USER_EMAIL: <EMAIL>
  # Directory within the Cloud Manager Git repository
  PROJECT_DIR: project-a
  # Cloud Manager's Git repository
  MAIN_REPOSITORY: https://$MAIN_USER:$MAIN_PASSWORD@git.cloudmanager.adobe.com/<PATH>
  # The branch in Cloud Manager's Git repository to push to
  MAIN_BRANCH : <BRANCH_NAME>
 
# Only run on a push to this branch
on:
  push:
     branches: [ main ]
 
jobs:
  build:
    runs-on: ubuntu-latest
 
    steps:
      # Checkout this project into a sub folder
      - uses: actions/checkout@v2
        with:
          path: sub
      # Cleanup sub project
      - name: Clean project
        run: |
          git -C sub log --format="%an : %s" -n 1 > commit.txt
          rm -rf sub/.git
          rm -rf sub/.github
      # Set global git configuration
      - name: Set git config
        run: |
          git config --global credential.helper cache
          git config --global user.email ${USER_EMAIL}
          git config --global user.name ${USER_NAME}
      # Checkout the main project
      - name: Checkout main project
        run:
          git clone -b ${MAIN_BRANCH} ${MAIN_REPOSITORY} ${MAIN_BRANCH} 
      # Move sub project
      - name: Move project to main project
        run: |
          rm -rf ${MAIN_BRANCH}/${PROJECT_DIR} 
          mv sub ${MAIN_BRANCH}/${PROJECT_DIR}
      - name: Commit Changes
        run: |
          git -C ${MAIN_BRANCH} add -f ${PROJECT_DIR}
          git -C ${MAIN_BRANCH} commit -F ../commit.txt
          git -C ${MAIN_BRANCH} push
```

Using a GitHub action is flexible. Any mapping between branches of the Git repositories can be performed and any mapping of the separate Git projects into the directory layout of the main project.

>[!NOTE]
>
>The sample script uses `git add` to update the repository. The script assumes that removals are included. Depending on the default configuration of Git, it must be replaced with `git add --all`.

## Sample Jenkins job {#sample-jenkins-job}

The following is a sample script that can be used in a Jenkins job or similar and has the following flow:

1. It gets triggered by a change in a Git repository.
1. The Jenkins job checks out the latest state of that project or branch.
1. The job then triggers this script.
1. This script in turn checks out Cloud Manager's Git repository and commits the project code to a subdirectory.

The Jenkins job must be provided with two secrets, `MAIN_USER` and `MAIN_PASSWORD`, to be able to connect and push to Cloud Manager's Git repository.

```java
# Username/email used to commit to Cloud Manager's Git repository
export USER_NAME=<NAME>
export USER_EMAIL=<EMAIL>
# Directory within the Cloud Manager Git repository
export PROJECT_DIR=project-a
# Cloud Manager's Git repository
export MAIN_REPOSITORY=https://$MAIN_USER:$MAIN_PASSWORD@git.cloudmanager.adobe.com/<PATH>
# The branch in Cloud Manager's Git repository to push to
export MAIN_BRANCH=<BRANCH_NAME>
 
# clean up and init
rm -rf target
mkdir target
 
# mv project to sub folder
mkdir target/sub
for f in .* *
do
    if [ "$f" != "." -a "$f" != ".." -a "$f" != "target" ]
    then
        mv "$f" target/sub
    fi
done
cd target
 
# capture log and remove git info
cd sub
git log --format="%an : %s" -n 1 > ../commit.txt
rm -rf .git
rm -rf .github
cd ..
 
# checkout main repository
git clone -b $MAIN_BRANCH $MAIN_REPOSITORY main
cd main
 
# configure main repository
git config credential.helper cache
git config user.email $USER_EMAIL
git config user.name $USER_NAME
 
# update project in main
rm -rf $PROJECT_DIR
mv ../sub $PROJECT_DIR
 
# commit changes to main
git add -f $PROJECT_DIR
git commit -F ../commit.txt
git push
```

Using a Jenkins job is flexible. Any mapping between branches of the Git repositories can be performed and any mapping of the separate Git projects into the directory layout of the main project.

>[!NOTE]
>
>The sample script uses `git add` to update the repository. The script assumes that removals are included. Depending on the default configuration of Git, it must be replaced with `git add --all`.
