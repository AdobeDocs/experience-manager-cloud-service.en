---
title: Build Environment
description: Learn about Cloud Manager's build environment and how it builds and tests your code.
exl-id: a4e19c59-ef2c-4683-a1be-3ec6c0d2f435
solution: Experience Manager
feature: "Cloud Manager, Developing"
role: "Admin, Architect, Developer"
---

# Build Environment {#build-environment} 

Learn about Cloud Manager's build environment and how it builds and tests your code.

## Build Environment Details {#build-environment-details}

Cloud Manager builds and tests your code using a specialized build environment.

* The build environment is Linux-based, derived from Ubuntu 22.04.
* Apache Maven 3.9.4 is installed.
  * Adobe recommends users [update their Maven repositories to use HTTPS instead of HTTP.](#https-maven)
* The Java versions installed are Oracle JDK 11.0.22 and Oracle JDK 8u401.
* **IMPORTANT**: By default, the `JAVA_HOME` environment variable is set to `/usr/lib/jvm/jdk1.8.0_401` which contains Oracle JDK 8u401. *_This default should be overridden for AEM Cloud Projects to use JDK 11_*. See the [Setting the Maven JDK Version](#alternate-maven-jdk-version) section for more details.
* There are some additional system packages installed which are necessary.
  * `bzip2`
  * `unzip`
  * `libpng`
  * `imagemagick`
  * `graphicsmagick`
* Other packages may be installed at build time as described in the section [Installing Additional System Packages.](#installing-additional-system-packages)
* Every build is done on a pristine environment; the build container does not keep any state between executions.
* Maven is always run with the following three commands.
  * `mvn --batch-mode org.apache.maven.plugins:maven-dependency-plugin:3.1.2:resolve-plugins`
  * `mvn --batch-mode org.apache.maven.plugins:maven-clean-plugin:3.1.0:clean -Dmaven.clean.failOnError=false`
  * `mvn --batch-mode org.jacoco:jacoco-maven-plugin:prepare-agent package`
* Maven is configured at a system level with a `settings.xml` file, which automatically includes the public Adobe artifact repository using a profile named `adobe-public`. (See [Adobe Public Maven Repository](https://repo1.maven.org/) for more details).

>[!NOTE]
>
>Although Cloud Manager does not define a specific version of the `jacoco-maven-plugin`, the version used must be at least `0.7.5.201505241946`.

## HTTPS Maven Repositories {#https-maven}

Cloud Manager [release 2023.10.0](/help/implementing/cloud-manager/release-notes/2023/2023-10-0.md) began a rolling update to the build environment (completing with release 2023.12.0), which included an update to Maven 3.8.8. A significant change introduced in Maven 3.8.1 was a security enhancement aimed at mitigating potential vulnerabilities. Specifically, Maven now disables all insecure `http://*` mirrors by default, as outlined in the [Maven release notes.](http://maven.apache.org/docs/3.8.1/release-notes.html#cve-2021-26291)

As a result of this security enhancement, some users may face issues during the build step, particularly when downloading artifacts from Maven repositories that use insecure HTTP connections.

To ensure a smooth experience with the updated version, Adobe recommends that users update their Maven repositories to use HTTPS instead of HTTP. This adjustment aligns with the industry's growing shift towards secure communication protocols and helps maintain a secure and reliable build process.

### Using a Specific Java Version {#using-java-support}

By default, projects are built by the Cloud Manager build process using the Oracle 8 JDK, but AEM Cloud Service customers are strongly advised to set the JDK version used to execute Maven to `11`.

#### Setting the Maven JDK Version {#alternate-maven-jdk-version}

It is recommended to set the JDK version for the entire Maven execution to `11` in a `.cloudmanager/java-version` file.

To do this, create a file named `.cloudmanager/java-version` in the git repository branch used by the pipeline. Edit the file so that it contains only the text, `11`. While Cloud Manager also accepts a value of `8`, this version is no longer supported for AEM Cloud Service projects. Any other value is ignored. When `11` is specified, Oracle 11 is used and the `JAVA_HOME` environment variable is set to `/usr/lib/jvm/jdk-11.0.22`.

## Environment Variables {#environment-variables}

### Standard Environment Variables {#standard-environ-variables}

You may find it necessary to vary the build process based on information about the program or pipeline. 

For example, if build-time JavaScript minification is being done through a tool like gulp, there may be a desire to use a different minification level when building for a development environment as opposed to building for staging and production. 

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

### Pipeline Variables {#pipeline-variables}

Your build process may depend upon specific configuration variables which would be inappropriate to place in the git repository or you may need to vary them between pipeline executions using the same branch.

Please see the document [Configuring Pipeline Variables](/help/implementing/cloud-manager/configuring-pipelines/pipeline-variables.md) for more information

## Installing Additional System Packages {#installing-additional-system-packages}

Some builds require additional system packages to be installed to function fully. For example, a build may invoke a Python or Ruby script and must have an appropriate language interpreter installed. This can be done by calling the [`exec-maven-plugin`](https://www.mojohaus.org/exec-maven-plugin/) in your `pom.xml` to invoke APT. This execution should generally be wrapped in a Cloud Manager-specific Maven profile. This example installs Python.

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
