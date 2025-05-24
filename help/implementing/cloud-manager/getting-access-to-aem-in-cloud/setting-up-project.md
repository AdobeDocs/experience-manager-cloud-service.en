---
title: Project Setup
description: Learn how AEM Projects are built with Maven and the standards you must observe when creating your own project.
exl-id: 76af0171-8ed5-4fc7-b5d5-7da5a1a06fa8
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Project setup {#project-setup}

Learn how AEM Projects are built with Maven and the standards you must observe when creating your own project.

## Project setup details {#project-setup-details}

To build and deploy successfully with Cloud Manager, AEM Projects need to adhere to the following guidelines:

* Projects must be built using [Apache Maven](https://maven.apache.org).
* There must be a `pom.xml` file in the root of the git repository. This `pom.xml` file can refer to as many sub-modules (which in turn may have other sub-modules, and so on) as necessary.
* You can add references to additional Maven artifact repositories in your `pom.xml` files. Access to [password-protected artifact repositories](#password-protected-maven-repositories) is supported when configured. However, access to network-protected artifact repositories is not supported.
* Deployable content packages are discovered by scanning for content package `.zip` files, which are contained in a directory named `target`. Any number of sub-modules may produce content packages.
* Deployable Dispatcher artifacts are discovered by scanning for `.zip` files (also contained in the directory named `target`), which have directories named `conf` and `conf.d`.
* If there is more than one content package, the ordering of package deployments is not guaranteed. Should a specific order be needed, content package dependencies can be used to define the order.
* Packages may be [skipped](#skipping-content-packages) during deployment.

## Activating Maven profiles in Cloud Manager {#activating-maven-profiles-in-cloud-manager}

In some limited cases, you may need to vary your build process slightly when running inside Cloud Manager as opposed to when running on developer workstations. For these cases, [Maven profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html) can be used to define how the build should be different in different environments, including Cloud Manager.

Activation of a Maven profile inside the Cloud Manager build environment should be done by looking for the `CM_BUILD` [environment variable](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md). Likewise, a profile intended to be used only outside of the Cloud Manager build environment should be done by looking for the absence of this variable.

For example, if you wanted to output a simple message only when the build is run inside Cloud Manager, you would do the following:

```xml
        <profile>
            <id>cmBuild</id>
            <activation>
                  <property>
                        <name>env.CM_BUILD</name>
                  </property>
            </activation>
            <build>
                <plugins>
                    <plugin>
                        <artifactId>maven-antrun-plugin</artifactId>
                        <version>1.8</version>
                        <executions>
                            <execution>
                                <phase>initialize</phase>
                                <configuration>
                                    <target>
                                        <echo>I'm running inside Cloud Manager!</echo>
                                    </target>
                                </configuration>
                                <goals>
                                    <goal>run</goal>
                                </goals>
                            </execution>
                        </executions>
                    </plugin>
                </plugins>
            </build>
        </profile>
```

>[!NOTE]
>
>To test this profile on a developer workstation, you can either enable it on the command line (with `-PcmBuild`) or in your integrated development environment (IDE).

And if you wanted to output a simple message only when the build is run outside of Cloud Manager, you would do the following:

```xml
        <profile>
            <id>notCMBuild</id>
            <activation>
                  <property>
                        <name>!env.CM_BUILD</name>
                  </property>
            </activation>
            <build>
                <plugins>
                    <plugin>
                        <artifactId>maven-antrun-plugin</artifactId>
                        <version>1.8</version>
                        <executions>
                            <execution>
                                <phase>initialize</phase>
                                <configuration>
                                    <target>
                                        <echo>I'm running outside Cloud Manager!</echo>
                                    </target>
                                </configuration>
                                <goals>
                                    <goal>run</goal>
                                </goals>
                            </execution>
                        </executions>
                    </plugin>
                </plugins>
            </build>
        </profile>
```

## Use a password-protected Maven repository within Cloud Manager {#password-protected-maven-repositories}

>[!NOTE]
>
>Deploy artifacts from password-protected Maven repositories cautiously, as Cloud Manager does not evaluate this code with its [code quality rules](/help/implementing/cloud-manager/custom-code-quality-rules.md). This method should be reserved for rare situations and applied only to code unrelated to AEM. Adobe advises including both the Java sources and the entire project source code along with the binary. Doing so ensures greater transparency and maintainability throughout the deployment process.

**To use a password-protected Maven repository within Cloud Manager:**

1. Specify the password (and optionally, the username) as a secret [pipeline variable](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md).
1. Then reference that secret inside a file named `.cloudmanager/maven/settings.xml` in the git repository, which follows the [Maven Settings File](https://maven.apache.org/settings.html) schema. 

When the Cloud Manager build process starts:

* The `<servers>` element in this file is merged into the default `settings.xml` file provided by Cloud Manager.
  * Server IDs starting with `adobe` and `cloud-manager` are considered reserved. Do not use them on custom servers.
  * Cloud Manager mirrors only those server IDs that match specific prefixes or the default ID `central`; all other server IDs are excluded from mirroring.
* With this file in place, the server ID would be referenced from inside a `<repository>` and/or `<pluginRepository>` element inside the `pom.xml` file.
* Generally, these `<repository>` and `<pluginRepository>` elements are included within a [Cloud Manager-specific profile](#activating-maven-profiles-in-cloud-manager), though their inclusion is not strictly required.

As an example, let's say that the repository is at `https://repository.myco.com/maven2`, the username Cloud Manager should use is `cloudmanager`, and the password is `secretword`. You would take the following steps:

1. Set the password as a secret in the pipeline.

   ```text
   $ aio cloudmanager:set-pipeline-variables PIPELINEID --secret CUSTOM_MYCO_REPOSITORY_PASSWORD secretword`
   ```

1. Reference this secret from the `.cloudmanager/maven/settings.xml` file in the following:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <settings xmlns="https://maven.apache.org/SETTINGS/1.0.0" xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="https://maven.apache.org/SETTINGS/1.0.0 https://maven.apache.org/xsd/settings-1.0.0.xsd">
       <servers>
           <server>
               <id>myco-repository</id>
               <username>cloudmanager</username>
              <password>${env.CUSTOM_MYCO_REPOSITORY_PASSWORD}</password>
           </server>
       </servers>
   </settings>
   ```

1. Finally reference the server id inside the `pom.xml` file:

   ```xml
   <profiles>
       <profile>
           <id>cmBuild</id>
           <activation>
                   <property>
                       <name>env.CM_BUILD</name>
                   </property>
           </activation>
           <repositories>
                <repository>
                    <id>myco-repository</id>
                    <name>MyCo Releases</name>
                    <url>https://repository.myco.com/maven2</url>
                    <snapshots>
                        <enabled>false</enabled>
                    </snapshots>
                    <releases>
                        <enabled>true</enabled>
                    </releases>
                </repository>
            </repositories>
            <pluginRepositories>
                <pluginRepository>
                    <id>myco-repository</id>
                    <name>MyCo Releases</name>
                    <url>https://repository.myco.com/maven2</url>
                    <snapshots>
                        <enabled>false</enabled>
                    </snapshots>
                    <releases>
                        <enabled>true</enabled>
                    </releases>
                </pluginRepository>
            </pluginRepositories>
       </profile>
   </profiles>
   ```

### Deploy sources {#deploying-sources}

It is a good practice to deploy the Java sources alongside with the binary to a Maven repository. 
 
To do so, configure the maven-source-plugin in your project.

```xml
         <plugin>
             <groupId>org.apache.maven.plugins</groupId>
             <artifactId>maven-source-plugin</artifactId>
             <executions>
                 <execution>
                     <id>attach-sources</id>
                     <goals>
                         <goal>jar-no-fork</goal>
                     </goals>
                 </execution>
             </executions>
         </plugin>
```

### Deploying Project Sources {#deploying-project-sources}

It is a good practice to deploy the whole project source alongside with the binary to a Maven repository. Doing so allows it to rebuild the exact artifact. 
 
Configure the maven-assembly-plugin in your project in the following manner:

```xml
         <plugin>
             <groupId>org.apache.maven.plugins</groupId>
             <artifactId>maven-assembly-plugin</artifactId>
             <executions>
                 <execution>
                     <id>project-assembly</id>
                     <phase>package</phase>
                     <goals>
                         <goal>single</goal>
                     </goals>
                     <configuration>
                         <descriptorRefs>
                             <descriptorRef>project</descriptorRef>
                         </descriptorRefs>
                     </configuration>
                 </execution>
             </executions>
         </plugin>
```

## Skipping Content Packages {#skipping-content-packages}

In Cloud Manager, builds may produce any number of content packages. For a variety of reasons, it may be desirable to produce a content package but not deploy it. An example occurs when content packages are built solely for testing purposes or when another step in the build process repackages them. That is, a sub-package of another package. 

To accommodate these scenarios, Cloud Manager looks for a property named `cloudManagerTarget` in the properties of built content packages. If this property is set to `none`, the package is skipped and not deployed. 

The mechanism to set this property depends upon the way the build produces the content package. For example, with the `filevault-maven-plugin` you would configure the plugin as follows.

```xml
        <plugin>
            <groupId>org.apache.jackrabbit</groupId>
            <artifactId>filevault-package-maven-plugin</artifactId>
            <extensions>true</extensions>
            <configuration>
                <properties>
                    <cloudManagerTarget>none</cloudManagerTarget>
                </properties>
        <!-- other configuration -->
            </configuration>
        </plugin>
```

The `content-package-maven-plugin` has a similar configuration.

```xml
        <plugin>
            <groupId>com.day.jcr.vault</groupId>
            <artifactId>content-package-maven-plugin</artifactId>
            <extensions>true</extensions>
            <configuration>
                <properties>
                    <cloudManagerTarget>none</cloudManagerTarget>
                </properties>
        <!-- other configuration -->
            </configuration>
        </plugin>
```

## Build Artifact Reuse {#build-artifact-reuse}

In many cases, the same code is deployed to multiple AEM environments. Where possible, Cloud Manager avoids rebuilding the code base when it detects that the same git commit is used in multiple full-stack pipeline executions.

When an execution is started, the current HEAD commit for the branch pipeline is extracted. The commit hash is visible in the UI and via the API. When the build step completes successfully, the resulting artifacts are stored based on that commit hash and may be reused in subsequent pipeline executions.

Packages are reused across pipelines if they are in the same program. When looking for packages that can be reused, AEM disregards branches and reuses artifacts across branches.

When a reuse occurs, the build and code quality steps are effectively replaced with the results from the original execution. The log file for the build step lists the artifacts and the execution information that was used to build them originally.

The following is an example of such log output.

```shell
The following build artifacts were reused from the prior execution 4 of pipeline 1 which used commit f6ac5e6943ba8bce8804086241ba28bd94909aef:
build/aem-guides-wknd.all-2021.1216.1101633.0000884042.zip (content-package)
build/aem-guides-wknd.dispatcher.cloud-2021.1216.1101633.0000884042.zip (dispatcher-configuration)
```

The log of the code quality step contains similar information.

### Examples {#example-reuse}

#### Example 1 {#example-1}

Consider that your program has two development pipelines:

* Pipeline 1 on branch `foo`
* Pipeline 2 on branch `bar`

Both branches are on the same commit ID.

1. Running Pipeline 1 first builds the packages normally.
1. Then, running Pipeline 2 reuses the packages created by Pipeline 1.

#### Example 2 {#example-2}

Consider that your program has two branches:

* Branch `foo`
* Branch `bar`

Both branches have the same commit ID.

1. A development pipeline builds and executes `foo`.
1. Subsequently, a production pipeline builds and executes `bar`.

In this case, the artifact from `foo` is reused for the production pipeline since the same commit hash was identified.

### Opting Out {#opting-out}

If desired, the reuse behavior can be disabled for specific pipelines by setting the pipeline variable `CM_DISABLE_BUILD_REUSE` to `true`. If this variable is set, the system extracts the commit hash and stores the resulting artifacts for later use but skips reusing any previously stored artifacts. To understand this behavior, consider the following scenario:

1. A new pipeline is created.
1. The pipeline is executed (execution #1) and the current HEAD commit is `becdddb`. The execution is successful and the resulting artifacts are stored.
1. The `CM_DISABLE_BUILD_REUSE` variable is set.
1. The pipeline is re-executed without changing code. Although there are stored artifacts associated with `becdddb`, they are not reused due to the `CM_DISABLE_BUILD_REUSE` variable.
1. The code is changed and the pipeline is executed. The HEAD commit is now `f6ac5e6`. The execution is successful and the resulting artifacts are stored.
1. The `CM_DISABLE_BUILD_REUSE` variable is deleted.
1. The pipeline is re-executed without changing the code. Since there are stored artifacts associated with `f6ac5e6`, those artifacts are reused.

### Caveats {#caveats}

* Build artifacts are not reused across different programs, regardless if the commit hash is identical.
* Build artifacts are reused within the same program even if the branch and/or pipeline is different.
* [Maven version handling](/help/implementing/cloud-manager/managing-code/project-version-handling.md) replaces the project version only in production pipelines.
    If the same commit is used for both a development deploy and production pipeline, and the development deploy runs first, the versions are deployed to stage and production unchanged. However, a tag is still created in this case.
* If the retrieval of the stored artifacts is not successful, the build step is run as if no artifacts were stored.
* Pipeline variables other than `CM_DISABLE_BUILD_REUSE` are not considered when Cloud Manager decides to reuse previously created build artifacts.
