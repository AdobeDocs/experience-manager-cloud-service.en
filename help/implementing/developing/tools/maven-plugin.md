---
title: Adobe Content Package Maven Plugin
description: Use the Content Package Maven plugin to deploy AEM applications
exl-id: d631d6df-7507-4752-862b-9094af9759a0
feature: Developing
role: Admin, Architect, Developer
---
# Adobe Content Package Maven Plugin {#adobe-content-package-maven-plugin}

Use the Adobe Content Package Maven plugin to integrate package deployment and management tasks into your Maven projects.

The deployment of the constructed packages to AEM is performed by the Adobe Content Package Maven plugin and enables the automation of tasks normally performed using AEM [Package Manager](/help/implementing/developing/tools/package-manager.md)

* Create new packages from files in the file system.
* Install and uninstall packages on AEM.
* Build packages that are already defined on AEM.
* Obtain a list of packages that are installed on AEM.
* Remove a package from AEM.

This document details how to use the Maven to manage these tasks. However it is also important to understand [how AEM projects and their packages are structured](#aem-project-structure).

>[!NOTE]
>
>Please always use the latest available versions of these plugins.

>[!NOTE]
>
>Package **creation** is now owned by the [Apache Jackrabbit FileVault Package Maven plugin](https://jackrabbit.apache.org/filevault-package-maven-plugin/).
>
>This article describes the **deployment** of the constructed packages to AEM as performed by the Adobe Content Package Maven plugin.

## Packages and the AEM Project Structure {#aem-project-structure}

AEM as a Cloud Service adheres to the latest best practices for package management and project structure as implemented by the latest AEM Project Archetype.

>[!TIP]
>
>See the [AEM Project Structure](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-project-content-package-structure.html) article in the AEM as a Cloud Service documentation and the [AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html) documentation. Both of which are fully supported for AEM 6.5.

## Obtaining the Content Package Maven Plugin {#obtaining-the-content-package-maven-plugin}

The plugin is available from the [Maven Central Repository](https://mvnrepository.com/artifact/com.day.jcr.vault/content-package-maven-plugin?repo=adobe-public).

## Content Package Maven Plugin Goals and Parameters

To use the Content Package Maven Plugin, add the following plugin element inside the build element of your POM file:

```xml
<plugin>
 <groupId>com.day.jcr.vault</groupId>
 <artifactId>content-package-maven-plugin</artifactId>
 <version>1.0.4</version>
 <configuration>
       <!-- parameters and values common to all goals, as required -->
 </configuration>
</plugin>
```

To enable Maven to download the plugin, use the profile provided in the [Obtaining the Content Package Maven Plugin](#obtaining-the-content-package-maven-plugin) section on this page.

## Goals of the Content Package Maven Plugin {#goals-of-the-content-package-maven-plugin}

The goals and goal parameters that the Content Package plugin provides are described in the sections that follow. Parameters that are described in the Common Parameters section can be used for most of the goals. Parameters that apply to one goal are described in the section for that goal.

### Plugin Prefix {#plugin-prefix}

The plugin prefix is `content-package`. Use this prefix to execute a goal from the command line, as in the following example:

```shell
mvn content-package:build
```

### Parameter Prefix {#parameter-prefix}

Unless otherwise noted, the plugin goals and parameters use the `vault` prefix, as in the following example:

```shell
mvn content-package:install -Dvault.targetURL="https://192.168.1.100:4502/crx/packmgr/service.jsp"
```

### Proxies {#proxies}

Goals that use proxies for AEM use the first valid proxy configuration found in the Maven settings. If no proxy configuration is found, no proxy is used. See the `useProxy` parameter in the [Common Parameters](#common-parameters) section.

### Common Parameters {#common-parameters}

The parameters in the following table are common to all goals except when noted in the **Goals** column.

|Name|Type|Required|Default Value|Description|Goals|
|---|---|---|---|---|---|
|`failOnError`|`boolean`|No|`false`|A value of `true` causes the build to fail when an error occurs. A value of `false` causes the build to ignore the error.|All goals except `package`|
|`name`|`String`|`build`: Yes, `install`: No, `rm`: Yes|`build`: No default, `install`: The value of the `artifactId` property of the Maven project|The name of the package to act on|All goals except `ls`|
|`password`|`String`|Yes|`admin`|The password used for authentication with AEM|All goals except `package`|
|`serverId`|`String`|No|The server ID from which to retrieve the user name and password for authentication|All goals except `package`|
|`targetURL`|`String`|Yes|`http://localhost:4502/crx/packmgr/service.jsp`|The URL of the HTTP service API of the AEM package manager|All goals except `package`|
|`timeout`|`int`|No|`5`|The connection timeout for communicating with the package manager service, in seconds|All goals except `package`|
|`useProxy`|`boolean`|No|`true`|A value of `true` causes Maven to use the first active proxy configuration found to proxy requests to the Package Manager.|All goals except `package`|
|`userId`|`String`|Yes|`admin`|The user name to authenticate with AEM|All goals except `package`|
|`verbose`|`boolean`|No|`false`|Enables or disables verbose logging|All goals except `package`|

### build {#build}

Builds a content package that is already defined on an AEM instance.

>[!NOTE]
>
>This goal does not need to be executed within a Maven project.

#### Parameters {#parameters}

All parameters for the build goal are described in the [Common Parameters](#common-parameters) section.

### install {#install}

Installs a package in the repository. Execution of this goal does not require a Maven project. The goal is bound to the `install` phase of the Maven build lifecycle.

#### Parameters {#parameters-1}

In addition to the following parameters, see the descriptions in the [Common Parameters](#common-parameters) section.

|Name|Type|Required|Default Value|Description|
|---|---|---|---|---|
|`artifact`|`String`|No|The value of the `artifactId` property of the Maven project|A string of the form `groupId:artifactId:version[:packaging]`|
|`artifactId`|`String`|No|None|The ID of the artifact to install|
|`groupId`|`String`|No|None|The `groupId` of the artifact to install|
|`install`|`boolean`|No|`true`|Determines whether to unpack the package automatically when it is uploaded|
|`localRepository`|`org.apache.maven.artifact.repository.ArtifactRepository`|No|The value of the `localRepository` system variable|The local Maven repository which cannot be configured using the plugin configuration as the system property is always used|
|`packageFile`|`java.io.File`|No|The primary artifact that is defined for the Maven project|The name of the package file to install|
|`packaging`|`String`|No|`zip`|The type of packaging of the artifact to install|
|`pomRemoteRepositories`|`java.util.List`|Yes|The value of the `remoteArtifactRepositories` property that is defined for the Maven project|This value cannot be configured using the plugin configuration and must be specified in the project.|
|`project`|`org.apache.maven.project.MavenProject`|Yes|The project for which the plugin is configured|The Maven project which is implicit because the project contains the plugin configuration|
|`repositoryId` (POM), `repoID` (command line)|`String`|No|`temp`|The ID of the repository from which the artifact is retrieved|
|`repositoryUrl` (POM), `repoURL` (command line)|`String`|No|None|The URL of the repository from which the artifact is retrieved|
|version|String|No|None|The version of the artifact to install|

### ls {#ls}

Lists the packages that are deployed to [Package Manager](/help/implementing/developing/tools/package-manager.md).

#### Parameters {#parameters-2}

All parameters of the ls goal are described in the [Common Parameters](#common-parameters) section.

### rm {#rm}

Removes a package from [Package Manager](/help/implementing/developing/tools/package-manager.md).

#### Parameters {#parameters-3}

All parameters of the rm goal are described in the [Common Parameters](#common-parameters) section.

### uninstall {#uninstall}

Uninstalls a package. The package remains on the server in the uninstalled state.

#### Parameters {#parameters-4}

All parameters of the uninstall goal are described in the [Common Parameters](#common-parameters) section.


### help {#help}

#### Parameters {#parameters-6}

| Name |Type |Required |Default Value |Description |
|---|---|---|---|---|
|`detail`|`boolean`|No|`false`|Determines whether to display all settable properties for each goal|
|`goal`|`String`|No|None|This parameters defines the name of the goal for which to show help. If no value is specified, help for all goals is displayed.|
|`indentSize`|`int`|No|`2`|The number of spaces to use for the indentation of each level (must be positive if defined)|
|`lineLength`|`int`|No|`80`|The maximum length of a display line (must be positive if defined)|

## Including a Thumbnail Image or Properties File in the Package {#including-a-thumbnail-image-or-properties-file-in-the-package}

Replace the default package configuration files to customize the package properties. For example, include a thumbnail image to distinguish the package in [Package Manager](/help/implementing/developing/tools/package-manager.md).

The source files can be located anywhere in your file system. In the POM file, define build resources to copy the source files to the `target/vault-work/META-INF` for inclusion in the package.

The following POM code adds the files in the `META-INF` folder of the project source to the package:

```xml
<build>
    <resources>
        <!-- vault META-INF resources (thumbnail and so on) -->
        <resource>
            <directory>${basedir}/src/main/content/META-INF</directory>
            <targetPath>../vault-work/META-INF</targetPath>
        </resource>
    </resources>
</build>
```

The following POM code adds only a thumbnail image to the package. The thumbnail image must be named `thumbnail.png`, and must be located in the `META-INF/vault/definition` folder of the package. In this example, the source file is located in the `/src/main/content/META-INF/vault/definition` folder of the project:

```xml
<build>
    <resources>
        <!-- thumbnail only -->
        <resource>
            <directory>${basedir}/src/main/content/META-INF/vault/definition</directory>
            <targetPath>../vault-work/META-INF/vault/definition</targetPath>
        </resource>
    </resources>
</build>
```

## Using the AEM Project Archetype to Generate AEM Projects {#using-archetypes}

The latest AEM Project Archetype implements the best-practice package structure for both on-premises and AMS implementations and is recommended for all AEM projects.

>[!TIP]
>
>See the [AEM Project Structure](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-project-content-package-structure.html) article in the AEM as a Cloud Service documentation and the [AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html) documentation. Both of which are fully supported for AEM 6.5.
