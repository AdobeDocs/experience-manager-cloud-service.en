---
title: Build Environment of Cloud Manager
description: Learn about Cloud Manager's build environment and how it builds and tests your code.
exl-id: a4e19c59-ef2c-4683-a1be-3ec6c0d2f435
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer

---

# Build environment {#build-environment} 

Learn about Cloud Manager's build environment and how it builds and tests your code.

>[!TIP]
>
>This document covers Cloud Manager's build environment for developing your AEM as a Cloud Service project. For details on client platforms supported by AEM as a Cloud Service for content authoring, please see the document [Supported Client Platforms.](/help/overview/supported-platforms.md)

## Build environment details {#build-environment-details}

Cloud Manager builds and tests your code using a specialized build environment.

* The build environment is Linux-based, derived from Ubuntu 22.04.
* Apache Maven 3.9.4 is installed.
  * Adobe recommends users [update their Maven repositories to use HTTPS instead of HTTP](#https-maven).
<!-- OLD Removed 1/16/25 * The Java versions installed are Oracle JDK 11.0.22 and Oracle JDK 8u401. -->
* The Java versions installed are Oracle JDK 11.0.22, Oracle JDK 17.0.10, and Oracle JDK 21.0.4.

<!-- OLD Removed 1/16/25 * **IMPORTANT:** By default, the JAVA_HOME environment variable is set to `/usr/lib/jvm/jdk1.8.0_401`, which contains Oracle JDK 8u401. This default should be overridden for AEM Cloud Projects to use JDK 11. See the Setting the Maven JDK Version section for more details. -->
* **IMPORTANT:** By default, the `JAVA_HOME` environment variable is set to `/usr/lib/jvm/jdk1.8.0_401`, which contains Oracle JDK 8u401. ***This default should be overridden for AEM Cloud Projects to use JDK 21 (preferred), 17, or 11***. See the [Setting the Maven JDK Version](#alternate-maven-jdk-version) section for more details.
* There are some additional system packages installed which are necessary.
  * `bzip2`
  * `unzip`
  * `libpng`
  * `imagemagick`
  * `graphicsmagick`
* Other packages may be installed at build time as described in the section [Installing Additional System Packages](#installing-additional-system-packages).
* Each build runs in a clean environment, with the build container retaining no state between executions.
* Maven is always run with the following three commands.
  * `mvn --batch-mode org.apache.maven.plugins:maven-dependency-plugin:3.1.2:resolve-plugins`
  * `mvn --batch-mode org.apache.maven.plugins:maven-clean-plugin:3.1.0:clean -Dmaven.clean.failOnError=false`
  * `mvn --batch-mode org.jacoco:jacoco-maven-plugin:prepare-agent package`
* Maven is configured at a system level with a `settings.xml` file, which automatically includes the public Adobe artifact repository using a profile named `adobe-public`. (See [Adobe Public Maven Repository](https://repo1.maven.org/) for more details).

>[!NOTE]
>
>Although Cloud Manager does not define a specific version of the `jacoco-maven-plugin`, the version used must be at least `0.7.5.201505241946`.

## HTTPS Maven repositories {#https-maven}

Cloud Manager [release 2023.10.0](/help/implementing/cloud-manager/release-notes/2023/2023-10-0.md) began a rolling update to the build environment (completing with release 2023.12.0), which included an update to Maven 3.8.8. A significant change introduced in Maven 3.8.1 was a security enhancement aimed at mitigating potential vulnerabilities. Specifically, Maven now disables all insecure `http://*` mirrors by default, as outlined in the [Maven release notes](https://maven.apache.org/docs/3.8.1/release-notes.html#cve-2021-26291).

As a result of this security enhancement, some users may face issues during the build step, particularly when downloading artifacts from Maven repositories that use insecure HTTP connections.

To ensure a smooth experience with the updated version, Adobe recommends that users update their Maven repositories to use HTTPS instead of HTTP. This adjustment aligns with the industry's growing shift towards secure communication protocols and helps maintain a secure and reliable build process.

<!-- OLD below Removed 1/16/25

### Use a specific Java version

The Cloud Manager build process uses the Oracle 8 JDK to build projects by default, but AEM Cloud Service customers should set the Maven execution JDK version to 11. -->

<!-- OLD below Removed 1/16/25

#### Set the Maven JDK version

Adobe recommends that you set the JDK version for the entire Maven execution to `11` in a `.cloudmanager/java-version file`.

To do so, create a file named `.cloudmanager/java-version` in the git repository branch used by the pipeline. Edit the file so that it contains only the text, `11`. While Cloud Manager also accepts a value of `8`, this version is no longer supported for AEM Cloud Service projects. Any other value is ignored. When `11` is specified, Oracle 11 is used and the `JAVA_HOME` environment variable is set to `/usr/lib/jvm/jdk-11.0.22`. -->

### Use a specific Java version {#using-java-support}

The Cloud Manager build process uses the Oracle 8 JDK to build projects by default, but AEM Cloud Service customers should set the Maven execution JDK version to 21 (preferred), 17, or 11.

#### Set the Maven JDK version {#alternate-maven-jdk-version}

To set the Maven execution JDK, create a file named `.cloudmanager/java-version` in the Git repository branch used by the pipeline. Edit the file so that it contains only the text, `21` or `17`. While Cloud Manager also accepts a value of `8`, this version is no longer supported for AEM Cloud Service projects. Any other value is ignored. When `21` or `17` is specified, Oracle Java 21 or Oracle Java 17 is used. 


#### Prerequisites for migrating to building with Java 21 or Java 17 {#prereq-for-building}

To migrate to building with Java 21 or Java 17, you must first upgrade to the latest SonarQube version. For details, see the [Release Notes for Cloud Manager 2025.1.0](/help/implementing/cloud-manager/release-notes/current.md#what-is-new).

When migrating your application to a new Java build version and runtime version, thoroughly test in dev and stage environments before deploying to production.

We recommend the following deployment strategy:

1. Run your local SDK with Java 21, which you can download from https://experience.adobe.com/#/downloads, and deploy your application to it and validate its functionality. Check the logs that there are no errors, which indicate problems with classloading or bytecode weaving.
1. Configure a branch in your Cloud Manager repository to use Java 21 as buildtime Java version, configure a DEV pipeline to use this branch and run the pipeline. Run your validation tests.
1. If it looks good, configure your stage/prod pipeline to use Java 21 as buildtime Java version and run the pipeline.

##### About some translation features {#translation-features}

The following features might not function correctly when deployed on the Java 21 runtime, and Adobe expects to resolve them by early 2025:

* `XLIFF` (XML Localization Interchange File Format) fails when using Human Translation.  
* `I18n` (Internationalization) does not properly handle language locales Hebrew (`he`), Indonesian (`in`), and Yiddish (`yi`) due to changes in the Locale constructor in newer Java versions.

#### Runtime requirements {#runtime-requirements}

The Java 21 runtime is used for builds with Java 21 and Java 17, and it will gradually be applied to Java 11 builds too (see the Note below). An environment must be on AEM release 17098 or more recent to receive the Java 21 update. To ensure compatibility, the following adjustments are required.

Library updates can be applied anytime, as they remain compatible with older Java versions.

* **Minimum version of ASM:**
Update the usage of  the Java package`org.objectweb.asm`, often bundled in `org.ow2.asm.*` artifacts, to version 9.5 or higher to ensure support for newer JVM runtimes.

* **Minimum version of Groovy:**
Update the usage of the Java packages `org.apache.groovy` or `org.codehaus.groovy` to version 4.0.22 or higher to ensure support for newer JVM runtimes.

  This bundle can be indirectly included by adding third party dependencies such as the AEM Groovy Console.

* **Minimum version of Aries SPIFly:**
Update the usage of the Java package `org.apache.aries.spifly.dynamic.bundle` to version 1.3.6 or newer to ensure support for newer JVM runtimes.

The AEM Cloud Service SDK is compatible with Java 21 and can be used to validate the compatibility of your project with Java 21 before executing a Cloud Manager pipeline.

* **Edit a runtime parameter:**
When running AEM locally with Java 21, the start scripts (`crx-quickstart/bin/start` or `crx-quickstart/bin/start.bat`) fail due to the `MaxPermSize` parameter. As a remedy, either remove `-XX:MaxPermSize=256M` from the script or define the environment variable `CQ_JVM_OPTS`, setting it to `-Xmx1024m -Djava.awt.headless=true`.

  This issue is solved in the AEM Cloud Service SDK version 19149 and later.

>[!IMPORTANT]
>
>When `.cloudmanager/java-version` is set to `21` or `17`, the Java 21 runtime is deployed. The Java 21 runtime is scheduled for gradual rollout to all environments (not just those environments whose code is built with Java 11) starting Tuesday, February 4, 2025. The rollout will begin with sandboxes and development environments, and then rollout to all production environments in April 2025. Customers who want to adopt the Java 21 runtime *earlier* can contact Adobe at [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com).


#### Build time requirements {#build-time-reqs}

The following adjustments are required to allow building the project with Java 21 and Java 17. They can be updated even before you are running Java 21 and Java 17 because they are compatible with older Java versions.

AEM Cloud Service customers are recommended to build their projects with Java 21 as early as possible to take advantage of new language features.

* **Minimum version of `bnd-maven-plugin`:**
Update the usage of `bnd-maven-plugin` to version 6.4.0 to ensure support for newer JVM runtimes. 

  Versions 7 or higher are not compatible with Java 11 or lower so an upgrade to that version is not recommended.

* **Minimum version of `aemanalyser-maven-plugin`:**
Update the usage of `aemanalyser-maven-plugin` to version 1.6.6 or higher to ensure support for newer JVM runtimes.

* **Minimum version of `maven-bundle-plugin`:**
Update the usage of `maven-bundle-plugin` to version 5.1.5 or higher to ensure support for newer JVM runtimes. 

  Versions 6 or higher are not compatible with Java 11 or lower so an upgrade to that version is not recommended.

* **Update dependencies in `maven-scr-plugin`:**
The `maven-scr-plugin` is not directly compatible with Java 21 or Java 17. However, descriptor files can be generated by updating the ASM dependency version in the plugin configuration, as shown in the following example:

```XML
<project>
  ...
  <build>
    ...
    <plugins>
      ...
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-scr-plugin</artifactId>
        <version>1.26.4</version>
        <executions>
          <execution>
            <id>generate-scr-scrdescriptor</id>
            <goals>
              <goal>scr</goal>
            </goals>
          </execution>
        </executions>
        <dependencies>
          <dependency>
            <groupId>org.ow2.asm</groupId>
            <artifactId>asm-analysis</artifactId>
            <version>9.7.1</version>
            <scope>compile</scope>
          </dependency>
        </dependencies>
      </plugin>
      ...
    </plugins>
    ...
  </build>
  ...
</project>
```

## Environment variables - standard {#environment-variables}

You may find it necessary to vary the build process based on information about the program or pipeline. 

For instance, if JavaScript minification occurs at build time using a tool like gulp, different minification levels may be preferred for various environments. A development build might use a lighter minification level compared to staging and production.

To support this, Cloud Manager adds these standard environment variables to the build container for every execution.

| Variable Name | Definition |
|---|---|
| `CM_BUILD` |  Always set to `true` | 
| `BRANCH` | The configured branch for the execution  |
| `CM_PIPELINE_ID` |  The numeric pipeline identifier | 
| `CM_PIPELINE_NAME` |  The pipeline name | 
| `CM_PROGRAM_ID` |  The numeric program identifier | 
| `CM_PROGRAM_NAME` |  The program name | 
| `ARTIFACTS_VERSION` |  For a stage or production pipeline, the synthetic version generated by Cloud Manager | 
| `CM_AEM_PRODUCT_VERSION` |  The release version |

## Environment variables - pipeline {#pipeline-variables}

Your build process might require specific configuration variables that should not be stored in the Git repository. Additionally, you may need to adjust these variables between pipeline executions using the same branch.

See also [Configure Pipeline Variables](/help/implementing/cloud-manager/configuring-pipelines/pipeline-variables.md) for more information.

## Install additional system packages {#installing-additional-system-packages}

Some builds require additional system packages to function fully. For example, a build may invoke a Python or Ruby script and must have an appropriate language interpreter installed. This installation process can be managed by calling the [`exec-maven-plugin`](https://www.mojohaus.org/exec-maven-plugin/) in your `pom.xml` to invoke APT. This execution should generally be wrapped in a Cloud Manager-specific Maven profile. This example installs Python.

```xml
        <profile>
            <id>install-python</id>
            <activation>
                <property>
                        <name>env.CM_BUILD</name>
                </property>
            </activation>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.codehaus.mojo</groupId>
                        <artifactId>exec-maven-plugin</artifactId>
                        <version>1.6.0</version>
                        <executions>
                            <execution>
                                <id>apt-get-update</id>
                                <phase>validate</phase>
                                <goals>
                                    <goal>exec</goal>
                                </goals>
                                <configuration>
                                    <executable>apt-get</executable>
                                    <arguments>
                                        <argument>update</argument>
                                    </arguments>
                                </configuration>
                            </execution>
                            <execution>
                                <id>install-python</id>
                                <phase>validate</phase>
                                <goals>
                                    <goal>exec</goal>
                                </goals>
                                <configuration>
                                    <executable>apt-get</executable>
                                    <arguments>
                                        <argument>install</argument>
                                        <argument>-y</argument>
                                        <argument>--no-install-recommends</argument>
                                        <argument>python</argument>
                                    </arguments>
                                </configuration>
                            </execution>
                        </executions>
                    </plugin>
                </plugins>
            </build>
        </profile>
```

This same technique can be used to install language-specific packages, for example, using `gem` for RubyGems or `pip` for Python Packages.

>[!NOTE]
>
>Installing a system package in this manner does not install it in the runtime environment used for running Adobe Experience Manager. If you need a system package installed on the AEM environment, contact your Adobe Representative.

>[!TIP]
>
>For details about the front-end build environment, see [Developing Sites with the Front-End Pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md).
