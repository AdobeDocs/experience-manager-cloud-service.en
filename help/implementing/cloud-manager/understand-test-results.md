---
title: Understand Test Results - Cloud Services
seo-title: Understand Test Results - Cloud Services
description: Understand Test Results - Cloud Services
seo-description: Understand Test Results - Cloud Services
---

# Understand Test Results - Cloud Services {#understand-test-results} 

Cloud Manager for Cloud Services pipeline executions will support execution of tests that run against the stage environment. This is in contrast to tests run during the Build and Unit Testing step which are run offline, without access to any running AEM environment. 
There are two types of tests run in this context:
* Customer-written tests 
* Adobe-written tests

 Both types of tests are run in a containerized infrastructure designed for running these types of tests.

 ## Writing Functional Tests {functional-tests}

 Customer-written functional tests must be packaged as a separate JAR file produced by the same Maven build as the artifacts to be deployed to AEM. Generally this would be a separate Maven module. The resulting JAR file must contain all required dependencies and would generally be created using the maven-assembly-plugin using the jar-with-dependencies descriptor. 

 In addition, the JAR must have the Cloud-Manager-TestType manifest header set to integration-test. In the future, it is expected that additional header values will be supported. An example configuration for the maven-assembly-plugin is:

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

 Within this JAR file, the class names of the actual tests to be executed must end in IT. 
 
 For example, a class named `com.myco.tests.aem.ExampleIT` would be executed but a class named `com.myco.tests.aem.ExampleTest` would not. 
 
 The test classes need to be normal JUnit tests. The test infrastructure is designed and configured to be compatible with the conventions used by the aem-testing-clients test library. Developers are strongly encouraged to use this library and follow its best practices.

## Custom Functional Testing {#custom-functional-test}

The Custom Functional testing step in the pipeline is always present and cannot be skipped. 

However, if no test JAR is produced by the build, the test passes by default. This step is current done immediately after the stage deployment.

> Note:
>The **Download Log** button allows access to a ZIP file containing the logs for the test execution detailed form. These logs do not include the logs of the actual AEM runtime process – those can be accessed using the regular Download or Tail Logs functionality described above.


## Local Test Execution {#local-test-execution}

As the test classes are JUnit tests, they can be run from mainstream Java IDEs like Eclipse, IntelliJ, NetBeans, and so on. 

However, when running these tests necessarily, it will be necessary to set a variety of system properties expected by the aem-testing-clients (and the underlying Sling Testing Clients). 

The system properties are as follows:

* `sling.it.instances - should be set to 2`
* `sling.it.instance.url.1 - should be set to the author URL, for example, http://localhost:4502`
* `sling.it.instance.runmode.1 - should be set to author`
* `sling.it.instance.adminUser.1 - should be set to the author admin user, e.g. admin`
* `sling.it.instance.adminPassword.1 - should be set to the author admin password`
* `sling.it.instance.url.2 - should be set to the author URL, for example, http://localhost:4503`
* `sling.it.instance.runmode.2 - should be set to publish`
* `sling.it.instance.adminUser.2 - should be set to the publish admin user, for example, admin`
* `sling.it.instance.adminPassword.2 - should be set to the publish admin password`