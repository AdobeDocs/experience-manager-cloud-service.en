---
title: Java &trade; Functional Tests
description: Learn how to write Java &trade; functional tests for AEM as a Cloud Service
exl-id: e014b8ad-ac9f-446c-bee8-adf05a6b4d70
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Java&trade; Functional Testing

Learn how to write Java&trade; functional tests for AEM as a Cloud Service

## Getting Started with Functional Tests {#getting-started-functional-tests}

Upon creation of a new code repository in Cloud Manager, an `it.tests` folder is automatically created with sample test cases.

>[!NOTE]
>
>If your repository was created before Cloud Manager automatically created `it.tests` folders, you may also generate the latest version using the [AEM Project Archetype](https://github.com/adobe/aem-project-archetype/tree/master/src/main/archetype/it.tests).

Once you have the contents of the `it.tests` folder, you can use it as a basis for your own tests and then:

1. [Develop your test cases](#writing-functional-tests).
1. [Run the tests locally](#local-test-execution).
1. Commit your code into the Cloud Manager repository and execute a Cloud Manager pipeline.

## Writing Custom Functional Tests {#writing-functional-tests}

The same tools that Adobe uses to write product functional tests can be used to write your custom functional tests. Use the [product functional tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke) in GitHub as an example of how to write your tests.

The code for custom functional test is Java&trade; code in the `it.tests` folder of your project. It should produce a single JAR with all the functional tests. If the build produces more than one test JAR, which JAR is selected is non-deterministic. If it produces zero test JARs, the test step passes by default. See [AEM Project Archetype](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/it.tests) for sample tests.

The tests are run on Adobe-maintained testing infrastructure including at least two author instances, two publish instances, and a Dispatcher configuration. This setup means that your custom functional tests run against the entire AEM stack.

### Functional Tests Structure {#functional-tests-structure}

 Custom functional tests must be packaged as a separate JAR file produced by the same Maven build as the artifacts to be deployed to AEM. Generally, this build would be a separate Maven module. The resulting JAR file must contain all required dependencies and would generally be created using the `maven-assembly-plugin` using the `jar-with-dependencies` descriptor.

In addition, the JAR must have the `Cloud-Manager-TestType` manifest header set to `integration-test`.

The following is an example configuration for the `maven-assembly-plugin`.

```XML
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
</build>
```

Within this JAR file, the class names of the actual tests to be executed must end in `IT`.

For example, a class named `com.myco.tests.aem.it.ExampleIT` would be executed, but a class named `com.myco.tests.aem.it.ExampleTest` would not.

Furthermore, to exclude test code from the coverage check of the code scanning, the test code must be below a package named `it` (the coverage exclusion filter is `**/it/**/*.java`).

The test classes must be normal JUnit tests. The test infrastructure is designed and configured to be compatible with the conventions used by the `aem-testing-clients` test library. Developers are encouraged to use this library and follow its best practices.

See [`aem-testing-clients` GitHub repo](https://github.com/adobe/aem-testing-clients) for more details.

>[!TIP]
>
>[Watch this video](https://www.youtube.com/watch?v=yJX6r3xRLHU) about how you can use custom functional tests to improve your confidence in your CI/CD pipelines.

### Prerequisites {#prerequisites}

1. The tests in Cloud Manager are run using a technical admin user.

>[!NOTE]
>
>For running the functional tests from your local machine, create a user with admin-like permissions to achieve the same behavior.

1. The containerized infrastructure that is scoped for functional testing is limited by the following boundaries:


| Type                 | Value | Description                                                        |
|----------------------|-------|--------------------------------------------------------------------|
| CPU                  | 0.5   | Amount of CPU-time reserved per test execution                     |
| Memory               | 0.5 Gi | Amount of memory allocated to the test, value in gibibytes        |
| Timeout              | 30 m   | The time limit after which the test is stopped.                |
| Recommended Duration | 15 m   | Adobe recommends writing the tests not to take longer than this time. |

>[!NOTE]
>
> Should you need more resources, create a Customer Care case, and describe your use-case. Adobe's team reviews your request and provides appropriate assistance.

#### Dependencies

* aem-cloud-testing-clients:

Upcoming changes to the containerized infrastructure for executing functional tests require updating the [aem-cloud-testing-clients](https://github.com/adobe/aem-testing-clients) library in your custom functional tests to version **1.2.1** or higher. Ensure that the dependency in your `it.tests/pom.xml` file is updated accordingly.

```
<dependency>
   <groupId>com.adobe.cq</groupId>
   <artifactId>aem-cloud-testing-clients</artifactId>
   <version>1.2.1</version>
</dependency>
```

>[!NOTE]
>
>This change needs to be performed before April 6, 2024. 
>Failing to update the dependency library can result in pipeline failures at the "Custom Functional Testing" step.

### Local Test Execution {#local-test-execution}

Before activating functional tests in a Cloud Manager pipeline, it's recommended to run the functional tests locally using the [AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md) or an actual AEM as a Cloud Service instance.

#### Running in an IDE {#running-in-an-ide}

Because test classes are JUnit tests, they can be run from mainstream Java &trade; IDEs like Eclipse, IntelliJ, and NetBeans. Because both product functional tests and custom functional tests are based on the same technology, both can be run locally by copying the product tests into your custom tests.

However, when running these tests, it is necessary to set various system properties expected by the `aem-testing-clients` (and the underlying Sling Testing Clients) library.

The system properties are as follows.

| Property                            | Description                                                      | Example                 |
|-------------------------------------|------------------------------------------------------------------|-------------------------|
| `sling.it.instances`                | Number of instances, to match cloud service should be set to `2`. | `2`                     |
| `sling.it.instance.url.1`           | Set to author URL.                                  | `http://localhost:4502` | 
| `sling.it.instance.runmode.1`       | Run mode of the first instance. Set to `author`.         | `author`                | 
| `sling.it.instance.adminUser.1`     | Set to author admin user.                          | `admin`                 | 
| `sling.it.instance.adminPassword.1` | Set to author admin password.                      |                         | 
| `sling.it.instance.url.2`           | set to publish URL.                                 | `http://localhost:4503` |
| `sling.it.instance.runmode.2`       | Run mode of the second instance. Set to `publish`.       | `publish`            | 
| `sling.it.instance.adminUser.2`     | Set to publish admin user.                         | `admin`                 | 
| `sling.it.instance.adminPassword.2` | Set to publish admin password.                     |                         | 



#### Running All Tests Using Maven {#using-maven}

1. Open a shell and navigate to the `it.tests` folder in your repository.

1. Execute the following command providing the necessary parameters to start the tests using Maven.

```shell
mvn verify -Plocal \
    -Dit.author.url=https://author-<program-id>-<environment-id>.adobeaemcloud.com \
    -Dit.author.user=<user> \
    -Dit.author.password=<password> \
    -Dit.publish.url=https://publish-<program-id>-<environment-id>.adobeaemcloud.com \
    -Dit.publish.user=<user> \
    -Dit.publish.password=<password>
```

