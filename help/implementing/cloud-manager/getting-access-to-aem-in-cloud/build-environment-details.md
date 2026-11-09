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

## Java support {#using-java-support}

### Java 25 support {#java-25-support}

Java 25 is the next long-term support (LTS) release after Java 21, delivering improvements across performance, developer productivity, and security:

* **Performance** — Reduced memory footprint, more efficient garbage collection, and faster JVM warm-up benefit cloud-native deployments.
* **Developer productivity** — Cleaner object initialization, more expressive pattern matching, and simplified concurrent task management reduce boilerplate and improve code clarity.
* **Security** — A modernized cryptographic key derivation API simplifies common security workflows.

Use the AEM Cloud Service SDK to validate your application locally, then [opt in to the Java 25 runtime](#java-25-runtime-opt-in) in your Cloud environments ahead of the automatic upgrade.

#### Runtime upgrade timeline {#java-25-runtime-upgrade-timeline}

Adobe is providing the following target dates to help you plan testing and validation ahead of the Java 25 runtime upgrade. Any changes to this timeline will be communicated through the [AEM as a Cloud Service release notes](/help/release-notes/release-notes-cloud/release-notes-current.md#java25-announcement).

| Timeframe | Milestone |
| --- | --- |
| **October 29, 2026** | AEM Cloud Service SDK supports Java 25 runtime. The Java 25 JDK is available for download from the Adobe Software Distribution portal. |
| **November 20, 2026** | Customers are encouraged to optionally enable the Java 25 runtime in their Cloud environments to validate behavior. Early adoption maximizes time to surface and resolve issues. |
| **January – April 2027** | Adobe will gradually migrate sandboxes and lower environments (RDE, Dev) to the Java 25 runtime. Customers should validate behavior and report unexpected issues, and are encouraged to enable staging and production environments as well. A temporary rollback to Java 21 is available while resolving any problems. |
| **May 2027** | All environment runtimes (including staging and production) migrate to Java 25. Java 21 runtime is decommissioned. The AEM Cloud Service SDK will no longer support Java 21. |

#### Java 25 runtime opt-in {#java-25-runtime-opt-in}

>[!IMPORTANT]
>
>The Java 25 runtime opt-in requires **AEM release 28386 or later**. Ensure that each environment meets this requirement and review the [runtime requirements](#runtime-requirements) before enabling the opt-in.

Choose one of the following options to enable the Java 25 runtime:

* **Environment variable:** Preferred for quick tests or when changing the build-time JVM is not an option. This enables the Java 25 runtime without changing your build JDK.
* **Build-time Java version:** Use this option when you want to use Java 25 language features. Building with Java 25 also opts the target environment into the Java 25 runtime.

##### Enable Java 25 with an environment variable {#java-25-runtime-env-var}

1. In Cloud Manager, select the environment that you want to enable.
1. [Add an environment variable](/help/implementing/cloud-manager/environment-variables.md#add-variables) with the following configuration:

   | Field | Value |
   | --- | --- |
   | **Name** | `AEM_JAVA_25_OPT_IN` |
   | **Value** | `true` (lowercase) |
   | **Step Applied** | **All** |
   | **Type** | **Normal** (not a secret) |

1. Save the configuration and wait for the environment update to complete.
1. Validate your application's behavior in the updated environment.

>[!NOTE]
>
>With this option, set the variable in each environment that you want to enable. **Stage and production environments must be enabled separately**, even if they use the same production pipeline.

##### Enable Java 25 through the build JDK {#java-25-runtime-build-jdk}

You do not need to set `AEM_JAVA_25_OPT_IN` for this option.

1. Review the [build requirements](#build-time-reqs) and [build and runtime compatibility](#java-build-runtime-compatibility).
1. Set `.cloudmanager/java-version` to `25` in the repository branch used by your Cloud Manager pipeline. See [Set the Maven JDK version](#alternate-maven-jdk-version).
1. Configure your development pipeline to use this branch, then run it to build and deploy your application.
1. Follow the [validation procedure](#validate-your-application) before applying the same change to stage and production.

##### Roll back the environment-variable opt-in {#java-25-runtime-rollback}

This procedure applies only to an environment opted in through the environment variable. Deleting the variable does not undo an opt-in caused by building with Java 25.

Before rolling back, ensure that the deployed application and its dependencies are compatible with the previous Java version. See [Build and runtime compatibility](#java-build-runtime-compatibility).

To roll back during the opt-in period, [delete `AEM_JAVA_25_OPT_IN`](/help/implementing/cloud-manager/environment-variables.md#delete-env-variable) and save the configuration. When the environment update completes, the environment returns to its previous Java version. Repeat this procedure for each environment that you want to roll back.

### Set the Maven JDK version {#alternate-maven-jdk-version}

Adobe recommends Java 25 for building AEM Cloud Service projects. Java 21, 17, and 11 are also supported.

To set the Maven execution JDK, create a file named `.cloudmanager/java-version` in the Git repository branch used by the pipeline. The file must contain only the major version number: `25`, `21`, `17`, or `11`. Cloud Manager uses the corresponding Oracle JDK. Although Cloud Manager also accepts `8`, this version is no longer supported for AEM Cloud Service projects. Other values are ignored.

Building with JDK 25 also opts the target environment into the Java 25 runtime. For a runtime-only test, use the [environment-variable option](#java-25-runtime-env-var) instead.

#### Build and runtime compatibility {#java-build-runtime-compatibility}

The `.cloudmanager/java-version` file selects the JDK that runs Maven. It does not set the Java release targeted by the compiler.

If your application must remain compatible with Java 21, configure the Maven Compiler Plugin to target Java 21, for example by setting `maven.compiler.release` to `21`. Your dependencies must also support Java 21. Building with JDK 25 still opts the target environment into the Java 25 runtime, even when the compiler targets Java 21.

To use Java 25 language features and APIs, configure the compiler to target Java 25. The resulting code cannot run on Java 21. Before reverting to Java 21, redeploy an application version and dependencies that are compatible with Java 21.

### Prepare your application {#prereq-for-building}

Before changing your build or runtime Java version, review the [build requirements](#build-time-reqs) and [runtime requirements](#runtime-requirements), then validate your application as described below.

#### Validate your application {#validate-your-application}

1. Download the latest [AEM Cloud Service SDK](https://experience.adobe.com/#/downloads), run it with your intended runtime Java version, and deploy your application. Validate its functionality and check the logs for class-loading or bytecode-weaving errors.
1. Apply your chosen Java settings in development. For Java 25, follow your selected [opt-in option](#java-25-runtime-opt-in). For other build JDK changes, configure the [Maven JDK](#alternate-maven-jdk-version) in the branch used by your development pipeline.
1. For a build JDK change, ensure that the development pipeline passes code-quality checks and tests. For a runtime-only change, wait for the environment update to complete; rebuilding the application is not required. Validate the application's functionality in the updated environment.
1. After successful validation in development, apply the same change to stage and validate the application there.
1. After successful validation in stage, apply the validated change to production.

### Build requirements {#build-time-reqs}

#### Java 25 builds {#java-25-build-requirements}

Java 25 build requirements are additive to the [Java 17 and Java 21 requirements](#java-17-21-build-requirements) below. In addition to those requirements, use [JaCoCo 0.8.14 or later](https://www.jacoco.org/jacoco/trunk/doc/changes.html) and update build plugins that inspect or transform bytecode to releases that support Java 25. Validate the complete Cloud Manager pipeline, not just local compilation.

#### Java 17 and Java 21 builds {#java-17-21-build-requirements}

The following minimum plugin versions are the baseline for Java 17 and Java 21 builds and also apply to Java 25 builds. Java 25 can require newer plugin versions, so meeting these minimums alone does not guarantee Java 25 compatibility.

| Plugin | Minimum version |
| --- | --- |
| `bnd-maven-plugin` | 6.4.0 |
| `aemanalyser-maven-plugin` | 1.6.16 |
| `maven-bundle-plugin` | 5.1.5 |

If the project must also build with Java 11, keep `bnd-maven-plugin` below version 7 and `maven-bundle-plugin` below version 6. Those newer plugin versions require a build JDK later than Java 11.

Cloud Manager uses SonarQube 9.9 for builds with Java 17 or Java 21. No customer action is required to upgrade SonarQube. For details about that upgrade, see the [Release Notes for Cloud Manager 2025.1.0](/help/implementing/cloud-manager/release-notes/2025/2025-1-0.md).

#### Projects using `maven-scr-plugin` {#maven-scr-plugin}

If your project uses `maven-scr-plugin`, override its ASM dependency to support newer Java versions. The following example uses [ASM 9.8](https://asm.ow2.io/versions.html), which supports Java 25.

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

### Java 25 runtime requirements {#runtime-requirements}

Review libraries bundled with your application that inspect, generate, or transform bytecode. Older versions can fail on the Java 25 runtime even if your own code targets an earlier Java release. Check both direct and transitive dependencies, including libraries embedded in third-party bundles such as the AEM Groovy Console.

If your application includes the following libraries, update them to versions with Java 25 bytecode support before opting in:

| Library | Version with Java 25 bytecode support |
| --- | --- |
| ASM (`org.objectweb.asm`, typically supplied by `org.ow2.asm.*` artifacts) | [9.8 or later](https://asm.ow2.io/versions.html) |
| Groovy (`org.apache.groovy` artifacts) | [4.0.27 or later in the 4.0 release line](https://groovy-lang.org/changelogs/changelog-4.0.27.html) |
| Aries SPI Fly (`org.apache.aries.spifly.dynamic.bundle`) | [1.3.8 or later](https://aries.apache.org/documentation/modules/spi-fly.html) |

Keep related ASM artifacts at the same version and honor the dependency versions required by libraries such as SPI Fly. These versions address bytecode support; follow the [validation procedure](#validate-your-application) to check the complete application and third-party bundles.

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
