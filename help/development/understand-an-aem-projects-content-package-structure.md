---
title: Understand Project Package Structure
description: Learn about how to properly define AEM application package structures for deployment to AEM Cloud Service.
seo-title: Understand Project Content Package Structure
seo-description: Learn about how to properly define AEM application package structures for deployment to AEM Cloud Service.
sub-product: cloud-manager
feature: 
topics: best-practices
version: 
doc-type: article
activity: understand
audience: implementer, architect
kt: 3404
---

# Understand an AEM Project's Content Package Structure
 
AEM application deployments must be comprised of a single AEM package. This package should in turn contain sub-packages that comprise everything required by the application to function, including code, configuration and any supporting baseline content.

AEM requires a separation of __content__ and __code__, which means a single content package __cannot__ deploy to **both** `/apps` and runtime-writable areas (`/content`, `/conf`, `/home`, etc. - in short, anything not `/apps`) of the repository, instead, the application must separate code and content into discrete packages for deployment into AEM.

The package structure outlined in this document is compatible with **both** local development deployments and AEM Cloud Service deployments.

## Mutable vs. Immutable Areas of the Repository

`/apps` and `/libs` are considered **immutable** areas of AEM as they cannot be changed (create, update, delete) after AEM starts (ie. at runtime). If an attempt to change an immutable area is made at run time, the action will fail.

Everything else in the repository, `/content`, `/conf`, `/var`, `/home`, `/etc`, `/oak:index`, `/system`, `/tmp`, etc. are all **mutable** areas, meaning they can be changed at run time.

>[!WARNING]
>
> `/libs` remains off-limits. Only Adobe Experience Manager product code may deploy to `/libs`.

## Recommended Package Structure

![AEM Project Package Structure](./assets/understand-an-aem-projects-content-package-structure/content-package-organization.png)

This diagram provides an overview of the recommended project structure and package deployment artifacts.

The recommended application deployment structure is as follows:

+ The `ui.apps` package, or Content Package, contains all the code to be deployed and only deploys to `/apps`. Common elements of the `ui.apps` package include, but are not limited to:
  + OSGi bundles
    + `/apps/my-app/install`
  + OSGi configurations
    + `/apps/my-app/config`
  + HTL scripts
    + `/apps/my-app/components`
  + JavaScript and CSS (via Client Libraries)
    + `/apps/my-app/clientlibs`
  + Overlays of /libs
    + `/apps/cq`, `/apps/dam/`, etc.
  + Fallback context-aware configurations
    + `/apps/settings`
  + ACLs (permissions)
    + Any `rep:policy` for any path under `/apps`
+ The `ui.content` package, or Code Package, contains all content and configuration. Common elements of the `ui.content` package include, but are not limited to:
  + Context-aware configurations
    + `/conf`
  + Baseline content structures (Asset folders, Sites root pages)
    + `/content`, `/content/dam`, etc.
  + Governed tagging taxonomies
    + `/content/cq:tags`
  + Service users
    + `/home/users`
  + User groups
    + `/home/groups`  
  + Oak indexes
    + `/oak:indexes`
  + Etc legacy nodes
    + `/etc`
  + ACLs (permissions)
    + Any `rep:policy` for any path **not** under `/apps`
+ The `all` package is a container package that ONLY includes the `ui.apps` and `ui.content` packages as embeds under `/etc/packages`. The `all` package must not have _any_ content of its own, but rather delegate all deployment to the repository to its sub-packages.

  For complex AEM deployments, it may be desirable to create multiple `ui.apps` and `ui.content` projects/packages that represent specific sites or tenants in AEM. If this is done, ensure the split between mutable and immutable content is respected, and the required content packages are added as sub-packages in the `all` container content package.

  For example, a complex deployment content package structure may look like this:

  + `all` content package embeds the following packages, to create a singular deployment artifact
    + `ui.apps.common` deploys code required by __both__ Site A and Site B
    + `ui.apps.site-a` deploys code required by Site A
    + `ui.content.site-a` deploys content and configuration required by Site A
    + `ui.apps.site-b` deploys code required by Site B
    + `ui.content.site-b` deploys content and configuration required by Site B

## Package Types

Packages are to be marked with their declared package type.

+ Container packages must not have a `packageType` set.
+ Code (immutable) packages must set their `packageType` to `application`.
+ Content (mutable) packages must set their `packageType` to `content`.

