---
title: Functional Testing
description: Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment process to ensure quality and reliability of your code.
exl-id: 7eb50225-e638-4c05-a755-4647a00d8357
---

# Functional Testing {#functional-testing}

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_functionaltesting"
>title="Functional Testing"
>abstract="Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment process to ensure quality and reliability of your code."

Learn about the three different types of functional testing built into the [AEM as a Cloud Service deployment process](/help/implementing/cloud-manager/deploy-code.md) to ensure quality and reliability of your code.

## Overview {#overview}

There are three different types of functional testing in AEM as a Cloud Service.

* [Product Functional Testing](#product-functional-testing)
* [Custom Functional Testing](#custom-functional-testing)
* [Custom UI Testing](#custom-ui-testing)

For all functional tests, the detailed results of the tests can be downloaded as a `.zip` file by using the **Download build log** button in the build overview screen as part of the [deployment process.](/help/implementing/cloud-manager/deploy-code.md)

These logs do not include the logs of the actual AEM runtime process. To access those logs, please refer to the document [Accessing and Managing Logs](/help/implementing/cloud-manager/manage-logs.md) for more details.

Both the product functional tests and sample custom functional tests are based on the [AEM Testing Clients.](https://github.com/adobe/aem-testing-clients)

### Product Functional Testing {#product-functional-testing}

Product functional tests are a set of stable HTTP integration tests (ITs) of core functionality in AEM such as authoring and replication tasks. These tests are maintained by Adobe and are intended to prevent  changes to custom application code from being deployed if it breaks core functionality.

* [Production Pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md): Product functional tests run automatically whenever you deploy new code to Cloud Manager and cannot be skipped.
* [Non-Production Pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md): Product functional tests can be optionally selected to run whenever you execute your non-production pipeline.

Product functional tests are maintained as an open-source project. Please refer to [product functional tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke) in GitHub for details.

### Custom Functional Testing {#custom-functional-testing}

While product functional testing is defined by Adobe, you can write your own quality testing for your own application. This will be executed as custom functional testing as part of the [production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) or optionally [non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md) to ensure the quality of your application.

Custom functional testing is executed both for custom code deployments as well as push upgrades, which makes it especially important to write good functional tests which prevent AEM code changes from breaking your application code. The custom functional testing step is always present and cannot be skipped.

### Custom UI Testing {#custom-ui-testing}

Custom UI testing is an optional feature that enables you to create and automatically run UI tests for your applications. UI tests are Selenium-based tests packaged in a Docker image in order to allow for a wide choice of language and frameworks such as Java and Maven, Node and WebDriver.io, or any other framework and technology built upon Selenium.

Please refer to the document [Custom UI Testing](/help/implementing/cloud-manager/ui-testing.md#custom-ui-testing) for more information.

## Getting Started with Functional Tests {#getting-started-functional-tests}

Upon creation of a new code repository in Cloud Manager, an `it.tests` folder is automatically created with sample test cases.

>[!NOTE]
>
>If your repository was created before Cloud Manager automatically created `it.tests` folders, you may also generate the latest version using the [AEM Project Archetype.](https://github.com/adobe/aem-project-archetype/tree/master/src/main/archetype/it.tests)

Once you have the contents of the `it.tests` folder, you can use it as a basis for your own tests and then:

1. [Develop your test cases.](#writing-functional-tests)
1. [Run the tests locally.](#local-test-execution)
1. Commit your code into the Cloud Manager repository and execute a Cloud Manager pipeline.

## Writing Custom Functional Tests {#writing-functional-tests}

The same tools that Adobe uses to write product functional tests can be used to write your custom functional tests. Use the [product functional tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke) in GitHub as an example of how to write your tests.

The code for custom functional test is Java code located in the `it.tests` folder of your project. It should produce a single JAR with all the functional tests. If the build produces more than one test JAR, which JAR is selected is non-deterministic. If it produces zero test JARs, the test step passes by default. [See the AEM Project Archetype](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/it.tests) for sample tests.

The tests are executed on Adobe-maintained testing infrastructure including at least two author instances, two publish instances, and a dispatcher configuration. This means that your custom functional tests run against the entire AEM stack.

### Functional Tests Structure {#functional-tests-structure}

 Custom functional tests must be packaged as a separate JAR file produced by the same Maven build as the artifacts to be deployed to AEM. Generally this would be a separate Maven module. The resulting JAR file must contain all required dependencies and would generally be created using the `maven-assembly-plugin` using the `jar-with-dependencies` descriptor.

In addition, the JAR must have the `Cloud-Manager-TestType` manifest header set to `integration-test`.

The following is an example configuration for the `maven-assembly-plugin`.

```java
<build>
    <plugins>
        <!-- Create self-contained jar with dependencies -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-assembly-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <descriptorRefs>
                    <descriptorRef>jar-with-dependencies</descriptorRef>
                </descriptorRefs>
                <archive>
                    <manifestEntries>
                        <Cloud-Manager-TestType>integration-test</Cloud-Manager-TestType>
                    </manifestEntries>
                </archive>
            </configuration>
            <executions>
                <execution>
                    <id>make-assembly</id>
                    <phase>package</phase>
                    <goals>
                        <goal>single</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
```

Within this JAR file, the class names of the actual tests to be executed must end in `IT`.

For example, a class named `com.myco.tests.aem.it.ExampleIT` would be executed, but a class named `com.myco.tests.aem.it.ExampleTest` would not.

Furthermore, to exclude test code from the coverage check of the code scanning, the test code must be below a package named `it` (the coverage exclusion filter is `**/it/**/*.java`).

The test classes need to be normal JUnit tests. The test infrastructure is designed and configured to be compatible with the conventions used by the `aem-testing-clients` test library. Developers are strongly encouraged to use this library and follow its best practices.

Please refer to the [`aem-testing-clients` GitHub repo](https://github.com/adobe/aem-testing-clients) for more details.

>[!TIP]
>
>[Watch this video](https://www.youtube.com/watch?v=yJX6r3xRLHU) about how you can use custom functional tests to improve your confidence in your CI/CD pipelines.

### Local Test Execution {#local-test-execution}

Before activating functional tests in a Cloud Manager pipeline, it's recommended to run the functional tests locally using the [AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md) or an actual AEM as a Cloud Service instance.

#### Prerequisites {#prerequisites}

The tests in Cloud Manager will be executed using a technical admin user.

For running the functional tests from your local machine, create a user with admin-like permissions to achieve the same behavior.

#### Running in an IDE {#running-in-an-ide}

Because test classes are JUnit tests, they can be run from mainstream Java IDEs like Eclipse, IntelliJ, and NetBeans. Because both product functional tests and custom functional tests are based on the same technology, both can be run locally by copying the product tests into your custom tests.

However, when running these tests, it will be necessary to set a variety of system properties expected by the `aem-testing-clients` (and the underlying Sling Testing Clients) library.

The system properties are as follows.

* `sling.it.instances - should be set to 2`
* `sling.it.instance.url.1 - should be set to the author URL, for example, http://localhost:4502`
* `sling.it.instance.runmode.1 - should be set to author`
* `sling.it.instance.adminUser.1 - should be set to the author admin user, for example, admin`
* `sling.it.instance.adminPassword.1 - should be set to the author admin password`
* `sling.it.instance.url.2 - should be set to the publish URL, for example, http://localhost:4503`
* `sling.it.instance.runmode.2 - should be set to publish`
* `sling.it.instance.adminUser.2 - should be set to the publish admin user, for example, admin`
* `sling.it.instance.adminPassword.2 - should be set to the publish admin password`

#### Running All Tests Using Maven {#using-maven}

1. Open a shell and navigate to the `it.tests` folder in your repository.

1. Execute the following command providing the necessary paremters to start the tests using Maven.

```shell
mvn verify -Plocal \
    -Dit.author.url=https://author-<program-id>-<environment-id>.adobeaemcloud.com \
    -Dit.author.user=<user> \
    -Dit.author.password=<password> \
    -Dit.publish.url=https://publish-<program-id>-<environment-id>.adobeaemcloud.com \
    -Dit.publish.user=<user> \
    -Dit.publish.password=<password>
```
