---
title: Develop a Repository Structure Package   
description: Adobe Experience Manager as a Cloud Service Maven projects requires a Repository Structure Sub-package definition whose sole purpose is to define the JCR repository roots in which the project's Code sub-packages deploy into.
seo-title: Develop a Repository Structure Package   
seo-description: Adobe Experience Manager as a Cloud Service Maven projects requires a Repository Structure Sub-package definition whose sole purpose is to define the JCR repository roots in which the project's Code sub-packages deploy into.
kt: 3796
product: experience-manager
sub-product: cloud-manager
feature: cloud-manager
topics: cicd, development
version: 
doc-type: article, code
activity: develop
team: TM
audience:  developer
---
 
# Develop a Repository Structure Package

Adobe Experience Manager as a Cloud Service Maven projects requires a Repository Structure Sub-package definition whose sole purpose is to define the JCR repository roots in which the project's Code sub-packages deploy into.

This allows Experience Manager as a Cloud Service to ensure the Code packages do not inadvertently wipe out each others code. The JCR repository structure defined in this package, are known resources are not being installed by another package - so there is no risk of those resources coming from a package would wipe out your content.

If your Code package deploys into a location not covered __by__ the Code package, then the resources __too__ that location must be enumerated in the Repository Structure Package.

![Repository Structure Package](./assets/understand-an-aem-projects-content-package-structure/repository-structure-package.png)


The Repository Structure Package defines the expected, common state of `/apps` which the Package validator uses to determine areas "safe from potential conflicts" as they are standard roots.

The most typical paths to include in the Repository Structure Package are:

+ `/apps` which is a system-provided node
+ `/apps/cq/...`, `/apps/dam/...`, `/apps/wcm/...`, and `/apps/sling/...` which provide common overlays for `/libs`.
+ `/apps/settings` which is the shared context-aware configuration root path

Note that this Sub-package does __not__ have any content and is comprised solely of a `pom.xml` defining the filter roots.

## Creating the Repository Structure Package

To create a Repository Structure Package for you Maven project, create a new empty Maven sub-project, with the following `pom.xml`, updating the Project metadata to conform with your parent Maven project.

Update the `<filters>` to include all the JCR repository path roots your Code packages deploy into.

Make sure to add this new Maven sub-project to the parent projects `<modules>` list.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <!-- ====================================================================== -->
    <!-- P A R E N T  P R O J E C T  D E S C R I P T I O N                      -->
    <!-- ====================================================================== -->
    <parent>
        <groupId>com.my-company</groupId>
        <artifactId>my-app</artifactId>
        <version>x.x.x</version>
        <relativePath>../pom.xml</relativePath>
    </parent>

    <!-- ====================================================================== -->
    <!-- P R O J E C T  D E S C R I P T I O N                                   -->
    <!-- ====================================================================== -->
    <artifactId>my-app.repository-structure</artifactId>
    <packaging>content-package</packaging>
    <name>My App - Adobe Experience Manager Repository Structure Package</name>

    <description>
        Empty package that defines the structure of the Adobe Experience Manager repository the Code packages in this project deploy into.
        Any roots in the Code packages of this project should have their parent enumerated in the Filters list below.
    </description>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.jackrabbit</groupId>
                <artifactId>filevault-package-maven-plugin</artifactId>
                <extensions>true</extensions>
                <configuration>
                    <filters>

                        <!-- /apps root -->
                        <filter><root>/apps</root></filter>

                        <!-- Common overlay roots -->
                        <filter><root>/apps/sling</root></filter>
                        <filter><root>/apps/cq</root></filter>
                        <filter><root>/apps/dam</root></filter>
                        <filter><root>/apps/wcm</root></filter>

                        <!-- Immutable context-aware configurations -->
                        <filter><root>/apps/settings</root></filter>

                    </filters>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
 ```

## Referencing the Repository Structure Package

To use the Repository Structure Package, reference it via all Code package (the sub-packages that deploy to `/apps`) Maven project's via the FileVault Content Package Maven Plug-in's `<repositoryStructurePackage>` configuration.

In the `ui.apps/pom.xml`, and any other Code package `pom.xml's`, add a reference to the project's Repository Structure Package (#repository-structure-package) configuration to the FileVault Package Maven plug-in.

```xml
...
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.jackrabbit</groupId>
      <artifactId>filevault-package-maven-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        ...
        <repositoryStructurePackages>
          <repositoryStructurePackage>
              <groupId>${project.groupId}</groupId>
              <artifactId>my-app.repository-structure</artifactId>
              <version>${project.version}</version>
          </repositoryStructurePackage>
        </repositoryStructurePackages>
      </configuration>
    </plugin>
    ...
</build>
<dependencies>
    <!-- Add the dependency for the Repository Structure Package so it resolves -->
    <dependency>
        <groupId>${project.groupId}</groupId>
        <artifactId>my-app.repository-structure</artifactId>
        <version>${project.version}</version>
        <type>zip</type>
    </dependency>
    ...
</dependencies>
```

## Multi-Code Package Use Case

A less common, and more complex use-case, is supporting the deployment multiple Code packages that install into the same areas of the JCR repository.

For example:

+ Code Package A deploys into `/apps/a`
+ Code Package B deploys into `/apps/a/b`

If a Package-level dependency is not established from Code package B on Code package A, Code Package B may deploy first into `/apps/a`, followed by Code package B, which deploys into `/apps/a`, resulting in a removal of the previously installed `/apps/a/b`.

In this case:

+ Code package A should define a `<repositoryStructurePackage>` on the project's Repository Structure Package (which should have a filter for `/apps`).
+ Code package B should define a `<repositoryStructurePackage>` on Code Package A, because Code Package B deploys into space shared by Code Package A.

Creating this dependency chain on JCR repository resources removes 

## Errors and Debugging

If the repository structure packages are not set-up correctly, at Maven build an error will be reported:

```
1 error(s) detected during dependency analysis.
Filter root's ancestor '/apps/some/path' is not covered by any of the specified dependencies.
```

This indicates the breaking Code package does not have a `<repositoryStructurePackage>` that lists `/apps/some/path` in its filter list.

## Additional Resources

+ [FileVault Content Package Maven Plug-in](http://jackrabbit.apache.org/filevault-package-maven-plugin/)