For more information see [Apache Jackrabbit FileVault - Package Maven Plugin documentation](https://jackrabbit.apache.org/filevault-package-maven-plugin/package-mojo.html#packageType) and the [FileVault Maven configuration snippet](#declaring-package-types) below.

# Author/Publish-specific Content (Mutable) Packages

>[!NOTE]
> This section described the __only exception__ in putting an `/apps` folder or file in a Content (mutable) package.

Mutable Content packages (rather than immutable Code packages) can be targeted for installation on either AEM Author, AEM Publish or Both.

Common use cases for this include:

* ACLs/permissions that differ between AEM Author users and AEM Publish users
* Configurations that are used to support activities only on AEM Author

To target AEM Author or AEM Publish, add an empty `install` folder under your application's `/apps/<my-app>` folder:

* To __only__ install the Content package on __AEM Author__, create and empty folder at: `/apps/<my-app>/install.author`.
* To __only__ install the Content package on __AEM Publish__, create and empty folder at: `/apps/<my-app>/install.publish`.
* To install the Content package on __both AEM Author and Publish__, do NOT create an `install` folder.

Do NOT add this path to the package's `filter.xml`. This folder will NOT be installed as it is only a marker for Adobe Cloud Manager, providing instructions for which AEM Cloud Service tier the package will be installed on.

Only `.../install.author`  and `../install.publish` are supported targets. Other run modes are NOT supported.

For example, a deployment that contains AEM Author and Publish specific Content packages may look like this:

  + `all` content package embeds the following packages, to create a singular deployment artifact
    + `ui.apps` deploys code
    + `ui.content.common` deploys content and configuration required by __both__ AEM Author and AEM Publish
    + `ui.content.author` deploys content and configuration required __ONLY__ by AEM Author, by including an empty folder `/apps/<my-app>/install.author`
    + `ui.content.pubish` deploys content and configuration required __ONLY__ by AEM Publish, by including an empty folder `/apps/<my-app>/install.publish`

## Package Dependency Management

In order to ensure proper installation of the packages, it is recommended inter-package dependencies are established.

The general rule is packages containing mutable content (`ui.content`) should depend on the immutable content (`ui.apps`) that supports the rendering and use of the mutable content.

The common patterns for content package dependencies are:

### Simple Deployment Package Dependencies

The simple case sets the `ui.content` mutable Content package to depend on the `ui.apps` immutable Code package.

+ `all` has no dependencies
  + `ui.apps` has no dependencies
  + `ui.content` depends on `ui.apps`

### Complex Deployment Package Dependencies

Complex deployments expand on the simple case, and set dependencies between the corresponding mutable Content and immutable Code packages. As required, dependencies can be established between immutable Code packages as well.

+ `all` has no dependencies
  + `ui.apps.common` has no dependencies
  + `ui.apps.site-a` depends on `ui.apps.common`
  + `ui.content.site-a` depends on `ui.apps.site-a`
  + `ui.apps.site-b` depends on `ui.apps.common`
  + `ui.content.site-b` depends on `ui.apps.site-b`

## Local Development and Deployment

The project structures and organization outlined in this article is fully compatible local development AEM instances.

## pom.xml Configuration Snippets

The following are Maven `pom.xml` configuration snippets that can be added to Maven projects to align to the above recommendations.

### Declaring Package Types{#declaring-package-types}

Code and content packages, which are deployed as sub-packages, must declare a package type of __application__ or __content__, depending on what they contain.

#### Container Package Types

The container `all/pom.xml` project does __not__ declare a `<packageType>`.

#### Code (Immutable) Package Types

Code packages must set their `packageType` to `application`.

In the `ui.apps/pom.xml`, the `<packageType>application</packageType>` build configuration directives of the `filevault-package-maven-plugin` plugin declaration declares its package type.

```
...
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.jackrabbit</groupId>
      <artifactId>filevault-package-maven-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <group>${project.groupId}</group>
        <name>${my-app.ui.apps}</name>
        <packageType>application</packageType>
        <accessControlHandling>merge</accessControlHandling>
      </configuration>
    </plugin>
    ...
```

#### Content (Mutable) Package Types

Content packages must set their `packageType` to `content`.

In the `ui.content/pom.xml`, the `<packageType>content</packageType>` build configuration directive of the `filevault-package-maven-plugin` plugin declaration declares its package type.

```
...
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.jackrabbit</groupId>
      <artifactId>filevault-package-maven-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <group>${project.groupId}</group>
        <name>${my-app.ui.content}</name>
        <packageType>content</packageType>
        <accessControlHandling>merge</accessControlHandling>
      </configuration>
    </plugin>
    ...
```

### Adding Sub-packages to the `all` Package

In the `all/pom.xml`, add the following `<subPackage>` directives to the `filevault-package-maven-plugin` plugin declaration.

```
...
<plugin>
  <groupId>org.apache.jackrabbit</groupId>
  <artifactId>filevault-package-maven-plugin</artifactId>
  <extensions>true</extensions>
  <configuration>
      ...
      <subPackages>
          
          <!-- Include the application's ui.apps and ui.content packages -->
          <!-- Ensure the artifactIds are correct -->
          <subPackage>
              <groupId>${project.groupId}</groupId>
              <artifactId>my-app.ui.apps</artifactId>
              <filter>true</filter>
          </subPackage>
          
          <subPackage>
              <groupId>${project.groupId}</groupId>
              <artifactId>my-app.ui.content</artifactId>
              <filter>true</filter>
          </subPackage>

          <!-- Include any other extra packages such as AEM WCM Core Components -->
          <subPackage>
              <groupId>com.adobe.cq</groupId>
              <artifactId>core.wcm.components.all</artifactId>
              <filter>true</filter>
          </subPackage>
      <subPackages>
  </configuration>
</plugin>
...
```

### Establishing a Dependency between the `ui.apps` from `ui.content` Packages

In the `ui.content/pom.xml`, add the following `<subPackage>` directives to the `filevault-package-maven-plugin` plugin declaration.

```
...
<plugin>
  <groupId>org.apache.jackrabbit</groupId>
  <artifactId>filevault-package-maven-plugin</artifactId>
  <extensions>true</extensions>
  <configuration>
     <group>my/package/group</group>

      ...
      <dependencies>
        <!-- Declare the content package dependency in the ui.content/pom.xml on the ui.apps project -->
        <dependency>
            <!-- The group refers to the content package group, NOT the maven project groupId -->
            <group>my/package/group</group>
            <!-- Ensure the correct package name is listed -->
            <name>my-app.ui.apps</name>
            <version>${project.version}</version>
        </dependency>
      </dependencies>
    ...
  </configuration>
</plugin>
...
```
