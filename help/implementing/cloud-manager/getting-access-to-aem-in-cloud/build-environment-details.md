---
title: Build Environment of Cloud Manager
description: Learn about Cloud Manager's build environment and how it builds and tests your code.
exl-id: a4e19c59-ef2c-4683-a1be-3ec6c0d2f435
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer

---

# Build environment of Cloud Manager {#build-environment}

Learn about Cloud Manager's build environment and how it builds and tests your code.

>[!TIP]
>
>This document covers Cloud Manager's build environment for developing your AEM as a Cloud Service project. For details on client platforms supported by AEM as a Cloud Service for content authoring, see [Supported Client Platforms](/help/overview/supported-platforms.md).

## Build environment details {#build-environment-details}

Cloud Manager builds and tests your code using a specialized build environment.

* The build environment is Linux-based, derived from Ubuntu 22.04.
* Apache Maven 3.9.4 is installed.
  * Use [HTTPS for Maven repositories](#https-maven).
* The Java versions installed are Oracle JDK 11.0.22, Oracle JDK 17.0.10, Oracle JDK 21.0.4, and Oracle JDK 25.0.2.
* **IMPORTANT:** By default, the `JAVA_HOME` environment variable is set to `/usr/lib/jvm/jdk1.8.0_401`, which contains Oracle JDK 8u401. Override this default for AEM Cloud Service projects by [setting the Maven JDK version](#alternate-maven-jdk-version).
* There are some additional necessary system packages installed.
  * `bzip2`
  * `unzip`
  * `libpng`
  * `imagemagick`
  * `graphicsmagick`
* Other packages are installed at build time as described in the section [Installing Additional System Packages](#installing-additional-system-packages).
* Each build runs in a new environment; the build container does not persist data between executions.
* Maven is always run with the following three commands.
  * `mvn --batch-mode org.apache.maven.plugins:maven-dependency-plugin:3.1.2:resolve-plugins`
  * `mvn --batch-mode org.apache.maven.plugins:maven-clean-plugin:3.1.0:clean -Dmaven.clean.failOnError=false`
  * `mvn --batch-mode org.jacoco:jacoco-maven-plugin:prepare-agent package`
* Maven is configured at a system level with a `settings.xml` file, which automatically includes the public Adobe artifact repository using a profile named `adobe-public`. (See [Adobe Public Maven Repository](https://repo1.maven.org/) for more details).

>[!NOTE]
>
>Cloud Manager does not specify a version of the `jacoco-maven-plugin`. Configure a version that supports your build JDK and compiled code. See [Build requirements](#build-time-reqs).

## HTTPS Maven repositories {#https-maven}

Use HTTPS URLs for Maven repositories and mirrors. Maven [blocks external HTTP repositories by default](https://maven.apache.org/docs/3.8.1/release-notes.html#cve-2021-26291), which can cause dependency or plugin downloads to fail. If your build references an HTTP repository, update the repository or mirror configuration to use its HTTPS endpoint.

### Use a specific Java version {#using-java-support}

The Cloud Manager build process uses the Oracle 8 JDK to build projects by default, but AEM Cloud Service customers should set the Maven execution JDK version to 25, 21, 17, or 11.

The build JDK runs Maven; the compiler target determines the Java release targeted by your code; the AEM runtime runs the deployed application. These are distinct settings. The sections below cover build configuration and upgrade prerequisites. For Java 25-specific requirements and opt-in options, see [Java 25 support](#java-25-support).

#### Set the Maven JDK version {#alternate-maven-jdk-version}

To set the Maven execution JDK, create a file named `.cloudmanager/java-version` in the Git repository branch used by the pipeline. The file must contain only the major version number: `25`, `21`, `17`, or `11`. Cloud Manager uses the corresponding Oracle JDK. Although Cloud Manager also accepts `8`, this version is no longer supported for AEM Cloud Service projects. Other values are ignored.

The file selects the JDK that runs Maven, not the compiler target. The default AEM runtime is currently Java 21. Building with JDK 25 also opts the target environment into the Java 25 runtime, regardless of the compiler target. Review [Java 25 support](#java-25-support) before selecting `25`.

#### Prerequisites for migrating to a newer Java version {#prereq-for-building}

To build with Java 21 or Java 17, Cloud Manager now uses SonarQube 9.9, which is compatible with these Java versions. This change was introduced in Cloud Manager release 2025.1.0. No customer action is required to upgrade SonarQube. For more details and to understand the change, see the [Release Notes for Cloud Manager 2025.1.0](/help/implementing/cloud-manager/release-notes/2025/2025-1-0.md).

For a build JDK change, review the [build time requirements](#build-time-reqs) for your target version. For a runtime-only change, review the requirements for the target runtime; changing the build JDK is not required. When migrating your application to a new Java build version or runtime version, thoroughly test in dev and stage environments before deploying to production.

Adobe recommends the following deployment strategy:

1. Download an [AEM Cloud Service SDK](https://experience.adobe.com/#/downloads) version that supports your intended Java runtime. Run the SDK with that runtime, deploy your application to it, and validate its functionality. Check the logs for class-loading or bytecode-weaving errors.
1. For a build JDK change, configure the [Maven JDK](#alternate-maven-jdk-version) in a branch in your Cloud Manager repository, configure a DEV pipeline to use this branch, and run the pipeline. For a runtime-only change, apply the runtime configuration and wait for the environment update; rebuilding the application is not required. Run your validation tests.
1. If the results are satisfactory in development, apply the same change to stage and validate it before proceeding to production.

#### Runtime requirements {#runtime-requirements}

The following requirements apply to the **Java 21 runtime**. For Java 25, use the separate [Java 25 runtime requirements](#java-25-runtime-requirements).

* **Minimum version of ASM:**
Update the usage of the Java package `org.objectweb.asm`, often bundled in `org.ow2.asm.*` artifacts, to version 9.8 or higher to ensure support for newer JVM runtimes.

* **Minimum version of Groovy:**
Update the usage of the Java packages `org.apache.groovy` or `org.codehaus.groovy` to version 4.0.22 or higher to ensure support for newer JVM runtimes.

  This bundle can be indirectly included by adding third party dependencies such as the AEM Groovy Console.

* **Minimum version of Aries SPIFly:**
Update the usage of the Java package `org.apache.aries.spifly.dynamic.bundle` to version 1.3.6 or newer to ensure support for newer JVM runtimes.

#### Build time requirements {#build-time-reqs}

The following adjustments are required to allow building the project with Java 21 and Java 17. They can be updated even before you are running Java 21 and Java 17 because they are compatible with older Java versions.

For Java 25 builds, also follow the [Java 25 build requirements](#java-25-build-requirements). The minimum versions below alone do not guarantee Java 25 compatibility. Update only the plugins that your project uses.

* **Minimum version of `bnd-maven-plugin`:**
Update the usage of `bnd-maven-plugin` to version 6.4.0 to ensure support for newer JVM runtimes.

  Versions 7 or higher are not compatible with Java 11 or lower so an upgrade to that version is not recommended.

* **Minimum version of `aemanalyser-maven-plugin`:**
Update the usage of `aemanalyser-maven-plugin` to version 1.6.16 or higher to ensure support for newer JVM runtimes.

* **Minimum version of `maven-bundle-plugin`:**
Update the usage of `maven-bundle-plugin` to version 5.1.5 or higher to ensure support for newer JVM runtimes.

  Versions 6 or higher are not compatible with Java 11 or lower so an upgrade to that version is not recommended.

* **Update dependencies in `maven-scr-plugin`:**
The `maven-scr-plugin` is not directly compatible with Java version 17 or newer. However, descriptor files can be generated by updating the ASM dependency version in the plugin configuration, as shown in the following example:

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
            <version>9.8</version>
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

#### Java 25 support {#java-25-support}

Adobe recommends Java 25 for building AEM Cloud Service projects. You can also validate an existing application on the Java 25 runtime without changing its build JDK. Follow the [deployment strategy](#prereq-for-building) above for either option.

##### Runtime upgrade timeline {#java-25-runtime-upgrade-timeline}

Adobe is providing the following target dates to help you plan testing and validation ahead of the Java 25 runtime upgrade. Any changes to this timeline will be communicated through the [AEM as a Cloud Service release notes](/help/release-notes/release-notes-cloud/release-notes-current.md#java25-announcement).

| Timeframe | Milestone |
| --- | --- |
| **October 29, 2026** | AEM Cloud Service SDK supports Java 25 runtime. The Java 25 JDK is available for download from the Adobe Software Distribution portal. |
| **November 20, 2026** | Customers are encouraged to optionally enable the Java 25 runtime in their Cloud environments to validate behavior. Early adoption maximizes time to surface and resolve issues. |
| **January – April 2027** | Adobe will gradually migrate sandboxes and lower environments (RDE, Dev) to the Java 25 runtime. Customers should validate behavior and report unexpected issues, and are encouraged to enable staging and production environments as well. A temporary rollback to Java 21 is available while resolving any problems. |
| **May 2027** | All environment runtimes (including staging and production) migrate to Java 25. Java 21 runtime is decommissioned. The AEM Cloud Service SDK will no longer support Java 21. |

##### Java 25 runtime requirements {#java-25-runtime-requirements}

>[!IMPORTANT]
>
>Both opt-in options require **AEM release 28386 or later** in each environment.

If your application bundles the following libraries, directly or through third-party dependencies such as the AEM Groovy Console, update them to versions with Java 25 bytecode support before opting in:

* **ASM** (`org.objectweb.asm`, typically supplied by `org.ow2.asm.*` artifacts): [9.8 or later](https://asm.ow2.io/versions.html).
* **Groovy** (`org.apache.groovy` artifacts): [4.0.27 or later in the 4.0 release line](https://groovy-lang.org/changelogs/changelog-4.0.27.html).
* **Aries SPI Fly** (`org.apache.aries.spifly.dynamic.bundle`): [1.3.8 or later](https://aries.apache.org/documentation/modules/spi-fly.html).

Older bytecode-processing libraries can fail on Java 25 even if your code targets an earlier Java release. Keep related ASM artifacts at the same version and honor the dependency versions required by libraries such as SPI Fly. Validate the complete application, including third-party bundles.

##### Java 25 build requirements {#java-25-build-requirements}

These requirements apply only when building with JDK 25, not to a runtime-only opt-in. In addition to the [build time requirements](#build-time-reqs), use [JaCoCo 0.8.14 or later](https://www.jacoco.org/jacoco/trunk/doc/changes.html) and bytecode-processing build plugins that support Java 25. If using `maven-scr-plugin`, set its `asm-analysis` dependency to [9.8 or later](https://asm.ow2.io/versions.html) in the example above. Validate the complete Cloud Manager pipeline, not just local compilation.

Set `.cloudmanager/java-version` to `25` to build with JDK 25 and opt the target environment into the Java 25 runtime. The [runtime requirements](#java-25-runtime-requirements) also apply; `AEM_JAVA_25_OPT_IN` is not needed. To use Java 25 language features and APIs, configure the compiler to target Java 25. To retain Java 21 compatibility, set `maven.compiler.release` to `21` and use dependencies compatible with Java 21. This lower compiler target does not prevent the Java 25 runtime opt-in.

##### Java 25 runtime opt-in {#java-25-runtime-opt-in}

To enable only the Java 25 runtime, review the [runtime requirements](#java-25-runtime-requirements), then use the environment variable below. Keep your existing build JDK and compiler settings; the Java 25 build requirements do not apply to this option.

1. In Cloud Manager, select the environment that you want to enable.
1. [Add an environment variable](/help/implementing/cloud-manager/environment-variables.md#add-variables) with the following configuration:

   | Field | Value |
   | --- | --- |
   | **Name** | `AEM_JAVA_25_OPT_IN` |
   | **Value** | `true` (lowercase) |
   | **Step Applied** | **All** |
   | **Type** | **Normal** (not a secret) |

1. Save the configuration and wait for the environment update to complete.
1. Validate your application's behavior in the updated environment. Rebuilding the application is not required for this runtime-only change.

>[!NOTE]
>
>With this option, set the variable in each environment that you want to enable. **Stage and production environments must be enabled separately**, even if they use the same production pipeline. Validate in development and stage before enabling production.

Before rolling back, ensure that the deployed application and its dependencies support the previous Java version; if necessary, redeploy a compatible version. Deleting the variable does not undo an opt-in caused by building with JDK 25, even if the compiler targets Java 21.

To roll back during the opt-in period, [delete `AEM_JAVA_25_OPT_IN`](/help/implementing/cloud-manager/environment-variables.md#delete-env-variable) and save the configuration. When the environment update completes, the environment returns to its previous Java version. Repeat this procedure for each environment that you want to roll back.

## Environment variables - standard {#environment-variables}

Configure the build process based on information about the program or pipeline.

For instance, if JavaScript minification occurs at build time using a tool like gulp, different minification levels are preferred for various environments. A development build uses a lighter minification level compared to staging and production.

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

Your build process requires specific configuration variables that are not stored in the Git repository. Additionally, you need to adjust these variables between pipeline executions using the same branch.

See also [Configure Pipeline Variables](/help/implementing/cloud-manager/configuring-pipelines/pipeline-variables.md) for more information.

## Install additional system packages {#installing-additional-system-packages}

Some builds require additional system packages to function fully. For example, a build invokes a Python or Ruby script and must have an appropriate language interpreter installed. This installation process can be managed by calling the [`exec-maven-plugin`](https://www.mojohaus.org/exec-maven-plugin/) in your `pom.xml` to invoke APT. This execution is wrapped in a Cloud Manager-specific Maven profile. This example installs Python.

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
>Installing a system package in this manner does not install it in the runtime environment used for running Adobe Experience Manager. If you need a system package installed on the AEM environment, contact your Adobe representative.

>[!TIP]
>
>For details about the front-end build environment, see [Developing Sites with the Front-End Pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md).
