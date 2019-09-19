---
title: Understand Project Content Package Structure
description: Learn about how to properly define Application Content Package Structures for deployment to AEM Cloud Service.
seo-title: Understand Project Content Package Structure
seo-description: Learn about how to properly define Application Content Package Structures for deployment to AEM Cloud Service.
sub-product: cloud-manager
feature: 
topics: best-practices
version: 
doc-type: article
activity: understand
audience: implementer, architect
kt: 3404
---

# Understand an AEM Project's Content Package Structure (DRAFT)
 
AEM application deployments must be comprised of a single AEM content package. This content package should in turn contain sub-packages that comprise everything required by the application to function, including code, configuration and any supporting baseline content.

AEM requires a separation of content and code, which means a single content package cannot deploy to **both** `/apps` and runtime-writable areas (`/content`, `/conf`, `/home`, etc. - in short, anything not `/apps`) of the repository, instead, the application must separate code and content into discrete content packages for deployment into AEM.

The content package structure outlined in this document is compatible with **both** local development deployments and cloud deployments.

## Mutable vs. Immutable Areas of the Repository

`/apps` and `/libs` are considered **immutable** areas of AEM, because they cannot be changed (create, update, delete) after AEM starts (ie. at runtime). If an attempt to change an immutable areas is made at run time, the action will fail.

Everything else in the repository, `/content`, `/conf`, `/var`, `/home`, `/etc`, `/oak:index`, `/system`, `/tmp`, etc. are all **mutable** areas, meaning they can be changed at run time.

>[!WARNING]
>
> `/libs` remains off-limits. Only Adobe Experience Manager product code may deploy to `/libs`.

## Recommended Content Package Structure

![Project Content Package Structure](./assets/understand-project-content-packages/content-package-organization.png)

This diagram provides an overview of the recommended project structure and deployment artifacts.

The recommended application deployment structure is as follows:

+ The `ui.apps` content package contains all the code to be deployed and only deploys to `/apps`. Common elements of the `ui.apps` package include, but are not limited to:
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
+ The `ui.content` content package contains all content and configuration. Common elements of the `ui.content` package include, but are not limited to:
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
+ The `all` content package is a container package that ONLY includes the `ui.apps` and `ui.content` content packages as embeds under `/etc/packages`. The `all` package should not have *any* content of its own, but rather delegate all deployment to the repository to its sub-packages.

  For complex AEM deployments, it may be desirable to create multiple `ui.apps` and `ui.content` projects that represent specific sites or tenants in AEM. If this is done, ensure the split between mutable and immutable content is respected, and the required content packages are added as sub-packages in the `all` container content package.

  For example, a complex deployment content package structure may look like this:

  + `all` content package embeds the following packages, to create a singular deployment artifact
    + `ui.apps.common` deploys code required by **both** Site A and Site B
    + `ui.apps.site-a` deploys code required by Site A
    + `ui.content.site-a` deploys content and configuration required by Site A
    + `ui.apps.site-b` deploys code required by Site B
    + `ui.content.site-b` deploys content and configuration required by Site B

## Content Package Types

Content packages are to be marked with their declared package type.

+ Container content packages should not have a `packageType` set.
+ Code (immutable) content packages should set their `packageType` to `application`.
+ Content (mutable) content packages should set their `packageType` to `content`.

For more information see [Apache Jackrabbit FileVault - Package Maven Plugin documentation](https://jackrabbit.apache.org/filevault-package-maven-plugin/package-mojo.html#packageType).

## Content Package Dependency Management

In order to ensure proper installation of the content packages, it is recommended that content package dependencies are established.

The general rule is content packages containing mutable content (`ui.content`) should depend on the immutable content (`ui.apps`) that supports the rendering and use of the mutable content.

The common patterns for content package dependencies are:

### Simple Deployment Content Package Dependencies

The simple case sets the `ui.content` mutable content package depends on the  `ui.apps` immutable content package.

+ `all` has no dependencies
  + `ui.apps` has no dependencies
  + `ui.content` depends on `ui.apps`

### Complex Deployment Content Package Dependencies

Complex deployments should expand on the simple case, and set dependencies between the corresponding mutable and immutable packages. As required, dependencies can be established between immutable packages as well.

+ `all` has no dependencies
  + `ui.apps.common` has no dependencies
  + `ui.apps.site-a` depends on `ui.apps.common`
  + `ui.content.site-a` depends on `ui.apps.site-a`
  + `ui.apps.site-b` depends on `ui.apps.common`
  + `ui.content.site-b` depends on `ui.apps.site-b`

## Local Development and Deployment

The project structure and organization outlined in this article is fully compatible local development AEM instances.

## pom.xml Configuration Snippets

The following are pom.xml configuration snippets that can be added to existing Maven projects to achieve sub-packaging and content package dependencies.

### Declaring Package Types

Code and content packages, which are deployed as sub-packaged, must declare a package type of __application__ or __content__, depending on what they contain.

#### Container Package Types

The container `all/pom.xml` project does not declare a `<packageType>`.

#### Code (Immutable) Package Types

Code packages must set their __packageType__ to __application__.

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

Content packages must set their __packageType__ to __application__.

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

### Adding Sub-packages to the `all` Content Package

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

### Establishing a Dependency between the `ui.apps` from `ui.content` Content Packages

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
